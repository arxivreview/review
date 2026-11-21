# HuggingFace最新推荐论文 ｜Multiscale Policy Optimization for Long-Horizon LLM Agents ｜多尺度策略优化

作者：Tao Ren、Hui Yang、Jia Deng 等 19 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.35013)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.35013)

> 长程大语言模型（Large Language Models, LLMs）智能体在稀疏奖励下难以将终端结果有效归因至中间决策，导致信用分配失效。现有强化学习（Reinforcement Learning, RL）方法割裂了宏观交互轮次与微观Token生成尺度，组相对方法无法区分轮内Token贡献，Token级方法则引入轮内分布偏移惩罚。MPO通过多尺度优势估计（Multiscale Advantage Estimation, MAE）在轮次间传播信用并在轮内细化Token权重，结合轮级重要性采样对齐策略更新。该框架在搜索与工具调用任务中显著优于单尺度基线，但其在开放域任务中的泛化边界及轮级比率对细粒度探索的潜在限制仍待验证。

## 研究背景

当LLM智能体执行长程任务时，其策略以Token为单位自回归生成动作，而环境反馈与奖励信号仅在完整的交互轮次（Turn）结束后产生。这种生成粒度与决策粒度的错位构成了信用分配的核心困境：终端奖励无法直接指导中间Token的优化，且不同轮次间的价值波动远大于轮内Token的价值波动。传统RL方法在此场景下暴露出结构性缺陷，组相对方法如GRPO（Group Relative Policy Optimization）为整个序列分配单一优势值，抹杀了轮内Token的相对贡献；而Token级方法如PPO（Proximal Policy Optimization）虽提供细粒度信用，却将每个Token视为独立动作，忽略了轮内分布偏移带来的额外偏差。

领域内主流路线在计算效率与信用精度之间做出了不同取舍。GRPO及其变体通过移除Critic网络降低开销，但牺牲了细粒度归因能力；PPO及其变体（如VAPO, SAO）依赖Critic估计Token级优势，但理论分析表明Token级代理在相同KL约束下会引入轮内分布偏移惩罚。MPO的切入点在于识别出“轮次”作为宏观决策单元与“Token”作为微观生成单元之间的尺度差异，提出在优势估计与重要性采样中分别对齐这两个尺度，以消除单尺度方法的固有偏差。

## 核心方法

### 方法参照系：轮次与Token的尺度错位

在Agentic RL中，智能体轨迹由交替的助手输出与环境观察组成。标准流程通常将完整输出或单个Token作为动作空间，导致优势估计与重要性采样在尺度上不一致。MPO将完整助手输出定义为宏观动作，保留历史上下文作为状态，从而在理论上建立轮次级改进界，并指出Token级代理因轮内分布偏移产生的额外代价。

### 多尺度优势估计（MAE）

MAE旨在解决终端奖励无法有效传播至中间Token的问题。传统GAE（Generalized Advantage Estimation）在Token级计算优势，导致信用衰减过快且受轮内长度影响。MPO首先在轮次级时间轴上应用GAE，利用边界值传播任务级信用，随后通过局部修正细化轮内Token权重。

轮次级优势计算如下：

$$ A^{turn}_t = \delta^{turn}_t + \lambda A^{turn}_{t+1} $$

其中 $\delta^{turn}_t$ 为轮次级TD残差，$\lambda$ 为衰减系数。该公式确保信用在交互边界间传播，而非在Token间快速衰减。

为保留轮内Token的相对差异，MPO引入局部追踪信号 $A^{intra}_{t,i}$，并通过约束投影将轮次级优势作为均值，局部信号作为偏差进行分配：

$$ A^{MAE}_{t,i} = A^{turn}_t + \beta (A^{intra}_{t,i} - \bar{A}^{intra}_t) $$

该公式通过中心化处理，确保轮内Token优势均值等于轮次级优势，同时保留局部信号中的相对差异，解决了直接相加导致均值偏移的问题。

### 轮级重要性采样与梯度隔离

在策略更新阶段，MPO采用轮级重要性比率以消除Token级代理的分布偏移惩罚，同时通过Stop-gradient机制保留Token级梯度。传统PPO使用Token级比率，导致轮内前缀分布不一致。MPO定义轮级比率 $\rho_t$ 与Token级比率 $\rho_{t,i}$，并构造如下估计量：

$$ \tilde{\rho}_{t,i}(\theta) = \rho_{t,i}(\theta) \cdot \text{sg}\left( \prod_{j \neq i} \rho_{t,j}(\theta) \right) $$

其中 $\text{sg}$ 表示停止梯度。该构造使得前向传播中每个Token受完整轮次比率约束，而反向传播中梯度仅通过当前Token比率计算，从而在保持轮级稳定性的同时实现Token级细粒度优化。

## 实验评估

实验在BrowseComp-Plus、GAIA、HLE等搜索与智能体基准上评估Qwen3-4B与Qwen3-30B-A3B模型。基线覆盖GRPO、PPO、VAPO、SAO等主流RL方法。MPO在9项指标上均取得最高分，相对最强基线在GAIA pass@1上提升3.85个百分点（4B模型）。

| 方法 | BrowseComp-Plus pass@1 | GAIA pass@1 | HLE pass@1 |
| :--- | :--- | :--- | :--- |
| PPO | 40.85 | 31.71 | 7.22 |
| VAPO | 43.23 | 33.91 | 7.54 |
| MPO (Ours) | 48.08 | 39.47 | 9.92 |

消融实验显示，轮级重要性采样对性能贡献显著。将轮级比率替换为Token级比率（MPO w/ token IS）导致GAIA pass@1下降3.12个百分点，验证了轮内分布偏移惩罚的存在。此外，局部修正强度 $\beta$ 在1.0时达到最优，过高或过低均导致性能下降，表明轮内信用分配需平衡局部差异与全局一致性。

评估边界方面，实验未覆盖Tree-GRPO等树搜索类方法，且未报告置信区间。测试时扩展（Test-time Scaling）分析表明，MPO在pass@32上仍保持优势，但低熵值伴随高性能的现象挑战了“熵坍缩即探索不足”的传统认知，提示需结合pass@k综合评估探索能力。

## 关联研究分析

从信用分配机制看，MPO与Tree-GRPO（Ji et al., 2025）均针对稀疏奖励下的细粒度归因，但路线不同。Tree-GRPO通过树搜索扩展采样空间，在分支节点进行信用分配；MPO则在单轨迹内通过MAE实现轮次与Token的尺度对齐。Tree-GRPO依赖额外的树结构计算开销，而MPO通过理论推导优化现有Critic架构，在计算效率上更具优势。然而，MPO未探索树结构在长程规划中的潜在增益，其在复杂分支决策任务中的表现尚不明确。

从算法稳定性看，MPO与ARLArena（Wang et al., 2026）均关注训练稳定性，但侧重点不同。ARLArena通过标准化测试环境揭示熵坍缩与推理模板化的联系，强调显式正则化；MPO则通过轮级重要性采样从理论上消除分布偏移，并观察到低熵与高性能共存的现象。这一冲突暗示，在Agentic RL中，熵可能并非探索能力的唯一指标，轮级对齐可能通过稳定价值估计间接维持了有效探索，而非依赖高熵。

## 总结

MPO针对长程LLM智能体中轮次与Token尺度错位导致的信用分配失效问题，提出多尺度优势估计与轮级重要性采样框架。通过MAE在轮次间传播信用并在轮内细化Token权重，结合轮级比率消除分布偏移，MPO在GAIA pass@1上较PPO提升7.76个百分点。该方法的边界在于其理论分析基于固定轮次假设，且实验未覆盖树搜索类基线，轮级比率是否限制长轮次内的细粒度探索仍待验证。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.35013)