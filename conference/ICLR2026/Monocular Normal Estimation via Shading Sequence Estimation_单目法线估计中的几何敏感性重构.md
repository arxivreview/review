# ICLR2026最新论文 ｜Monocular Normal Estimation via Shading Sequence Estimation ｜单目法线估计中的几何敏感性重构

研究机构：新加坡南洋理工大学、浙江大学

作者：Zongrui Li、Xinhua Ma、Minghui Hu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.09929)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.09929)

> 单目法线估计旨在从单张RGB图像恢复物体表面法线，但现有方法常陷入“3D misalignment”困境：预测的法线图视觉外观正确，却与真实3D几何细节错位。根源在于法线表示中几何变化仅体现为细微色彩差异，模型难以区分。RoSE将任务重构为Shading Sequence（光照序列）估计，利用视频扩散模型生成对几何更敏感的光照序列，再通过OLS求解法线。该方法在LUCES和DiLiGenT基准上取得SOTA性能，但其依赖合成数据训练，对真实复杂场景的泛化边界尚待验证。

## 研究背景

法线估计的核心困境在于表示形式的几何敏感性不足。法线图以RGB色彩编码表面朝向，几何结构的细微变化（如边缘、曲面曲率）在色彩空间中仅表现为微小的像素值差异。这种紧凑表示导致深度神经网络在训练时难以有效区分几何细节，尤其在单目输入缺乏深度线索时，模型倾向于生成平滑但几何错误的法线，即“3D misalignment”。为突破此瓶颈，需引入对几何变化更敏感的监督信号，同时保持与法线估计任务的等价性。

单目法线估计的主流路线分为直接回归与多光照生成两类。直接回归方法（如StableNormal, Lotus-G）直接从RGB图像预测法线，受限于法线表示的低敏感性，细节恢复能力弱。多光照生成方法（如Neural LightRig）先生成多光照下的RGB图像再估法线，但RGB生成过程中的材质与光照伪影会累积，加剧3D misalignment。RoSE的切入点在于改变生成目标：不生成RGB图像，而是生成Shading Sequence（法线与规范光照方向的点积序列）。该表示通过亮度变化直接编码几何信息，排除材质干扰，且可通过OLS无损还原法线，从表示层面解决了几何敏感性不足的问题。

## 核心方法

### 方法参照系

单目法线估计的标准流程是从单张RGB图像直接回归法线图，或生成多光照RGB图像后求解法线。本文的关键差异在于将生成目标从RGB图像替换为Shading Sequence，利用视频扩散模型的时间一致性建模光照变化，并通过解析求解替代端到端回归。

### Shading Sequence表示与等价性

Shading Sequence定义为法线图与一组规范平行光方向的截断点积：

$$
\mathbf{S} \triangleq \{ \mathbf{s}_p = \max(\mathbf{n}_p \cdot \mathbf{l}, 0) \mid p \in P \}
$$

其中 $\mathbf{n}_p$ 为像素 $p$ 的法线，$\mathbf{l}$ 为光照方向，$\max(\cdot, 0)$ 截断负值以排除背光区域。该表示通过亮度变化敏感地编码几何结构，且当光照矩阵 $\mathbf{L}$ 满秩时，可通过OLS无损还原法线：

$$
\hat{\mathbf{N}} = \arg\min_{\mathbf{N}} \sum_{i=1}^f \|\mathbf{S}_i - \max(\mathbf{N} \cdot \mathbf{l}_i, 0)\|^2
$$

设计动机在于解决法线表示中几何变化仅体现为细微色彩差异的问题，Shading Sequence通过亮度变化直接放大几何敏感性，使模型更易区分细节。

### 视频扩散模型生成与条件注入

RoSE采用视频扩散U-Net生成Shading Sequence，输入为灰度图像 $\mathbf{I}_g$，通过双分支条件注入引导生成：

$$
\mathbf{z}_t = \alpha_t \epsilon + \sigma_t \mathbf{z}_0, \quad \mathbf{z}_0 = E(\mathbf{S}^{[s]})
$$

其中 $E$ 为VAE编码器，$\mathbf{z}_t$ 为噪声潜变量。CLIP嵌入提供全局语义引导，VAE潜变量拼接保留局部空间细节。灰度输入消除色彩干扰，使模型聚焦几何线索。设计动机在于利用视频模型的时间一致性建模光照序列的结构化变化，同时通过条件注入确保生成序列与输入图像的几何结构对齐，避免RGB生成中的伪影累积。

## 实验评估

实验在LUCES、DiLiGenT和Objaverse基准上进行，对比GeoWizard、DSINE、StableNormal、Lotus-G/D、Neural LightRig、NiRNE等7种方法。基线覆盖直接回归与多光照生成两类路线，但缺失早期CNN基线（如Eigen & Fergus），符合当前SOTA对比惯例。

| 方法 | LUCES MAE (°) | DiLiGenT MAE (°) |
|---|---|---|
| GeoWizard | 22.49 | 21.79 |
| Lotus-G | 17.44 | 21.41 |
| NiRNE | 17.88 | 29.10 |
| RoSE | 14.48 | 16.36 |

RoSE在LUCES上MAE为14.48°，较Lotus-G（17.44°）降低2.96°；在DiLiGenT上MAE为16.36°，较GeoWizard（21.79°）降低5.43°，显著优于所有基线。

消融实验验证了关键设计决策：移除Shading Sequence截断（w/o clamp）导致LUCES MAE从14.48°升至15.88°，证明截断操作对几何敏感性的贡献；移除材料增强（w/o MA）使MAE升至16.19°，表明材料多样性对鲁棒性至关重要。使用SVD XL骨干（Ours w/ SVD XL）的MAE为14.58°，与主模型（14.48°）接近，说明框架对骨干网络的泛化性良好。

评估指标以MAE为主，辅以SNE（边界区域法线误差）和PSNR/SSIM/LPIPS。SNE显示RoSE（26.74°）与NiRNE（26.78°）持平，表明细节恢复并非主要增益来源，整体几何对齐才是核心优势。代码与超参数已开源，训练使用8×H100 GPU，学习率1e-5，可复现性良好。

## 关联研究分析

从问题动机看，RoSE与Neural LightRig同属多光照生成路线，但RoSE将生成目标从RGB图像改为Shading Sequence。Neural LightRig的RGB生成受材质与光照伪影影响，伪影在后续法线估计中累积，加剧3D misalignment；RoSE的Shading Sequence直接编码几何，排除材质干扰，从源头避免伪影累积。这一差异源于任务特性：法线估计对几何敏感性的要求高于对材质真实性的要求，Shading Sequence的亮度变化比RGB色彩更直接地反映几何结构。

从方法设计看，RoSE与StableNormal同属生成式框架，但StableNormal直接生成法线图，而RoSE生成Shading Sequence后通过OLS求解。StableNormal受限于法线表示的低敏感性，细节恢复能力弱；RoSE通过Shading Sequence的几何敏感性提升，使模型更易区分细节。这一差异源于表示形式的选择：法线表示中几何变化仅体现为细微色彩差异，而Shading Sequence通过亮度变化放大几何敏感性，使视频扩散模型的时间一致性建模更有效地捕捉几何结构。

## 总结

RoSE解决的核心矛盾是法线表示中几何敏感性不足导致的3D misalignment。其切入点在于将生成目标从RGB图像或法线图替换为Shading Sequence，利用亮度变化直接编码几何信息，并通过OLS无损还原法线。RoSE采用视频扩散模型生成Shading Sequence，通过双分支条件注入确保几何对齐，在LUCES上MAE为14.48°，较Lotus-G降低2.96°。其边界在于依赖MultiShade合成数据训练，对真实复杂场景（如非朗伯表面、动态光照）的泛化能力未充分验证。当输入图像包含复杂材质反射或动态光照变化时，Shading Sequence的几何敏感性是否仍能有效约束法线估计，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.09929)