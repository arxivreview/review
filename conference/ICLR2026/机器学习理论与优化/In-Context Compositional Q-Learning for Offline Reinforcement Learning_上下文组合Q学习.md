# ICLR2026最新论文 ｜In-Context Compositional Q-Learning for Offline Reinforcement Learning ｜上下文组合Q学习

研究机构：美国宾夕法尼亚州立大学、南京大学

作者：Qiushui Xu、Yuhao Huang、Yushu Jiang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.24067)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24067)

> 离线强化学习（Offline RL）面临的核心困境是分布偏移导致的值函数过估计，传统全局Q函数难以捕捉任务中子任务间的语义差异。现有方法通过策略约束或值正则化缓解此问题，但在全局近似器上存在泛化与保守性的固有矛盾。ICQL将Q学习重构为上下文推断问题，利用线性Transformer从检索的局部转移中推断局部Q函数。该框架在组合性任务上表现突出，但其局部线性假设在高维连续空间中的普适性仍存疑。

## 研究背景

当策略查询数据未覆盖的状态-动作对时，值函数外推误差会累积并导致性能退化，这一现象称为分布偏移。分布偏移使得全局Q函数在几何相似但语义不同的状态簇上产生混淆，例如MuJoCo行走任务中，加速行走的知识无法迁移到非正常状态恢复。为缓解此问题，研究者引入了覆盖假设，如集中性（Concentrability），量化数据对目标策略的支持程度，但全局函数逼近仍受限于单一近似器的表达能力。

离线RL的主流路线分为策略约束与值正则化两类。策略约束方法如TD3+BC受限于行为策略质量，值正则化方法如CQL和IQL通过保守惩罚抑制OOD动作，但在全局数据集有限且偏斜时，最优性无法保证。ICQL的切入点在于识别出状态空间的可组合结构，即任务可自然划分为多个子任务，每个子任务对应特定的局部动力学。通过局部化建模，ICQL避免了全局近似器在语义混淆状态上的失效，将值估计问题转化为基于检索上下文的局部推断。

## 核心方法

### 局部Q函数近似

ICQL基于局部邻域定义Q函数，摒弃全局近似器。对于查询状态 $s_{query}$，定义局部邻域 $\Omega_{d, s_{query}}$ 为距离小于 $d$ 的转移集合。局部Q函数近似为：

$$ Q_{\Omega}(s, a) = w_s^T \phi(s, a) $$

其中 $\phi$ 为特征映射，$w_s$ 为局部最优权重向量。这一设计解决了全局Q函数在几何相似但语义不同状态上的混淆问题，通过局部线性逼近捕捉子任务特定的价值模式。

### 上下文推断与线性Transformer

ICQL利用线性Transformer从检索的 $k$ 个转移中推断局部权重 $w_s$。输入矩阵 $Z_0$ 由查询状态-动作对与检索转移的特征构成，通过线性注意力层 $LinAttn(Z; P, G) \triangleq PZM^\top Z^\top GZ$ 计算上下文依赖的权重。最终Q估计为：

$$ \hat{Q}(s_{query}, a_{query} | \Omega_{d, s_{query}}^k) = w_{s_{query}}^L(\Omega_{d, s_{query}}^k)^T \phi(s_{query}, a_{query}) $$

该机制允许Q函数随检索上下文动态调整，无需显式子任务标签。训练采用IQL框架，通过期望回归更新局部Q函数，优势加权回归提取策略。理论分析表明，在局部线性可逼近与权重准确推断假设下，贪心策略的性能差距有界。

## 实验评估

实验在D4RL基准的MuJoCo、Adroit和Kitchen任务上进行，对比BC、DT、TD3+BC、CQL和IQL。基线覆盖策略约束与值正则化两条路线，但缺失DR类OPE估计器及最新SOTA如DPBAC。

| 任务 | CQL | IQL | ICQL | 增益(%) |
|---|---|---|---|---|
| Walker2d-Medium-Expert | 98.7 | 109.8 | 113.3 | 3.1 |
| Hopper-Medium-Expert | 105.4 | 98.5 | 111.0 | 5.3 |
| Kitchen-Complete | 43.8 | 59.2 | 79.3 | 22.0 |

ICQL在MuJoCo任务上平均比次优基线CQL高8.8%，在Adroit任务上比IQL高6.3%，在Kitchen任务上比DT高16.4%。Kitchen任务的高增益源于其多阶段组合结构，局部Q函数能更好捕捉子任务间的价值差异。

| 检索策略 | Walker2d-Medium | Hopper-Medium | Kitchen-Complete |
|---|---|---|---|
| Random | 78.1 | 74.1 | 70.0 |
| State-Similar | 80.3 | 62.6 | 79.3 |
| State-Similar-High-Reward | 83.9 | 59.9 | 71.3 |

消融显示，State-Similar检索在Walker2d和Kitchen任务上优于Random，但在Hopper-Medium上表现最差（62.6 vs 74.1），表明检索策略的有效性高度依赖任务结构。State-Similar-High-Reward在Walker2d上最优（83.9），但在Kitchen-Complete上低于State-Similar（71.3 vs 79.3），暗示高奖励筛选可能损失局部多样性。

评估边界方面，论文未报告置信区间，多数结果基于5个随机种子。代码未公开，超参数如检索大小 $k$ 和特征维度 $d$ 对性能影响未充分消融。Hammer-Human数据集上ICQL表现不佳（3.7 vs IQL 7.2），可能源于数据集规模小且查询状态与检索状态距离大，导致上下文学习失效。

## 关联研究分析

从问题动机看，ICQL与FQE等值函数近似方法共享缓解分布偏移的目标，但FQE依赖Bellman完备性假设，而ICQL通过局部线性假设放松了这一约束。FQE的全局近似器在组合性任务上易产生语义混淆，ICQL的局部推断机制直接针对此失效。然而，ICQL的局部线性假设在高维连续空间中是否成立，论文未提供理论保证或实证验证。

从方法设计看，ICQL借鉴了In-context Learning在监督学习中的思路，将其迁移至RL值估计。与Decision Transformer等序列建模方法不同，ICQL不直接生成动作，而是推断局部Q函数。DT在Kitchen-Mixed任务上表现最优（60.0），而ICQL为59.5，表明在部分组合任务上序列建模可能更具优势。ICQL的线性注意力机制在计算效率上优于标准Transformer，但检索机制引入了额外的 $O(Nk)$ 复杂度，其中 $N$ 为数据集大小。

## 总结

ICQL解决的核心矛盾是全局Q函数在组合性任务中的语义混淆，其切入点在于利用状态空间的局部结构，通过上下文推断实现局部Q函数近似。该方法在Kitchen任务上实现16.4%的性能提升，在MuJoCo任务上平均提升8.8%。其边界在于局部线性假设的普适性未验证，且在Hammer-Human等小数据集上表现退化。当状态空间维度增加或子任务边界模糊时，局部线性近似是否仍能捕捉复杂的价值结构，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24067)