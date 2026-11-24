# WACV2026 · 三维点云Transformer与鲁棒学习方向论文汇编

> 本方向共 1 篇（WACV2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【GFT: Graph Feature Tuning for Efficient Point Cloud Analysis ｜图特征调优

作者：Manish Dhakal、Venkat R. Dasari、Rajshekhar Sunderraman 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.10799)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.10799)

> 参数高效微调（PEFT）旨在以极小参数代价适配预训练模型，但通用PEFT在无序点云上表现次优，而点云专用PEFT如IDPT存在参数冗余且对预算缩减敏感的问题。本文切入点在于将图特征学习从模型末端移至输入端，并通过稀疏交叉注意力注入深层。GFT通过轻量级EdgeConv提取局部拓扑特征，仅更新0.73M参数即可在ScanObjectNN上取得92.56%的OA，实现了精度与参数效率的平衡。其价值在于证明了前端图特征提取的有效性，但真实场景下的泛化能力仍受限于合成预训练数据分布。

】
