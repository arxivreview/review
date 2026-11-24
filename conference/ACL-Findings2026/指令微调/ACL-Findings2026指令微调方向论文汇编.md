# ACL-Findings2026 · 指令微调方向论文汇编

> 本方向共 6 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Data Selection for Multi-turn Dialogue Instruction Tuning ｜多轮对话指令微调的数据选择

研究机构：北京大学

作者：Bo Li、Shikun Zhang、Wei Ye

论文原文见 [arXiv](https://arxiv.org/abs/2604.07892)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07892)

> 导读 多轮对话指令微调面临的核心矛盾是：大规模对话语料虽能提供丰富的交互轨迹，但其中充斥着主题漂移、重复闲聊及格式错配等结构性噪声，直接训练会损害模型在长对话中的连贯性与任务执行能力。现有单轮数据选择方法将对话拆解为独立指令对，忽略了跨轮次的语义依赖与结构完整性，导致筛选出的子集在长对话场景下表现退化。本文提出 MDS（Multi-turn Dialogue Selection），通过全局语义覆盖与局部结构可靠性的两阶段联合优化，在固定预算下筛选出既多样又结构完整的多轮对话子集。该方法在通用与领域特定语料上均优于单轮选择器及对话级评分基线，但其对分箱数量敏感性及跨域泛化边界的量化验证仍显不足。

】

---

【Empirical Analysis of Task Mixture Effects in Small-scale Instruction Tuning: A Statistical Approach ｜无标签指令语料的任务混合统计优化

研究机构：韩国科学技术院

作者：Jeesu Jung、Sangkeun Jung

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ff89e41f116b)

> 指令微调的性能高度依赖训练数据中任务类型的比例，但现有研究多依赖人工标注或固定比例，缺乏对无标签语料中任务交互效应的定量分析。本文提出一种最小监督框架，利用种子指令嵌入检索自动识别任务，并通过统计混合建模量化不同任务组合在多种数据规模下的协同与干扰效应。该方法将混合比例设计转化为可统计检验的优化问题，揭示了编程与数学任务的协同性及编程与创意写作的干扰性。其价值在于提供了可解释的混合设计指南，但实验局限于小模型与特定数据集，结论向大模型泛化的能力存疑。

】

---

【GCIG: GraphRAG-based Cross-document Instruction Generation for Boosting LLM Reasoning ｜基于图检索的跨文档指令生成

作者：Xiaoliang Xu、Huang Yuan、Junmei Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9f7cd3b98e26)

> 现有自动指令生成方法在处理知识密集型领域时，常因依赖单文档片段而导致多跳推理指令缺乏逻辑连贯性。本文指出，缺乏跨文档证据的结构化组织是造成指令逻辑扁平化与事实幻觉的核心瓶颈。GCIG 框架通过构建增强知识图谱并引入思维链引导的答案生成机制，自动化合成具备可追溯证据链的高质量指令数据。该方法在 HotpotQA 等基准上显著提升了多跳推理性能，但其对高文档密度场景下的噪声抑制能力仍显不足。

】

---

【Meeseeks: A Feedback-Driven, Iterative Self-Correction Benchmark evaluating LLMs’ Instruction Following Capability ｜多轮迭代指令遵循基准

研究机构：美团

作者：Jiaming Wang、Yunke Zhao、Peng Ding 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8021b9dbd77d)

> 大语言模型在单次响应中难以同时满足复杂多约束指令，而现有评估基准仅关注单轮静态表现，无法量化模型在反馈驱动下的自我修正上限。Meeseeks 通过引入 20 轮迭代反馈机制，将评估从“单次成功率”转向“能力上限探测”，并采用代码引导的规则增强评估框架解决长文本提取的准确性与成本瓶颈。该基准揭示了模型单次表现与最终能力上限的巨大差距，但受限于自建数据集分布，其结论在跨基准泛化性上仍存疑。

】

---

【PlanE: Meta Planning of Data, Tuning, and Inference for Extractive-based LLMs ｜面向信息抽取的LLM构建元规划框架

作者：Jiacheng Wang、Weiyan Zhang、Guangya Yu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a180f129a762)

> 信息抽取（IE）任务中，大语言模型（LLM）的指令微调面临数据标注成本高且缺乏针对特定任务的最优配置策略的困境。现有方法多聚焦于单一环节优化，如数据筛选或强化学习，却忽略了数据、训练与推理三者的联合配置对最终性能的非线性影响。本文提出PlanE框架，通过元学习自动选择最优的“数据-训练-推理”（DTI）组合，以平衡构建效率与模型性能。该框架在特定IE任务上实现了与网格搜索持平的性能，但显著降低了搜索成本，其通用性仍存疑。

】

---

【Self-Guided Plan Extraction for Instruction-Following Tasks with Goal-Conditional Reinforcement Learning ｜自引导计划提取与目标条件强化学习

作者：Zoya Volovikova、Nikita Sorokin、Dmitriy Lukashevskiy 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.20601)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.20601)

> 具身智能体在动态开放环境中遵循自然语言指令时，面临长程依赖与稀疏奖励导致的信用分配难题。现有基于演示的方法受限于数据成本，而纯强化学习方法在缺乏预定义技能库时难以将语言指令映射到具体动作。SuperIgor 通过 LLM 与 RL 智能体的迭代共训练，利用 DPO 反馈闭环自动筛选高价值计划，实现了无预定义技能库下的指令遵循。该框架在 CrafText 基准上显著优于纯 RL 基线，但计算成本高昂且与 Oracle 计划仍存在性能差距，其自学习闭环的收敛效率尚待验证。

】
