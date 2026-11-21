# CVPR2026最新论文 ｜From Pairs to Sequences: Track-Aware Policy Gradients for Keypoint Detection ｜序列感知关键点策略学习

研究机构：武汉大学、小米

作者：Yepeng Liu、Hao Li、Liwen Yang 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.20630)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.20630)

> 3D视觉系统依赖关键点在长序列中的稳定性，但现有方法仅优化单帧对匹配性，导致轨迹断裂。TraqPoint将关键点检测重构为序列决策问题，通过强化学习直接优化长期可跟踪性。其核心是设计基于多视角一致性与区分度的复合奖励函数。该方法在相对位姿估计与3D重建任务上超越现有SOTA，但其收益是否源于强化学习范式本身而非骨干网络升级，仍需更严格的消融验证。

## 研究背景

Structure-from-Motion (SfM) 与 Simultaneous Localization and Mapping (SLAM) 系统的精度上限取决于关键点在视角剧烈变化下的重复检测能力。传统关键点定义基于局部纹理显著性，但在长序列中，单帧对匹配良好的点可能因光照漂移或运动模糊而丢失，这种“瞬时匹配性”与“长期可跟踪性”的错位是序列应用失效的根源。为弥合这一差距，研究者需将优化目标从孤立图像对扩展至整个视频序列，使检测策略直接服务于轨迹的持久性。

现有学习式关键点方法主要分为自监督与监督两类。自监督方法如SuperPoint利用几何变换生成伪标签，监督方法如RDD在MegaDepth等大规模真实数据集上训练，但二者均遵循“成对训练”范式：奖励函数仅基于单帧对内的匹配内点数或相似度计算。这种范式在短基线匹配任务中表现优异，却忽略了序列累积误差。强化学习（Reinforcement Learning, RL）方法如DISK和RIPE虽引入策略梯度，但其奖励信号仍局限于单帧对，未能捕捉跨帧的时间依赖。TraqPoint的切入点在于将环境状态从“图像对”扩展为“图像序列”，使策略网络能够感知并优化关键点在整个序列中的生存概率。

## 核心方法

### 双分支架构与策略网络定义

TraqPoint沿用RDD的双分支架构，但将关键点分支重新定义为RL策略网络 $\pi_\theta$。描述分支采用DINOv3-ConvNeXt骨干提取多尺度特征，经可变形Transformer聚合后冻结，为奖励计算提供稳定描述子；关键点分支保留ALIKED的轻量卷积结构，输出全分辨率logit图 $L \in \mathbb{R}^{H \times W}$。该设计的关键差异在于：描述分支不再参与端到端梯度更新，而是作为固定环境观测器，确保策略优化仅聚焦于检测位置的选择，而非特征表示的学习。

### 混合采样与轨迹奖励机制

策略网络的动作空间为从logit图中采样 $N$ 个关键点。为避免全局采样导致的空间聚集，TraqPoint采用混合采样策略：$N_g$ 个点从全局分布 $P_\theta$ 中抽取以利用高概率区域，$N_{grid}$ 个点从 $G \times G$ 网格的局部softmax分布中抽取以保证空间覆盖。奖励函数 $R_i$ 针对每个采样点 $\mathbf{x}_i$ 计算其在序列中的轨迹质量，定义为可见帧内逐帧奖励的均值：

$$
R_i = \frac{1}{|\mathcal{V}_i|} \sum_{t \in \mathcal{V}_i} R_i^{[t]}
$$

其中 $\mathcal{V}_i$ 为 $\mathbf{x}_i$ 可见的帧索引集。逐帧奖励 $R_i^{[t]}$ 由Rank Reward与Distinctiveness Reward加权平均构成。Rank Reward量化关键点在目标帧局部邻域内的显著性百分位，仅当超过阈值 $\tau_{rank}=0.2$ 时给予线性奖励；Distinctiveness Reward借鉴Lowe ratio test，计算参考描述子与目标帧最近邻距离比 $d_1/d_2$，仅当比值低于 $\tau_{dist}=0.85$ 时给予奖励。该设计动机在于：纯匹配奖励无法区分“易匹配但易漂移”的点与“难匹配但稳定”的点，复合奖励通过显式建模显著性持久性与全局唯一性，筛选出具备长期生存潜力的关键点。

### 策略梯度优化

策略网络通过最大化期望轨迹奖励进行优化，损失函数包含策略梯度项、空间熵正则项及早期warm-up项：

$$
\mathcal{L}_\theta = -\frac{1}{N} \sum_{i=1}^N R_i \log P_\theta(\mathbf{x}_i) - \lambda \mathcal{H}(P_\theta) + \alpha_t \mathcal{L}_w
$$

其中 $\mathcal{H}(P_\theta)$ 为logit图的空间熵，防止模式坍塌；$\mathcal{L}_w$ 为基于FAST检测器的弱监督BCE损失，权重 $\alpha_t$ 在前10% epoch内从1.0线性衰减至0.0。该优化过程将离散的关键点选择问题转化为连续的概率分布调整，使网络能够学习“哪些位置更可能生成稳定轨迹”而非“哪些位置在当前帧对中最易匹配”。

## 实验评估

| 方法 | MegaDepth AUC@5° | ScanNet AUC@5° | KITTI Seq-01 ATE |
| :--- | :--- | :--- | :--- |
| RDD | 51.9 | 13.7 | 35.3 |
| RIPE | 45.4 | 9.4 | 43.7 |
| TraqPoint | **55.8** | **16.6** | **29.9** |

实验在MegaDepth、ScanNet、KITTI及ETH基准上进行，基线覆盖监督学习（RDD、ALIKED）与RL方法（DISK、RIPE）。TraqPoint在MegaDepth AUC@5°上较RDD提升3.9，在KITTI视觉里程计Seq-01的ATE上降低5.4m，表明序列感知奖励有效提升了长序列稳定性。然而，基线中缺乏近期基于Transformer的密集匹配方法（如MASt3R）的稀疏化对比，且未报告计算开销，无法评估RL训练与推理的效率代价。

| 变体 | AUC@5° | AKTL |
| :--- | :--- | :--- |
| TraqPoint-Full | **55.8** | **6.6** |
| w/o Ranking Reward | 52.6 | 4.0 |
| w/o Distinctiveness Reward | 54.6 | 5.9 |
| TraqPoint – Pairwise | 53.3 | 4.3 |

消融实验显示，移除Rank Reward导致AUC@5°下降3.2、AKTL下降2.6，移除Distinctiveness Reward导致AUC@5°下降1.2、AKTL下降0.7，表明显著性持久性对轨迹长度贡献更大。将序列奖励替换为成对奖励后，AKTL从6.6降至4.3，验证了序列优化范式对长时稳定性的核心作用。但消融未单独隔离DINOv3骨干的贡献，无法区分性能提升源于RL范式还是更强的特征提取器。

评估协议采用标准AUC与ATE指标，但未报告置信区间或多次运行方差。代码未开源，超参数（如 $\tau_{rank}$、$\tau_{dist}$）的敏感性分析缺失，限制了可复现性。

## 关联研究分析

从问题动机看，TraqPoint与RDD的核心差异在于优化目标的时序范围。RDD在MegaDepth上通过监督学习优化单帧对匹配精度，其奖励信号隐含假设“当前帧匹配良好即未来匹配良好”；TraqPoint则显式建模轨迹断裂风险，通过序列奖励惩罚那些在后续帧中显著性衰减或描述子混淆的点。这一差异源于任务特性：SfM/SLAM对轨迹连续性的依赖远高于单帧匹配，但RDD等基线未针对此特性调整训练目标，导致其在长序列中性能衰减。

从方法设计看，TraqPoint与DISK/RIPE同属RL范式，但奖励函数设计存在本质区别。DISK/RIPE的奖励基于单帧对内几何一致内点数，本质仍是成对匹配性的代理指标；TraqPoint的奖励直接计算关键点在序列中的可见性、显著性排名与描述子区分度，将“可跟踪性”从隐式目标转为显式优化变量。这种设计使策略网络能够学习超越瞬时匹配的长期稳定性特征，但也引入了对深度与位姿先验的依赖——若初始位姿估计不准，投影可见性判断将失效，而DISK/RIPE无需此先验。

## 总结

TraqPoint针对成对训练范式与序列应用需求的目标错位，通过RL框架将关键点检测重构为序列决策问题，直接优化长期可跟踪性。其复合奖励机制在MegaDepth AUC@5°上达到55.8，KITTI Seq-01 ATE降至29.9m，验证了序列感知优化的有效性。然而，实验未隔离DINOv3骨干的贡献，且依赖深度与位姿先验计算奖励，限制了其在无几何先验场景的适用性。当骨干网络固定为ResNet-50时，RL范式相对监督学习的增益是否仍显著，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.20630)