# Others2026 · 大语言模型安全对齐与拒答机制方向论文汇编

> 本方向共 1 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Refusal Steering: Fine-grained Control over LLM Refusal Behaviour for Sensitive Topics ｜拒绝转向：基于岭正则化激活引导的政治敏感话题细粒度控制

作者：Iker García-Ferrero、David Montero、Roman Orus

论文原文见 [arXiv](https://arxiv.org/abs/2512.16602)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.16602)

> 导读 大语言模型在政治敏感话题上常表现出意识形态偏见，导致对合法信息的过度拒绝，而传统微调方法因成本高且易破坏通用能力而难以精准修正。现有激活引导方法依赖简单的均值差或模式匹配，无法处理现代推理模型中复杂的、非显式的拒绝行为（如宣传式回答）。本文提出一种推理时干预方法，通过LLM-as-a-judge量化拒绝置信度，并引入岭正则化变体计算更鲁棒的转向向量，在不重训练的前提下实现政治拒绝的移除或引入。该方法在80B模型上有效降低了政治拒绝率并保持了安全性，但在小模型上安全性显著下降，其解耦能力的边界尚存疑。

】
