# CVPR2026最新论文 ｜AnchorSplat: Feed-Forward 3D Gaussian Splatting with 3D Geometric Priors ｜锚点对齐前馈高斯重建

研究机构：华为

作者：Xiaoxue Zhang、Xiaoxu Zheng、Yixuan Yin 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.07053)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07053)

> 前馈式3D高斯泼溅（3D Gaussian Splatting, 3DGS）重建面临像素对齐导致的几何冗余与视图偏差问题，现有体素对齐方法虽缓解冗余但仍未解耦高斯数量与输入分辨率。本文提出锚点对齐框架，利用多视图立体（Multi-View Stereo, MVS）先验生成稀疏3D锚点，将高斯生成从2D像素网格转移至3D空间，实现高斯数量固定化。该方法在ScanNet++上以约1/20的高斯数量实现了优于AnySplat的重建质量，但其性能高度依赖上游MVS模块的几何精度，在极端稀疏视图下的鲁棒性尚存疑。

## 研究背景

前馈式3D重建旨在通过单次网络推理从多视图图像直接预测3D场景表示，以替代耗时的逐场景优化。传统像素对齐方法将每个2D像素映射为一个高斯基元，导致高斯总数随输入视图数与分辨率线性增长（$N = H \times W \times V$），且在遮挡与弱纹理区域产生浮点伪影。为打破这种2D网格绑定，体素对齐方法（如AnySplat）引入可微体素化进行剪枝，但其初始高斯仍源自像素对齐，未能从根本上消除视图偏差与冗余。

该领域当前瓶颈在于如何在保持几何一致性的同时，将高斯表示从输入图像解耦。PixelSplat等早期工作确立了像素对齐范式，但其在稀疏视图下几何退化严重；VolSplat转向体素空间以增强稳定性，却引入了量化误差与计算开销。AnchorSplat的切入点在于引入3D几何先验作为“锚点”，不再从像素出发，而是从稀疏的3D空间点出发预测高斯，从而在架构层面切断高斯数量与输入视图数的耦合关系。

## 核心方法

### 方法参照系

前馈3DGS的标准流程为：图像特征提取 → 跨视图特征融合 → 像素对齐高斯预测。本文的关键差异在于将“像素对齐高斯预测”替换为“锚点对齐高斯预测”，即先由MVS模块生成稀疏3D锚点，再基于锚点特征预测高斯，使高斯分布独立于输入分辨率。

### 锚点预测与特征投影

设计动机：解决像素对齐导致的高斯密度随视图偏差变化及3D空间交互弱的问题。AnchorSplat首先利用预训练MVS模型（如MapAnything）从$V$张无位姿图像预测深度$D_i$与位姿$(K_i, R_i, T_i)$。随后，通过反投影将像素对齐的3D点下采样为稀疏锚点集合$\{A_j\}_{j=1}^N$，其中$N \ll H \times W \times V$。下采样采用最远点采样（Farthest Point Sampling, FPS），其数量由3D空间体素化决定：

$$ A_j = \text{FPS}\left( \bigcup_{i=1}^V \text{BackProj}(D_i, K_i, R_i, T_i) \right) $$

该公式将密集像素点压缩为稀疏3D锚点，保留了场景几何骨架，消除了重复观测带来的冗余。接着，利用轻量级2D U-Net提取图像、深度及相机射线嵌入的特征$F_i$，并将其投影至锚点位置，得到锚点特征$\tilde{A}_j$。

### 高斯解码与迭代细化

设计动机：解决固定锚点数量下局部细节缺失及渲染模糊问题。高斯解码器（Gaussian Decoder）接收锚点特征，通过Transformer建模3D空间交互，预测每个锚点对应的4个高斯属性。高斯中心$\mu_j$由锚点位置$A_j$加上预测偏移$\delta \mu_j$得到：

$$ \mu_j = A_j + \delta \mu_j, \quad \text{where } \|\delta \mu_j\| < \epsilon $$

该约束确保高斯在锚点附近局部生长，维持几何一致性。随后，高斯细化器（Gaussian Refiner）介入，它不重新预测高斯，而是基于渲染误差$e_i = F_i - \hat{F}_i$（其中$F_i$与$\hat{F}_i$为真值与渲染图像的多尺度特征）对现有高斯属性进行修正。通过可微反投影将2D误差映射至3D高斯，再利用Point Transformer更新属性：

$$ G_j^{refined} = \text{PointTrans}(G_j, \tilde{F}_j, E_j) $$

这一机制允许模型在固定高斯预算下，通过误差驱动的方式填补空洞并锐化边界，弥补了稀疏锚点带来的细节损失。

## 实验评估

实验在ScanNet++ V2数据集上进行，输入32/48/64视图，渲染分辨率448×672。基线包括优化式方法（3DGS, Mip-Splatting）及前馈体素对齐方法AnySplat。值得注意的是，论文未对比YoNoSplat、VolSplat等最新前馈SOTA方法，这可能高估了其在当前前馈架构中的相对优势。

| 模型 | 类别 | PSNR (dB) | SSIM | LPIPS | NumGS | ReconTime (s) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 3DGS | Opt. | 19.98 | 0.72 | 0.30 | 496,087 | 391.44 |
| AnySplat | Feed-fwd | 20.20 | 0.73 | 0.32 | 5,550,940 | 6.83 |
| AnchorSplat | Feed-fwd | 21.48 | 0.79 | 0.38 | 247,153 | 5.52 |

在32视图/4新视图设定下，AnchorSplat以21.48 PSNR领先AnySplat（20.20 dB），且高斯数量仅为AnySplat的约1/20（247,153 vs 5,550,940），重建时间缩短至5.52秒。消融实验显示，移除Gaussian Refiner（AnchorSplat⋆）后，PSNR从21.48降至20.96，LPIPS从0.38升至0.47，表明细化模块对填补稀疏锚点导致的细节缺失至关重要。在极端稀疏（3视图）下，AnchorSplat⋆的PSNR（19.99）仍高于AnySplat（19.51），但优势缩小，暗示其对MVS先验的依赖在观测不足时可能成为瓶颈。

评估指标涵盖PSNR、SSIM、LPIPS及深度误差（AbsRel, $\delta_1$），但缺乏对几何网格提取质量（如Chamfer Distance）的直接评估，限制了对其表面重建精度的判断。论文声明将开源代码与模型，但训练依赖64块Ascend 910B3 NPU，复现门槛较高。

## 关联研究分析

从方法设计看，AnchorSplat与VolSplat均试图摆脱像素对齐，但VolSplat通过体素化实现均匀分布，而AnchorSplat依赖MVS生成的稀疏锚点。VolSplat的体素化是数据驱动的均匀采样，而AnchorSplat的锚点采样是几何驱动的稀疏采样。这一差异导致AnchorSplat在高斯数量上更具优势，但若MVS预测的深度存在系统性偏差，锚点分布将偏离真实几何，而VolSplat的体素网格虽冗余但分布更均匀，对深度误差的容忍度可能更高。

从问题动机看，AnchorSplat与ReSplat均关注前馈推理的质量上限，但ReSplat通过迭代细化突破单步推理瓶颈，而AnchorSplat通过引入渲染误差反馈实现类似效果。ReSplat的迭代是时间维度的多次前馈，AnchorSplat的细化是空间维度的误差驱动修正。AnchorSplat的细化模块仅使用1个注意力块和4个串行注意力块，参数量（31M）远小于解码器（84M），这种轻量化设计是否足以处理复杂场景中的多尺度误差，论文未提供不同复杂度场景下的细化效果对比。

## 总结

AnchorSplat旨在解决前馈3DGS中像素对齐导致的高斯冗余与几何不一致矛盾。其切入点在于利用MVS先验生成稀疏3D锚点，将高斯生成从2D像素网格解耦至3D空间，并通过误差驱动的细化模块弥补稀疏表示的细节损失。实验证明，该方法在ScanNet++上以247,153个高斯实现了21.48 PSNR，较AnySplat在保持更高PSNR的同时将高斯数量减少约20倍。然而，其性能边界受限于上游MVS模块的精度：当输入视图极少（3视图）时，MVS预测的深度噪声增大，锚点分布失真，导致重建质量优势收窄。当MVS先验在弱纹理或动态场景中失效时，锚点对齐框架是否仍能维持几何一致性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07053)