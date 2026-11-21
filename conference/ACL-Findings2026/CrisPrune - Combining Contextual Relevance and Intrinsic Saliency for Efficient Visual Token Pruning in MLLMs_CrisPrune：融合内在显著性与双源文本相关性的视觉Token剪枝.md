# ACL-Findings2026最新论文 ｜CrisPrune: Combining Contextual Relevance and Intrinsic Saliency for Efficient Visual Token Pruning in MLLMs ｜CrisPrune：融合内在显著性与双源文本相关性的视觉Token剪枝

作者：Ziniu Liu、Shuheng Zhou、Mingqing Liu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c3fde539d866)

> 视觉语言模型处理高分辨率图像时，视觉Token数量激增导致二次方注意力计算成本成为部署瓶颈。现有剪枝方法面临两难：纯视觉方法受注意力汇聚现象干扰且忽略任务语义，纯文本引导方法则因过度聚焦指令而丢失背景上下文。CrisPrune通过鲁棒归一化修复视觉显著性计算，并引入通用语义先验与指令对齐的双源文本相关性，结合行列式点过程（Determinantal Point Process, DPP）实现质量与多样性的平衡选择。该方法在极端压缩率下显著优于现有Training-free方法，但其对特定架构的依赖性及视频场景的适用性仍存疑。

## 研究背景

多模态大语言模型（Multimodal Large Language Models, MLLMs）通常由视觉编码器、模态投影层和大语言模型（Large Language Models, LLMs）组成。视觉编码器将图像转换为Token序列，投影层将其映射至LLM嵌入空间。当输入分辨率提升以捕捉细粒度细节时，Token数量从数百激增至数千，导致LLM内部注意力计算复杂度呈二次方增长，形成推理延迟与内存占用的主要瓶颈。

视觉Token中存在大量空间冗余，这为剪枝提供了理论基础。早期方法如FastV依赖LLM浅层注意力分数进行剪枝，但注意力分数受位置偏差影响，且存在注意力汇聚现象，即少数异常Token占据过高权重，抑制了其他信息丰富Token的评分。另一类方法如CDPruner利用文本指令引导剪枝，但仅依赖当前指令会导致模型忽略未提及的背景结构，在模糊查询下表现不佳。CrisPrune的切入点在于同时修复视觉信号的鲁棒性并扩展文本信号的覆盖范围，通过融合内在视觉显著性与双源文本相关性，在保持任务对齐的同时保留全局视觉完整性。

## 核心方法

### 方法参照系

本文属于Pre-LLM剪枝路线，即在视觉编码器或投影层后、LLM输入前进行Token筛选。标准流程包括计算Token重要性评分、融合多源信号、选择保留子集。本文的关键差异在于对视觉显著性计算的鲁棒性处理，以及文本相关性中引入通用语义先验以弥补指令对齐的盲区。

### 鲁棒内在视觉显著性

传统方法直接使用视觉编码器的注意力分数进行Min-Max归一化，但注意力汇聚现象导致少数异常Token拉伸归一化范围，使大多数信息丰富Token的评分被压缩至接近零。CrisPrune提出鲁棒Min-Max归一化策略，用高分位数（如98百分位）替代绝对最大值作为上界，避免异常值干扰。该设计解决了纯视觉方法在极端压缩下丢失细粒度细节的问题，确保显著性评分能真实反映Token的信息密度。

$$s_{vis}^i = \frac{\min(a_i, v_{high}) - \min(a)}{v_{high} - \min(a) + \epsilon}$$

其中 $a_i$ 为第 $i$ 个Token的原始注意力分数，$v_{high}$ 为分数分布的高分位数上界，$\epsilon$ 为数值稳定常数。该公式通过截断异常高分，使归一化后的评分分布更均匀，保留了中间分数段Token的区分度。

### 双源文本相关性与DPP选择

仅依赖指令对齐的文本相关性会导致模型忽略未提及的背景结构。CrisPrune引入通用语义先验，使用“所有物体”、“显著区域”等通用提示词计算Token与场景全局信息的相似度，并与指令对齐分数融合。该设计解决了纯文本引导方法在模糊查询下丢失背景上下文的问题，确保模型既响应用户意图又保留环境完整性。

$$s_{sem}^i = \max(r_{inst}^i, \lambda \cdot r_{gen}^i)$$

其中 $r_{inst}^i$ 为Token与指令嵌入的余弦相似度，$r_{gen}^i$ 为Token与通用提示词嵌入的最大相似度，$\lambda$ 为平衡因子。融合后的语义相关性 $s_{sem}^i$ 与鲁棒视觉显著性 $s_{vis}^i$ 结合生成质量向量 $q$，再通过DPP选择子集。DPP通过最大化行列式，在保持高质量Token的同时最大化子集内的特征多样性，避免Top-K选择导致的空间冗余。

## 实验评估

实验在LLaVA-1.5-7B、LLaVA-NeXT-7B和Qwen2.5-VL-7B上评估，覆盖GQA、VQAv2、MME、POPE等9个基准。基线包括FastV、VisionZip、CDPruner、DivPrune等Training-free方法，但未对比端到端学习类方法如VisionSelector。

| 方法 | LLaVA-1.5-7B (32 Tokens) Avg. Rel (%) | LLaVA-NeXT-7B (160 Tokens) Avg. Rel (%) | Qwen2.5-VL-7B (11.1% Tokens) Rel (%) |
|---|---|---|---|
| FastV | 74.9 | 74.6 | — |
| VisionZip | 88.4 | 88.3 | — |
| CDPruner | 93.0 | 97.6 | — |
| CrisPrune | 95.5 | 97.3 | 91.6 |

在LLaVA-1.5-7B极端压缩（32 Tokens）下，CrisPrune相对准确率为95.5%，超越CDPruner 2.5%。在LLaVA-NeXT-7B（160 Tokens）下，CrisPrune保持97.3%性能，超越VisionZip 9.0%。消融实验显示，仅使用文本相关性的TextPrune在TextVQA上优于纯视觉方法，但CrisPrune通过融合视觉显著性恢复了被文本对齐忽略的结构细节，在多数设置下表现最佳。

评估边界方面，论文未报告置信区间，且部分基准使用GPT-3.5-turbo评分，可能引入评估偏差。代码未公开，超参数 $\alpha$ 和 $\lambda$ 的敏感性分析仅在附录中简要提及，可复现性受限。

## 关联研究分析

从信号来源看，CrisPrune与ZOO-Prune存在根本差异。ZOO-Prune基于零阶梯度估计Token敏感性，认为注意力分数不稳定，应使用梯度信号；CrisPrune则通过鲁棒归一化修复注意力分数，保留其作为显著性代理的价值。这一差异源于任务特性：ZOO-Prune针对极端压缩下的鲁棒性，而CrisPrune侧重中等压缩下的语义保真度。鲁棒归一化是否在所有视觉编码器架构下都有效，论文未给出回答。

从选择机制看，CrisPrune与CRISP形成对比。CRISP采用两阶段流水线，先识别文本相关Token，再补充多样性Token；CrisPrune通过DPP在单一优化目标中同时平衡质量与多样性。CRISP的解耦设计确保了语义聚焦与全局代表性的明确分离，但增加了算法复杂度；CrisPrune的DPP框架更简洁，但依赖质量向量 $q$ 的准确性。若质量向量计算存在偏差，DPP的多样性最大化可能引入噪声Token，这一风险在论文中未充分讨论。

## 总结

CrisPrune旨在解决视觉Token剪枝中效率与语义保真度的矛盾，通过鲁棒归一化修复视觉显著性计算，并引入通用语义先验扩展文本相关性覆盖范围，结合DPP实现质量与多样性的平衡选择。实验证明，在LLaVA-1.5-7B极端压缩下，该方法保持95.5%相对准确率，超越CDPruner 2.5%；在LLaVA-NeXT-7B下，13倍FLOPs降低同时保持97%性能。其边界在于对特定架构（如CLIP文本编码器）的依赖，以及未验证视频时空冗余场景的适用性。当输入序列长度从图像扩展至视频时，通用语义先验的静态提示词是否仍能捕捉动态场景中的时序背景，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_c3fde539d866)