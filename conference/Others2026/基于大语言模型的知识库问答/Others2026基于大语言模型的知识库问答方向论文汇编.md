# Others2026 · 基于大语言模型的知识库问答方向论文汇编

> 本方向共 1 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【S-Path-RAG: Semantic-Aware Shortest-Path Retrieval Augmented Generation for Multi-Hop Knowledge Graph Question Answering ｜语义感知最短路径检索增强生成

研究机构：澳门大学、厦门大学

作者：Rong Fu、Yemin Wang、Tianxiang Xu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.23512)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.23512)

> 多跳知识图谱问答（KGQA）的核心矛盾在于大语言模型（LLM）的语义泛化能力与知识图谱（KG）的事实精确性难以在单次检索中同时满足。现有图检索增强生成（GraphRAG）方法多采用一次性文本化路径注入，导致上下文冗余且无法在模型不确定时迭代修正证据。S-Path-RAG 通过语义加权路径枚举、可微分潜变量交叉注意力注入及迭代图编辑循环，实现了拓扑感知与语义对齐的协同。该框架在 WebQSP 上达到了 88.9 的 Hits@1，但在复杂组合推理基准 CWQ 上落后于最新智能体方法，其迭代机制在长程推理中的有效性仍存疑。

】
