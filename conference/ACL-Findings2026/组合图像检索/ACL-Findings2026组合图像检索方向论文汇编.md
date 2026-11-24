# ACL-Findings2026 · 组合图像检索方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Beyond Query Bias: Candidate-Aware Iterative Refinement for Zero-Shot Composed Image Retrieval ｜基于检索反馈的零样本组合图像检索自修正框架

研究机构：华中科技大学、阿里巴巴集团

作者：Nan Sun、Jing Tang、Lei Sun 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b942bea1a63e)

> 零样本组合图像检索（Zero-Shot Composed Image Retrieval, ZS-CIR）旨在通过参考图像与修改文本检索目标图像，但现有方法在生成查询时因无法感知候选分布而陷入“认知偏差”，导致语义合理的查询与真实目标错位。本文提出 CoRR 框架，将检索过程重构为“检索-反思-修正”的迭代闭环，利用多模态大语言模型（Multimodal Large Language Model, MLLM）分析检索反馈以修正查询偏差。该方法通过历史查询融合与检索驱动字幕优化稳定迭代过程，在 CIRCO 基准上取得领先性能，但其对 MLLM 推理能力的依赖及在细粒度属性修改任务上的表现仍存疑。

】

---

【CSMCIR: CoT-Enhanced Symmetric Alignment with Memory Bank for Composed Image Retrieval ｜对称架构下的组合图像检索：CSMCIR

研究机构：快手、厦门大学

作者：Zhipeng Qian、Zihan Liang、Yufei Ma 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.03728)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03728)

> 导读 组合图像检索（Composed Image Retrieval, CIR）旨在通过参考图像与修改文本的联合输入，精准定位目标图像，其核心痛点在于查询侧（图+文）与目标侧（仅图）的模态异构性导致表示空间碎片化。现有方法多采用非对称编码器处理两侧输入，依赖事后对齐弥合空间差异，但T-SNE可视化证实这种碎片化在训练后依然显著存在，限制了检索性能。本文提出CSMCIR，通过多模态大模型离线生成目标图像描述实现模态对称，结合共享参数双塔架构与熵感知记忆库，在四个基准上取得SOTA性能。该框架在训练效率与检索精度间取得平衡，但其对称设计是否牺牲了对查询侧细粒度修改意图的捕捉能力，尚需进一步验证。

】
