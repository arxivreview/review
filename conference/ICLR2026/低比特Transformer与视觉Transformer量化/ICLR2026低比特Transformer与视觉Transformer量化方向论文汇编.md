# ICLR2026 · 低比特Transformer与视觉Transformer量化方向论文汇编

> 本方向共 2 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Quantized Visual Geometry Grounded Transformer ｜视觉几何基础Transformer量化

研究机构：中国科学院、中国科学院大学

作者：Weilun Feng、Haotong Qin、Mingqiang Wu 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.21302)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.21302)

> 3D重建模型VGGT因数据无关的特殊Token引发重尾激活分布，导致通用量化方法在低比特下精度崩塌。现有平滑或旋转策略无法同时处理全局离群值与通道内方差，且多视图数据校准样本代表性不足。本文提出双平滑细粒度量化与噪声过滤多样采样，通过先旋转后平滑及帧感知聚类解决上述问题。该方法在W4A4下保持98%精度，但仅验证了PTQ路径，未探索QAT上限。

】

---

【STaMP: Sequence Transformation and Mixed Precision for Low-Precision Activation Quantization ｜序列变换与混合精度量化

作者：Marco Federici、Riccardo Del Chiaro、Boris van Breugel 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.26771)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.26771)

> 低比特Transformer量化长期受困于激活值异常值对量化步长的支配，导致W4A4精度崩塌。现有特征维度变换（如Hadamard旋转）忽略了序列维度中相邻Token的强局部相关性，无法实现能量的高效集中。STaMP通过引入序列维度的离散小波变换（DWT）将激活能量压缩至前64个Token，并采用8/4-bit双精度分配策略，在无需重训练的前提下显著提升了LLM与LVM的量化保真度。该方法验证了序列维度治理的必要性，但其离散能量层级对比特分配细粒度的限制尚待进一步探索。

】
