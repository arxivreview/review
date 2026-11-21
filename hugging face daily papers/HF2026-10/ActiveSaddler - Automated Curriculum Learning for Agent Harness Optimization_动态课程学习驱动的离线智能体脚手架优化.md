# HuggingFace最新推荐论文 ｜ActiveSaddler: Automated Curriculum Learning for Agent Harness Optimization ｜动态课程学习驱动的离线智能体脚手架优化

研究机构：韩国科学技术院

作者：Sungho Park、Wonjoong Kim、Jue Zhang 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.00906)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.00906)

> 离线智能体脚手架（Harness）优化面临固定训练场景调度与动态缺陷演化之间的失配，导致有限计算预算被低价值目标消耗。现有方法仅关注“如何更新脚手架”，却忽略了“用哪些场景驱动更新”这一维度。本文将该调度问题形式化为非平稳多臂赌博机（Non-Stationary Multi-Armed Bandit, NS-Bandit），提出 ActiveSaddler 框架，通过动态实例化失败模式臂并自适应平衡探索与利用，实现脚手架与课程协同进化。该框架在 GAIA2 和 Terminal-Bench 2.0 上显著提升了单位成本下的性能增益，但其对 LLM 评分模块的依赖及跨基准泛化性仍存疑。

## 研究背景

智能体在长程任务中的可靠性高度依赖外部脚手架，该脚手架定义了提示策略、工具接口及运行时控制逻辑。当模型能力或任务分布发生漂移时，静态脚手架的有效性迅速衰减，迫使研究者开发自动化优化机制。然而，执行轨迹的随机性与脚手架的迭代更新导致“可修复缺陷”的集合处于动态变化中，这构成了一个典型的非平稳资源分配问题。

主流离线脚手架优化方法（如 AutoSaddler、GEPA）通常预设训练场景的执行顺序或采用固定难度排序，这种静态课程无法响应优化过程中的状态转移。具体而言，已修复的缺陷不再需要额外关注，而未解决的缺陷可能因脚手架更新而变得更具可修复性；同时，当已知缺陷的修复潜力耗尽时，探索未见场景以发现新缺陷的价值上升。固定调度无法捕捉这种价值动态，导致大量 Rollout 预算浪费在低价值目标上，或在缺陷未充分修复时过早转移。ActiveSaddler 的切入点在于将场景选择从“预定义序列”转变为“在线决策过程”，使课程本身成为可优化的对象，与脚手架更新形成闭环反馈。

## 核心方法

### 方法参照系

本文问题可置于离线学习式脚手架优化（Learning-based AHO）框架下，其标准流程为：执行当前脚手架 -> 收集执行轨迹 -> 诊断缺陷 -> 生成补丁 -> 评估候选。关键差异在于，传统流程中训练 Mini-batch 的选取是静态的，而本文将其替换为基于非平稳 Bandit 的动态调度机制，将“场景选择”提升为与“脚手架更新”同等重要的优化维度。

### 失败模式臂的在线实例化

传统方法将每个失败场景视为独立优化目标，导致缺陷证据碎片化且无法跨场景复用。ActiveSaddler 引入 Failure-Pattern Extractor，将归因于同一底层缺陷的多个失败轨迹聚合为一个“失败模式臂”（Failure-Pattern Arm）。这一设计解决了场景级臂（Scenario Arm）在有限预算下因臂数量过多（如 75 个独立臂）导致单个缺陷难以被反复观察和修复的问题。臂的集合 $A_t$ 在优化过程中动态扩展，新发现的缺陷模式通过 $pattern \ register$ 操作实例化为新臂，其状态由严重程度、可修复性、广度及副作用四个维度评分：

$$
\phi_t(a) = g_{select}(a, I_{<t}) = f(\text{severity}, \text{fixability}, \text{breadth}, \text{side-effect})
$$

该评分函数 $\phi_t(a)$ 估计针对臂 $a$ 进行下一轮优化的潜在学习进度，而非简单的失败率。通过 LLM 对执行轨迹进行语义诊断，该评分能捕捉“缺陷是否在当前脚手架版本下仍具可修复性”，从而避免将预算分配给已失效或不可修复的缺陷。

### 自适应探索-利用平衡

在已知臂集合 $A_t$ 中，Arm Prioritizer 根据 $\phi_t(a)$ 选择高优先级臂进行利用（Exploit）；同时，Exploration Controller 决定何时从未见场景池 $U_t$ 中采样新场景以发现新缺陷（Explore）。这一平衡机制解决了固定探索率（如 UCB-AIR）无法适应脚手架演化状态的问题。当已知臂的评分普遍降低时，探索价值上升；反之，利用价值上升。探索决策 $d_t$ 由 LLM 基于当前脚手架状态 $H_t$、臂集合 $A_t$ 及历史 $I_{<t}$ 生成：

$$
d_t = g_{explore}(H_t, A_t, U_t, I_{<t}) \in \{\text{pull}, \text{draw}\}
$$

其中 $\text{pull}$ 表示选择已知臂，$\text{draw}$ 表示采样未见场景。该机制确保了在缺陷空间发生漂移时，课程能及时调整焦点，避免在已饱和的缺陷上过度利用，或在缺陷未充分暴露时过早探索。

## 实验评估

实验在 GAIA2 和 Terminal-Bench 2.0 上进行，基线包括 AutoSaddler（固定顺序）、Category/Scenario Order（固定难度/场景顺序）及 GEPA（进化搜索）。缺失 DarwinX 等自然选择类基线，但覆盖了主要离线优化路线。

| 方法 | GAIA2 Test Pass@1 (%) | Terminal-Bench 2.0 Test Pass@1 (%) |
| :--- | :--- | :--- |
| AutoSaddler (Run 1) | 55.4 ± 1.2 | 72.5 ± 0.0 |
| AutoSaddler w/ Scenario Acc. Order | 55.9 ± 0.7 | 73.3 ± 1.4 |
| ActiveSaddler (Run 1) | 59.8 ± 1.0 | 80.0 ± 2.5 |
| ActiveSaddler (Run 2) | 61.6 ± 2.9 | — |

ActiveSaddler 在 GAIA2 上较 AutoSaddler 提升 4.4 个百分点，在 Terminal-Bench 2.0 上提升 7.5 个百分点。消融实验显示，移除 Arm Prioritizer 导致 GAIA2 性能下降 4.5 个百分点（59.8% -> 55.3%），移除 Exploration Controller 下降 4.5 个百分点（59.8% -> 55.3%），表明两个组件均不可或缺。替换为 EMA 评分（56.7%）或 UCB-AIR 控制器（55.6%）均显著劣于 LLM 自适应评分，证实了语义级评分对捕捉复杂缺陷动态的必要性。

评估边界方面，GAIA2 采用 Universe 级划分以测试分布外泛化，而 Terminal-Bench 2.0 采用随机划分，两者协议不一致可能影响跨基准比较。论文未报告计算效率的置信区间，且 LLM 评分模块的开销（每补丁 $11.44 vs $7.87）虽被 Rollout 效率提升抵消，但在极端预算受限场景下的净收益未充分验证。

## 关联研究分析

从问题动机看，ActiveSaddler 与 DarwinX 等 Harness 进化方法同属非参数化路线，但前者聚焦于“优化过程的调度效率”，后者聚焦于“脚手架结构的搜索空间”。DarwinX 通过自然选择机制在冻结权重下优化脚手架，其课程选择隐含在种群更新中，未显式建模缺陷的动态价值；ActiveSaddler 则通过显式的 Bandit 框架将调度决策解耦，使其可独立优化。这一差异源于任务特性：DarwinX 面向结构搜索，而 ActiveSaddler 面向缺陷修复，后者对“何时修复哪个缺陷”的时序敏感性更高。

从方法设计看，ActiveSaddler 与 TSCL（Matiisen et al., 2017）共享非平稳 Bandit 框架，但 TSCL 使用 EMA 评分跟踪失败率，而 ActiveSaddler 使用 LLM 评分估计“可修复性”。这一差异源于缺陷的语义复杂性：TSCL 处理的是数值型任务，失败率即可反映难度；而 ActiveSaddler 处理的是自然语言任务，同一失败模式在不同脚手架版本下的可修复性可能截然不同，EMA 无法捕捉这种语义漂移。论文未验证 LLM 评分在缺陷空间高度稳定场景下的边际收益，其优势是否完全依赖于缺陷的动态性尚不明确。

## 总结

ActiveSaddler 解决了离线脚手架优化中固定课程与动态缺陷演化之间的失配矛盾，通过非平稳 Bandit 框架将场景选择转化为在线决策问题，实现了课程与脚手架的协同进化。该框架在 GAIA2 和 Terminal-Bench 2.0 上分别提升 4.4 和 7.5 个百分点，证明了动态调度对有限预算下性能增益的关键作用。其边界在于对 LLM 评分模块的强依赖，以及跨基准协议不一致导致的泛化性验证不足。当缺陷空间趋于稳定或 LLM 评分成本占比超过 Rollout 成本时，该框架的净收益是否仍能保持优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.00906)