# ACL-Findings2026 · 噪声标签学习方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Learning on Imbalanced Noisy Data via Debiased Sample Selection and LLM-Driven Annotation ｜去偏样本选择与LLM协同标注的噪声长尾学习

研究机构：国防科技大学、浙江大学

作者：Bo Yuan、Yulin Chen、Yin Zhang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_64fce0d6bf8b)

> 噪声标签与类别不平衡在真实文本数据中常同时出现，传统基于全局固定损失阈值的样本选择方法会系统性忽略尾部类干净样本，导致选择偏差。本文指出该偏差源于头部与尾部类损失分布的动态演化差异，提出DeCo框架，通过多专家模型解耦训练与选择、动态类内阈值筛选样本，并引入LLM对噪声子集进行主动重标注。该方法在文本分类任务上显著优于现有基线，但其对LLM标注质量的依赖及跨模态泛化能力尚存疑。

】
