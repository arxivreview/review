# ACL-Findings2026 · CLIP分析与增强方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【microCLIP: Unsupervised CLIP Adaptation via Coarse-Fine Token Fusion for Fine-Grained Image Classification ｜microCLIP：无监督CLIP适应中的粗-细粒度Token融合

研究机构：阿联酋扎耶德大学、印度理工学院德里分校

作者：Sathira Silva、Eman Ali、Chetan Arora 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.02270)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.02270)

> 无监督适应（Unsupervised Adaptation, UA）旨在利用未标注数据提升CLIP在细粒度分类上的表现，但现有方法依赖全局[CLS] token，无法捕捉区分近邻类别所需的局部空间细节。本文指出，仅靠文本侧的细粒度描述无法弥补视觉侧的空间缺失，必须从图像patch token中提取局部线索。microCLIP通过显著性导向注意力池化（Saliency-Oriented Attention Pooling, SOAP）构建细粒度[FG] token，并与[CLS] token对称融合，结合动态知识聚合实现自训练。该方法在13个细粒度数据集上平均提升2.90%，验证了视觉局部线索的必要性，但其性能上限受限于ViT-B/32骨干的patch分辨率。

】
