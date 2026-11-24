# WACV2026最新论文 ｜Spec-Gloss Surfels and Normal-Diffuse Priors for Relightable Glossy Objects ｜基于2D高斯面元与Spec-Gloss参数化的可重光照高反射物体重建

研究机构：比利时鲁汶大学

作者：Georgios Kouros、Minye Wu、Tinne Tuytelaars

论文原文见 [arXiv](https://arxiv.org/abs/2510.02069)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.02069)

> 高反射物体逆渲染的核心困境在于几何、材质与光照的非线性耦合导致病态歧义，现有3D高斯泼溅方法因缺乏显式法线且材质参数化耦合，难以实现物理一致的重光照。本文切入点在于识别出主流Metallic-Roughness参数化在逆渲染中的可辨识性缺陷，转而采用Spec-Gloss参数化并嵌入2D高斯面元表示，辅以扩散先验抑制早期优化歧义。该方法通过解耦漫反射与镜面反射属性，显著提升了光泽表面的重光照保真度。其价值在于提供了比现有高斯方法更物理准确的材质分解，但依赖逐场景优化且未解决动态场景下的时序一致性。

## 研究背景

高反射物体重建面临的核心挑战是镜面高光的高频视角依赖性，这导致多视图立体（Multi-View Stereo, MVS）失效。为恢复表面属性，逆渲染需解耦几何、材质与光照，但图像形成过程的非线性耦合使得多种材质-光照组合产生相同观测，构成病态反演问题。物理基于渲染（Physically Based Rendering, PBR）模型通过双向反射分布函数（Bidirectional Reflectance Distribution Function, BRDF）约束这一过程，其中材质参数化的选择直接决定解耦的可辨识性。

主流神经渲染路线在表示与物理建模上存在权衡。辐射场与3D高斯泼溅（3D Gaussian Splatting, 3DGS）虽实现实时渲染，但隐式或椭球原语缺乏显式表面法线，导致几何噪声大且难以精确建模高频反射；有符号距离函数（Signed Distance Function, SDF）方法几何精度高但计算成本阻碍实时应用。在材质建模上，Disney BRDF采用的Metallic-Roughness参数化将镜面反射率与基础色耦合，在逆渲染中加剧了漫反射与镜面分量的歧义，限制了重光照质量。本文针对高反射场景，通过引入显式法线的2D高斯面元与解耦的Spec-Gloss参数化，结合扩散先验，旨在突破现有高斯方法在材质解耦与重光照保真度上的瓶颈。

## 核心方法

### 2D高斯面元与延迟着色参照系

本文基于2D高斯泼溅（2D Gaussian Splatting, 2DGS）构建场景表示，将3D高斯坍缩为视图一致的平面圆盘，其显式法线 $\mathbf{n} = \mathbf{t}_u \times \mathbf{t}_v$ 由切向向量叉积定义。该表示通过像素级延迟着色（Deferred Shading）将几何渲染与材质着色解耦，先光栅化生成包含反照率、粗糙度与法线的G-buffer，再在屏幕空间应用物理BRDF。这一流程解决了3DGS中法线缺失导致的高光模糊与几何不稳定问题，为高频反射建模提供了稳定的几何基础。

### Spec-Gloss参数化与微表面BRDF

设计动机在于解决Metallic-Roughness参数化中漫反射与镜面反射的耦合歧义。本文采用Spec-Gloss参数化，将材质显式分解为漫反射反照率 $\rho_d$、法线入射镜面反射率 $F_0$ 与粗糙度 $r$。出射辐射度通过Split-Sum近似计算：

$$ L_o(\mathbf{v}, \mathbf{n}) = \rho_d L_d(\mathbf{n}) + (F_0 \beta_1 + \beta_2) \odot L_s(\mathbf{v}, \mathbf{n}, r) $$

其中 $L_d$ 为低频漫反射项，$L_s$ 为镜面项，$\beta_1, \beta_2$ 为预计算的BRDF查找表系数。该公式将镜面反射率 $F_0$ 作为自由RGB参数，彻底解耦了漫反射颜色与镜面强度，避免了Metallic参数对基础色的隐式依赖，从而在逆渲染中提升了材质属性的可辨识性，使重光照时能更准确地分离漫反射与镜面贡献。

### 扩散先验与粗到细光照优化

为抑制逆渲染的病态歧义，本文引入StableNormal与StableDelight作为软约束。法线先验 $\tilde{N}$ 作为伪真值约束G-buffer法线，漫反射先验 $I_{dp}$ 在训练初期（$T_{dp}=15k$ 前）引导颜色分解。同时，环境图采用粗到细（Coarse-to-Fine）策略，从分辨率64逐步上采样至512，并应用负值裁剪（Negative-only Clipping, NOC）保留HDR峰值。

$$ \mathcal{L}_{total} = \mathcal{L}_{RGB} + \lambda_n \mathcal{L}_n + \lambda_{np} \mathcal{L}_{np} + \lambda_{dp} \mathcal{L}_{dp} + \lambda_{light} \mathcal{L}_{light} $$

该复合损失函数中，先验项 $\mathcal{L}_{np}, \mathcal{L}_{dp}$ 仅在早期优化阶段生效，防止光照吸收材质误差。NOC通过 $E \leftarrow \max(0, E_{raw})$ 保留高光细节，避免了传统[0,1]裁剪导致的曝光不足与材质-光照解耦失效，确保了重光照时的物理一致性。

## 实验评估

实验在Glossy Synthetic与Shiny Synthetic数据集上进行，基线覆盖GShader、3DGS-DR、RefGauss等高斯渲染方法，但缺乏SDF类高精度几何基线的直接对比。重光照评估使用训练未见过的HDR环境图，本文方法在Glossy Synthetic上取得24.76 PSNR，显著优于RefGauss的20.82 PSNR与3DGS-DR的20.22 PSNR，表明Spec-Gloss参数化在材质解耦上的优势。

| 方法 | Relighting PSNR (avg) | Relighting SSIM (avg) | Relighting LPIPS (avg) |
|---|---|---|---|
| GShader [9] | 17.31 | 0.856 | 0.121 |
| 3DGS-DR [12] | 20.22 | 0.884 | 0.098 |
| RefGauss [33] | 20.82 | 0.893 | 0.090 |
| Ours (SG) | 24.76 | 0.932 | 0.068 |

消融实验显示，粗到细上采样（PU）将训练时间从112分钟降至61分钟，且未降低新视角合成质量。先验（Priors）与NOC的组合对重光照提升最大，单独使用先验对重光照影响有限，因为光照裁剪限制了高光表现。这表明重光照质量的提升主要源于Spec-Gloss参数化与NOC保留的HDR峰值，而非单纯的环境图分辨率增加。

评估边界方面，本文仅报告了平均指标，未提供置信区间或逐场景方差分析。代码已开源，训练在NVIDIA RTX 4090上进行，合成场景50k迭代，真实场景20k迭代。然而，实验未涵盖动态场景或极端稀疏视图，且真实场景数据量有限，泛化性验证不足。

## 关联研究分析

从材质参数化选择看，本文与RefGauss（采用Metallic-Roughness-Specular, MRS）形成鲜明对比。RefGauss通过引入Specular Tint解耦基础色与镜面反射，但增加了自由度导致逆问题更欠定，且MRS在工业管线中兼容性有限。本文选择Spec-Gloss，其简单性与可编辑性更适合逆渲染，但牺牲了Metallic参数的直观性。这一差异根源在于任务特性：逆渲染需要高可辨识性，而前向渲染更关注参数直观性。Spec-Gloss在工业管线中的长期兼容性是否足以支撑其作为标准接口，论文未给出回答。

从先验利用策略看，本文与MatSpray等扩散生成方法不同。MatSpray将扩散模型作为直接生成器预测材质图，而本文仅将StableNormal与StableDelight作为早期软约束，随后禁用先验以依赖RGB真值优化。这种“先验引导+物理优化”的策略在物理一致性上更稳，但可能损失扩散模型在复杂纹理细节上的生成能力。本文未对比直接生成材质图再融合3D几何的方案，因此无法判断在极端复杂纹理下，生成式先验是否比软约束先验更具优势。

## 总结

本文针对高反射物体逆渲染中材质-光照歧义问题，指出主流Metallic-Roughness参数化在逆渲染中的可辨识性缺陷，提出基于2D高斯面元与Spec-Gloss参数化的解耦框架。通过引入扩散先验抑制早期歧义及粗到细HDR光照优化，该方法在Glossy Synthetic上实现24.76 PSNR的重光照质量，显著超越RefGauss的20.82 PSNR。其边界在于依赖逐场景优化，训练时间仍达61分钟，且未解决动态场景下的时序一致性问题。当场景包含快速运动物体时，Spec-Gloss参数化在时间维度上的稳定性与2D高斯面元的形变能力是否匹配，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.02069)