# CVPR2026最新论文 ｜ZeroIDIR: Zero-Reference Illumination Degradation Image Restoration with Perturbed Consistency Diffusion Models ｜零参考光照退化图像恢复

研究机构：四川大学、电子科技大学

作者：Hai Jiang、Zhen Liu、Yinjie Lei 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.11435)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.11435)

> 光照退化图像恢复（IDIR）旨在从低光照、逆光或过曝图像中重建正常光照图像，核心难点在于缺乏配对监督数据时的泛化能力。现有监督方法依赖大规模配对数据导致过拟合，无监督方法则受限于退化类型假设或分布不匹配。本文切入点是将恢复过程解耦为自适应光照校正与扩散重建，通过零参考训练消除对配对数据的依赖。该方法在LOL数据集上以20.874 dB的PSNR超越无监督SOTA，但距离监督SOTA仍有4.306 dB差距，其零参考范式在极端光照场景下的鲁棒性存疑。

## 研究背景

光照退化图像恢复（IDIR）面临的核心困境是病态性：同一退化图像对应多种可能的正常光照解，传统手工先验（如直方图均衡化、Retinex理论）难以适应多样光照条件。深度学习虽提升了鲁棒性，但监督方法依赖配对数据导致过拟合，无监督方法则受限于零样本设定的退化类型假设或非配对数据的分布不匹配，在真实场景中产生曝光错误、细节模糊或噪声放大。扩散模型虽能提升感知质量，但其低频生成偏差（特别是曝光方面）使得联合处理光照校正与细节重建变得困难。

IDIR领域的主流路线分为监督与无监督两类。监督方法如UHDFour、Reti-Diff依赖大规模配对数据，虽性能优异但泛化能力有限；无监督方法如Zero-DCE、LightenDiff通过对抗学习或非配对对齐避免配对依赖，但前者假设退化类型固定，后者受限于非配对数据的分布差距。本文的切入点在于解耦恢复过程：先通过自适应伽马校正模块（AGCM）处理低频曝光问题，再利用扰动一致性扩散模型（PCDM）重建高频细节，从而在零参考设定下同时解决曝光校正与细节恢复的矛盾。

## 核心方法

### 方法参照系

标准扩散模型图像恢复流程以退化图像为条件，通过前向加噪与反向去噪学习从退化到清洁图像的映射。本文的关键差异在于：不直接使用退化图像作为条件，而是先通过AGCM生成光照校正后的中间态，将其视为扩散轨迹中的部分噪声状态，从而将低频校正与高频重建解耦。

### 自适应伽马校正模块（AGCM）

AGCM的设计动机是解决扩散模型在低频曝光生成上的偏差。标准流程中，扩散模型需同时处理曝光校正与细节重建，导致曝光不稳定。AGCM通过Retinex分解将图像分离为反射率图$\mathbf{R}_d$与光照图$\mathbf{L}_d$，仅对光照图进行空间自适应校正，避免噪声放大。具体地，$\mathbf{L}_d$与$\mathbf{R}_d$拼接后通过卷积块生成结构特征$\mathbf{F}_s$，$\mathbf{L}_d$作为全局曝光先验与$\mathbf{F}_s$融合，预测空间变化的伽马映射$\{\gamma_u, \gamma_o\}$与权重映射$\{W_u, W_o\}$，分别处理欠曝与过曝区域。校正后的光照图$\mathbf{L}'_d$与反射率图相乘得到中间态$I_d'$：

$$I_d' = \mathbf{L}'_d \odot \mathbf{R}_d$$

该公式表明，AGCM通过解耦光照与内容，确保校正过程仅调整曝光而不改变结构信息。为约束校正后的光照分布接近自然场景，引入直方图引导损失$\mathcal{L}_{hic}$，将$I_d'$的光照直方图与从约20k张正常光照图像聚合的经验先验分布$\mathbf{H}_{prior}$对齐，避免全局伽马校正的僵化性。

### 扰动一致性扩散模型（PCDM）

PCDM的设计动机是解决零参考设定下缺乏清洁目标图像的问题。标准扩散训练需清洁图像$\mathbf{x}_0$，但本文仅有中间态$I_d'$。PCDM将$I_d'$视为扩散轨迹中时间步$t^*$的状态$\mathbf{x}_{t^*}$，通过继续前向加噪$\Delta_t$步生成训练样本$\mathbf{x}_t$：

$$\mathbf{x}_t = \sqrt{\bar{\alpha}_t \bar{\alpha}_{t^*}} \mathbf{x}_{t^*} + \sqrt{1 - \bar{\alpha}_t \bar{\alpha}_{t^*}} \boldsymbol{\epsilon}_t$$

该公式表明，$I_d'$被嵌入扩散轨迹的中间位置，模型学习从该状态去噪至清洁图像。为约束生成图像$\hat{\mathbf{x}}_0$的前向扩散轨迹与中间态$\mathbf{x}_{t^*}$一致，提出扰动扩散一致性损失$\mathcal{L}_{pdc}$：

$$\mathcal{L}_{pdc} = \|\phi(\mathbf{x}_{t^*}) - \phi(\hat{\mathbf{x}}_{t^*})\|_2^2$$

其中$\phi(\cdot)$为预训练VGG-16特征提取器，$\hat{\mathbf{x}}_{t^*}$为$\hat{\mathbf{x}}_0$前向加噪$t^*$步的结果。该损失确保生成图像在特征空间与中间态保持轨迹一致性，避免扩散过程中的漂移，从而提升细节重建的保真度与稳定性。

## 实验评估

实验在LOL、LSRW、MIT5K（低光照）、BAID、Backlit300（逆光）、MSEC、SICE（多曝光）数据集上进行，基线覆盖监督（UHDFour、Reti-Diff）与无监督（Zero-DCE、LightenDiff）方法，但缺失AiOIR类多任务基线（因任务不同）。

| 数据集 | 方法 | PSNR (dB) | SSIM | LPIPS |
| :--- | :--- | :--- | :--- | :--- |
| LOL | ZeroIDIR | 20.874 | 0.811 | 0.167 |
| LOL | LightenDiff | 20.190 | 0.809 | 0.182 |
| LOL | Reti-Diff | 25.180 | 0.869 | 0.094 |
| SICE-over | ZeroIDIR | 16.975 | 0.661 | 0.259 |
| SICE-over | LightenDiff | 15.514 | 0.603 | 0.280 |
| SICE-over | Reti-Diff | 16.840 | 0.638 | 0.288 |

ZeroIDIR在LOL上PSNR 20.874 dB，较无监督SOTA LightenDiff高0.684 dB，但较监督SOTA Reti-Diff低4.306 dB；在SICE-over上PSNR 16.975 dB，较LightenDiff高1.461 dB，与Reti-Diff（16.840 dB）相当。

消融实验验证了AGCM与PCDM的关键作用。移除Retinex分解导致噪声放大与颜色失真（LOL PSNR从19.599降至18.378）；移除$\mathcal{L}_{hic}$导致亮度校正不稳定（LOL PSNR从19.599降至18.406）。PCDM消融中，使用原始退化图像$I_d$作为条件而非$I_d'$导致曝光偏差（LOL PSNR从20.874降至17.571）；移除$\mathcal{L}_{pdc}$导致轨迹漂移与伪影（LOL PSNR从20.874降至19.780）。

评估边界：指标覆盖PSNR/SSIM/LPIPS（配对）与NIQE/CLIPIQA（非配对），但缺乏计算效率维度；代码开源（https://github.com/JianghaiSCU/ZeroIDIR），超参数（$\lambda_1=0.5, \lambda_2=0.1, \lambda_3=1.0, \lambda_g=20.0$）与训练细节（A100 GPU，两阶段训练）完整披露，可复现性良好。

## 关联研究分析

从问题动机看，ZeroIDIR与LightenDiff同属无监督扩散恢复，但LightenDiff依赖非配对数据对齐，受限于分布不匹配；ZeroIDIR通过零参考训练完全消除参考图像依赖，其AGCM模块显式处理低频曝光，而LightenDiff将曝光校正与细节重建耦合在扩散过程中，导致曝光不稳定。这一差异源于任务特性：光照退化的低频偏差需前置处理，而非在扩散过程中隐式学习。

从方法设计看，ZeroIDIR与Reti-Diff同用扩散模型，但Reti-Diff依赖配对数据，其条件为退化图像；ZeroIDIR以AGCM校正后的中间态为条件，解耦了低频与高频处理。Reti-Diff在LOL上PSNR 25.180 dB，较ZeroIDIR高4.306 dB，这一差距是否主要源于配对监督提供的精确目标，而非架构缺陷，论文未给出消融验证。此外，ZeroIDIR未使用CLIP/MLLM等视觉基础模型，仅用VGG-16特征，与领域共识中“视觉基础模型辅助退化识别”的路径存在差异，其零参考范式是否足以替代TTA应对极端未知光照场景，论文未提供对比实验。

## 总结

ZeroIDIR要解决的核心矛盾是零参考设定下光照校正与细节重建的耦合失效。现有监督方法依赖配对数据导致过拟合，无监督方法受限于退化假设或分布不匹配，而扩散模型的低频偏差加剧了这一矛盾。本文抓住的切入点是解耦恢复过程：AGCM通过空间自适应伽马校正处理低频曝光，PCDM通过扰动一致性扩散重建高频细节，从而在零参考训练下消除对配对数据的依赖。实验证明，该方法在LOL上PSNR 20.874 dB，超越无监督SOTA LightenDiff 0.684 dB，与监督SOTA Reti-Diff差距缩小至4.306 dB。本文的边界在于：AGCM的Retinex分解假设光照与反射率可分离，在极端逆光或混合退化场景下可能失效；PCDM的$t^*$范围[0,50]固定，未自适应调整。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.11435)