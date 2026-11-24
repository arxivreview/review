# WACV2026 · 高斯溅射SLAM方向论文汇编

> 本方向共 2 篇（WACV2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Gaussian Splatting Map Registration with Orthographic Bird's-Eye-View Renderings ｜基于正交鸟瞰图渲染的高斯泼溅地图配准

研究机构：法国国家科学研究中心

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c9f9562c8a7e)

> 3D高斯泼溅（3DGS）SLAM系统缺乏全局一致性保障，核心瓶颈在于现有配准方法强依赖原始训练位姿与图像，导致地图对齐在元数据缺失或跨重建管线场景下失效。本文切入点在于剥离对原始传感器数据的依赖，仅利用优化后的高斯模型本身进行配准。通过沿重力方向生成正交鸟瞰图（BEV）渲染，将6自由度（6-DoF）配准问题降维至4自由度（4-DoF），结合特征匹配与深度对齐实现鲁棒对齐。该方法在室内与室外场景中显著优于依赖位姿的基线，但在跨高斯变体配准及极端光照下的泛化能力仍存疑。

】

---

【Gaussian Splatting Map Registration with Orthographic Bird’s-Eye-View Renderings ｜基于正交鸟瞰图渲染的高斯泼溅地图配准

研究机构：法国国家科学研究中心

作者：H. Leblond、G. Simon、R. Martins 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_WACV_2026_69572353)

> 独立构建的三维高斯泼溅（3DGS）地图间缺乏全局一致性，传统配准方法依赖原始相机位姿或点云数据，无法处理元数据缺失场景。现有基于高斯中心的配准算法泛化性差，且未系统评估跨重建算法的鲁棒性。本文提出一种仅依赖优化后高斯模型的正交鸟瞰图（BEV）渲染配准方法，将6自由度（DoF）问题降维至4 DoF。该方法在室内外数据集上显著优于基线，但在极端光照与非刚性形变场景下的适用性仍存疑。

】
