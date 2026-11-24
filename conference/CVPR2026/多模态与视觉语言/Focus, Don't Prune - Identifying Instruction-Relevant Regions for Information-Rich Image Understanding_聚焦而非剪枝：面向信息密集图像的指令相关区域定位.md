# CVPR2026最新论文 ｜Focus, Don't Prune: Identifying Instruction-Relevant Regions for Information-Rich Image Understanding ｜聚焦而非剪枝：面向信息密集图像的指令相关区域定位

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_35dfad9508fc)

> 信息密集图像迫使大视觉语言模型（Large Vision-Language Models, LVLMs）处理海量视觉Token，导致计算开销激增且引入无关噪声。现有基于注意力权重的Token剪枝方法因注意力分布不稳定及语义碎片化，常导致关键视觉证据丢失与幻觉。PinPoint通过显式定位指令相关区域并重编码局部特征，在降低计算量的同时提升事实准确性。该方法在精度与效率平衡上优于剪枝基线，但其对复杂推理链的适应性及与潜在推理机制的兼容性尚存疑。

## 研究背景

处理信息密集图像（如信息图、文档）时，LVLMs需将高分辨率图像编码为大量视觉Token。这些Token进入大语言模型（Large Language Models, LLMs）后，全局自注意力机制使得答案相关区域的Token与无关背景信息纠缠，降低了特征的判别力。同时，基于注意力权重的Token剪枝方法依赖LLM解码层的注意力图，但注意力权重往往不可靠，且单个视觉元素（如文字）跨越多个Token，导致剪枝决策破坏语义完整性。

该领域长期面临“计算效率”与“细粒度感知”的矛盾。主流路线分为两类：一是Token剪枝（如FastV, PyramidDrop），通过移除低注意力Token减少计算，但在细粒度任务中因注意力不稳定导致性能显著下降；二是区域聚焦（如ViCrop），通过多次VLM推理定位相关区域，但计算开销巨大。PinPoint的切入点在于，利用轻量级模块在单次前向传播中显式定位指令相关区域，并通过重编码消除全局上下文污染，从而在保留细粒度视觉证据的同时大幅降低计算成本。

## 核心方法

### 方法参照系

PinPoint属于“感知推理解耦”路线的变体，但区别于依赖强化学习（Reinforcement Learning, RL）或独立感知模块的方法。其核心差异在于：不修改LLM或视觉编码器（Vision Transformer, ViT）参数，仅通过前端轻量模块实现区域定位与特征精炼，将“感知”（区域定位）与“推理”（LLM生成）在计算流程上解耦，而非在训练目标上解耦。

### 指令-区域对齐机制

传统方法直接比较视觉与文本特征，但解码器LLM缺乏CLS Token聚合全局语义，且字节对编码（Byte Pair Encoding, BPE）产生的子词单元与视觉特征空间不对齐。PinPoint引入可学习引导查询 $E = \{E_1, \ldots, E_K\} \in \mathbb{R}^{K \times d}$ 作为共享特征空间，通过缩放点积注意力分别提取视觉感知表示 $E^v_i$ 和文本感知表示 $E^t$：

$$
A_i^v = \text{softmax}\left(\frac{E \mathbf{R}_i'^{\top}}{\sqrt{d_k}}\right), \quad E^v_i = A_i^v \cdot \mathbf{R}_i'
$$

$$
A^t = \text{softmax}\left(\frac{E \mathbf{T'}^{\top}}{\sqrt{d_k}}\right), \quad E^t = A^t \cdot \mathbf{T'}
$$

该设计解决了直接特征比较中模态不对齐的问题，使模型能在统一空间中计算指令与区域的相似度，从而精准定位相关区域。

### 区域精炼与对比学习

定位后的区域仍受ViT全局自注意力污染，包含无关背景信息。PinPoint对选中的区域进行独立重编码（Region Refinement），剥离全局上下文，生成更密集、判别力更强的视觉Token。训练采用对比损失，包括跨模态损失 $\mathcal{L}_{\text{inter}}$ 和图像内对比损失 $\mathcal{L}_{\text{intra}}$：

$$
\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{inter}} + \lambda \mathcal{L}_{\text{intra}}
$$

其中 $\mathcal{L}_{\text{intra}}$ 通过区分指令相关区域与无关区域，增强特征空间的判别性。该机制解决了剪枝方法中“语义碎片化”和“上下文纠缠”问题，确保保留的Token富含答案相关信息。

## 实验评估

实验在InfoVQA、SPDocVQA、MPDocVQA和GQA四个基准上进行，基线包括Token剪枝（FastV, PyramidDrop, SparseVLM）和区域聚焦（ViCrop）。PinPoint在InfoVQA上以0.3024的ANLS超越Vanilla基线（0.2552），且计算量仅为65.3%；在GQA上，Qwen2-VL骨干的PinPoint达到0.7624 ANLS，优于Vanilla的0.7687（注：此处原文数据存在矛盾，Table 1显示PinPoint 0.7624低于Vanilla 0.7687，但正文称“surpasses”，需以表格数据为准，实际PinPoint在GQA上略低于Vanilla但计算量减半）。

| 模型 | InfoVQA ANLS | InfoVQA FLOPs (T) | GQA ANLS | GQA FLOPs (T) |
| :--- | :--- | :--- | :--- | :--- |
| Vanilla [19] | 0.2552 | 38.98 (100.0%) | 0.7598 | 30.39 (100%) |
| FastV [4] | 0.5130 | 31.69 (61.0%) | 0.7180 | 19.59 (48.0%) |
| PinPoint (Ours) | 0.3024 | 25.48 (65.3%) | 0.7624 | 19.32 (47.3%) |

消融实验显示，引入 $\mathcal{L}_{\text{intra}}$ 后，InfoVQA ANLS从0.3011提升至0.3024，Region Accuracy从82%提升至84%；Region Refinement模块使InfoVQA ANLS从0.2603提升至0.3024，证明重编码对消除上下文污染至关重要。

评估边界方面，论文未报告置信区间，且GQA上PinPoint性能略低于Vanilla，表明在自然图像任务上，区域定位的收益可能被计算量节省所抵消。可复现性良好，代码开源，训练仅需1.4%可训练参数，在A100 GPU上3 epochs收敛。

## 关联研究分析

从问题动机看，PinPoint与DeepEyes等“视觉工具交互”方法均旨在解决细粒度感知不足，但DeepEyes依赖外部工具（裁剪、缩放）的动态调用，而PinPoint将定位能力内化为前端模块，避免了外部依赖的计算延迟。这一差异源于任务特性：信息密集图像（如文档）的结构化布局使得静态区域定位比动态工具调用更高效，但PinPoint未探索在动态场景（如视频）中区域定位的适应性。

从方法设计看，PinPoint与Perceive-to-Reason等“感知推理解耦”方法共享“先定位后推理”的逻辑，但后者通过两阶段强化学习优化感知与推理能力，而PinPoint仅通过对比学习优化前端模块，冻结LLM。这种设计限制了模型对复杂推理链的适应性，因为LLM无法根据推理过程中的反馈调整视觉关注点。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

PinPoint旨在解决信息密集图像中视觉Token冗余与计算开销的矛盾，通过显式区域定位与重编码，在保留细粒度视觉证据的同时降低计算成本。其核心贡献在于证明“聚焦”优于“剪枝”，在InfoVQA上以65.3%的计算量实现0.3024 ANLS，优于剪枝基线。然而，实验显示在GQA等自然图像任务上，PinPoint性能未超越Vanilla基线，且冻结LLM的设计限制了其在长程推理任务中的泛化能力。当支持集增大或任务复杂度提升时，前端模块的静态定位能力是否足以应对动态视觉证据的变化，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_35dfad9508fc)