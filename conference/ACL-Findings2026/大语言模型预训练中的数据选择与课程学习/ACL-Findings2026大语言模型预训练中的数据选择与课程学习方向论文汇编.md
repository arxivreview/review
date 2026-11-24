# ACL-Findings2026 · 大语言模型预训练中的数据选择与课程学习方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Diversity Diet for a Healthier Model: A Case Study of French ModernBERT ｜词汇多样性驱动的预训练数据采样

研究机构：法国巴黎萨克雷大学、法国国家科学研究中心

作者：Louis Estève、Christophe Servan、Thomas Lavergne 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a90563273852)

> 预训练数据规模扩张伴随算力成本激增，而自然文本的冗余性导致随机扩充数据的边际多样性收益递减。现有数据策展方法多聚焦于动态权重调整或质量过滤，忽略了静态子集选择中词汇分布的结构性优化空间。本文提出基于Shannon熵最大化的离线采样算法，在固定算力下将预训练数据缩减94%且维持或提升性能。该策略在编码器预训练场景下验证了多样性对数据量的替代效应，但其结论能否迁移至自回归大语言模型（LLM）尚存疑。

】

---

【Heterogeneity in Formal Linguistic Competence of Language Models: Is Data the Real Bottleneck? ｜语法范式数据稀缺性诊断与最小干预

作者：H S V N S Kowndinya Renduchintala、Sumit Bhatia

论文原文见 [arXiv](https://arxiv.org/abs/2604.17930)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17930)

> 大语言模型在通用基准上表现优异，却在特定语法范式上出现低于随机猜测的失败，且单纯扩大预训练数据量无法解决这一异质性。现有宏观数据混合优化方法关注全局分布比例，缺乏对微观语法结构暴露量的因果归因能力，导致无法区分架构限制与数据稀缺。本文通过向预训练语料中注入1%的定向合成文本，验证了数据稀缺是主要瓶颈。该研究提供了“数据阈值”的新视角，但仅在小规模模型上验证，其结论向大规模模型的迁移性存疑。

】
