# CVPR2026最新论文 ｜PromptStereo: Zero-Shot Stereo Matching via Structure and Motion Prompts ｜PromptStereo：基于结构与运动提示的零样本立体匹配

研究机构：华中科技大学

作者：Xianqi Wang、Hao Yang、Hangtian Wang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.01650)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.01650)

> 零样本立体匹配旨在让模型在未见场景下直接输出几何一致的视差图，以解决合成数据训练模型在真实域性能崩塌的问题。现有方法虽利用单目深度基础模型（VFM）提取特征或初始化视差，但迭代细化阶段仍依赖从零训练的GRU，导致VFM先验在关键修正环节失效。本文提出Prompt Recurrent Unit (PRU)，将VFM解码器架构改造为递归单元，并通过结构与运动提示注入立体线索，实现先验继承与立体修正的统一。该方法在多个基准上刷新了零样本泛化精度，但其对极端恶劣天气的鲁棒性仍受限于训练数据分布。

## 研究背景

立体匹配的核心难点在于弱纹理与遮挡区域的匹配歧义，传统局部特征在此类病态区域缺乏唯一性。为突破此局限，领域主流转向迭代优化范式，通过递归更新替代昂贵的3D卷积聚合。然而，当视觉基础模型（VFM）兴起后，研究重心转向零样本泛化，即利用预训练的单目深度先验解决跨域差距。

当前VFM驱动的零样本方法（如MonSter、FoundationStereo）主要将VFM用于特征提取或代价体构建，而迭代细化阶段仍沿用RAFT-Stereo确立的GRU架构。GRU存在三个根本缺陷：其一，GRU独立于VFM，必须从零训练，无法继承VFM的视觉理解能力；其二，GRU隐藏状态范围受限，难以处理极端视差变化；其三，GRU通过直接卷积融合输入与状态，导致原始状态信息扭曲且外部输入被压缩，产生模糊引导。本文的切入点在于重新审视迭代细化阶段，主张该环节应直接继承VFM先验，而非作为独立模块从零学习。

## 核心方法

### 方法参照系

本文基于MonSter架构，共享其特征提取与代价体构建流程。MonSter利用Depth Anything V2提取单目特征，构建几何编码体积（GEV）回归初始视差，随后通过双分支GRU进行迭代细化。本文的关键差异在于替换GRU为PRU，并引入Affine-Invariant Fusion (AIF) 优化初始视差，使迭代过程从“从零学习”转变为“先验引导”。

### Affine-Invariant Fusion (AIF)

AIF解决初始视差缺乏全局几何一致性、而单目深度存在仿射歧义的问题。传统方法直接拼接初始视差与单目深度，导致尺度与偏移不一致。AIF通过归一化操作消除仿射不变性，公式如下：

$$ \hat{d}_M = \frac{d_M - t(d_M)}{s(d_M)}, \quad \hat{d}_0 = \frac{d_0 - t(d_0)}{s(d_0)} $$

其中 $t(\cdot)$ 和 $s(\cdot)$ 分别为均值与标准差归一化。随后，利用初始视差 $d_0$ 对右图特征进行Warping，与左图特征拼接后通过Sigmoid生成置信图 $c$，融合视差 $d_F = c \cdot \hat{d}_M + (1-c) \cdot \hat{d}_0$。这一设计确保初始视差在几何尺度上对齐，为后续迭代提供稳定起点。

### Prompt Recurrent Unit (PRU)

PRU取代GRU，采用DPT解码器架构作为多分辨率递归单元，直接继承VFM预训练权重。其核心创新在于通过提示机制注入立体线索，避免破坏VFM先验。结构提示（SP）计算归一化视差与单目深度的差异，捕捉几何不一致区域：

$$ SP = ConvBlock(Encoder(F_M, \hat{d}_k - \hat{d}_M)) $$

运动提示（MP）编码局部代价体中的立体运动线索：

$$ MP = ConvBlock(Encoder(V_k)) $$

PRU的更新策略移除GRU的重置门，仅保留更新门 $z_k$，且隐藏状态不受范围约束。公式为：

$$ h_k = z_k \cdot h_{k-1} + (1 - z_k) \cdot (h_{k-1} + SP + MP) $$

这一设计允许隐藏状态在更大空间内演化，处理复杂几何结构，同时通过残差连接保持VFM先验的完整性。

## 实验评估

| 数据集 | 方法 | EPE (px) | Bad 2.0 (%) |
| :--- | :--- | :--- | :--- |
| Midd-2021 | MonSter | 1.52 | 13.66 |
| Midd-2021 | PromptStereo | 0.78 | 5.97 |
| Booster | MGStereo | 1.24 | 7.91 |
| Booster | PromptStereo | 0.67 | 3.67 |

实验在KITTI 2012/2015、Middlebury、ETH3D、DrivingStereo及Booster上进行，基线覆盖RAFT-Stereo、IGEV-Stereo、MonSter、BridgeDepth等主流方法。在Midd-2021上，PromptStereo的EPE从MonSter的1.52降至0.78，Bad 2.0从13.66%降至5.97，降幅超过50%。在Booster上，PromptStereo的Bad 2.0为3.67%，显著优于微调过TransScene的MGStereo（7.91%），表明PRU在反射与透明表面等病态区域具有更强的泛化能力。

消融实验显示，PRU+MP已带来显著提速与精度提升，加入SP与AIF后性能进一步改善，但推理时间仅增加0.01秒。移除预训练权重导致性能明显下降，证实VFM先验继承的关键性。将PRU应用于RAFT-Stereo与IGEV-Stereo，均在不增加推理时间的前提下提升精度，验证了PRU的通用性与可插拔性。

评估边界方面，论文未报告FPS或MACs等计算效率指标，仅给出推理时间（秒）。代码已开源，训练使用4张RTX 4090，超参数公开。然而，DrivingStereo雨天子集上PromptStereo的EPE为1.59，高于MonSter的1.38，表明在极端恶劣天气下，PRU的泛化能力仍受限于训练数据分布，未完全解决恶劣天气鲁棒性问题。

## 关联研究分析

从方法设计看，PromptStereo与MonSter的核心差异在于迭代单元的架构选择。MonSter依赖GRU，其隐藏状态更新受限于门控机制，无法有效利用VFM的深层语义信息。PromptStereo采用DPT解码器，其多分辨率架构天然适合视差细化，且预训练权重提供了强大的几何先验。这一差异的根源在于任务特性：立体匹配需要全局几何一致性，而GRU的局部递归更新难以捕捉长程依赖，DPT的全局注意力机制则能更好地处理弱纹理区域的歧义。

从问题动机看，PromptStereo与FoundationStereo同属零样本泛化路线，但侧重点不同。FoundationStereo通过大规模数据训练提升泛化，而PromptStereo通过架构创新（PRU）提升模型对VFM先验的利用率。在Booster数据集上，PromptStereo超越FoundationStereo，表明在数据有限或场景复杂时，架构对先验的利用效率比数据规模更重要。然而，FoundationStereo在KITTI 2012上的EPE为0.68，低于PromptStereo的0.70，暗示在数据充足的标准场景下，大规模数据训练仍具优势。

## 总结

PromptStereo针对零样本立体匹配中迭代细化阶段VFM先验失效的矛盾，提出PRU架构，将VFM解码器改造为递归单元，并通过结构与运动提示注入立体线索。该方法在Midd-2021上将Bad 2.0从13.66%降至5.97%，在Booster上超越微调基线，证明了先验继承与立体修正统一的有效性。然而，论文在DrivingStereo雨天子集上的性能劣于MonSter，暴露了PRU在极端恶劣天气下的鲁棒性局限。当训练数据缺乏极端天气样本时，PRU的几何先验是否仍能引导有效修正，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.01650)