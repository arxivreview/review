# CVPR2026最新论文 ｜GDPO-SR: Group Direct Preference Optimization for One-Step Generative Image Super-Resolution ｜组直接偏好优化一步超分

研究机构：香港理工大学

作者：Qiaosi Yi、Shuai Li、Rongyuan Wu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.16769)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.16769)

> 真实世界图像超分辨率（Real-ISR）面临一步扩散模型生成能力受限与多步模型推理低效的双重困境，现有强化学习（RL）算法因缺乏样本多样性或忽略局部细节而难以直接应用。本文切入点在于通过噪声注入打破一步模型的确定性映射，并设计融合直接偏好优化（DPO）与组相对策略优化（GRPO）优势的GDPO框架，实现在线偏好对齐。该方法在保持单步推理效率的同时，显著提升了重建图像的保真度与感知质量，但其对预训练T2I骨干的依赖及在极端退化下的泛化边界仍需进一步审视。

## 研究背景

一步扩散超分模型通过蒸馏技术将多步去噪压缩为单次前向传播，解决了实时部署需求，但牺牲了生成多样性，导致纹理细节模糊。直接偏好优化（DPO）旨在通过离线正负样本对优化模型偏好，但其静态数据限制了样本多样性；组相对策略优化（GRPO）虽支持在线采样，却仅计算全局图像似然，忽略局部纹理细节。这两种RL算法均无法直接应用于确定性的一步超分模型，因为策略模型需具备对同一输入生成多样输出的能力。

Real-ISR的核心挑战在于平衡保真度与真实感，多步模型虽能生成逼真纹理但推理耗时且易产生幻觉，一步模型虽快但细节不足。现有RL方法如DP2O-SR仅适用于多步模型，且DPO的离线配对与GRPO的全局似然计算均存在缺陷。本文提出GDPO，通过噪声感知一步扩散模型（NAOSD）引入可控随机性，并设计属性感知奖励函数（ARF）与组相对优势计算，实现一步模型的高效偏好优化。

## 核心方法

### 方法参照系

标准一步扩散超分流程将低分辨率（LR）图像直接映射为高分辨率（HR）图像，缺乏随机性。本文问题与该通用流程的关键差异在于：需在不增加推理步数的前提下，引入可控噪声以支持RL优化，同时保持保真度。

### 噪声感知一步扩散模型

NAOSD在潜空间注入可控高斯噪声，打破确定性映射。设计动机在于解决一步模型无法生成多样样本导致RL算法失效的问题。给定LR图像 $I_{LR}$，经VAE编码器得到潜变量 $z_{LR}$，注入噪声 $\epsilon$ 得到扰动潜变量 $\tilde{z}$：

$$ \tilde{z} = \sqrt{\alpha_{t_{add}}} z_{LR} + \sqrt{\beta_{t_{add}}} \epsilon $$

其中 $t_{add}$ 控制噪声强度。随后，UNet在时间步 $t_{diff}$ 执行去噪，恢复潜变量 $z_{SR}$：

$$ z_{SR} = \sqrt{\alpha_{t_{diff}}} \tilde{z} + \sqrt{\beta_{t_{diff}}} \epsilon_{pred} $$

采用不等时间步策略（$t_{add} > t_{diff}$），扩大采样空间的同时稳定保真度，避免噪声注入导致的性能退化。

### 组直接偏好优化

GDPO融合DPO的精确性与GRPO的在线效率。设计动机在于解决DPO离线数据多样性不足与GRPO忽略局部细节的问题。首先，通过ARF计算每个样本的奖励 $R_i$，动态平衡保真度（FR）与感知（NR）指标：

$$ R_i = \rho_s \cdot R_{FR}(I_i) + \rho_d \cdot R_{NR}(I_i) $$

其中 $\rho_s, \rho_d$ 为自适应权重。其次，计算组相对优势 $A_i$：

$$ A_i = \frac{R_i - \mu_R}{\sigma_R} $$

最后，最小化GDPO损失，引导策略模型偏好高奖励样本：

$$ \mathcal{L}_{GDPO} = -\mathbb{E} \left[ \log \sigma \left( \omega \left( \log \frac{\pi_\theta(x_i|x_{LR})}{\pi_{ref}(x_i|x_{LR})} - \log \frac{\pi_{ref}(x_i|x_{LR})}{\pi_{old}(x_i|x_{LR})} \right) \cdot A_i \right) \right] $$

该损失函数利用组内相对优势，优先优化高奖励样本，同时抑制低质量输出。

## 实验评估

实验在RealSR、DRealSR和DIV2K-val数据集上进行，对比StableSR、OSEDiff、InvSR等基线。GDPO-SR在RealSR上PSNR达25.48 dB，MUSIQ达69.42，优于基线NAOSD（25.25 dB, 69.06）及OSEDiff（25.21 dB, 68.75）。

| 数据集 | 方法 | PSNR (dB) | MUSIQ | LPIPS |
|---|---|---|---|---|
| RealSR | NAOSD | 25.25 | 69.06 | 0.2689 |
| RealSR | GDPO-SR | 25.48 | 69.42 | 0.2675 |
| DRealSR | GDPO-SR | 28.18 | 65.63 | 0.2851 |

消融实验显示，ARF中自适应权重（AW）移除后，MUSIQ从69.42降至68.42，PSNR从25.48降至25.10，验证了动态平衡FR与NR指标的必要性。组大小 $G=6$ 时性能最优，$G=8$ 时PSNR略降（25.34），表明样本多样性存在边际收益递减。

评估指标涵盖FR（PSNR, SSIM, LPIPS, FID, DISTS）与NR（MUSIQ, MANIQA, CLIPIQA, AFINE），但未报告置信区间。代码开源，超参数（LoRA rank=4, $t_{add}=250, t_{diff}=100$）明确，可复现性良好。

## 关联研究分析

从问题动机看，GDPO-SR与DP2O-SR均利用RL优化超分，但DP2O-SR针对多步模型，依赖离线DPO配对，导致样本多样性受限；GDPO-SR通过NAOSD引入在线噪声采样，解决了一步模型的随机性缺失。差异根源在于任务特性：一步模型需额外机制打破确定性，而多步模型天然具备随机性。

从方法设计看，GDPO-SR与DanceGRPO同属RL框架，但DanceGRPO计算全局图像似然，忽略局部纹理；GDPO-SR引入ARF，通过Sobel梯度与Shannon熵区分平滑与纹理区域，动态调整奖励权重。这一设计源于Real-ISR对局部细节的高要求，全局似然无法捕捉纹理区域的细微差异。

## 总结

GDPO-SR解决了一步扩散超分模型生成能力受限与RL算法适用性不足的矛盾，通过NAOSD引入可控噪声，并设计GDPO框架实现在线偏好优化。实验证明，GDPO-SR在RealSR上PSNR提升0.23 dB，MUSIQ提升0.36，且推理时间保持0.11秒，验证了RL对一步模型的有效增强。然而，其性能仍低于多步SOTA（如Bridging Fidelity-Reality的28.24 dB PSNR），且依赖预训练T2I骨干，在极端退化下的泛化能力未充分验证。当噪声强度 $t_{add}$ 进一步增大时，保真度与生成多样性的平衡是否仍能维持，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.16769)