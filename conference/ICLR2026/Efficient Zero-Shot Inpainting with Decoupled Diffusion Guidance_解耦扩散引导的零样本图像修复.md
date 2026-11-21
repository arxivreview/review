# ICLR2026最新论文 ｜Efficient Zero-Shot Inpainting with Decoupled Diffusion Guidance ｜解耦扩散引导的零样本图像修复

研究机构：瑞典皇家理工学院

作者：Badr Moufad、Navid Bagheri Shouraki、Alain Oliviero Durmus 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.18365)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.18365)

> 零样本图像修复旨在利用预训练扩散模型作为先验，在不微调的情况下恢复缺失区域，但主流方法依赖向量-雅可比积（VJP）计算导致推理内存与延迟激增。本文通过解耦似然近似，将后验转移转化为闭式高斯混合分布，彻底消除对去噪器梯度的依赖。该方法在低步数预算下实现了比微调模型更优的保真度与感知质量平衡，但其在极端复杂语义场景下的结构稳定性仍存疑。

## 研究背景

图像修复任务要求生成内容既符合自然图像分布，又严格匹配观测像素。在贝叶斯框架下，这被建模为从后验分布 $\pi_0(\cdot|\mathbf{y})$ 中采样，其中先验由预训练扩散模型提供，似然项约束观测一致性。直接采样后验分布不可行，需通过引导项修改去噪过程。

现有零样本方法（如DDNM, DIFFPIR）采用“扭曲函数”近似似然，即在去噪器输出处评估观测概率。这一操作要求对去噪器网络进行反向传播以计算VJP，导致内存占用高达22GB以上且推理速度缓慢。相比之下，微调式条件扩散模型虽推理高效，但需针对特定任务重新训练，丧失了零样本方法的通用性。DING的切入点在于打破似然评估与去噪器输入之间的依赖关系，通过引入独立采样点实现无梯度的高效后验采样。

## 核心方法

### 贝叶斯后验采样参照系

标准零样本修复基于DDIM反向过程，通过近似后验去噪器 $\hat{\mathbf{x}}_0(\mathbf{x}_t, t|\mathbf{y})$ 引导采样。其核心恒等式涉及先验去噪器与引导项 $\nabla \log \ell_t(\mathbf{y}|\mathbf{x}_t)$ 的耦合。该框架的关键差异在于，本文不直接计算该梯度，而是重构似然近似形式以规避反向传播。

### 解耦似然近似与闭式采样

传统方法在 $\mathbf{x}_s$ 处评估去噪器以近似似然，导致计算图依赖 $\mathbf{x}_s$。DING引入独立随机变量 $\mathbf{z}_s \sim p_{\theta, s|t}(\cdot|\mathbf{x}_t)$ 作为代理，在 $\mathbf{z}_s$ 处评估噪声预测。这一解耦使得似然近似不再依赖当前状态 $\mathbf{x}_s$ 的梯度。

$$
\hat{\ell}_{\theta, s}(\mathbf{y}|\mathbf{x}_s) \approx \mathcal{N}(\mathbf{y}; \alpha_s \hat{\mathbf{x}}_{\theta, 0}(\mathbf{z}_s, s), \sigma_s^2 I)
$$

该公式表明，观测似然由独立采样点 $\mathbf{z}_s$ 的去噪结果决定，切断了 $\mathbf{x}_s$ 与去噪器之间的微分路径。基于此，后验转移 $\hat{\pi}_{\theta, s|t}(\mathbf{x}_s|\mathbf{x}_t, \mathbf{y})$ 呈现混合结构，对于修复任务，其条件分布具有闭式高斯解：

$$
\hat{\pi}_{\theta, s|t}(\mathbf{x}_s|\mathbf{z}_s, \mathbf{x}_t, \mathbf{y}) = \mathcal{N}(\mathbf{x}_s; \boldsymbol{\mu}_{s|t}, \Sigma_{s|t})
$$

其中均值 $\boldsymbol{\mu}_{s|t}$ 由DDIM均值与观测 $\mathbf{y}$ 加权合成，权重 $\gamma_{s|t} = \eta_s^2 / (\eta_s^2 + \alpha_s^2 \sigma_{\mathbf{y}}^2)$ 控制观测保真度。这一设计使得掩码区域与未掩码区域可独立采样，无需VJP，将推理内存降至22.09GB，时间缩短至2.9秒。

## 实验评估

实验在FFHQ、DIV2K及PIE-Bench上进行，对比DDNM、FLOWCHEF等10种零样本方法及微调基线SD3 Inpaint。基线覆盖了主流引导策略，但缺乏针对大掩码结构一致性的专项评估。

| 方法 | FID | pFID | LPIPS | cPSNR |
|---|---|---|---|---|
| DDNM | 12.3 | 25.1 | 0.38 | 31.54 |
| FLOWCHEF | 20.2 | 30.50 | 0.36 | 31.61 |
| DING | 9.6 | 6.6 | 0.33 | 31.03 |

在FFHQ上，DING的FID 9.6显著优于DDNM的12.3和FLOWCHEF的20.2，pFID从25.1降至6.6，表明感知质量大幅提升。然而，cPSNR 31.03略低于DDNM的31.54，显示解耦近似在严格保真度上存在轻微妥协。

| 方法 | FID | pFID | LPIPS | CLIP |
|---|---|---|---|---|
| SD3 Inpaint (56) | 68.2 | 30.3 | 0.34 | 26.38 |
| DING (56) | 63.6 | 24.6 | 0.30 | 26.63 |

在PIE-Bench上，DING以FID 63.6和pFID 24.6超越微调模型SD3 Inpaint（FID 68.2, pFID 30.3），验证了零样本方法在同等运行时预算下的优越性。消融实验显示，DDIM调度参数 $\eta_t$ 对低NFE下的质量影响显著，默认设置 $\eta_t = \sigma_t(1-\alpha_t)$ 在FID与LPIPS间取得最佳平衡。

评估指标涵盖分布距离（FID/pFID）、感知质量（LPIPS）及保真度（cPSNR），但缺乏对物体幻觉的专门惩罚机制。代码已开源，超参数仅依赖 $\eta_t$ 序列，复现门槛较低。

## 关联研究分析

从问题动机看，DING与SONIC同属效率优化路线，但SONIC通过线性化去噪器优化初始噪声，仍依赖多步迭代；DING则从似然近似层面消除梯度计算，实现了单步内的无VJP采样。这一差异源于DING将修复任务的高斯似然特性显式利用，而SONIC针对的是通用零样本优化问题，未利用修复任务的代数结构。

从方法设计看，DING与CSF-Net均旨在解决大掩码下的结构缺失，但CSF-Net引入非模态补全模型提供语义骨架，属于结构约束路线；DING仅依赖扩散先验与观测约束，属于纯生成路线。DING在FFHQ上cPSNR略低于DDNM的现象暗示，缺乏显式结构先验可能在复杂语义区域导致轻微的结构漂移，这是纯生成路线在语义准确性上的固有局限。

## 总结

DING解决了零样本修复中VJP计算导致的效率瓶颈，通过解耦似然近似实现闭式采样，在FFHQ上FID达9.6，PIE-Bench上FID 63.6超越微调基线。其边界在于依赖高斯似然假设，且在严格保真度指标（cPSNR）上略逊于传统梯度引导方法。当掩码覆盖复杂语义结构时，解耦近似是否足以维持全局结构一致性，论文未提供针对极端大掩码的专项验证。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.18365)