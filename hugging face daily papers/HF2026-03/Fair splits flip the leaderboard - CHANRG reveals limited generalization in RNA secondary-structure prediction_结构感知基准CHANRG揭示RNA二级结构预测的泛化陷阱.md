# HuggingFace最新推荐论文 ｜Fair splits flip the leaderboard: CHANRG reveals limited generalization in RNA secondary-structure prediction ｜结构感知基准CHANRG揭示RNA二级结构预测的泛化陷阱

研究机构：加拿大多伦多大学、加拿大向量研究所

论文原文见 [arXiv](https://arxiv.org/abs/2603.22330)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.22330)

> 导读 RNA二级结构预测旨在从序列推断碱基配对模式，以支撑转录组注释与RNA药物设计。现有基准因结构冗余与基因组泄漏，导致模型在保留集上的高分无法反映真实泛化能力，特别是基础模型（Foundation Model, FM）的优越性存疑。本文构建结构感知去重与架构感知划分的基准CHANRG，并配套无填充对称卷积实现，量化了不同预测器在分布外（Out-of-Distribution, OOD）场景下的性能衰减。该工作挑战了“预训练规模决定泛化”的共识，但仅针对RNA二级结构，未涉及DNA基因组或三维结构预测。

## 研究背景

RNA二级结构由分子内碱基对模式定义，决定其催化与调控功能。计算预测需处理变长序列，传统密集张量填充导致接触图（Contact Map）内存与计算量随序列长度平方增长，且批次内最长序列决定填充尺寸，引发批次上下文依赖性。这种依赖使得同一RNA在不同批次中的预测结果不一致，破坏了评估的可复现性。

现有RNA二级结构预测器分为三类：结构化解码器（Structured Decoder, SD）如EternaFold，通过热力学优化生成结构；直接神经预测器（Direct Neural, DL）如bpFold，直接学习接触图；基础模型预测器（FM）如RiNALMo，结合预训练编码器与结构头。主流基准如bpRNA主要基于序列身份去重，忽略了结构相似性导致的泄漏，且缺乏针对架构、进化距离或基因组稀疏性的OOD划分。这导致FM在保留集上的高分可能源于对训练分布的过拟合，而非可迁移的结构学习。

本文切入点在于构建一个结构感知、泄漏控制的基准CHANRG，并揭示FM在OOD下的系统性失效。通过引入基于bpRNA-CosMoS的结构去重与架构感知划分，CHANRG确保了评估样本相对于训练集具有真正的结构新颖性，从而暴露了现有评估体系的盲区。

## 核心方法

### 方法参照系

RNA二级结构预测的标准流程包括序列输入、结构预测与评估。传统评估使用保留集（Held-out Set）计算碱基对F1分数，但缺乏对结构新颖性与基因组泄漏的控制。本文问题与该通用流程的关键差异在于：评估目标从“保留集精度”转向“分布外鲁棒性”，且计算路径需消除变长序列的批次依赖性。

### 结构感知去重与架构感知划分

传统基准仅按序列相似度去重，导致结构相似但序列不同的RNA跨越评估边界。CHANRG采用bpRNA-CosMoS结构相似度分数进行二次去重，移除结构冗余。划分设计基于RNArchitecture层级，将数据分为保留集（Test/Validation）与三个OOD区域：GenA（架构新颖）、GenC（进化距离远）、GenF（基因组稀疏）。

$$
\text{Retention}_{\text{OOD}} = \frac{\text{Metric}_{\text{OODmean}}}{\text{Metric}_{\text{Test}}}
$$

该公式量化了模型从保留集到OOD的性能保留率，揭示了FM在结构新颖性下的崩溃。设计动机在于解决序列去重无法捕捉结构拓扑相似性的问题，确保评估样本具有真正的生物学新颖性。

### 无填充对称卷积实现

密集张量填充导致批次上下文依赖，同一RNA在不同批次中预测结果不同。CHANRG提供NestedTensor参考实现，将填充位置从计算图中移除，并在输出层通过对称平均 $o = (y + y^\top)/2$ 强制对称性。

$$
\text{Latency}_{\text{Nested}} = \frac{\text{Latency}_{\text{Padded}}}{3.3}, \quad \text{Memory}_{\text{Nested}} = \frac{\text{Memory}_{\text{Padded}}}{6.7}
$$

该实现消除了批次依赖，使评估结果仅取决于序列内容。设计动机在于解决密集卷积混合有效与填充区域导致的预测偏差，同时降低计算成本。

## 实验评估

实验基于CHANRG基准，包含170,083个结构非冗余RNA，覆盖29个预测器。基线涵盖SD（EternaFold, RNAfold）、DL（bpFold, SPOT-RNA）与FM（RiNALMo, ERNIE-RNA）。核心发现是FM在保留集上表现最佳，但在OOD下显著劣于SD与DL。

| 方法类别 | 代表模型 | Test Base-pair F1 | OODmean Base-pair F1 | OODmean Topology F1 |
| :--- | :--- | :--- | :--- | :--- |
| FM | RiNALMo-giga | 0.7579 | 0.2140 | 0.0911 |
| SD | EternaFold | 0.3189 | 0.3064 | 0.1227 |
| DL | bpFold | 0.4065 | 0.3608 | 0.1552 |

FM在Test上的高分（0.7579）在OODmean上骤降至0.2140，而SD与DL的OODmean分数（0.3064, 0.3608）远高于FM。这表明FM的保留集优势主要源于对训练分布的拟合，而非可迁移的结构学习。

消融实验显示，序列长度匹配后，FM在GenA上的性能有所提升，但在GenC与GenF上仍显著低于SD与DL。这排除了序列长度作为OOD失效的唯一解释，指向结构/进化偏移的根本原因。模型规模扩展（RiNALMo micro到giga）仅轻微提升OODmean（0.1460到0.2140），进一步证实规模无法解决泛化问题。

评估边界方面，CHANRG未覆盖伪结（Pseudoknot）的复杂预测，且仅针对RNA二级结构，未涉及DNA或三维结构。代码未公开，但提供了NestedTensor参考实现，确保评估的可复现性。

## 关联研究分析

从问题动机看，CHANRG与DNA基因组基础模型（如Nucleotide Transformer）的评估范式存在根本差异。DNA领域关注长程依赖与分词错位，而RNA领域聚焦结构新颖性与批次不变性。CHANRG的结构感知去重直接回应了RNA结构预测中“序列相似但结构不同”的泄漏问题，这在DNA基准中较少被强调。

从方法设计看，CHANRG的无填充对称卷积与DNA领域的状态空间模型（SSM）架构创新不同。SSM旨在降低长序列计算复杂度，而NestedTensor旨在消除变长序列的批次依赖。两者均针对计算效率，但解决的问题不同：SSM解决长程依赖的二次方复杂度，NestedTensor解决变长序列的填充偏差。

## 总结

本文核心矛盾在于现有RNA二级结构基准无法区分“保留集拟合”与“真实泛化”。CHANRG通过结构感知去重与架构感知划分，揭示了FM在OOD下的系统性失效，其Test F1 0.7579在OODmean上降至0.2140，远低于SD与DL。该基准与无填充实现提供了更严格的评估框架，但仅针对RNA二级结构，未涉及DNA或三维结构。当预训练数据引入结构标注时，FM的OOD泛化能力是否可恢复，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.22330)