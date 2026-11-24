# ACL-Findings2026 · 语言模型中的性别偏见方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【From If-Statements to ML Pipelines: Revisiting Bias in Code-Generation ｜代码生成中的隐性偏见：从条件语句到机器学习管道

研究机构：美国科罗拉多大学博尔德分校

作者：Minh Duc Bui、Xenia Heilmann、Mattia Cerrato 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.21716)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1c07c93183ff)

> 代码生成模型在构建决策系统时，常将敏感属性作为预测特征，导致隐性歧视。现有评估仅检测显式条件语句，严重低估了实际部署中的偏见风险。本文通过对比条件语句与完整机器学习管道的特征选择行为，量化了这一评估盲区。该工作揭示了评估范式的结构性缺陷，但未提供去偏方案，其结论对模型内部机制的解释力仍待检验。

】

---

【Real Men are Tough: Evaluating Gender Bias and Sensitivity to Masculinity Norms in LLMs ｜男性规范作为潜在先验的隐性偏见评估

作者：Elisa Leonardelli、Camilla Casula、Boglarka Nyul 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a7dcfc7b119f)

> 语言模型在证据不足时，往往依赖社会规范填补信息空白，但现有评估多聚焦于显式刻板印象输出，忽略了规范作为“潜在先验”在歧义推理中的隐性作用。本文切入点在于区分“显式同意”与“隐式依赖”，通过构建基于心理学量表的场景推断基准，量化模型在信息缺失时对男性规范的归因倾向。其核心做法是设计消歧与歧义变体，控制性别标记，测量模型在不确定性下的行为偏移。该工作揭示了表面合规与内部偏见脱节的机制，但缺乏对去偏干预的验证，且评估范围局限于英语和意大利语。

】
