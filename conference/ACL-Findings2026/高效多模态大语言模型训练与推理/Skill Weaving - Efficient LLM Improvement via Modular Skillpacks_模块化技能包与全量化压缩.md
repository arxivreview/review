# ACL-Findings2026最新论文 ｜Skill Weaving: Efficient LLM Improvement via Modular Skillpacks ｜模块化技能包与全量化压缩

研究机构：哈尔滨工业大学、香港理工大学

作者：Zhuo Li、Guodong Du、Zesheng Shi 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.22205)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.22205)

> 多域大语言模型（LLMs）在固定内存与延迟预算下难以兼顾多领域性能，现有参数高效微调（PEFT）方法能力保留不足，而全参数微调又导致存储与推理开销激增。SkillWeave 通过域隔离的全参数微调构建技能包，再经全量化压缩实现低延迟部署，解决了能力与效率的矛盾。该框架在 9B 规模下超越 32B 单体模型并实现 4 倍加速，但其全参微调训练成本与自生成数据质量依赖未充分量化，长期泛化能力存疑。

## 研究背景

当 LLM 需同时服务对话、推理、编码等异构任务时，单一参数空间内的任务干扰导致性能次优与灾难性遗忘。任务向量（Task Vector）定义为微调模型与基座模型的参数差 $\Delta = \theta_{ft} - \theta_0$，其线性叠加可实现能力融合，但直接存储多个全参数 $\Delta$ 带来 $O(K \cdot N)$ 的内存开销（$K$ 为任务数，$N$ 为参数量）。Delta 压缩技术（如 BitDelta、ASVD）通过低秩分解或比特量化降低存储，但推理时需反量化回 FP16，引入额外计算延迟，且低秩近似在复杂任务上精度损失显著。

现有自改进方法依赖自生成数据，但 Self-Specialization 等直接微调方法未解决跨域干扰，而 Self-MoE 等路由方法虽隔离专家，但 LoRA 专家容量有限，难以吸收细粒度领域能力。主流路线在“能力保留”与“部署效率”间存在根本冲突：PEFT 轻量但能力不足，全参数微调能力强但部署成本高。SkillWeave 的切入点在于将“能力获取”与“部署优化”解耦——先以全参数预算充分吸收领域能力，再通过全量化压缩消除推理时的反量化开销，从而在固定预算下实现多域性能与低延迟的协同。

## 核心方法

### 任务向量分解与共享知识合并

SkillWeave 将基座模型能力分解为 $K$ 个域专属技能包（Skillpacks），每个技能包对应一个任务向量 $\Delta_k$。与 Task Arithmetic 直接叠加任务向量不同，本文先通过模型合并提取共享知识 $\Delta_{shared} = \text{Merge}([\Delta_1, \dots, \Delta_K])$，再将其从各 $\Delta_k$ 中减去，使剩余 $\Delta_k$ 更稀疏且任务特异性更强。这一设计动机在于：共享知识（如基础语言结构）在多个任务中重复出现，若保留在各技能包中，不仅浪费存储，还会在推理时引入冗余计算；合并后，骨干网络承载通用能力，技能包仅存储增量领域知识，降低压缩难度。

### 全量化 Delta 压缩（SkillZip）

SkillZip 的核心创新在于对 Delta 权重与激活同时量化，实现 INT8/INT4 直接计算，消除运行时反量化。设 Delta 权重矩阵 $W$ 与输入激活 $X$，SkillZip 采用低秩分解 $W \approx AB$（$A \in \mathbb{R}^{C_i \times R}, B \in \mathbb{R}^{R \times C_o}$），并优化量化表示 $\hat{X}, \hat{A}, \hat{B}$ 以最小化端到端重建误差：

$$
\min_{\hat{X}, \hat{A}, \hat{B}} \| X W - (\hat{X} \cdot \hat{A} \cdot \hat{B}) \|_F
$$

该公式的物理含义是：在低比特整数域中，量化后的激活与权重乘积应尽可能逼近原始 FP16 计算结果。与 DeltaCome 仅量化权重不同，SkillZip 对激活采用 per-token 量化，对 $A$ 采用 per-tensor 量化，对 $B$ 采用 per-channel 量化，以适配硬件 GEMM 内核的缩放因子限制。此外，SkillZip 引入双重平滑策略：通道级平滑通过缩放向量 $s \in \mathbb{R}^{C_i}$ 重分布激活离群值，秩级平滑通过正交旋转矩阵 $Q$ 分散 $A$ 和 $B$ 中的奇异值能量，使量化轴对齐，降低重建误差。这一设计解决了传统 Delta 压缩中离群值导致量化精度下降的问题，使低比特推理在精度与延迟间取得更优平衡。

## 实验评估

实验基于 Llama-3.1-8B-Instruct 与 Qwen-2.5-7B-Instruct，评估场景涵盖通用多能力（GSM8K、MATH、HumanEval、BBH 等）与 LLM-as-Agent（AgentBench 的 DB、OS、KG、WS、WB 子集）。基线覆盖 PEFT（LoRA）、全参数微调、Delta 压缩（BitDelta、ASVD、DeltaCome）、自改进（Self-Specialization、Self-Rewarding）及模型合并（Ties-Merging、Twin-Merging），但未包含多模态专用基线（如 LLaVA-PruMerge），因本文聚焦纯文本场景。

| 方法 | MATH | MBPP | GPQA | Average |
| :--- | :--- | :--- | :--- | :--- |
| SkillZip ($X_8A_8B_8$) | 67.6 | 73.8 | 38.3 | 59.8 |
| DeltaCome | 67.2 | 73.6 | 38.3 | 59.7 |
| ASVD ($X_{16}A_{16}B_{16}$) | 61.0 | 71.1 | 36.2 | 56.3 |
| BitDelta ($X_{16}W_1$) | 63.2 | 72.8 | 37.3 | 57.7 |

SkillWeave 在 MATH 上比 Gemma2-27B-it 高 +8.1，GSM8K 高 +0.6，验证了模块化专精可超越模型规模扩展。消融实验显示，全量化组合（Merge+Smooth+Rotate）比基础量化平均提升 +2.1，其中秩级平滑贡献最大，表明离群值处理对低比特精度至关重要。

评估边界方面，论文未报告置信区间，且自生成数据的质量依赖规则过滤，可能引入偏差。代码未公开，超参数（如 DPO 学习率、量化比特数）未详细披露，可复现性受限。

## 关联研究分析

从问题动机看，SkillWeave 与 Self-MoE 均解决多域性能与部署效率的矛盾，但 Self-MoE 依赖 LoRA 专家与动态路由，而 SkillWeave 采用全参数微调后静态技能包选择。差异根源在于任务特性：Self-MoE 适合任务差异小、路由可学习的场景，而 SkillWeave 针对任务干扰严重、需细粒度能力保留的场景，全参数微调能吸收更丰富的领域知识，但训练成本更高。

从方法设计看，SkillZip 与 DeltaCome 同属 Delta 压缩，但 DeltaCome 仅量化权重，推理时需反量化，而 SkillZip 全量化权重与激活，实现低比特直接计算。这一差异源于硬件适配：DeltaCome 优化存储，SkillZip 优化推理延迟，后者更适用于边缘部署。然而，SkillZip 的全量化依赖硬件对 INT8/INT4 GEMM 的支持，若硬件不支持，其优势将消失。

## 总结

SkillWeave 解决的核心矛盾是多域 LLM 在固定预算下能力与效率的冲突。其切入点在于解耦能力获取与部署优化，通过全参数微调吸收领域能力，再经全量化压缩消除推理延迟。实验证明 9B 模型超越 32B 单体并实现 4.2 倍加速，但全参微调的训练成本与自生成数据质量依赖未量化，且缺乏多模态场景验证。当支持集增大或任务分布漂移时，静态技能包选择是否仍能保持性能优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.22205)