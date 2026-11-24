# ICLR2026最新论文 ｜PENG’S Q( _λ_ ) FOR CONSERVATIVE VALUE ESTIMATION IN OFFLINE REINFORCEMENT LEARNING ｜保守彭氏Q(λ)离线强化学习

研究机构：韩国首尔大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_33348728)

> 离线强化学习（Offline RL）的核心困境在于分布偏移导致的Q值过估计与保守正则化引发的过悲观估计相互纠缠。现有单步Bellman算子方法难以同时缓解这两者，而多步算子在离线场景下的理论可行性长期存疑。本文提出保守彭氏Q(λ)（Conservative Peng’s Q(λ), CPQL），将彭氏Q(λ)算子嵌入保守价值估计框架，利用离线轨迹的多步信息隐式正则化策略。该方法在D4RL基准上超越了主流单步基线，但其理论保证仍依赖固定行为策略假设，且在部分可观测或重尾分布场景下的鲁棒性未经验证。

## 研究背景

当智能体在静态数据集中学习策略时，其生成的状态-动作分布往往偏离行为策略的覆盖范围，即分布偏移。这种偏移导致值函数在未见过的动作上产生外推误差，进而引发Q值过估计。为抑制过估计，保守Q学习（Conservative Q-Learning, CQL）通过惩罚OOD动作的Q值来约束策略，但过度的惩罚导致了对数据内动作的过悲观估计，限制了策略的探索能力。

离线RL的主流路线分为保守正则化、策略约束与不确定性量化三类。CQL及其变体（如IQL, Cal-QL）通过调整惩罚强度或引入隐式Q学习来平衡保守性与探索，但均依赖单步TD更新，未能充分利用离线数据中固有的多步轨迹信息。在线RL中，彭氏Q(λ)（Peng’s Q(λ), PQL）算子已被证明能加速收敛并提升性能，但其固定点性质在离线场景下的理论适配性此前未被研究。本文切入点在于：PQL算子的固定点更接近行为策略的值函数，这种隐式行为正则化特性恰好能缓解CQL的过悲观问题，且无需额外估计行为策略。

## 核心方法

### 方法参照系

本文问题属于离线RL中的保守价值估计类别，标准流程为：基于CQL框架，使用单步Bellman算子更新Q函数，并添加log-sum-exp惩罚项抑制OOD动作。本文的关键差异在于将单步Bellman算子替换为多步PQL算子，从而在价值更新中引入轨迹级信息。

### PQL算子的离线适配

PQL算子 $T_{\lambda}^{\pi_\beta, \pi}$ 定义为 $(1-\lambda)\sum_{n=1}^{\infty} \lambda^{n-1} T_{\pi_\beta, \pi}^n Q$，其中 $T_{\pi_\beta, \pi}^n$ 是未校正的n步回报算子。在离线设置中，行为策略 $\pi_\beta$ 固定为数据集的实证策略 $\hat{\pi}_\beta$。PQL的固定点 $Q^{\lambda\hat{\pi}_\beta + (1-\lambda)\pi}$ 是行为策略与目标策略的混合策略值函数，其收缩率为 $\beta = \frac{\gamma(1-\gamma\lambda)}{1-\gamma\lambda}$。这一设计动机在于：通过 $\lambda$ 参数将固定点拉近行为策略值函数，隐式引入行为正则化，从而在无需额外网络的情况下缓解CQL的过悲观。

### 保守PQL算法

CPQL将PQL算子嵌入CQL损失函数，Q值更新规则为 $Q_{k+1} = T_{\lambda}^{\hat{\pi}_\beta, \pi_k} Q_k$，其中 $\pi_k$ 是 $Q_k$ 的贪心策略。损失函数包含两项：$\alpha \mathbb{E}_{s \sim D} \log \mathbb{E}_{a \sim \pi_\phi(\cdot|s)} e^{Q_{\theta_j}(s,a)} - \mathbb{E}_{a \sim \hat{\pi}_\beta(\cdot|s)} Q_{\theta_j}(s,a)$ 和 $\frac{1}{2}\mathbb{E}_{s,a,s' \sim D} (Q_{\theta_j}(s,a) - y)^2$，其中目标值 $y = \min_{j=1,2} Q_{\theta_j^-} - \gamma^n \alpha_{td} \log \pi_\phi(\cdot|s_n)$。该设计通过多步轨迹计算目标值，减少了单步更新中OOD动作的累积误差，同时保留了CQL的保守惩罚机制。

## 实验评估

实验在D4RL基准上进行，涵盖MuJoCo、Adroit和AntMaze任务，所有算法训练1M梯度步。基线包括CQL、IQL、TD3+BC、BC、MCQ、MISA、CSVE和EPQ，覆盖了保守正则化、隐式Q学习和策略约束等主要路线，但未对比FORE或Q-MMR等无Bellman完备性依赖的OPE方法。

| 任务 | CQL | IQL | CPQL |
|---|---|---|---|
| halfcheetah-medium | 47.0* | 47.4 | 66.6±0.9 |
| hopper-medium | 53.0* | 66.2 | 99.7±2.0 |
| walker2d-medium | 73.3* | 78.3 | 90.0±1.5 |
| halfcheetah-medium-expert | 75.6* | 86.7 | 95.3±0.6 |
| hopper-medium-expert | 105.6* | 91.5 | 111.3±1.2 |
| walker2d-medium-expert | 107.9* | 109.6 | 112.9±2.0 |

CPQL在MuJoCo运动任务上全面超越CQL和IQL，尤其在medium-expert数据集上表现突出。消融实验显示，CPQL对保守参数 $\alpha$ 的敏感性显著低于CQL，在 $\alpha=0.1$ 时仍能保持高性能，而CQL在相同参数下性能急剧下降。

| 算子 | halfcheetah-random | hopper-medium | walker2d-medium-replay |
|---|---|---|---|
| CPQL | 38.8±1.0 | 99.7±2.0 | 97.4±4.0 |
| CQL w/ N-step | - | - | - |
| CQL w/ Retrace | - | - | - |
| CQL w/ Tree-backup | - | - | - |

注：原文未提供CQL w/ N-step、Retrace和Tree-backup的具体数值，仅定性描述其性能在早期峰值后下降。

评估边界方面，论文未报告计算效率的详细对比，仅指出CPQL的运行时比CQL增加4.4%。代码已开源，超参数设置完整，但缺乏对部分可观测或重尾分布场景的测试。

## 关联研究分析

从问题动机看，CPQL与IQL（Kostrikov et al., 2021）均旨在缓解CQL的过悲观，但IQL通过隐式Q学习避免查询OOD动作，而CPQL通过多步算子隐式正则化。IQL的优势在于无需显式惩罚项，但CPQL在多步轨迹信息利用上更直接，且对 $\alpha$ 的鲁棒性更强。这一差异源于任务特性：IQL假设数据覆盖充分，而CPQL通过轨迹级信息弥补覆盖不足。

从方法设计看，CPQL与Retrace（Munos et al., 2016）均使用多步算子，但Retrace依赖行为策略估计，而CPQL使用固定实证策略。Retrace在离线场景中因行为策略估计不准导致性能下降，而CPQL避免了这一问题。这一差异暗示了离线RL中行为策略估计的必要性存疑，固定策略的多步算子可能更稳定。

## 总结

CPQL解决的核心矛盾是离线RL中分布偏移导致的Q值过估计与保守正则化引发的过悲观估计之间的权衡。其切入点在于利用PQL算子固定点接近行为策略值函数的特性，隐式引入行为正则化，从而在无需额外估计行为策略的情况下缓解过悲观。方法上，CPQL将PQL算子嵌入CQL框架，通过多步轨迹计算目标值。实验证明，CPQL在D4RL基准上超越了CQL和IQL，尤其在medium-expert数据集上表现突出，且对保守参数 $\alpha$ 的敏感性显著降低。其边界在于理论保证依赖固定行为策略假设，且在部分可观测或重尾分布场景下的鲁棒性未经验证。当行为策略未知或数据覆盖极度稀疏时，PQL算子的固定点性质是否仍能维持稳定的价值估计，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_33348728)