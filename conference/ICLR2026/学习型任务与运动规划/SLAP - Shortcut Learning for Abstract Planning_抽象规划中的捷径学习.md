# ICLR2026最新论文 ｜SLAP: Shortcut Learning for Abstract Planning ｜抽象规划中的捷径学习

研究机构：美国普林斯顿大学、美国卡内基梅隆大学

作者：Y. Isabel Liu、Bowen Li、Benjamin Eysenbach 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.01107)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.01107)

> 长时程具身任务中，传统任务与运动规划（Task and Motion Planning, TAMP）依赖手工定义的技能（如抓取、放置），导致执行路径冗长且受限于人类工程师的物理交互假设。现有分层强化学习（Hierarchical Reinforcement Learning, HRL）方法虽能发现底层技能，但缺乏高层结构引导，在稀疏奖励下难以收敛。本文提出SLAP，利用现有TAMP选项构建抽象规划图，并通过离线强化学习自动发现连接抽象状态的“捷径”策略。该方法在四个仿真环境中将规划长度平均缩短50%以上，但缺乏实时闭环机制，其在动态干扰下的鲁棒性存疑。

## 研究背景

当机器人执行堆叠积木任务时，传统TAMP规划器会生成“逐个移除障碍物再放置目标”的长序列计划。这种低效源于选项（Options）的强假设：每个技能仅影响预定义的小对象集合，且接触仅限于指尖。为突破此限制，HRL尝试从底层环境线索中发现新技能，但这类从零开始（tabula rasa）的方法在长时程、稀疏奖励的操纵任务中表现不佳，因为缺乏高层任务结构的引导。

TAMP的核心矛盾在于符号逻辑的严谨性与物理执行的灵活性之间的脱节。主流路线通过预定义技能库解耦高层符号推理与低层连续控制，但技能库的静态性导致执行效率低下。SLAP的切入点在于利用现有技能的高层结构作为先验，引导强化学习发现超越手工定义的动态物理行为（如“拍打”、“晃动”），从而在保持规划逻辑正确性的同时优化执行时间。

## 核心方法

### 抽象规划图构建

SLAP基于TAMP的标准流程，但将搜索空间显式化为双层图结构。顶层节点为抽象状态 $s \in S$，边为预定义选项 $a \in A$；底层节点为环境状态 $x \in X$，边为环境动作 $u \in U$。给定任务 $(x_0, g)$，算法通过模拟选项构建广度优先搜索图，直至覆盖目标状态。在底层图上运行Dijkstra算法，可找到执行时间最短的轨迹。这一参照系确保了SLAP的解在符号层面是可行的，且继承了TAMP的渐近完备性。

### 基于剪枝的捷径策略学习

SLAP的核心创新在于将捷径学习建模为独立的MDP问题。对于抽象状态对 $(s_{init}, s_{term})$，若不存在直接选项，则定义捷径 $\hat{a} = \langle s_{init}, \pi_\theta, s_{term} \rangle$。其奖励函数设为常数负值，以最小化步数：

$$
R(x) = -1, \quad \text{terminal states} = s_{term}
$$

设计动机在于解决纯RL在稀疏奖励下无法引导策略收敛的问题。SLAP引入随机滚动剪枝机制：若 $K_{rollout}$ 次随机滚动中，$s_{term}$ 在 $T_{rollout}$ 步内被达到的次数超过阈值，则保留该捷径候选进行PPO训练。这一机制利用了“初始成功率”作为策略可学习性的代理指标，避免了在不可行捷径上浪费计算资源。

### 对象替换泛化机制

为应对测试时对象数量或属性变化，SLAP引入状态投影与对象替换。对于捷径 $\hat{a}$，定义相关原子集合 $add(\hat{a})$ 和 $del(\hat{a})$，进而确定相关对象集合 $rel(\hat{a})$。训练时，策略输入仅为相关对象的状态投影：

$$
proj_{\hat{a}}(x) = \alpha(o_1, x) \circ \cdots \circ \alpha(o_k, x), \quad o_i \in rel(\hat{a})
$$

评估时，若新任务中存在对象映射 $\sigma: rel(\hat{a}_{train}) \to rel(\hat{a}_{eval})$ 使得原子关系保持类型一致，则复用训练好的策略。这一设计使得SLAP能够泛化到未见过的对象组合，突破了TAMP中对象数量固定的假设。

## 实验评估

实验在Obstacle 2D、Obstacle Tower、Cluttered Drawer和Cleanup Table四个仿真环境中进行，基线包括Pure Planning、PPO、SAC+HER、Hierarchical RL及SOL。SLAP在所有环境中均达到100%成功率，而纯RL基线（PPO, SAC+HER）在长时程任务中成功率均为0%，Hierarchical RL在Obstacle Tower和Cluttered Drawer中也未能收敛。

| 环境 | 方法 | 成功率 (%) | 规划长度 (步) | 相对路径长度减少 |
| :--- | :--- | :--- | :--- | :--- |
| Obstacle 2D | SLAP | 100% ± 0% | 17.6 ± 1.5 | ↓ 32% ± 7% |
| Obstacle 2D | Pure Planning | 100% ± 0% | 25.9 ± 1.7 | 0% |
| Obstacle Tower | SLAP | 100% ± 0% | 79.2 ± 3.2 | ↓ 68% ± 2% |
| Obstacle Tower | Pure Planning | 100% ± 0% | 245.8 ± 10.4 | 0% |
| Cluttered Drawer | SLAP | 100% ± 0% | 165.8 ± 43.6 | ↓ 53% ± 14% |
| Cluttered Drawer | Pure Planning | 100% ± 0% | 352.1 ± 49.5 | 0% |
| Cleanup Table | SLAP | 100% ± 0% | 115.2 ± 12.3 | ↓ 73% ± 4% |
| Cleanup Table | Pure Planning | 100% ± 0% | 431.8 ± 33.1 | 0% |

SLAP在Obstacle Tower上将规划长度从245.8步降至79.2步，降幅达68%。消融实验显示，随着训练步数增加，发现的捷径数量从Obstacle 2D的11个增至Obstacle Tower的92个，规划长度持续下降。泛化测试表明，当测试时物体质量与摩擦系数加倍时，SLAP仍能维持短规划长度，而Pure Planning随障碍物数量增加性能急剧恶化。

评估边界方面，实验仅在静态、完全可观测的仿真环境中进行，未涉及动态障碍物或感知噪声。代码开源，但超参数（如剪枝阈值 $K_{rollout}$）对性能的影响未详细消融。计算成本方面，Obstacle Tower的训练耗时约9小时，使用单张H100 GPU，表明该方法在复杂环境中计算开销较高。

## 关联研究分析

从问题动机看，SLAP与ViReSkill均关注技能复用，但路径截然不同。ViReSkill依赖视觉接地重规划，在在线执行中从失败中恢复并积累技能，强调闭环鲁棒性；SLAP则完全离线学习物理捷径，依赖抽象规划的逻辑正确性，缺乏实时反馈机制。这一差异源于任务假设：ViReSkill面向动态非结构化环境，而SLAP假设环境静态且技能库足够鲁棒。SLAP的离线性质使其在计算效率上可能更优，但在应对执行偏差时缺乏ViReSkill的自适应能力。

从方法设计看，SLAP与SOL（Skill Option Learning）形成对比。SOL从底层环境线索（如熵最大化）发现选项，属于自底向上的技能发现；SLAP利用高层抽象状态结构引导底层策略学习，属于自顶向下的捷径优化。SOL在NetHack等离散环境中表现良好，但在连续操纵任务中因缺乏高层约束而难以收敛。SLAP通过引入TAMP的抽象图结构，为RL提供了明确的目标导向，解决了SOL在长时程任务中的稀疏奖励问题。然而，SLAP依赖预定义抽象状态的质量，若抽象粒度不当，可能导致捷径发现失败。

## 总结

SLAP旨在解决TAMP中预定义技能导致的执行低效问题，其切入点在于利用现有技能的高层结构引导RL发现动态物理捷径。通过构建抽象规划图并引入基于剪枝的捷径策略学习，SLAP在四个仿真环境中将规划长度平均缩短50%以上，最高达73%。然而，其实验仅在静态环境中进行，且依赖预定义抽象状态的质量，未验证在动态干扰或感知噪声下的鲁棒性。当环境出现未预见的动态变化时，SLAP的离线捷径策略是否仍能保持执行效率，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.01107)