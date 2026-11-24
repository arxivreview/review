# ACL-Findings2026 · 视觉语言模型中的视觉推理方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Can MLLMs Reason Beyond Language? VisReason: A Comprehensive Benchmark for Vision-Centric Reasoning ｜视觉中心推理基准

研究机构：中国科学院、中国科学院大学

作者：Longteng Guo、Yifan Wang、Pengkang Huo 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.25364)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.25364)

> 多模态大语言模型在现有视觉推理基准上的高分表现，掩盖了其依赖语言中介而非直接视觉证据推理的事实。现有基准允许模型通过文本描述抽象视觉信息，导致评估失效。本文通过构建强制依赖直接视觉输入的VisReason基准，量化了语言捷径对评估的干扰。该基准揭示了当前模型在视觉接地上的根本缺陷，但其诊断能力受限于未覆盖潜在推理等新兴方法。

】

---

【S2H-DPO: Hardness-Aware Preference Optimization for Vision-Language Models ｜难度感知偏好优化

研究机构：美国密歇根州立大学、美国卡内基梅隆大学

作者：Nitish Shukla、Surgan Jandial、Arun Ross

论文原文见 [arXiv](https://arxiv.org/abs/2604.18512)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18512)

> 视觉语言模型（Vision-Language Models, VLMs）在处理多图输入时，常因预设索引问题而回避自主视觉搜索，导致跨图证据整合能力缺失。现有偏好对齐方法仅针对单图局部推理，无法覆盖全局搜索等高阶认知任务。本文通过构建从单图定位到全局搜索的三级难度层级合成数据，利用直接偏好优化（Direct Preference Optimization, DPO）强化模型的多图推理能力。该方法在多图基准上取得显著增益，但其对单图性能的保持机制及层级数据比例的敏感性仍存疑。

】
