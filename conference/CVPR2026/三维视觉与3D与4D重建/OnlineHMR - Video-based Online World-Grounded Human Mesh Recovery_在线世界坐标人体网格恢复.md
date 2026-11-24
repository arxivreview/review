# CVPR2026最新论文 ｜OnlineHMR: Video-based Online World-Grounded Human Mesh Recovery ｜在线世界坐标人体网格恢复

研究机构：美国卡内基梅隆大学、美国宾夕法尼亚大学

作者：Yiwen Zhao、Ce Zheng、Yufu Wang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.17355)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.17355)

> 视频人体网格恢复（Human Mesh Recovery, HMR）旨在从单目视频中重建3D人体姿态与形状，其核心价值在于以低成本替代昂贵的运动捕捉。现有世界坐标恢复方法多依赖离线全局优化，无法支持实时交互应用。本文切入点在于构建严格因果的在线框架，通过滑动窗口学习与增量式SLAM实现流式推理。该方法在保持与离线方法相当精度的同时，实现了低延迟的实时处理，但其精度仍受限于在线约束下的累积误差。

## 研究背景

当相机在动态场景中移动时，单目图像中的人体观测不仅受姿态多解性影响，还受相机位姿估计误差的干扰。这种干扰导致相机坐标系下重建的人体网格无法直接用于需要度量尺度与全局轨迹的应用场景。为了解决这一问题，研究者引入了同时定位与建图（Simultaneous Localization and Mapping, SLAM）技术来估计相机轨迹，将局部人体运动锚定到全局世界坐标系中。然而，传统SLAM假设场景静态，而人体作为动态物体破坏了这一假设，导致特征匹配失败与轨迹漂移。

视频HMR的主流路线分为离线与在线两类。离线方法如TRAM利用全局优化获得高精度，但需访问完整视频序列，无法满足实时性需求。在线方法如Human3R虽支持流式推理，但局部运动精度不足且存在时序抖动。本文针对这一矛盾，提出OnlineHMR框架，旨在严格因果约束下实现高保真的世界坐标人体恢复。该框架需同时满足系统级因果性、重建保真度、时序一致性与计算效率四项标准，填补了在线世界坐标HMR的性能空白。

## 核心方法

### 方法参照系

本文基于TRAM框架，将其从离线全局优化改造为在线增量处理。标准流程中，相机坐标系HMR与全局轨迹估计独立进行，本文将其解耦为两个因果分支：前者通过滑动窗口融合时序信息，后者通过增量SLAM估计相机位姿。关键差异在于，所有模块仅依赖当前及过去帧，禁止访问未来信息或进行全局优化。

### 滑动窗口学习与KV缓存推理

为在因果约束下利用时序信息，本文采用滑动窗口学习策略。训练时，将视频分割为重叠窗口，每个窗口内最后一帧通过自注意力与交叉注意力融合前序帧特征，回归SMPL参数。推理时，引入键值（Key-Value, KV）缓存机制，存储前序帧的键与值向量，实现常数时间的流式处理。该设计解决了传统固定长度序列输入需访问未来帧导致的因果违规问题。注意力计算公式为：

$$ \text{Attn}(\mathbf{q}_i, \mathbf{k}_{prev}, \mathbf{v}_{prev}) = \text{softmax}\left(\frac{\mathbf{q}_i \mathbf{k}_{prev}^T}{\sqrt{d}}\right) \mathbf{v}_{prev} $$

其中 $\mathbf{q}_i$ 为当前帧查询，$\mathbf{k}_{prev}, \mathbf{v}_{prev}$ 为缓存的前序帧键值。此机制在保持时序平滑性的同时，避免了重叠帧的冗余计算。

### 人体中心增量SLAM与物理约束

针对动态人体干扰SLAM特征匹配的问题，本文引入软人体掩码与指数移动平均（Exponential Moving Average, EMA）校正。首先，利用SAM2分割人体区域，并通过膨胀与高斯模糊生成软置信掩码 $C_i^{soft}$，抑制动态区域对相机轨迹估计的干扰。其次，对SLAM输出的相机平移与旋转施加EMA校正，抑制高频抖动。平移更新公式为：

$$ \mathbf{t}_i^{smooth} = \mathbf{t}_i^{ema} + \Delta \mathbf{t}_i \cdot \mathbb{I}(\|\Delta \mathbf{t}_i\| \leq \tau) $$

其中 $\tau = \lambda_{clamp} v$ 为速度依赖的钳制阈值。该设计通过物理平滑约束间接正则化人体运动，解决了增量SLAM在长序列下的累积噪声问题，确保了世界坐标轨迹的物理合理性。

## 实验评估

实验在3DPW、EMDB-1与EMDB-2数据集上进行，基线覆盖逐帧、离线视频与在线视频三类方法。对比方法包括HMR2.0、TRAM、Human3R等，但缺失SAM 3D Body等最新SOTA对比。

| 方法 | 3DPW PA-MPJPE (mm) | 3DPW MPJPE (mm) | EMDB-2 WA-MPJPE (mm) |
|---|---|---|---|
| TRAM | 35.6 | 63.9 | 76.4 |
| Human3R | 44.1 | 71.2 | 112.2 |
| OnlineHMR | 43.7 | 69.9 | 93.5 |

OnlineHMR在3DPW上PA-MPJPE为43.7mm，略优于Human3R的44.1mm，但显著高于TRAM的35.6mm。在EMDB-2世界坐标评估中，OnlineHMR的WA-MPJPE为93.5mm，优于Human3R的112.2mm，但落后于TRAM的76.4mm。这表明在线约束下精度有所牺牲，但仍优于现有在线方法。

| 方法 | 3DPW Accel (mm) | 3DPW Jitter (mm) |
|---|---|---|
| w/o Velocity Reg | 8.9 | 32.3 |
| w/ Velocity Reg | 6.4 | 19.5 |

消融实验显示，速度正则化使Accel从8.9降至6.4，Jitter从32.3降至19.5，验证了其对时序一致性的贡献。软掩码策略使MASt3R-SLAM的ATE从1.22降至0.83，证明其对相机轨迹精度的提升。

评估指标包含MPJPE、PA-MPJPE、PVE、Accel与Jitter，但缺乏置信区间报告。代码已开源，训练使用单张H100 GPU，收敛于52K迭代。评估协议遵循TRAM标准，但在线方法的延迟指标（Avg. Delay）显示OnlineHMR为0.30秒，低于离线方法的线性增长延迟。

## 关联研究分析

从问题动机看，OnlineHMR与Human3R均针对在线世界坐标恢复，但Human3R依赖轻量级循环状态，导致局部运动细节丢失。OnlineHMR通过滑动窗口学习保留短时程时序相关性，在3DPW上PA-MPJPE优于Human3R 0.4mm。这一差异源于Human3R未显式建模帧间运动学约束，而OnlineHMR引入速度正则化损失，直接惩罚关节速度突变。

从方法设计看，OnlineHMR与TRAM共享ViT骨干与HMR2.0预训练权重，但TRAM采用离线全局优化，而OnlineHMR使用增量SLAM与KV缓存。TRAM在3DPW上PA-MPJPE为35.6mm，优于OnlineHMR的43.7mm，差距主要源于全局优化对累积误差的修正能力。OnlineHMR的EMA校正虽抑制高频噪声，但无法完全消除长序列下的尺度漂移，这导致其W-MPJPE（未对齐尺度）表现滞后于WA-MPJPE（对齐尺度）。

## 总结

OnlineHMR旨在解决在线世界坐标HMR中因果性与精度的矛盾。现有离线方法无法实时，在线方法精度不足，本文通过滑动窗口学习与增量SLAM实现严格因果下的流式推理。实验表明，该方法在3DPW上PA-MPJPE为43.7mm，EMDB-2上WA-MPJPE为93.5mm，优于Human3R但落后于TRAM。其边界在于增量SLAM的累积误差导致尺度不一致，且速度正则化可能过度平滑快速运动。当视频序列长度增加时，EMA校正的窗口大小如何自适应调整以平衡噪声抑制与运动保真，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.17355)