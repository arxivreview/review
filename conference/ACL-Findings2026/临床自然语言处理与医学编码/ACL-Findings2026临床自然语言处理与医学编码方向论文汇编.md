# ACL-Findings2026 · 临床自然语言处理与医学编码方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【MedDCR: Learning to Design Agentic Workflows for Medical Coding ｜医学编码智能体工作流自动优化

研究机构：澳大利亚悉尼大学

作者：Jiyang Zheng、Islam Nassar、Thanh Vu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.13361)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.13361)

> 医学编码需将非结构化笔记映射为ICD代码，传统判别式模型受限于长尾分布，而现有智能体框架依赖人工设计固定流程，难以捕捉复杂规则间的协同效应。MedDCR将工作流设计形式化为迭代搜索问题，通过Designer-Coder-Reflector闭环与记忆档案自动发现最优工具组合。该方法在MDACE上取得0.51 Micro-F1，较次优基线提升6.2%，但绝对精度仍低于微调型判别式SOTA，其通用LLM骨干在缺乏领域微调时的性能上限存疑。

】

---

【Travel on the ICD Tree: Benchmarking Agentic Reasoning for ICD Coding from Chinese Electronic Medical Records ｜基于树搜索的中文ICD叶节点编码智能体框架

研究机构：复旦大学

作者：Xinjie Xu、Yongqi Fan、Shuang-shuang Chen 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3a7b05c497ee)

> 临床编码自动化长期受困于英文基准的粗粒度标注与中文细粒度场景的缺失，导致现有模型在复杂规则推理与叶节点定位上表现不佳。本文切入点在于构建首个中文全电子病历叶节点级基准Code4Detail，并设计ToT-ICD框架将编码重构为ICD树上的导航与回溯过程。该方法通过集成检索增强与规则验证，在复杂场景下优于传统检索重排范式。其价值在于揭示了LLM在层级推理中的能力边界，但缺乏与判别式基线的直接对比，且未量化树搜索相对于线性工作流的效率代价。

】
