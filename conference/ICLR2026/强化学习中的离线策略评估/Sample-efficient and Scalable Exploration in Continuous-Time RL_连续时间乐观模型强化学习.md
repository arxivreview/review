# ICLR2026最新论文 ｜Sample-efficient and Scalable Exploration in Continuous-Time RL ｜连续时间乐观模型强化学习

作者：Klemens Iten、Lenart Treven、Bhavya Sukhija 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.24482)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.24482)

> 连续时间控制系统的动力学建模与策略优化长期受限于离散化带来的时间行为模糊与计算开销。现有连续时间强化学习方法要么仅依赖外部奖励导致探索不足，要么通过联合优化策略与动力学实现乐观性但计算复杂度随维度指数增长。COMBRL 通过引入内在奖励机制，将模型认知不确定性直接转化为探索驱动力，实现了奖励与探索的解耦平衡。该方法在理论上证明了亚线性后悔界，在实验中展示了优于基线的样本效率，但其理论保证依赖于高斯过程等特定概率模型的良校准假设，在真实物理系统中的鲁棒性尚待检验。

## 研究背景

连续时间强化学习（Continuous-Time Reinforcement Learning, CT-RL）要求智能体在连续时间轴上决定何时观测与控制，而非固定步长。这一特性使得不确定性不再局限于离散状态点，而是沿整个轨迹累积，导致后悔值不仅取决于策略，还取决于测量选择策略（Measurement Selection Strategy, MSS）。若 MSS 采样密度不足，模型对动力学方程的估计误差将随时间积分放大，直接限制策略性能的上界。

传统离散时间模型强化学习（Model-Based Reinforcement Learning, MBRL）如 PETS 依赖固定网格上的不确定性估计，无法捕捉连续时间系统中的关键瞬态行为。针对连续时间场景，Treven et al. (2023) 提出的 OCORL 通过联合优化策略与可信动力学集合来强制乐观性，但该优化问题在高维状态空间中不可解，且仅适用于存在外部奖励的任务。当面临无监督系统辨识或需要全局动力学建模的场景时，缺乏外部奖励信号使得上述方法失效，亟需一种既能平衡任务奖励与模型探索，又能避免高维联合优化计算瓶颈的算法。

## 核心方法

### 方法参照系

连续时间 MBRL 的标准流程是在每个回合中，基于历史数据更新动力学模型，并求解最优控制问题以生成策略。本文问题与该通用流程的关键差异在于：传统方法将探索视为对动力学参数的隐式优化，而 COMBRL 将探索显式化为对模型认知不确定性的最大化，从而将策略优化与模型学习解耦。

### 内在奖励驱动的乐观规划

COMBRL 的核心创新在于将乐观性原则转化为一个标量加权目标函数，而非对可信动力学集合的联合优化。在每回合 $n$，算法从上一回合的置信集 $\mathcal{M}_{n-1}$ 中选取任意一个 $L_f$-Lipschitz 连续模型 $\mathbf{f}_n$（实践中通常使用均值模型 $\boldsymbol{\mu}_n$），并求解如下优化问题：

$$
\boldsymbol{\pi}_n = \arg\max_{\boldsymbol{\pi} \in \Pi} \mathbb{E}_{\boldsymbol{\pi}, \mathbf{f}_n} \left[ \int_0^T \left( r(\mathbf{x}(t), \mathbf{u}(t)) + \lambda_n \boldsymbol{\sigma}_{n-1}(\mathbf{z}(t)) \right) dt \right]
$$

其中 $\boldsymbol{\sigma}_{n-1}(\mathbf{z}(t))$ 是模型在状态-动作空间 $\mathbf{z}(t)$ 处的认知不确定性，$\lambda_n$ 是平衡探索与利用的超参数。这一设计解决了 OCORL 中因联合优化导致的维度灾难问题：通过固定模型 $\mathbf{f}_n$ 并仅优化策略 $\boldsymbol{\pi}_n$，计算复杂度从对动力学函数的优化降维至对策略函数的优化，使得算法可扩展至高维像素控制等场景。$\lambda_n$ 的取值决定了算法行为：$\lambda_n=0$ 退化为纯利用，$\lambda_n \to \infty$ 则转化为无监督主动学习，引导智能体访问模型最不确定区域。

### 基于测量选择策略的后悔界

COMBRL 的理论保证依赖于模型复杂度 $I_N(\mathbf{f}^*, \mathcal{S})$，该量定义为轨迹上认知不确定性的积分：

$$
I_N(\mathbf{f}^*, \mathcal{S}) = \int_0^T \boldsymbol{\sigma}_{N-1}(\mathbf{z}(t)) dt
$$

与离散时间中不确定性在固定网格上的求和不同，连续时间模型复杂度需沿轨迹积分，且其收敛速率由 MSS $\mathcal{S}$ 的采样密度决定。定理 1 表明，在 Lipschitz 连续性与良校准假设下，COMBRL 的累计后悔 $R_N$ 以概率至少 $1-\delta$ 被 $O(\sqrt{N I_N})$ 界住。对于高斯过程（GP）动力学，若采用等距 MSS 且 $|\mathcal{S}_n|=n$，模型复杂度以 $\text{polylog}(N)$ 增长，从而保证亚线性后悔。这一结果揭示了连续时间 RL 中测量调度与学习性能的内在联系：要竞争最优策略，MSS 必须随回合数增加采样密度，否则不确定性积分无法快速衰减。

## 实验评估

实验在 OpenAI/Farama Gymnasium 与 DeepMind Control Suite 上进行，对比基线包括 PETS（离散时间 MBRL）、OCORL（连续时间乐观 MBRL）及 MPC（真动力学最优控制）。基线覆盖了离散/连续时间、有/无外部奖励的主要路线，但缺失了基于贝叶斯神经网络（BNN）的连续时间基线，且未对比其他主动学习策略。

| 环境 | 任务 | 方法 | 归一化回报 |
| :--- | :--- | :--- | :--- |
| Pendulum-GP | Swing-up | COMBRL | 1.0 |
| Pendulum-GP | Swing-up | MPC (true dynamics) | 1.0 |
| Pendulum-GP | Swing-up | OCORL | 0.5 |
| Pendulum-GP | Swing-up | PETS | 0.0 |
| Mountaincar-GP | Go up | COMBRL | 1.0 |
| Mountaincar-GP | Go up | MPC (true dynamics) | 1.0 |
| Mountaincar-GP | Go up | OCORL | 0.5 |
| Mountaincar-GP | Go up | PETS | 0.0 |

在 Pendulum-GP 与 Mountaincar-GP 任务中，COMBRL 达到 1.0 的归一化回报，与使用真动力学的 MPC 持平，显著优于 OCORL（0.5）和 PETS（0.0）。这表明 COMBRL 在稀疏奖励环境中能有效利用内在奖励引导探索，快速收敛至最优策略。

消融实验显示，COMBRL 的无监督变体（$\lambda_n \to \infty$）在下游任务泛化上表现最佳，而平衡变体（$0 < \lambda_n < \infty$）在主任务性能上更优。这一结果验证了 $\lambda_n$ 作为探索-利用权衡杠杆的有效性：高 $\lambda_n$ 促进全局动力学建模，低 $\lambda_n$ 聚焦任务相关区域。然而，论文未报告不同 $\lambda_n$ 调度策略（静态、退火、自动调优）对最终性能的具体影响幅度，仅定性描述了其有效性。

评估边界方面，实验主要依赖 GP 动力学模型，未测试 BNN 或集成模型在连续时间下的表现，而 GP 的良校准假设在真实物理系统中可能因噪声非高斯性或模型误设而失效。代码已开源，但超参数 $\lambda_n$ 的选取依赖交叉验证，缺乏自动调优的默认配置，限制了其在未知环境中的即插即用能力。

## 关联研究分析

从问题动机看，COMBRL 与离线策略评估（OPE）中的双重稳健（Doubly Robust, DR）估计器存在深层结构相似性，但应用场景截然不同。DR 估计器通过结合直接方法与重要性采样，在离线数据中平衡偏差与方差，其核心假设是行为策略已知或价值函数正确。COMBRL 则通过内在奖励在线平衡探索与利用，其“偏差”体现为模型对动力学的外推误差，“方差”体现为认知不确定性。两者的关键差异在于：DR 依赖离线数据的覆盖假设（如集中性）来保证无偏性，而 COMBRL 依赖 MSS 的动态调整来保证模型复杂度的收敛。这种差异源于任务特性：OPE 是静态评估问题，数据分布固定；CT-RL 是动态学习问题，数据分布随策略演化。COMBRL 的 MSS 可视为 OPE 中覆盖假设的动态实现，但论文未探讨如何将 OPE 的样本复杂度理论迁移至连续时间在线设置。

从方法设计看，COMBRL 与离散时间内在动机方法如 RND（Random Network Distillation）共享“不确定性作为内在奖励”的核心思想，但连续时间设定引入了轨迹积分与测量调度的新维度。RND 在离散状态点上计算不确定性，而 COMBRL 需沿连续轨迹积分不确定性，这使得模型复杂度 $I_N$ 成为新的理论瓶颈。论文通过证明 $I_N$ 在 GP 下的亚线性增长解决了这一瓶颈，但未讨论当动力学具有长程依赖或非平稳特性时，MSS 的采样密度是否需进一步增加。这种对 MSS 的显式依赖是连续时间 RL 独有的挑战，离散时间方法无需考虑测量时机，因此无法直接借鉴其理论工具。

## 总结

COMBRL 旨在解决连续时间模型强化学习中探索不足与高维联合优化计算瓶颈的矛盾。现有方法如 OCORL 通过联合优化策略与动力学实现乐观性，但计算复杂度随维度指数增长，且无法处理无外部奖励场景。COMBRL 抓住“不确定性可显式转化为内在奖励”这一被忽略的点，通过标量 $\lambda_n$ 解耦探索与利用，避免了高维优化。该方法证明了在 GP 动力学下，基于 MSS 的亚线性后悔界，并在 Pendulum-GP 等任务中达到与真动力学 MPC 持平的 1.0 归一化回报。其边界在于理论保证依赖 GP 的良校准假设，且实验未覆盖 BNN 等更通用的概率模型。当真实物理系统的噪声偏离高斯分布或存在模型误设时，COMBRL 的内在奖励是否仍能引导有效探索，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.24482)