# CVPR2026最新论文 ｜SR3R: Rethinking Super-Resolution 3D Reconstruction With Feed-Forward Gaussian Splatting ｜前馈式3D超分重建

研究机构：上海科技大学、澳大利亚格里菲斯大学

作者：Xiang Feng、Xiangbo Wang、Tieshi Zhong 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.24020)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.24020)

> 3D超分重建（3D Super-Resolution, 3DSR）旨在从低分辨率（LR）多视图观测中恢复高分辨率（HR）3D场景，以突破传感器分辨率与存储带宽的物理限制。现有主流方法依赖预训练2D超分模型生成伪HR图像作为监督信号，并执行逐场景优化，导致高频先验受限于2D模型且无法跨场景泛化。SR3R将3DSR重构为从稀疏LR视图直接映射至HR 3D高斯泼溅（3D Gaussian Splatting, 3DGS）表示的前馈问题，通过高斯偏移学习实现数据驱动的3D特定高频先验学习。该方法在零样本设定下超越了逐场景优化基线，但其性能高度依赖骨干网络提供的初始几何脚手架，且未验证在极端稀疏或动态场景下的鲁棒性。

## 研究背景

当3DGS重建管线接收低分辨率输入时，其可微光栅化过程无法恢复高频几何与纹理细节，导致重建结果模糊。这一缺陷源于3DGS对密集HR视图的强依赖，而实际采集受限于传感器分辨率与带宽，使得直接获取高质量观测不可行。为弥补这一信息缺失，研究者引入2D超分（2DSR）模型生成伪HR图像，将其作为光度监督信号注入3DGS优化过程。然而，2DSR模型仅在图像域操作，无法强制跨视图几何一致性，且其生成的伪HR标签质量构成了重建保真度的上限。

3DSR领域的核心矛盾在于如何在不依赖密集HR输入的前提下，获取3D特定的高频先验。主流路线采用“2DSR伪监督+逐场景优化”范式，如SRGS与FSGS，它们将每个场景视为独立问题，通过迭代优化拟合伪HR标签。这种范式存在三重瓶颈：逐场景优化计算成本高且缺乏跨场景泛化能力；高频知识来源局限于预训练2DSR模型的隐式先验，无法利用大规模多场景数据学习3D结构；密集多视图合成与迭代优化引入巨大的计算与数据开销。SR3R的切入点在于消除对2DSR伪监督的依赖，将3DSR重新定义为从稀疏LR视图到HR 3DGS的直接前馈映射，使网络能够从大规模多场景数据中自主学习3D高频几何与外观特征。

## 核心方法

### 前馈3DGS重建参照系

前馈3DGS重建的标准流程是通过神经网络直接从输入视图预测高斯参数，消除逐场景优化。SR3R沿用此范式，但关键差异在于输入为LR视图，目标为HR 3DGS表示。标准前馈模型直接回归绝对高斯参数，而SR3R引入“LR脚手架+HR偏移”的两阶段策略，将高频恢复任务解耦为结构预测与细节细化。

### 高斯脚手架构建与特征细化

设计动机在于解决LR输入下直接回归HR参数导致的优化不稳定与高频幻觉问题。SR3R首先利用任意前馈3DGS骨干（如NoPoSplat）从LR视图预测LR 3DGS $\mathcal{G}_{LR}$，随后通过高斯洗牌分裂（Gaussian Shuffle Split）操作将其稠密化为 $\mathcal{G}_{Dense}$。该操作将每个高斯 $g_j$ 沿其三个主轴的正负方向分裂为6个子高斯，子高斯中心偏移量为 $\beta \mathbf{s}_j$（$\beta=0.5$），尺度沿偏移轴缩小至1/4，从而在保持空间覆盖的同时提供更精细的结构脚手架。随后，LR图像经上采样后由ViT编码器提取特征，并通过双向交叉注意力与骨干网络的几何感知特征对齐，抑制上采样引入的幻觉纹理，生成跨视图一致的细化特征 $\mathbf{t}_{de}$。

$$
\mathbf{t}_{ca} = \text{FC}(\mathbf{U}_{o \leftarrow p} \oplus \mathbf{U}_{p \leftarrow o}), \quad \mathbf{U}_{o \leftarrow p} = \text{Attn}(\mathbf{W}_Q \mathbf{t}_{en}, \mathbf{W}_K \mathbf{t}_{pre}, \mathbf{W}_V \mathbf{t}_{pre})
$$

该公式表明，编码器特征 $\mathbf{t}_{en}$ 与预训练骨干特征 $\mathbf{t}_{pre}$ 通过双向注意力交互，将3D几何先验注入2D特征空间，确保特征与底层高斯结构对齐。

### 高斯偏移学习

设计动机在于直接回归HR高斯参数的预测空间过大且多模态，而 $\mathcal{G}_{Dense}$ 已提供可靠的结构基础，剩余差异主要为局部高频细节。SR3R引入高斯偏移学习模块，预测相对于 $\mathcal{G}_{Dense}$ 的残差偏移量，而非绝对参数。对于 $\mathcal{G}_{Dense}$ 中的每个高斯 $g_i$，将其中心 $\boldsymbol{\mu}_i$ 投影至图像平面，采样局部特征 $\mathbf{F}_i$，结合相机内参 $\mathbf{K}$ 输入PointTransformerV3（PTv3）进行多尺度空间推理，再通过轻量级MLP预测残差偏移 $(\Delta \boldsymbol{\mu}, \Delta \boldsymbol{\sigma}, \Delta \mathbf{r}, \Delta \mathbf{s}, \Delta \mathbf{c})$。

$$
\mathcal{G}_{HR} = \{ (\boldsymbol{\mu}_i + \Delta \boldsymbol{\mu}_i, \alpha_i + \Delta \alpha_i, \mathbf{r}_i \oplus \Delta \mathbf{r}_i, \mathbf{s}_i + \Delta \mathbf{s}_i, \mathbf{c}_i + \Delta \mathbf{c}_i) \}_{i=1}^{N}
$$

该残差组合公式将网络学习目标约束在局部几何与光度偏移上，显著提升了收敛稳定性与高频纹理保真度，避免了直接回归导致的几何畸变。

## 实验评估

SR3R在RealEstate10K（RE10K）、ACID与DTU三个基准上评估，对比前馈基线（NoPoSplat, DepthSplat）与逐场景优化基线（SRGS, FSGS）。在RE10K 4x超分任务（64x64至256x256）中，SR3R（NoPoSplat骨干）取得24.794 PSNR，显著优于NoPoSplat基线的21.326 PSNR与上采样变体Up-NoPoSplat的23.374 PSNR；在ACID数据集上，SR3R（DepthSplat骨干）取得27.018 PSNR，超越DepthSplat基线的23.801 PSNR。

| 数据集 | 方法 | PSNR (dB) | SSIM | LPIPS | 高斯数量 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| RE10K | NoPoSplat | 21.326 | 0.612 | 0.307 | 8,192 |
| RE10K | Up-NoPoSplat | 23.374 | 0.771 | 0.251 | 131,072 |
| RE10K | SR3R (NoPoSplat) | 24.794 | 0.827 | 0.188 | 49,152 |
| ACID | DepthSplat | 23.801 | 0.624 | 0.437 | 8,192 |
| ACID | Up-DepthSplat | 25.315 | 0.721 | 0.322 | 131,072 |
| ACID | SR3R (DepthSplat) | 27.018 | 0.797 | 0.261 | 49,152 |

消融实验显示，高斯偏移学习贡献最大增益，使PSNR从23.504提升至24.447，同时减少可学习高斯参数数量；PTv3进一步将PSNR提升至24.794。上采样策略对结果影响较小，Bilinear插值（24.586 PSNR）与SwinIR（24.794 PSNR）性能接近，表明SR3R不依赖特定2DSR模型。

评估边界方面，实验仅覆盖4x超分倍率，未验证8x或更高倍率下的几何稳定性；零样本泛化测试仅在DTU上进行，缺乏对动态场景或极端光照变化的鲁棒性评估。代码与超参数已公开，训练使用4块NVIDIA RTX 5090 GPU，75,000次迭代，batch size为8。

## 关联研究分析

从问题动机看，SR3R与SRGS等逐场景优化方法的核心差异在于高频先验的来源。SRGS依赖预训练2DSR模型生成的伪HR标签，其保真度受限于2D模型的图像域先验，且无法利用跨场景数据学习3D结构；SR3R则通过大规模多场景训练，直接从LR视图学习3D特定的高频映射，实现了从“2D伪监督”到“3D数据驱动”的范式转变。这一差异源于任务特性：3D重建需要跨视图几何一致性，而2DSR模型无法提供此约束，导致伪HR标签在3D优化中引入纹理漂移与几何歧义。

从方法设计看，SR3R与NoPoSplat等前馈3DGS重建模型共享ViT编码器-解码器架构，但SR3R引入了高斯偏移学习机制。NoPoSplat直接回归绝对高斯参数，适用于HR输入下的结构预测；SR3R则针对LR输入下的细节恢复，通过预测相对于稠密脚手架的残差，将高频恢复任务解耦。这一设计选择解决了LR输入下直接回归参数导致的优化不稳定问题，但依赖于骨干网络提供的初始几何质量。若骨干网络在LR输入下几何预测严重失真，偏移学习可能无法弥补结构错误，这一局限性在论文中未充分探讨。

## 总结

SR3R旨在解决低分辨率多视图输入下3D超分重建的高频细节缺失问题，其切入点在于消除对2DSR伪监督的依赖，通过前馈映射直接从稀疏LR视图学习3D特定高频先验。该方法通过高斯脚手架构建与偏移学习，在RE10K上取得24.794 PSNR，零样本设定下超越逐场景优化基线SRGS（12.420 PSNR）。然而，其性能高度依赖骨干网络提供的初始几何脚手架，且在极端稀疏或动态场景下的鲁棒性未经验证。当输入视图数量进一步减少至1-2张且分辨率极低时，高斯脚手架的结构可靠性是否足以支撑偏移学习的有效收敛，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.24020)