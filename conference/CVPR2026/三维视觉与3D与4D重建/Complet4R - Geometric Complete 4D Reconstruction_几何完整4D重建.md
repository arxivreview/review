# CVPR2026最新论文 ｜Complet4R: Geometric Complete 4D Reconstruction ｜几何完整4D重建

研究机构：清华大学

作者：Weibang Wang、Kenan Li、Zhuoguang Chen 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.27300)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.27300)

> 动态场景重建长期受困于单帧视角的几何缺失，运动物体在目标帧中被遮挡的部分无法恢复，导致时空表示碎片化。现有前馈方法如VGGT仅预测当前帧可见点图，缺乏跨时间维度的几何补全能力。Complet4R通过引入聚合Token机制，将全序列观测向单一目标时间戳聚合，实现包含遮挡区域的完整几何重建。该方法在3D跟踪任务上超越SOTA，但在4D重建新基准上缺乏与优化类方法的直接对比，其泛化边界尚待验证。

## 研究背景

动态4D重建的核心困境在于投影歧义：单个3D点在不同视角下映射到不同像素，而遮挡导致部分几何仅在特定时间步可见。传统运动恢复结构（SfM）依赖刚性假设，将动态区域视为噪声剔除，无法建模非刚性形变。神经辐射场（NeRF）虽引入时间维度，但逐场景优化耗时数小时，且仅重建可见几何，无法恢复被遮挡部分。

前馈式重建范式通过大规模预训练基础模型（如DUSt3R、VGGT）实现了毫秒级推理，但主流方法仍采用成对推理逻辑：每步仅处理两帧，误差沿序列累积，且中间表示（点图或3D流场）以帧为中心，无法直接融合全序列信息形成全局一致的4D结构。St4RTrack虽引入动态跟踪，但其成对对应关系限制了长程预测能力，需锚定每帧后聚合结果，导致计算开销大且一致性差。Complet4R的切入点在于将任务重新定义为“几何完整4D重建”：不是预测每帧的可见点图，而是从全序列观测中聚合信息，重建每个时间步的完整几何，包括在其他帧中可见但在当前帧被遮挡的区域。

## 核心方法

### 前馈Transformer架构参照系

Complet4R基于VGGT的Decoder-only Transformer架构，继承其相机Token、注册Token及DPT风格解码器。与VGGT仅预测当前帧点图不同，本文新增聚合头（Aggregation Head）与聚合Token（Aggregation Token），将任务从“单帧几何预测”扩展为“跨时间几何聚合”。关键差异在于：VGGT的注意力机制在帧内和全局层面交换信息以估计相机位姿和深度，而Complet4R的注意力机制需显式区分目标时间戳与其他时间戳，实现几何信息的定向聚合。

### 聚合Token设计与定向注意力

设计动机：成对推理方法无法解决遮挡区域的几何缺失，因为被遮挡部分在当前帧无观测，需从其他帧获取。Complet4R引入两组聚合Token：$t_{D_a}$ 专用于目标时间戳 $a$，$t_{D_{/a}}$ 共享于所有其他时间戳。这些Token与每帧的视觉Token（由DINOv2嵌入）拼接，使模型能显式识别聚合目标。在帧级和全局注意力阶段，$t_{D_a}$ 与 $t_{D_{/a}}$ 通过自注意力交互，逐步将所有帧的特征对齐至目标帧，整合过去与未来的观测。该机制解决了成对方法中“每步仅看两帧”的短视问题，使模型能从全序列中提取互补几何，重建单帧不可见的区域。

### 焦点加权点损失与绝对坐标监督

设计动机：动态区域点分布不平衡，传统均匀监督导致模型忽略高难度动态点。Complet4R引入焦点加权点损失（Focal-Weighted Point Loss），对预测点 $\hat{P}_{a,i}$ 与真值 $P_{a,i}$ 的对齐误差进行自适应加权：

$$
\mathcal{L}_{\text{focal}} = \sum_{i} w_i \cdot \| \hat{P}_{a,i} - P_{a,i} \|_2^2, \quad w_i = (1 - \sigma_i)^{\gamma}
$$

其中 $\sigma_i$ 为预测不确定性，$\gamma$ 为焦点参数。该损失增加对大误差点的监督权重，提升动态区域鲁棒性。同时，采用绝对坐标（Endpoint）而非相对偏移（Offset）作为聚合表示，确保重建几何在统一坐标系下的全局一致性。消融实验表明，焦点损失比动态加权损失在Accuracy上提升0.03（0.50 vs 0.47），Endpoint比Offset在Completion上提升0.29（0.26 vs 0.50），验证了设计选择的有效性。

## 实验评估

实验在SAIL-VOS 3D-test（44个序列）和WorldTrack（含Point Odyssey、Dynamic Replica等）上进行。基线包括St4RTrack（成对跟踪）、MonST3R（前馈重建）和SpaTracker（稀疏跟踪），但缺乏4DGS类优化方法（如4DGS、MoRel）及VGGT4D的直接对比，限制了前馈范式与优化范式在几何精度上的公平比较。

| 方法 | Acc. Mean ↓ | Complet. Mean ↓ | N.C. Mean ↑ |
|---|---|---|---|
| St4RTrack-seq | 0.92 | 3.10 | 0.48 |
| St4RTrack-pairs | 0.94 | 2.67 | 0.46 |
| Complet4R (Ours) | 0.50 | 0.26 | 0.49 |

Complet4R在Accuracy上较St4RTrack-seq提升45.7%（0.50 vs 0.92），Completion提升91.6%（0.26 vs 3.10），表明其在全局几何完整性上显著优于成对方法。

| 变体 | Acc. Mean ↓ | Complet. Mean ↓ | N.C. Mean ↑ |
|---|---|---|---|
| Dynamic Loss | 0.47 | 0.20 | 0.48 |
| Offset Repre. | 0.63 | 0.50 | 0.44 |
| Add Token | 0.57 | 0.32 | 0.50 |
| Complet4R (Ours) | 0.50 | 0.26 | 0.49 |

消融显示，Endpoint表示比Offset在Completion上提升48%（0.26 vs 0.50），Concatenate Token比Add在N.C.上提升1.0%（0.49 vs 0.50），但Acc.下降12.3%（0.50 vs 0.57），表明Token融合方式对精度与一致性存在权衡。

评估边界：SAIL-VOS基准缺乏与优化类方法的对比，无法证明前馈范式在几何精度上优于优化范式；WorldTrack跟踪任务中，Complet4R未专门训练，仅作为重建副产品评估，其跟踪性能上限未知；代码未公开，超参数（如焦点参数 $\gamma$）未详细报告，可复现性受限。

## 关联研究分析

从问题动机看，Complet4R与St4RTrack的核心差异在于任务定义：St4RTrack聚焦成对跟踪与重建，需后处理聚合，而Complet4R将聚合内嵌于前馈推理，直接输出完整几何。这一差异源于对“几何完整性”的不同理解：St4RTrack认为完整几何是可见部分的拼接，Complet4R认为完整几何需包含遮挡区域，后者更符合物理世界的时空连续性。根源在于St4RTrack的成对架构无法全局正则化，而Complet4R的全局注意力机制提供了跨时间约束。

从方法设计看，Complet4R与VGGT共享Transformer骨干，但VGGT仅预测当前帧点图，Complet4R新增聚合头实现跨时间聚合。这一差异源于任务需求：VGGT面向静态场景，无需处理遮挡，而Complet4R面向动态场景，需从其他帧补全当前帧缺失几何。VGGT4D虽也处理动态场景，但其动态-静态解耦依赖显式掩码，而Complet4R通过隐式聚合实现解耦，避免了掩码预测的误差传播。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

Complet4R解决的核心矛盾是动态场景中单帧几何缺失与全序列信息冗余之间的冲突。现有前馈方法如VGGT仅预测可见几何，无法恢复遮挡区域，而Complet4R通过聚合Token机制将全序列观测向目标时间戳聚合，实现了包含遮挡区域的完整几何重建。实验表明，其在SAIL-VOS基准上Accuracy较St4RTrack提升45.7%，Completion提升91.6%，在Point Odyssey跟踪任务上APD达80.17%，超越DINO_4D的78.1%。然而，其边界在于缺乏与4DGS类优化方法的直接对比，无法证明前馈范式在几何精度上的优越性；且聚合Token的计算复杂度随帧数平方增长，长序列扩展性未验证。当序列长度超过Transformer上下文窗口时，聚合机制是否仍能保持全局一致性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.27300)