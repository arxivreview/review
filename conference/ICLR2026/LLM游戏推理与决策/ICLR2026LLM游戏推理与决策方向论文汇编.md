# ICLR2026 · LLM游戏推理与决策方向论文汇编

> 本方向共 7 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Code World Models for General Game Playing ｜代码世界模型（CWM）：从策略生成到环境形式化的范式转移

研究机构：谷歌DeepMind

作者：Wolfgang Lehrach、Daniel Hennes、Miguel Lazaro-Gredilla 等 16 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.04542)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.04542)

> 大语言模型（LLM）在动态博弈中直接作为策略时，常因缺乏深层前瞻与精确状态追踪而陷入浅层模式匹配。现有方法试图通过强化学习或思维链增强策略，但在面对未见过的规则（OOD）时泛化能力受限。本文提出将LLM定位为“归纳引擎”，利用其语义理解能力将游戏规则与少量轨迹转化为可执行的Python代码世界模型（Code World Model, CWM），并交由经典规划算法求解。这一“模型-规划”分离架构在10款游戏中9款超越Gemini 2.5 Pro，但其对复杂子程序规则的代码合成能力仍显脆弱。

】

---

【Evaluating Language Models' Evaluations of Games ｜评估评估者：语言模型对博弈系统元认知能力的量化分析

研究机构：英国剑桥大学、美国麻省理工学院

作者：Katherine M. Collins、Cedegao E. Zhang、Graham Todd 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.10930)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.10930)

> 现有AI评估范式聚焦于模型“解题”能力，即如何在游戏中获胜，却忽视了“选题”能力，即判断一个博弈系统是否值得投入资源去解决。这种缺失导致模型在静态基准上的高分无法反映其在真实资源约束下的决策合理性。本文提出“评估评估者”的新范式，通过构建121个新颖棋盘游戏数据集，量化模型对游戏预期收益与趣味性的判断与人类及理论最优解的偏差。该工作揭示了推理模型在逼近博弈论最优解时与人类判断出现非单调背离的现象，为理解AI元认知边界提供了实证基础，但其静态文本评估协议是否足以代理动态博弈中的复杂推理过程仍存疑。

】

---

【How Far Are LLMs from Professional Poker Players? Revisiting Game-Theoretic Reasoning with Agentic Tool Use ｜工具集成推理框架

研究机构：清华大学

作者：Minhua Lin、Enyan Dai、Hui Liu 等 14 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.00528)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.00528)

> 导读 扑克作为不完全信息博弈的典范，要求智能体在隐藏信息下估计对手范围并做出符合博弈论原理的决策，而现有大语言模型（LLM）在此类任务中普遍依赖浅层启发式且存在严重的“知道-做”差距。本文指出，仅靠内部策略微调无法弥补LLM在精确数值计算与均衡策略推导上的固有缺陷。为此，作者提出ToolPoker，通过统一接口调用外部求解器获取GTO动作，并由LLM生成专业级解释。该框架在Leduc Hold'em中实现了+6.8的平均筹码收益，显著优于未微调基线，但其性能高度依赖外部求解器的准确性，LLM自身的推理能力并未得到本质提升。

】

---

【LLMS AS RULES ORACLES: EXPLORING REAL WORLD MULTIMODAL REASONING IN TABLETOP STRATEGY GAME ENVIRONMENTS ｜多模态桌游规则理解基准

研究机构：美国密歇根大学

作者：Joseph Peper、Sai Krishna Gandra、Yunxiang Zhang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_2547363)

> 现有游戏推理研究多依赖规则强制的数字模拟器，导致模型在移除脚手架后无法处理真实物理场景中的杂乱视觉状态与异构规则书。本文切入点在于剥离动态博弈的复杂性，聚焦于“首次玩家”面临的静态规则获取与视觉接地问题。通过构建包含感知、规则整合与短程优化的三级多模态基准，量化了前沿大语言模型在真实桌游场景下的推理断点。该工作揭示了当前模型在符号接地与空间推理上的系统性失效，但其单步静态设定限制了对其动态策略适应性的评估。

】

---

【Look-ahead Reasoning with a Learned Model in Imperfect Information Games ｜基于学习抽象模型的不完全信息博弈前瞻推理

研究机构：捷克布拉格捷克理工大学

作者：Ondřej Kubíček、Viliam Lisý

论文原文见 [arXiv](https://arxiv.org/abs/2510.05048)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.05048)

> 不完全信息博弈（IIG）中的前瞻推理长期受限于状态空间爆炸与显式规则依赖，导致理论最优策略在大规模游戏中不可计算。现有直接策略优化方法虽能训练出基础策略，但缺乏测试时计算能力，致使策略极易被对手利用；而传统求解器又依赖手工抽象或深度限制，无法处理超大规模共享知识状态。本文提出 LAMIR，通过从交互轨迹中自动学习域无关的抽象模型，将子博弈规模限制在可管理范围内，从而在无显式规则支持下实现理论合理的前瞻推理。该方法在超大状态空间下显著优于基线，但其抽象机制可能引入的信息损失对策略最优性的影响尚存疑。

】

---

【MARSHAL: Incentivizing Multi-Agent Reasoning via Self-Play with Strategic LLMs ｜多智能体自博弈强化学习框架

研究机构：清华大学、芬兰阿尔托大学

作者：Huining Yuan、Zelai Xu、Zheyue Tan 等 13 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.15414)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.15414)

> 多智能体强化学习（Multi-Agent Reinforcement Learning, MARL）在长程交互中面临信用分配与优势估计方差的双重困境，导致策略更新不稳定且难以归因。现有单轮强化学习框架无法处理多回合、多角色的异构收益结构，而传统自博弈方法仅聚焦零和竞争，缺乏对合作场景的覆盖。MARSHAL 通过引入回合级优势估计器与角色特定归一化机制，在合作与竞争混合博弈中实现端到端自博弈训练。该框架验证了游戏内习得的推理能力可向非游戏多智能体系统泛化，但其泛化边界是否受限于双人博弈的简化结构，仍需进一步检验。

】

---

【Shoot First, Ask Questions Later? Building Rational Agents that Explore and Act Like People ｜贝叶斯实验设计驱动的语言模型信息获取代理

研究机构：美国麻省理工学院

作者：Gabriel Grand、Valerio Pepe、Jacob Andreas 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.20886)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.20886)

> 该方向旨在解决语言模型在动态环境中“提问”与“行动”的决策失衡问题。现有方法多依赖静态知识匹配或纯语言推理，缺乏对不确定性量化的显式建模，导致在资源受限场景下效率低下。本文切入点是将自然语言问题转化为可执行代码，结合贝叶斯实验设计（Bayesian Experimental Design, BED）计算期望信息增益。通过引入蒙特卡洛推理策略，本文实现了推理时增强，使弱模型达到超人类性能。其价值在于提供了可复用的理性代理框架，但单步前瞻策略在长程依赖任务中的有效性存疑。

】
