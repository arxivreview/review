# ACL-Findings2026 · 视觉标记剪枝与压缩：面向高效视觉-语言模型方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CAPA: Contribution-Aware Pruning and FFN Approximation for Efficient Large Vision-Language Models ｜贡献感知剪枝与FFN近似

研究机构：印度理工学院、美国伊利诺伊大学厄巴纳-香槟分校

作者：Samyak Jha、Junho Kim

论文原文见 [arXiv](https://arxiv.org/abs/2602.00247)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.00247)

> 视觉语言模型（VLMs）推理瓶颈源于高分辨率输入导致的视觉Token激增，现有剪枝方法依赖注意力分数却忽略Value向量幅度，导致误删关键语义信息。CAPA通过引入“注意力贡献度”指标替代原始注意力分数进行Token选择，并针对视觉Token在中间层FFN中表现出的线性冗余，采用Hadamard积近似替代密集FFN计算。该双策略框架在保持任务性能的同时实现了78%的FLOPs减少，但其FFN近似依赖特定骨干的线性冗余特性，跨模型泛化能力存疑。

】

---

【CrisPrune: Combining Contextual Relevance and Intrinsic Saliency for Efficient Visual Token Pruning in MLLMs ｜CrisPrune：融合内在显著性与双源文本相关性的视觉Token剪枝

作者：Ziniu Liu、Shuheng Zhou、Mingqing Liu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c3fde539d866)

> 视觉语言模型处理高分辨率图像时，视觉Token数量激增导致二次方注意力计算成本成为部署瓶颈。现有剪枝方法面临两难：纯视觉方法受注意力汇聚现象干扰且忽略任务语义，纯文本引导方法则因过度聚焦指令而丢失背景上下文。CrisPrune通过鲁棒归一化修复视觉显著性计算，并引入通用语义先验与指令对齐的双源文本相关性，结合行列式点过程（Determinantal Point Process, DPP）实现质量与多样性的平衡选择。该方法在极端压缩率下显著优于现有Training-free方法，但其对特定架构的依赖性及视频场景的适用性仍存疑。

】
