# ACL-Findings2026 · 大语言模型辅助学术写作与评审方向论文汇编

> 本方向共 7 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Automatic Paper Analysis and Categorisation for Systematic Reviews with Combined Reasoning-Augmented SFT and DAPO RL ｜低资源科学论文结构化标注：推理增强SFT与DAPO强化学习

作者：Michela Lorandi、Anya Belz、Simon Mille 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b652a2a95557)

> 系统性综述（Systematic Review）的核心瓶颈在于人工标注论文分类标签的高昂成本与时效性滞后。现有大语言模型（LLM）直接生成结构化标签时，常因缺乏逻辑推理过程导致多标签预测错误及格式合规性差，且单纯监督微调（SFT）难以捕捉字段间的依赖关系。本文切入点在于将标注任务重构为推理增强分类问题，通过合成推理轨迹进行SFT，并引入动态采样策略优化（Dynamic sAmpling Policy Optimisation, DAPO）强化学习以优化奖励信号。该方法在100样本低资源约束下显著提升了标注准确率，但受限于仅评估开源模型且未对比检索增强生成（RAG）基线，其结论在闭源模型及长文本场景下的泛化性存疑。

】

---

【Can AI Revise Research Papers with Human Review Feedback? An Empirical Study and Benchmark ｜基于反馈的自主论文修订基准

作者：Zihan Luo、Hong Huang、Jianxun Lian 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_123b9d0fced9)

> 现有LLM辅助学术写作研究多聚焦于单轮生成或静态评审，缺乏对“人类反馈驱动迭代优化”这一核心科研闭环能力的量化评估。主流基准如PaperBench仅测试代码复现，忽略了评审意见理解与文本-代码联合修订的复杂性。本文通过构建包含真实ICLR 2025论文、代码仓库及评审意见的三元组数据，提出ReviseBench，利用Camera-ready版本作为人类金标准进行成对比较。该基准揭示了当前SOTA模型在学术严谨性与实验真实性上的巨大缺口，但其小规模数据集限制了结论的普适性。

】

---

【DRPG (Decompose, Retrieve, Plan, Generate): An Agentic Framework for Academic Rebuttal ｜学术反驳生成代理框架

研究机构：美国伊利诺伊大学厄巴纳-香槟分校

作者：Peixuan Han、Yingjie Yu、Jingjun Xu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.18081)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.18081)

> 学术出版流程中，作者对评审意见的回应（Rebuttal）是决定论文命运的关键环节，但现有自动化方法难以兼顾长文本理解与说服性论证。本文指出，直接调用大语言模型（LLM）生成反驳时，模型常因“中间迷失”现象忽略关键证据，且缺乏针对评审质疑的策略性规划，导致回复泛化或过度防御。DRPG通过分解、检索、规划、生成四阶段流水线，引入基于支持度评分的视角选择机制，在8B参数模型上超越人类平均反驳水平。其价值在于将辩论规划技术引入学术场景，但评估依赖LLM裁判，且未对比最新的心智理论基线，泛化性存疑。

】

---

【Feedback Is The Key for Automated Survey Generation ｜反馈驱动的可验证综述生成

研究机构：香港城市大学、华中科技大学

作者：Tianyi Xu、Zhe Zhao、Tianshuo Wei 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_048ddbd610fa)

> 自动综述生成面临的核心困境是LLM在长文本合成中产生的幻觉引用与结构松散，导致输出缺乏学术可信度。现有主流方法如AutoSurvey和SurveyX采用线性流水线，将生成视为单向过程，忽略了人类写作中至关重要的“评审-修订”迭代环节，致使引用忠实度难以保证。FIKSurvey通过引入双智能体协作机制，将同行评审范式外化为显式的反馈循环，并利用滑动窗口自然语言推理（NLI）实现引用的可验证对齐。该框架在引用召回率上显著超越基线，但其依赖闭源大模型且评估协议存在单一性，限制了其通用性与可复现性。

】

---

【GRASP: Graph-Reasoning Aided Survey Planning for High-Fidelity Related Work Generation ｜图推理辅助综述规划

作者：Haoming Li、Jessica Ouyang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d0e072d0ec69)

> 导读 自动综述生成面临的核心挑战在于，当引用文献数量超过模型上下文窗口时，LLM难以维持跨文档的逻辑一致性并准确捕捉论文间的论证关系。现有方法多依赖线性大纲或简单的引用网络特征，导致生成的相关工作部分（Related Work Section, RWS）往往沦为孤立摘要的堆砌，缺乏对研究脉络的深度整合。GRASP提出了一种双层图结构框架，结合思维图（Graph of Thoughts, GoT）与论证-反论证规划网络（Argument-Counterargument Planning Network, ACPN），并通过Steiner树剪枝保留核心语义骨架。该框架在OARelatedWork数据集上显著提升了引用意图与话语角色的保真度，但其对稀疏引用领域的泛化能力及计算开销仍存疑。

】

---

【PeerCheck: Enhancing LLM-Generated Academic Reviews Towards Human-Level Quality ｜PeerCheck：基于差异分析与提示优化的LLM学术评审增强框架

作者：Zeyuan Chen、Ziqing Yang、Yihan Ma 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.20897)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.20897)

> 导读

】

---

【RbtAct: Rebuttal as Supervision for Actionable Review Feedback Generation ｜基于反驳监督的可执行评审生成

研究机构：美国耶鲁大学、美国纽约大学

作者：Sihong Wu、Yiling Ma、Yilun Zhao 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.09723)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.09723)

> 同行评审自动化长期面临“生成流畅但缺乏行动指导”的困境，现有方法多依赖静态标注或通用提示，无法捕捉评论对作者实际修改行为的因果影响。RBTACT 将作者反驳（Rebuttal）转化为隐式偏好信号，通过直接偏好优化（DPO）训练模型生成能触发具体修改的评审片段。该方法在 8B 参数规模下实现了超越 70B 通用大模型的可执行性评分，但其效果高度依赖反驳数据的对齐质量，且未验证对最终论文录用率的直接贡献。

】
