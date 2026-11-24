# ICLR2026 · 视觉Transformer架构创新方向论文汇编

> 本方向共 1 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【SONIC: Spectral Oriented Neural Invariant Convolutions ｜谱域方向不变卷积

研究机构：荷兰阿姆斯特丹大学

作者：Gijs Joppe Moens、Regina Beets-Tan、Eduardo H. P. Pooch

论文原文见 [arXiv](https://arxiv.org/abs/2601.19884)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.19884)

> 视觉模型在几何变换与分辨率变化下的鲁棒性不足，源于空间域卷积的局部性限制与自注意力机制的二次方复杂度及分辨率依赖。现有频域算子如 FNO 和 S4ND 虽具备全局感受野，但缺乏方向选择性或受限于轴对齐结构，无法有效捕捉自然图像中的各向异性纹理。SONIC 通过引入方向选择性连续谱算子，在频域构建低秩、分辨率不变的滤波器，以极少的参数实现全局上下文建模。该方法在医学影像分割与合成基准上展现了优异的鲁棒性，但其通用分类精度与主流 ViT 架构相比仍有差距，且缺乏大规模预训练验证。

】
