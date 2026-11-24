# ACL-Findings2026最新论文 ｜Towards Proactive Information Probing: Customer Service Chatbots Harvesting Value from Conversation ｜客服对话中的主动信息探测

研究机构：新加坡国立大学、四川大学

作者：Chen Huang、Zitan Jiang、Changyi Zou 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.11077)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11077)

> 客服机器人长期被定位为被动响应工具，难以在解决用户问题的同时获取高价值商业情报。现有主动代理方法多聚焦于提升用户服务体验，缺乏针对系统侧信息获取目标的时序决策机制，导致探测时机不当引发用户反感或信息遗漏。本文提出PROCHATIP框架，通过独立的对话策略模块结合两阶段训练，优化探测时机以平衡信息获取与用户满意度。该方法在FinQA和ConvQA基准上显著优于基线，但受限于单一信息不对称假设，其策略在复杂真实场景中的泛化能力存疑。

## 研究背景

客服对话中的核心矛盾在于用户意图的即时满足与系统侧信息获取目标之间的冲突。用户通常只关注自身问题是否解决，对机器人发起的额外询问（即“探测”）持抵触态度，若探测时机不当或频率过高，会导致用户拒绝回答甚至终止对话。这种交互摩擦使得传统的被动响应模式无法实现商业情报的规模化采集，而简单的提示工程无法精确控制探测的时序策略，因为LLM缺乏对“等待”这一动作的战略价值评估能力。

任务导向对话（Task-Oriented Dialogue, TOD）研究已确立多轮状态跟踪与意图识别的基础，但主流路线如SimpleTOD和Dual Sentence Encoders主要解决“听懂用户”的问题，而非“主动问用户”的问题。随着大语言模型（Large Language Models, LLMs）的引入，主动代理（Proactive Agent）范式兴起，旨在让系统预判用户需求。然而，现有主动代理工作（如Deng et al., 2023c）多服务于用户中心效用，例如澄清模糊查询或推荐偏好，其目标函数中不包含系统侧的信息收益。PROCHATIP的切入点在于将“主动行为”从服务辅助转向商业情报采集，形式化为一个双目标优化问题：在最大化目标信息获取率的同时，最小化对话轮次和用户摩擦。

## 核心方法

### 对话策略模块解耦架构

PROCHATIP将探测决策从LLM骨干中剥离，引入一个轻量级的对话策略模块（Conversation Strategy Module, CS）。该模块基于Qwen3-0.6B实现，独立于负责生成响应的LLM骨干。这种解耦设计的动机在于，LLM骨干擅长语言生成但缺乏对“何时行动”的时序敏感性，而专用的小模型CS模块可以专注于学习探测时机的二元决策，避免干扰LLM的服务质量。CS模块接收对话历史 $h_t$ 和目标信息 $I$，输出二元决策 $d_t \in \{0, 1\}$，其中 $d_t=1$ 表示执行探测，$d_t=0$ 表示仅回答用户查询。

### 两阶段课程学习与双奖励机制

CS模块的训练分为监督微调（Supervised Fine-Tuning, SFT）和强化学习（Reinforcement Learning, RL）两个阶段。SFT阶段使用基于规则合成的对话数据，建立CS模块识别“合适”与“不合适”探测场景的基线能力。RL阶段引入动态用户模拟器，通过REINFORCE算法优化CS模块的策略。核心创新在于设计了包含“主动探测”与“被动等待”的双奖励函数 $R_t$，以捕捉时序决策中的战略价值。

$$
R_t = \begin{cases}
r_{success} & \text{if } d_t=1 \text{ and probe succeeds} \\
r_{reject} & \text{if } d_t=1 \text{ and user rejects} \\
r_{invalid} & \text{if } d_t=1 \text{ and probe is ignored} \\
r_{smart\_stop} & \text{if } d_t=0 \text{ and previous turn was rejected} \\
r_{passive\_penalty} & \text{if } d_t=0 \text{ and previous turn was passive}
\end{cases}
$$

该公式的物理含义是：奖励不仅取决于探测是否成功，还取决于“不探测”这一动作在特定上下文中的价值。例如，若上一轮探测被拒绝，当前轮选择等待（$d_t=0$）会获得高额奖励（$r_{smart\_stop}$），鼓励系统动态退让；若连续多轮无动作，则施加惩罚（$r_{passive\_penalty}$），防止系统陷入惰性策略。这种机制解决了SFT阶段仅能模仿静态规则、无法适应动态用户抵抗模式的问题。

## 实验评估

实验在FinQA（复杂多跳问题）和ConvQA（简化分解问题）两个数据集上进行，使用GPT-4o Mini和Qwen3 8B作为LLM骨干。基线包括被动响应（Vanilla）和两种通用主动代理方法（Proactive, ICL-AIF）。PROCHATIP在两个数据集上均取得最高任务成功率（TSR），在FinQA上达到93.42%（GPT-4o Mini），在ConvQA上达到81.33%。

| 骨干网络 | 方法 | FinQA TSR (%) | FinQA AvgT | ConvQA TSR (%) | ConvQA AvgT |
|---|---|---|---|---|---|
| GPT-4o Mini | Proactive | 90.75 | 2.80 | 80.83 | 3.38 |
| GPT-4o Mini | ICL-AIF | 70.33 | 3.66 | 58.50 | 4.55 |
| GPT-4o Mini | PROCHATIP | 93.42 | 1.47 | 81.33 | 2.36 |
| Qwen3 8B | Proactive | 64.00 | 4.99 | 58.58 | 5.16 |
| Qwen3 8B | ICL-AIF | 27.17 | 6.67 | 27.00 | 6.70 |
| Qwen3 8B | PROCHATIP | 77.92 | 2.68 | 70.25 | 3.29 |

PROCHATIP相比次优基线Proactive，在平均TSR上提升11.36%，平均对话轮次（AvgT）降低39.50%，表明其策略不仅提高了信息获取效率，还显著减少了用户交互成本。

消融实验显示，SFT和RL阶段均不可或缺。仅使用SFT（w/o RL）的模型表现出保守策略，拒绝探测率（RPR）低但TSR也低，说明其缺乏主动探索的动力；仅使用RL（w/o SFT）的模型则过于激进，RPR高且TSR不稳定。这表明SFT提供了探测的语义基础，而RL优化了时序策略，两者协同作用才能实现最佳平衡。

评估边界方面，实验仅使用6名人类参与者进行主观满意度评估，样本量较小，统计显著性有限。此外，实验假设用户拥有目标信息且愿意在适当时机回答，未考虑用户信息不对称或恶意拒绝的极端场景。代码已公开，但超参数细节（如奖励权重）未在正文中完全披露，可能影响复现性。

## 关联研究分析

从问题动机看，PROCHATIP与ProActor（Ding et al., 2026）同属主动代理时序决策范畴，但目标函数存在本质差异。ProActor优化的是任务完成时机，旨在最大化任务成功率，其奖励函数聚焦于动作正确性；而PROCHATIP优化的是信息获取时机，旨在平衡信息收益与用户摩擦，其奖励函数包含“被动等待”的战略价值。这一差异源于任务特性：任务调度中“等待”通常意味着延迟，而信息探测中“等待”可能是避免用户反感的关键策略。PROCHATIP的双奖励机制正是为了捕捉这种“等待的价值”，这是ProActor等任务导向方法未涉及的设计维度。

从方法设计看，PROCHATIP与InteractCS-RL（Gao et al., 2026）均关注成本-效用平衡，但实现路径不同。InteractCS-RL使用拉格朗日惩罚项在单一奖励函数中平衡服务效用与运营成本，属于约束优化范式；而PROCHATIP通过显式的“主动/被动”二元决策和分阶段奖励，将平衡问题转化为策略学习问题。PROCHATIP的解耦架构允许CS模块独立于LLM骨干优化，这可能限制了LLM对复杂语境的动态适应能力，因为CS模块仅基于对话历史和目标信息做决策，未直接利用LLM的深层语义理解。在低资源骨干（如Qwen3 8B）上，缺乏结构化意图表示是否导致性能瓶颈，论文未给出明确回答，但实验显示Qwen3 8B上的TSR仍显著高于基线，暗示解耦架构在一定程度上弥补了骨干能力的不足。

## 总结

PROCHATIP解决的核心矛盾是客服场景中信息获取与用户满意度的冲突，其切入点在于将探测时机形式化为独立的时序决策问题，并通过解耦的策略模块和双奖励机制实现优化。该方法在FinQA和ConvQA上分别取得93.42%和81.33%的TSR，证明了专用策略模块优于通用提示工程。然而，实验假设用户信息对称且配合，未覆盖用户信息缺失或恶意拒绝的场景，且人类评估样本量较小。当用户行为模式从“配合型”转向“对抗型”时，PROCHATIP的被动等待奖励机制是否仍能维持低摩擦，论文未提供相关实验数据。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11077)