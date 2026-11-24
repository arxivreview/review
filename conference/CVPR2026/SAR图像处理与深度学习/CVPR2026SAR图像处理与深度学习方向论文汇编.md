# CVPR2026 · SAR图像处理与深度学习方向论文汇编

> 本方向共 1 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【SARMAE: Masked Autoencoder for SAR Representation Learning ｜SARMAE：面向合成孔径雷达表征学习的掩码自编码器

研究机构：北京理工大学、武汉大学

作者：Danxu Liu、Di Wang、Hebaixu Wang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.16635)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.16635)

> 导读 SAR 图像表征学习长期受困于标注数据稀缺与固有斑点噪声对语义提取的干扰，现有预训练方法直接迁移光学图像策略，忽略了雷达成像的物理特性。本文切入点在于构建首个百万级 SAR 数据集 SAR-1M，并设计物理感知的预训练目标。具体做法是改造掩码自编码器（MAE）的重建任务，注入斑点噪声并引入光学语义对齐约束。该框架在分类、检测与分割任务上刷新了多项基准记录，但其性能高度依赖地理配对的 SAR-光学数据，在无配对数据场景下的泛化能力存疑。

】
