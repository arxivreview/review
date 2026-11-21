# CVPR2026最新论文 ｜Ultra Diffusion Poser: Diffusion-Based Human Motion Tracking From Sparse Inertial Sensors and Ranging-Based Between-Sensor Distances ｜超宽带扩散姿态估计

研究机构：瑞士苏黎世联邦理工学院

作者：Dominik Hollidt、Tommaso Bendinelli、Christian Holz

论文原文见 [arXiv](https://arxiv.org/abs/2606.02153)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.02153)

> 稀疏惯性传感器与超宽带（UWB）测距融合旨在解决IMU积分漂移导致的全身姿态估计不准问题。现有方法仅将UWB距离作为辅助特征输入网络，忽略了其蕴含的几何约束，导致预测姿态与实测距离冲突。本文提出Ultra Diffusion Poser (UDP)，通过解析重建3D传感器布局并引入扩散引导机制，显式建模距离约束。该方法在多数基准上显著降低关节位置误差，但对高噪声UWB信号敏感，鲁棒性有待验证。

## 研究背景

当穿戴式惯性测量单元（IMU）用于全身姿态重建时，加速度与角速度信号的积分误差会随时间累积，导致根节点轨迹漂移。这种漂移在缺乏绝对位置参考的开放场景中尤为严重，因为IMU无法直接观测帧间空间位移或跨身体段的位置关系。为校正漂移，研究者引入UWB测距提供非漂移的传感器间距离，但早期方法仅将这些距离标量作为网络输入特征，未利用其几何意义。

稀疏惯性姿态估计的主流路线分为纯学习系统与混合系统。纯学习系统如Deep Inertial Poser (DIP) 和 TransPose 依赖大规模数据学习运动学先验，但难以消除积分漂移；混合系统如PIP 和 GlobalPose 结合物理优化器，虽能减少脚滑，却引入计算开销且易产生抖动。UWB融合方法如UIP 和 UMotion 虽缓解了漂移，但将距离视为辅助特征，导致预测姿态可能违反实测距离约束（如预测手腕间距70cm而实测90cm）。本文切入点在于将UWB距离从“特征”提升为“几何约束”，通过解析重建3D传感器布局并融入扩散采样过程，确保生成姿态与实测距离一致。

## 核心方法

### 方法参照系

本文问题属于多模态融合姿态估计，标准流程为：输入IMU信号与UWB距离，通过神经网络回归SMPL姿态。关键差异在于，本文不将距离作为标量特征，而是将其解析为3D传感器位置，并作为扩散模型的强条件信号与引导项。

### 空间布局模块

设计动机：解决MDS重建的旋转与反射歧义，提供方向一致的3D传感器布局作为姿态先验。空间布局模块（SPL）首先通过经典多维标度（MDS）从距离矩阵 $\mathbf{D}_t$ 解析求解3D传感器坐标 $\mathbf{X}_{MDS}$：

$$ \mathbf{X}_{MDS} = \mathbf{V}_3 \Lambda_3^{1/2} $$

其中 $\mathbf{V}_3$ 为Gram矩阵的前三个特征向量，$\Lambda_3$ 为对应特征值。由于MDS解仅定义至旋转与反射，SPL引入可学习的旋转估计器（3层LSTM），端到端训练以恢复定向布局 $\mathbf{P}_{SPL}$ 及其镜像 $\bar{\mathbf{P}}_{SPL}$，并添加残差 $\mathbf{P}_{res}$ 校正噪声。该模块将距离标量转化为几何位置，为扩散模型提供强条件信号。

### UWB-扩散引导

设计动机：解决扩散采样过程中预测姿态违反UWB距离约束的问题，避免后处理优化导致的抖动。UWB-扩散引导借鉴分类器引导机制，在采样循环中通过前向运动学（FK）计算预测传感器位置，并定义引导损失 $\epsilon_{uwb}$：

$$ \epsilon_{uwb} = \sum_{i<j} \| \hat{d}_{ij} - d_{ij} \|_2 $$

其中 $\hat{d}_{ij}$ 为预测距离，$d_{ij}$ 为实测距离。在扩散采样步骤中，均值 $\mu_t$ 被修正为：

$$ \tilde{\mu}_t = \mu_t(M_t, \hat{M}_0) - \lambda \Sigma_t \nabla \epsilon_{uwb} $$

该机制实时校正偏离实测距离的姿态，确保生成运动在满足几何约束的同时保持平滑，无需额外的物理优化器。

## 实验评估

实验在DIP-IMU、DanceDB、TotalCapture、UIP-DB和GIP-DB上进行，基线覆盖IMU-only（PIP, GlobalPose）和IMU+UWB（UIP, UMotion, GIP）路线，但未对比最新纯生成式方法如KineST或ProbIP。UDP在DIP-IMU上JPE为3.42cm，较UIP的5.05cm降低22%；在GIP-DB上JPE为8.86cm，优于GIP的9.45cm。

| 数据集 | 模型 | UWB | SIP (°) | GAE (°) | JPE (cm) | Jitter |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| DIP-IMU | UDP | ✓ | 10.39 | 8.19 | 3.42 | 0.125 |
| DIP-IMU | UIP | ✓ | 13.20 | 8.23 | 5.05 | 0.240 |
| GIP-DB | UDP | ✓ | 25.74 | 22.23 | 8.86 | 0.125 |
| GIP-DB | GIP | ✓ | 27.77 | 23.34 | 9.45 | 0.706 |

消融实验显示，移除SPL和UWB引导后，SIP误差从8.95°升至10.22°，JPE从3.76cm升至4.39cm，表明几何约束对精度贡献显著。UWB噪声敏感性分析表明，当UWB噪声降低至50%时，UDP较UIP的JPE优势扩大至3.76cm，但高噪声下（UIP-DB）需微调才能达标，暴露了对传感器质量的依赖。

评估指标包含SIP、GAE、JPE和Jitter，覆盖精度与平滑性，但缺乏对长序列漂移的量化指标。代码已开源，但论文未报告训练超参数与GPU配置，可复现性依赖补充材料。

## 关联研究分析

从问题动机看，UDP与UIP、UMotion同属IMU+UWB融合路线，但UDP将距离从“特征”提升为“几何约束”，而UIP仅通过图卷积网络处理距离标量，UMotion依赖卡尔曼滤波手动调参。这一差异源于UDP对几何一致性的强调，但代价是对UWB噪声更敏感，而UIP在原始噪声下表现略优，暗示特征级融合在噪声鲁棒性上可能更具优势。

从方法设计看，UDP与DiffusionPoser同属扩散模型框架，但DiffusionPoser未引入UWB特有的几何引导，仅依赖IMU信号。UDP的UWB-扩散引导机制借鉴了分类器引导思想，将距离约束融入采样过程，而DiffusionPoser缺乏此类约束，导致其在稀疏信号下可能产生违反物理布局的姿态。这一设计差异表明，扩散模型在姿态估计中的优势不仅来自生成能力，更来自对物理约束的显式建模。

## 总结

UDP旨在解决IMU积分漂移与UWB距离约束未被充分利用的矛盾，通过解析重建3D传感器布局并引入扩散引导，确保生成姿态与实测距离一致。该方法在DIP-IMU上JPE降低22%，在GIP-DB上优于SOTA，证明了几何约束显式建模的有效性。然而，实验暴露了对高噪声UWB信号的敏感性，在UIP-DB上需微调才能达标，且未对比最新纯生成式方法。当UWB噪声进一步降低时，UDP的几何约束优势是否持续扩大，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.02153)