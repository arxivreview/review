# HuggingFace最新推荐论文 ｜WorkRover: Scaling Long-Horizon Cowork Agent Training Via Recursive Environment Evolution ｜长程协作智能体训练中的递归环境演化与验证器接地信用分配

研究机构：复旦大学、华东师范大学

作者：Hang He、Linting Wang、Guanming Liu 等 17 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.18067)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.18067)

> 导读 长程协作智能体（Cowork Agent）在跨文件、工具与应用的复杂工作流中，面临环境构建缺陷与稀疏奖励归因困难的双重瓶颈。现有方法多假设环境已就绪，缺乏对上下文、任务与验证器之间语义对齐的递归修复机制，且终端奖励难以有效指导中间步骤优化。WorkRover 提出 Harness 驱动的环境合成与 Factorial Compatibility Replay (FCR) 递归演化机制，结合 Verifier-to-Turn Credit Assignment (VTCA) 将验证器状态检查转化为回合级优势信号。该框架在职业任务基准上显著超越基线，但其有效性高度依赖环境可验证性与确定性检查的覆盖范围。

## 研究背景

当智能体在包含文件、技能与应用环境的复杂工作空间中执行长程任务时，其决策依赖于对状态变化的精确追踪与跨工件的一致性维护。这一过程可形式化为部分可观测马尔可夫决策过程（Partially Observable Markov Decision Process, POMDP），其中动作空间扩展至自然语言与外部 API 调用，状态空间受限于上下文窗口。然而，环境反馈的可靠性直接决定了强化学习（Reinforcement Learning, RL）训练的有效性：若工作上下文缺失依赖、任务规范不一致或验证器存在错误，智能体的有效行为可能被误判为失败，或错误结果被错误奖励。

现有环境合成管线虽能扩展任务规模，但难以在反复修订中维持组件间的对齐。对任务或上下文的修正往往需要同步更新验证器，而传统流程缺乏协调这些变更的机制。此外，稀疏的终端奖励导致信用分配困难：失败轨迹中可能包含有效步骤，成功轨迹中可能包含冗余动作，早期信息收集仅通过后续状态变化间接贡献。这要求一种能同时优化环境可靠性与细粒度学习信号的协同训练范式。

## 核心方法

### Harness 驱动的环境合成与递归演化

WorkRover 将训练环境组织为任务包，包含工作上下文 $C_i$、任务 $T_i$ 与验证器 $V_i$，由 Harness $H$ 协调构建与执行。Harness 显式追踪组件依赖，确保任务可行性与验证器一致性。针对环境构建后出现的兼容性不匹配，引入 Factorial Compatibility Replay (FCR) 进行递归演化。FCR 冻结每个组件的一个修复提案 $\Delta C, \Delta T, \Delta H, \Delta V$，并测试所有组合 $\chi \in \{0, 1\}^d$。每个组合扩展为依赖闭合更新集：

$$ \Gamma(\chi) = \text{Close}(\chi) $$

该公式表示在应用选定修复 $\chi$ 后，自动包含所有为保持依赖组件兼容所需的额外更新。FCR 在匹配的执行预算与随机种子下重放重建后的任务包，选择通过独立检查且改变组件版本最少的最小验证修复 $\chi^*$。这一机制解决了局部编辑破坏绑定关系或导致跨任务回归的问题，确保修复在保持任务意图与评估约束的前提下最小化副作用。

### 验证器接地的回合级信用分配

终端奖励无法区分轨迹中哪些回合产生了实质进展。Verifier-to-Turn Credit Assignment (VTCA) 利用验证器对记录工作空间状态的确定性检查，生成回合级进度信号。冻结的检查器计算每回合前后的支持标准得分，其差值 $\delta_t$ 指示进展或倒退。VTCA 将正向进展信用分配给产生该进展的回合及其前置依赖回合，负向倒退仅保留在产生回合。策略更新采用形状化优势：

$$ \hat{A}_{i,r,t} = \text{sg}(A_{i,r}^{\text{traj}} + \alpha H_{i,r} \delta_{i,r,t}^{\text{crit}} - \eta c_{i,r,t}) $$

其中 $A_{i,r}^{\text{traj}}$ 为轨迹级 GRPO 优势，$\delta_{i,r,t}^{\text{crit}}$ 为基于标准权重的回合级信用，$c_{i,r,t}$ 为局部追踪成本，$H_{i,r}$ 为完整性门控。该公式将稀疏终端奖励细化为密集的过程信号，无需中间 Judge 调用，解决了长程任务中信息收集回合因无直接奖励而被忽视的问题。

## 实验评估

实验在 JobBench、GDPval、AutomationBench、WorkBuddy Bench (Office) 与 OfficeQA Pro 五个外部基准上评估 WorkRover-35B-A3B。基线覆盖包括 SFT、Episode-only GRPO (E-GRPO) 及多个开源/闭源大模型。主结果显示，WorkRover 在 27–35B 开源模型中取得最高分，较 Qwen3.5-35B-A3B 骨干在 JobBench 提升 26.27 个百分点，在 OfficeQA Pro 提升 29.32 个百分点，在 GDPval 提升 413.25 Elo。

| 方法 | JobBench (%) | GDPval (Elo) | AutomationBench (%) | WorkBuddy Bench (Office) (%) | OfficeQA Pro (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Backbone SFT | 33.5 | 805 | 10.6 | 60.5 | 43.5 |
| SFT + E-GRPO | 36.9 | 1218 | 15.5 | 68.0 | 65.0 |
| SFT + VTCA | 36.9 | 1218 | 21.2 | 74.1 | 71.5 |

消融实验验证了 FCR 与 VTCA 的贡献。在匹配修复预算下，FCR 将任务包合成通过率从 49.8% 提升至 74.8%，较全量重生成（68.8%）提升 6.0 个百分点。FCR 将自然缺陷的安全解决率（SRR）从 60.7% 提升至 70.3%，并将跨任务回归率从 7.0% 降至 0.7%。VTCA 在所有五个基准上均优于 E-GRPO，最大增益出现在 AutomationBench (+5.7) 与 OfficeQA Pro (+5.4)。

评估边界方面，论文未报告置信区间，且缺乏与 Tree-GRPO 等细粒度信用分配方法的直接对比，难以排除 VTCA 增益仅源于环境质量提升。此外，VTCA 依赖确定性检查与依赖记录，其信号可靠性受限于检查器覆盖率，在开放域生成任务中的适用性未经验证。

## 关联研究分析

从信用分配机制看，Tree-GRPO 通过树搜索扩展轨迹采样空间，利用分支探索增强策略多样性，其优势估计基于树结构的相对回报。VTCA 则通过环境状态变化的确定性检查提供细粒度信号，计算开销更低但依赖环境可验证性。Tree-GRPO 适用于奖励稀疏但状态可模拟的场景，而 VTCA 适用于工作空间状态可精确追踪的职业任务。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

从系统架构看，AgentRL 构建全异步框架以解决长尾延迟与资源闲置，侧重多节点间的任务调度与并行轨迹生成。WorkRover 的 Harness 则聚焦单任务包内的组件依赖管理与递归修复，解决环境构建中的语义对齐问题。两者在系统层级互补：AgentRL 优化训练吞吐量，WorkRover 优化训练反馈质量。当环境缺陷率较高时，单纯提升异步并行度可能放大噪声，而 FCR 的递归演化机制能从根本上提升环境可靠性。

## 总结

WorkRover 针对长程协作智能体训练中环境可靠性与细粒度归因的双重瓶颈，提出 Harness 驱动的环境合成、FCR 递归演化与 VTCA 信用分配机制。该框架通过组合测试组件修复方案确保环境对齐，并利用验证器状态检查将终端奖励细化为回合级优势。实验显示，WorkRover-35B-A3B 在 JobBench 与 OfficeQA Pro 上分别较骨干提升 26.27 与 29.32 个百分点，VTCA 较 E-GRPO 在多个基准上提升 5.4–5.7 个百分点。其边界在于高度依赖环境可验证性与确定性检查覆盖，在开放域任务中的泛化能力未经验证。当检查器覆盖率不足或依赖记录缺失时，VTCA 的信用分配信号是否会退化为噪声，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.18067)