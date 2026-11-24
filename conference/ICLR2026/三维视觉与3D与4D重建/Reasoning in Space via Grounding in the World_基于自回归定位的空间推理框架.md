# ICLR2026最新论文 ｜Reasoning in Space via Grounding in the World ｜基于自回归定位的空间推理框架

研究机构：西湖大学、浙江大学

作者：Yiming Chen、Zekun Qi、Wenyao Zhang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.13800)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.13800)

> 视觉空间智能旨在让模型从2D图像或视频中推断3D空间布局、物体尺寸及位置关系，以支撑具身智能与自动驾驶。现有3D大语言模型（3D LLM）在空间推理时往往依赖外部检测器或预训练解码器进行3D视觉定位，导致定位与推理过程割裂，且难以在自回归生成中自然整合几何信息。GS-Reasoner 提出了一种语义-几何混合3D场景表示，通过双路径池化机制将点云几何特征与图像语义特征在Patch粒度对齐，使模型无需外部模块即可自回归地生成3D边界框，并将其作为思维链（Chain-of-Thought, CoT）的中间步骤参与后续推理。该框架在3D定位任务上取得了超越依赖外部模块方法的性能，但在综合空间推理基准上仍落后于最新SOTA，其定位优势向推理优势的转化效率存疑。

## 研究背景

当3D LLM尝试回答“沙发距离电视多远”这类问题时，它首先需要准确识别场景中的“沙发”和“电视”在3D空间中的具体位置。这一将文本描述映射到3D物体坐标的过程称为3D视觉定位（3D Visual Grounding）。然而，早期模型如3D-LLM（Hong et al., 2023a）使用Q-Former压缩点云特征，虽降低了Token数量，却牺牲了几何保真度，导致定位精度受限。为弥补这一缺陷，后续工作如Chat-Scene（Huang et al., 2024）引入了外部检测器生成候选框，再由LLM进行选择，但这种“检测-选择”的两阶段架构不仅增加了系统复杂度，更使得定位误差无法在推理过程中被动态修正，阻碍了定位与推理的深度融合。

3D空间推理的核心瓶颈在于模型缺乏统一的表示来同时捕获语义信息与几何结构。纯语义特征缺乏深度线索，而纯几何特征（如点云）缺乏语义上下文，且点云数据稀疏、标注稀缺，使得直接建模困难。现有3D VQA数据集（如ScanQA, SQA3D）仅提供短答案，缺乏定位标注与推理步骤，无法训练模型建立“先定位、后推理”的认知路径。GS-Reasoner 的切入点在于重构3D场景表示，将定位从独立任务转化为推理的中间步骤，并通过构建包含定位标注的思维链数据集，强制模型在生成答案前显式地输出相关物体的3D边界框，从而在自回归框架内实现定位与推理的闭环。

## 核心方法

### 方法参照系

3D LLM的标准流程通常包含点云编码、特征对齐与LLM解码三个阶段。传统方法如3D-LLM使用Q-Former将点云特征投影至LLM空间，或采用体素化表示以平衡效率与保真度。本文的关键差异在于摒弃了Q-Former等压缩模块，转而设计了一种在图像Patch粒度上融合语义、几何与位置信息的混合表示，使得LLM能够直接自回归地预测3D坐标，而非从外部候选集中选择。

### 语义-几何混合3D场景表示

传统点云编码器在处理整个点云时，通过序列化注意力捕获全局上下文，但导致Patch内的几何特征与语义特征错位。GS-Reasoner 提出双路径池化（Dual-Path Pooling）机制，在Patch级别对齐异构信号。首先，利用交叉注意力网络，以Patch的语义特征为Query，Patch内K个几何特征为Key和Value，生成语义对齐的几何特征，解决语义-几何错位问题。其次，采样Patch中心像素对应的3D点坐标，基于该位置插值几何特征，获得位置对齐的几何特征，解决位置-几何错位。最终，将语义对齐与位置对齐的几何特征拼接，并与投影后的语义特征及3D位置编码融合，形成统一的混合特征。

$$
\mathbf{f}_{geo}^{aligned} = \text{CrossAttn}(\mathbf{f}_{sem}, \mathbf{F}_{geo}^{patch}), \quad \mathbf{f}_{geo}^{pos} = \text{Interp}(\mathbf{F}_{geo}^{patch}, \mathbf{p}_{center})
$$

$$
\mathbf{h}_{patch} = \text{Proj}([\mathbf{f}_{sem}; \mathbf{f}_{geo}^{aligned}; \mathbf{f}_{geo}^{pos}; \mathbf{e}_{pos}])
$$

该设计通过局部注意力机制，确保几何特征仅响应与当前Patch语义相关的点云结构，同时通过中心点插值保证位置编码与几何特征的空间一致性，从而在不增加输入Token数量的前提下，显著提升了自回归定位的精度。

### Grounded Chain-of-Thought 数据集构建

现有空间推理数据集缺乏定位标注，导致模型无法学习“定位-推理”的因果链。GS-Reasoner 构建了GCoT数据集，包含156k个QA对，其中79%包含CoT标注。数据集构建流程为：首先基于ScanNet、ScanNet++和ARKitScenes生成空间QA对并保留物体边界框信息；随后，利用GPT-4o结合鸟瞰图、物体信息及QA对，生成包含3D边界框坐标的推理路径。

$$
\text{Output} = \text{think}(\text{Analysis}) + \sum_{i=1}^{N} \text{OBJECT}_i \text{bbox}(x_1, y_1, z_1, x_2, y_2, z_2) + \text{think}(\text{Reasoning}) + \text{answer}(\text{Final})
$$

该格式强制模型在输出最终答案前，显式地列出所有相关物体的3D边界框。这种结构化监督不仅提供了比短答案更丰富的几何信号，还使推理过程可解释，符合人类“先识别物体，再判断关系”的认知模式。

## 实验评估

实验在ScanRefer、Multi3DRef、SR3D、NR3D、VSI-Bench、ScanQA、SQA3D等基准上进行。基线覆盖专家模型、依赖网格点云提案的3D LLM、依赖外部定位模块的3D LLM及纯自回归3D LLM四类。GS-Reasoner 在ScanRefer Acc@25上达到60.8%，超越依赖外部模块的LLaVA-3D（54.1%）和纯自回归的3D-LLM（30.3%），但略低于依赖网格提案的SeeGround（58.1%）在Multi3DRef F1@25上的表现。在VSI-Bench上，使用预测深度时平均得分为64.7%，使用真实深度时提升至70.1%，超越VLM-3R（60.9%）和Spatial-MLLM（48.4%），但低于领域综述中提到的SpaceMind等最新SOTA（82.91%）。

| 方法 | ScanRefer Acc@25 | Multi3DRef F1@25 | VSI-Bench Avg (pred dep.) | VSI-Bench Avg (gt dep.) |
|---|---|---|---|---|
| 3D-LLM | 30.3 | - | - | - |
| LLaVA-3D | 54.1 | - | - | - |
| SeeGround | 58.1 | 58.0 | - | - |
| VLM-3R | - | - | 60.9 | - |
| GS-Reasoner | 60.8 | 61.7 | 64.7 | 70.1 |

消融实验表明，双路径池化中的交叉注意力与位置插值对定位精度贡献显著。移除数据增强和位置编码后，ScanRefer Acc@25从60.8%降至0.0%（LLaVA-NeXT基线）或15.4%（Video-3D LLM）。在GCoT机制消融中，使用完整CoT训练的GS-Reasoner在VSI-Bench平均得分上比无CoT版本高13.8分，其中Relative Direction任务提升28.2分，表明定位作为中间步骤对复杂空间关系推理至关重要。

评估边界方面，GS-Reasoner 在SQA3D上的EM准确率为30.1%，低于领域综述中提到的CVP等方法的47.2%，表明其在场景级问答上的泛化能力有限。论文未报告计算效率指标，且依赖深度图输入，在纯2D视频场景下的鲁棒性未充分验证。代码与模型权重已开源，但GCoT数据集的构建依赖GPT-4o，可能存在生成偏差。

## 关联研究分析

从问题动机看，GS-Reasoner 与SR-3D（Cheng et al., 2025）均致力于消除外部定位模块，但SR-3D通过共享视觉令牌空间连接2D图像与3D数据，侧重于多视图视频输入下的跨帧对应，而GS-Reasoner 聚焦于单视图或短序列下的语义-几何对齐。GS-Reasoner 的双路径池化机制在Patch粒度上解决了点云稀疏导致的特征错位问题，而SR-3D 依赖3D位置嵌入注入2D特征，几何线索相对较弱。这种差异源于任务特性：GS-Reasoner 强调定位精度以支撑推理，而SR-3D 强调多视图一致性以支撑长程记忆。

从方法设计看，GS-Reasoner 与SpatialVLM（Guo et al., 2025）在数据驱动范式上存在分歧。SpatialVLM 利用大规模合成数据微调VLM，使其隐式学习空间关系，但缺乏显式定位步骤，导致推理不可解释。GS-Reasoner 通过GCoT数据集显式引入定位标注，将定位转化为CoT中间步骤，提升了可解释性，但牺牲了部分泛化性，表现为在SQA3D等开放域问答任务上性能落后。这种取舍反映了“隐式端到端学习”与“显式几何表示”之间的核心争论：GS-Reasoner 选择了显式路径，以定位精度换取推理的可控性，但在复杂场景下的鲁棒性是否优于隐式方法，论文未给出直接对比。

## 总结

GS-Reasoner 旨在解决3D LLM中定位与推理割裂的问题，通过语义-几何混合表示与GCoT数据集，实现了无外部模块的自回归定位，并将其作为推理的中间步骤。该方法在ScanRefer上达到60.8%的Acc@25，在VSI-Bench上使用真实深度时平均得分70.1%，验证了定位对空间推理的增益。然而，其在SQA3D上的30.1% EM准确率远低于领域SOTA，且VSI-Bench成绩落后于SpaceMind等最新方法，表明其定位优势尚未完全转化为综合推理优势。当输入深度图存在噪声或缺失时，双路径池化机制的鲁棒性如何，以及显式定位步骤在开放域动态场景中的泛化边界，仍是该框架面临的具体挑战。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.13800)