# CVPR2026最新论文 ｜PhyGaP: Physically-Grounded Gaussians with Polarization Cues ｜物理引导高斯泼溅与偏振线索

研究机构：浙江大学

作者：Jiale Wu、Xiaoyang Bai、Zongqi He 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.14001)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.14001)

> 反射表面重建的核心矛盾在于几何形状与材质属性在RGB观测中的强耦合，导致现有3D高斯泼溅（3D Gaussian Splatting, 3DGS）方法在重光照时出现颜色偏移与阴影失真。传统延迟渲染依赖球谐函数近似间接光，无法解耦反照率与反射光，而偏振信息虽能提供物理线索，但此前缺乏将其高效融入高斯表示并支持非凸物体间接光照的完整管线。PhyGaP通过构建偏振延迟渲染（PolarDR）流程与自遮挡感知环境图（GridMap），实现了物理一致的反光分解与重光照。该方法在合成与真实数据集上均优于现有偏振高斯方法，但其对偏振相机硬件的依赖及非朗伯表面的泛化能力仍存疑。

## 研究背景

当相机面对高反光物体时，镜面反射分量与漫反射分量在像素级叠加，导致传统光度立体或神经辐射场（Neural Radiance Fields, NeRF）难以区分物体固有颜色（反照率）与环境光照贡献。这种耦合使得重建模型在更换光照条件时产生不真实的阴影或色彩断层。偏振成像通过斯托克斯矢量（Stokes Vector）中的线偏振度（Degree of Linear Polarization, DoLP）和偏振角（Angle of Polarization, AoP）提供了独立于光强的几何与材质线索，理论上可解耦漫反射与镜面反射。然而，将偏振物理模型嵌入高效渲染框架并处理非凸物体的自遮挡间接光照，仍是当前反射表面重建的未解难题。

现有3DGS变体如Ref-Gaussian虽引入延迟渲染，但依赖球谐函数表示间接光，无法支持重光照；PANDORA等NeRF方法虽利用偏振解耦反射，但计算成本高且实时性差。PhyGaP的切入点在于将偏振物理先验直接融入2D高斯泼溅（2DGS）的延迟渲染流程，摒弃球谐颜色表示，显式建模反照率、粗糙度与折射率，从而在保持高斯表示效率的同时实现物理一致的重建。

## 核心方法

### 2DGS与延迟渲染参照系

PhyGaP基于Ref-Gaussian框架，使用2DGS表示几何，每个高斯原语由均值位置、切向向量及缩放因子定义，法线由切向向量叉积计算。标准延迟渲染通过α混合将物理属性（反照率、金属度、粗糙度）渲染为材质图，再评估渲染方程计算辐射。本文的关键差异在于摒弃球谐函数颜色表示，改用偏振物理模型直接计算斯托克斯矢量，以解决RGB图像中反射状态不可观测的问题。

### PolarDR：偏振延迟渲染

PolarDR将渲染方程扩展为偏振形式，利用偏振BRDF（pBRDF）模型计算出射光的偏振状态。设计动机在于解决RGB图像无法区分漫反射与镜面反射导致的反照率估计错误。具体而言，假设入射光为非偏振光，镜面反射与漫反射分别通过Fresnel系数与偏振角计算：

$$
\mathbf{S}_{\omega_o}^{s} = \mathbf{L}_s(\omega_o) \cdot \mathbf{M}_s(\theta_n, \phi_n, \eta)
$$

$$
\mathbf{S}_{\omega_o}^{d} = \mathbf{L}_d(\omega_o) \cdot \mathbf{M}_d(\theta_n, \phi_n)
$$

其中 $\mathbf{M}_s$ 和 $\mathbf{M}_d$ 为镜面与漫反射的Mueller矩阵，$\eta$ 为折射率。该公式将物理属性（法线、粗糙度、折射率）映射为偏振信号，使优化过程直接受偏振线索约束，从而精确解耦反射分量。

### GridMap：自遮挡感知环境图

GridMap解决非凸物体自遮挡导致的间接光照不一致问题。设计动机在于Ref-Gaussian的球谐间接光表示无法区分全局照明与互反射，导致重光照时阴影失真。具体做法是将物体包围盒的每个面划分为 $3 \times 3$ 网格，在除底面外的52个网格点放置锚点相机。对每个锚点相机，通过单步光线追踪构建局部立方体贴图 $\tilde{E}_i$，混合物体颜色与全局环境图。渲染时，像素 $(x, y)$ 的局部漫反射斯托克斯矢量通过距离加权计算：

$$
\mathbf{S}_{\tilde{d}} = \sum_{i=1}^{N} w_i \mathbf{S}_{\tilde{d}}^{(i)}
$$

其中 $w_i$ 为表面点 $\mathbf{p}$ 到锚点 $\mathbf{c}_i$ 的距离权重。该机制无需学习场景特定参数，即可捕捉非凸几何的复杂阴影，提升重光照鲁棒性。

## 实验评估

实验在PANDORA、RMVP3D、SMVP3D及Mitsuba3渲染的9个场景上进行，基线包括RGB-only方法（3DGS-DR、Ref-Gaussian）及偏振方法（PolGS、PANDORA）。PhyGaP在SMVP3D上取得0.0261的余弦距离（CD），优于PolGS的0.0297；在RMVP3D上CD为0.0482，优于PolGS的0.0658。新视角合成（NVS）方面，PhyGaP在SMVP3D上PSNR达32.92 dB，显著高于PolGS的28.25 dB。

| 数据集 | 方法 | CD (↓) | PSNR (↑) |
|---|---|---|---|
| SMVP3D | PhyGaP | 0.0261 | 32.92 |
| SMVP3D | PolGS | 0.0297 | 28.25 |
| RMVP3D | PhyGaP | 0.0482 | 32.92 |
| RMVP3D | PolGS | 0.0658 | 28.25 |

消融实验显示，移除PolarDR导致环境图PSNR从12.39降至10.69，移除GridMap导致重光照PSNR从19.18降至17.81，证明两者对反射分解与间接光照建模的必要性。评估边界方面，论文未报告置信区间，且PANDORA与NeRSP的训练数据包含测试视角，其结果可比性受限。代码尚未发布，超参数细节需参考补充材料。

## 关联研究分析

从问题动机看，PhyGaP与PolGS同属偏振高斯泼溅路线，但PolGS未显式建模反照率，仅将偏振作为损失函数输入，导致无法支持重光照。PhyGaP通过PolarDR显式解耦反射分量，解决了PolGS在环境图估计上的失效。这一差异源于任务目标的不同：PolGS聚焦几何重建，而PhyGaP强调物理一致性与重光照能力。

从方法设计看，PhyGaP与PANDORA共享pBRDF物理模型，但PANDORA基于NeRF，计算成本高且实时性差。PhyGaP将物理模型迁移至2DGS框架，通过GridMap替代球谐间接光表示，解决了非凸物体自遮挡问题。这一设计选择是否导致在极端非朗伯表面上的泛化能力下降，论文未给出回答。

## 总结

PhyGaP旨在解决反射表面几何-材质耦合导致的重光照失真问题，其切入点在于将偏振物理先验融入2DGS延迟渲染，通过PolarDR解耦反射分量，通过GridMap处理非凸间接光照。实验证明其在SMVP3D上CD达0.0261，PSNR达32.92 dB，优于现有偏振高斯方法。然而，该方法依赖偏振相机硬件，且对复杂非朗伯表面的泛化能力未充分验证。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.14001)