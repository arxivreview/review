# ACL-Findings2026 · 面向科学发现与推理的大语言模型方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【ClimAgent: LLM as Agents for Autonomous Open-ended Climate Science Analysis ｜气候科学自主智能体

研究机构：香港科技大学、山东大学

作者：Hao Wang、Jindong Han、Wei Fan 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.16922)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16922)

> 气候分析面临物理约束复杂与数据驱动特性双重挑战，现有LLM智能体多局限于简单问答，缺乏对物理机制的深度建模能力。本文切入点在于构建专用气候环境（Climate Environment, CE）以提供物理接地，并通过四阶段闭环流程实现开放式气候问题的端到端求解。ClimAgent通过检索增强与任务特定优化确保物理一致性，并在自建基准ClimaBench上验证了其相对于通用智能体的优越性。该工作填补了气候领域数据驱动基准的空白，但其泛化能力与多模态适配性仍存疑。

】

---

【GR1: Reinforcement-Enhanced LLM for Geoscience Reasoning ｜地球科学多模态推理的强化学习微调

作者：Yule Xie、Jiaxin Ding、Cheng Deng 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e3e2648ce8ae)

> 地球科学问题耦合了广域事实记忆与多步因果推理，且超过30%的题目依赖地图或剖面图，导致现有基于监督微调的专用模型难以通过自动验证信号优化深层推理能力。通用大语言模型在直接处理此类多模态任务时，常因遗漏关键视觉线索或泄露答案而失效，使得基于结果验证的强化学习无法直接应用。本文通过构建多智能体转文本管线与事实奖励机制，在纯文本环境下实现了地球科学推理能力的显著提升。该工作验证了强化学习在垂直科学领域的迁移有效性，但其将多模态问题降维为文本的处理方式，可能损失了空间推理的关键信息。

】

---

【PAPERMIND: Benchmarking Agentic Reasoning and Critique over Scientific Papers in Multimodal LLMs ｜科学文献智能体推理基准

研究机构：美国伊利诺伊大学厄巴纳-香槟分校

作者：Yanjun Zhao、Tianxin Wei、Jiaru Zou 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3662611738a2)

> 现有科学文献理解基准将多模态感知、证据检索与批判性评估割裂为孤立任务，无法衡量模型在真实科研工作流中“决策-检索-批判”的集成推理能力。PAPERMIND 通过整合真实审稿数据与工具增强推理，构建了首个覆盖多域、多任务的智能体科学文献理解基准。该基准揭示了闭源模型在集成推理上的显著优势，但 F1 分数普遍偏低且依赖 LLM-as-a-Judge 评估，其生态效度与指标客观性仍存疑。

】

---

【SciExplore: Evaluating Autonomous Agents from Scientific Navigation to Information Integration ｜科学信息检索与结构化合成基准

研究机构：中国科学技术大学

作者：Yinhao Tang、Youqing Fang、Yanan Sun 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.20926)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.20926)

> 现有科学大语言模型（LLM）评估体系割裂了通用检索与静态问答，无法衡量智能体在真实科研场景中从噪声文献中获取证据并构建结构化知识的能力。SCIEXPLORE 通过专家构建的 103 个博士级任务，将评估焦点从答案正确性转向证据接地与表格级合成。该基准揭示了当前最先进智能体在长程检索与格式遵循上的系统性失效，为科学智能体评估提供了过程级新维度，但其对“搜索深度”与任务难度关系的反直觉发现尚需更多实证支撑。

】

---

【WildSci: Advancing Scientific Reasoning from In-the-Wild Literature ｜WildSci：基于同行评审文献的科学推理强化学习数据集

研究机构：美国加州大学圣塔芭芭拉分校

作者：Tengxiao Liu、Deepak Nathani、Zekun Li 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.05567)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05567)

> 科学推理领域长期面临高质量训练数据稀缺与开放性问题难以自动验证的双重困境，导致强化学习在数学与代码领域的成功难以迁移至医学、材料等复杂学科。现有数据集多源自教科书或通用语料，缺乏研究级深度且存在数据污染风险，而开放式科学问题又无法提供明确的奖励信号。本文提出 WildSci，通过自动化管线从 Nature Communications 论文中合成 56K 道多选科学题，利用模型投票确保质量，并采用 GRPO 算法进行强化学习训练。该工作验证了文献接地数据在小模型上的有效性，但其多选格式对开放推理能力的评估边界仍存疑。

】
