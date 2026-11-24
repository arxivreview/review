# WACV2026 · 视觉Transformer架构创新方向论文汇编

> 本方向共 1 篇（WACV2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AdaptViG: Adaptive Vision GNN with Exponential Decay Gating ｜自适应视觉图神经网络

研究机构：美国德克萨斯大学奥斯汀分校

作者：Mustafa Munir、Md Mostafijur Rahman、Radu Marculescu

论文原文见 [arXiv](https://arxiv.org/abs/2511.09942)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.09942)

> 视觉图神经网络（Vision Graph Neural Networks, ViGs）试图通过图结构建模图像块间的非刚性空间关系，以突破卷积神经网络（CNN）的固定网格限制与视觉Transformer（ViT）的序列处理局限。然而，ViGs的核心瓶颈在于图构建阶段：动态KNN搜索具有二次方复杂度，而静态图虽高效却丧失了对图像内容的自适应能力。本文提出AdaptViG，通过“静态轴向骨架+指数衰减门控”的混合策略，在保持线性计算复杂度的同时实现内容感知的稀疏图构建。该架构在参数效率上建立了新的帕累托前沿，但其绝对精度仍低于同等规模下最新的混合ViT架构，且缺乏对密集预测任务中图结构优势的独立验证。

】
