# HuggingFace最新推荐论文 ｜Decoding Without a Decoder: Direct Pixel Prediction from Diffusion Transformers ｜无解码器扩散：直接像素预测

研究机构：美国加州理工学院、美国斯坦福大学

作者：Hansheng Chen、Shengqu Cai、Jan Ackermann 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2611.22287)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2611.22287)

> 导读 扩散模型在生成图像或视频时，通常依赖一个独立的卷积解码器将去噪后的潜在表示映射为像素，这一过程不仅增加了部署复杂度，还占据了显著的推理时间。现有的加速方法多聚焦于优化扩散Transformer（Diffusion Transformer, DiT）内部的注意力计算或缓存机制，却忽视了DiT与解码器接口处的结构性冗余。本文提出DWD方法，通过在DiT末端并行添加一个线性输出头，直接利用最后层Token生成最终像素，从而在推理时完全移除解码器。该架构通过双头分离机制解耦了去噪轨迹与像素渲染，在提升生成质量的同时降低了计算开销。然而，该方法在基线解码器已高度优化的模型上收益有限，其普适性仍受限于潜在空间的维度特性。

## 研究背景

当扩散模型在潜在空间完成去噪后，必须通过变分自编码器（Variational Autoencoder, VAE）的解码器将低维潜在向量还原为高维像素。这一过程在视频生成中尤为昂贵，例如在H100 GPU上，Wan 1.3B模型生成5秒视频时，解码耗时占到了总推理时间的70%。尽管DiT内部的Transformer块已具备强大的特征提取能力，但标准范式仍强制要求通过独立的卷积网络进行上采样和色彩空间转换，导致计算资源在模型边界处被重复消耗。

领域内对DiT的加速研究主要沿着稀疏注意力、特征缓存和量化剪枝三条路线展开，旨在降低DiT内部的二次方计算复杂度或内存访问开销。然而，这些方法均未触及DiT与解码器之间的接口瓶颈。近期研究表明，DiT最后层的Token已包含丰富的像素级信息，甚至可以通过简单的线性探针恢复大部分图像结构。这一发现挑战了“解码器不可或缺”的传统假设，揭示了通过重构输出头来消除解码器冗余的可能性。DWD正是基于这一被忽略的接口冗余，提出了一种无需重训整个模型即可替代解码器的轻量级架构。

## 核心方法

### 双头分离架构与线性像素映射

在标准DiT架构中，去噪头（Denoising Head）负责预测速度场或噪声，其输出需经解码器映射为像素。DWD在DiT的最后一层Transformer块之后，并行引入了一个线性DWD头。该头直接读取经过归一化和调制后的最后层Token $\bm{h}$，通过线性变换生成像素块 $\hat{\bm{x}}_i$：

$$ \hat{\bm{x}}_{i}=\operatorname{Linear}({\bm{h}}_{i})={\bm{W}}{\bm{h}}_{i}+{\bm{b}} $$

其中 $\bm{W}$ 和 $\bm{b}$ 为可学习参数。这一设计动机在于利用DiT内部已完成的非线性特征变换，避免解码器中重复的卷积计算。DWD头仅在去噪过程的最后一步（$t$ 为小正数）被激活，此时输入仍保留少量噪声，赋予模型生成高频细节的自由度，避免了在 $t=0$ 时因输入完全平滑而导致的细节丢失。

### 解耦训练目标与轨迹锚定

为了在移除解码器的同时保持预训练模型的生成能力，DWD采用解耦的训练策略。DWD头使用像素质量损失 $\mathcal{L}_{\mathrm{pix}}$ 进行优化，包含L1重建、LPIPS感知损失和对抗损失：

$$ \mathcal{L}_{\mathrm{pix}}=\mathbb{E}_{{\bm{x}},{\bm{z}},{\bm{c}},t\sim p_{\mathrm{pix}}}\Big[\|\hat{{\bm{x}}}-{\bm{x}}\|_{1}+\mathrm{LPIPS}(\hat{{\bm{x}}},{\bm{x}})+\ell_{\mathrm{adv}}(\hat{{\bm{x}}})\Big] $$

与此同时，去噪头通过轨迹锚定损失 $\mathcal{L}_{\mathrm{traj}}$ 与冻结的预训练模型保持一致：

$$ \mathcal{L}_{\mathrm{traj}}=\mathbb{E}_{{\bm{x}},{\bm{z}},{\bm{c}},t\sim p_{\mathrm{traj}}}\Big[\big\|\hat{{\bm{u}}}-\hat{{\bm{u}}}^{\mathrm{ref}}\big\|_{2}^{2}\Big] $$

这种双头分离机制解决了像素扩散模型中常见的“平滑效应”问题。若将像素损失直接施加于去噪头，$\ell_2$ 损失倾向于预测条件均值，导致样本多样性坍缩和细节模糊。通过分离，去噪头专注于维持轨迹的分布一致性，而DWD头专注于提升感知质量，二者在训练时通过不同的时间步分布 $p_{\mathrm{pix}}$ 和 $p_{\mathrm{traj}}$ 进行采样，实现了功能解耦。

## 实验评估

实验在ImageNet 256x256、COCO-10k文本到图像生成以及Wan视频生成任务上进行。基线覆盖了潜在空间模型（SiT-XL/2-REPA, FLUX.2 klein）和像素空间模型（JiT, AnisoFlow）。

| 方法 | 骨干模型 | 解码器 | FID (ImageNet) | IS (ImageNet) |
| :--- | :--- | :--- | :--- | :--- |
| SiT-XL/2-REPA | SiT-XL/2 | SD-VAE | 1.38 | 306.2 |
| **DWD** | SiT-XL/2 | – | **1.36** | **312.5** |
| SiT-XL/2-REPA-E | SiT-XL/2 | E2E-VA-VAE | 1.12 | 302.9 |
| **DWD** | SiT-XL/2 | – | **1.06** | **303.1** |
| AnisoFlow-H/16 | AnisoFlow | – | 1.55 | 300.1 |
| **DWD** | AnisoFlow | – | **1.43** | **303.5** |

在ImageNet上，DWD在所有测试模型上均降低了FID。特别是在像素模型AnisoFlow上，FID从1.55降至1.43，达到了像素流模型的SOTA。在视频生成中，DWD使Wan模型的Warping Error降低了23%，显著减少了闪烁和细节扭曲。

消融实验揭示了双头分离的必要性。若移除独立头，将像素损失直接施加于去噪头（w/o separate head），AnisoFlow的FID反而从1.55恶化至1.71。这表明感知损失与去噪目标存在内在冲突，必须通过架构分离来调和。此外，线性头与卷积头（DWD-conv）的性能差异不显著，证实了线性映射足以提取最后层Token中的像素信息。

评估边界方面，DWD在FLUX.2 klein模型上的提升微乎其微（FID 15.13 vs 15.05）。这是因为FLUX.2的潜在空间维度极高（128维），解码本身已非常高效，限制了线性头的优化空间。此外，论文未提供与TeaCache等主流加速方法的直接对比，无法评估DWD与内部加速技术的叠加收益。

## 关联研究分析

从问题动机看，DWD与REPA（Representation Alignment）存在本质差异。REPA通过引入外部视觉编码器特征对齐来加速训练收敛，属于训练阶段的辅助手段；而DWD将内部Token直接用于推理阶段的像素生成，属于架构层面的重构。REPA证明了内部特征与语义的关联，DWD则进一步证明了这种关联足以替代独立的解码网络。

从方法设计看，DWD与PiD（Pixel Diffusion Decoder）代表了简化解码的两种路径。PiD使用蒸馏后的像素扩散模型作为解码器，保留了生成式解码的能力，但计算量依然较大；DWD则采用非生成式的线性映射，计算量极低。然而，PiD在低维潜在空间（如SD-VAE）上可能更具鲁棒性，而DWD在FLUX.2等高维空间上的优势是否能在低维空间复现，论文未给出明确回答。

## 总结

本文针对扩散模型推理中解码器计算冗余与质量瓶颈的矛盾，提出DWD方法，通过双头分离架构利用DiT最后层Token直接生成像素。实验证明，该架构在ImageNet上将AnisoFlow的FID降至1.43，并在视频生成中显著降低Warping Error。然而，DWD的收益高度依赖于基线解码器的效率，在FLUX.2等高效解码器上提升有限。当潜在空间维度较低时，线性头是否仍能保持对高频细节的恢复能力，仍需进一步验证。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2611.22287)