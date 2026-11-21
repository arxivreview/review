# CVPR2026最新论文 ｜D$^2$-FOSA: Dual-Diffusion Guided EEG-to-Image Reconstruction with Frequency-Oriented Semantic Alignment ｜频率导向双扩散框架

研究机构：北京航空航天大学

作者：Chenglong Yu、Shuai Shen、Xiangsheng Li 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_72f05670fcde)

> 脑电视觉解码旨在从低信噪比信号中还原感知内容，核心瓶颈在于传统编码器忽略频率特异性神经动力学，且对比学习难以弥合模态鸿沟。现有方法多依赖通用时空特征提取，缺乏对Beta/Gamma等关键频带的针对性增强，导致语义对齐精度受限。D2-FOSA通过频率导向Mamba编码器提取判别性特征，并引入双向扩散潜变量生成器强制生成一致性，实现从检索到高保真重建的闭环。该框架在200-way检索任务上超越同期基线，但跨被试泛化能力仍受限于缺乏大规模预训练，其性能优势是否源于特定频带假设尚存疑。

## 研究背景

脑电（EEG）信号的信噪比极低，且空间分辨率粗糙，直接提取细粒度语义信息面临巨大挑战。传统线性模型或通用卷积网络难以捕捉大脑处理视觉信息时的频率特异性动态，如Beta（13-30 Hz）和Gamma（30-60 Hz）节律，这些节律与高级视觉概念编码密切相关。同时，EEG表征与CLIP等高维视觉语义空间之间存在显著的模态鸿沟，简单的对比损失往往导致对齐不稳定，生成式重建时出现语义幻觉或细节缺失。

自2022年THINGS-EEG数据集确立零样本检索基准以来，领域主流路线从分类驱动转向对齐驱动。BraVL等早期工作证明了自监督对比学习的可行性，但受限于编码器对噪声的鲁棒性不足，跨被试性能大幅下降。MB2C等方法尝试引入生成式组件，但单向生成机制难以保证潜空间的双向一致性。D2-FOSA的切入点在于：一方面通过频率感知的状态空间模型强化EEG特征提取，另一方面通过双向扩散约束替代或辅助对比学习，以解决对齐不紧和生成保真度低的双重问题。

## 核心方法

### 方法参照系

标准EEG视觉解码流程通常包含：EEG编码器提取时空特征，通过投影头映射至共享潜空间，利用InfoNCE损失与冻结的CLIP图像嵌入进行对比对齐。本文的关键差异在于：编码器从通用CNN/Transformer替换为频率导向Mamba，对齐机制从单一对比损失扩展为“对比+双向扩散”的复合目标，旨在同时优化判别性与生成性。

### 频率导向Mamba编码器

传统状态空间模型（SSM）的状态矩阵$A$通常为对角矩阵，难以捕捉EEG信号的耦合振荡特性。D2-FOSA提出FOMamba，将$A$结构化为块对角矩阵，每个$2 \times 2$子块显式建模衰减振荡模式：

$$
A_k = \begin{bmatrix} -\rho_k & -\omega_k \\ \omega_k & -\rho_k \end{bmatrix}
$$

其中$\rho_k > 0$为阻尼因子，$\omega_k > 0$为角频率，对应复共轭特征对$\lambda_k = -\rho_k \pm j\omega_k$。通过引入可学习的对数频率偏置$F_{log,k}$，模型动态调整振荡频率$\tilde{\omega}_k = \text{softplus}(\omega_k + F_{log,k})$，从而选择性放大Beta和Gamma频带的信号功率。这一设计解决了通用Mamba在高频段抑制过度、导致视觉相关特征丢失的问题，使提取的EEG嵌入更具判别力。

### 双向扩散潜变量生成器

仅靠对比学习难以保证潜空间的细粒度结构对齐。D2-FOSA引入双向扩散潜变量生成器（DDLG），包含EEG-to-Image（E2I）和Image-to-EEG（I2E）两个对称模块。E2I模块以EEG嵌入$X_e$为条件，从噪声中重构图像嵌入$X_i$，其损失函数为：

$$
\mathcal{L}_{E2I} = \mathbb{E}_{z_0 \sim X_i, \epsilon \sim \mathcal{N}(0, I), t \sim U[1, T]} \left[ \| \epsilon - \epsilon_\theta(\sqrt{\bar{\alpha}_t} z_0 + \sqrt{1 - \bar{\alpha}_t} \epsilon, X_e, t) \|^2 \right]
$$

I2E模块执行反向重构。总损失为$\mathcal{L}_{total} = \mathcal{L}_{align} + \lambda_{E2I}\mathcal{L}_{E2I} + \lambda_{I2E}\mathcal{L}_{I2E}$，其中$\lambda$设为0.5。这种双向生成一致性约束作为强正则化器，迫使EEG和图像嵌入在潜空间中形成双射关系，不仅提升了检索精度，还为后续基于SDXL的高保真图像重建提供了结构稳定的条件输入。

## 实验评估

实验在THINGS-EEG、THINGS-MEG、EEGCVPR40和EEGImageNet四个数据集上进行，涵盖受试者内（Intra-subject）和受试者间（Inter-subject）两种协议。基线覆盖BraVL、NICE系列、ATM、MB2C及2025年的VE-SDN和UBP，但未包含LaBraM、NeuroBridge等2025-2026年基于大规模预训练的最新SOTA方法。

| 数据集 | 协议 | 方法 | Top-1 (%) | Top-5 (%) |
| :--- | :--- | :--- | :--- | :--- |
| THINGS-EEG | Intra-subject | MB2C | 28.5 | 60.4 |
| THINGS-EEG | Intra-subject | VE-SDN | 37.2 | 69.9 |
| THINGS-EEG | Intra-subject | D2-FOSA | 38.0 | 70.7 |
| THINGS-EEG | Inter-subject | MB2C | 11.9 | 32.0 |
| THINGS-EEG | Inter-subject | UBP | 12.4 | 33.4 |
| THINGS-EEG | Inter-subject | D2-FOSA | 13.1 | 34.6 |

在THINGS-EEG受试者内200-way检索任务中，D2-FOSA以38.0%的Top-1准确率超越MB2C（28.5%）和VE-SDN（37.2%）。受试者间协议下，D2-FOSA（13.1%）略优于UBP（12.4%），但绝对值较低，显示跨被试泛化仍是瓶颈。在图像重建任务中，D2-FOSA的FID为146.33，优于MB2C的163.94，表明双向扩散约束确实提升了生成保真度。

消融实验显示，FOMamba相比标准Mamba将Top-1准确率从27.75%提升至31.18%，验证了频率感知机制的有效性。DDLG的双向约束（✓）相比单向（†）进一步提升至37.96%，说明生成一致性对潜空间对齐至关重要。然而，在THINGS-MEG受试者间任务中，D2-FOSA（3.2%）仅略高于UBP（2.2%），提升幅度有限，暗示频率导向假设在MEG信号上的普适性可能弱于EEG。

评估指标涵盖检索准确率（Top-1/5）和重建质量（FID, KID, SSIM, PCC）。局限在于：未报告置信区间，且200-way检索与全库零样本检索协议不同，导致与领域综述中Aligning What EEG Can See（84.6%）等全库SOTA无法直接比较。代码在补充材料中提供，但未公开独立仓库，超参数细节（如$\rho$的范围[0.5, 0.995]）需查阅补充材料。

## 关联研究分析

从问题动机看，D2-FOSA与MB2C同属生成式重建路线，但MB2C依赖单向生成，而D2-FOSA引入双向扩散。这一差异的根源在于对“对齐”定义的不同：MB2C视生成为解码后的独立步骤，D2-FOSA视生成为训练阶段的正则化手段。D2-FOSA的双向约束在THINGS-EEG上带来约17 FID的改善，但在THINGS-MEG上增益微弱，这可能源于MEG信号的空间分辨率更高，频率特异性动态与EEG存在差异，导致FOMamba的频率假设在MEG上失效。

从方法设计看，D2-FOSA与BraVL共享CLIP对齐框架，但BraVL使用通用CNN/Transformer编码器，D2-FOSA使用FOMamba。BraVL在受试者间任务中表现较差（1.8%），D2-FOSA（13.1%）虽有提升，但仍远低于基于大规模预训练的LaBraM或NeuroBridge。这表明，仅靠架构改进（频率感知）难以弥补数据规模不足带来的泛化差距。D2-FOSA未采用多被试预训练，而是依赖单任务内的频率特征优化，这种“任务内优化”策略在数据充足时有效，但在跨被试场景下，其性能上限可能受限于缺乏跨个体神经动力学的共享表征。

## 总结

D2-FOSA旨在解决EEG解码中频率动态提取不足与模态对齐不紧的矛盾。其切入点在于利用FOMamba显式建模Beta/Gamma振荡，并通过双向扩散强制潜空间一致性，从而在200-way检索和图像重建任务上超越MB2C等基线。实验证明，频率导向编码将Top-1准确率从27.75%提升至31.18%，双向扩散进一步将其推至37.96%。然而，论文自身实验暴露了边界：在受试者间协议下，性能仅13.1%，且THINGS-MEG上的增益有限，表明频率假设的普适性和跨被试泛化能力仍是短板。当支持集从单被试扩展到多被试时，FOMamba的频率参数是否需进行个体化适配，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_72f05670fcde)