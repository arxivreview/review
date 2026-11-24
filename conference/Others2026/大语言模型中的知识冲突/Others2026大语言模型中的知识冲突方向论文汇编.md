# Others2026 · 大语言模型中的知识冲突方向论文汇编

> 本方向共 1 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【大连理工团队新研究：基于置信度信号的重排序

研究机构：大连理工大学

作者：Zhipeng Song、Xiangyu Kong、Xinrui Bao 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.13571)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.13571)

> 检索增强生成（RAG）系统常因检索文档排序不佳导致大语言模型（LLM）生成幻觉，现有重排序方法依赖专用训练或高算力，且未充分利用LLM的语义置信度信号。本文提出免训练、即插即用的LLM-Confidence Reranker（LCR），通过最大语义簇比例（MSCP）量化文档置信度并分箱排序。该方法在BEIR和TREC基准上实现NDCG@5最高20.6%的提升，但仅优化输入排序，未解决模型内部对参数化知识的依赖问题。

】
