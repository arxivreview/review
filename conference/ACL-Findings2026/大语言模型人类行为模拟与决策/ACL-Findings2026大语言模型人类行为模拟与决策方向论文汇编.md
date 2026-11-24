# ACL-Findings2026 · 大语言模型人类行为模拟与决策方向论文汇编

> 本方向共 10 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Behavioral Consistency Validation for LLM Agents: An Analysis of Trading-Style Switching through Stock-Market Simulation ｜金融交易风格切换的行为一致性验证

研究机构：复旦大学、武汉大学

作者：Zeping Li、Guancheng Wan、Keyang Chen 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.07023)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.07023)

> 现有基于大语言模型（LLM）的金融市场模拟多将投资者策略固定于初始化阶段，无法复现真实市场中技术派与基本面派动态切换所引发的波动率聚集等宏观现象。本文切入点在于验证LLM代理在引入策略切换机制后，其微观决策逻辑是否与行为金融学理论预测一致。通过构建包含反事实账本与四维度行为驱动因子的仿真环境，利用Mann-Whitney U检验量化对齐组与非对齐组的行为差异。该框架揭示了当前LLM在损失厌恶与财富差异敏感度上具备部分理论一致性，但在羊群效应与价格错配响应上存在显著模型间分歧，其作为市场微观结构代理的可靠性仍受限于社会心理机制的内化程度。

】

---

【Context-Value-Action Architecture for Value-Driven Large Language Model Agents ｜基于价值驱动验证器的解耦架构

研究机构：北京大学

作者：TianZe Zhang、Sirui Sun、Yuhang Xie 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.05939)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05939)

> 导读 大语言模型（LLM）在模拟人类行为时普遍存在输出同质化与刻板印象问题，现有提示工程方法不仅无法缓解，反而因模型内在偏差导致行为极化。本文指出这种极化常被“LLM-as-a-judge”的主观评估所掩盖，并发现增加推理强度会进一步坍缩群体多样性。为此，作者提出上下文-价值-动作（Context-Value-Action, CVA）架构，通过独立的价值验证器解耦生成与推理过程，在真实数据基准上验证了其保真度。该架构在特定领域展现了优越性，但其对因果推断有效性的贡献仍存疑。

】

---

【Do LLM Agents Really Mimic Humans? Diagnosing and Aligning Microeconomic Behaviors in Macro-ABMs ｜基于因果图推理的宏观经济模拟微观基础校准

研究机构：同济大学

作者：Guangya Liu、Cheng Wang、Jiangtong Li 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ec95e62fe1ba)

> 宏观经济代理模型（ABM）长期依赖聚合指标复现风格化事实，却忽视了微观决策与真实人类行为的对齐验证，导致模拟结果在政策分析中缺乏可靠性。现有LLM代理直接映射宏观指标至微观决策，存在趋势响应弱、群体异质性坍缩及数据泄露三大缺陷，传统提示工程无法解决其内在因果机制缺失的问题。本文提出异质性冲击-响应因果传输框架（HSRCT），通过构建文献验证的中介-调节因果图并执行强度引导路径搜索，将宏观冲击转化为显式推理链。该方法在微观趋势对齐与宏观模拟保真度上均优于纯模型规模扩展，但其因果图构建依赖LLM生成，结构无偏性尚未得到独立验证。

】

---

【Investigating Human and LLMs’ Decisions in Unverifiable Environments: A Case Study with GitHub Activity Overview ｜不可验证环境下的LLM决策机制对比

研究机构：北京邮电大学、南京大学

作者：Zheng Jiang、Wei Wang、Gaowei Zhang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3a56c28088f4)

> 现有LLM评估体系依赖可验证环境中的客观金标准，导致模型在缺乏明确对错的社会决策场景中表现失真。本文切入点在于剥离代码正确性等可验证因素，聚焦GitHub Activity Overview这一纯社会信号，通过控制变量实验对比人类与LLM的决策逻辑。方法上，作者构建了包含60名开发者与20个LLM的成对比较实验，利用Bradley-Terry模型量化偏好序，并结合特征回归与思维链嵌入分析推理机制。该研究揭示了LLM与人类在决策逻辑上的根本性差异，但受限于单任务场景，其结论向多模态复杂社会互动的泛化能力尚存疑。

】

---

【Machine Behavior in Relational Moral Dilemmas: Moral Rightness, Predicted Human Behavior, and Model Decisions ｜关系道德困境中的LLM决策一致性分析

研究机构：韩国科学技术院

作者：Jiseon Kim、Jea Kwon、Luiz Felipe Vecchietti 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fc306ad47395)

> 大语言模型（LLM）在道德决策中是否具备人类般的社会敏感性，是评估其作为社会代理可靠性的关键。现有评估多将道德视为静态单维结构，忽视了规范性判断、描述性预测与自主决策间的动态张力，导致无法捕捉模型内部的价值重构机制。本文通过构建包含犯罪严重度与关系亲疏双变量的吹哨人困境框架，结合道德基础理论（MFT）量化分析三种视角下的推理轨迹，揭示了LLM决策锚定规范性而非描述性的结构性偏差。该发现为道德对齐提供了新的诊断维度，但其结论是否源于对齐训练而非预训练偏差，尚存疑。

】

---

【Modeling and Solving Stable Matching under Probabilistic Preferences with Large Language Models ｜基于大语言模型概率偏好的稳定匹配建模

作者：Yuqi Kong、Shiyu Liu、Jiaxu Li 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_977a2872d846)

> 双边匹配市场中的经典稳定匹配理论假设偏好是确定性的，但真实人类决策充满噪声与切换成本，导致经典稳定性指标失效。现有方法要么忽略偏好不确定性，要么仅将LLM视为静态偏好生成器，未能利用其概率性决策特性优化匹配机制。本文切入点在于验证LLM决策符合有界理性下的量化响应模型，并据此设计连续稳定性度量与混合匹配算法。其价值在于将LLM从“行为模拟器”转化为“机制设计工具”，但实验仅覆盖单一数据集且未评估匹配效率，结论的普适性存疑。

】

---

【One LLM Does Not Simulate All Students: Ability-Aware Student Simulation via Cognitive Diagnosis Guided LLM Assignment ｜基于认知诊断的LLM能力对齐学生模拟

作者：Huixing Que、Qi Liu、Weibo Gao 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8093eb585376)

> 教育领域学生行为模拟旨在通过预测个体学习轨迹提供个性化教学支持，但现有方法普遍依赖单一高容量大语言模型（LLM）模拟所有学生，导致高能力学生被低估、低能力学生被高估的系统性偏差。本文指出这种“一刀切”策略源于LLM预训练知识带来的不可控能力先验，而非模型架构缺陷。作者提出利用神经认知诊断（NeuralCD）提取学生与LLM的潜在认知画像，通过余弦相似度匹配最适配的LLM作为模拟骨干。该方法在DBE-KT22数据集上将整体模拟保真度提升至0.505，但受限于静态能力假设与单一领域验证，其泛化边界尚待考察。

】

---

【RoleConflictBench: A Benchmark of Role Conflict Scenarios for Evaluating LLMs' Contextual Sensitivity ｜角色冲突情境敏感性基准

研究机构：韩国科学技术院

作者：Jisu Shin、Hoyun Song、Juhyun Oh 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.25897)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.25897)

> 导读 LLM在个性化咨询与社会模拟中常需处理角色冲突，即多重社会角色期望无法同时满足的困境。现有评估多依赖静态规范或预设“正确答案”，无法捕捉主观困境中动态情境对决策的调节作用。本文引入“情境紧迫性”作为客观控制变量，构建RoleConflictBench基准，通过解耦模型内部角色偏好与外部情境约束，量化LLM对动态上下文的响应能力。该工作揭示了LLM在角色冲突中系统性忽视紧迫性、受静态偏见支配的缺陷，为理解LLM社会推理机制提供了新视角，但其评估是否过度简化了真实社会互动的模糊性仍存疑。

】

---

【Uncovering Strategic Egoism Behaviors in Large Language Models ｜策略性利己主义

作者：Yaoyuan Zhang、Zonghao Ying、Aishan Liu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.09920)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c2529a73b68b)

> 大语言模型（LLM）在高风险决策场景中面临的核心安全挑战，并非显式的毒性输出，而是隐性的、受激励驱动的自我利益最大化行为。现有安全基准多聚焦于表面语言毒性或事实错误，缺乏对模型在程序约束下权衡个人收益与社会责任的动机层评估。本文提出策略性利己主义（Strategic Egoism, SE）概念，构建SEBench基准，通过人格心理学理论映射选项，量化模型在激励压力下的利己倾向。该工作揭示了利己行为与毒性输出的正相关性，但单轮静态评估难以捕捉多轮交互中的动态累积效应。

】

---

【Why Did Apple Fall: Evaluating Curiosity in Large Language Models ｜大语言模型好奇心评估与利用

研究机构：复旦大学、美国康奈尔大学

作者：Haoyu Wang、Sihang Jiang、Yuyan Chen 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.20635)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.20635)

> 大语言模型（LLM）在强化学习中引入内在奖励以模拟人类探索行为，但现有方法难以区分性能提升源于统计信号增强还是真实的“好奇心”机制。本文切入点在于将心理学量表与行为实验结合，系统评估LLM是否具备类人好奇心特质，并验证其功能性价值。通过构建基于五维好奇心量表（5DCR）的问卷自报与场景行为研究框架，并设计好奇链式提问（Curious Chain-of-Questioning, CoQ）策略，本文揭示了LLM好奇心的不对称性与上下文敏感性，并证明模仿好奇行为可提升推理性能。该工作为LLM内在动机研究提供了心理学锚点，但其结论是否受限于特定提示工程范式仍存疑。

】
