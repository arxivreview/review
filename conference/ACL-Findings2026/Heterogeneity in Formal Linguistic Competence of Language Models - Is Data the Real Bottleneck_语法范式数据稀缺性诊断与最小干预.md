# ACL-Findings2026最新论文 ｜Heterogeneity in Formal Linguistic Competence of Language Models: Is Data the Real Bottleneck? ｜语法范式数据稀缺性诊断与最小干预

作者：H S V N S Kowndinya Renduchintala、Sumit Bhatia

论文原文见 [arXiv](https://arxiv.org/abs/2604.17930)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17930)

> 大语言模型在通用基准上表现优异，却在特定语法范式上出现低于随机猜测的失败，且单纯扩大预训练数据量无法解决这一异质性。现有宏观数据混合优化方法关注全局分布比例，缺乏对微观语法结构暴露量的因果归因能力，导致无法区分架构限制与数据稀缺。本文通过向预训练语料中注入1%的定向合成文本，验证了数据稀缺是主要瓶颈。该研究提供了“数据阈值”的新视角，但仅在小规模模型上验证，其结论向大规模模型的迁移性存疑。

## 研究背景

当模型在BLiMP基准上呈现聚合分数高、单项范式低分的矛盾现象时，核心问题在于区分这种失败是源于模型架构的归纳偏置不足，还是源于预训练语料中特定语法结构的分布稀疏。这种区分依赖于对“形式语言胜任力”（Formal Linguistic Competence）的细粒度评估，即模型对语言规则及统计规律的内化程度。BLiMP通过最小对句（minimally different pairs）隔离特定句法现象，迫使模型在语法正确与错误之间做出概率判断，从而暴露出模型在特定范式上的知识盲区。

主流的数据策展研究聚焦于宏观层面的数据混合优化，如RegMix通过代理模型回归拟合最优比例，FastMix利用端到端梯度下降调整领域权重。这些方法旨在最大化通用基准（如MMLU）的性能，假设数据效用是全局且平滑的。然而，对于低频语法范式，宏观混合策略无法捕捉其“数据阈值”效应——即极少量特定数据即可突破学习瓶颈。现有方案缺乏针对单一语法结构的因果干预机制，无法回答“增加特定结构暴露量是否足以解决失败”这一关键问题。本文切入点在于设计最小化控制实验，通过定向注入特定语法模板的合成数据，隔离数据稀缺这一单一变量，验证其对特定范式学习的决定性作用。

## 核心方法

### 方法参照系

本文问题归属于数据增强与合成路线，但区别于RePro等通用重述方法，其核心差异在于“语法结构控制”与“因果归因”。通用合成数据旨在扩充候选池或提升多样性，而本文旨在通过精准控制特定句法模板的暴露量，验证数据稀缺是否为特定范式失败的充分原因。

### 定向合成数据生成

传统合成数据生成往往忽略风格多样性，导致模型过拟合于特定文体。本文采用“语法模板+随机风格”的解耦生成策略，确保目标语法结构嵌入自然文本中。设计动机是消除合成数据分布偏移对基线性能的干扰，使性能提升可归因于语法结构本身。

$$
\mathcal{D}_{syn} = \{ d_i \mid d_i \sim \mathcal{G}(\mathcal{T}_p, \mathcal{S}_g, \mathcal{L}_l) \}
$$

其中 $\mathcal{T}_p$ 为目标范式 $p$ 的句法模板，$\mathcal{S}_g$ 为随机采样的文体（Genre），$\mathcal{L}_l$ 为随机采样的词元集合。该公式表明，生成过程强制约束目标语法结构存在，同时随机化文体与词汇，以模拟真实语料的分布特性。

### 最小干预实验设计

为了隔离数据稀缺的影响，本文采用“替换式”干预而非“追加式”。设计动机是保持总Token数恒定，排除数据量增加带来的混淆变量。具体做法是将预训练语料中1%的FineWeb文本替换为定向合成数据。

$$
\mathcal{D}_{train} = (1-\alpha)\mathcal{D}_{web} + \alpha\mathcal{D}_{syn}
$$

其中 $\alpha=0.01$，$\mathcal{D}_{web}$ 为FineWeb子集，$\mathcal{D}_{syn}$ 为定向合成数据。该公式确保模型在相同计算预算下，仅改变特定语法结构的暴露比例，从而直接检验数据密度对语法习得的因果效应。

## 实验评估

实验基于GPT-2 Small (124M) 在100M FineWeb Token上预训练，评估指标为BLiMP基准。基线覆盖Baseline（纯FineWeb）与Random（1%随机合成数据），但缺乏RegMix或FastMix等宏观混合优化基线，因任务粒度不同，此类基线不适用。

| 范式 | Baseline | Random | Targeted | ∆ |
|---|---|---|---|---|
| only_npi_scope | 20.9 | 17.0 | 69.4 | +48.5 |
| principle_A_reconstruction | 37.2 | 44.7 | 78.9 | +41.7 |
| existential_there_quantifiers_2 | 23.4 | 12.6 | 51.8 | +28.4 |
| wh_vs_that_with_gap_long_distance | 23.8 | 24.6 | 41.2 | +17.4 |
| matrix_question_npi_licensor_present | 30.8 | 25.2 | 44.2 | +13.4 |
| sentential_subject_island | 40.4 | 31.3 | 52.2 | +11.8 |
| left_branch_island_echo_question | 45.3 | 44.6 | 63.2 | +17.9 |
| coordinate_structure_constraint_complex_left_branch | 46.5 | 40.7 | 62.4 | +15.9 |
| principle_A_c_command | 49.0 | 50.4 | 46.0 | -3.0 |

Targeted组在8/9范式上显著优于Baseline，其中only_npi_scope提升48.5点，证明数据稀缺是主要瓶颈。Random组与Baseline表现相近，排除了合成数据分布偏移的干扰。

| 范式 | Baseline | 0.01% | 0.1% | 1% |
|---|---|---|---|---|
| only_npi_scope | 20.9 | 41.9 | 31.0 | 69.4 |
| principle_A_reconstruction | 37.2 | 72.3 | 71.3 | 78.9 |
| existential_there_quantifiers_2 | 23.4 | 13.2 | 25.2 | 51.8 |
| wh_vs_that_with_gap_long_distance | 23.8 | 26.4 | 28.6 | 41.2 |
| matrix_question_npi_licensor_present | 30.8 | 38.1 | 35.1 | 44.2 |
| sentential_subject_island | 40.4 | 40.5 | 43.9 | 52.2 |
| left_branch_island_echo_question | 45.3 | 49.3 | 52.5 | 63.2 |
| coordinate_structure_constraint_complex_left_branch | 46.5 | 52.7 | 59.3 | 62.4 |
| principle_A_c_command | 49.0 | 46.1 | 49.6 | 46.0 |

消融实验显示，principle_A_reconstruction在0.01%注入时即从37.2%跃升至72.3%，表明存在极低的数据阈值。然而，only_npi_scope在0.1%时性能（31.0%）低于0.01%（41.9%），呈现非单调性，暗示特定范式与语料统计的交互复杂。principle_A_c_command在所有比例下均低于随机水平，表明其失败可能源于架构限制或需更高数据密度。

评估边界受限于GPT-2 Small (124M) 与100M Token预算，未验证向Billion级模型的迁移性。代码已开源，但合成数据生成依赖GPT-OSS 120B，复现成本较高。BLiMP仅覆盖67个范式，未评估其他语言学维度。

## 关联研究分析

从问题动机看，本文与RePro (P2) 同属合成数据增强，但RePro侧重语义重述以提升多样性，本文侧重语法结构控制以诊断稀缺性。RePro假设合成数据可替代真实数据，而本文证明特定结构需定向暴露，根源在于任务特性：通用能力依赖分布覆盖，而语法习得依赖结构信号密度。

从方法设计看，本文与Online Reweighting (P20) 均关注数据分布影响，但P20是在线动态调整，本文是离线静态干预。P20假设模型偏好随训练阶段变化，需实时响应；本文证明对于稀疏语法信号，静态的1%注入即可突破瓶颈，暗示动态调度在微观语法习得中可能非必需。这一差异源于数据信号类型：通用知识信号密集且连续，语法信号稀疏且离散。

## 总结

本文核心矛盾在于LLM在特定语法范式上的失败归因不明，现有宏观混合优化无法区分架构限制与数据稀缺。本文抓住“数据阈值”这一被忽略的微观机制，通过最小干预实验证明数据稀缺是主要瓶颈。方法上，采用定向合成数据替换1%预训练语料，验证了因果效应。实验证明only_npi_scope提升48.5点，principle_A_reconstruction在0.01%注入时即显著提升。边界在于仅验证124M模型，且principle_A_c_command未获改善，暗示部分范式需更高数据密度或架构支持。当模型规模扩大至Billion级时，1%的静态注入是否仍足以突破语法习得瓶颈，还是需结合动态调度机制，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17930)