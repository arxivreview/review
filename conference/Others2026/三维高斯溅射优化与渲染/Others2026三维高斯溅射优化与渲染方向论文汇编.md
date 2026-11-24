# Others2026 · 三维高斯溅射优化与渲染方向论文汇编

> 本方向共 2 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Long-LRM++: Preserving Fine Details in Feed-Forward Wide-Coverage Reconstruction ｜半显式特征高斯前馈重建

研究机构：Adobe研究院、美国俄勒冈州立大学

作者：Chen Ziwen、Hao Tan、Peng Wang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.10267)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.10267)

> 前馈式新视角合成旨在摆脱逐场景优化，实现即时重建，但现有显式高斯方法因需预测海量颜色基元导致高频细节模糊，而隐式方法虽质量高却牺牲了实时渲染速度。Long-LRM++ 指出颜色光栅化的误差敏感性是核心瓶颈，提出以自由分布的特征高斯替代像素对齐颜色高斯，并通过轻量级解码器与多空间分区机制恢复细节。该方法在保持 14 FPS 实时渲染的同时，将重建质量提升至接近隐式方法水平，但其在复杂几何结构下的泛化边界尚待进一步验证。

】

---

【野外场景可重光照3D高斯泼溅

作者：Margherita Lea Corona、Wieland Morgenstern、Peter Eisert 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.02801)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.02801)

> 3D高斯泼溅（3D Gaussian Splatting, 3DGS）在静态室内场景中已实现实时渲染，但无法处理户外无约束照片集带来的动态光照与天空反射解耦难题。现有重光照方法要么假设光照恒定，要么仅建模漫反射且将天空与前景混同表示，导致重光照失真与深度伪影。R3GW通过分离前景与天空高斯集合，并在前景中集成Cook-Torrance BRDF与每图像球谐函数（Spherical Harmonics, SH）光照，实现了户外场景的任意环境光重光照。该方法在效率上显著优于神经辐射场（NeRF）基线，但在绝对重建质量上仍略逊于部分NeRF方法，且未显式建模阴影。

】
