# CVPR2026最新论文 ｜InverFill: One-Step Inversion for Enhanced Few-Step Diffusion Inpainting ｜一步反转网络

作者：Duc Vu、Kien Nguyen、Trong-Tung Nguyen 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.23463)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.23463)

> 少步扩散模型在图像修复中因随机噪声初始化导致语义错位，现有混合采样策略无法在低函数评估次数（NFEs）下恢复背景一致性。InverFill 通过一步反转网络将掩码图像映射为语义对齐的初始噪声，替代随机高斯初始化。该方法无需真实图像监督，仅增加0.06秒推理延迟，使少步模型性能逼近多步专用修复系统。其核心贡献在于解决了少步修复中的分布失配问题，但在极端复杂语义场景下的泛化能力仍存疑。

## 研究背景

潜空间扩散模型通过变分自编码器（VAE）将图像压缩至低维潜空间，利用去噪过程从随机高斯噪声逐步生成图像。传统多步模型依赖数十次迭代修正噪声，而少步蒸馏模型（如SANA-Sprint、SDXL-Turbo）将步骤压缩至4-8步，每步执行大幅离散更新。这种加速机制导致模型缺乏逐步适应上下文的机会，当初始噪声与掩码区域语义距离过大时，少步去噪无法纠正错位，产生模糊或风格不一致的伪影。

图像修复任务要求生成内容既符合文本提示，又与未掩码背景视觉连贯。主流方案分为两类：一是微调专用修复架构（如BrushNet），依赖大规模真实图像-掩码-文本三元组训练；二是无训练混合采样（Blended Sampling），在每步去噪时强制保留未掩码区域像素。前者计算开销大且泛化受限，后者在多步模型中有效，但在少步模型中因更新幅度过大而失效。现有少步修复尝试如TurboFill采用3步对抗训练，仍需真实图像监督且架构复杂。InverFill的切入点在于：不修改生成器本身，而是通过一步反转网络为少步模型提供语义对齐的初始噪声，从源头消除随机初始化带来的语义错位。

## 核心方法

### 方法参照系

标准少步修复流程为：随机高斯噪声 $z_T \sim \mathcal{N}(0, I)$ 输入少步生成器，结合混合采样策略逐步去噪。本文问题与该通用流程的关键差异在于：随机噪声缺乏对未掩码区域语义结构的感知，导致少步更新无法收敛至与背景和谐的解。

### 掩码图像一步反转网络

设计动机：解决随机噪声初始化在少步修复中导致的语义错位，使初始噪声携带未掩码区域的语义信息。InverFill引入一步反转网络 $\mathbf{F}_\theta$，其架构继承自少步生成器 $\mathbf{G}$ 并共享预训练权重。给定掩码图像 $I_m$ 和文本提示 $c$，网络将掩码潜变量 $z_0[m] = E(I_m)$ 映射为反转噪声潜变量 $\hat{z}_T$。训练目标为最小化重构损失，使 $\mathbf{G}(\hat{z}_T, c)$ 生成的图像潜变量 $\hat{z}_0$ 与原始图像潜变量 $z_0$ 一致。该设计将随机初始化替换为语义感知初始化，使少步去噪从语义对齐的起点开始，大幅降低收敛难度。

$$
\mathcal{L}_{noise} = \| (\hat{z}_T - z_T) \odot (1 - m) \|_2^2, \quad \mathcal{L}_{image} = \| \hat{z}_0 - z_0 \|_2^2
$$

其中 $m$ 为潜空间掩码，$\odot$ 表示逐元素乘法。该公式表明：噪声空间损失仅在未掩码区域计算，避免对无信息掩码区域的无效惩罚；图像空间损失确保整体重构保真度。

### Re-Blending与高斯正则化

设计动机：解决掩码输入导致的信息泄漏与分布失配问题。直接训练 $\mathbf{F}_\theta$ 时，未掩码区域的图像结构会泄漏至 $\hat{z}_T$，而掩码区域因缺乏监督呈现低方差伪影，导致 $\hat{z}_T$ 偏离高斯分布，使生成器 $\mathbf{G}$ 在计算 $\hat{z}_0$ 时崩溃。Re-Blending操作在训练和推理中，将 $\hat{z}_T$ 的掩码区域替换为随机高斯噪声 $\epsilon' \sim \mathcal{N}(0, I)$，形成混合潜变量 $\hat{z}_T[blend]$。高斯正则化损失进一步约束 $\hat{z}_T[blend]$ 对齐标准高斯分布：

$$
\mathcal{L}_{reg} = \| \hat{z}_T[blend] - \epsilon' \|_2^2
$$

该公式强制反转噪声在掩码区域保持高斯特性，防止分布失配导致的重构失败。Re-Blending与 $\mathcal{L}_{reg}$ 协同作用，既保留未掩码区域的语义信息，又确保掩码区域的噪声符合扩散模型先验，实现少步修复中的稳定收敛。

## 实验评估

实验在BrushBench（600张图像）和MagicBrush（535张图像）上进行，分辨率1024×1024。基线覆盖少步模型（SANA-Sprint 0.6B、SDXL-Turbo）与多步模型（HD-Painter、SDXL-Inpainting），但缺失GAN类及传统修复基线。InverFill在少步设置下显著提升性能：SANA-Sprint 0.6B（2 NFEs）+ InverFill在BrushBench上IR从11.02提升至11.65，HPS从26.21提升至27.93；SDXL-Turbo（4 NFEs）+ InverFill的IR达12.38，超过多步HD-Painter（30 NFEs）的12.82？不，12.38低于12.82，但论文声称“outperforms HD-Painter on key metrics”，需核对原文。原文称“SDXL-Turbo + InverFill (4 NFEs) outperforms HD-Painter (30 NFEs) on key metrics”，但表格中HD-Painter IR为12.82，SDXL-Turbo + InverFill IR为12.38，IR未超过。可能指HPS或CLIP？HD-Painter HPS 28.17，SDXL-Turbo + InverFill HPS 28.44，确实超过。CLIP HD-Painter 27.43，SDXL-Turbo + InverFill 27.67，也超过。因此“key metrics”指HPS和CLIP，非IR。

| 方法 | NFEs | BrushBench IR×10↑ | BrushBench HPS×10²↑ | BrushBench AS↑ | BrushBench CLIP↑ |
|---|---|---|---|---|---|
| SANA-Sprint 0.6B | 2 | 11.02 | 26.21 | 6.05 | 27.12 |
| SANA-Sprint 0.6B + InverFill | 2 | 11.65 | 27.93 | 6.15 | 27.17 |
| SDXL Turbo | 4 | 11.42 | 28.20 | 6.06 | 27.26 |
| SDXL Turbo + InverFill | 4 | 12.38 | 28.44 | 6.08 | 27.67 |
| HD-Painter | 30 | 12.82 | 28.17 | 6.30 | 27.43 |

InverFill在少步设置下，HPS和CLIP指标超过多步HD-Painter，IR略低但差距缩小。消融实验显示，高斯正则化损失 $\mathcal{L}_{reg}$ 对性能提升关键：SANA-Sprint 0.6B（2 NFEs）中，无 $\mathcal{L}_{reg}$ 时IR为11.11，有 $\mathcal{L}_{reg}$ 时IR为11.40，HPS从26.69提升至27.22。Re-Blending操作防止信息泄漏，但单独使用不足以恢复细节，需 $\mathcal{L}_{reg}$ 协同。评估指标涵盖图像质量（IR、HPS、AS）与文本对齐（CLIP），但未报告FID或LPIPS等分布距离指标，可能低估语义错误。可复现性方面，论文未提供代码URL，超参数细节有限，GPU为NVIDIA A100 40GB。

## 关联研究分析

从问题动机看，InverFill与SONIC同属效率优化路线，但解决机制不同。SONIC通过频谱域线性化优化初始噪声，避免反向传播通过去噪器，侧重计算效率；InverFill通过一步反转网络生成语义对齐噪声，侧重语义一致性。SONIC的线性化近似可能引入去噪轨迹偏差，而InverFill的语义噪声初始化直接缓解少步更新中的语义错位，二者在“噪声优化”与“噪声初始化”上形成互补。InverFill无需重训练生成器，而SONIC需优化初始种子，计算开销更低。

从方法设计看，InverFill与SwiftEdit同属一步反转框架，但任务适配不同。SwiftEdit针对图像编辑，直接映射完整图像至噪声潜变量；InverFill针对掩码输入，引入Re-Blending解决信息泄漏。SwiftEdit的重构目标未约束高斯分布，导致InverFill需额外 $\mathcal{L}_{reg}$。这一差异源于修复任务中掩码区域缺乏监督，而编辑任务中完整图像提供充分约束。InverFill的Re-Blending是否可推广至非掩码编辑任务，论文未探索，可能因编辑任务中信息泄漏问题不显著。

## 总结

InverFill解决的核心矛盾是少步扩散模型在图像修复中因随机噪声初始化导致的语义错位与背景不一致。其切入点在于：不修改生成器，而是通过一步反转网络提供语义对齐的初始噪声，从源头消除随机性带来的收敛困难。该方法通过Re-Blending与高斯正则化解决掩码输入的信息泄漏与分布失配，无需真实图像监督，仅增加0.06秒延迟。实验证明，InverFill使SANA-Sprint 0.6B（2 NFEs）的HPS从26.21提升至27.93，SDXL-Turbo（4 NFEs）的CLIP从27.26提升至27.67，超越多步HD-Painter在HPS和CLIP上的表现。其边界在于：实验未覆盖极端复杂语义或大掩码场景，且未报告FID等分布距离指标，可能低估语义错误。当掩码区域占比超过50%时，反转噪声的语义强度是否足以维持背景一致性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.23463)