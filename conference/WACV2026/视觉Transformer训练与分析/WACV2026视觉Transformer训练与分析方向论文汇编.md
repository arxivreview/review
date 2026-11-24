# WACV2026 · 视觉Transformer训练与分析方向论文汇编

> 本方向共 2 篇（WACV2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Correction ｜头级注意力修正

研究机构：日本东京科学大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_WACV_2026_80175974)

> 视觉Transformer（ViT）通过Token Merging (ToMe)降低序列长度以缓解二次方计算复杂度，但现有比例注意力机制仅补偿合并Token对其他Token的影响，忽略了合并Token自身自注意力分数变化引发的全局注意力重分布。本文通过双线性形式分析揭示该失真与Query-Key投影权重迹的强相关性，提出头级注意力修正（Head-wise Attention Correction, HAC）以动态补偿这一被忽略的偏差。实验表明HAC在保持ToMe效率优势的同时显著提升了精度-效率权衡，但其修正效果依赖于特定骨干的校准数据，跨架构泛化能力尚存疑。

】

---

【GrowTAS: Progressive Expansion from Small to Large Subnets for Efficient ViT Architecture Search ｜渐进式扩展搜索

研究机构：韩国延世大学

作者：Hyunju Lee、Youngmin Oh、Jeimin Jeon 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.12296)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.12296)

> Transformer架构搜索（Transformer Architecture Search, TAS）旨在自动化发现高效视觉Transformer（ViT）架构，以替代耗时的人工试错。现有One-shot TAS方法通过训练包含所有候选子网的超网来加速搜索，但子网间共享权重导致训练干扰，严重损害小子网性能。本文发现训练良好的小子网可作为大子网的有效基础，据此提出渐进式训练框架GrowTAS，从小子网逐步扩展至大子网，并引入GrowTAS+微调新增权重以平衡大小子网性能。该方法在ImageNet上实现了SOTA搜索性能，但其对非嵌套搜索空间的适用性及大子网提升幅度有限，限制了其通用性。

】
