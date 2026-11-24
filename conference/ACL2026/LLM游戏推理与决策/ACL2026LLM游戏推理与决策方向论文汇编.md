# ACL2026 · LLM游戏推理与决策方向论文汇编

> 本方向共 5 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【ChessArena: A Chess Testbed for Evaluating Strategic Reasoning Capabilities of Large Language Models ｜国际象棋战略推理竞技场

研究机构：南京大学、电子科技大学

作者：Jincheng Liu、Sijun He、Jingjing Wu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.24239)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24239)

> 大语言模型在静态基准上的高分无法转化为动态博弈中的胜率，核心症结在于缺乏对状态转移与对手反应的实时建模能力。现有评测多聚焦孤立问答，无法捕捉长程规划与多轮一致性，且普遍存在数据污染风险。本文构建ChessArena，通过四种对局模式解耦不同认知维度，并利用对局数据蒸馏训练集以弥合“知道-做”差距。该框架量化了当前模型在战略推理上的显著短板，但8B参数模型在移除合法动作提示后性能骤降，暗示其可能仍依赖记忆而非真正的策略理解。

】

---

【Foresight Optimization for Strategic Reasoning in Large Language Models ｜前瞻策略优化

研究机构：香港理工大学、荷兰阿姆斯特丹自由大学

作者：Jessie Wang、Jiawen Duan、Jian Wang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.13592)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f07bbd5ce2d0)

> 导读 多智能体环境中的战略推理要求模型不仅理解当前状态，还需预判对手行为并据此调整自身决策，这一“前瞻”能力在现有大语言模型（LLM）推理增强方法中缺乏显式建模。主流强化学习（RL）算法如PPO仅优化自身策略，忽略了对手策略更新对己方未来收益的反向影响，导致模型在动态博弈中表现受限。本文提出FoPO算法，通过引入耦合对手梯度的前瞻修正项，将对手建模原理嵌入策略优化过程。该方法在自建数据集上显著提升了LLM的战略推理能力，但其泛化性受限于对话类任务，未验证在复杂棋盘或实时战略游戏中的有效性。

】

---

【Generative Gamer: Learning Equilibrium Strategy by LLM-driven Dynamic Deduction ｜生成式博弈求解器：动态演绎树

研究机构：华东师范大学

作者：Yadong Zhang、Xinshu Shen、Yupei Ren 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9ffc9d718969)

> 战略博弈求解长期依赖高频率环境交互的搜索算法，而大语言模型（LLM）的高推理延迟使其无法执行每秒数千次的模拟，导致其在动态对抗中表现远逊于静态基准。现有方法或依赖外部求解器辅助，或仅优化最终胜负结果，缺乏对推理过程质量的细粒度控制。本文提出动态演绎树（Dynamic Deduction Tree, DDT），将Minimax搜索逻辑转化为LLM的单次生成任务，并通过节点级过程奖励优化策略精度。该方法在简单博弈中显著优于基线LLM，但尚未验证其在复杂高维状态空间中的泛化能力。

】

---

【Stratagem: Learning Transferable Reasoning via Trajectory-Modulated Game Self-Play ｜轨迹调制自博弈学习可迁移推理

研究机构：哈尔滨工业大学

作者：Xiachong Feng、Deyi Yin、Xiaocheng Feng 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17696)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17696)

> 游戏自博弈训练旨在将博弈中习得的策略规划能力迁移至数学与代码等下游任务，但现有方法仅依赖终端胜负信号，无法区分可泛化的抽象推理与游戏特定启发式。本文指出该失效源于“领域特异性”与“上下文静止”两个结构性障碍，并通过引入推理可迁移性系数与演化奖励对轨迹优势进行调制，选择性强化具备抽象性与渐进性的推理链。这一机制在竞赛级数学基准上实现了显著增益，但其依赖外部大模型评估器计算调制信号，且未验证该调制在需要随机策略的博弈中是否依然有效。

】

---

【TriEx: A Game-based Tri-View Framework for Explaining Internal Reasoning in Multi-Agent LLMs ｜三视图博弈解释框架

研究机构：丰田研究所

作者：Ziyi Wang、Chen Zhang、Wenjun Peng 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.20043)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.20043)

> 多智能体大语言模型（LLM）在动态博弈中的决策机制长期处于黑箱状态，现有解释方法仅能处理静态单轮任务，无法捕捉交互依赖的信念动态。本文切入点在于将解释性从自由叙事转化为结构化、可证伪的声明，通过同步记录第一人称自解释、第二人称对手信念与第三人称审计，构建可交叉验证的解释框架。TriEx在德州扑克环境中量化了解释忠实度随复杂度下降、信念对干预敏感且评估者可靠性存在层级差异。该框架填补了机制分析路线在解释忠实度维度的空白，但其结论是否泛化至非零和博弈尚存疑。

】
