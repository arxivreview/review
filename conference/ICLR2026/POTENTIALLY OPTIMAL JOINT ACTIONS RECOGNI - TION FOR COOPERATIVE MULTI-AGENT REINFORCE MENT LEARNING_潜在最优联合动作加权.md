# ICLR2026最新论文 ｜POTENTIALLY OPTIMAL JOINT ACTIONS RECOGNI - TION FOR COOPERATIVE MULTI-AGENT REINFORCE MENT LEARNING ｜潜在最优联合动作加权

研究机构：同济大学、美国斯坦福大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_40179853)

> 合作型多智能体强化学习（Cooperative Multi-Agent Reinforcement Learning, MARL）中，价值分解方法通过单调性约束保证去中心化执行，但牺牲了联合价值函数的表达力，导致在非单调奖励结构下无法恢复最优策略。WQMIX 提出加权训练以弥补此缺陷，但其启发式近似导致权重与真实最优动作集错位。本文引入识别模块 $Q_r$ 显式估计联合动作价值，通过迭代加权机制使候选集收敛至真实最优集，从而在理论上保证最优策略恢复。该方案在矩阵博弈和捕食者-猎物任务中显著优于基线，但在大规模连续动作空间中的可扩展性尚未验证。

## 研究背景

在去中心化部分可观测马尔可夫决策过程（Dec-POMDP）中，智能体仅能观测局部状态，却需协调以最大化团队奖励。集中训练去中心化执行（Centralized Training with Decentralized Execution, CTDE）范式允许训练时访问全局信息以缓解非平稳性，执行时仅依赖局部历史。价值分解是 CTDE 下的主流路线，其核心假设是联合动作价值函数 $Q_{tot}$ 可分解为个体价值函数的单调组合，如 QMIX（Rashid et al., 2020a）通过超网络生成混合参数保证单调性，确保 $\arg\max_{\mathbf{a}} Q_{tot} = \arg\max_{\mathbf{a}} Q^*$。然而，单调性约束限制了 $Q_{tot}$ 对联合动作空间的覆盖能力，当环境奖励结构呈现非单调性（如惩罚未协调动作）时，$Q_{tot}$ 可能将次优动作评估为最优，导致策略陷入局部最优。

WQMIX（Rashid et al., 2020b）试图通过加权训练解决此问题，理想情况下对最优联合动作赋予高权重，使 $Q_{tot}$ 逼近真实最优目标 $Q^*$。然而，识别真实最优动作需遍历指数级增长的联合动作空间，实际不可行。现有变体 CW-QMIX 和 OW-QMIX 采用启发式近似：前者以 $\arg\max Q_{tot}$ 为锚点，后者直接使用 $Q_{tot}$ 值进行乐观估计。这两种方法均导致权重分配与真实最优集错位——次优动作可能获得高权重，而真正最优动作被低估。本文切入点在于，通过引入一个显式条件化于状态和联合动作的识别模块，替代启发式近似，从而在理论上闭合 WQMIX 的承诺与实现之间的差距。

## 核心方法

### 方法参照系

标准价值分解流程中，$Q_{tot}$ 直接最小化 TD 误差，权重均匀分配。本文的关键差异在于，训练过程中引入一个独立的识别模块 $Q_r$，其输出决定每个联合动作的更新权重，且 $Q_r$ 与 $Q_{tot}$ 共享同一个无约束估计器 $\hat{Q}^*$ 作为 Bootstrap 目标。

### 识别模块与潜在最优动作集

识别模块 $Q_r$ 的设计动机是解决 CW-QMIX 和 OW-QMIX 中权重与真实最优集错位的问题。$Q_r$ 显式接收全局状态 $s$、个体动作价值 $Q_i(\tau_i, a_i)$ 和联合动作 $\mathbf{a}$ 作为输入，其结构定义为：

$$
Q_r(\tau, \mathbf{a}) = V(s) + \sum_{i=1}^n \lambda_i(s, \mathbf{a}) \left( Q_i(\tau_i, a_i) - \max_{a_i' \in A_i} Q_i(\tau_i, a_i') \right)
$$

其中 $\lambda_i(s, \mathbf{a}) \ge 0$ 由超网络生成，取绝对值确保非负。该公式的物理含义是：$Q_r$ 通过中心化项衡量每个智能体动作相对于其个体最优的偏离程度，并通过自适应缩放因子 $\lambda_i$ 加权这种偏离，从而区分不同联合动作的价值。由于每个智能体的贡献在其个体最优动作处最大化，$Q_r$ 天然满足个体-全局-最大（Individual-Global-Max, IGM）原则，无需对 $Q_i$ 施加单调性约束。潜在最优联合动作集 $\mathbf{A}_r$ 定义为：

$$
\mathbf{A}_r = \{ \mathbf{a} \in \mathbf{A}_{igm} \mid Q_r(\tau, \mathbf{a}) \ge \max_{\mathbf{a}' \in \mathbf{A}_{igm}} Q_r(\tau, \mathbf{a}') - C \}
$$

其中 $\mathbf{A}_{igm}$ 是个体贪心动作组成的联合动作集，$C \ge 0$ 为稳定性容差。该定义确保 $\mathbf{A}_r$ 至少包含个体贪心动作，并可能包含其他高价值联合动作。

### 迭代加权训练机制

迭代加权机制的设计动机是确保 $\mathbf{A}_r$ 随训练进程收敛至真实最优动作集。训练权重 $w(s, \mathbf{a})$ 定义为：

$$
w(s, \mathbf{a}) = \begin{cases} 1 & \text{if } \mathbf{a} \in \mathbf{A}_r \\ \alpha & \text{otherwise} \end{cases}
$$

实验中 $\alpha=0$，即仅 $\mathbf{A}_r$ 内的动作参与 $Q_{tot}$ 的梯度更新。$Q_{tot}$ 的训练目标为：

$$
\mathcal{L}_{Q_{tot}} = \mathbb{E}_{\tau, \mathbf{a}} \left[ w(s, \mathbf{a}) \left( Q_{tot}(\tau, \mathbf{a}) - y \right)^2 \right]
$$

其中目标 $y = r + \gamma Q_{\hat{Q}^*}(\tau', \arg\max_{\mathbf{a}'} Q_{tot}(\tau', \mathbf{a}'))$。该机制通过三个网络的协同更新实现收敛：$Q_r$ 通过监督学习逼近 $\hat{Q}^*$，$\hat{Q}^*$ 作为无约束估计器提供一致的 Bootstrap 目标，$Q_{tot}$ 在加权下更新。理论证明表明，若 $Q_r$ 收敛至 $Q^*$，则 $\mathbf{A}_r$ 包含真实最优动作集，进而 $Q_{tot}$ 恢复最优策略。

## 实验评估

实验在矩阵博弈、捕食者-猎物、SMAC、SMACv2 和 Highway-Env 五个基准上进行，基线覆盖 QMIX、VDN、QPLEX、ResQ、CW-QMIX 和 OW-QMIX，但缺失 MAPPO 等策略梯度方法作为对比。

| 算法 | Predator-Prey (p=-4) | Predator-Prey (p=-5) | SMAC 3s5z | SMAC 3s_vs_5z | SMACv2 protoss |
| :--- | :--- | :--- | :--- | :--- | :--- |
| QMIX | 0 | 0 | 1.00 | 0.30 | 18.3 |
| QPLEX | 0.28 | 0.26 | 0.98 | 0.00 | 17.6 |
| CW-QMIX | 0.88 | 0.88 | 0.96 | 0.99 | 17.0 |
| OW-QMIX | 0 | 0 | 0.81 | 0.92 | 15.5 |
| ResQ | 0 | 0 | 0.97 | 0.79 | 17.5 |
| POW-QMIX | 40 | 40 | 1.00 | 1.00 | 18.8 |

POW-QMIX 在捕食者-猎物任务中，当惩罚 $p=-4$ 和 $p=-5$ 时，测试回报分别达到 40，而 QMIX 和 ResQ 均为 0，QPLEX 仅为 0.28 和 0.26，表明 POW 在非单调结构下具有显著优势。在 SMAC 3s_vs_5z 任务中，POW-QMIX 胜率为 1.00，优于 QPLEX 的 0.00 和 QMIX 的 0.30。

消融实验显示，POW 可集成至 VDN 和 QPLEX。POW-VDN 在 SMAC 3s5z 中胜率为 0.95，高于 VDN 的 0.69；POW-QPLEX 在 SMACv2 zerg 任务中回报为 19.9，高于 QPLEX 的 16.0，且稳定了 QPLEX 在 zerg 场景中的崩溃现象。这表明 POW 的增益不仅限于 QMIX 骨干，而是源于识别加权机制本身。

评估边界方面，SMACv2 使用平均测试回报而非胜率，因胜率常饱和至 1.00 无法区分算法差异。论文未提供代码 URL，但基于 PyMARL2 实现，超参数针对每种方法单独调优。所有结果基于五次独立运行的均值和 95% 置信区间，但原文未报告具体置信区间数值。

## 关联研究分析

从问题动机看，POW 与 WQMIX 直接对标，但解决了后者启发式加权的根本缺陷。WQMIX 的理论承诺是加权训练使 $Q_{tot}$ 逼近 $Q^*$，但 CW-QMIX 和 OW-QMIX 的近似导致权重错位。POW 通过 $Q_r$ 显式估计联合动作价值，使权重分配基于真实价值而非启发式规则。这一差异源于任务特性：在非单调环境中，$Q_{tot}$ 的单调性约束使其无法正确评估次优动作，而 $Q_r$ 的非单调结构能准确区分动作价值。相比之下，MAGIC（Yu et al., 2026）通过因果影响模块量化动作对队友未来状态的影响，解决稀疏奖励下的协调信号缺失，但 MAGIC 聚焦于信用分配的时序维度，而 POW 聚焦于动作空间的离散维度。两者均试图超越简单团队奖励共享，但 MAGIC 依赖前瞻模型滚动，计算开销随时间步增长，而 POW 的 $Q_r$ 开销仅与联合动作空间大小相关。

从方法设计看，POW 与 QPLEX 同属 CTDE 价值分解框架，但 QPLEX 通过 Dueling 结构增强 $Q_{tot}$ 的表达力，而 POW 通过外部识别模块 $Q_r$ 实现加权。QPLEX 的 Dueling 结构将价值函数分解为状态价值和动作优势，提升了对状态依赖的建模能力，但仍未解决单调性约束下的最优策略恢复问题。POW 的 $Q_r$ 设计借鉴了 QPLEX 的 Dueling 思想，但将其应用于识别模块而非 $Q_{tot}$ 本身，从而解耦了表达力增强与最优性保证。这一设计选择暗示，单纯增强 $Q_{tot}$ 的表达力不足以解决非单调环境下的策略恢复问题，需要独立的价值估计器来指导训练权重。

## 总结

本文要解决的核心矛盾是价值分解方法中单调性约束与最优策略恢复之间的冲突。现有方法如 CW-QMIX 和 OW-QMIX 采用启发式加权，但无法保证权重与真实最优动作集对齐。本文抓住的切入点是，通过引入显式条件化于状态和联合动作的识别模块 $Q_r$，替代启发式近似，从而在理论上保证候选集收敛至真实最优集。本文做了什么：提出 POW 框架，通过迭代加权训练使 $Q_{tot}$ 恢复最优策略。证明了什么：在捕食者-猎物任务中，POW-QMIX 测试回报达到 40，而 QMIX 和 ResQ 均为 0；在 SMAC 3s_vs_5z 中，POW-QMIX 胜率为 1.00，优于 QPLEX 的 0.00。本文的边界在于，实验仅在离散动作空间验证，$Q_r$ 的超网络参数量随智能体数增长，在大规模连续动作空间中的计算开销和可扩展性未验证。当智能体数量增加至 20 以上时，$Q_r$ 的联合动作条件化输入维度是否导致训练不稳定，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_40179853)