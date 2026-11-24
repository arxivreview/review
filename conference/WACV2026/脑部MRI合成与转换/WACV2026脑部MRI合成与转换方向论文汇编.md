# WACV2026 · 脑部MRI合成与转换方向论文汇编

> 本方向共 3 篇（WACV2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Novel Metric for Detecting Memorization in Generative Models for Brain MRI Synthesis ｜脑MRI生成模型记忆化检测新指标

作者：Antonio Scardace、Lemuel Puglisi、Francesco Guarnera 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.16582)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.16582)

> 脑MRI生成模型在合成数据时可能复现训练集中的患者隐私信息，但现有通用去重方法无法捕捉医学影像中决定身份识别的细粒度解剖结构。本文提出DeepSSIM，一种自监督嵌入度量，通过强制嵌入空间的余弦相似度匹配图像空间的SSIM分数，实现无需配准的高效记忆化量化。该方法在空间错位场景下将F1分数从基线的31.39%提升至76.43%，但仅验证了2D切片数据，其向3D体积及实时训练监控的扩展性尚未证实。

】

---

【brat: Aligned Multi-View Embeddings for Brain MRI Analysis ｜脑MRI多视图对齐表征学习

研究机构：英国牛津大学

作者：Maxime Kayser、Maksim Gridnev、Wanting Wang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.18679)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.18679)

> 脑MRI临床报告包含大量分散于3D体积不同区域的细微病灶描述，传统单向量视觉-语言预训练无法捕捉这种空间与语义的多样性，导致下游任务泛化能力受限。本文提出brat框架，借鉴文档检索中的多向量思想，将报告句子作为查询子单元，通过贪心匹配与行列式点过程（DPP）约束，迫使图像特征分解为多个对齐特定临床特征的视图。该方法在80K规模的MSKBrain数据集上验证了检索与分割性能的提升，但其依赖文本报告作为隐式解剖先验，未显式处理拓扑一致性，且88%的异常率可能限制对正常脑结构的表征学习。

】

---

【ReBrain: Brain MRI Reconstruction from Sparse CT Slice via Retrieval-Augmented Diffusion ｜稀疏CT驱动的脑MRI重建

研究机构：同济大学

作者：Junming Liu、Yifei Sun、Weihua Cheng 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.17068)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.17068)

> 临床低剂量CT扫描常因辐射限制导致轴向切片稀疏，直接用于跨模态MRI合成会引发严重的体积连续性断裂。现有跨模态翻译方法假设源数据密集，而模态内插值方法无法处理CT到MRI的域差异，导致重建结果在层间出现解剖结构漂移。ReBrain通过引入基于检索增强的布朗桥扩散模型（BBDM），利用外部知识库中的相似切片作为结构控制信号，填补了稀疏输入下的信息空白。该框架在稀疏条件下实现了SOTA性能，但其对知识库覆盖率的依赖及2D切片处理的局限性，限制了其在极端病理或全新解剖结构场景下的泛化能力。

】
