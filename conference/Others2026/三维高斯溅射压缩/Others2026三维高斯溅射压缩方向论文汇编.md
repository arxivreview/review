# Others2026 · 三维高斯溅射压缩方向论文汇编

> 本方向共 1 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A 129FPS Full HD Real-Time Accelerator for 3D Gaussian Splatting ｜面向边缘设备的3D高斯溅射硬件加速器与协同压缩

研究机构：国立阳明交通大学

作者：Fang-Chi Chang、Tian-Sheuan Chang

论文原文见 [arXiv](https://arxiv.org/abs/2604.10223)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10223)

> 3D高斯溅射（3D Gaussian Splatting, 3DGS）在AR/VR设备上的部署受限于GB级存储与高功耗，现有软件压缩方法无法直接映射至低功耗硬件，而既有硬件加速器因实现原始算法导致面积与能耗超标。本文切入点在于将压缩策略与硬件流水线进行协同设计，通过固定压缩比消除数据变异性，并优化渲染数据流。具体做法是改造LightGaussian管线实现51.6倍压缩，并设计混合粒度帧级流水线加速器。该工作验证了亚瓦特功耗下全高清实时渲染的可行性，但其压缩质量显著低于当前算法SOTA，且缺乏硅片实测数据。

】
