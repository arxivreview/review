# Others2026 · 多模态情感识别方向论文汇编

> 本方向共 2 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Decoupled Hierarchical Distillation for Multimodal Emotion Recognition ｜解耦层级蒸馏多模态情感识别

研究机构：美国卡内基梅隆大学、东南大学

作者：Yong Li、Yuanzhi Wang、Yi Ding 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.04260)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.04260)

> 多模态情感识别（MER）旨在整合语言、视觉与听觉信号推断人类情感，但模态间的固有异质性导致直接融合时弱模态常被强模态抑制，且不同样本中各模态的贡献权重动态变化。现有解耦方法虽分离了共享与特定特征，却缺乏在解耦空间内建立跨模态语义对齐的有效机制，导致分布不匹配下的知识转移效率低下。本文提出解耦层级多模态蒸馏（DHMD），通过自回归解耦特征，并在共享与私有空间内分别实施粗粒度图蒸馏与细粒度字典匹配，实现自适应的跨模态知识对齐。该方法在CMU-MOSI和CMU-MOSEI上取得了优于现有解耦类方法的性能，但其依赖手工特征提取的设定限制了在大规模预训练范式下的泛化潜力。

】

---

【Relational graph-driven differential denoising and diffusion attention fusion for multimodal conversation emotion recognition ｜关系图驱动差分去噪与扩散注意力融合

研究机构：中南大学

作者：Ying Liu、Yuntao Shou、Wei Ai 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.25752)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.25752)

> 多模态对话情感识别（MCER）面临音视频模态噪声干扰与文本模态主导性被忽视的双重困境，导致融合阶段的信息失真与权重偏差。现有方法多依赖隐式注意力权重处理模态不平衡，缺乏针对噪声的显式抑制机制。本文通过差分Transformer抑制时间无关噪声，并构建文本主导的单向扩散注意力融合机制，在IEMOCAP上取得75.17%的加权准确率，但在MELD上显著落后于最新SOTA，其文本单向主导策略在复杂多说话者场景下的泛化能力存疑。

】
