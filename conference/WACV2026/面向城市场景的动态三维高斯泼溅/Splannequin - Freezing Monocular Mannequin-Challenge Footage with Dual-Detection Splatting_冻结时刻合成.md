# WACV2026最新论文 ｜Splannequin: Freezing Monocular Mannequin-Challenge Footage with Dual-Detection Splatting ｜冻结时刻合成

研究机构：国立阳明交通大学、美国俄亥俄州立大学

作者：Hao-Jen Chien、Yi-Chuan Huang、Chung-Ho Wu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.05113)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.05113)

> 动态城市场景重建旨在从多视角观测中恢复具有时间一致性的四维表示，但现有方法在单目稀疏监督下固定时间渲染时，常因高斯基元缺乏约束而产生鬼影与模糊。Splannequin 针对这一特定失效模式，提出双检测时间锚定正则化，将未观测或弱监督的高斯基元锚定至可靠的历史或未来状态。该方法以简单损失项嵌入现有动态高斯框架，无需架构修改即可实现零推理开销的冻结时刻合成。其价值在于为消费级视频提供了低成本的高保真静态视图生成方案，但受限于近静态假设，对快速非刚体运动的泛化能力存疑。

## 研究背景

动态高斯泼溅（3D Gaussian Splatting, 3DGS）通过显式高斯基元与可微光栅化实现了实时新视角合成，其时间扩展版本通过变形网络预测高斯参数随时间的演化。然而，标准动态重建的目标是保真地再现观测到的运动，其训练信号仅来自高斯可见且贡献梯度的时间步。当相机运动导致部分高斯在特定时刻离开视锥或被遮挡时，这些高斯在该时刻缺乏监督，其变形网络输出变得不稳定。这种监督缺失在常规动态渲染中可能被运动模糊掩盖，但在固定时间渲染（Freeze-time Rendering）中，这些未约束的高斯会直接导致鬼影和模糊伪影。

现有动态高斯方法如 4DGaussians、D-3DGS 和 SC-GS 均假设场景运动是主要目标，其损失函数旨在最小化光度误差以拟合运动轨迹。然而，Mannequin Challenge（MC）视频的核心需求是合成“冻结”场景，即抑制微动并保留静态细节。传统多相机子弹时间系统成本高昂，而单目 MC 视频虽低成本，但其稀疏的时间监督（平均可见性低于 10%）使得直接固定时间参数无法获得清晰结果。Splannequin 的切入点在于识别并修复这种由稀疏监督导致的几何漂移，而非优化运动保真度，从而在保持动态模型灵活性的同时，实现高质量的静态时刻合成。

## 核心方法

### 动态高斯参照系

标准动态高斯框架将场景表示为规范高斯集合，通过变形网络 $f_\theta$ 预测每个高斯在时间 $t$ 的位移 $\Delta \mu_{k,t}$ 和协方差变化 $\Delta \Sigma_{k,t}$。训练目标是最小化渲染图像与真实图像的光度损失。本文的关键差异在于，不优化运动轨迹的准确性，而是优化固定时间 $t^*$ 下所有高斯参数的稳定性，以消除因时间监督缺失导致的伪影。

### 双检测状态分类

设计动机在于区分两种导致伪影的未监督状态：相机已越过的高斯（Hidden）与尚未被充分观测的高斯（Defective）。对于高斯 $k$ 在时间 $t$，若其中心投影在视锥外，定义为 Hidden；若其在视锥内但渲染贡献梯度小于 $1e-9$，定义为 Defective。这种分类基于可微光栅化器的输出，无需额外网络。

$$
s_{hidden}(k, t) = \begin{cases} 1, & \text{visibility is 0} \\ 0, & \text{otherwise} \end{cases}, \quad s_{defective}(k, t) = \begin{cases} 1, & \text{visibility is 1 with gradient } \le 1e-9 \\ 0, & \text{otherwise} \end{cases}
$$

该定义将模糊的“无监督”状态细化为具有明确时空因果关系的两类，为后续差异化锚定策略提供了基础。

### 时间锚定正则化

针对 Hidden 高斯，其状态应锚定至过去可靠观测的状态；针对 Defective 高斯，其状态应锚定至未来可靠观测的状态。对于未监督高斯 $k$ 在时间 $t$，随机采样参考时间 $t_{ref}$，若 $t_{ref}$ 满足方向约束（Hidden 要求 $t_{ref} < t$，Defective 要求 $t_{ref} > t$）且高斯在 $t_{ref}$ 为 Well-supervised，则施加一致性损失：

$$
\mathcal{L}_{consistency} = \phi(t, t_{ref}) \cdot D(\theta_k(t), \theta_k(t_{ref}))
$$

其中 $\phi(t, t_{ref}) = e^{-\tau |t - t_{ref}|}$ 为时间距离加权，$\tau=5$，$D$ 为 $L_1$ 或 $L_2$ 范数。总损失为 $\mathcal{L}_{total} = \mathcal{L}_{recon} + \lambda_{hidden} \mathcal{L}_{hidden} + \lambda_{defective} \mathcal{L}_{defective}$，权重 $\lambda=10$。该机制通过指数衰减确保近邻时间步的锚定强度更高，既抑制了漂移，又保留了必要的动态变化。

## 实验评估

实验在自建 10 个真实 MC 视频基准上进行，分辨率 640×360，共 2,869 帧。基线包括 4DGaussians、D-3DGS 和 SC-GS，均为当前主流动态高斯方法。由于缺乏共享数据集，无法与 UniSplat 等前馈方法直接比较，但本文聚焦于冻结时刻合成这一特定任务，基线选择覆盖了主要的动态高斯骨干。

| 方法 | CQA 提升 (%) | COVER Technical 提升 (%) |
| :--- | :--- | :--- |
| 4DGaussians + Splannequin | 121.33 | 73.03 |
| D-3DGS + Splannequin | 243.80 | 339.85 |
| SC-GS + Splannequin | 48.88 | 75.24 |

D-3DGS 在加入 Splannequin 后获得最大提升，CQA 提升 243.80%，COVER Technical 提升 339.85%，表明该方法对伪影最严重的骨干效果最显著。消融实验显示，移除 Hidden 损失导致 COVER Overall 下降 1072.41%，移除 Defective 损失导致 CQA 下降 162.23%，证明两类锚定策略均不可或缺，且 Hidden 损失对整体视频质量影响更大。

评估主要依赖无参考感知指标（CQA, COVER, TOPIQ-NR 等），因为真实帧包含需抑制的运动，全参考指标不适用。代码基于 PyTorch 扩展官方动态高斯框架，在 RTX 4090 上训练 30,000 次迭代，推理速度超过 280 FPS。局限性在于假设场景近静态，对快速非刚体运动缺乏可靠锚点，且未提供运动阈值的定量分析。

## 关联研究分析

从问题动机看，Splannequin 与 Shape of Motion 均关注单目动态重建中的遮挡与模糊，但前者旨在保留运动细节，后者旨在抑制运动以合成静态视图。这一差异源于任务目标的不同：Shape of Motion 服务于动态场景理解，而 Splannequin 服务于 VFX 中的冻结时刻合成。Splannequin 的双检测机制是其核心创新，而 Shape of Motion 依赖更复杂的几何约束，导致计算开销更大。

从方法设计看，Splannequin 与 EFA-GS 等静态伪影去除方法不同，后者通过频域分析消除漂浮物，但假设场景完全刚性。Splannequin 利用动态高斯的时间维度，通过时间锚定而非空间滤波来稳定高斯，这使得它能够处理微动场景，而 EFA-GS 在存在运动时会失效。然而，Splannequin 的锚定策略依赖时间距离加权，对于非单调运动或快速方向变化的场景，其有效性可能受限，论文未对此进行充分验证。

## 总结

Splannequin 解决了单目 MC 视频中固定时间渲染的鬼影与模糊问题，其核心在于识别 Hidden 与 Defective 高斯并施加时间锚定正则化。该方法在 D-3DGS 上实现了 CQA 243.80% 和 COVER Technical 339.85% 的提升，证明了时间锚定在稀疏监督下的有效性。然而，其近静态假设限制了在快速非刚体运动场景中的应用，且缺乏对运动阈值的定量分析。当场景中存在快速方向变化或大幅非刚体形变时，时间锚定策略是否仍能保持几何稳定性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.05113)