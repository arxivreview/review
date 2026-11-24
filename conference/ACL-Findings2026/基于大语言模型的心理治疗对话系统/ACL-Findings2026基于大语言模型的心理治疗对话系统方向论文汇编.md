# ACL-Findings2026 · 基于大语言模型的心理治疗对话系统方向论文汇编

> 本方向共 12 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CFlowPsyD: An Analysis-Enhanced Dataset for Asynchronous Psychological Counseling through Self-Optimizing Multi-Agent Framework ｜异步心理咨询对话合成框架

研究机构：中国科学院、北京理工大学

作者：Donghao Li、Yifan Deng、Jinta Weng 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1db0fd52dfea)

> 异步心理咨询（Asynchronous Psychological Counseling, APC）旨在通过时空解耦的交互模式，支持认知行为疗法（CBT）等依赖客户自主反思的循证干预，但真实语料因隐私法规极度稀缺。现有同步心理咨询（SPC）数据集缺乏深层分析推理，且静态多智能体框架无法捕捉客户跨轮次的情绪与认知演变。本文提出自优化多智能体框架 CFlowPsy，利用动态画像模块 Persona-Flow 实时追踪客户状态，并注入显式思维链以生成高质量 APC 对话。该框架发布了首个中文 APC 数据集 CFlowPsyD，在一致性与真实性上优于现有同步数据集，但其评估局限于中文同步基线，缺乏与最新多智能体合成框架的直接对比。

】

---

【CogEmp:A Cognitive Empathy-Oriented Dialogue System for Structured Psychological Counseling ｜认知共情导向的心理咨询对话系统

作者：Yiguo Deng、Xia Lei、Yuan Zhang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_51c2ca5c0351)

> 现有LLM心理咨询系统多停留在情感共鸣层面，缺乏对用户情绪背后深层心理动因的建模能力，导致干预流于表面安慰。本文切入点在于将认知共情操作化为“情绪识别+因果归因”的双轨任务，通过合作博弈论算法自动提取情绪触发源，并以此驱动检索增强生成。具体做法是构建识别-理解-生成三阶段流水线，利用Harsanyi分解定位情绪原因，再匹配主题与策略生成响应。该方案在中文共情基准上显著优于基线，但其因果归因仅作用于单轮输入，且依赖合成数据，深层信念追踪能力存疑。

】

---

【MIThinker: A Plug-and-Play Policy-Optimized Thinker For Motivational Interviewing Counseling ｜解耦式思维生成与策略对齐

研究机构：北京理工大学、新加坡管理大学

作者：Yizhe Yang、Palakorn Achananuparp、Heyan Huang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_98ca20f8f58f)

> 动机访谈（Motivational Interviewing, MI）咨询要求模型在生成回复前，先完成对客户心理状态的评估与策略选择，但现有大语言模型（LLM）往往直接生成回复，缺乏显式的临床推理过程，导致干预缺乏深度且计算开销巨大。本文切入点在于将“思维生成”与“响应生成”解耦，提出轻量级思维模型 MIThinker，通过逆向工程构建思维数据并采用强化学习优化策略对齐。该方法以极低的计算成本实现了接近多智能体框架的临床保真度，但其对复杂危机情境的覆盖能力仍存疑。

】

---

【PhaseMI: A Motivational Interviewing Dataset for Enhancing Phase Progression in LLM-based Counseling ｜阶段结构化动机访谈数据集

研究机构：韩国科学技术院、韩国高丽大学

作者：Jina Kim、Myeongho Jeon、Soohyun Cho 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a25eab4e18f1)

> 现有动机访谈（Motivational Interviewing, MI）数据集缺乏对咨询阶段结构的显式建模，导致模型在长对话中易发生治疗漂移，无法有效引导客户从探索走向行动规划。本文通过引入监督者大语言模型（Supervisor LLM）显式控制阶段转换，构建了包含13,897条对话的PHASEMI数据集。该方法在指导（Guiding）和选择（Choosing）阶段的覆盖率上显著优于基线，验证了结构化生成对提升临床逻辑一致性的作用，但其依赖合成数据且未评估真实临床场景下的泛化能力。

】

---

【Preference Learning Unlocks LLMs’ Psycho-Counseling Skills ｜基于专业原则的心理咨询偏好对齐

研究机构：美国匹兹堡大学

作者：Mian Zhang、Shaun M. Eack、Zhiyu Chen

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cc440e110757)

> 该方向旨在解决大语言模型在心理咨询场景中因缺乏真实临床数据监督而导致的响应质量不稳定问题。现有方法多依赖通用对话数据或单一维度的情感评估，无法捕捉循证心理治疗中关于自主性、阶段敏感性等深层专业逻辑，导致模型响应虽流畅但缺乏临床有效性。本文切入点在于构建一套由社会工作与精神病学专家定义的七维专业评估原则，并以此生成大规模偏好数据集 PsyCoPref，通过迭代式直接偏好优化（Iterative DPO）训练模型。其价值在于证明了领域特定偏好数据能显著提升小参数模型对 GPT-4o 的胜率，但存疑点在于该评估体系是否过度依赖 GPT-4o 作为裁判的隐性偏差。

】

---

【PsyChain: A Collaborative Chain-of-Agents Framework for Generating Personalized and Professional Counseling Dialogues ｜基于人格原型的链式智能体心理咨询对话生成框架

研究机构：北京交通大学

作者：Yi Feng、Zijie Yang、Chen Zhang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d693979079cb)

> 现有心理咨询数据集普遍存在客户画像同质化、治疗深度不足及过程不可控的缺陷，导致模型生成的响应缺乏临床针对性。PsyChain 通过引入 DSM-5 人格原型与多智能体协作机制，将静态语料转化为高保真对话。该框架利用六个专职智能体模拟完整的咨询流程，在自建数据集上验证了其在认知重构与策略专业性上的优势，但其合成数据能否替代真实临床数据的等效性仍存疑。

】

---

【PsychePass: Calibrating LLM Therapeutic Competence via Trajectory-Anchored Tournaments ｜轨迹锚定锦标赛校准大模型治疗能力

研究机构：中南大学、清华大学

作者：Zhuang Chen、Dazhen Wan、Zhangkai Zheng 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.20330)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.20330)

> 大语言模型在心理咨询中的评估长期受困于“无锚定缺陷”：模拟对话缺乏临床方向导致过程漂移，静态评分缺乏参照导致标准漂移，使得现有基准无法区分模型的真实治疗能力。PSYCHEPASS 通过基于单会话疗法理论的脚本化探针锚定交互轨迹，并利用瑞士制锦标赛与 Bradley-Terry 模型锚定判断轨迹，将评估转化为可优化的奖励信号。该框架实现了从评估到强化学习优化的闭环，但其在危机干预维度上的性能回退提示了疗效与安全性的潜在冲突。

】

---

【PsychEval: A Multi-Session and Multi-Therapy Benchmark for High-Realism AI Psychological Counselor ｜多会话多疗法心理咨询基准

研究机构：华东师范大学

作者：Qianjun Pan、Junyi Wang、Jie Zhou 等 13 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.01802)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.01802)

> 现有AI心理咨询评估体系受限于单轮静态问答，无法捕捉治疗过程中的纵向动态与多流派技术差异，导致模型在长程对话中易出现治疗漂移。本文通过重构369份真实临床案例报告，构建了覆盖5种疗法、平均7.6个会话的纵向基准，并引入层级技能树与双维评估框架。其价值在于填补了动态临床保真度评估的空白，但基于LLM-as-a-Judge的评估协议是否真正消除了主观偏差，仍存疑。

】

---

【Psychological Counseling Cannot Be Achieved Overnight: Automated Psychological Counseling Through Multi-Session Conversations ｜多会话心理咨询中的纵向一致性建模

研究机构：哈尔滨工业大学

作者：Bichen Wang、Junzhe Wang、Yixin Sun 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_873f6ad96583)

> 自动化心理咨询长期受限于单会话设定，无法模拟真实治疗中跨次数的状态演进与目标调整，导致模型在长程交互中出现治疗漂移。现有合成数据集多聚焦单轮或简单多轮扩展，缺乏对客户心理状态动态变化的结构化追踪。本文通过构建基于认知行为疗法（CBT）的多会话数据集 MusPsy-Dataset，并训练具备记忆增强能力的 MusPsy-Model，实现了会话间目标的动态规划与一致性维持。该工作验证了结构化记忆对纵向咨询质量的提升作用，但其依赖 LLM 模拟客户的评估协议可能高估实际临床疗效。

】

---

【Schema-Guided Response Generation using Multi-Frame Dialogue State for Motivational Interviewing Systems ｜基于多帧对话状态的动机访谈响应生成

作者：Jie Zeng、Yukiko Nakano

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_98d0df49da8a)

> 动机访谈（Motivational Interviewing, MI）旨在通过协作式对话激发客户内在改变动机，而非由咨询师直接提供建议。现有大语言模型（LLM）驱动的MI系统常陷入“建议导向”陷阱，即过度依赖AI生成具体解决方案，导致客户自主性丧失与改变谈话（Change Talk, CT）频率低下。本文提出SGR-MI，通过多帧对话状态追踪与基于检索的对话策略生成，在低资源场景下实现MI原则的严格遵循。该方法在真实用户研究中显著降低了非MI行为率并提升了CT激发效率，但其策略池的构建依赖LLM生成的伪策略，缺乏独立临床验证，且文本交互形式限制了CT的绝对数量上限。

】

---

【StoryMI: Steerable Multi-Agent Therapeutic Dialogue Generation ｜情境化多智能体动机访谈对话生成

研究机构：荷兰阿姆斯特丹自由大学、日本国立情报学研究所

作者：Qingyu Meng、Min Chen、Dingming Liu 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d01a0b722a42)

> 动机访谈（Motivational Interviewing, MI）对话生成面临情境缺失与策略僵化的双重困境，导致模型难以维持长程临床逻辑。现有方法或依赖手工脚本，或仅做单轮代码预测，无法实现动态的宏观策略控制。StoryMI 通过问卷生成情境故事，并引入交互代理动态选择 MI 代码，实现了可控的多轮治疗对话。该框架在自建基准上验证了宏观策略的有效性，但其评估体系未涵盖安全约束，且缺乏与最新多智能体框架的直接对比。

】

---

【TRACE: Two-Phase RL for Causal Graph Exploration and Deeper Psychological Intervention in Dynamic Counseling Scenarios ｜因果图重构驱动的双阶段强化学习心理干预框架

研究机构：西安电子科技大学、北京师范大学

作者：Shilin Tang、Zunyi Yin、Xuefeng Liang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5ce838746ee5)

> 现有大语言模型心理咨询系统受限于表面情绪响应，缺乏对深层认知因果链的主动探索能力，导致干预无法触及核心信念。本文切入点在于将咨询过程形式化为在线因果图重构问题，通过双阶段强化学习强制模型遵循“先探索后干预”的临床逻辑。具体做法是利用因果图填充状态作为奖励信号，训练模型在对话中逐步还原客户心理结构并实施针对性认知重构。该框架在自建基准上显著优于基线，但其依赖LLM生成的理想因果图质量，且缺乏跨基准的泛化验证，临床等效性存疑。

】
