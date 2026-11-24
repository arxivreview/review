# ICLR2026最新论文 ｜Beyond Masks: Efficient, Flexible Diffusion Language Models via Deletion-Insertion Processes ｜删除-插入扩散语言模型

研究机构：香港中文大学

作者：Fangyu Ding、Ding Ding、Sijin Chen 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.23507)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.23507)

> 导读

掩码扩散语言模型（MDLM）在并行生成中面临固定长度约束与计算冗余的双重瓶颈，导致变长序列建模效率低下且缺乏自校正能力。现有方案通过填充（Padding）或复杂采样策略缓解，但未能从范式层面消除非信息性Token的计算开销。本文提出删除-插入扩散语言模型（DID），将前向过程重构为Token删除、反向过程重构为Token插入，彻底移除掩码与填充Token。该范式在同等算力下显著提升了训练与推理效率，并原生支持变长生成，但在大规模复杂推理任务上的泛化能力尚待验证。

## 研究背景

离散扩散模型基于连续时间马尔可夫链（CTMC）框架，通过前向加噪与反向去噪实现序列生成。在MDLM中，前向过程将Token转化为吸收态`<MASK>`，反向过程通过迭代去噪恢复文本。这种机制要求序列长度在扩散过程中保持恒定，导致处理变长数据时必须填充至最大长度，且每个去噪步骤都需处理全序列，造成大量FLOPs浪费在非信息性的`<MASK>`和`<PAD>`Token上。

MDLM的固定长度特性还限制了其生成灵活性：一旦Token被去噪，其位置与内容即被锁定，无法像自回归模型那样通过后续上下文修正早期错误，导致误差累积。主流路线如RADD等MDLM变体虽优化了训练目标，但仍未摆脱掩码范式的结构性限制。插入式语言模型（ILM）尝试通过迭代插入生成变长序列，但其训练目标缺乏似然界定，且每步仅插入一个Token，效率低下。本文切入点在于重构扩散过程本身，用删除-插入机制替代掩码-去噪机制，从根源上解决长度固定与计算冗余问题。

## 核心方法

### 离散扩散参照系

本文基于CTMC离散扩散框架，区别于MDLM的掩码吸收态，DID将状态空间定义为变长序列集合。前向过程通过独立Token删除逐步缩短序列，反向过程通过Token插入逐步重建序列。关键差异在于DID消除了`<MASK>`与`<PAD>`，使序列长度在扩散过程中动态变化，从而原生支持变长数据。

### 插入分数与DISE目标

MDLM的反向过程预测被掩码位置的真实Token，而DID需预测在任意位置插入任意Token的概率。直接计算具体分数（Concrete Score）因插入位置与Token组合导致状态空间爆炸而不可行。本文定义插入分数 $\bar{s}_\theta(\mathbf{x}_t, t)_{i,v}$，表示在时间 $t$ 于位置 $i$ 插入Token $v$ 的得分，其形状为 $|\mathbf{x}_t| \times |V|$，适配Transformer架构。

训练目标采用去噪插入分数熵（DISE），它是DSE目标的可处理变分上界：

$$
\mathcal{L}_{\text{DISE}}^\theta(\mathbf{x}_0) = \mathbb{E}_{t, \mathbf{x}_t} \left[ \frac{\sigma(t)}{1-t} e^{-\bar{\sigma}(t)} \sum_{i,v} \left( s_\theta(\mathbf{x}_t, t)_{i,v} - \log \bar{s}_\theta(\mathbf{x}_t, t)_{i,v} + C \right) \right]
$$

其中 $C$ 为与参数无关的常数，训练目标基于插入前后子序列计数比。该设计解决了ILM训练目标启发式、缺乏似然界定的问题，确保模型学习真实的反向插入过程。

### 并行动态规划与DICE简化

计算DISE目标需高效求解所有 $(i, v)$ 对的子序列计数比 $N(\text{Ins}(\mathbf{x}_t, i, v), \mathbf{x}_0) / N(\mathbf{x}_t, \mathbf{x}_0)$。朴素方法复杂度为 $O(mn^2V)$，本文提出并行动态规划算法，通过前缀DP与后缀DP将复杂度降至 $O(mn)$，支持向量化并行执行。

在固定长度设置下，插入分数变为时间无关，DISE目标可简化为去噪插入交叉熵（DICE）：

$$
\mathcal{L}_{\text{DICE}}^\theta(\mathbf{x}_t, \mathbf{x}_0) = \frac{\sigma(t)}{1-t} e^{-\bar{\sigma}(t)} \sum_{i,v} \left( \frac{N(\text{Ins}(\mathbf{x}_t, i, v), \mathbf{x}_0)}{N(\mathbf{x}_t, \mathbf{x}_0)} - \log \bar{s}_\theta(\mathbf{x}_t)_{i,v} + C' \right)
$$

该简化消除了时间嵌入参数，使网络输出可显式归一化，提升了固定长度基准下的训练稳定性与参数效率。

## 实验评估

| 方法 | WikiText PPL | Lambada PPL | Pubmed PPL | AG News PPL |
| :--- | :--- | :--- | :--- | :--- |
| RADD (400k) | 38.27 | 51.82 | 56.99 | 73.18 |
| DID-S (400k) | 38.72 | 49.10 | 55.02 | 76.02 |
| DID-F (800k) | 36.91 | 48.00 | 52.89 | 71.48 |

实验在OpenWebText上训练，对比RADD（MDLM基线）与ILM（插入式基线）。DID-F在同等FLOPs下（800k步 vs RADD 400k步）在7个语言建模基准中多数取得更优困惑度，验证了消除`<MASK>`带来的算力节省可转化为性能提升。变长设置下，DID在Stories数据集上生成PPL显著低于RADD与ILM，且长度分布CDF与数据分布高度一致，而RADD因填充导致长度分布偏移。

| 方法 | 训练加速比 (Small) | 训练加速比 (Large) | 推理加速比 (Fixed) | 推理加速比 (Variable) |
| :--- | :--- | :--- | :--- | :--- |
| DID vs RADD | 1.89× | 1.99× | 1.58× | 3.79× |

消融实验显示，固定长度下使用DICE目标比DISE目标性能更优，证实序列级归一化的有效性。DP算法开销随序列长度呈幂律增长（指数1.26），在4k长度下耗时11.2秒/50步，表明长序列扩展存在计算瓶颈。

评估边界方面，模型规模限于85M-1.1B参数，未验证大规模预训练下的稳定性；GSM8K评估仅对比SMDM，未涵盖LLaDA等强基线；代码未开源，超参数严格遵循RADD，缺乏独立调参验证。

## 关联研究分析

从问题动机看，DID与Block Diffusion均旨在解决MDLM效率瓶颈，但路径截然不同。Block Diffusion通过块级生成复用KV缓存，保留掩码机制；DID则彻底重构扩散过程，消除掩码。前者依赖架构修改，后者依赖范式转换。DID的变长支持源于删除-插入机制的本质属性，而Block Diffusion仍需处理固定块大小，这暗示DID在自然语言变长特性上更具结构性优势，但Block Diffusion的缓存机制在长文本推理中可能更实用。

从方法设计看，DID与ILM同属插入式生成，但理论根基不同。ILM使用启发式目标，每步单Token插入；DID基于DSE似然界定，支持并行插入。DID的DP算法精确计算子序列计数比，避免了Edit Flows中蒙特卡洛采样引入的方差。然而，DID的并行插入依赖Tau-leaping近似，在低步数生成中可能引入误差，而ILM的串行插入虽慢但确定性更强。DID在GSM8K上优于SMDM，但差距是否源于并行插入的误差累积而非架构优势，论文未提供机制解释。

## 总结

DID旨在解决MDLM固定长度约束与计算冗余的核心矛盾，通过删除-插入范式重构扩散过程，消除`<MASK>`与`<PAD>`，实现变长生成与效率提升。实验证明在同等FLOPs下，DID在语言建模困惑度与变长生成质量上优于RADD，训练加速达1.99×，推理加速达3.79×。然而，模型规模限于1.1B，GSM8K表现虽优于SMDM但远低于领域SOTA，且DP算法在长序列下计算开销显著。当序列长度扩展至4k以上时，DP算法的幂律增长是否成为DID大规模部署的主要瓶颈，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.23507)