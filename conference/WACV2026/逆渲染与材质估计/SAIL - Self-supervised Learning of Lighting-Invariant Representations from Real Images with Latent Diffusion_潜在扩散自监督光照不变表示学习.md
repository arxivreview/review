# WACV2026最新论文 ｜SAIL: Self-supervised Learning of Lighting-Invariant Representations from Real Images with Latent Diffusion ｜潜在扩散自监督光照不变表示学习

研究机构：法国巴黎萨克雷大学

作者：Hala Djeghim、Céline Loscos、Désiré Sidibé

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7bddac92d9fe)

> 图像内在分解旨在从单张真实图像中分离出与光照无关的反照率（Albedo）与依赖光照的阴影（Shading）分量，以支持重光照与场景编辑。现有监督方法受限于合成数据域差距，自监督方法则难以在复杂光照下保持反照率一致性。SAIL 将预训练潜在扩散模型（Latent Diffusion Model, LDM）重用于无监督场景重光照作为代理目标，在潜在空间显式分解光照不变与依赖分量，并引入正则化防止坍缩。该方法在真实世界数据上实现了优于现有基线的鲁棒性，但其缺乏物理渲染约束的统计分解是否足以支撑高保真重光照，仍存疑。

## 研究背景

当相机捕获自然场景时，像素值是表面反射率、法线方向与入射光场的非线性乘积。这种耦合导致从单张图像恢复反照率成为病态问题：多种材质-光照组合可产生完全相同的观测。Retinex 理论指出，图像中的高频梯度通常对应反照率变化，而低频平滑变化对应光照效应，这为解耦提供了早期启发。然而，真实世界光照的复杂性与多样性使得基于梯度的启发式规则失效，必须引入更强的先验来约束解空间。

逆渲染领域的主流路线依赖合成数据集提供真值标签进行监督训练，但合成数据与真实图像存在显著域差距，导致模型在野外场景泛化能力不足。另一条路线利用多光照序列的自监督一致性约束，如 Li et al. 利用时间序列视频训练网络，但其在强光照变化下易产生阴影残留与颜色偏移。Zhang et al. 提出在潜在空间学习重光照模型，虽改善了结果，但仍依赖隐式涌现的反照率表示，缺乏显式分解机制，导致高光反射无法彻底移除。SAIL 的切入点在于：利用 LDM 强大的生成先验，将其改造为无监督重光照引擎，并在潜在空间显式分离光照不变与依赖分量，从而摆脱对真值标签的依赖。

## 核心方法

### 潜在空间内在分解框架

SAIL 基于 Stable Diffusion V2.1 架构，但摒弃了文本条件，采用图像到图像架构。其核心差异在于：传统扩散模型预测噪声以重建图像，而 SAIL 直接预测潜在空间中的反照率分量 $z^A$ 与光照分量 $z^E$。给定同一场景在不同光照下的图像 $I_i, I_j$，经冻结 VAE 编码器映射为潜在变量 $z_i, z_j$。模型 $F_\theta$ 以 $z_i$ 为条件，对加噪的 $z_j + \epsilon$ 进行去噪，输出分解结果：

$$
F_\theta(z_j + \epsilon, t, z_i) = \left\{ \hat{z}_i^A, \hat{z}_j^E \right\}
$$

其中 $\hat{z}_i^A$ 为条件于 $z_i$ 的反照率潜在，$\hat{z}_j^E$ 为 $z_j$ 的光照潜在。重光照图像通过 $\hat{z}_j = \hat{z}_i^A + \hat{z}_j^E$ 重构。这一设计动机在于：像素域的阴影分量需满足物理可解释性，而潜在域的光照分量 $z^E$ 仅需捕捉统计上的光照变化，降低了学习难度，使模型能更专注于分离高频细节。

### 无监督重光照代理目标与正则化

SAIL 的关键创新在于将“无监督重光照”作为学习光照不变表示的代理目标。训练损失包含重光照重建项 $\mathcal{L}_{\text{relight}} = \| z_j - (\hat{z}_i^A + \hat{z}_j^E) \|_2^2$，迫使模型学习跨光照的一致性。为防止模型坍缩为常数反照率（即将所有信息塞入光照分量），SAIL 引入两项正则化：一是不变性损失 $\mathcal{L}_{\text{invariant}} = \| z_j - \hat{z}_i^A \|_2^2$，约束反照率潜在接近原始图像潜在，保留高频细节；二是光照分量正则化 $\mathcal{L}_{\text{reg}} = \max(0, \hat{z}_i^E)$，惩罚光照潜在的正值，因其分布偏向负值。此外，通过高斯模糊平滑 $\hat{z}_i^E$，抑制高频细节泄漏至光照分量。总损失为：

$$
\mathcal{L} = \mathcal{L}_{\text{relight}} + \mathcal{L}_{\text{albedo}} + \mathcal{L}_{\text{consistency}} + \lambda (\mathcal{L}_{\text{invariant}} + \mathcal{L}_{\text{reg}})
$$

其中 $\lambda=0.5$。该设计解决了自监督方法中“反照率-阴影”歧义性导致的解空间坍缩问题，确保反照率估计在多种光照下保持一致且富含细节。

## 实验评估

SAIL 在 MIDIntrinsics、IIW 和 MAW 三个真实世界数据集上评估，对比 IntrinsicDiffusion、RGB→X 和 LatentIntrinsics 等基线。基线覆盖监督扩散、自监督 CNN 及潜在空间重光照三类路线，但未包含 3D 逆渲染方法（因任务维度不同）。在 MIDIntrinsics 上，SAIL 取得 17.00 PSNR 和 0.63 SSIM，显著优于 LatentIntrinsics（13.12 PSNR, 0.54 SSIM）和 IntrinsicDiffusion（11.73 PSNR, 0.39 SSIM）。

| 方法 | PSNR (dB) | SSIM |
|---|---|---|
| IntrinsicDiffusion [13] | 11.73 | 0.39 |
| RGB →X [28] | 7.19 | 0.35 |
| LatentIntrinsics [29] | 13.12 | 0.54 |
| SAIL (Ours) | 17.00 | 0.63 |

消融实验显示，移除正则化损失导致模型坍缩，PSNR 降至 15.26；移除交叉一致性损失 $\mathcal{L}_{\text{consistency}}$ 使跨光照稳定性下降，PSNR 为 16.68；移除光照分量高斯模糊则导致细节保留不足，PSNR 为 17.85。这表明正则化项对防止解空间坍缩至关重要，而高斯模糊在细节保留与稳定性间取得平衡。

评估边界方面，SAIL 仅报告 PSNR 和 SSIM，缺乏感知质量指标（如 LPIPS）或物理一致性度量。训练依赖 MIT Dataset 和 BigTime 的多光照序列，若序列光照变化不足，可能影响泛化。代码未公开，但超参数（batch size 40, 35k steps, 4x H200 GPUs）详细披露，可复现性较高。

## 关联研究分析

从问题动机看，SAIL 与 LatentIntrinsics [29] 均利用潜在空间重光照，但 SAIL 引入显式分解与正则化，解决了 LatentIntrinsics 中反照率隐含涌现导致的高光残留问题。这一差异源于 SAIL 对“光照不变性”的显式建模，而非依赖隐式学习。然而，SAIL 缺乏物理渲染方程约束，其光照分量 $z^E$ 仅为统计近似，而非物理阴影，这可能导致在极端光照下重光照失真。

从方法设计看，SAIL 与 IntrinsicDiffusion [13] 同属扩散模型路线，但 SAIL 采用无监督代理目标，摆脱了对合成真值的依赖。IntrinsicDiffusion 依赖监督信号，在域外数据上泛化能力受限；SAIL 通过自监督一致性约束，在真实世界数据上表现更优。但 SAIL 的训练数据仍限于多光照序列，若场景动态变化或光照剧烈突变，其一致性假设可能失效。

## 总结

SAIL 旨在解决真实世界单图反照率估计中因光照耦合导致的病态问题，现有监督方法受域差距限制，自监督方法缺乏显式分解机制。SAIL 利用 LDM 的无监督重光照作为代理目标，在潜在空间显式分离光照不变与依赖分量，并通过正则化防止坍缩。实验表明，SAIL 在 MIDIntrinsics 上取得 17.00 PSNR，优于 LatentIntrinsics 的 13.12 PSNR。其边界在于缺乏物理约束，光照分量为统计近似，且在光照剧烈变化下的一致性假设可能失效。当训练序列的光照变化范围有限时，模型对未见光照条件的泛化能力是否依然鲁棒，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_7bddac92d9fe)