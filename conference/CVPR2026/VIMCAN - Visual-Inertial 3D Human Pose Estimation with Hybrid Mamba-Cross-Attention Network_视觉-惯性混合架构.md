# CVPR2026最新论文 ｜VIMCAN: Visual-Inertial 3D Human Pose Estimation with Hybrid Mamba-Cross-Attention Network ｜视觉-惯性混合架构

研究机构：北京航空航天大学、中国科学院

作者：Zepeng Yang、Junxuan Bai、Hao Li 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.07552)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.07552)

> 视觉-惯性3D人体姿态估计旨在融合RGB关键点与惯性测量单元（IMU）数据以消除单目深度歧义，但现有Transformer骨干因二次方计算复杂度难以满足长序列实时处理需求。本文切入点在于利用Mamba的线性复杂度优势弥补时序建模效率瓶颈，同时保留Cross-Attention的空间推理能力以克服纯Mamba在跨模态融合中的表达局限。通过构建骨架感知扫描机制与混合融合模块，VIMCAN在TotalCapture数据集上实现了17.2mm的MPJPE，同时保持60FPS以上的推理速度。该架构在精度与效率间取得了显著平衡，但其对严格传感器标定的依赖限制了在动态无约束场景下的泛化能力。

## 研究背景

单目图像投影丢失深度信息，导致2D关键点到3D姿态的映射存在固有歧义。引入IMU数据可提供高频、低延迟的动态旋转信息，与视觉模态形成互补，从而约束深度不确定性。然而，多模态融合要求模型同时处理异构数据的时空对齐与特征交互，这对骨干网络的表达能力与计算效率提出了双重挑战。

主流视觉-惯性融合方法依赖Transformer架构，利用Cross-Attention机制建模跨模态依赖。Wang et al. (2024)提出的GCN-Transformer混合架构通过运动学先验分组实现了鲁棒融合，但其注意力机制的计算复杂度随序列长度$L$呈$O(L^2)$增长，导致长序列推理时内存占用急剧上升，难以部署于资源受限设备。Mamba架构通过选择性状态空间模型将复杂度降至$O(L)$，解决了效率瓶颈，但实证研究表明纯Mamba在捕捉复杂空间依赖方面弱于卷积或注意力机制，导致其在需要精确空间建模的多模态任务中表现受限。

VIMCAN针对这一矛盾，提出混合架构以结合Mamba的时序效率与Cross-Attention的空间推理能力。该设计旨在保留多模态融合精度的同时，突破Transformer在长序列处理中的计算瓶颈，实现实时变长序列推理。

## 核心方法

### 方法参照系

视觉-惯性3D姿态估计的标准流程包括特征提取、多模态融合与姿态回归。传统方法采用Transformer进行跨模态融合，但本文问题与该通用流程的关键差异在于：需在保持跨模态空间交互精度的前提下，将时序建模复杂度从二次方降至线性，以支持长序列实时处理。

### 骨架感知时空Mamba模块

在特征提取阶段，视觉与惯性数据分别通过STMamba模块处理。设计动机在于：纯Mamba的扫描顺序若未考虑人体骨架拓扑，会丢失关节间的运动学先验，导致空间结构建模失效。VIMCAN引入骨架感知扫描策略，在空间前向扫描时依据父子关节关系重排关键点顺序，将运动学先验嵌入SSM扫描路径。对于视觉特征$F_V$，空间扫描输出通过深度卷积与SiLU激活增强局部交互，公式为：

$$ F_{x,ssm} = \text{LN}(\text{SS2D}(\sigma(\text{DWConv}(F_x)))) $$

其中$\sigma$为SiLU激活函数，$\text{SS2D}$为双向时空选择性扫描。该设计使模型在保持线性复杂度的同时，显式编码了关节间的拓扑依赖，弥补了纯Mamba在空间结构感知上的不足。

### 跨模态Cross-Attention融合

在融合阶段，视觉特征作为Query，惯性特征作为Key和Value，通过多头Cross-Attention（MHCA）进行跨模态交互。设计动机在于：Mamba的选择性机制为效率牺牲了部分表达容量，导致跨模态空间依赖捕捉能力下降，而Cross-Attention能聚合所有Token信息，适合捕捉异构模态间的复杂空间关系。对于每个身体部位组$g$，融合特征$Z_g$通过全连接层降维后拼接为全局表示，公式为：

$$ Z_g = \text{FC}(\text{MHCA}(Q_V^g, K_I^g, V_I^g)) $$

其中$Q_V^g$、$K_I^g$、$V_I^g$分别为视觉Query与惯性Key/Value。该模块在Mamba时序建模后插入，专门负责跨模态空间对齐，解决了纯Mamba在融合环节的信息损失问题，使模型能同时利用IMU的动态约束与视觉的空间细节。

## 实验评估

实验在TotalCapture与3DPW数据集上进行，对比基线包括RNN、TCN、CNN-Transformer及GCN-Transformer方法，覆盖了主流融合路线，但缺失纯Mamba基线在TotalCapture上的直接对比。

| 方法 | 2D检测器 | #IMUs | P1 (mm) | P2 (mm) |
| :--- | :--- | :--- | :--- | :--- |
| Wang's [29] | SN | 6 | 34.9 | 26.9 |
| VIMCAN | SN | 6 | 31.2 | 23.6 |
| Wang's [29] | GT | 6 | 28.6 | 17.6 |
| VIMCAN | GT | 6 | 17.2 | 13.8 |

在SimpleNet 2D输入下，VIMCAN的P1为31.2mm，优于Wang et al.的34.9mm；在Ground-Truth 2D输入下，VIMCAN的P1降至17.2mm，较Wang et al.的28.6mm降低11.4mm，表明多模态融合在消除2D检测噪声方面具有显著优势。

| 配置 | P1 (mm) | #Params. | Peak (MB) | FPS |
| :--- | :--- | :--- | :--- | :--- |
| Wang's [29] | 34.9 | 7.3M | 969.8 | 45.8 |
| VIMCAN-B | 31.2 | 12.3M | 282.5 | 61.4 |
| VIMCAN-T | 34.5 | 3.9M | 156.4 | 71.1 |

消融实验显示，变长训练策略（V）的P1为18.9mm，接近固定长度81帧的最优结果17.2mm，验证了策略的稳定性。在融合策略对比中，视觉-only PoseMamba的P1为28.1mm，加入Self-Attention后降至26.9mm，而VIMCAN的Cross-Attention融合达到17.2mm，证明跨模态融合带来的9.7mm精度提升远超单模态注意力增强。

评估指标涵盖MPJPE、Procrustes对齐MPJPE、参数量、峰值内存与FPS，指标完备。但3DPW实验使用合成IMU数据，可能高估真实场景下的鲁棒性。代码已开源，超参数与训练细节完整披露，可复现性高。

## 关联研究分析

从方法设计看，VIMCAN与SasMamba同属Mamba架构路线，但SasMamba专注单目视觉，通过固定空间时间扫描策略保留骨架结构，而VIMCAN将扫描策略拓展至多模态场景，并引入Cross-Attention弥补Mamba的空间推理短板。差异根源在于任务特性：单目任务中深度歧义主要依赖时序平滑与先验正则化，而视觉-惯性任务中IMU提供了额外的动态约束，需要更强的跨模态空间交互能力，纯Mamba的线性扫描难以充分捕捉这种异构模态间的复杂依赖。

从问题动机看，VIMCAN与Wang et al.的GCN-Transformer架构解决相同的多模态融合问题，但后者依赖Transformer的二次方注意力，前者采用Mamba-Cross-Attention混合架构。VIMCAN在TotalCapture上将峰值内存从969.8MB降至282.5MB，FPS从45.8提升至61.4，证明混合架构在效率上的优势。然而，VIMCAN对传感器标定的依赖比Wang et al.更严格，后者通过运动学先验分组在一定程度上缓解了对精确标定的需求，而VIMCAN的骨架感知扫描策略直接依赖关节拓扑与IMU姿态的精确对齐，这在动态无约束场景中可能成为瓶颈。

## 总结

VIMCAN要解决的核心矛盾是多模态融合中精度与实时性的权衡，现有Transformer方法因二次方复杂度无法兼顾，而纯Mamba方法因空间推理能力不足难以保证融合精度。本文抓住的切入点是Mamba的线性时序效率与Cross-Attention的空间推理能力互补，通过骨架感知扫描与混合融合模块，在TotalCapture上实现了17.2mm的MPJPE与61.4FPS的推理速度。本文的边界在于对严格传感器标定的依赖，骨架感知扫描策略要求IMU姿态与关节拓扑精确对齐，这在动态无约束场景中难以保证。当传感器标定误差超过一定阈值时，骨架感知扫描的空间结构编码是否失效，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.07552)