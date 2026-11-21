# HuggingFace最新推荐论文 ｜Pixel-level Scene Understanding in One Token: Visual States Need What-is-Where Composition ｜像素级场景构图学习：单一瓶颈Token的视觉状态表示

作者：Seokmin Lee、Yunghee Lee、Byeonghyun Pak 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.13904)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.13904)

> 动态环境中的机器人代理需要从视频流构建支持序列决策的内部状态，但现有自监督方法未明确该状态应编码何种信息。ToBo等前驱工作通过时间相邻帧重建学习紧凑表示，却忽略了帧内空间结构，导致模型难以捕捉细微的空间位移。本文提出CroBo，通过全局到局部重建目标，强制单一瓶颈Token保留场景的像素级“what-is-where”构图信息。该方法在机器人策略学习任务上取得SOTA，但其单一Token架构在密集多对象场景下的解耦能力存疑。

## 研究背景

机器人代理在动态环境中执行任务时，必须将原始视觉观测压缩为紧凑的内部状态以支持决策。这种状态表示需同时保留场景元素的语义身份与精确空间位置，即“what-is-where”构图，才能检测物体间的细微位移与交互。若表示仅编码全局语义而丢失空间细节，模型将无法区分“物体A在左”与“物体A在右”的细微差异，导致决策失效。

视觉状态表示学习（State Representation Learning, SRL）旨在解决这一挑战。ToBo（Kim et al., 2024）引入瓶颈Token，通过重建时间相邻帧的掩码区域来学习时序感知表示，但在帧内空间结构建模上存在盲区。CropMAE（Li et al., 2023）虽通过静态图像的全局-局部裁剪学习对应关系，但其补丁级对应机制无法生成单一紧凑帧表示，难以直接用于机器人控制。现有方法要么侧重时序对应而忽略空间构图，要么侧重空间对应而缺乏紧凑性，导致在需要同时理解“什么在动”与“动到哪里”的动态任务中表现受限。

## 核心方法

### 方法参照系

CroBo基于Siamese掩码自编码器架构，与MAE（He et al., 2022）共享编码器-解码器框架，但关键差异在于：MAE重建同一帧的掩码区域，CroBo则利用全局源视图的瓶颈Token重建局部目标视图的掩码区域，将空间构图学习嵌入重建目标。

### 全局到局部重建目标

传统SRL方法如ToBo使用时间相邻帧作为重建目标，导致瓶颈Token主要编码时序变化而非空间构图。CroBo将重建目标改为从全局源视图裁剪出的局部目标视图，迫使模型推断裁剪区域在场景中的位置及内容。设全局源视图为 $\mathbf{x}_g$，局部目标视图为 $\mathbf{x}_l$，掩码比例为 $r$，则损失函数为：

$$
\mathcal{L} = \frac{1}{|M|} \sum_{i \in M} \| \hat{\mathbf{x}}_l^i - \mathbf{x}_l^i \|^2
$$

其中 $M$ 为掩码补丁索引集，$\hat{\mathbf{x}}_l^i$ 为重建值。该设计使瓶颈Token必须保留场景全局空间构图，而非仅时序信息。

### 高掩码率与瓶颈约束

CroBo采用90%掩码率，高于MAE的75%，防止目标视图仅从可见Token重建。瓶颈Token $z_{g}^{cls}$ 作为唯一全局上下文输入解码器，其信息容量受限，迫使模型将“what-is-where”信息压缩至单一向量。这一约束解决了ToBo中瓶颈Token可能编码冗余时序特征的问题，确保表示聚焦于空间构图。

## 实验评估

CroBo在Kinetics-400上预训练ViT-S/16，冻结骨干后训练MLP策略头，评估于Franka Kitchen与DMC基准。基线覆盖MAE、DINO、DINOv2、SiamMAE、CropMAE、RSP、ToBo，但未包含OCRL专用方法如Slot Attention变体。

| 模型 | Franka Kitchen (Knob on) | Franka Kitchen (Micro open) | DMC (reacher/easy) |
| :--- | :--- | :--- | :--- |
| ToBo | 44.8±9.3 | 89.6±3.8 | 68.5±0.7 |
| CroBo | 65.6±3.7 | 64.8±4.4 | 95.8±2.1 |

CroBo在Franka Kitchen的Micro open任务上较ToBo提升13.6%，在DMC的reacher/easy任务上提升8.3%，验证了空间构图表示对动态决策的有效性。

消融实验显示，掩码率从75%提升至90%时，Franka Kitchen平均成功率从35.0%升至50.4%，表明高掩码率对空间构图学习至关重要。目标视图构建中，使用空间裁剪而非时间裁剪，Knob on任务成功率从44.4%升至57.6%，证实空间构图优于时序对应。

评估边界：实验仅覆盖模拟环境，缺乏真实世界视频验证；未报告计算效率；未与OCRL标准分割指标（如mIoU）对比，无法直接证明其优于多槽位方法。

## 关联研究分析

从问题动机看，CroBo与ToBo均解决视觉状态表示学习，但ToBo聚焦时序对应，CroBo聚焦空间构图。这一差异源于任务特性：机器人操作需精确空间定位，而时序预测仅需相对变化。CroBo的全局-局部裁剪机制借鉴CropMAE，但引入瓶颈Token约束，解决了CropMAE无法生成单一紧凑表示的问题。

从方法设计看，CroBo与OCRL方法如Slot Attention（Locatello et al., 2020）均旨在结构化场景表示，但Slot Attention使用多槽位并行解码，CroBo使用单一Token。这一差异暗示：单一Token在复杂多对象场景中可能面临信息瓶颈，而多槽位方法通过离散解耦避免此问题。CroBo未验证其在密集遮挡场景下的表现，单一Token是否足以编码多对象独立身份，论文未给出回答。

## 总结

CroBo解决的核心矛盾是视觉状态表示需同时编码语义身份与空间位置以支持动态决策。现有方法如ToBo侧重时序对应而忽略空间构图，CroBo通过全局到局部重建目标，强制单一瓶颈Token保留像素级“what-is-where”信息。实验显示，CroBo在Franka Kitchen Micro open任务上较ToBo提升13.6%，在DMC reacher/easy任务上提升8.3%。其边界在于：单一Token架构在密集多对象场景下的解耦能力未验证，且缺乏真实世界视频评估。当场景包含多个重叠物体时，单一瓶颈Token是否仍能保留各物体的独立空间位置，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.13904)