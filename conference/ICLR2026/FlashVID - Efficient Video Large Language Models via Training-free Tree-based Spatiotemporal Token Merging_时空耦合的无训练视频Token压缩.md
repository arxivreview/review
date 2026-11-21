# ICLR2026最新论文 ｜FlashVID: Efficient Video Large Language Models via Training-free Tree-based Spatiotemporal Token Merging ｜时空耦合的无训练视频Token压缩

研究机构：哈尔滨工业大学、香港中文大学

作者：Ziyang Fan、Keyu Chen、Ruilong Xing 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.08024)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.08024)

> 视频大语言模型（VLLM）在处理长序列时，注意力计算的二次方复杂度导致显存与延迟激增，而现有加速框架往往独立处理空间与时间冗余，忽视了视频动态变化中语义元素的空间位移。FlashVID指出，固定空间对应关系下的时间合并会错误聚合低相关Token，从而引入噪声。该方法通过构建时空冗余树联合建模冗余，并结合注意力与多样性筛选，在无需训练的前提下实现了高效压缩。其价值在于以极低的计算开销换取了长视频上下文的扩展能力，但绝对性能仍略低于需训练的强化学习基线，且对极端压缩率下的语义保真边界缺乏深入探讨。

## 研究背景

VLLM的推理瓶颈源于视觉Token数量随时长线性增长，导致Transformer自注意力机制的计算量呈二次方爆炸。为缓解此问题，视觉Token压缩通过移除或合并低信息量Token来缩短序列长度。然而，视频数据同时具备帧内空间冗余与帧间时间冗余，且二者在动态场景中紧密耦合：语义一致的视觉元素常随运动发生位置、尺度或朝向变化，导致相邻帧中最高相关的特征往往不在同一空间位置。

主流加速框架通常采用解耦策略，即先进行帧内空间剪枝，再进行帧间时间合并。这种独立处理忽视了时空关系的内在耦合性，当视频内容动态变化时，基于固定空间位置的时间合并（如Temporal Token Merging, TTM）容易错误聚合低相关Token，扭曲视频表示并误导模型。FlashVID的切入点在于识别出“时空冗余耦合”这一被忽视的结构特性，主张通过联合建模空间与时间冗余，在动态视频条件下实现更精准的压缩，从而在保持关键语义的同时大幅降低计算开销。

## 核心方法

### 方法参照系

现有VLLM加速框架主要分为LLM前压缩、LLM内剪枝及混合压缩三类。本文聚焦于LLM前压缩，旨在在进入语言模型前减少视觉Token数量。与FastV等基于浅层注意力剪枝的方法不同，FlashVID不依赖单一信号，而是通过结构化的树状合并机制处理时空冗余，解决了独立压缩策略在动态场景下的失效问题。

### 基于注意力和多样性的Token选择（ADTS）

ADTS模块旨在从每帧中筛选出最具代表性且多样化的Token，避免直接构建冗余树时偏向主要但无关的背景信息。该模块将Token选择形式化为帧内最大最小距离问题（Max-Min Diversity Problem, MMDP），并引入[CLS]注意力与事件相关性校准项。其核心公式为：

$$
I_f = \arg\max_{S \subseteq \{1,...,N_v\}, |S|=k} \min_{i,j \in S} (D_f(i,j) + \lambda_1 A^{[CLS]}_f(i) + \lambda_2 \bar{S}_e(f))
$$

该公式通过最大化Token间的最小距离确保多样性，同时利用注意力权重和事件相似度加权，优先保留对视频事件关键的语义Token。这一设计解决了传统多样性选择可能忽略高信息量Token的问题，为后续合并提供了高质量的初始集合。

### 基于树的时空Token合并（TSTM）

TSTM模块在ADTS筛选后的Token集合上构建时空冗余树，以捕捉动态视频中的细粒度时空关系。它计算相邻帧间视觉特征的余弦相似度矩阵，若相似度超过阈值 $T_\tau$，则将当前帧Token链接至前一帧最相似的Token，形成冗余树。聚合公式为：

$$
\hat{X} = \bigcup_{T \in \mathcal{T}} \text{Agg}(T) \cup \bigcup_{f=1}^F I_f
$$

其中 $\text{Agg}(\cdot)$ 为均值池化。TSTM通过树结构灵活地合并跨帧且空间位置变化的相似Token，避免了TTM因固定空间对应导致的错误合并。这种联合建模使得在相同阈值下，TSTM能合并更多Token且保持更高的合并相似度，从而在保留动态细节的同时实现更高效的压缩。

## 实验评估

实验在VideoMME、EgoSchema、LongVideoBench、MVBench和MLVU五个基准上，针对LLaVA-OneVision、LLaVA-Video和Qwen2.5-VL三个VLLM进行。基线包括FastV、VisionZip、PruneVID和FastVID，覆盖了注意力剪枝、空间合并及密度剪枝等主流无训练方法，但缺失了需训练的强化学习基线（如SCORE）。

| 方法 | 保留率 | VideoMME Overall | EgoSchema | LongVideoBench | MVBench Total | 相对准确率 (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Vanilla (LLaVA-OneVision) | 100% | 58.5 | 62.2 | 60.3 | 58.3 | 100.0 |
| FastV | 10% | 53.4 | 59.0 | 56.0 | 53.4 | 91.8 |
| VisionZip | 10% | 54.8 | 61.6 | 58.5 | 54.8 | 94.0 |
| FastVID | 10% | 57.0 | 62.4 | 60.0 | 56.5 | 97.8 |
| FlashVID | 10% | 57.9 | 62.8 | 60.4 | 57.9 | 99.1 |

在LLaVA-OneVision上，FlashVID在10%保留率下取得了57.9的VideoMME总分，相对准确率达99.1%，显著优于FastV（91.8%）和VisionZip（94.0%）。值得注意的是，当保留率在25%-15%区间时，FlashVID的性能甚至超过了100%保留率的Vanilla模型，验证了“少即是多”的现象，即冗余Token过多反而干扰模型推理。

| 方法 | 帧数 | 保留率 | VideoMME Overall | 相对准确率 (%) |
| :--- | :--- | :--- | :--- | :--- |
| Vanilla (Qwen2.5-VL) | 16 (1x) | 100% | 57.0 | 100.0 |
| VisionZip | 80 (5x) | 20% | 62.1 | 104.9 |
| FastVID | 80 (5x) | 20% | 61.5 | 105.7 |
| FlashVID | 80 (5x) | 20% | 62.4 | 106.8 |
| FlashVID | 160 (10x) | 10% | 62.4 | 108.6 |

在Qwen2.5-VL固定预算实验中，FlashVID支持处理10倍帧数（160帧），在相同计算预算下相对性能提升8.6%，优于VisionZip（4.9%）和FastVID（5.7%）。消融实验显示，ADTS中的[CLS]注意力校准（C.A.）对性能贡献最大，单独使用C.A.时相对准确率达98.5%，而仅使用多样性（DTS）为97.1%。TSTM与ADTS的混合比例 $\alpha=0.7$ 时效果最佳，表明两种机制的协同作用优于单一机制。

评估边界方面，论文未报告置信区间，且多数对比基线为无训练方法，缺乏与需训练SOTA（如SCORE 58.5% on VideoMME）的直接对比。代码已开源，超参数统一，实验在NVIDIA A800 80G GPU上进行，可复现性较好。但指标仅关注准确率，未深入分析压缩后的时序一致性或伪影问题。

## 关联研究分析

从问题动机看，FlashVID与FastV（Chen et al., 2024）均利用注意力信号筛选Token，但FastV依赖LLM浅层注意力进行全局剪枝，而FlashVID在视觉编码器阶段通过ADTS结合多样性约束进行帧内筛选。这一差异源于FastV假设注意力权重直接反映Token重要性，而FlashVID认为单一注意力信号易受背景干扰，需通过多样性确保表示的鲁棒性。根源在于视频数据的动态性使得固定空间位置的注意力分布不稳定，FlashVID通过结构化的时空建模弥补了这一盲区。

从方法设计看，FlashVID与VisionZip（Yang et al., 2025c）都采用Token合并策略，但VisionZip主要处理空间冗余，而FlashVID通过TSTM显式建模跨帧时空关系。VisionZip在静态图像或低动态视频上表现良好，但在动态场景中因忽略时间位移导致合并错误。FlashVID的树结构允许Token在空间位置变化时仍能被正确关联，这是其优于VisionZip的关键。然而，TSTM的构建依赖余弦相似度阈值，对于极端快速运动或场景切换，该阈值可能失效，论文未对此类边界情况提供额外分析。

## 总结

FlashVID旨在解决VLLM中时空冗余独立压缩导致的动态视频表示失真问题。其切入点在于识别出语义元素的空间位移特性，通过ADTS筛选代表性Token，并利用TSTM构建时空冗余树进行联合合并。实验证明，该方法在10%保留率下保留了LLaVA-OneVision 99.1%的性能，并支持Qwen2.5-VL处理10倍帧数，相对提升8.6%。其边界在于作为无训练方法，绝对性能略低于需训练的强化学习基线，且TSTM对极端动态场景的鲁棒性未充分验证。当视频包含剧烈场景切换或快速非刚性运动时，基于余弦相似度的树构建是否仍能保持语义一致性，论文未给出明确回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.08024)