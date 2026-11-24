# CVPR2026最新论文 ｜VLM-Pruner: Buffering for Spatial Sparsity in an Efficient VLM Centrifugal Token Pruning Paradigm ｜VLM-Pruner：基于空间稀疏缓冲的离心式视觉Token剪枝

研究机构：浙江大学、华为

作者：Zhenkai Wu、Xiaowen Ma、Zhenliang Ni 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.02700)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.02700)

> 视觉语言模型（Vision-Language Models, VLMs）在处理高分辨率图像时，视觉Token数量激增导致二次方注意力计算成为部署瓶颈。现有剪枝方法要么因依赖重要性评分导致局部冗余，要么因追求多样性导致Token分布分散而丢失细粒度细节。本文提出VLM-Pruner，一种训练-free的离心式剪枝范式，通过空间稀疏缓冲准则强制“由近及远”的选择顺序，并在最后阶段将丢弃Token的信息加权融合回保留Token。该方法在88.9%剪枝率下实现了领先的性能保持，但其缺乏文本引导机制可能限制其在强语义依赖任务上的表现。

## 研究背景

当VLM接收高分辨率图像输入时，视觉编码器输出的Token数量可达数千，远超文本Token，导致LLM解码器层的注意力计算成本呈二次方增长。这一计算瓶颈源于Transformer架构对长序列的低效处理，而视觉Token中存在的空间冗余为压缩提供了理论可能。然而，简单的固定比率剪枝忽视了任务语义对Token重要性的动态影响，导致在保持计算效率与语义保真度之间难以平衡。

视觉Token剪枝领域已形成两条主要技术路线：重要性驱动剪枝与冗余度降低剪枝。前者如FastV和SparseVLM，利用LLM浅层注意力或跨模态相似度保留显著Token，但往往在同一物体周围保留多个相似局部区域，造成冗余；后者如DivPrune和DART，通过贪心算法选择与已选Token相似度低的Token以最大化多样性，但导致Token分布分散，无法完整覆盖目标物体的细粒度细节。这两种策略在极端压缩率下均表现出性能退化，且未能有效解决空间连续性与信息完整性的矛盾。

本文切入点在于指出上述两类方法的共同缺陷：缺乏对空间邻近性的显式建模。重要性驱动方法忽略了空间冗余，而冗余度降低方法忽略了空间连续性。VLM-Pruner通过引入空间稀疏缓冲准则，将剪枝过程重构为“由近及远”的离心式选择，旨在平衡Token冗余与局部细节完整性，从而在保持计算效率的同时提升细粒度感知能力。

## 核心方法

### 方法参照系

VLM-Pruner属于训练-free的冗余度降低剪枝路线，其基础流程与DivPrune和DART相似，即通过贪心算法迭代选择与已选Token相似度低的Token。关键差异在于，本文在相似度计算中引入了空间距离约束，并在选择完成后增加了信息恢复阶段，而非直接丢弃未选Token。

### 空间稀疏缓冲准则

传统贪心选择仅基于特征相似度，导致Token选择分散。VLM-Pruner在LLM解码器第二层执行剪枝，通过空间稀疏缓冲（Buffering for Spatial Sparsity, BSS）准则调制候选Token与已选Token的相似度。对于候选Token $i$，计算其到已选集合 $S$ 中最近Token的归一化空间距离 $\bar{\delta}_i(S)$，并定义BSS调制相似度：

$$ \tilde{M}_{ij} = M_{ij} \cdot (1 + \lambda \cdot \bar{\delta}_i(S)) $$

其中 $M_{ij}$ 为基于Top-q方差通道的余弦相似度，$\lambda=0.5$ 为BSS强度。该公式的物理含义是：空间距离越远的候选Token，其调制后相似度越高，从而被判定为更“冗余”而推迟选择。这种机制强制选择过程优先填充局部邻域，实现由近及远的离心式扩展，解决了纯冗余度降低方法导致的Token分布分散问题。

### 相似性加权聚合

离心式选择虽保留了局部细节，但丢弃了外围Token中的互补语义信息。VLM-Pruner引入相似性加权聚合（Similarity-Weighted Aggregation, SWA）机制，将丢弃Token的信息融合回最相似的保留Token。对于丢弃Token $u$，找到其最相似的保留Token $j^*(u)$，并计算归一化权重 $\alpha_{u \to j}$，更新保留Token的隐藏状态：

$$ \mathbf{H}_j' = \mathbf{H}_j + \beta \cdot \sum_{u \in D_j} \alpha_{u \to j} \mathbf{H}_u $$

其中 $\beta=0.3$ 控制融合比例，$D_j$ 为分配给保留Token $j$ 的丢弃Token集合。该设计动机在于弥补剪枝过程中的信息损失，通过加权融合恢复外围Token的语义线索，提升了在OCR等细节敏感任务上的表现。

## 实验评估

实验在LLaVA-1.5-7B、LLaVA-1.5-13B、LLaVA-Next-7B、Qwen2-VL-7B和LLaVA-Video-7B五个VLM上，覆盖GQA、MMB、MME、POPE、SQA、TextVQA、OCRBench、SEEDBench、OKVQA等9个图像基准和4个视频基准。基线包括重要性驱动的FastV、SparseVLM、MustDrop和冗余度降低的DART、DivPrune。

| 方法 | GQA Acc. | MMB Acc. | MME P+C | POPE F1 | OCRBench Final | Avg. |
|---|---|---|---|---|---|---|
| FastV | 55.75 | 57.06 | 1670 | 69.5 | 270 | 84.75% |
| DART | 57.54 | 57.93 | 1736 | 76.0 | 264 | 88.12% |
| DivPrune | 57.32 | 57.32 | 1754 | 84.8 | 287 | 90.20% |
| VLM-Pruner | 61.21 | 65.7 | 1779 | 84.7 | 306 | 92.68% |

在LLaVA-1.5-7B上，88.9%剪枝率下，VLM-Pruner的Avg.为92.68%，高于DivPrune的90.20%和FastV的84.75%。在Qwen2-VL-7B上，OCRBench得分581，比DART的481高12.56%，表明空间连续性对细粒度文本识别至关重要。

消融实验显示，移除BSS准则中的归一化距离项导致Avg.下降1.11%，替换Stage 2选择器为DivPrune导致Avg.降至46.47%，证实了离心式选择对细节保留的关键作用。SWA机制贡献了0.23%的性能提升，虽幅度较小但稳定。

评估边界方面，论文未报告置信区间，且未对比端到端学习式方法如VisionSelector。代码已开源，超参数（$\lambda=0.5$, $\tau^{(0)}=0.8$）固定，实验在8块32GB GPU上进行，可复现性良好。

## 关联研究分析

从问题动机看，VLM-Pruner与FlashVLM和CRISP存在显著差异。FlashVLM和CRISP依赖文本查询引导，通过跨模态相似度或语义覆盖确保Token与任务相关，而VLM-Pruner完全基于视觉空间结构，未显式引入文本信号。这种差异源于任务特性：VLM-Pruner针对的是通用视觉理解中的细节保留，而非特定查询下的语义对齐。在强语义依赖任务如TextVQA上，缺乏文本引导可能导致性能增益有限，论文未对此进行专门验证。

从方法设计看，VLM-Pruner与ToMe和DivPrune形成对比。ToMe通过二分软匹配合并Token，DivPrune通过贪心选择最大化多样性，两者均直接丢弃或合并Token，而VLM-Pruner通过SWA机制将丢弃Token的信息融合回保留Token。这种“剪枝-融合”联合优化策略在保留Token数量不变的前提下恢复了部分丢失信息，但可能引入噪声。与DivPrune相比，VLM-Pruner的空间约束解决了分散问题，但计算复杂度略高，因为需要预计算空间距离矩阵。

## 总结

VLM-Pruner旨在解决视觉Token剪枝中冗余与细节平衡的矛盾，通过空间稀疏缓冲准则强制由近及远的选择顺序，并引入相似性加权聚合恢复丢弃Token的信息。在88.9%剪枝率下，该方法在LLaVA-1.5-7B上实现92.68%的Avg.性能，OCRBench得分比基线高12.56%。其边界在于缺乏文本引导机制，可能限制在强语义依赖任务上的表现，且SWA融合的计算开销未详细分析。当输入图像包含多个语义相关但空间分散的物体时，离心式选择是否仍能保持足够的语义覆盖，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.02700)