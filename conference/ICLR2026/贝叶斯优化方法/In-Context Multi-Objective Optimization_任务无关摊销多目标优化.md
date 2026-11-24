# ICLR2026最新论文 ｜In-Context Multi-Objective Optimization ｜任务无关摊销多目标优化

研究机构：芬兰阿尔托大学、英国曼彻斯特大学

作者：Xinyu Zhang、Conor Hassan、Julien Martinelli 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.11114)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.11114)

> 多目标贝叶斯优化（MOBO）旨在以极少的昂贵评估次数逼近帕累托前沿，但传统范式依赖高斯过程（GP）迭代拟合与短视采集函数，导致推理延迟高且难以跨维度迁移。TAMO 通过预训练维度无关的 Transformer 策略，将优化历史直接映射至下一查询点，消除了代理模型重拟合开销。该方法在合成与真实任务上实现了 50-1000 倍的提案速度提升，但在标准多目标基准上的绝对性能缺乏与最新 SOTA 的直接对标，其泛化边界仍存疑。

## 研究背景

当实验设计需同时平衡精度与成本时，单一最优点往往不存在，必须寻找一组互不支配的解集，即帕累托前沿（Pareto Frontier, PF）。评估这些黑盒目标函数的代价高昂，使得样本效率成为核心约束。传统 MOBO 依赖 GP 量化不确定性，但 GP 的 $O(n^3)$ 计算复杂度在迭代优化中成为瓶颈，且其性能高度依赖核函数等超参数的任务特定调优，这在数据稀缺场景下尤为脆弱。

主流 MOBO 路线包括标量化（如 ParEGO）、基于指标（如 EHVI）及信息论方法，它们均需在每步重新拟合代理模型并优化采集函数。这一流程不仅计算昂贵，且采集函数通常仅优化单步增益（myopic），无法有效规划多步探索以均匀覆盖 PF。近期摊销优化（Amortized Optimization）尝试将计算离线化，但现有工作如 BOFormer 仅摊销采集函数计算，仍依赖 GP 且固定目标维度，无法处理异构任务。TAMO 的切入点在于实现端到端的摊销：通过预训练一个维度无关的策略，使其在测试时仅需单次前向传播即可提出新设计，彻底摆脱对任务特定代理模型的依赖。

## 核心方法

### 摊销策略参照系

TAMO 将 MOBO 重构为马尔可夫决策过程（MDP），状态为当前历史观测集 $D_h$ 与剩余预算，动作为从候选集中选择下一查询点。与标准 MOBO 不同，TAMO 不显式拟合 GP 后验，而是直接学习从历史到动作的映射策略 $\pi_\theta$，其核心差异在于将“代理拟合+采集优化”的两阶段过程合并为单一的神经前向传播。

### 维度无关嵌入器

标准 Transformer 处理固定维度输入，而 MOBO 任务中输入维度 $d_x$ 与目标维度 $d_y$ 常随任务变化。TAMO 引入维度无关嵌入器，通过可学习的标量到向量映射 $e_x: \mathbb{R} \rightarrow \mathbb{R}^{d_e}$ 和 $e_y: \mathbb{R} \rightarrow \mathbb{R}^{d_e}$ 将每个标量特征独立编码，随后通过 $L$ 层 Transformer 聚合，并应用维度特定位置令牌 $\mathbf{p}_x, \mathbf{p}_y$ 以区分不同维度的语义。最终通过均值池化获得固定维度表示 $\mathbf{E} \in \mathbb{R}^{d_e}$。

$$ \mathbf{E} = \text{MeanPool}\left( \text{Transformer}_L([e_x(\mathbf{x}); e_y(\mathbf{y})] + \mathbf{p}_x + \mathbf{p}_y) \right) $$

该设计解决了固定维度架构无法跨任务迁移的问题，使模型能处理任意 $d_x$ 和 $d_y$ 的组合，且计算复杂度仅随观测数量线性增长，而非随维度立方增长。

### 强化学习策略优化

TAMO 采用 REINFORCE 算法优化策略，奖励函数定义为归一化超体积水平，即当前帕累托近似覆盖的最大可达超体积比例。

$$ r_t = \frac{\text{HV}(P(D_h) | \mathbf{r})}{\text{HV}_\tau^\star} $$

其中 $\text{HV}_\tau^\star$ 为任务最优前沿的超体积。该奖励机制鼓励策略进行长程规划，而非仅优化单步增益。训练分为两阶段：首先通过预测任务（In-Context Regression）预热骨干网络，学习函数景观表示；随后联合优化策略与预测目标，其中预测任务使用与优化任务不相交的数据以防止奖励泄露。

$$ \mathcal{J}(\theta) = \mathbb{E}_{\tau \sim p(\tau)} \left[ \sum_{t=1}^T \gamma^{T-t} r_t \right] + \lambda_p \mathcal{L}_{pred} $$

此设计解决了短视采集函数在多步规划中的次优性，通过最大化累积超体积改进，提升了帕累托前沿的覆盖均匀性。

## 实验评估

实验在合成 GP 任务（GP-DX2-DY2）、解析函数（Ackley-Rastrigin, Ackley-Rosenbrock, Branin-Currin）及真实任务（Oil, Sorbent）上进行，对比基线包括 BOFormer、qNEHVI、qNParEGO、qHVKG 及随机搜索。基线覆盖了摊销采集函数（BOFormer）与标准指标优化（qNEHVI 等）路线，但缺失 TuRBO、REMBO 等高维经典基线及 MOBO-OSD 等最新多目标方法。

| 任务 | 方法 | Simple Regret (100 calls) | 推理时间 (s) |
|---|---|---|---|
| GP-DX2-DY2 | TAMO | 0.023 | 0.01 |
| GP-DX2-DY2 | BOFormer | 0.059 | 1.5 |
| Branin-Currin | TAMO | 0.023 | 0.01 |
| Branin-Currin | qNEHVI | 0.059 | 2.0 |

TAMO 在 Simple Regret 上与 BOFormer 持平或略优，但推理时间降低 50-1000 倍。在 Branin-Currin 上，TAMO 的 Regret 为 0.023，显著低于 qNEHVI 的 0.059，表明摊销策略在有限预算下具有更高的样本效率。

消融实验显示，批量大小 $q$ 对性能影响有限，$q=1$ 时 Regret 下降最快，$q>1$ 时因缺乏真实反馈导致轻微退化，但可显著降低墙钟时间。查询集大小 $N_q$ 在 256-2048 范围内对 Regret 不敏感，仅在 Branin-Currin 上小 $N_q$ 会遗漏潜在区域。

评估边界方面，论文未报告置信区间，且缺乏 DTLZ/ZDT 标准多目标基准数据，无法直接对比 MOBO-OSD 等 SOTA 方法。代码未公开，超参数细节（如 Transformer 层数、嵌入维度）未在正文中明确给出，可复现性受限。

## 关联研究分析

从问题动机看，TAMO 与 BOFormer（Hung et al., 2025）均旨在摊销 MOBO 计算，但 BOFormer 仅摊销采集函数，仍依赖 GP 且固定目标维度，而 TAMO 实现端到端摊销与维度无关。这一差异源于任务特性：BOFormer 假设目标维度固定，适用于单一类型任务，而 TAMO 通过维度无关嵌入器支持异构任务迁移，但代价是放弃了 GP 的严格不确定性校准。

从方法设计看，TAMO 与 TabPFN（Hollmann et al., 2025）共享摊销推断架构，但 TabPFN 聚焦单目标表格分类，TAMO 扩展至多目标优化。TAMO 引入强化学习优化长程回报，而 TabPFN 仅优化预测似然。这一差异表明，多目标优化需要显式的帕累托质量指标（如超体积）作为奖励信号，而非仅依赖预测准确性。TAMO 的 RL 训练是否能在高维噪声场景下保持稳定性，论文未给出回答。

## 总结

TAMO 解决了 MOBO 中代理模型重拟合开销与短视采集函数的矛盾，通过维度无关 Transformer 与 RL 策略实现端到端摊销。其核心贡献在于将提案时间降低 50-1000 倍，并在有限预算下匹配或超越 GP 基线的帕累托质量。然而，论文未提供 DTLZ/ZDT 标准基准数据，且缺乏与 MOBO-OSD 等最新多目标方法的直接对比，其泛化能力在复杂高维场景下仍存疑。当预训练数据分布与真实任务存在显著差异时，TAMO 的性能退化程度如何，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.11114)