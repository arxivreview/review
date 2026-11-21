# HuggingFace最新推荐论文 ｜The PokeAgent Challenge: Competitive and Long-Context Learning at Scale ｜宝可梦智能体挑战：具身长程博弈基准

研究机构：美国卡内基梅隆大学、美国纽约大学

作者：Seth Karten、Jake Grigsby、Tersoo Upaa 等 31 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.15563)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.15563)

> 现有游戏基准往往孤立测试部分可观测性或长程规划，缺乏在真实对抗环境下同时施加三重压力的标准化测试场。本文切入点在于利用宝可梦生态的复杂性，构建包含竞技对战与RPG速通的双轨基准，通过解耦Harness架构与底层模型能力，量化通用大语言模型与专用强化学习在具身决策中的真实差距。其价值在于填补了视觉感知与长程一致性评估的空白，但当前结果主要验证了基准的区分度，而非特定算法的优越性。

## 研究背景

当智能体面对隐藏对手队伍与动态地图时，其决策依赖于对未观测状态的信念构建，这一过程称为部分可观测马尔可夫决策过程（Partially Observable Markov Decision Process, POMDP）。POMDP要求智能体在信息不完备下维持长程策略一致性，而传统强化学习（Reinforcement Learning, RL）在完全可观测环境中虽能超越人类，但在随机且部分可观测的场景中优势显著衰减。大语言模型（Large Language Model, LLM）虽具备语义推理能力，但在需要精确状态追踪与实时反应的高频交互中，常因上下文窗口限制与缺乏显式状态机制导致策略漂移。

游戏AI领域长期存在“静态知识”与“动态战略”的割裂。早期基准如Chess或Poker侧重均衡计算，而NetHack等开放环境侧重探索，但均未能同时涵盖对抗性推理与数千步的长程规划。现有LLM评估多依赖文本符号状态，忽略了视觉感知在具身任务中的核心作用。PokéAgent Challenge针对这一空白，利用宝可梦庞大的状态空间与持续演化的竞技元游戏，构建了首个结合视觉感知、对抗博弈与长程规划的标准化基准，旨在揭示通用模型在具身长程任务中的真实上限。

## 核心方法

### 双轨基准架构

本文基准区别于单一任务测试，采用互补的双轨设计。Battling Track聚焦于两人零和随机博弈，通过隐藏队伍信息测试信念更新与策略泛化；Speedrunning Track则要求智能体在数千步内完成RPG关卡，测试长程规划与记忆保持。这种设计迫使评估对象同时应对即时对抗与长期目标，避免了单一维度评估的片面性。

### Harness-Model解耦评估

传统LLM游戏评估常将模型能力与外部脚手架（Harness）混淆，导致无法归因性能来源。本文提出五维解耦框架，将系统分解为状态表示（$S$）、工具（$T$）、记忆（$M$）、反馈（$F$）与微调（$\Phi$）。

$$ \text{Performance} = f(S, T, M, F, \Phi) $$

该公式表明，最终性能是架构组件与底层模型参数的联合函数。通过固定Harness并替换底层模型，或固定模型并改变Harness，可独立量化各维度的贡献。这一设计解决了此前研究中“模型强则系统强”的归因谬误，揭示了CLI代理架构在长程一致性上的结构性缺陷。

### 多智能体编排与上下文压缩

针对长程任务中的上下文爆炸问题，本文设计了多智能体编排系统。中央协调器维护高层路线计划，动态调度战斗策略、自我反思等子智能体。

$$ C_{t+1} = \text{Compact}(C_t, o_t, a_t, \text{Plan}_t) $$

其中 $C_t$ 为上下文状态，$\text{Compact}$ 为自动压缩函数。该机制通过定期压缩历史推理步骤并保留关键里程碑，解决了数千步决策中LLM因上下文窗口溢出导致的逻辑断裂。实验表明，缺乏此机制的原始模型在速通任务中完成率为0%，而具备该Harness的系统实现了非零进展。

## 实验评估

实验基于Pokémon Showdown模拟器与Pokémon Emerald游戏环境，对比了RL、LLM及启发式基线。Battling Track使用Glicko-1与Full-History Bradley-Terry（FH-BT）评分，Speedrunning Track记录完成时间、动作数与Token消耗。基线覆盖从紧凑RNN到200M参数Transformer的RL模型，以及GPT、Claude、Gemini等前沿LLM。

| 模型/方法 | Battling GXE (Gen 9 OU) | Speedrunning 平均完成时间 |
| :--- | :--- | :--- |
| RL (PokéAgent) | 90% | — |
| LLM (Gemini 3.1 Pro) | 91% | — |
| LLM (Claude Sonnet 4.5) | — | 6:25–20:45 (高方差) |
| LLM (Gemini 3 Flash) | — | ~2:24 |
| Human (Average) | — | 1:22:05 |

数据显示，RL基线在Battling中达到90% GXE，接近人类顶尖水平，而LLM基线在Gen 9 OU中表现波动，最高为Gemini 3.1 Pro的91%。在Speedrunning中，Gemini 3 Flash最快（~2:24），但仍比平均人类慢1.8倍。值得注意的是，无Harness的原始前沿模型完成率为0%，证明架构在具身长程任务中的必要性。

消融分析显示，CLI代理架构（如Claude Code）在相同模型下无法维持长程一致性，而专用Harness显著提升了稳定性。Gemini 3 Flash虽速度快，但动作数多于Gemini 3 Pro，揭示了推理速度与样本效率的权衡。Claude Sonnet 4.5虽完成所有里程碑，但成本为Gemini变体的3-4倍，且方差极大。

评估边界方面，Battling Track依赖Showdown服务器，可能存在网络延迟干扰；Speedrunning Track仅评估至第一个道馆，未覆盖完整游戏。代码与数据已开源，但RL基线的超参数细节未在正文中完全披露，复现需依赖附录。

## 关联研究分析

从问题动机看，PokéAgent与MineRL均关注长程规划，但MineRL侧重开放世界探索，缺乏对抗性对手；PokéAgent引入实时博弈，测试信念更新能力。与NetHack相比，PokéAgent强调视觉感知与竞技生态的演化，而NetHack多为文本符号状态。这种差异源于任务特性：宝可梦的元游戏持续变化，要求智能体适应分布偏移，而非仅记忆静态规则。

从方法设计看，本文的Harness解耦框架与Voyager等LLM智能体研究不同。Voyager侧重代码生成与技能库积累，而PokéAgent聚焦于状态追踪与上下文压缩。与PokerSkill等文本博弈基准相比，PokéAgent引入了像素级感知，增加了视觉-语言对齐的难度。这种多模态引入可能掩盖了纯文本推理能力的评估，因为视觉噪声可能干扰战略决策的归因。

## 总结

本文核心矛盾在于通用LLM在具身长程博弈中缺乏状态一致性与实时反应能力。切入点在于利用宝可梦生态的复杂性，构建双轨基准并解耦Harness与模型能力。通过多智能体编排与上下文压缩，证明了架构在长程任务中的必要性。实验显示RL在对抗中占优，LLM在速通中虽能完成但效率远低于人类。边界在于当前评估仅覆盖游戏早期阶段，且视觉模态的引入可能混淆战略推理与感知能力的评估。当支持集增大到完整游戏时，Harness的上下文压缩机制是否仍能维持策略一致性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.15563)