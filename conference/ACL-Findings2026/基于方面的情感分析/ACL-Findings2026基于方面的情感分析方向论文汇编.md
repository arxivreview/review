# ACL-Findings2026 · 基于方面的情感分析方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【E-ABSA20K: A Dataset and Propose-and-Verify for Aspect-Based Sentiment Analysis in Long E-commerce Reviews ｜长电商评论方面级情感分析的两阶段提议-验证框架

作者：Tong Sun、Mingyang Ma、Cheng Yu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dd9e5c7a411b)

> 长电商评论中的方面级情感分析（ABSA）面临跨句证据分散、多粒度目标混淆及单次生成导致的范围泄漏难题，现有单次生成范式在长文本中易产生未接地或越界四元组。本文针对此瓶颈，构建了包含2万条长评论的多域数据集E-ABSA20K，并提出解耦高召回提议与严格验证整合的两阶段框架。该方法通过显式的接地性、范围与模态检查抑制幻觉，但其在服务类方面上的高错误率及固定清单的局限性，限制了其在复杂语境下的泛化能力。

】

---

【Tree-CoT-RT: An Explainable Multi-Path Tree-Guided Chain-of-Thought and Reinforcement Learning Framework for Aspect Sentiment Quad Prediction ｜树引导思维链与强化学习框架

研究机构：浙江大学、香港理工大学

作者：Hao Zhang、Jiahao Wang、Zhenke Duan 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ff9bf142340e)

> 方面情感四元组预测（Aspect Sentiment Quad Prediction, ASQP）旨在从文本中同时提取方面、类别、观点词与情感极性，其核心难点在于隐式元素缺乏显式文本线索，导致传统生成模型易产生逻辑无效或结构不一致的输出。现有基于大语言模型（LLM）的方法虽提升了泛化能力，但推理过程黑盒化且缺乏对隐式推理路径的结构约束，难以保证输出的可解释性与鲁棒性。本文提出 Tree-CoT-RT 框架，通过类型特定的树结构引导思维链生成，并结合基于组相对策略优化（Group Relative Policy Optimization, GRPO）的强化学习筛选高质量推理路径，最终通过自一致性投票输出四元组。该框架在 REST-ACOS 与 LAPTOP-ACOS 基准上取得了当前最优性能，尤其在隐式情感子集上优势显著，但其规则奖励函数对语义细微差别的覆盖能力仍存疑。

】
