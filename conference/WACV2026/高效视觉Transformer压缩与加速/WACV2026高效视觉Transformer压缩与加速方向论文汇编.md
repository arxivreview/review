# WACV2026 · 高效视觉Transformer压缩与加速方向论文汇编

> 本方向共 1 篇（WACV2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Efficient Vision Transformers via Token Merging with Head-wise Attention Correction ｜基于头特异性注意力修正的Token合并方法

研究机构：日本东京科学大学

作者：Yuki Ichikawa、Masato Motomura、Thiem Van Chu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_35ca7cbb7b11)

> 视觉Transformer（ViT）在高分辨率输入下因自注意力机制的二次方复杂度导致计算量激增，Token合并（ToMe）通过减少序列长度缓解此问题，但标准比例注意力机制未能完全消除合并引发的注意力分布失真。本文指出比例注意力仅补偿合并Token对其他Token的影响，忽略了合并Token自身自注意力分数变化导致的系统性偏差，且该偏差随注意力头投影权重特性显著变化。通过双线性形式分析揭示失真与头特异性统计量的关联，提出头特异性注意力修正（Head-wise Attention Correction, HAC）方法，动态调整注意力分数以恢复原始平衡。该方法在理论上填补了ToMe精度保持的机制空白，但缺乏与主流压缩方法的定量对比，实际部署收益尚待验证。

】
