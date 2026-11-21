# HuggingFace最新推荐论文 ｜OSP-Next: Efficient High-Quality Video Generation with Sparse Sequence Parallelism, HiF8 Quantization, and Reinforcement Learning ｜稀疏序列并行与混合精度视频生成

研究机构：新加坡南洋理工大学、北京大学

作者：Yunyang Ge、Xianyi He、Zezhong Zhang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.28691)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.28691)

> 视频扩散模型受限于全注意力机制的二次方计算复杂度，导致高分辨率视频生成耗时过长。现有稀疏化方法多依赖动态Token选择，难以兼容高效内核与并行策略，且低精度训练易引发性能损失。OSP-Next通过固定规则的2D稀疏注意力、原生稀疏序列并行及混合精度强化学习后训练，在保持生成质量的同时实现跨硬件加速。该方案验证了稀疏架构与系统优化的协同可行性，但其加速比在绝对值上仍低于特征缓存类方法，且缺乏与主流蒸馏路线的直接对比。

## 研究背景

视频生成模型中，潜变量序列长度随分辨率与时长呈平方级增长，全注意力机制的计算开销成为主要瓶颈。为降低复杂度，稀疏注意力通过限制Token交互范围来近似全注意力，但动态选择策略导致注意力掩码不规则，难以利用FlashAttention等高效内核，且在多卡并行时引发负载不均。此外，8-bit量化因动态范围不足，常导致稀疏模型微调时训练不稳定，进一步限制了效率优化的落地。

早期稀疏化研究如Sparse VideoGen采用免训练策略，通过识别空间与时间注意力头进行稀疏计算，但无法适应注意力模式变化带来的分布偏移。可训练稀疏方法如VSA引入粗到细的Token选择，虽提升了表达力，却依赖FlexAttention等自定义内核，与标准并行框架兼容差。Open-Sora Plan v1.3提出的Skiparse-1D Attention虽实现了可训练稀疏，但将视频展平为一维序列，忽略了图像与视频固有的二维空间局部性，导致局部Token交互受限。OSP-Next的切入点在于构建一种既保留空间局部性、又天然兼容FlashAttention内核与序列并行的固定稀疏模式，并解决稀疏模型在低精度下的训练稳定性问题。

## 核心方法

### 方法参照系

视频DiT的高效化通常遵循“稀疏注意力设计+并行策略适配+精度优化”的流程。标准流程中，稀疏注意力多采用动态Token选择，并行策略基于通用Ulysses序列并行，精度优化独立于架构设计。本文的关键差异在于：稀疏模式固定化以兼容内核，并行策略针对稀疏结构定制，精度优化与稀疏微调联合进行。

### Skiparse-2D Attention

Skiparse-1D Attention将视频展平为一维序列，交替应用Token级与组级稀疏注意力，但忽略了二维空间局部性，导致空间相邻Token无法在单次注意力中交互。OSP-Next提出Skiparse-2D Attention，将Skiparse-1D模式正交应用于高度与宽度维度，使任意两个Token最多通过两次注意力操作交互。其计算复杂度降至全注意力的$1/k$，其中$k$为稀疏比率。该设计避免了动态掩码构建，保持与FlashAttention内核的原生兼容，同时更好地匹配视觉模态的空间局部性。

$$
\text{Attn}_{\text{Skiparse-2D}}(Q, K, V) = \text{Concat}\left(\text{Attn}_{\text{Token}}(Q_h, K_h, V_h), \text{Attn}_{\text{Group}}(Q_w, K_w, V_w)\right)
$$

该公式表明，Skiparse-2D Attention通过分别沿高度和宽度维度执行稀疏注意力，再拼接结果，实现了对二维局部性的显式建模。

### Sparse Sequence Parallelism (SSP)

Ulysses序列并行将序列维度切分，但稀疏注意力中不同秩可能接收不同数量的活跃Token，导致负载不均与不规则通信。OSP-Next提出SSP，利用Skiparse Rearrange的局部等价性，将子序列分配至不同秩，通过单次All-to-All通信完成稀疏模式切换。相比Ulysses SP，SSP将每块通信量减少75%，通信步数从4步降至1步，且保持秩间负载均衡。

$$
\text{Comm}_{\text{SSP}} = \frac{1}{4} \text{Comm}_{\text{Ulysses}}, \quad \text{Steps}_{\text{SSP}} = 1
$$

该公式量化了SSP在通信效率上的优势，其核心在于利用稀疏结构的局部等价性，将全局通信转化为局部重排加单次All-to-All。

### HiF8量化与Mix-GRPO后训练

稀疏模型从全注意力基线初始化时存在迁移差距，直接微调易导致生成质量下降。OSP-Next引入HiF8量化，其动态调整指数与尾数位数，提供比标准FP8更宽的动态范围，支持稀疏微调与8-bit训练的联合进行。同时，采用Mix-GRPO强化学习后训练，以VideoAlign整体分数为奖励，优化稀疏模型在空间关系、文本对齐与美学质量上的表现。

$$
\mathcal{L}_{\text{Mix-GRPO}} = \mathbb{E}_{\tau \sim \pi_\theta} \left[ \sum_{t \in \mathcal{T}_{\text{selected}}} A_t(\tau) \log \pi_\theta(\tau_t | \tau_{<t}) \right]
$$

该公式表明，Mix-GRPO仅对选定的去噪时间步进行策略梯度更新，结合SDE与ODE采样，降低了视频生成中轨迹级优化的计算成本。

## 实验评估

实验在VBench T2V基准上评估生成质量，在NVIDIA H200与Ascend 950PR上评估推理速度。基线仅对比Wan2.1全注意力模型，缺失SANA-Video、DMD等稀疏或蒸馏路线的强基线，限制了横向比较的完整性。

| 模型 | VBench Total Score (%) | 单卡H200加速比 (720P) | 8卡H200加速比 (720P) |
|---|---|---|---|
| Wan2.1 Baseline | 83.69 | 1.00× | 1.00× |
| OSP-Next | 83.73 | 1.53× | 1.42× |
| OSP-Next-HiF8 | 83.29 | 1.69× (Ascend 950PR) | 2.27× (Ascend 950PR) |

OSP-Next在VBench总分上略超Wan2.1基线，HiF8版本仅下降0.4%，验证了联合训练的可行性。加速比在768P无填充设置下更高，单卡达1.64×，8卡达1.52×，表明稀疏架构在高分辨率下优势更明显。

消融实验显示，增加全注意力块数量可逐步缩小稀疏模型与基线的差距，8个全注意力块为最优配置。Skiparse-2D Attention在零样本推理中比Skiparse-1D更接近基线，证实了二维局部性建模的有效性。HiF8量化下损失曲线与BF16几乎重叠，说明动态精度调整有效缓解了8-bit训练的稳定性问题。

评估边界方面，论文未报告置信区间，且仅在5秒视频上测试，长视频时序一致性未验证。代码与模型已开源，但超参数细节未完全披露，复现需依赖GitHub仓库。

## 关联研究分析

从问题动机看，OSP-Next与SANA-Video均针对DiT二次复杂度，但SANA-Video采用块线性注意力将复杂度降至线性，而OSP-Next采用固定稀疏模式，保留部分全注意力层以维持表达力。这一差异源于任务特性：SANA-Video侧重长视频内存优化，OSP-Next侧重高分辨率短视频的质量-效率平衡。固定稀疏模式在极端动态场景下是否比线性注意力更鲁棒，论文未给出回答。

从方法设计看，OSP-Next的SSP与Ulysses SP同属序列并行，但SSP针对稀疏结构定制，通信量减少75%。相比之下，DMD等蒸馏方法通过分布匹配压缩步数，未涉及注意力结构优化。OSP-Next用RL替代蒸馏进行质量对齐，避免了蒸馏中教师-学生轨迹匹配的精度损失，但RL后训练的计算成本未量化，其与蒸馏路线在质量-效率权衡上的优劣尚不明确。

## 总结

OSP-Next旨在解决视频DiT中稀疏注意力与系统优化、低精度训练的协同难题。其切入点在于固定稀疏模式与原生并行策略的结合，以及HiF8量化与RL后训练的联合流程。实验证明，OSP-Next在VBench总分上达到83.73%，单卡H200加速比达1.64×，HiF8版本在Ascend 950PR上加速比达2.27×。其边界在于加速比绝对值低于特征缓存方法，且缺乏与蒸馏路线的直接对比。当视频时长从5秒扩展至分钟级时，固定稀疏模式下的时序漂移是否加剧，论文未提供数据支持。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.28691)