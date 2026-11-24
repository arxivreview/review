# 人大小米提出TimeViper：混合Mamba-Transformer架构，通过TransV模块将视觉Token转移至指令Token，支持10K+帧长视频高效理解

研究机构：中国人民大学、小米

作者：Boshen Xu、Zihan Xiao、Jiaze Li 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.16595)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.16595)

> 长视频理解面临Transformer二次方复杂度与视觉Token冗余的双重瓶颈，现有前端压缩或纯线性架构难以兼顾效率与长程依赖。本文切入点在于发现混合架构中视觉信息向文本聚合的深层冗余现象，提出TransV模块在LLM内部将视觉Token转移至指令Token。通过门控交叉注意力实现上下文渐进缩短，支持10K+帧处理。该方法在效率上显著优于纯Transformer，但在通用QA精度上低于数据规模更大的SOTA模型，其混合架构在复杂推理任务上的表达力边界尚存疑。

## 研究背景

长视频理解的核心困境源于视觉Token数量与计算复杂度的非线性增长。当视频以每秒1帧采样且每帧编码为768个视觉Token时，一小时视频将产生约270万个Token，远超现有大语言模型的上下文窗口限制。这种冗余不仅导致显存溢出，更引发注意力稀释，使得模型难以捕捉长程时序依赖。解决此问题需同时优化骨干架构的效率与Token压缩策略的保真度，二者共同决定了模型在长上下文下的可扩展性。

主流方法分为前端压缩与后端优化两条路线。前端压缩如LLaMA-VID通过投影层合并视觉特征，但未能解决LLM内部的计算瓶颈；后端优化如Video-XL在LLM内部丢弃Token，但依赖Transformer的全局注意力机制，难以直接迁移至线性架构。混合Mamba-Transformer架构虽结合了状态空间模型的线性复杂度与注意力的表达力，但其内部Token信息流动机制尚未被充分探索，导致无法设计针对性的压缩策略。本文针对这一空白，通过信息阻断实验揭示了混合架构中视觉信息向文本聚合的现象，为内部Token压缩提供了理论依据。

## 核心方法

### 混合骨干与Token信息流动分析

TimeViper采用Nanov2-9B作为骨干，包含27层Mamba-2、4层自注意力和25层MLP。Mamba-2层通过状态空间模型以$O(n)$复杂度编码时序依赖，自注意力层保留全局检索能力。为分析Token间信息流动，本文设计信息阻断实验：在$l$层阻断视觉Token到指令Token（V2I）或视觉Token到响应Token（V2R）的信息传递。实验发现，在指令中心任务（如视频QA）中，深层阻断V2I对性能影响微乎其微，表明视觉信息已聚合至指令Token；而在视觉中心任务（如字幕生成）中，浅层阻断V2R导致性能骤降，说明视觉Token直接参与响应生成。这一现象揭示了混合架构中视觉冗余随层深增加的规律，为TransV的设计提供了依据。

### TransV：门控交叉注意力Token转移

TransV是首个在混合LLM内部将视觉Token压缩至文本Token的模块，旨在解决前端压缩无法消除LLM内部冗余的问题。其核心机制是通过门控交叉注意力，将部分视觉Token的信息转移至指令Token，同时丢弃冗余视觉Token。具体而言，TransV在浅层（第7层）采用均匀丢弃策略，丢弃率$p=50\%$；在深层（第39层）采用注意力引导策略，丢弃率$p=90\%$。注意力引导策略保留被最后指令Token关注最多的Top-$k$视觉Token，丢弃其余部分。转移过程通过门控交叉注意力实现：

$$
\text{TransV}(X_0, X_1) = \text{GatedCrossAttn}(Q=X_1, K=X_0, V=X_0) + X_1
$$

其中$X_0$为视觉Token序列，$X_1$为指令Token序列。该公式的物理含义是：指令Token作为查询，从视觉Token中提取关键信息并融合至自身，从而在减少视觉Token数量的同时保留关键视觉语义。TransV在浅层均匀丢弃以快速降低Token数量，在深层注意力引导丢弃以精准保留关键信息，二者协同实现渐进式上下文缩短。

## 实验评估

TimeViper在VideoMME、LVBench、MLVU、LongVideoBench、Charades和VDC六个基准上评估，对比基线包括Transformer模型（Qwen2.5-VL、Video-XL）和混合模型（Nanov2-VL、AuroraLong）。实验设置采用每秒1帧采样，每帧压缩至16个视觉Token，训练数据量为7.8M样本。主实验结果显示，TimeViper在VideoMME上取得56.2%准确率，略高于Video-XL的55.5%；在Charades时间定位任务上mIoU达40.5%，显著优于VTimeLLM的34.6%；在VDC字幕生成任务上准确率为39.1%，与AuroraCap持平。然而，在LVBench上TimeViper仅得35.5%，远低于VideoMem的77.4%（据领域综述），表明其在超长视频长程依赖建模上存在局限。

| 模型 | VideoMME | LVBench | Charades | VDC |
|---|---|---|---|---|
| TimeViper (w/ TransV) | 56.2 | 35.5 | 37.9 | 39.1 |
| Video-XL | 55.5 | - | - | - |
| VTimeLLM | - | - | 34.6 | - |
| Qwen2.5-VL | 69.6 | 56.0 | - | - |

消融实验揭示了TransV的关键设计决策。浅层压缩率从50%提升至90%时，VideoMME准确率从56.7%降至53.4%，表明过高的浅层压缩率导致关键视觉信息丢失。深层采用注意力引导策略比均匀策略在VideoMME上高0.4个点（56.6% vs 56.2%），验证了注意力引导在深层精准保留关键信息的必要性。此外，TransV在4096帧输入下将预填充时间减少15.7%，且支持10K+帧处理，而纯Transformer模型在128帧即出现显存溢出。

评估边界方面，TimeViper未微调ViT，可能限制了视觉特征提取能力；训练数据量（7.8M）远小于Nanov2-VL（46.7M），精度差距可能部分源于数据规模而非架构本身。论文未报告置信区间，且缺乏与纯RAG或代理式方法的直接对比，限制了对其在检索增强任务上表现的全面评估。

## 关联研究分析

从方法设计看，TimeViper与Video-XL同属LLM内部Token压缩路线，但机制存在本质差异。Video-XL通过生成新特殊Token压缩视觉信息，而TimeViper通过门控交叉注意力将视觉信息转移至指令Token，避免了新Token的引入。这一差异源于混合架构的特性：Mamba层的固定大小隐状态使得视觉信息更易聚合至文本Token，而非独立存在。Video-XL依赖Transformer的全局注意力生成新Token，在混合架构中可能因Mamba层的遗忘机制导致信息丢失，而TimeViper的转移机制更适配混合架构的信息流动规律。

从问题动机看，TimeViper与LLaMA-VID均关注视觉Token冗余，但解决层级不同。LLaMA-VID在投影层压缩，仅减少输入LLM的Token数量，未解决LLM内部的计算瓶颈；TimeViper在LLM内部压缩，直接降低LLM的处理负担。这一差异源于对瓶颈位置的认知：LLaMA-VID认为冗余主要在ViT表示中，而TimeViper通过信息阻断实验发现冗余在LLM深层更为显著。LLaMA-VID的前端压缩无法消除LLM内部的冗余计算，而TimeViper的内部压缩直接针对LLM的计算瓶颈，实现了更彻底的效率提升。

## 总结

TimeViper针对长视频理解中混合架构内部Token冗余未被有效利用的问题，通过信息阻断实验揭示视觉信息向文本聚合的现象，提出TransV模块在LLM内部实现视觉-文本Token转移。该方法在4096帧输入下将预填充时间减少15.7%，支持10K+帧处理，且在Charades时间定位任务上mIoU达40.5%，优于VTimeLLM的34.6%。然而，其在LVBench上仅得35.5%，远低于VideoMem的77.4%，暴露了混合架构在超长视频长程依赖建模上的局限。当视频长度超过10K帧时，TransV的固定压缩率是否会导致关键时序信息丢失，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.16595)