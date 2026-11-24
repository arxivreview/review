# Others2026 · 开放词汇语义分割方向论文汇编

> 本方向共 1 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【MagicSeg: Open-World Segmentation Pretraining via Counterfactural Diffusion-Based Auto-Generation ｜MagicSeg：基于反事实扩散生成的开放世界分割预训练

研究机构：中山大学

作者：Kaixin Cai、Pengzhen Ren、Jianhua Han 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.19575)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.19575)

> 开放世界语义分割（Open-World Semantic Segmentation, OWSS）旨在让模型识别训练集未见的任意类别，但现有方法受限于缺乏大规模像素级标注数据，导致泛化能力不足。传统合成数据方法依赖扩散模型注意力图生成掩码，噪声大且仅覆盖封闭类别集，无法支撑开放世界场景。MagicSeg 提出一种反事实扩散生成流水线，利用大语言模型（Large Language Model, LLM）生成丰富文本描述，结合 Grounding DINO 与 SAM 提取高精度掩码，并引入反事实图像对进行对比训练。该方法在 PASCAL VOC 上达到 62.9% mIoU，超越了 GroupViT 等基线，但其性能仍低于当前免训练 SOTA，且合成数据分布偏差对长尾类别泛化的影响尚不明确。

】
