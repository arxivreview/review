# CVPR2026最新论文 ｜PixelDiT: Pixel Diffusion Transformers for Image Generation ｜像素空间扩散的双层级解耦架构

研究机构：美国罗切斯特大学

作者：Yongsheng Yu、Wei Xiong、Weili Nie 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.20645)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.20645)

> 扩散模型在潜空间中迭代去噪虽降低了计算开销，但预训练自编码器（Autoencoder, AE）的重构上限限制了高频细节保真度，且两阶段训练存在目标错位。现有像素空间方法因缺乏高效的逐像素建模机制，难以在可接受算力下平衡全局语义与局部纹理。PixelDiT 提出双层级 Transformer 架构，将语义推理与像素细节解耦，并通过像素级自适应层归一化（Pixel-wise AdaLN）与 Token 压缩实现端到端像素生成。该架构在 ImageNet 256 上取得 1.61 FID，逼近潜空间模型上限，但其在超高分辨率下的显存扩展策略与训练收敛稳定性仍存疑。

## 研究背景

扩散模型（Diffusion Models）通过前向加噪与反向去噪建模数据分布，其推理效率受限于多步迭代机制。为降低计算成本，潜空间扩散模型（Latent Diffusion Models, LDMs）引入变分自编码器（VAE）将图像压缩至低维潜空间，确立了“编码器-扩散-解码器”的两阶段范式。然而，VAE 的重构目标与下游生成目标仅部分对齐，且压缩过程不可逆地丢弃高频细节，导致生成图像保真度受限于 AE 的重构上限。

像素空间扩散直接在原始 RGB 空间去噪，消除了 AE 信息瓶颈，但面临高维数据分布复杂与优化收敛慢的挑战。现有像素空间方法存在根本性权衡：激进的分块（Patchification）策略虽降低了注意力计算成本，但削弱了逐像素交互建模，阻碍精细纹理生成；而接近像素粒度的设计虽保留细节，但全局注意力需处理极长序列，导致二次方计算复杂度与高昂的训练采样成本。PixelDiT 的切入点在于指出“缺乏高效像素建模机制”是像素空间扩散落地的核心障碍，旨在通过架构解耦同时捕获全局语义与逐像素更新。

## 核心方法

### 双层级 DiT 架构参照系

本文问题属于像素空间高效生成路线，与标准潜空间扩散的关键差异在于摒弃了预训练 AE，直接在像素空间进行端到端训练。参照系为单一骨干 Transformer 扩散模型，其通常做法是将图像划分为固定大小的 Patch 作为 Token 进行全局注意力计算。本文的核心差异在于将语义学习与像素细节建模解耦为两条并行路径，以解决单一骨干在像素空间下无法兼顾全局布局与局部纹理的失效问题。

### 语义与像素解耦的双路径设计

双层级架构将图像语义推理委托给粗粒度的 Patch-level DiT，将细节精化委托给细粒度的 Pixel-level DiT（PiT）。Patch-level 路径采用大 Patch 尺寸（如 $p=16$），在短序列上执行长程注意力以捕获全局布局；Pixel-level 路径则操作于逐像素 Token，通过降低隐藏维度（$D_{pix} \ll D$）确保密集计算的高效性。该设计解决了单一骨干中全局注意力与局部细节建模相互干扰的问题，使得模型能在保持全局一致性的同时，以可接受的算力成本进行逐像素的高频细节生成。

### 像素级自适应调制与 Token 压缩

Pixel-wise AdaLN 机制通过线性投影将 Patch-level 输出的语义 Token 扩展为逐像素的调制参数，实现像素级更新与全局语义的对齐。其调制参数 $\Theta$ 由语义 Token $s_{cond}$ 经线性层 $\Phi$ 生成：

$$ \Theta = \Phi(s_{cond}) \in \mathbb{R}^{B \cdot L \times p^2 \times 6D_{pix}} $$

该公式将每个 Patch 的语义上下文映射为 $p^2$ 组独立的缩放、平移与门控参数，使每个像素的更新均受全局语义引导，克服了传统 Patch-wise AdaLN 无法捕获密集空间变化的局限。

为降低全局注意力的二次方复杂度，Pixel Token Compaction 机制在注意力前将 $p^2$ 个像素 Token 压缩为单个紧凑 Patch Token，注意力后再扩展回像素。压缩算子 $\mathcal{C}$ 与扩展算子 $\mathcal{E}$ 定义为：

$$ \mathcal{C}: \mathbb{R}^{p^2 \times D_{pix}} \rightarrow \mathbb{R}^{D}, \quad \mathcal{E}: \mathbb{R}^{D} \rightarrow \mathbb{R}^{p^2 \times D_{pix}} $$

该机制将注意力序列长度从 $H \times W$ 降至 $L = (H/p)(W/p)$，实现 $p^4$ 倍的注意力成本缩减。与 VAE 的有损瓶颈不同，此压缩仅针对注意力操作，高频信息通过残差连接与学习到的扩展层保留，确保了细节保真度。

## 实验评估

实验在 ImageNet 256×256 与 512×512 上进行，基线覆盖潜空间 SOTA（如 RAE, LightningDiT）与像素空间模型（如 JiT, PixelFlow）。缺失最新蒸馏加速模型对比，但覆盖了主要架构路线。

| 方法 | 训练 Epochs | 参数量 | gFID↓ | sFID↓ | IS↑ | Precision↑ | Recall↑ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| RAE-XL | 800 | 839M | 1.13 | - | 262.6 | 0.78 | 0.67 |
| LightningDiT | 800 | 675M | 1.35 | 4.15 | 295.3 | 0.79 | 0.65 |
| JiT-G | 600 | 2B | 1.82 | - | 292.6 | 0.79 | 0.62 |
| PixelFlow-XL | 320 | 677M | 1.98 | 5.83 | 282.1 | 0.81 | 0.60 |
| PixelDiT-XL | 320 | 797M | 1.61 | 4.68 | 292.7 | 0.78 | 0.64 |

PixelDiT-XL 在 320 epochs 下取得 1.61 gFID，显著优于像素空间基线 PixelFlow-XL（1.98）与 JiT-G（1.82），且 Recall 达到 0.64，优于 PixelFlow-XL 的 0.60，表明其在多样性-保真度权衡上更具优势。

| 模型变体 | Epoch | gFID↓ |
| :--- | :--- | :--- |
| A: Vanilla DiT/16 | 80 | 9.84 |
| B: + Dual-level, patch-wise AdaLN | 80 | OOM |
| B: + Pixel Token Compaction | 80 | 3.50 |
| C: + Pixel-wise AdaLN | 80 | 2.36 |
| C: + Pixel-wise AdaLN | 320 | 1.61 |

消融实验显示，引入双层级架构但未使用 Token 压缩导致显存溢出（OOM），验证了压缩机制的必要性。添加 Pixel Token Compaction 后，80 epochs 的 gFID 从 OOM 降至 3.50；进一步引入 Pixel-wise AdaLN 后，gFID 降至 2.36，证明像素级调制对对齐全局语义与局部更新的关键作用。

评估指标涵盖 gFID、sFID、IS 及 Precision-Recall，协议遵循 ADM 标准。代码与模型权重已开源，超参数（如学习率、Batch Size）详细披露，可复现性良好。局限在于未报告低比特量化下的性能，且 1024 分辨率 T2I 实验未提供与潜空间 SOTA 的严格同预算对比。

## 关联研究分析

从问题动机看，PixelDiT 与 JiT 同属像素空间回归路线，但 JiT 依赖大 Patch 与 $x_0$-prediction 解决高维优化，而 PixelDiT 通过双层级解耦显式建模逐像素交互。JiT 的单一骨干设计在细节生成上受限于 Patch 粒度，PixelDiT 的 PiT 路径弥补了这一盲区，但引入了额外的架构复杂度。从方法设计看，PixelDiT 借鉴了 REPA 的表示对齐思想，但将其应用于像素空间而非潜空间。REPA 通过 DINOv2 对齐加速潜空间收敛，PixelDiT 则利用 Patch-level 语义 Token 调制 Pixel-level 更新，验证了语义对齐在像素域的必要性。然而，PixelDiT 的 Token 压缩机制与潜空间 VAE 的压缩在信息保留机制上存在本质差异，前者为可逆的注意力优化，后者为有损的重构瓶颈，这一差异在超高分辨率下的长期影响尚不明确。

## 总结

PixelDiT 旨在解决像素空间扩散中全局语义与局部纹理建模的计算效率矛盾。现有方法因单一骨干无法兼顾两者而陷入权衡，PixelDiT 凭借双层级解耦架构与 Pixel-wise AdaLN 机制，实现了端到端像素生成的高效性。实验证明其在 ImageNet 256 上取得 1.61 gFID，逼近潜空间 SOTA，并在 T2I 任务中展现扩展潜力。其边界在于 320 epochs 的训练成本高于部分潜空间模型，且 1024 分辨率下的显存扩展策略未充分验证。当分辨率进一步提升至 4K 时，Pixel Token Compaction 的压缩比是否足以维持显存可控，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.20645)