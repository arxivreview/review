# AAAI2026 · 三维点云Transformer与鲁棒学习方向论文汇编

> 本方向共 1 篇（AAAI2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Point-SRA: Self-Representation Alignment for 3D Representation Learning ｜掩码比率互补性与概率流对齐的3D自监督表示学习

作者：Lintong Wei、Jian Lu、Haozhe Cheng 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.01746)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.01746)

> 3D点云自监督学习长期受限于固定掩码策略导致的特征单一性与确定性重建对几何多解性的失效。Point-SRA通过理论分析揭示高低掩码比率在几何细节与语义抽象间的互补性，并引入MeanFlow Transformer (MFT) 以概率轨迹建模替代点式重建。该方法构建了双层级自表示对齐机制，在ScanObjectNN分类上超越Point-MAE 5.51%，但在S3DIS分割任务上仍落后于当前SOTA 6.3%。其核心价值在于将掩码策略从经验调参升级为信息论驱动的结构设计，但多模态条件依赖与纯几何泛化能力之间的张力尚未完全消解。

】
