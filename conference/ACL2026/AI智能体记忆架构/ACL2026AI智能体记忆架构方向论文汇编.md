# ACL2026 · AI智能体记忆架构方向论文汇编

> 本方向共 2 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CloneMem: Benchmarking Long-Term Memory for AI Clones ｜基于非对话数字痕迹的AI克隆记忆基准

研究机构：北京大学

作者：Sen Hu、Zhiyu Zhang、Yuxiang Wei 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.07023)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.07023)

> 现有智能体记忆系统依赖对话历史，无法捕捉个体在日记、邮件等非对话痕迹中呈现的连续情感与观点演化轨迹。本文切入点在于将记忆评估从离散会话迁移至纵向生活流，并揭示现有巩固机制在此场景下的保真度缺陷。通过层级化生成非对话痕迹并设计轨迹追踪任务，实验表明扁平检索优于结构化巩固，但所有系统均远低于Oracle上限。该基准填补了个性化AI克隆的记忆评估空白，但其合成数据特性与单一模态限制了结论向真实场景的泛化。

】

---

【Does Memory Need Graphs? A Unified Framework and Empirical Analysis for Long-Term Dialog Memory ｜对话记忆系统统一框架与实证分析

研究机构：北京大学

作者：Sen Hu、Yuxiang Wei、Jiaxin Ran 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.01280)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.01280)

> 长期对话记忆系统面临的核心矛盾是：图谱结构被广泛采用以捕捉实体关联，但不同研究在相同基准上报告了相互矛盾的性能结论，导致无法归因于具体设计选择。现有方法缺乏统一的系统级框架，各组件（表示、索引、检索）的实现细节不一致，使得跨研究比较失效。本文提出一个六元组统一框架，将图谱与非图谱方法纳入同一分析空间，并通过受控消融实验识别出稳定的强基线配置。其价值在于提供了可复现的对比基准，但实验仅覆盖两种骨干模型组合，且未验证图结构在超大规模记忆库下的扩展性。

】
