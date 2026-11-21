# CVPR2026最新论文 ｜EventHub: Data Factory for Generalizable Event-Based Stereo Networks without Active Sensors ｜事件立体匹配的数据工厂：无真值训练框架

研究机构：德国柏林工业大学、意大利博洛尼亚大学

作者：Luca Bartolomei、Fabio Tosi、Matteo Poggi 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.02331)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.02331)

> 事件相机立体匹配旨在从异步像素亮度变化流中恢复深度，但受限于LiDAR真值标注的稀疏性与成本，现有模型泛化能力受限。传统方法依赖昂贵的主动传感器采集，导致训练数据规模远小于帧式领域，难以支撑基础模型的零样本迁移。EventHub通过神经辐射场合成代理事件与深度，结合RGB立体基础模型的跨模态蒸馏，构建无真值训练数据工厂。该框架在跨域测试中将误差降低50%，验证了代理数据的有效性，但其对动态场景与极端光照的鲁棒性仍存疑。

## 研究背景

事件相机通过记录像素亮度变化的时间戳与极性，以微秒级分辨率捕捉场景动态，避免了帧式相机的运动模糊与过曝问题。然而，事件流的异步稀疏特性使得传统基于帧的立体匹配算法无法直接应用，且现有事件立体数据集（如DSEC、M3ED）规模仅为帧式数据集的千分之一，严重制约了深度学习模型的泛化能力。

帧式立体匹配领域已建立成熟的迭代优化与基础模型范式，如RAFT-Stereo通过GRU递归更新提升效率，FoundationStereo利用单目深度先验实现零样本泛化。然而，这些方法依赖海量标注数据，而事件域缺乏此类资源。LiDAR虽能提供真值，但其稀疏采样、动态物体累积误差及非朗伯表面失效问题，导致基于LiDAR监督的模型在跨域场景中性能骤降。现有事件立体方法（如SE-CFF、EMatch）多局限于域内训练，缺乏应对传感器差异与场景变化的鲁棒性。

EventHub切入这一数据瓶颈，提出不依赖主动传感器的训练框架。它利用神经辐射场（NVS）从单目RGB序列合成代理事件与深度标签，或通过RGB-Event跨模态蒸馏生成代理监督。这一策略将事件立体匹配的训练范式从“昂贵真值驱动”转向“合成数据驱动”，旨在解决数据稀缺导致的泛化不足问题。

## 核心方法

### 方法参照系

事件立体匹配的标准流程通常包括事件表示、代价体构建与视差预测。主流方法如SE-CFF采用Tencode表示事件，通过3D卷积聚合代价体；EMatch则使用VoxelGrid处理时空稀疏性。本文问题与通用流程的关键差异在于：不直接优化网络架构，而是重构训练数据生成环节，利用RGB域先验替代LiDAR真值，从而解耦网络设计与数据质量。

### 神经辐射场代理数据生成

针对单目RGB序列缺乏事件对应物的问题，EventHub引入SVRaster作为NVS基础，通过虚拟轨迹模拟事件相机自运动。设计动机在于解决LiDAR真值在动态场景下的累积误差与稀疏性缺陷。具体而言，系统首先通过COLMAP估计相机位姿，再利用SVRaster优化辐射场表示。渲染时，采用局部轨迹 $\Gamma(\tau)$ 或全局轨迹 $\Omega(\tau)$ 生成连续位姿序列，其中 $\Gamma(\tau) = [\hat{R}_i | \hat{t}_i + \tau \mathbf{r}]$ 表示沿任意轴的平移。通过ESIM将渲染帧转换为模拟事件流，视差图 $\mathbf{D} = (b \cdot f) / \mathbf{Z}$ 作为监督信号。该过程生成的代理数据在域内测试中MAE降至0.89px，接近LiDAR真值水平，且避免了LiDAR重投影误差。

### 跨模态蒸馏与模型复用

当存在配对的RGB-Event数据时，EventHub利用RGB立体基础模型（SFM）生成代理标签。设计动机在于利用RGB域成熟的SOTA模型先验，弥补事件域标注缺失。具体流程为：使用FoundationStereo或StereoAnywhere处理RGB立体对 $(I_L, I_R)$，预测视差图，再通过相对位姿 $\mathbf{T}_{c \to e}$ 重投影至事件域。公式表达为 $\hat{D}_e = \text{Reproject}(\hat{D}_c, \mathbf{T}_{c \to e})$，其中 $\hat{D}_c$ 为RGB预测视差。随后，将预训练的RGB模型（如FoundationStereo ViT-S）微调为事件模型（E-FoundationStereo），冻结Depth Anything V2先验模块。这一策略使事件模型继承RGB域的几何理解能力，在M3ED夜间场景中MAE从3.89px降至1.01px，显著优于LiDAR监督模型。

## 实验评估

实验在DSEC、M3ED、MVSEC三个数据集上进行，评估指标包括MAE与1PE/2PE/3PE。基线覆盖LiDAR监督模型、SE-CFF、EMatch及帧式SOTA（FoundationStereo、StereoAnywhere）。缺失纯自监督事件方法或NVS生成方法的直接对比，但LiDAR监督作为强基线已充分验证代理数据的有效性。

| 模型 | 训练方式 | M3ED Day MAE (px) | M3ED Night MAE (px) | MVSEC Indoor MAE (px) |
|---|---|---|---|---|
| E-FoundationStereo | MIX 4 | 0.98 | 1.54 | 2.45 |
| E-FoundationStereo | LiDAR (GT) | 2.89 | 1.99 | 2.87 |
| EMatch | MIX 4 | 2.23 | 5.03 | 3.10 |
| EMatch | LiDAR (GT) | 12.22 | 18.63 | 7.95 |

MIX 4组合（NeRF-Stereo + ScanNet++ + DSEC代理数据）在M3ED Day场景下MAE为0.98px，较LiDAR监督的2.89px降低66%。在MVSEC Indoor场景，E-FoundationStereo的MAE为2.45px，优于LiDAR监督的2.87px。这表明代理数据不仅弥补了LiDAR稀疏性缺陷，还通过多源数据融合提升了跨域泛化能力。

消融实验显示，MIX 1（仅NeRF-Stereo）MAE为1.87px，MIX 3（加入DSEC代理数据）降至1.15px，MIX 4进一步降至0.98px。边际收益递减现象明显：从MIX 3到MIX 4，MAE仅降低0.16px，说明DSEC域内数据对泛化贡献有限，而合成数据（NeRF-Stereo、ScanNet++）是泛化提升的主要驱动力。LiDAR监督在域内精度上仍具优势（DSEC Night MAE 1.01px vs MIX 3 Night 1.01px），但在跨域场景中全面落后。

评估边界方面，论文未报告计算效率（FPS、MACs），且NVS生成过程需离线优化，不适用于实时部署。代码已开源，但NVS场景优化参数（如 $\lambda_{SSIM}=0.02$）未提供完整复现指南。LiDAR真值的稀疏性导致评估指标（基于LiDAR点）可能低估代理数据在密集区域的实际精度，这一偏差在论文图5中通过定性对比揭示，但未量化。

## 关联研究分析

从问题动机看，EventHub与FoundationStereo同属基础模型范式，但前者聚焦数据生成而非模型架构。FoundationStereo依赖海量RGB标注数据实现零样本泛化，而EventHub针对事件域数据稀缺，通过NVS合成代理数据解决训练瓶颈。这一差异源于任务特性：事件相机数据获取成本远高于RGB，且LiDAR真值质量较差，使得“数据工厂”策略比“模型增强”更具性价比。

从方法设计看，EventHub与NeRF-Stereo（Li et al., 2023）均利用NVS生成训练数据，但后者仅生成RGB立体对，未处理事件流。EventHub引入ESIM将渲染帧转换为事件，并设计虚拟轨迹模拟自运动，解决了NVS不原生支持事件的问题。这一创新源于事件相机的异步特性：静态NVS渲染无法产生事件，必须通过相机运动触发亮度变化。论文未探讨NVS生成事件与真实事件在统计特性上的差异，如事件密度与噪声分布，这可能影响模型在极端动态场景下的鲁棒性。

## 总结

EventHub解决的核心矛盾是事件立体匹配中LiDAR真值稀缺与模型泛化需求之间的张力。其切入点在于利用RGB域成熟的NVS与SFM技术，通过合成代理数据替代昂贵真值，从而绕过主动传感器依赖。方法上，它结合神经辐射场生成代理事件与深度，并通过跨模态蒸馏复用RGB基础模型，实现了无真值训练。实验证明，MIX 4策略在M3ED Day场景MAE降至0.98px，较LiDAR监督降低66%，验证了代理数据的有效性。然而，论文未量化NVS生成事件与真实事件在统计特性上的差异，且NVS优化过程离线耗时，限制了实时应用。当场景动态性超过虚拟轨迹模拟能力时，代理数据的物理一致性是否仍能支撑高精度匹配，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.02331)