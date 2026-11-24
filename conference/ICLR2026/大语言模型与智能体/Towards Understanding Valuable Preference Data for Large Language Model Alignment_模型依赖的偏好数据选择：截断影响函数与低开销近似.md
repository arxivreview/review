# ICLR2026最新论文 ｜Towards Understanding Valuable Preference Data for Large Language Model Alignment ｜模型依赖的偏好数据选择：截断影响函数与低开销近似

研究机构：香港浸会大学、澳大利亚悉尼科技大学

作者：Zizhuo Zhang、Qizhou Wang、Shanshan Ye 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.13212)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.13212)

> 大语言模型对齐依赖高质量偏好数据，但现有预处理范式将数据质量视为静态固有属性，忽略了模型状态对数据效用的动态影响。本文指出数据价值随模型参数变化，提出截断影响函数（Truncated Influence Function, TIF）识别中等影响值数据，并设计仅需前向传播的LossDiff-IRM近似以解决TIF的计算瓶颈。该方法在多个基准上以50%-64%的数据量实现了优于全量训练的对齐效果，但其模型依赖性假设在跨预训练范式的泛化性上仍存疑。

## 研究背景

偏好对齐的核心困境在于，人工标注的成对偏好数据 $(x, y_w, y_l)$ 存在主观噪声，而直接训练会导致模型过拟合或学习错误信号。传统影响函数（Influence Function, IF）通过一阶泰勒近似量化单个训练样本对验证集性能的影响，但在开放域对齐任务中，高IF值数据往往对应模型对少量样本的过拟合，而非真正的泛化能力。

主流数据清洗路线依赖外部奖励模型或GPT-4评分进行静态筛选，隐含假设数据质量独立于训练配置。然而，这种静态视角无法捕捉模型参数演化过程中数据效用的动态变化，导致筛选出的数据在特定模型阶段可能产生负迁移。本文切入点在于将数据质量重构为模型依赖属性，通过动态评估当前模型状态下每个偏好对的实际贡献，打破静态筛选的局限。

## 核心方法

### 方法参照系

本文问题属于偏好数据选择策略，但区别于基于外部评分的静态清洗。标准流程通常利用奖励模型分数排序数据，而本文的关键差异在于引入模型状态作为筛选依据，将数据效用与当前策略 $\pi_\theta$ 绑定。

### 截断影响函数（TIF）

传统IF假设高影响值数据最具价值，但在DPO训练中，高IF数据会导致验证损失先降后升，奖励边际（Reward Margin）持续增加但泛化能力下降。TIF通过截断机制排除极端值，仅保留中等影响值数据。其定义为：

$$ \text{TIF}(d; \pi_\theta; D_{val}) = \mathbb{I}[\delta_{small} < \text{IF}(d; \pi_\theta; D_{val}) < \delta_{large}] $$

该公式通过指示函数筛选出IF值位于 $\delta_{small}$ 和 $\delta_{large}$ 百分位之间的数据，物理含义是排除噪声（低IF）和过拟合（高IF）样本，仅保留提供稳定学习信号的数据。

### LossDiff-IRM 近似

TIF计算需反向传播，在大规模LLM中不可行。本文提出两个仅需前向传播的评分函数：LossDiff（当前模型与验证集对齐辅助模型的损失差）和IRM（DPO损失中的隐式奖励边际）。组合指标定义为：

$$ \text{LossDiff-IRM}(d) = \mathbb{I}[\xi_{small} < \text{LossDiff}(d) < \xi_{large}] \cdot \mathbb{I}[\tau_{small} < \text{IRM}(d) < \tau_{large}] $$

该设计动机在于，单一评分函数存在特定偏差，而LossDiff基于验证集方向，IRM基于模型内部感知，二者偏差源不同，取交集可抵消误差，实现高效且鲁棒的数据筛选。

## 实验评估

实验在Llama-3.1-8B、Qwen3-8B-Base及Pythia系列上，使用UltraFeedback数据集，对比Full Data、Random、GPT4、Reward Model及CurriDPO等基线。本文方法在AlpacaEval 2.0上Llama-3.1-8B (DPO) WinRate达87.08%，显著高于Full Data的78.41%和GPT4筛选的84.30%。

| 方法 | Llama-3.1-8B (DPO) AlpacaEval WinRate (%) | Qwen3-8B-Base (DPO) UltraFeedback WinRate (%) |
| :--- | :--- | :--- |
| Full Data | 78.41 | 63.85 |
| GPT4 | 84.30 | 64.12 |
| LossDiff-IRM | 87.08 | 71.52 |

消融实验显示，单独使用LossDiff或IRM的效果均低于组合指标，验证了偏差抵消机制的有效性。在Pythia-410M上，LossDiff-IRM的WinRate为85.16%，而Full Data仅为76.62%，表明该方法在小模型上同样有效。

评估边界方面，本文未报告计算效率的具体数值对比，仅定性说明LossDiff-IRM仅需前向传播。代码已开源，但超参数 $\delta, \xi, \tau$ 的敏感性分析未在正文中详细展开，可能影响复现性。

## 关联研究分析

从问题动机看，本文挑战了CurriDPO和RS-DPO等静态筛选方法的根本假设。CurriDPO基于GPT-4分数排序，RS-DPO基于奖励模型分数，二者均假设数据质量独立于模型状态。本文通过TIF证明，同一数据在不同模型阶段可能从有益变为有害，这种动态性源于DPO损失的非凸性，静态评分无法捕捉参数空间中的局部最优陷阱。

从方法设计看，本文与InSPO等内在自反思方法不同，后者通过模型自身生成反思文本来优化，而本文通过外部评分函数筛选数据。InSPO在AlpacaEval 2.0上LC Win Rate为14.80，而本文LossDiff-IRM在相同基准上WinRate为87.08%，指标定义差异导致直接比较困难。本文方法更侧重于数据层面的筛选，而非模型推理层面的优化，二者可互补但解决不同层面的问题。

## 总结

本文核心矛盾在于静态数据筛选无法适应模型参数演化，切入点是通过影响函数动态评估数据效用。方法上提出TIF及LossDiff-IRM近似，证明了中等影响值数据的最优性。实验显示，使用50%-64%的数据即可超越全量训练，如Llama-3.1-8B在AlpacaEval上WinRate从78.41%提升至87.08%。边界在于，TIF的截断阈值需随训练阶段调整，且模型依赖性假设在跨预训练范式下的泛化性未充分验证。当支持集规模扩大时，中等影响值数据的比例是否稳定，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.13212)