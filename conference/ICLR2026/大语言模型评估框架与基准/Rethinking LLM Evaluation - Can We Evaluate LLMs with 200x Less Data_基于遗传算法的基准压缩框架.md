# ICLR2026最新论文 ｜Rethinking LLM Evaluation: Can We Evaluate LLMs with 200x Less Data? ｜基于遗传算法的基准压缩框架

研究机构：阿里巴巴集团

作者：Shaobo Wang、Cong Wang、Wenjie Fu 等 14 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.10457)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.10457)

> 大语言模型（LLM）评估面临计算成本高昂与样本冗余并存的困境，传统统计方法在子集选择中收敛效率低且忽略样本间语义关联。本文切入点在于将基准压缩重构为离散优化问题，通过引入样本冗余度量化与迭代遗传算法（Genetic Algorithm, GA）实现高效子集搜索。该方法在 HellaSwag 上以 25 倍压缩比保持排名稳定，但在无历史数据场景下的泛化能力存疑。

## 研究背景

LLM 评估的核心矛盾在于基准规模扩张与计算资源有限性之间的冲突。OpenCompass 等集成平台包含超过 60 个子任务，评估 Qwen2.5-7B-Instruct 需消耗约 1000 GPU 小时。这种高成本源于基准中普遍存在的样本冗余：文本层面的语义重叠与排名层面的行为一致性导致大量题目对模型区分度贡献极低。冗余度可通过嵌入相似度与排名相关性量化，但如何从指数级离散空间中高效剔除冗余并保留信息量最大的子集，仍是未解决的组合优化难题。

现有基准压缩路线主要依赖统计启发式或心理测量学方法。TinyBenchmarks 结合聚类与项目反应理论（Item Response Theory, IRT）选取 100 道代表题，MetaBench 利用广义可加模型（Generalized Additive Models, GAM）与 Fisher 信息量筛选判别性样本。然而，这些方法将样本视为独立实体，忽略了高相似样本间的强相关性，且统计搜索机制在复杂语义空间中易陷入局部最优，收敛速度慢。EssenceBench 针对这一瓶颈，提出一种粗到细的迭代压缩框架，通过显式建模样本交互与元启发式搜索，在保持重构精度的同时大幅降低计算开销。

## 核心方法

### 基准压缩的离散优化参照系

基准压缩本质是从全集 $D$ 中选取 $k$ 元子集 $D_{\tilde{}}$ 以重构全量分数。传统流程依赖 IRT 参数估计或 Fisher 信息量进行贪心选择，假设样本独立且难度固定。本文的关键差异在于将问题形式化为 NP-hard 组合优化任务，引入样本间交互权重，并采用元启发式搜索替代统计启发式，以应对高维离散空间中的非凸性。

### 双重冗余度量化与粗过滤

设计动机在于解决传统方法忽略样本语义关联导致的冗余残留。本文定义文本冗余度 $R_{text}(i, j) = \langle \text{Emb}(x_i), \text{Emb}(x_j) \rangle$ 与排名冗余度 $R_{ranking}(i, j) = \rho(\text{Rank}(x_i), \text{Rank}(x_j))$，其中 $\rho$ 为 Pearson 相关系数。

$$
\epsilon_i = \mathbb{I}\left( \exists j < i, R_{text}(j, i) > \tau_{text} \lor R_{ranking}(j, i) > \tau_{ranking} \right)
$$

该公式通过阈值 $\tau$ 判定样本 $x_i$ 是否被前序样本覆盖，若任一冗余度超阈值则丢弃。此步骤在 GA 搜索前剔除低信息量样本，将搜索空间从 $N$ 缩减至 $M$，显著降低后续优化难度。

### 迭代遗传算法与归因分组

设计动机在于克服统计搜索在复杂空间中的局部最优陷阱。GA 以 $k$ 元掩码 $\mathbf{m}$ 为个体，适应度函数为预测分数与全量分数的负 RMSE：

$$
\text{Fitness}(\mathbf{m}) = -\text{RMSE}\left( \hat{y}(\mathbf{S}_{\mathbf{m}}), y \right)
$$

其中 $\hat{y}$ 由 GAM 预测。在每轮迭代中，基于训练权重计算样本归因 $A_j = \|f_j(\mathbf{m})\|_2$，将样本分为高、低、随机归因组。GA 在各组内独立搜索，强制探索不同信息区域，避免单一子集主导导致的多样性丧失。

## 实验评估

实验在 GSM8K、ARC、HellaSwag、WinoGrande 和 MMLU 五个基准上进行，基线包括 Random、PPL、GraNd 和 MetaBench。缺失 TinyBenchmarks 等 IRT 类强基线，限制了与心理测量学路线的直接对比。

| Dataset | Method | k=200 RMSE | k=500 RMSE |
| :--- | :--- | :--- | :--- |
| GSM8K | MetaBench | 1.7597 | 0.9579 |
| GSM8K | EssenceBench | 0.8635 | 0.3769 |
| WinoGrande | MetaBench | 1.5297 | 0.7850 |
| WinoGrande | EssenceBench | 0.7772 | 0.3905 |

在 GSM8K 上，EssenceBench 在 k=200 时 RMSE 为 0.8635，较 MetaBench 的 1.7597 降低 50.9%；在 k=500 时，RMSE 从 0.9579 降至 0.3769，降幅达 60.7%。这表明 GA 搜索在复杂语义空间中具有更强的全局优化能力，能在更小样本量下保持更高的分数重构精度。

消融实验显示，粗过滤在子集小于 400 时显著降低 RMSE，归因分组在子集小于 400 时优于无归因选择，但子集超过 400 后收益递减。参数敏感性分析表明，增加迭代轮数（从 2 到 5）在固定 generations=1000 时，RMSE 从 2.7685 降至 2.4731，而增加 generations 在轮数不足时可能因过度探索导致性能下降。

评估边界方面，论文未报告置信区间，仅展示点估计，统计显著性检验缺失。代码未开源，超参数（如 $\tau_{text}$、$\tau_{ranking}$）的具体取值未详细披露，可复现性受限。依赖 Open LLM Leaderboard 历史数据，若历史数据存在污染，压缩子集的泛化性可能受损。

## 关联研究分析

从问题动机看，EssenceBench 与 MetaBench 均旨在降低评估成本，但 MetaBench 依赖 IRT 参数估计，假设题目难度固定，而 EssenceBench 通过冗余度量化动态调整样本权重，更适应模型能力快速迭代导致的难度分布漂移。这一差异源于任务特性：MetaBench 适用于静态题库，而 EssenceBench 更适合频繁更新的动态评估场景。

从方法设计看，EssenceBench 与 Scales++ 同属高效评估路线，但 Scales++ 依赖认知尺度嵌入进行冷启动预测，无需历史数据；EssenceBench 则依赖历史分数矩阵，在冷启动场景下失效。这一限制暗示，若将 GA 搜索与动态题目生成结合，可能解决历史数据依赖问题，但论文未探索此方向。

## 总结

EssenceBench 针对 LLM 评估中样本冗余与计算成本高昂的矛盾，通过双重冗余度量化与迭代 GA 搜索，实现了基准压缩的高效重构。其在 GSM8K 上以 200 倍压缩比保持排名稳定，证明了元启发式搜索在离散优化中的优势。然而，方法依赖历史数据，且未提供统计保证，边界在于无法处理无历史数据的冷启动场景。当历史数据存在系统性偏差时，GA 搜索是否仍能收敛至无偏子集，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.10457)