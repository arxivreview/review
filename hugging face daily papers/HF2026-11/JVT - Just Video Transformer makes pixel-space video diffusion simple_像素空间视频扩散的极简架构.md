# HuggingFace最新推荐论文 ｜JVT: Just Video Transformer makes pixel-space video diffusion simple ｜像素空间视频扩散的极简架构

研究机构：浙江大学

作者：Jianjun Zhou、Hua Geng、Haoyu Guo

论文原文见 [arXiv](https://arxiv.org/abs/2611.18549)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2611.18549)

> 导读 视频生成领域长期受困于潜空间压缩带来的重建误差与跨模态建模壁垒，主流方案依赖变分自编码器（Variational Autoencoder, VAE）与扩散Transformer（Diffusion Transformer, DiT）的级联架构。现有像素空间生成方法虽规避了VAE瓶颈，却往往引入U-Net跳跃连接或级联阶段等复杂结构，限制了架构的简洁性与可扩展性。JVT（Just Video Transformer）提出一种纯DiT风格的像素空间视频生成模型，通过Patch-first嵌入与Register Tokens机制，在无需预训练自编码器的情况下实现高质量视频生成。该工作验证了极简Transformer在像素空间视频建模中的可行性，但其在高分辨率长视频场景下的计算效率与显存占用仍存疑。

## 研究背景

当视频生成模型试图在原始像素空间直接建模时，高维数据带来的计算复杂度呈指数级增长，迫使研究者引入潜空间压缩。潜空间扩散模型通过VAE将视频映射至低维潜空间，显著降低了DiT的Token数量与计算开销，确立了“VAE+DiT”的主流范式。然而，VAE的重建误差构成了生成质量的上限，且其RGB特定的编码结构阻碍了深度、光流等像素对齐模态的联合建模。

为突破VAE瓶颈，像素空间扩散模型应运而生。早期像素空间方法依赖U-Net跳跃连接、级联生成或频率分解等专用架构，虽能处理高分辨率数据，但引入了额外的架构与训练复杂度。近期，JiT（Li & He, 2026）在图像生成中证明，简单的大Patch DiT即可媲美潜空间扩散。这一发现激发了本文的核心问题：在视频领域，一个无U-Net、无级联、无VAE的纯DiT架构，能否通过简单的时空下采样与条件注入机制，实现与潜空间基线相当甚至更优的生成质量？

## 核心方法

### 像素空间DiT参照系

JVT将视频生成建模为从噪声像素预测干净视频的过程，遵循Rectified Flow目标。与潜空间DiT依赖VAE进行时空下采样不同，JVT通过Patch Embedding直接处理原始像素，将高维视频压缩为Transformer可处理的Token序列。该架构摒弃了U-Net的跳跃连接与级联阶段，仅保留标准Transformer块，其核心挑战在于如何设计高效的时空下采样策略与条件注入机制，以在保持Token数量可控的同时保留时空细节。

### Patch-first时空下采样

在像素空间DiT中，Patch Embedding承担了潜空间VAE的压缩功能。传统Tubelet嵌入使用单一3D卷积将时空Patch映射为Token，计算开销大且缺乏结构先验。JVT引入通道瓶颈（Bottleneck）结构，并借鉴深度可分离卷积的因子化原则，提出Patch-first嵌入。该设计将时空操作解耦：首先通过Patch-wise 2D卷积提取帧内空间特征，再通过Frame-wise 1D卷积聚合时序信息。

$$
x_t = (1 - t)x_0 + t\epsilon, \quad \hat{x}_0 = f_\theta(x_t, t, c)
$$

该公式定义了JVT的Clean Data Prediction目标，模型直接预测干净视频 $\hat{x}_0$，而非噪声或速度。Patch-first嵌入通过分离空间与时序操作，降低了3D卷积的计算复杂度，同时通过瓶颈宽度 $C_b$ 控制Token的维度，鼓励紧凑的低维表示。实验表明，Patch-first嵌入在降低FLOPs的同时，实现了比Tubelet更低的训练损失与更优的FVD。

### Register Tokens与条件引导

在像素空间DiT中，条件信息（如类别、噪声水平）通常通过自适应层归一化（Adaptive Layer Normalization, AdaLN）注入。JVT进一步引入Register Tokens，在Transformer块之间插入可学习的额外Token，作为条件信息的补充载体。Register Tokens在第一个 $L_1$ 块后插入，在剩余 $L_2$ 块后丢弃，其构造方式为：

$$
R = R_0 + \text{Repeat}(e_r, \ell_r), \quad \tilde{X}^{(L_1)} = \text{Concat}(R, X^{(L_1)})
$$

其中 $R_0$ 为可学习基础Register，$e_r$ 为条件嵌入。在采样阶段，JVT采用Register Guidance（RG）放大Register的贡献：

$$
v_{rg} = v_r + w_{rg}(v_r - v_{nr})
$$

该公式通过对比有Register与无Register的速度预测差异，动态调整生成轨迹。RG与Classifier-free Guidance（CFG）结合，形成 $v_{cfg+rg}$，分别加权条件引导与Register引导。这一机制在不增加推理步数的前提下，显著提升了生成质量，尤其在类别多样性高的UCF-101数据集上表现突出。

## 实验评估

JVT在UCF-101、FaceForensics、SkyTimelapse和Taichi-HD四个数据集上评估，采用Fréchet Video Distance（FVD）作为主要指标。基线覆盖GAN（StyleGAN-V）、自回归模型（VideoGPT）及潜空间DiT（Latte）。JVT在UCF-101类别条件生成上取得1365 FVD，显著优于Latte的47797，验证了像素空间DiT在小分辨率短片段场景下的竞争力。

| Method | Res. | Cond. UCF101 | Uncond. UCF101 | Uncond. FaceForensics | Uncond. SkyTimelapse | Uncond. Taichi-HD |
| --- | --- | --- | --- | --- | --- | --- |
| Latte | 256² | 47797 | – | 3400 | 5982 | 15960 |
| JVT (Ours) | 256² | 1365 | 4135 | 3286 | 4658 | 1191 |
| JVT+RG (Ours) | 256² | 1292 | 2159 | 3180 | 4780 | 1243 |

消融实验表明，Patch-first嵌入在 $C_b=32$ 时达到质量与效率的最佳平衡，其FVD为1350，低于Tubelet的1450，且Denoiser FLOPs从1089 TFLOPs降至1082 TFLOPs。Register Tokens在UCF-101上带来显著增益（FVD从4135降至2159），但在其他数据集上收益有限，表明其有效性依赖于数据多样性。

| Embedding | Cb | FVD(↓) | Final loss(↓) | Denoiser FLOPs (TFLOPs) | Denoiser Latency (ms, ↓) |
| --- | --- | --- | --- | --- | --- |
| Tubelet | – | 1450 | 0.0151 | 1089 | 1607 |
| Tubelet | 32 | 1474 | 0.0150 | 1083 | 1596 |
| Patch-first | 32 | 1350 | 0.0143 | 1082 | 1559 |
| Frame-first | 32 | 1466 | 0.0142 | 1101 | 1589 |

评估边界方面，JVT仅在256×256分辨率、16帧短片段上验证，未涉及高分辨率长视频场景。其像素空间特性导致Token数量随分辨率平方增长，在4K或分钟级视频生成中，显存占用与计算延迟可能成为不可逾越的瓶颈。此外，JVT未与Sora、Wan等大规模高效模型对比，其在工业级部署中的效率优势尚待验证。

## 关联研究分析

从问题动机看，JVT与SANA-Video均致力于突破DiT的计算瓶颈，但路径截然不同。SANA-Video通过线性注意力机制降低空间Token的二次方复杂度，仍依赖VAE压缩；JVT则通过像素空间直接建模规避VAE，但保留了二次方注意力。这一差异源于对“效率瓶颈”的不同归因：SANA-Video认为注意力计算是主要瓶颈，JVT认为VAE重建误差与跨模态壁垒是核心限制。在长视频场景下，JVT的Token数量将远超潜空间模型，其二次方注意力开销是否抵消省去VAE的增益，论文未给出回答。

从方法设计看，JVT与Latte同属DiT架构，但条件注入机制不同。Latte依赖AdaLN注入条件，JVT引入Register Tokens与RG。Register Tokens在UCF-101上的显著增益表明，像素空间DiT可能需要额外的计算槽位来补偿缺乏VAE先验带来的条件建模不足。然而，Register Tokens在FaceForensics等低多样性数据集上收益有限，暗示其有效性可能依赖于数据分布的复杂性，而非普适的架构改进。

## 总结

JVT针对潜空间扩散模型的重建误差与跨模态壁垒，提出纯DiT像素空间视频生成架构，通过Patch-first嵌入与Register Tokens机制，在256×256分辨率短片段上实现FVD 1365，优于潜空间基线Latte。该工作验证了极简Transformer在像素空间视频建模中的可行性，并展示了RGB-Disparity联合生成的跨模态能力。然而，其评估局限于小分辨率短片段，未验证高分辨率长视频场景下的显存与计算效率。当视频分辨率提升至4K或时长扩展至分钟级时，像素空间DiT的Token数量激增与二次方注意力开销，是否会使其效率优势彻底丧失，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2611.18549)