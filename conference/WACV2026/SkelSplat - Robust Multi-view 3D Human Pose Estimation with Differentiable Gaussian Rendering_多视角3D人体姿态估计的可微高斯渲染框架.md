# WACV2026最新论文 ｜SkelSplat: Robust Multi-view 3D Human Pose Estimation with Differentiable Gaussian Rendering ｜多视角3D人体姿态估计的可微高斯渲染框架

研究机构：荷兰阿姆斯特丹大学、美国卡内基梅隆大学

作者：Laura Bragagnolo、Leonardo Barcellona、Stefano Ghidoni

论文原文见 [arXiv](https://arxiv.org/abs/2511.08294)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.08294)

> 多视角3D人体姿态估计旨在利用多个同步相机的2D检测恢复人体关节的三维坐标，其核心价值在于通过几何约束消除单目成像的深度歧义。现有学习式融合方法依赖大规模标注数据训练，导致模型与特定相机配置、姿态分布及遮挡模式强耦合，跨场景泛化能力不足。SkelSplat将多视角融合重构为可微高斯渲染优化问题，通过One-hot关节编码与跨视角梯度累积实现免训练泛化。该方法在遮挡场景下展现出显著鲁棒性，但其迭代优化机制带来的推理延迟限制了实时应用潜力。

## 研究背景

多视角3D人体姿态估计的核心困境在于如何将多个视角的2D投影映射为一致的3D骨架。这一过程涉及两个关键概念：2D-to-3D提升与可微渲染。2D-to-3D提升范式将任务解耦为2D关键点检测与3D坐标恢复，前者提供视觉感知，后者负责几何推理。然而，传统提升方法多采用学习式融合网络，其权重在特定数据集上训练，当测试场景的相机布局或遮挡程度发生变化时，模型性能急剧下降。可微渲染技术（如Gaussian Splatting）允许通过反向传播优化3D表示以匹配2D观测，这为摆脱对预训练融合网络的依赖提供了可能。

多视角姿态估计的主流路线分为学习式融合与几何优化两类。学习式方法（如TransFusion, AdaFuse）通过注意力机制或自适应权重融合多视角特征，虽在受控数据集上精度较高，但泛化能力受限，需针对新场景重新训练。几何优化方法（如代数三角化、RANSAC）依赖显式几何约束，无需训练，但在严重遮挡或噪声2D检测下鲁棒性不足。SkelSplat的切入点在于将多视角融合视为一个可微优化问题，利用Gaussian Splatting的渲染机制直接优化3D关节位置，无需3D真值监督，从而在保持几何一致性的同时实现跨场景泛化。

## 核心方法

### 方法参照系

SkelSplat属于多视角几何融合路线，但偏离了标准的学习式融合流程。标准流程通常使用预训练网络融合多视角2D特征以回归3D坐标，而SkelSplat将3D姿态表示为各向异性高斯骨架，通过最小化渲染损失进行迭代优化。关键差异在于：本文不学习融合权重，而是通过可微渲染直接优化3D高斯参数，使方法对相机配置和遮挡模式具有内在灵活性。

### 高斯骨架表示与One-hot编码

传统Gaussian Splatting使用RGB颜色场表示场景外观，无法区分不同关节。SkelSplat将每个关节 $sk_j$ 表示为一个各向异性3D高斯 $gs_j = (\mu_j, \Sigma_j)$，其中 $\mu_j \in \mathbb{R}^3$ 为关节位置，$\Sigma_j \in \mathbb{R}^{3 \times 3}$ 为协方差矩阵。为解决多关节重叠时的监督混淆问题，本文引入One-hot编码：将原始RGB颜色场替换为 $N$ 通道身份向量，仅激活第 $j$ 个通道。渲染函数被修改为输出 $N$ 通道张量，每个通道对应单个关节高斯的投影。这一设计使得即使2D检测在图像平面重叠，每个关节高斯仍能独立接收监督信号，解决了传统RGB渲染在密集关节区域无法区分身份的问题。

### 伪真值生成与跨视角优化

监督信号来源于2D检测生成的伪真值热图。为确保多视角几何一致性，2D热图的协方差 $\Sigma_{ij}^{2D}$ 通过投影3D协方差 $\Sigma_j$ 计算：

$$ \Sigma_{ij}^{2D} = J_i W_i \Sigma_j W_i^\top J_i^\top $$

其中 $W_i$ 为相机外参，$J_i$ 为透视投影雅可比矩阵。优化目标为最小化渲染热图与伪真值热图之间的掩码 $L_2$ 损失，并加入3D结构对称损失以正则化对称肢体长度：

$$ \mathcal{L}_{total} = \sum_{i=1}^M \sum_{j=1}^N \mathcal{L}_{mask}(I_{ij}^{render}, I_{ij}^{pseudo}) + \lambda_{sym} \mathcal{L}_{sym} $$

跨视角梯度累积策略将多个视角的梯度合并后再更新参数，提升了优化稳定性。这一设计解决了单视角梯度更新在遮挡场景下易受局部噪声干扰的问题，通过全局一致性约束提高了鲁棒性。

## 实验评估

SkelSplat在Human3.6M、CMU Panoptic、Human3.6M-Occ及Occlusion-Person四个基准上进行评估。基线覆盖学习式融合（AdaFuse, TransFusion, Iskakov et al.）与几何方法（RANSAC, Algebraic Triangulation），但未包含单目SOTA方法（如SasMamba），因任务设定不同。在Human3.6M上，SkelSplat（ResNet-152 2D）取得20.3mm的绝对MPJPE，显著优于Iskakov et al.的34.0mm和Generalizable Triangulation的31.0mm。在CMU Panoptic上，SkelSplat（MeTRAbs）取得20.9mm，优于Voxelpose的25.5mm。

| 数据集 | 方法 | 2D检测器 | 绝对MPJPE (mm) |
| :--- | :--- | :--- | :--- |
| Human3.6M | SkelSplat | ResNet-152 | 20.3 |
| Human3.6M | Iskakov et al. - Vol | - | 34.0 |
| Human3.6M | Generalizable Triang. | - | 31.0 |
| CMU Panoptic | SkelSplat | MeTRAbs | 20.9 |
| CMU Panoptic | Voxelpose | - | 25.5 |

消融实验表明，One-hot编码相比RGB或单通道编码降低MPJPE达10.1%（MeTRAbs）和7.9%（ResNet-152）。跨视角梯度累积中，4视角累积比单视角提升2.7mm。初始化策略对最终精度影响较小，但高斯噪声鲁棒性在40mm标准差内保持稳定，超过80mm后性能急剧下降。对称损失中，仅约束下臂和下腿（Symm-1）在Human3.6M-Occ-2上带来+6.1%的增益，且计算成本最低。

评估边界方面，论文未报告推理延迟的具体数值，仅提及约3秒/姿态（4视角），限制了实时性评估。代码未明确开源，但提供项目页面。超参数如 $\lambda_{sym}=1e-5$ 和迭代次数125已披露，但GPU配置未说明。

## 关联研究分析

从问题动机看，SkelSplat与AdaFuse均针对遮挡鲁棒性，但AdaFuse依赖学习式自适应权重，其泛化能力受限于训练数据分布。SkelSplat通过可微优化摆脱了对特定分布的依赖，证明了优化式方法在跨场景泛化上的优势。这一差异根源在于任务特性：遮挡模式在野外场景中高度多变，学习式权重难以覆盖所有情况，而几何优化能动态适应观测噪声。

从方法设计看，SkelSplat与Gaussian Splatting同框架但不同问题。Gaussian Splatting用于密集场景重建，监督信号为RGB图像；SkelSplat用于稀疏骨架估计，监督信号为2D关键点热图。这一改造引入了One-hot编码和结构对称损失，解决了关节身份混淆和解剖学合理性问题。与单目方法（如SasMamba）相比，SkelSplat利用多视角几何约束消除深度歧义，但放弃了时序建模，适用于静态或短序列场景。

## 总结

SkelSplat要解决的核心矛盾是多视角融合方法在跨场景部署时的泛化失效。现有学习式方法因权重与特定相机配置耦合而难以适应新环境，SkelSplat通过可微高斯渲染优化，将融合过程转化为无监督的几何优化问题，从而摆脱对3D真值和特定分布的依赖。该方法在Human3.6M上取得20.3mm的MPJPE，在Human3.6M-Occ上展现SOTA鲁棒性。其边界在于迭代优化带来的推理延迟（约3秒/姿态）以及对2D检测器精度的依赖。当2D检测噪声超过80mm标准差时，性能急剧下降，这提示了优化式方法在极端噪声下的局限性。若2D检测器在野外场景中精度进一步降低，SkelSplat的鲁棒性是否仍能保持，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.08294)