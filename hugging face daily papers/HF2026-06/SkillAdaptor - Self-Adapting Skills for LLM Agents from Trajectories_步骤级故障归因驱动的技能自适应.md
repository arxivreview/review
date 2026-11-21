# HuggingFace最新推荐论文 ｜SkillAdaptor: Self-Adapting Skills for LLM Agents from Trajectories ｜步骤级故障归因驱动的技能自适应

研究机构：浙江大学

作者：Zhuoyun Yu、Xin Xie、Wuguannan Yao 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.01311)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.01311)

> 长程任务中，代理失败往往由早期单步错误引发，但现有训练-free技能优化方法依赖整条轨迹的最终结果进行反思，导致失败信号扩散至无关技能，产生过宽或错误的修订。SKILLADAPTOR 将反思单元从轨迹级下沉至步骤级，通过定位首个可操作故障步并关联具体责任技能，实现精准更新。该框架在冻结骨干模型上，通过归因、修改与资格验证三阶段闭环，提升了技能维护的稳定性与可审计性。其价值在于解决了信用分配模糊问题，但在稀疏反馈或依赖外部持久状态的任务中，归因有效性可能受限。

## 研究背景

长程交互式任务要求代理在环境中执行多步动作，每一步动作 $a_t$ 产生观测 $o_t$，形成轨迹 $\tau = (a_1, o_1, \dots, a_T, o_T)$。为了在不更新模型权重的前提下提升性能，系统维护一个外部技能库 $\mathcal{K}$，其中每个技能 $s_i$ 包含标题、原则及适用条件。代理在执行时检索相关技能作为上下文，执行结束后根据结果更新技能库。这一机制的核心挑战在于：当任务失败时，如何从冗长的轨迹中准确识别导致失败的根源，并仅修正受影响的技能，避免污染整个技能库。

现有训练-free技能优化方法（如 ExpeL, EvoSkill）通常将完整轨迹或会话摘要作为反思单元。这种轨迹级反馈在长程任务中表现出脆弱性：一条失败轨迹中可能包含大量正确的中间决策，真正的失败仅源于少数早期错误。当更新由最终结果驱动时，失败信号会扩散到无关步骤和技能，导致修订范围过宽或方向错误。这种信用分配（credit-assignment）问题在单一早期错误导致后续连锁失败的场景中尤为严重。SKILLADAPTOR 的切入点在于将反思粒度从“整条轨迹”细化为“单个步骤”，通过显式定位故障步来隔离责任，从而实现对技能库的精准、局部化更新。

## 核心方法

### 方法参照系

本文方法属于“技能自动优化”路线，其标准流程为：执行任务获取轨迹 → 基于轨迹生成技能更新建议 → 验证更新有效性 → 更新技能库。与 SkillOpt 或 SkillGrad 等基于文本梯度或全局反思的方法不同，SKILLADAPTOR 的关键差异在于引入了显式的“故障定位”与“责任链接”前置步骤，将更新信号从全局结果解耦为局部步骤级信号。

### 步骤级故障归因

传统方法直接基于最终失败结果生成修订建议，忽略了中间步骤的正确性。SKILLADAPTOR 引入 Localizer 和 Linker 模块，首先定位首个可操作故障步 $t^*$，即修正该步预期能改善最终结果的最早步骤。随后，Linker 估计检索到的候选技能中哪些对失败负有主要责任，输出加权嫌疑集 $\{w_j\}$ 及适配动作 $\hat{a} \in \{\text{REVISE}, \text{GENERATE}\}$。

$$
(t^*, \pi) = \text{Localizer}(\tau, \mathcal{S}_q), \quad \{w_j, \hat{a}\} = \text{Linker}(\tau, t^*, \mathcal{S}_q)
$$

其中 $\pi$ 为失败行为描述及改进建议，$\mathcal{S}_q$ 为任务 $q$ 检索到的技能集。该设计解决了轨迹级反思中失败信号扩散的问题，确保修订仅针对具体故障步对应的技能，而非整个轨迹涉及的所有技能。

### 资格验证与局部更新

归因后，Modifier 根据 $\hat{a}$ 执行更新：若为 REVISE，重写权重最高的技能；若为 GENERATE，从 $t^*$ 的局部上下文合成新技能。为防止有害更新，Qualifier 模块通过重执行对比候选技能库 $\mathcal{K}_{+}$ 与当前库 $\mathcal{K}$ 的性能差异 $\Delta$，仅当 $\Delta \ge 0$ 时接受更新。

$$
\Delta = M(\text{Run}(q, \mathcal{K}_{+})) - M(\text{Run}(q, \mathcal{K})), \quad \mathcal{K}_{+} = \begin{cases} \mathcal{K} \cup \{s_{new}\} & \text{if } \hat{a}=\text{GENERATE} \\ \mathcal{K} \setminus \{s_{old}\} \cup \{s_{new}\} & \text{if } \hat{a}=\text{REVISE} \end{cases}
$$

其中 $M(\cdot)$ 为执行反馈指标。该机制通过硬性过滤抑制了不稳定技能的进入，解决了迭代优化中技能过拟合或负迁移的问题，确保了技能库在长程交互中的稳定性。

## 实验评估

实验在 WebShop、PinchBench 和 Claw-Eval 三个基准上进行，使用 Kimi-K2.5、GLM-5 和 GPT-5.2 作为骨干模型。基线包括 Base Model、A-Mem、AWM、ExpeL、EvoSkill 和 OpenSpace。值得注意的是，实验未包含 SkillOpt、SkillGrad 等 2026 年 SOTA 方法的直接对比，这可能限制了与最新优化方法的横向比较。

| 方法 | WebShop (Kimi-K2.5) Score | WebShop (Kimi-K2.5) Succ% | PinchBench (Kimi-K2.5) Avg Score% | Claw-Eval (Kimi-K2.5) Avg Score |
| :--- | :--- | :--- | :--- | :--- |
| Base Model | 32.1±1.4 | 24.6±1.5 | 63.6±8.7 | 73.2±1.3 |
| EvoSkill | 34.0±0.9 | 31.3±0.8 | - | - |
| OpenSpace | 73.2±1.3 | 74.4% | - | - |
| SkillAdaptor | 41.6±0.5 | 33.0±1.1 | 67.2±5.2 | 75.8±1.6 |

在 WebShop 上，SkillAdaptor 的 Score 为 41.6，Succ% 为 33.0，显著优于 Base Model 的 32.1 和 24.6，也优于最强基线 EvoSkill 的 34.0 和 31.3。在 PinchBench 和 Claw-Eval 上，SkillAdaptor 分别达到 67.2 和 75.8，均高于 Base Model。然而，与领域综述中提到的 Skill1 在 ALFWorld 上 97.9% 的成功率相比，本文在 WebShop 上的绝对性能较低，这主要源于任务类型和骨干模型能力的差异，而非方法本身的缺陷。

| 配置 | WebShop Score | WebShop Succ% | PinchBench Avg Score% | Claw-Eval Avg Score |
| :--- | :--- | :--- | :--- | :--- |
| (1) Full | 41.6±0.8 | 33.0±1.0 | 67.2±5.2 | 75.8±1.6 |
| (2) w/o Localizer&Linker | 35.8±0.9 | 28.6±1.5 | 65.3±6.8 | 74.5±1.4 |
| (3) w/o Qualifier | 34.0±2.1 | 26.3±2.6 | 65.8±8.1 | 74.2±2.7 |
| (4) Initial skills only | 32.5±1.0 | 25.3±2.5 | 64.1±7.3 | 73.9±1.8 |

消融实验显示，移除 Localizer 和 Linker 后，WebShop Succ% 从 33.0 降至 28.6，表明步骤级归因对精准修订至关重要。移除 Qualifier 后，Succ% 进一步降至 26.3，且标准差增大（±2.6 vs ±1.0），说明资格验证在抑制不稳定更新方面发挥了关键作用。仅使用初始技能（无自适应）时，性能接近 Base Model，证实了自适应过程的必要性。

评估协议采用三次独立运行的均值和标准差，代码已开源。局限在于：实验未覆盖计算效率指标（如 Token 成本、延迟），且 PinchBench 和 Claw-Eval 的基线数据在表格中缺失，仅能对比 Base Model 和 SkillAdaptor。此外，方法依赖可观测的中间信号，在稀疏反馈或外部接口缺失的场景下，归因有效性可能下降。

## 关联研究分析

从问题动机看，SKILLADAPTOR 与 SkillOpt 均关注技能优化的稳定性，但解决路径不同。SkillOpt 基于文本梯度和有界编辑，假设技能文档是连续参数空间，通过验证门控接受提升性能的编辑。而 SKILLADAPTOR 认为轨迹级反馈的信用分配模糊是主要瓶颈，因此引入步骤级归因来隔离责任。这种差异源于任务特性：SkillOpt 更适用于结构化文档处理等确定性任务，而 SKILLADAPTOR 在 WebShop 等动态交互任务中表现更优，因为后者更依赖中间步骤的正确性。

从方法设计看，SKILLADAPTOR 与 Trace2Skill 在技能生成粒度上形成互补。Trace2Skill 从成功轨迹并行蒸馏通用 SOP，强调技能的泛化性和可分享性，但缺乏对失败轨迹的精细利用。SKILLADAPTOR 则从失败轨迹中提取局部故障信息，生成针对性修订，强调技能的精准性和可审计性。两者结合可能形成“生成-优化”闭环：先用 Trace2Skill 构建基础技能库，再用 SKILLADAPTOR 进行故障驱动的局部优化。然而，论文未探索这种组合策略，也未评估步骤级归因在缺乏明确中间状态的任务（如 Research、Security）中的有效性，这些场景下失败往往依赖持久状态或外部知识，局部修订可能无法解决根本问题。

## 总结

SKILLADAPTOR 旨在解决长程任务中技能优化的信用分配模糊问题，即失败信号在轨迹级反思中扩散导致修订过宽。其切入点在于将反思单元下沉至步骤级，通过 Localizer 定位首个可操作故障步，Linker 关联责任技能，Qualifier 验证更新有效性，实现了精准、局部的技能更新。实验表明，该方法在 WebShop 上较 Base Model 提升 8.4% 成功率，在 PinchBench 和 Claw-Eval 上均取得正向增益，且消融实验证实了步骤级归因和资格验证的关键作用。然而，方法的有效性依赖于可观测的中间信号，在稀疏反馈或依赖外部持久状态的任务中，归因可能失效。当任务失败源于跨会话上下文或外部系统状态时，步骤级归因是否仍能准确定位责任，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.01311)