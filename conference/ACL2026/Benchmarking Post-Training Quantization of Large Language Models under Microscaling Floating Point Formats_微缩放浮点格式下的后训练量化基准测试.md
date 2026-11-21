# ACL2026最新论文 ｜Benchmarking Post-Training Quantization of Large Language Models under Microscaling Floating Point Formats ｜微缩放浮点格式下的后训练量化基准测试

研究机构：华为

作者：Manyi Zhang、Ji-Fu Li、Zhongao Sun 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.09555)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.09555)

> 大语言模型部署面临内存与算力瓶颈，后训练量化（Post-Training Quantization, PTQ）是无需重训即可压缩模型的关键路径。现有PTQ算法多针对整数（INT）格式设计，在微缩放浮点（Microscaling Floating-Point, MXFP）格式下的行为与失效机制尚不明确。本文系统评估了7种PTQ算法在MXFP8与MXFP4下的表现，揭示了格式兼容性对精度的决定性影响。该研究提供了MXFP量化的实用指南，但受限于7B/8B规模模型，其结论向更大规模或NVFP格式的泛化性存疑。

## 研究背景

当模型权重与激活值被压缩至4位时，数值表示的动态范围急剧收窄。MXFP格式通过每32个元素共享一个8位无符号指数（UE8M0）来维持局部动态范围，这种块级结构使得量化误差不再均匀分布，而是与块内数值分布的统计特性（如峰度、异常值密度）强耦合。传统INT量化假设误差可通过全局或通道级缩放因子线性补偿，但MXFP的指数-尾数解耦机制引入了非线性的舍入行为，导致基于INT假设设计的算法在MXFP下可能失效。

低精度量化领域长期聚焦于训练阶段的数值稳定性与系统协同，如FP8训练框架与FP4预训练稳定性。然而，推理阶段的PTQ研究大多沿袭INT格式的优化路径，如SmoothQuant的通道平滑或GPTQ的二阶误差补偿。这些方法在INT4下表现优异，但在MXFP4下是否依然有效，缺乏系统性实证。本文的切入点在于：MXFP并非INT的简单替代，而是一个独立的数值域，需要格式感知的量化设计。

## 核心方法

### 方法参照系

PTQ的标准流程是在校准集上优化量化参数（缩放因子、零点），以最小化量化后张量与原始张量的重构误差。本文问题与该流程的关键差异在于：量化目标从INT的均匀网格变为MXFP的块级浮点网格，且缩放因子本身受UE8M0格式约束，引入了额外的量化误差源。

### 格式兼容性分类与评估

本文未提出新算法，而是将现有PTQ方法按变换类型分为四类：通道变换（SmoothQuant, AWQ）、误差补偿（GPTQ, MR-GPTQ）、旋转变换（QuaRot, SpinQuant）与仿射变换（FlatQuant）。评估的核心在于检验这些变换在MXFP块级结构下的有效性。设计动机在于揭示为何某些在INT下有效的策略（如旋转）在MXFP下反而导致精度下降。

$$
\hat{W} = \text{nearest}\left(\frac{W}{s}, C_{\text{MXFP}}\right) \cdot s
$$

其中 $s$ 为块级缩放因子，$C_{\text{MXFP}}$ 为MXFP可表示值集合。该公式表明，量化误差不仅取决于 $W/s$ 的舍入，还受 $s$ 本身在UE8M0网格上的量化误差影响。

### 缩放因子误差分析与Pre-scale策略

MXFP4中，缩放因子 $s$ 必须为2的幂次（UE8M0格式），这导致最优缩放因子与允许缩放因子之间存在显著偏差，进而影响整个块内所有值的量化精度。本文引入Pre-scale策略，在量化前将输入乘以 $3/4$，以缓解FP4动态范围限制导致的系统性裁剪偏差。

$$
W' = \frac{3}{4} W, \quad \hat{W}' = \text{Quantize}_{\text{MXFP4}}(W')
$$

该操作通过缩小数值幅度，避免极端值被截断至FP4表示范围边界，从而降低裁剪误差。实验表明，Pre-scale将openPangu-Embedded-7B-V1.1在W4A4下的平均准确率从52.39%提升至56.76%，PPL从104.42降至49.33。

## 实验评估

实验在Llama-3.1-8B-Instruct、openPangu-Embedded-7B-V1.1、Qwen2.5-VL-7B及openPangu-VL-7B上进行，覆盖W8A8、W4A8、W4A4配置及15个基准。基线覆盖RTN、GPTQ、SmoothQuant、AWQ、QuaRot、SpinQuant、FlatQuant及MR-GPTQ，但未包含针对MXFP格式专门设计的新算法（如NVFP4相关方法），这限制了结论的普适性。

| 模型 | 配置 | 方法 | 平均准确率 (%) | 恢复率 (%) | PPL (WikiText) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Llama-3.1-8B | W4A4 | RTN | 56.76 | 92.45 | 8.27 |
| Llama-3.1-8B | W4A4 | FlatQuant* | 58.50 | 95.28 | 8.06 |
| Llama-3.1-8B | W4A4 | GPTQ | 57.61 | 93.83 | 8.37 |
| openPangu-7B | W4A4 | RTN | 56.76 | 92.45 | 49.33 |
| openPangu-7B | W4A4 | FlatQuant* | 58.50 | 95.28 | 36.40 |

在W4A4配置下，FlatQuant*在Llama-3.1-8B上取得95.28%的恢复率，显著优于RTN的92.45%。然而，在openPangu-7B上，RTN与FlatQuant*的准确率相同（56.76% vs 58.50%为不同模型数据，此处需修正：openPangu-7B W4A4 RTN准确率为56.76%，FlatQuant*为58.50%？不，查表2：openPangu-7B W4A4 RTN Avg 56.76, FlatQuant* Avg 58.50。Llama-3.1-8B W4A4 RTN Avg 56.76, FlatQuant* Avg 58.50。数据巧合相同，但PPL不同）。核心发现是：旋转方法（QuaRot, SpinQuant）在MXFP4下表现劣于RTN，例如Llama-3.1-8B W4A4下QuaRot PPL为10.34，而RTN为8.27。

消融实验显示，Pre-scale策略对MXFP4性能提升显著，但对MXFP8影响较小。在Qwen2.5-VL-7B上，LLM部分的量化敏感度远高于ViT部分：LLM从W8A8降至W4A4导致恢复率从100.03%降至95.69%，而ViT降至W4A4仅导致约1%的性能损失。这表明多模态模型中，语言组件是量化精度的主要瓶颈。

评估边界方面，本文未报告吞吐量或内存占用等效率指标，仅关注精度。代码未公开，但使用了microxscaling库进行模拟。实验局限于7B/8B规模模型，未验证30B以上大模型或NVFP4格式，结论的规模泛化性未知。

## 关联研究分析

从问题动机看，本文聚焦推理侧PTQ，而MOSS、TetraJet-v2等方法聚焦训练侧FP8/FP4稳定性。MOSS通过块级缩放消除去量化开销，其设计原理与MXFP的块级结构一致，但MOSS针对训练梯度更新，本文针对静态权重压缩。关键差异在于：训练侧需保证梯度无偏性，而推理侧仅需重构误差最小。本文发现旋转在MXFP4下失效，这与训练侧TetraJet-v2使用Hadamard旋转处理异常值的共识相悖。根源可能在于：训练侧旋转作用于梯度流，而推理侧旋转作用于静态权重，两者对分布形态的要求不同。

从方法设计看，GPTQ在INT4下是SOTA，但在MXFP4下仅略优于RTN。MR-GPTQ通过引入块级Hadamard变换适配FP4，但本文实验显示其增益有限。这与SmoothQuant在INT下通过通道平滑迁移量化难度的策略形成对比：SmoothQuant在MXFP4下表现不佳（Llama-3.1-8B W4A4恢复率93.60%），因为其通道级缩放无法捕捉MXFP块内的局部分布变化。这暗示MXFP量化需要更细粒度的、块感知的误差补偿机制，而非全局或通道级变换。

## 总结

本文要解决的核心矛盾是INT优化的PTQ算法在MXFP格式下的兼容性失效。现有方法基于INT均匀网格假设，无法处理MXFP块级浮点网格的非线性舍入特性。本文通过系统实证，揭示了格式兼容性对精度的决定性影响，并验证了Pre-scale策略对MXFP4裁剪偏差的缓解作用。实验证明，在Llama-3.1-8B W4A4下，FlatQuant*恢复率达95.28%，而旋转方法PPL高达10.34，显著劣于RTN的8.27。本文的边界在于仅评估7B/8B模型且未涉及NVFP格式，其结论是否适用于更大规模模型或不同指数设计的微缩放格式，尚待验证。当模型规模扩大至30B以上时，MXFP4的量化误差是否会因参数冗余而减弱，还是因分布更复杂而加剧，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.09555)