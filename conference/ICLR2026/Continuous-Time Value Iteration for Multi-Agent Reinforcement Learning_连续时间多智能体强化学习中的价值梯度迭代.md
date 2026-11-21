# ICLR2026最新论文 ｜Continuous-Time Value Iteration for Multi-Agent Reinforcement Learning ｜连续时间多智能体强化学习中的价值梯度迭代

研究机构：美国普渡大学

作者：Xuefeng Wang、Lei Zhang、Henglin Pu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.09135)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.09135)

> 合作型多智能体强化学习（Cooperative Multi-Agent Reinforcement Learning, MARL）在离散时间框架下已趋于成熟，但真实物理系统往往以高频或连续时间运行，离散化步长导致控制不平滑或计算爆炸。现有连续时间强化学习（Continuous-Time Reinforcement Learning, CTRL）方法多局限于单智能体，且基于物理信息神经网络（Physics-Informed Neural Networks, PINNs）的求解器在耦合动态下易产生价值梯度偏差，破坏策略优化。本文提出 Value Iteration via PINN (VIP) 框架，通过引入价值梯度迭代（Value Gradient Iteration, VGI）模块，沿轨迹显式修正价值梯度，确保微分价值函数与哈密顿-雅可比-贝尔曼（Hamilton-Jacobi-Bellman, HJB）方程的一致性。该工作填补了连续时间合作 MARL 的价值学习空白，但其对确定性系统的依赖及缺乏显式通信机制，限制了其在部分可观测环境中的直接应用。

## 研究背景

当智能体在连续时间域中交互时，离散时间强化学习（Discrete-Time Reinforcement Learning, DTRL）依赖固定时间步 $\Delta t$ 进行贝尔曼更新。若 $\Delta t$ 过大，控制器动作不平滑导致次优；若 $\Delta t$ 趋近于零，贝尔曼算子病态化，时间差分目标被近似噪声主导，引发高方差与不稳定。这一困境促使研究转向 CTRL，其核心是用 HJB 偏微分方程（Partial Differential Equation, PDE）替代贝尔曼递归，直接学习微分价值函数。然而，高维状态空间下的 HJB 求解面临维数灾难（Curse of Dimensionality, CoD），传统数值方法失效。

PINNs 通过最小化 PDE 残差近似价值函数，缓解了 CoD，但现有 CTRL 研究几乎全集中于单智能体。在合作 MARL 中，智能体间的耦合动态放大了近似误差，导致 PDE 残差损失无法保证价值梯度的准确性。错误的价值梯度直接污染策略梯度，使去中心化执行下的协调失败。尽管集中训练去中心化执行（Centralized Training with Decentralized Execution, CTDE）范式在离散 MARL 中确立了非平稳性缓解的标准，但在连续时间下，如何构建既满足 HJB 物理约束又具备精确梯度的集中式评论家，仍是未被解决的瓶颈。

## 核心方法

### 连续时间 CTDE 架构与 HJB 评论家

VIP 框架沿用 CTDE 范式，但将评论家从离散时间价值网络替换为基于 PINNs 的微分价值网络 $V_\theta(x)$。在离散 MARL 中，评论家通常通过时序差分误差更新；而在 VIP 中，评论家通过最小化 HJB PDE 残差进行训练。对于 $N$ 个智能体的合作系统，全局状态 $x$ 和联合动作 $u$ 遵循动力学 $\dot{x} = f(x, u)$。最优价值函数 $V(x)$ 满足 HJB 方程：

$$
\rho V(x) = \max_{u \in \mathcal{U}} \left( \nabla_x V(x)^\top f(x, u) + r(x, u) \right)
$$

其中 $\rho$ 为折扣因子，$r$ 为全局奖励。该公式的物理含义是：在最优策略下，价值函数的时间变化率（由梯度和动力学决定）加上瞬时奖励，等于折扣后的价值本身。VIP 通过定义 HJB 残差 $R_\theta(x_t)$ 作为损失函数的一部分，强制神经网络逼近该偏微分方程的粘性解。这一设计将价值学习从离散的时间步跳跃转化为连续空间中的物理约束满足问题，消除了离散化步长带来的偏差。

### 价值梯度迭代（VGI）模块

仅依靠 HJB 残差损失无法保证价值梯度 $\nabla_x V(x)$ 的准确性，尤其在多智能体耦合动态下，微小的梯度误差会被放大。VIP 引入 VGI 模块，沿采样轨迹显式迭代修正价值梯度。VGI 估计器 $\hat{g}_t$ 定义为：

$$
\hat{g}_t = \nabla_{x_t} r_\phi(x_t, u_t) \Delta t + e^{-\rho \Delta t} \nabla_{x_t} f_\psi(x_t, u_t)^\top \nabla_{x_{t+\Delta t}} V_\theta(x_{t+\Delta t})
$$

其中 $f_\psi$ 和 $r_\phi$ 分别为学习到的动力学模型和奖励模型。该公式是贝尔曼方程在梯度空间的一步展开：第一项捕捉局部奖励梯度的瞬时贡献，第二项通过动力学雅可比矩阵传播下游价值信息。VGI 损失 $\mathcal{L}_{VGI}$ 最小化自动微分得到的梯度 $\nabla_{x_t} V_\theta(x_t)$ 与目标 $\hat{g}_t$ 之间的均方误差。这一机制提供了轨迹对齐的修正信号，补充了全局 PDE 约束，确保评论家不仅满足方程形式，更具备精确的局部梯度结构，从而为策略更新提供低方差、高准确度的优势函数。

### 连续时间优势函数与策略优化

基于修正后的价值梯度，VIP 推导连续时间瞬时优势函数用于去中心化策略更新。不同于离散 MARL 中基于 $Q(s,a) - V(s)$ 的优势估计，VIP 利用 HJB 残差直接构造优势信号。对于智能体 $i$，其策略 $\pi_{\phi_i}$ 通过最大化期望优势进行更新：

$$
\mathcal{L}_p = - \mathbb{E}_{u \sim \pi_\phi} \left[ R_\theta(x_t) \right]
$$

其中 $R_\theta(x_t)$ 为 HJB 残差。该公式表明，策略优化的方向直接由价值函数偏离 HJB 最优条件的程度决定。当残差为零时，策略达到连续时间最优。这种设计将策略梯度与物理约束的违反程度直接挂钩，避免了离散时间中因时间步离散化导致的优势估计偏差，使去中心化执行下的动作选择与连续时间最优性条件保持一致。

## 实验评估

实验在连续时间版本的 MPE（Multi-Agent Particle Environment）和 MuJoCo 基准上进行，对比了 CT-MBRL (ODE)、Differential Policy Iteration (DPI)、Integral Policy Iteration (IPI) 和 HJBPPO 等 CTRL 基线。由于知识库中缺乏连续时间 MARL 的 SOTA 数值，且论文正文未提供具体表格数据，此处无法列出精确数值表格。定性结果显示，VIP 在所有任务中收敛最快且最终累积回报最高。消融实验表明，移除 VGI 模块导致累积回报显著下降，证实了价值梯度一致性对策略学习的关键作用。

在评估边界方面，实验仅覆盖确定性系统，未涉及随机动力学或对抗环境。基线选择局限于 CTRL 方法，未与离散时间 SOTA（如 MAPPO）在连续时间域进行直接对比，仅在 Didactic 示例中提及 MADDPG 的离散化误差。此外，论文未报告置信区间，且未评估通信带宽受限下的性能，这与离散 MARL 中强调通信效率的共识形成差异。

## 关联研究分析

从问题动机看，VIP 与 HJBPPO（Mukherjee & Liu）同属 PINN+RL 路线，但 HJBPPO 仅依赖 PDE 残差损失，在多智能体耦合动态下易产生梯度偏差。VIP 通过 VGI 模块显式约束梯度，解决了 HJBPPO 在高维系统中价值近似不准确的问题。这一差异源于对“物理约束”理解的深化：HJBPPO 关注方程形式的满足，VIP 关注解的局部几何结构（梯度）的准确性。

从方法设计看，VIP 与 MADDPG（Lowe et al., 2017）共享 CTDE 架构，但 MADDPG 依赖离散时间贝尔曼更新，在连续时间域存在固有偏差。VIP 用 HJB PDE 替代贝尔曼递归，消除了离散化误差。然而，MADDPG 等离散方法通常结合注意力机制或通信协议处理部分可观测性，而 VIP 依赖全局状态（CTDE）和动力学模型，未显式建模通信。这暗示 VIP 在部分可观测环境中的协调机制可能弱于显式通信方法，其有效性高度依赖动力学模型的准确性。

## 总结

VIP 针对连续时间合作 MARL 中 HJB 方程求解的梯度偏差问题，提出结合 PINNs 与 VGI 的框架，通过轨迹级梯度迭代确保价值函数与微分结构的一致性。实验表明 VIP 在连续时间 MPE 和 MuJoCo 上收敛最快且回报最高，消融证实 VGI 的关键作用。然而，该方法局限于确定性系统，且未处理部分可观测性下的通信瓶颈。当动力学模型存在误差或环境具有随机性时，VGI 的梯度修正是否仍能保持鲁棒性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.09135)