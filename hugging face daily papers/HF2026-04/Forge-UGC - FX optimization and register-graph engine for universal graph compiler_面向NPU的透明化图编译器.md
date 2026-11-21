# HuggingFace最新推荐论文 ｜Forge-UGC: FX optimization and register-graph engine for universal graph compiler ｜面向NPU的透明化图编译器

论文原文见 [arXiv](https://arxiv.org/abs/2604.16498)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16498)

> 异构边缘设备中，NPU与CPU协同执行Transformer模型时，现有部署框架因中间格式导出丢失现代算子语义、编译时间随模型深度超线性增长，且缺乏对NPU受限内存层级的显式管理，导致推理延迟与能耗无法优化。FORGE-UGC通过直接操作PyTorch FX图，构建了包含六类可组合优化通道、类型化中间表示及基于活性分析的缓冲分配机制的纯Python编译栈，绕过了MLIR C++后端依赖。该方案在Intel AI Boost NPU上验证了编译加速与推理降延迟的有效性，但其“通用编译器”定位与仅验证单一硬件后端的事实存在张力，跨架构泛化能力尚待实证。

## 研究背景

边缘智能体推理管线需在单一SoC内协调NPU密集张量运算、GPU灵活并行计算与CPU不规则控制流，系统性能瓶颈已从单体加速器算力转移至跨设备数据搬运与调度效率。NPU虽提供高能效比，但其共享LPDDR5内存层级与PCIe/MMIO设备转换开销（每次约0.3–0.8ms）要求编译器具备显式的缓冲管理与指令调度能力，而传统部署框架将编译过程视为黑盒，无法暴露这些底层决策。

主流编译路线面临双重困境：基于MLIR的IREE与Hexagon-MLIR虽提供模块化IR基础设施，但自定义优化通道必须实现为C++ OperationPass子类，且IREE缺乏Intel NPU后端，导致针对NPU特定SRAM约束的活性分析无法在通用后端中实现；OpenVINO与ONNX Runtime虽支持NPU部署，但依赖TorchScript或ONNX等损失性导出格式，无法原生表示RoPE、GQA等现代LLM构造，且编译时间随模型层数呈超线性增长（8B参数模型达58–62秒）。FORGE-UGC的切入点在于利用torch.export在ATen算子层捕获FX图，以纯Python实现优化通道与NPU专用后端，将编译栈从“黑盒导出-转换”重构为“透明图操作-硬件感知调度”。

## 核心方法

### 方法参照系

本文问题归属于编译器基础设施类别，标准流程为前端捕获、中间优化、后端生成。关键差异在于：主流方案（如TVM、IREE）依赖C++实现的MLIR通道进行中间优化，而本文针对NPU后端缺失与C++迭代效率低的问题，将中间端完全迁移至PyTorch FX Python原生图操作，并新增NPU专用的类型化IR与缓冲分配层。

### 基于FX图的无损捕获与可组合优化

针对OpenVINO/ONNX Runtime因中间格式导出导致的算子覆盖缺口，本文在Phase 1直接使用torch.export.export()在ATen算子层捕获计算图，原生支持tied weights与静态边界内的动态形状。Phase 2实施六类独立可测量的优化通道：死代码消除（DCE）、公共子表达式消除（CSE）、常量折叠、注意力融合、算子融合与布局优化。注意力融合通过模式匹配分解的多头注意力子图并替换为单一融合调度，其节点减少量与模型深度正相关。该设计解决了现有框架无法对现代LLM构造进行无损编译的问题，使GPT-2至Llama-3.1-8B的图节点平均减少18.8%，且每个通道通过CompilationResult结构报告执行时间与节点增量，支持原则性消融研究。

### 类型化NPUIR与活性引导的缓冲分配

针对NPU受限SRAM层级导致的CPU-NPU设备转换开销，本文在Phase 3将优化后的FX图降低为类型化中间表示（NPUIR），为每条指令分配操作码、类型化虚拟寄存器、设备放置（NPU/CPU）及预解析可调用对象。Phase 4执行线性扫描缓冲分配与指令调度，其核心目标函数为最小化设备转换次数：

$$
\min_{\pi} \sum_{i=1}^{N} \mathbb{1}[\text{device}(op_i) \neq \text{device}(op_{i+1})]
$$

其中 $\pi$ 为指令调度序列，$\mathbb{1}[\cdot]$ 为指示函数。该调度基于活性分析识别可重叠的活跃区间，将连续NPU可执行操作聚类为单一调度批次。此机制解决了现有框架在EP级别进行内存规划时缺乏用户可见性与NPU特定活性推理的问题，使Llama-3.1-8B的设备转换次数从264降至93，消除了约50–130ms的每次推理开销。

## 实验评估

实验在WikiText-103与GLUE基准上评估六个模型家族（125M–8B参数），基线为OpenVINO与ONNX Runtime。基线覆盖审计显示，对比方法均为工业界标准部署框架，但缺失Torch Inductor（NPU实验性后端）与IREE（若存在NPU后端）等学术/工业混合基线，可能高估相对优势。

| 模型 | FORGE-UGC Mean (ms) | OpenVINO Mean (ms) | ONNX RT Mean (ms) | Δ vs. Best Baseline |
|---|---|---|---|---|
| GPT-2 (125M) | 6.82 | 8.45 | 9.13 | −19.3% |
| Llama-3.1-8B | 62.48 | 91.37 | 97.82 | −31.6% |

FORGE-UGC在所有模型上实现最低平均延迟，且优势随模型规模扩大：从GPT-2的19.3%提升至Llama-3.1-8B的31.6%（对比最佳基线）。编译时间方面，FORGE-UGC在Llama-3.1-8B上为6.7秒，而OpenVINO/ONNX Runtime为58.4–62.2秒，加速比达6.9–9.2倍。

| 消融项 (GPT-2) | Cost Model Score | Δ% |
|---|---|---|
| w/o Attention Fusion | 238.34 | +2,658% |
| w/o Operator Fusion | 8.84 | +2.3% |
| w/o DCE | 8.69 | +0.6% |

注意力融合移除导致成本模型分数激增27.6倍，确认为最关键优化；算子融合贡献2.3%改进；DCE/CSE/常量折叠在GPT-2上影响微小，因追踪图含较少死节点，但对更大模型必要。数值保真度方面，fp16模型max-abs logit差异低于 $1.2 \times 10^{-5}$，Llama-3.1-8B因int8权重量化达 $2.1 \times 10^{-5}$，KL散度低于 $8.4 \times 10^{-9}$，证实优化通道未引入显著数值误差。

评估边界方面，论文未报告置信区间，仅给出CV < 2.5%的可复现性指标；能耗节省（30.2–40.9%）高于延迟节省（18.2–35.7%），归因于设备转换减少降低平均功耗；P99/P50比值稳定在1.20，优于基线的1.27–1.28，反映确定性调度的尾部稳定性。代码未公开，超参数（如成本模型权重 $w_1$–$w_5$）未详细披露，限制了独立复现。

## 关联研究分析

从方法设计看，FORGE-UGC与Hexagon-MLIR同属NPU专用编译栈，但技术路线根本不同：Hexagon-MLIR基于MLIR构建显式空间时间结构IR，通过C++通道实现融合与协程代码生成，面向Qualcomm Hexagon的HVX/TCM指令；FORGE-UGC则放弃MLIR，采用PyTorch FX Python图操作，将硬件特定逻辑隔离在可插拔后端模块中。这一差异源于任务特性：Intel AI Boost NPU的NNFactory调度模型与IREE通用后端不兼容，且C++通道迭代效率低，迫使作者选择Python原生方案。然而，Python FX在表达复杂空间并行与细粒度内存层级方面是否具备MLIR的表达能力，论文未提供跨硬件对比实验，仅声称“架构上硬件无关”，但实际验证仅限于Intel NPU。

从问题动机看，FORGE-UGC与Torch Inductor同基于FX图操作，但目标硬件与优化焦点不同：Inductor针对GPU/CPU生成Triton/C++内核，优化粒度为循环级与Tile级；FORGE-UGC针对NPU，优化焦点为设备转换最小化与缓冲分配，不涉及内核生成。Inductor的Triton后端已证明Tile抽象在GPU上的有效性，但NPU的SRAM约束与PCIe瓶颈要求更粗粒度的调度决策，这正是FORGE-UGC引入NPUIR与线性扫描分配的原因。两者在“通用调度”与“硬件特定优化”间的取舍不同：Inductor追求跨GPU/CPU的通用性，FORGE-UGC牺牲部分底层自由度换取NPU部署的透明性与可调试性。

## 总结

FORGE-UGC解决的核心矛盾是NPU部署中现有框架的损失性导出、超线性编译时间与缺乏显式缓冲管理问题。其切入点在于利用torch.export在ATen层捕获FX图，以纯Python实现优化通道与NPU专用后端，绕过了MLIR C++依赖与IREE后端缺失的限制。方法上，通过六类可组合优化通道、类型化NPUIR与活性引导的线性扫描分配，实现了编译加速6.9–9.2倍与推理延迟降低18.2–35.7%。边界在于：仅验证Intel AI Boost NPU单一后端，未提供跨NPU架构（如AMD XDNA、Apple ANE）的对比实验；成本模型为启发式加权求和，未校准至实际墙钟时间；当前原型仅支持单批次推理，缺乏动态形状与批处理支持。当扩展至其他NPU架构时，Python FX图操作能否保持与MLIR相当的空间并行表达能力与调度精度，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16498)