# ACL-Findings2026 · 基于视觉语言模型的多模态文档理解方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Picture is Worth a Thousand Words? An Empirical Study of Aggregation Strategies for Visual Financial Document Retrieval ｜视觉金融文档检索中单向量聚合的失效诊断

研究机构：香港科技大学

作者：Ho Hung Lim、Yi Yang

论文原文见 [arXiv](https://arxiv.org/abs/2605.14581)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.14581)

> 视觉检索系统面临存储与精度的权衡：多向量保留细节但开销大，单向量聚合便于部署却可能丢失关键信息。现有方法在通用文档上表现尚可，但在数值密集的金融表格中，单向量聚合是否导致语义盲区尚缺乏系统性证据。本文构建诊断基准，通过敏感性分析与注意力归因，量化了聚合过程对细粒度数值信号的抹除效应。该研究揭示了单向量范式在金融场景的根本局限，但仅停留在诊断层面，未提供可部署的修复方案。

】

---

【Hybrid-Vector Retrieval for Visually Rich Documents: Combining Single-Vector Efficiency and Multi-Vector Accuracy ｜混合向量检索：兼顾单向量效率与多向量精度

研究机构：韩国科学技术院、韩国汉阳大学

作者：Juyeon Kim、Geon Lee、Dongwon Choi 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.22215)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.22215)

> 视觉文档检索（VDR）旨在从包含图表、表格等复杂视觉元素的文档库中定位相关页面，以支撑检索增强生成（RAG）的事实可靠性。现有单向量检索虽高效但精度不足，多向量检索虽精准但计算开销巨大，二者在效率与精度间存在刚性权衡。本文提出HEAVEN，通过两阶段混合架构，在索引期构建视觉摘要页（VS-Page）进行粗筛，在查询期过滤关键Token进行精排，以极低的计算成本逼近多向量模型的检索精度。该框架在四个基准上保留了99.87%的Recall@1性能，同时降低99.82%的FLOPs，但其依赖显式标题布局构建VS-Page的假设，在缺乏结构化标题的文档场景下的鲁棒性存疑。

】

---

【ShredBench: Evaluating the Semantic Reasoning Capabilities of Multimodal LLMs in Document Reconstruction ｜碎片化文档语义重建基准

研究机构：西安电子科技大学、上海交通大学

作者：Zichun Guo、Yuling Shi、Wenhao Zeng 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.23813)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.23813)

> 多模态大语言模型（MLLM）在完整文档解析上已接近人类水平，但面对物理撕裂、遮挡等结构断裂场景时，其依赖视觉边缘匹配的能力失效，亟需评估其跨碎片语义推理能力。现有基准多聚焦于光照噪声或长上下文检索，缺乏对离散结构破坏下语义连贯性的系统测试。本文通过物理仿真切割生成无序碎片图像，构建了首个针对碎片化内容恢复的评测基准。该基准揭示了当前MLLM在视觉位置嵌入与语义连续性对齐上的根本缺陷，但仅作为诊断工具，未提供解决该问题的算法方案。

】
