# CVPR2026最新论文 ｜Learnable Motion-Focused Tokenization for Effective and Efficient Video Unsupervised Domain Adaptation ｜可学习运动聚焦分词用于高效视频无监督域适应

研究机构：加拿大萨斯喀彻温大学

作者：Tzu Ling Liu、Ian Stavness、Mrigank Rochan

论文原文见 [arXiv](https://arxiv.org/abs/2604.09955)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.09955)

> 视频无监督域适应（VUDA）旨在将标注源域的动作识别模型迁移至无标签目标域，但现有方法常因背景域偏移导致性能远低于全监督上限，且普遍忽视计算效率。本文指出静态背景token既加剧域偏移又浪费算力，提出可学习运动聚焦分词（LMFT），通过强化学习动态丢弃低运动token以聚焦动作语义。该方案在三个基准上刷新SOTA并大幅降低训练成本，但其依赖伪标签质量与单一阈值泛化性存疑。

## 研究背景

当动作识别模型从源域迁移至目标域时，空间外观与时间动态的双重不匹配引发严重的分布偏移。这种偏移不仅源于光照或视角变化，更源于背景内容的差异：同一动作（如跑步）在室内与室外场景下，背景静态区域截然不同，却对动作语义无贡献。ViT架构中，每个时空patch被编码为token，自注意力复杂度随token数平方增长。若保留所有token，模型需处理大量无关背景信息，既干扰跨域特征对齐，又造成计算冗余。

主流VUDA方法如UNITE与UDAVT采用全token处理策略，通过掩码建模或信息瓶颈原则对齐源域与目标域表示。然而，这些方法未区分token的信息密度，导致静态背景token持续参与注意力计算，放大域间差异。此外，现有研究极少关注VUDA的计算效率，而实际部署中训练与推理成本是核心瓶颈。本文切入点在于：动作识别的核心信号集中于运动区域，静态背景可被安全丢弃。通过显式过滤低运动token，既能消除背景引起的域偏移，又能降低ViT的计算负载，实现精度与效率的双重提升。

## 核心方法

### 方法参照系

标准VUDA流程将源域与目标域视频统一分词后输入ViT，通过联合损失对齐特征分布。本文问题与该通用流程的关键差异在于：分词阶段引入内容感知的稀疏化机制，而非固定网格划分。传统分词产生固定数量token，无论视频内容如何；LMFT则根据运动强度动态调整token数量，使模型仅处理动作相关区域。

### 运动强度估计与可学习阈值

设计动机：固定阈值无法适应不同动作的运动幅度差异，手动调参成本高且泛化性差。本文计算相邻时间步patch的L1距离作为运动能量，经min-max归一化后得到运动张量 $E_{motion} \in \mathbb{R}^{N_t \times N_x \times N_y}$。token保留条件定义为：

$$
M_{t,x,y} = \mathbb{1}[E_{motion}(t,x,y) > \tau]
$$

其中 $\tau$ 为可学习阈值。该公式物理含义为：仅当某时空位置的运动能量超过阈值时，该token才被保留。$\tau$ 通过策略梯度强化学习优化，策略 $\pi_\theta(\tau)$ 采用logistic-normal分布，参数 $\theta = \{\mu, \log\sigma\}$。奖励函数 $R(\tau)$ 平衡域适应损失与token丢弃率，通过REINFORCE算法更新 $\theta$，使阈值自适应于视频内容。

### 伪标签过滤与联合训练

设计动机：目标域无标签，直接训练易受噪声伪标签干扰。本文利用CLIP零样本生成伪标签，并通过置信度阈值 $\gamma_c$ 过滤低质量样本。仅当目标视频最大类别概率超过 $\gamma_c$ 时，该样本才参与训练。联合损失定义为：

$$
\mathcal{L}_{da} = \mathcal{L}_s + \lambda_t \mathcal{L}_t
$$

其中 $\mathcal{L}_s$ 为源域交叉熵损失，$\mathcal{L}_t$ 为过滤后目标域伪标签损失。该公式物理含义为：源域提供强监督信号，目标域提供弱监督信号，$\lambda_t$ 调节两者权重。LMFT模块在训练过程中同步优化，其阈值 $\tau$ 的更新独立于ViT参数 $\phi$，通过奖励信号驱动。

## 实验评估

实验在Daily-DA、UCF-HMDBfull与ActorShift三个基准上进行，覆盖21种域适应设置。基线包括UNITE、UDAVT、DALL-V等SOTA方法，以及ToMe、PruMerge等token缩减技术。本文方法在Daily-DA上达到96.4% Top-1准确率，较UNITE的91.0%提升5.4%；在UCF-HMDBfull上达到88.4%，较UNITE的76.4%提升12.0%；在ActorShift上超越Target Only基线7.3%。

| 基准 | 方法 | Top-1 Accuracy (%) |
| :--- | :--- | :--- |
| Daily-DA | UNITE [22] | 91.0 |
| Daily-DA | Ours | 96.4 |
| UCF-HMDBfull | UNITE [22] | 76.4 |
| UCF-HMDBfull | Ours | 88.4 |

消融实验显示，移除LMFT后性能显著下降，证明运动聚焦分词的核心贡献。置信度阈值 $\gamma_c=0.8$ 时性能最优，过高或过低均导致性能衰退。训练效率方面，LMFT将训练时间从UNITE的27426秒降至2784秒，推理GFLOPs从358降至217，计算成本降低约40%。与Gumbel-Softmax相比，RL优化阈值在精度与内存消耗上均更优。

评估边界方面，论文未报告置信区间，数值比较需谨慎。代码未公开，但提供了详细超参数设置（$\gamma_c=0.8, \lambda_t=0.5, \lambda_L=10$）。GPU使用NVIDIA L40与RTX A6000，Flash Attention加速。可复现性受限于未公开代码与部分基线结果来自第三方运行。

## 关联研究分析

从问题动机看，LMFT与TrackMAE同属运动感知路线，但TrackMAE依赖外部轨迹监督信号，而LMFT仅利用帧间像素差异，无需额外数据。这一差异源于任务特性：VUDA中目标域无标签，无法获取轨迹标注，故必须依赖自监督运动估计。然而，帧间差异对缓慢动作或复杂背景下的细微运动可能不敏感，论文未验证此类场景下的鲁棒性。

从方法设计看，LMFT与ToMe、PruMerge等通用token缩减方法不同，后者基于相似度或注意力分数合并token，而LMFT基于运动强度丢弃token。ToMe在VUDA中精度低于LMFT（72.5% vs 74.2%），且推理吞吐量更低（1.8 vs 3.9 Clips/s）。这一差异表明，通用token缩减未考虑域适应中背景干扰的特殊性，而运动聚焦策略更契合动作识别的语义需求。但LMFT的阈值 $\tau$ 为全局标量，未区分不同动作类别的运动特性，是否导致某些低运动动作（如静坐）的token被过度丢弃，论文未给出分析。

## 总结

本文解决的核心矛盾是VUDA中背景域偏移与计算效率的冲突。现有方法通过全token处理对齐特征，但静态背景既干扰语义迁移又浪费算力；LMFT通过可学习运动阈值显式过滤背景，使模型聚焦动作区域。该方法在Daily-DA上达到96.4%准确率，训练时间较UNITE缩短10倍。其边界在于依赖CLIP伪标签质量，且全局阈值 $\tau$ 未适配不同动作的运动幅度差异。当目标域包含大量低运动动作时，固定阈值是否导致关键token丢失，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.09955)