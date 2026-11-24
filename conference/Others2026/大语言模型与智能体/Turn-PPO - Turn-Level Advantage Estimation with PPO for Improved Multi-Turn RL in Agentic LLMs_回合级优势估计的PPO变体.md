# EACL2026最新论文 ｜Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs ｜回合级优势估计的PPO变体

研究机构：美国德克萨斯大学奥斯汀分校

作者：Junbo Li、Peng Zhou、Rui Meng 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.17008)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.17008)

> 多轮智能体强化学习（Agentic RL）面临的核心困境是：在长程交互中，稀疏且延迟的奖励信号难以准确归因到具体的决策步骤，导致策略优化陷入不稳定甚至崩溃。当前主流算法组相对策略优化（Group Relative Policy Optimization, GRPO）因依赖采样均值估计优势，在高方差的多轮环境中表现脆弱，而传统近端策略优化（Proximal Policy Optimization, PPO）若沿用Token级建模，则因状态转移不连续导致Critic学习失效。本文通过重构马尔可夫决策过程（Markov Decision Process, MDP）的粒度，将状态-动作对从Token级提升至Turn级，提出Turn-PPO，利用可学习Critic在回合边界进行价值估计，从而获得更稳定的优势信号。该方案在防止训练崩溃方面表现出显著优势，但其绝对性能仍远低于多智能体协作方法，且对模型推理长度的敏感性揭示了其泛化边界的模糊性。

## 研究背景

多轮交互中，智能体需根据环境反馈动态调整策略，这一过程天然构成部分可观测马尔可夫决策过程（Partially Observable Markov Decision Process, POMDP）。然而，现有RL算法多继承自单轮推理场景，将每个Token视为独立动作，这种Token-MDP假设在多轮场景中失效：环境注入的外部Token导致状态转移呈现“块状”跳跃，而非Token级的平滑递进。这种状态表示错位使得Critic难以准确回归状态价值，进而污染优势估计，引发策略更新中的梯度噪声与熵坍缩。

GRPO作为DeepSeek-R1等模型的核心训练算法，通过移除Critic网络、采用组内相对优势估计来降低计算开销，成为当前Agentic RL的主流范式。然而，在多轮任务中，GRPO将轨迹级奖励均匀分配给所有Token，忽视了不同Turn对最终奖励贡献度的差异，且采样优势估计在高方差环境下波动剧烈，导致训练频繁崩溃。尽管GiGPO、MT-GRPO等工作尝试引入Turn级信用分配，但它们往往依赖特定场景的手动权重调优，缺乏通用性。本文切入点在于：重新审视PPO在多轮场景中的适用性，指出Token-MDP是Critic学习失效的根源，并通过Turn-MDP重构解决状态表示错位问题，无需额外调参即可实现稳定的优势估计。

## 核心方法

### 方法参照系

本文问题属于算法稳定性与信用分配机制的交叉领域。标准PPO流程包含Actor策略更新与Critic价值估计，通过广义优势估计（Generalized Advantage Estimation, GAE）计算优势。本文与通用PPO的关键差异在于MDP的状态-动作定义粒度：传统实现将每个Token视为独立步骤，而本文将其重构为以Turn为单位的离散决策单元，从而改变Critic的输入空间与优势计算逻辑。

### Turn-MDP状态重构

设计动机在于解决Token-MDP中环境Token注入导致的状态转移不连续问题，该问题使Critic回归目标模糊，无法区分“模型生成Token”与“环境反馈Token”的价值差异。在Turn-MDP中，状态 $s_n$ 定义为截至第 $n-1$ 轮的所有交互历史与第 $n$ 轮查询 $Q_n$ 的拼接，动作 $a_n$ 定义为第 $n$ 轮LLM生成的完整响应 $R_n$。这种定义使得状态转移在Turn边界处保持均匀性：每个 $s_n$ 都是完整历史加当前查询，每个 $a_n$ 都是对该查询的完整响应。Critic仅在Turn边界（即 $Q_n$ 末尾或 $R_n$ 末尾）输出价值 $V_n$，避免了在Token级混合序列上的回归噪声。

$$
s_n := \left( \bigoplus_{n'<n} (Q_{n'}, R_{n'}) \right) \oplus Q_n, \quad a_n := R_n
$$

该公式表明，Turn-MDP将多轮交互离散化为 $N$ 个独立的决策步骤，每个步骤的状态包含全部历史上下文，动作是完整的自然语言响应。这种重构使得Critic的学习目标从“预测下一个Token的价值”转变为“预测当前回合结束时的累积回报”，与任务结构（回合制交互）对齐，从而提升价值估计的保真度。

### Turn级优势估计与裁剪

设计动机在于解决GRPO中均匀优势分配导致的优化偏差，以及Token-PPO中Token级裁剪无法有效约束回合内策略剧烈变化的问题。Turn-PPO采用Turn级GAE计算优势，中间回合的优势为 $\gamma V_{n+1} - V_n$，最终回合为 $r - V_N$，其中 $\gamma$ 为折扣因子。与Token-PPO不同，裁剪操作在Turn级执行：若策略分布变化过大，整个回合的响应被裁剪，而非仅裁剪单个Token。

$$
\hat{A}_{n} = \begin{cases} \gamma V_{n+1} - V_n & n < N \\ r - V_N & n = N \end{cases}
$$

该公式表明，优势估计在Turn粒度上进行，Critic的价值预测 $V_n$ 仅依赖于回合边界的状态。Turn级裁剪机制通过限制整个回合的策略更新幅度，防止模型在单个回合内发生剧烈偏移，从而避免不稳定梯度步骤。这一设计在保持PPO稳定性的同时，消除了Token级裁剪在多轮场景中因粒度不匹配导致的优化低效问题。

## 实验评估

实验在WebShop与Sokoban两个多轮文本环境中进行，基线模型包括Qwen2.5-3B、Qwen2.5-7B及Qwen3-1.7B（开启/关闭推理）。对比方法涵盖GRPO、Token-PPO及GRPO变体（移除标准差、移除KL、增强多样性）。基线覆盖审计显示，本文未对比Tree-GRPO、SLEA-RL等最新SOTA方法，也未包含多智能体协作框架，限制了性能上限的评估。

| 环境 | 模型 | GRPO | Token-PPO | Turn-PPO |
| :--- | :--- | :--- | :--- | :--- |
| WebShop | Qwen2.5-3B | 0.72 | 0.73 | **0.75** |
| WebShop | Qwen3-1.7B (no think) | 0.78 | 0.77 | **0.80** |
| Sokoban | Qwen3-1.7B (think) | Crash | 0.54 | **0.55** |
| Sokoban | Qwen2.5-3B | Crash | 1.93 | **2.29** |
| Sokoban | Qwen2.5-7B | Crash | 2.90 | **3.74** |

Turn-PPO在所有未崩溃配置中均取得最高奖励，尤其在Sokoban任务中，Qwen2.5-7B的奖励从Token-PPO的2.90提升至3.74，增幅达28.97%。GRPO在Qwen3开启推理时频繁崩溃，而Turn-PPO稳定收敛，验证了Turn级Critic对高方差环境的鲁棒性。

消融实验聚焦于GRPO失败模式与PPO超参数。移除GRPO中的标准差项、KL项或增强批次多样性均未能防止崩溃，表明这些修改无法解决采样优势估计的根本方差问题。PPO中Actor与Critic的学习率敏感性较高，但论文未提供具体数值对比，仅指出Turn-PPO在Qwen3长推理场景下需更精细的超参数调优。

评估边界方面，本文仅使用文本环境，未涉及GUI或具身智能体场景，限制了结论的普适性。指标仅报告平均奖励，未提供成功率或置信区间，难以区分性能提升的统计显著性。代码基于RAGEN框架实现，但论文未提供独立代码库，超参数细节（如学习率、批大小）未在正文中完整披露，可复现性依赖附录或社区实现。

## 关联研究分析

从问题动机看，本文与GiGPO、MT-GRPO同属Turn级信用分配路线，但差异在于优势估计机制。GiGPO通过合并相同状态获取状态级优势，MT-GRPO依赖手动调优的Turn级权重，而Turn-PPO采用可学习Critic自动估计价值，避免了人工干预的偏差。这一差异源于任务特性：GiGPO适用于状态可精确匹配的环境（如Sokoban），而Turn-PPO更适用于状态连续变化、难以离散化的场景（如WebShop）。然而，Turn-PPO的Critic开销是否抵消了稳定性收益，论文未提供计算效率对比，这一盲区在多轮长轨迹场景中可能成为实际部署的瓶颈。

从方法设计看，本文与ArCHer同属层级RL思想，但ArCHer在Turn级使用Actor-Critic、Token级使用策略梯度，而Turn-PPO将Actor与Critic均提升至Turn级，简化了优化过程。这一简化牺牲了Token级控制的灵活性，但换来了Critic学习的稳定性。与GRPO相比，Turn-PPO重新引入了Critic网络，挑战了GRPO“无需Critic”的主流范式。这一冲突暗示：在多轮高方差环境中，采样优势估计的方差可能超过Critic引入的偏差，使得可学习价值函数更具优势。但Turn-PPO在WebShop上的0.75奖励远低于Stronger-MAS的99.5%成功率（据领域综述），表明单智能体算法在复杂协作任务中存在性能天花板，Turn-PPO的稳定性优势尚未转化为绝对性能领先。

## 总结

本文要解决的核心矛盾是多轮Agentic RL中GRPO采样优势估计的高方差与Token-MDP状态表示错位导致的训练崩溃。现有方法要么依赖手动调优的Turn级权重（如MT-GRPO），要么在Token级Critic学习中受困于状态转移不连续，而本文通过Turn-MDP重构与Turn级Critic，将优势估计与任务结构对齐，从而在无需额外调参的情况下实现稳定收敛。Turn-PPO在Sokoban任务中将Qwen2.5-7B的奖励从2.90提升至3.74，并在Qwen3长推理场景中避免了GRPO的崩溃，证明了Turn级粒度对稳定性的关键作用。然而，本文的边界在于：仅验证了单智能体文本环境，未评估多智能体协作场景，且Qwen3开启推理时性能仍低于关闭推理设置，暗示模型推理分布与任务结构的匹配度可能比算法稳定性更关键。当Turn-PPO应用于状态高度动态、Turn边界模糊的环境（如实时对话）时，Turn级Critic的价值估计是否仍能保持保真度，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.17008)