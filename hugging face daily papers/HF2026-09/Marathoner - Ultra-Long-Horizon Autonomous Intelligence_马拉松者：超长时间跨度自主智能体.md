# HuggingFace最新推荐论文 ｜Marathoner: Ultra-Long-Horizon Autonomous Intelligence ｜马拉松者：超长时间跨度自主智能体

研究机构：澳门大学、北京大学

作者：Zhang Ruiyang、Ou Jinpeng、Xie Yifan 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2609.34378)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.34378)

> 长程智能体在数小时执行中常因策略停滞或错误累积而失效，现有后训练管线缺乏针对“持续有效行动”的显式监督。本文切入点在于将“执行时长”而非“上下文窗口”作为核心能力维度，通过任务合成、拒绝采样微调与强化学习构建超长时间跨度执行能力。其价值在于验证了开源模型在10+小时执行中的潜力，但奖励机制对“有价值操作”的判定依赖外部LLM，存在主观性风险。

## 研究背景

当智能体面对需要数小时完成的复杂软件工程任务时，其核心挑战并非单次推理的上下文长度限制，而是如何在长时间跨度内维持策略的有效性与一致性。这一过程涉及两个关键概念：一是**超长时间跨度执行（Ultra-Long-Horizon Execution）**，指智能体在数小时至数天尺度上持续进行工具调用与环境交互的能力；二是**后期阶段价值保持**，即智能体在执行后期仍能识别并修复关键缺陷或进行核心优化，而非陷入重复性低价值操作。传统强化学习（RL）通常针对单轮或短程任务优化，其稀疏的最终奖励信号难以有效引导智能体在长程执行中保持后期阶段的高价值行为密度，导致“执行疲劳”或策略停滞。

长上下文大语言模型（Long-Context LLM）研究已揭示“中间迷失”与“上下文腐烂”现象，表明模型在长序列中信息利用率随位置增加而下降。然而，这些理论主要聚焦于单次前向传播的注意力机制缺陷，未充分解释多轮交互中智能体状态漂移与错误累积的机制。现有开源模型在长程执行任务上性能显著落后于闭源前沿模型（如GPT-6-Astra、Claude Fable 5.1），主要瓶颈在于缺乏针对超长时间尺度的系统性后训练范式。本文切入点在于将“执行时长”与“工具调用次数”作为独立能力维度，通过构建包含10+小时执行需求的任务池，并引入针对后期阶段操作的显式奖励机制，弥补现有方法在长程执行监督上的空白。

## 核心方法

### 方法参照系

本文问题属于智能体后训练（Post-Training for Agents）范畴，标准流程包括数据合成、监督微调（SFT）与强化学习（RL）。与通用智能体训练的关键差异在于：任务难度需匹配10+小时执行时长，且奖励信号需显式区分执行阶段的价值密度，而非仅关注最终结果正确性。

### 超长时间跨度任务合成与多任务链式

传统任务合成多基于单一代码库的局部修改，难以产生需要数小时执行的高难度任务。本文提出**多任务链式（Multi-Task Chaining）**，将5个原子任务随机串联为单一Frontier任务。每个原子任务源自GitHub主版本发布PR，代码库检出至PR前一个提交，指令取自PR首条评论或发布说明，奖励验证器包含fail-to-pass（验证新功能）与pass-to-pass（回归旧功能）单元测试。链式任务的软件组件为多个仓库，指令为各任务指令拼接，奖励验证器为各任务验证器的组合。该设计强制智能体在多个大型代码库间协调，执行时长从分钟级扩展至小时级，解决了单一任务难度不足导致的执行能力上限问题。

### 后期阶段奖励与强化学习

标准RL使用二元最终奖励 $R_{correctness} \in \{0,1\}$，无法区分执行过程中后期阶段的价值操作。本文提出**后期阶段奖励（Later Stage Bonus Reward）**，将轨迹划分为多个阶段，由LLM判断后期阶段是否包含高价值操作（如修复关键Bug、核心优化）。若存在，则赋予额外奖励 $R_{bonus} = 0.5$。最终奖励为：

$$
R_i = R_{correctness}(o_i) + R_{bonus}(o_i)
$$

其中 $R_{correctness}$ 由单元测试验证器计算，$R_{bonus}$ 由LLM裁判基于阶段摘要判定。该公式显式激励智能体在执行后期保持高价值行为密度，对抗长程执行中的策略停滞。强化学习采用GRPO算法，训练目标为：

$$
J_{GRPO}(\theta) = \mathbb{E}_{q \sim P(Q), \{o_i\}_{i=1}^G \sim \pi_{\theta_{old}}(\cdot|q)} \left[ \frac{1}{G} \sum_{i=1}^G \left( \min \left( \frac{\pi_\theta(o_i|q)}{\pi_{\theta_{old}}(o_i|q)} A_i, \text{clip} \left( \frac{\pi_\theta(o_i|q)}{\pi_{\theta_{old}}(o_i|q)}, 1-\epsilon, 1+\epsilon \right) A_i \right) - \beta D_{KL}(\pi_\theta \| \pi_{ref}) \right) \right]
$$

其中 $A_i$ 为基于奖励 $\{R_1, ..., R_G\}$ 计算的归一化优势，$\beta$ 为KL惩罚系数。该设计通过组内相对优势优化，结合后期阶段奖励，使智能体在真实沙箱环境中习得鲁棒的超长时间跨度执行能力。

## 实验评估

| 模型 | Harness | FrontierSWE | NL2Repo | SWE-Marathon | Terminal Bench 2.0 | SWE-Bench Verified |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| GPT-6-Astra | Codex | 89.1 | 78.2 | 48.7 | 87.4 | 90.7 |
| Claude Fable 5.1 | Claude Code | 86.2 | 73.2 | 42.8 | 85.9 | 91.8 |
| Gemini-3.1-Pro | Gemini CLI | 25.9 | 42.8 | 5.9 | 60.3 | 80.1 |
| Qwen3.5-9B | Claude Code | 10.2 | 17.9 | 27.3 | 43.8 | - |
| Marathoner-9B | Claude Code | 26.4 | 34.7 | 8.2 | 57.2 | 77.5 |

实验在5个超长时间跨度基准上进行，对比闭源前沿模型（GPT-6-Astra、Claude Fable 5.1、Gemini-3.1-Pro）与开源基线（Qwen3.5系列）。Marathoner-9B在FrontierSWE（26.4%）上超越Gemini-3.1-Pro（25.9%），在SWE-Bench Verified（77.5%）上显著优于开源基线Qwen3.5-9B（43.8%），但绝对性能仍落后于GPT-6-Astra（90.7%）与Claude Fable 5.1（91.8%）。基线覆盖审计显示，对比方法包含不同Harness（Claude Code、Codex、Gemini CLI），但缺失纯长上下文LLM基线（如Llama-3.1-8B），因任务性质为多轮交互而非单次推理。

| 设置 | FrontierSWE | Terminal Bench 2.0 |
| :--- | :--- | :--- |
| Marathoner (vanilla) | 22.7 | 51.3 |
| w. Multi-Task Chaining | 24.9 | 54.8 |
| w. Diverse-Harness Trajectory Generation | 24.1 | 53.7 |
| w. Later Stage Bonus Reward | 24.6 | 54.4 |

消融实验显示，Multi-Task Chaining带来最大提升（FrontierSWE +2.2，Terminal Bench 2.0 +3.5），验证了任务难度对执行能力的关键作用。Later Stage Bonus Reward提升FrontierSWE 1.9点、Terminal Bench 2.0 3.1点，表明后期阶段奖励对长程执行有效。Diverse-Harness Trajectory Generation提升较小（FrontierSWE +1.4，Terminal Bench 2.0 +2.4），暗示Harness多样性对执行能力的边际收益低于任务难度。环境扩展实验显示，RL训练任务从1,000增至8,000时，性能持续提升，表明真实环境多样性是提升执行能力上限的关键路径。

评估边界方面，指标完备性包含执行时长（10+小时）与工具调用次数（1000+），但缺乏对“有效操作密度”的细粒度量化。评估协议局限在于SWE-Bench Verified任务平均时长较短，能否证明10+小时执行能力的泛化性存疑。可复现性方面，论文提供详细超参数（学习率5e-6/1e-6，序列长度256k，32 H800 GPUs），但未公开代码URL，Harbor框架作为任务格式标准可作为参照。

## 关联研究分析

从问题动机看，本文与递归语言模型（RLM）共享任务分解思想，但RLM通过递归调用自身处理子片段，本文通过Multi-Task Chaining线性串联原子任务。差异根源在于任务特性：RLM面向任意长度文本理解，本文面向代码库修改，后者需要跨仓库状态协调，线性串联比递归调用更易于工程实现且状态管理更简单。从方法设计看，本文的Later Stage Bonus Reward与LongRLVR的过程奖励机制相似，但LongRLVR针对步骤维度优化，本文针对时间维度优化。这一差异源于长程执行中“时间”与“步骤”的非线性关系：步骤数增加不一定意味着时间消耗增加，后期阶段的价值操作密度比步骤正确性更能反映执行能力的鲁棒性。

## 总结

本文核心矛盾在于开源模型在超长时间跨度执行中缺乏持续有效行动能力，现有后训练管线未针对执行时长进行显式监督。本文抓住“后期阶段价值保持”这一被忽略的点，通过Multi-Task Chaining构造10+小时执行任务，并引入Later Stage Bonus Reward显式激励后期高价值操作。实验证明Marathoner-9B在FrontierSWE上超越Gemini-3.1-Pro，在SWE-Bench Verified上显著优于开源基线。其边界在于奖励判定依赖外部LLM，存在主观性风险，且SWE-Bench Verified任务时长较短，10+小时执行能力的泛化性未充分验证。当执行时长进一步扩展至数天尺度时，后期阶段奖励对策略停滞的缓解效果是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.34378)