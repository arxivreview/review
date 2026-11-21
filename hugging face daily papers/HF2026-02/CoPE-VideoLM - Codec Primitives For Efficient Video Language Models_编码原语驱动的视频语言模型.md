# HuggingFace最新推荐论文 ｜CoPE-VideoLM: Codec Primitives For Efficient Video Language Models ｜编码原语驱动的视频语言模型

研究机构：美国斯坦福大学、瑞士苏黎世联邦理工学院

作者：Sayan Deb Sarkar、Rémi Pautrat、Ondrej Miksik 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.13191)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.13191)

> 长视频理解面临上下文窗口限制与视觉Token爆炸的物理矛盾，现有方法通过均匀采样或后处理压缩缓解，但牺牲了时序覆盖密度或引入额外计算开销。CoPE-VideoLM 的切入点在于利用视频编码器（Codec）原生的运动向量与残差结构，直接替代冗余的RGB帧编码。该方法通过轻量级双分支编码器将P帧压缩为极少量Token，在保持时序顺序的同时大幅降低延迟。其价值在于证明了编码域信息足以支撑高质量视频理解，但在极端稀疏证据任务上的表现仍存疑。

## 研究背景

视频语言模型（VideoLMs）处理长视频时，必须将海量视觉帧压缩至有限的上下文窗口内。这一过程通常涉及关键帧采样，即从原始视频流中选取部分帧作为输入。然而，均匀采样策略在长视频中效率低下，既可能遗漏宏观事件，也可能丢失微观动作细节。更严重的是，将每个关键帧作为完整图像编码会产生大量冗余Token，显著增加预填充时间，导致首Token延迟（Time-to-First-Token, TTFT）过高，无法满足实时交互需求。

当前主流路线分为两类：一是扩展上下文窗口或采用动态帧选择，如LLaVA-Video固定采样64帧，但信息量不随视频时长线性增长；二是Token压缩技术，如Q-Former或注意力剪枝，但这些方法仍基于解码后的RGB帧，未利用视频编码过程中已存在的结构化冗余。视频编码器（如MPEG-4、H.264）通过I帧（关键帧）和P帧（预测帧）组织数据，P帧仅存储相对于前帧的运动向量和残差，天然具备稀疏性。CoPE-VideoLM 抓住这一被忽略的结构，直接编码编码原语而非解码后的像素，从而在源头消除冗余。

## 核心方法

### 编码原语Token化框架

传统VideoLMs将视频视为RGB帧序列，每帧独立编码为密集Token。CoPE-VideoLM 改变这一范式，利用GOP（图像组）结构，仅对I帧使用标准视觉编码器生成密集Token，而对P帧使用轻量级Δ-Encoder生成紧凑Token。I帧Token $X^I_t$ 由冻结的视觉编码器 $\phi_{RGB}$ 产生：

$$ X^I_t = \phi_{RGB}(I_t) \in \mathbb{R}^{M \times d} $$

其中 $M$ 为Token数量，$d$ 为维度。P帧不经过RGB解码，而是直接处理运动向量 $\tau_t$ 和残差 $\delta_t$，生成 $N \ll M$ 个Δ-Token。这种设计动机在于：P帧仅包含增量信息，全量RGB编码是计算浪费，而编码原语天然稀疏，可直接映射为低维表示。

### 双分支Δ-Encoder与预训练对齐

Δ-Encoder 采用双分支结构处理P帧信息。运动向量分支通过多层感知机提取局部特征，再经运动Transformer压缩为 $K_\tau$ 个Token；残差分支通过ResNet-18提取特征，经残差Transformer压缩为 $K_\delta$ 个Token。最终Δ-Token为两者拼接：

$$ X^P_t = [\tau^{tok}_t; \delta^{tok}_t] \in \mathbb{R}^{N \times d}, \quad N = K_\tau + K_\delta $$

为确保Δ-Token与I帧Token在同一语义空间，论文引入预训练阶段。预训练目标是通过参考Transformer和扭曲Transformer，利用运动向量扭曲参考帧特征，再叠加残差，使其逼近真实P帧的RGB特征。损失函数为逐块回归：

$$ \mathcal{L} = \| \hat{X}^P_t - \phi_{RGB}(\hat{I}_t) \|_2^2 $$

其中 $\hat{I}_t$ 为重构帧。这一设计解决了编码域特征与视觉编码器特征空间不一致的问题，使P帧Token能无缝插入I帧Token序列，无需修改LLM架构。

## 实验评估

实验基于LLaVA-Video-7B基座，在14个基准上评估，涵盖通用问答、时序推理、长视频理解和空间场景理解。基线包括LLaVA-Video不同采样率设置（1/2/4/64关键帧）及开源模型。论文未直接对比Video-o3、LongVT等代理式方法，也未报告VideoMME具体分数，仅声称“匹配或超越开源模型”。

| 模型 | 采样策略 | PerceptionTest Acc. (%) | NextQA Acc. (%) | ActNet-QA Acc. (%) | Token占比 (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| LLaVA-Video | 1 keyframe/GOP | 60.4 | 77.9 | 61.7 | 5.3 |
| **CoPE-VideoLM** | +7 P-frames/GOP | **65.5** | **78.3** | **62.3** | **6.9** |
| LLaVA-Video | 2 keyframes/GOP | 62.1 | 79.2 | 62.9 | 9.7 |
| **CoPE-VideoLM** | +6 P-frames/GOP | **68.7** | **80.4** | **63.6** | **11.3** |
| LLaVA-Video | 4 keyframes/GOP | 63.6 | 80.5 | 63.6 | 18.6 |
| **CoPE-VideoLM** | +4 P-frames/GOP | **70.3** | **82.1** | **64.8** | **20.1** |
| LLaVA-Video | 64 keyframes total | 67.9 | 83.2 | 64.1 | 100 |

在PerceptionTest上，CoPE-VideoLM 使用仅20.1%的Token，准确率70.3%，超过LLaVA-Video 64关键帧设置的67.9%。在NextQA上，以11.3%的Token达到80.4%，接近基线83.2%的水平。这表明编码原语在低Token预算下能有效保留关键信息，但绝对准确率仍低于全量RGB采样。

消融实验显示，增加P帧密度可提升准确率，但边际收益递减。例如，从1关键帧/GOP增加到2关键帧/GOP，PerceptionTest准确率提升6.6%；而从4关键帧/GOP增加到64关键帧，仅提升4.3%。此外，预训练阶段对性能至关重要，跳过预训练直接端到端训练会削弱表现，证实了特征空间对齐的必要性。

评估边界方面，论文未报告置信区间，且未覆盖计算效率的细粒度指标（如FLOPs）。代码已开源，但训练依赖21K GPU小时（64 A100-80G，14天），复现成本较高。评估协议使用lmms-eval，ActNet-QA采用GPT-4o评估，可能存在评估器偏差。

## 关联研究分析

从问题动机看，CoPE-VideoLM 与ReMoRa同属视频压缩路线，但ReMoRa基于解码后的RGB帧进行运动向量提取，而CoPE-VideoLM 直接使用编码器原生的运动向量和残差。这一差异源于对冗余来源的不同理解：ReMoRa认为冗余存在于像素空间，需后处理去除；CoPE-VideoLM 认为冗余已编码在压缩流中，直接利用更高效。然而，CoPE-VideoLM 未探索B帧支持，而ReMoRa可能通过解码帧间接处理双向预测，这在实时流场景中可能成为CoPE-VideoLM 的盲区。

从方法设计看，CoPE-VideoLM 与Video-o3代表两种截然不同的范式：前者是被动压缩，后者是主动代理。Video-o3 通过工具调用迭代检索稀疏证据，适合复杂多跳推理；CoPE-VideoLM 通过静态Token压缩，适合实时低延迟场景。两者在“证据稀疏度”与“延迟要求”的权衡上存在根本分歧。CoPE-VideoLM 未引入工具调用，意味着在极端稀疏证据任务上，其召回率可能低于代理式方法，但论文未提供此类任务的对比数据，无法判断被动压缩是否必然低于主动检索。

## 总结

CoPE-VideoLM 解决的核心矛盾是长视频处理中Token爆炸与实时性需求的冲突。其切入点在于利用视频编码器原生的稀疏结构，直接编码运动向量和残差，避免了RGB解码的计算开销。方法通过双分支Δ-Encoder和预训练对齐，将P帧压缩为极少量Token，在PerceptionTest上以20.1%的Token实现70.3%的准确率，超越全量RGB基线。然而，论文边界清晰：未支持B帧，固定融合窗口不适应变运动场景，且未验证在极端稀疏证据任务上的表现。当视频包含大量快速运动或复杂场景切换时，固定P帧融合窗口是否会导致关键动态信息丢失，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.13191)