# ICLR2026最新论文 ｜KERNELFUSION: ZERO-SHOT BLIND SUPER-RESOLUTION VIA PATCH DIFFUSION ｜零样本盲超分辨率：基于补丁扩散的任意核联合估计

研究机构：以色列魏茨曼科学研究所、以色列理工学院

作者：Oliver Heinimann、Tal Zimbalist、Assaf Shocher 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_85998319)

> 盲超分辨率旨在退化参数未知的情况下恢复图像，其核心挑战在于真实世界退化与合成训练数据之间的域差距。现有方法依赖预定义的合成退化分布，导致在复杂非高斯核下性能甚至劣于双三次插值。KernelFusion 通过单图内部训练补丁扩散模型，同时估计任意复杂核与高分辨率图像，消除了“分布外”概念。该方法在分布外数据上确立了可行性，但单图训练的高计算成本与全局核假设限制了其实际部署潜力。

## 研究背景

超分辨率（Super-Resolution, SR）通常假设低分辨率（Low-Resolution, LR）图像由已知的高斯核下采样得到，但真实成像中核具有图像特异性，受传感器光学、相机运动及手部抖动影响。这种核的不确定性导致传统方法在真实场景失效，而核估计的精度往往比图像先验或算法选择更关键。盲超分辨率（Blind SR）试图解决这一问题，但现有方法要么显式估计核，要么隐式表征退化，均受限于训练分布中的简单低通滤波器（如各向异性高斯核）。

主流盲超分路线分为三类：基于合成退化训练的方法（如 Real-ESRGAN）、基于潜在核表征的方法（如 DAN）以及显式核估计方法（如 KernelGAN）。前两类方法在分布外核下泛化能力不足，后两类方法虽能估计核，但通常仅支持高斯或运动模糊，且核估计与图像恢复分离，导致误差累积。KernelFusion 的切入点在于打破外部训练分布的束缚，利用单张 LR 图像的内部统计特性，通过零样本方式同时恢复核与高分辨率（High-Resolution, HR）图像，从而处理任意复杂下采样核。

## 核心方法

### 方法参照系

盲超分标准流程通常包含核估计与图像恢复两个独立阶段，或依赖预训练的大规模退化分布。本文的关键差异在于将核估计与图像恢复统一在反向扩散过程中，且完全依赖单图内部先验，无需外部训练数据或预训练模型。

### 补丁扩散模型训练

设计动机在于克服预训练模型在分布外核下的失效，通过内部训练捕捉图像特有的补丁统计。Phase 1 训练一个基于去噪概率扩散模型（Denoising Diffusion Probabilistic Model, DDPM）的补丁扩散（Patch-Diffusion, PD）模型，仅针对单张 LR 图像 $I_{LR}$ 进行去噪训练。模型预测速度 $v$，其损失函数为：

$$ \Psi = \arg\min_{\psi} \mathbb{E}_{t, \epsilon} \| PD_{\psi}(x_t) - v_t \|^2 $$

其中 $x_t = \sqrt{\bar{\alpha}_t} x_0 + \sqrt{1-\bar{\alpha}_t}\epsilon$，$v_t = \sqrt{\bar{\alpha}_t}\epsilon - \sqrt{1-\bar{\alpha}_t}x_0$。该公式表明模型学习从含噪图像到干净图像的速度场，从而隐式学习 LR 图像的补丁分布。PD 采用无全局注意力层的纯卷积网络，理论感受野限制在 15×15 像素，确保其仅捕获局部补丁统计而非全局结构。

### 联合核估计与图像恢复

设计动机在于解决核估计与图像恢复分离导致的误差累积，通过一致性约束实现联合优化。Phase 2 在反向扩散过程中，同时优化 HR 图像猜测 $\hat{x}_0$ 和核估计。核估计采用隐式神经表示（Implicit Neural Representation, INR）架构，以克服 CNN/MLP 的平滑偏置，恢复非平滑复杂核。优化目标包含一致性损失，确保估计的 HR 图像经估计核下采样后能重建原始 LR 图像：

$$ \mathcal{L}_{cons} = \| \hat{x}_0 \downarrow_s - I_{LR} \|^2 $$

其中 $\downarrow_s$ 表示使用 INR 估计的核进行下采样。该公式强制核与图像估计在物理退化过程上保持一致。PD 模型作为去噪器，将 HR 猜测向 LR 图像的补丁分布对齐，而 U-Net 则提供全局结构先验，补偿 PD 因小感受野导致的全局结构丢失。这种联合机制使得核估计与图像恢复相互促进，形成闭环优化。

## 实验评估

实验在 DIV2KRK（高斯核）、DIV2KFK（复杂非高斯核）和 Blind144（极端核）三个数据集上进行，基线覆盖 SwinIR、Real-ESRGAN、DPSR 等主流盲超分方法。在分布外数据集 DIV2KFK 和 Blind144 上，KernelFusion 显著优于所有对比方法，甚至超过使用真实核的双三次插值。

| 方法 | Blind144 PSNR (dB) | Blind144 SSIM | DIV2KFK PSNR (dB) | DIV2KFK SSIM | DIV2KRK PSNR (dB) | DIV2KRK SSIM |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Bicubic | 24.865 | 0.637 | 24.101 | 0.639 | 25.075 | 0.671 |
| DPSR | 24.824 | 0.637 | 23.977 | 0.637 | 25.317 | 0.682 |
| DCLS-SR | 24.808 | 0.633 | 23.886 | 0.634 | 25.431 | 0.668 |
| Real-ESRGAN | 24.323 | 0.678 | 23.003 | 0.617 | 25.895 | 0.703 |
| KernelFusion | 27.191 | 0.719 | 26.426 | 0.720 | 26.761 | 0.715 |

在 Blind144 上，KernelFusion 的 PSNR 达到 27.191 dB，比 Bicubic 高 2.326 dB，比 DPSR 高 2.367 dB，验证了其在复杂核下的鲁棒性。在 DIV2KRK（高斯核，分布内）上，KernelFusion 的 PSNR 为 26.761 dB，略低于 Real-ESRGAN 的 25.895 dB（注：此处原文数据可能有误，Real-ESRGAN 在 DIV2KRK 上通常更高，但根据表格数据，KernelFusion 26.761 > Real-ESRGAN 25.895，显示其在分布内也具有竞争力）。

消融实验表明，仅使用 U-Net 和 INR（无 PD）时，PSNR 为 25.804 dB；加入 PD 后，PSNR 降至 25.481 dB，这是因为 PD 的小感受野破坏了全局结构；最终 KernelFusion（双 U-Net + PD）达到 27.191 dB，证明 PD 提供的补丁分布约束与 U-Net 的全局结构先验互补。

评估主要依赖 PSNR 和 SSIM，未报告 LPIPS 或 FID 等感知指标，这与领域共识中“感知质量更重要”的观点存在偏差。此外，单图 PD 训练耗时约 20 分钟（L40S GPU），限制了实时应用。代码未公开，超参数细节有限，可复现性需进一步验证。

## 关联研究分析

从问题动机看，KernelFusion 与 KernelGAN（Bell-Kligler et al., 2019）均基于跨尺度补丁相似性原理，但 KernelGAN 仅估计核，需依赖外部 SR 算法，而 KernelFusion 联合估计核与图像，消除了误差累积。这一差异源于 KernelFusion 将核估计嵌入反向扩散过程，利用扩散模型的生成能力同时解决两个子问题。KernelGAN 的局限在于其 GAN 架构对复杂非高斯核的表达能力不足，而 KernelFusion 的 INR 架构能恢复非平滑核，这是任务特性决定的，而非论文未探索的盲区。

从方法设计看，KernelFusion 与 DIP（Ulyanov et al., 2018）同属深度图像先验，但 DIP 仅优化图像，不估计核，而 KernelFusion 引入 INR 和一致性损失，实现了盲超分。与 Real-ESRGAN 等基于合成退化训练的方法相比，KernelFusion 不依赖外部数据，这使其在分布外场景下具有优势，但在分布内场景下，Real-ESRGAN 利用大规模预训练先验，可能在感知质量上更具优势。KernelFusion 未报告感知指标，其感知质量是否优于 Real-ESRGAN 尚不明确。

## 总结

KernelFusion 解决了盲超分中复杂非高斯核下性能劣于插值的矛盾，通过单图内部训练补丁扩散模型，联合估计任意核与 HR 图像，消除了外部训练分布的束缚。在 Blind144 上，其 PSNR 达到 27.191 dB，显著优于 Bicubic 和 DPSR，证明了零样本范式在分布外数据上的可行性。然而，该方法假设核为全局均匀，无法处理空间变异模糊，且单图训练耗时约 20 分钟，限制了实际部署。当支持集增大或引入外部预训练先验时，单图 PD 的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_85998319)