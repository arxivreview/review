# ACL-Findings2026 · 可解释人工智能中的反事实解释方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Counterfactual Explanation Framework for Retrieval Models ｜检索模型反事实解释框架

研究机构：英国利物浦大学

作者：Bhavik Chandna、Procheta Sen

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1f74cf54d14d)

> 信息检索（IR）系统的可解释性长期聚焦于“为何文档被检索”，却忽视了“为何相关文档未被检索”这一关键盲区。现有解释方法无法回答哪些缺失词汇导致文档排名跌出Top-K，阻碍了模型偏差的诊断与修正。本文提出CFIR框架，通过构建局部二分类器并优化词频向量，生成仅包含新增词汇的反事实解释。该框架在多种检索模型上验证了有效性，但其解释的语义连贯性与因果有效性仍存疑。

】

---

【LIBERTy: A Causal Framework for Benchmarking Concept-Based Explanations of LLMs with Structural Counterfactuals ｜基于结构因果模型的LLM概念解释基准

研究机构：以色列理工学院

作者：Gilat Toker、Nitay Calderon、Ohad Amosy 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.10700)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.10700)

> 概念解释的忠实度评估长期受困于缺乏真实因果机制作为参照，导致现有方法无法区分统计关联与因果效应。Abraham et al. (2022) 提出的 CEBaB 虽引入干预数据集，但受限于人工标注成本、短文本场景及简单因果图，无法适配 LLM 的复杂生成过程。LIBERTy 通过显式定义文本生成的结构因果模型（SCM），利用 LLM 作为 SCM 组件自动生成结构反事实，从而构建具有因果对齐的评估基准。该框架解决了评估参考值与数据生成过程（DGP）脱节的问题，但受限于合成数据的分布偏差，其结论在真实世界文本上的泛化性存疑。

】
