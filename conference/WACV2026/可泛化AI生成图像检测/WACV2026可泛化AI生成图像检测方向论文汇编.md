# WACV2026 · 可泛化AI生成图像检测方向论文汇编

> 本方向共 1 篇（WACV2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【General and Domain-Specific Zero-shot Detection of Generated Images via Conditional Likelihood ｜条件似然零样本生成图像检测

研究机构：以色列理工学院

作者：Roy Betser、Omer Hofman、Roman Vainshtein 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.05590)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.05590)

> 生成模型迭代速度远超检测器更新周期，导致依赖特定伪迹或训练数据的检测器在未见生成器上失效。现有零样本方法虽免训练，但在窄域场景（如发票、受损车辆）中性能骤降甚至出现分类翻转。本文提出CLIDE，通过基于真实图像的条件似然估计，在无生成数据、无任务训练的前提下实现域自适应检测。该方法在通用与域特定任务上均优于现有零样本基线，但其有效性高度依赖CLIP嵌入的统计特性，对高保真生成模型的区分能力存疑。

】
