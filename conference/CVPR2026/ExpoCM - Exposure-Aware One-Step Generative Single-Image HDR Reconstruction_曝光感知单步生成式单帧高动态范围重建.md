# CVPR2026最新论文 ｜ExpoCM: Exposure-Aware One-Step Generative Single-Image HDR Reconstruction ｜曝光感知单步生成式单帧高动态范围重建

研究机构：电子科技大学

作者：Aoyu Liu、Zhen Liu、Ziyi Wang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.02464)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.02464)

> 单帧高动态范围（High Dynamic Range, HDR）重建旨在从一张低动态范围（Low Dynamic Range, LDR）图像恢复完整亮度信息，但过曝区细节丢失与欠曝区噪声放大导致逆问题高度病态。现有回归方法无法“幻觉”缺失细节，而标准扩散模型因空间均匀假设与数百步采样开销难以兼顾保真度与效率。ExpoCM 将重建重构为概率流常微分方程（Probability Flow Ordinary Differential Equation, PF-ODE）上的条件生成任务，通过曝光感知一致性轨迹实现单步推理。该方法在计算效率上取得突破，但其对极端过曝区细节幻觉的物理一致性边界尚存疑。

## 研究背景

单帧 HDR 重建的核心困境在于传感器动态范围受限导致的信号退化具有空间异质性。过曝区域像素值饱和，结构信息不可逆丢失，必须依赖生成先验进行“幻觉”；欠曝区域信号被噪声淹没，直接回归会放大噪声并模糊细节；而正常曝光区域则保留了可靠的结构与色彩信息。这种退化模式在空间上的非均匀分布，使得任何全局统一的映射函数都难以同时满足三类区域的差异化恢复需求。

传统单帧 HDR 重建多采用卷积神经网络（Convolutional Neural Network, CNN）进行端到端回归，如 HDRCNN 与 ExpandNet，这类方法在正常曝光区表现尚可，但在过曝区因信息缺失而失效。近期，扩散模型（Diffusion Models, DMs）因其强大的分布建模能力被引入该领域，如 RetiDiff，但标准扩散过程对所有像素施加均匀噪声扰动，无法区分过曝与欠曝区的不同退化机制，且需要数百步迭代采样，计算成本高昂。ExpoCM 的切入点在于利用一致性模型（Consistency Models, CMs）的单步生成特性，并针对 HDR 任务的空间异质退化设计曝光感知的生成轨迹，从而在单步推理中同时解决细节幻觉与噪声抑制问题。

## 核心方法

### 条件一致性生成参照系

单帧 HDR 重建通常被视为从 LDR 输入 $\mathbf{y}_0$ 到 HDR 目标 $\mathbf{x}_0$ 的回归映射。ExpoCM 将其重构为条件生成任务，基于 PF-ODE 框架。标准条件一致性轨迹定义中间状态 $\mathbf{x}_t$ 为：

$$ \mathbf{x}_t = \alpha(t)\mathbf{x}_0 + \sigma(t)\boldsymbol{\epsilon} $$

其中 $\alpha(t)$ 和 $\sigma(t)$ 为时变系数，$\boldsymbol{\epsilon} \sim \mathcal{N}(0, \mathbf{I})$。一致性网络 $f_\theta$ 被训练以从任意点 $(\mathbf{x}_t, t)$ 直接预测 $\mathbf{x}_0$，条件为 $\mathbf{y}_0$。该参照系的关键局限在于轨迹定义隐含了空间均匀退化假设，未区分输入图像中不同曝光区域的可靠性差异。

### 曝光感知一致性轨迹（EACT）

标准条件轨迹对所有像素一视同仁，导致过曝区无法有效幻觉细节，欠曝区噪声被直接引入生成过程。ExpoCM 引入曝光掩码生成模块，基于亮度百分位（第2与第98百分位）及过渡带 $\tau=0.02$，将输入软划分为过曝、欠曝与正常曝光区域。针对过曝区，轨迹定义为纯噪声驱动，以鼓励模型从噪声中合成合理细节；针对欠曝区，轨迹注入低通滤波后的 $\mathbf{y}_0$ 结构先验，以抑制噪声并保留粗结构。最终，曝光感知一致性轨迹（Exposure-Aware Consistency Trajectory, EACT）通过加权混合三种区域特定轨迹实现：

$$ \mathbf{x}_t^{EACT} = w_{over} \odot \mathbf{x}_t^{over} + w_{under} \odot \mathbf{x}_t^{under} + w_{good} \odot \mathbf{x}_t^{good} $$

其中 $w_{over}, w_{under}, w_{good}$ 为曝光感知权重图，$\odot$ 表示逐元素乘法。该设计解决了标准扩散过程空间无关性导致的退化处理失效，使生成流能够根据局部曝光条件自适应调整扰动强度与引导信号，从而在单步推理中实现差异化恢复。

### 曝光引导亮度-色度损失（ELC）

生成模型常存在亮度偏差与色度漂移，尤其在极端曝光区域。ExpoCM 在感知均匀的 CIE $L^*a^*b^*$ 空间定义曝光引导亮度-色度损失（Exposure-guided Luminance-Chromaticity, ELC），以解耦亮度与色度监督。损失函数定义为：

$$ \mathcal{L}_{ELC} = w_L \rho(\Delta L^*) + w_C \rho(\Delta C^*) $$

其中 $\Delta L^*$ 为亮度残差，$\Delta C^*$ 为色度残差，$\rho(\cdot)$ 为鲁棒惩罚函数。权重 $w_L$ 与 $w_C$ 根据曝光条件动态调整：在欠曝区，$w_L$ 增大以强制亮度一致性，$w_C$ 减小以容忍噪声导致的色度不可靠；在过曝区，$w_C$ 增大以抑制色度漂移，$w_L$ 减小以容忍亮度偏移。该损失函数通过曝光感知的权重分配，缓解了生成模型在极端光照下的感知失真，提升了重建结果的视觉保真度。

## 实验评估

实验在 HDR-REAL（1,838对）、HDR-EYE（46对）及 AIM2025（18,898对）数据集上进行，对比方法涵盖回归式（HDRCNN, SingleHDR, ExpandNet, HDRUNet）、Transformer 式（HDR-Transformer）及扩散式（DDPM, DDIM, RetiDiff）。基线覆盖较全面，但缺失最新基于大语言模型或智能体框架的单帧方法。

| 数据集 | 方法 | PSNR-µ (dB) | SSIM-µ | LPIPS | ΔE2000 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| HDR-REAL | DDPM | 25.45 | 0.8173 | 0.2365 | 14.26 |
| HDR-REAL | RetiDiff | 27.64 | 0.8354 | 0.2645 | 4.83 |
| HDR-REAL | ExpoCM | 28.66 | 0.8684 | 0.1919 | 4.02 |
| AIM2025 | DDPM | 23.03 | 0.8320 | 0.1580 | 11.24 |
| AIM2025 | RetiDiff | 23.31 | 0.8269 | 0.1511 | 7.74 |
| AIM2025 | ExpoCM | 29.02 | 0.8922 | 0.1286 | 3.90 |

ExpoCM 在两个数据集上均取得最优 PSNR-µ 与最低 LPIPS，其中 HDR-REAL 上 PSNR-µ 较 RetiDiff 提升 1.02 dB，LPIPS 降低 0.0726，表明其在保真度与感知质量上均优于多步扩散基线。

| 消融变体 | PSNR-µ (HDR-REAL) | SSIM-µ (HDR-REAL) | LPIPS (HDR-REAL) |
| :--- | :--- | :--- | :--- |
| Baseline (Uniform) | 21.09 | 0.6917 | 0.3041 |
| Two-Mask | 25.75 | 0.8076 | 0.2785 |
| Three-Mask (EACT) | 25.84 | 0.8282 | 0.2754 |
| w/o ELC (EACT) | 28.56 | 0.8663 | 4.06 |
| Default (EACT+ELC) | 28.66 | 0.8684 | 4.02 |

消融实验显示，从 Baseline 到 Two-Mask 的 PSNR-µ 提升 4.66 dB，验证了区分可靠与不可靠区域的重要性；Three-Mask 进一步微调，表明过曝与欠曝的独立处理优于合并处理。ELC 损失的引入使 PSNR-µ 从 28.56 提升至 28.66，ΔE2000 从 4.06 降至 4.02，证实了曝光感知权重对色彩保真度的贡献。

评估指标涵盖 PSNR、SSIM、MS-SSIM、HDR-VDP、LPIPS 及 ΔE2000，覆盖了保真度、感知质量与色彩准确性。局限在于未报告计算效率的具体数值（仅提及推理时间 0.33s vs DDPM 174.10s），且未提供置信区间。代码已开源，超参数（AdamW, 500k iterations, batch size 4）完整披露，可复现性良好。

## 关联研究分析

从问题动机看，ExpoCM 与 GMODiff 同属生成式单帧 HDR 重建，但 GMODiff 依赖预训练文本到图像扩散模型作为先验，而 ExpoCM 采用从头训练的一致性模型。GMODiff 的优势在于利用大规模预训练数据中的语义先验，但面临计算成本高与物理保真度挑战；ExpoCM 通过曝光感知轨迹设计，在单步推理中实现了更高效的退化处理，但其先验知识完全依赖于训练数据，缺乏 GMODiff 的语义泛化能力。这种差异源于任务特性：HDR 重建更关注物理辐射度恢复，而 GMODiff 更侧重感知美观度，ExpoCM 的 ELC 损失试图在两者间取得平衡，但物理一致性的验证不足。

从方法设计看，ExpoCM 与 RetiDiff 同属扩散模型框架，但 RetiDiff 采用标准迭代采样，而 ExpoCM 利用一致性模型实现单步生成。RetiDiff 通过多步去噪逐步细化细节，计算开销大但可能更稳定；ExpoCM 通过数学混合 ODE 轨迹实现单步推理，效率提升显著，但单步生成在极端过曝区的细节幻觉能力是否优于多步扩散，论文未提供直接对比。此外，ExpoCM 的曝光掩码基于亮度百分位，这是一种启发式策略，对于光照分布极不均匀的场景（如夜景），其鲁棒性可能受限，而 RetiDiff 等标准扩散方法虽无此设计，但通过多步迭代可能更适应复杂光照变化。

## 总结

ExpoCM 旨在解决单帧 HDR 重建中空间异质退化与生成效率的矛盾，通过曝光感知一致性轨迹（EACT）与曝光引导亮度-色度损失（ELC），在单步推理中实现了过曝区细节幻觉与欠曝区噪声抑制的差异化处理。实验表明，该方法在 HDR-REAL 与 AIM2025 上取得最优 PSNR-µ（28.66 dB 与 29.02 dB）及最低 LPIPS（0.1919 与 0.1286），验证了单步生成在保真度与感知质量上的有效性。然而，论文未报告极端过曝区细节幻觉的物理一致性指标，且曝光掩码的启发式设计在复杂光照场景下的鲁棒性未充分验证。当输入图像包含大面积非均匀光照时，基于亮度百分位的掩码划分是否仍能准确识别退化区域，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.02464)