# ACL-Findings2026最新论文 ｜CAPA: Contribution-Aware Pruning and FFN Approximation for Efficient Large Vision-Language Models ｜贡献感知剪枝与FFN近似

研究机构：印度理工学院、美国伊利诺伊大学厄巴纳-香槟分校

作者：Samyak Jha、Junho Kim

论文原文见 [arXiv](https://arxiv.org/abs/2602.00247)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.00247)

> 视觉语言模型（VLMs）推理瓶颈源于高分辨率输入导致的视觉Token激增，现有剪枝方法依赖注意力分数却忽略Value向量幅度，导致误删关键语义信息。CAPA通过引入“注意力贡献度”指标替代原始注意力分数进行Token选择，并针对视觉Token在中间层FFN中表现出的线性冗余，采用Hadamard积近似替代密集FFN计算。该双策略框架在保持任务性能的同时实现了78%的FLOPs减少，但其FFN近似依赖特定骨干的线性冗余特性，跨模型泛化能力存疑。

## 研究背景

当VLMs处理高分辨率图像时，视觉Token数量从数百激增至数千，Transformer二次方注意力计算成本成为部署核心障碍。视觉Token中存在大量空间冗余，但冗余分布并非均匀：部分Token仅承载Softmax产生的概率质量（Probability Dumps），而另一些Token作为残差流中的结构锚点（Structural Anchors）维持模型稳定性。区分这两类Token需要超越注意力概率的度量，因为注意力分数仅反映路由权重，未包含Value向量对残差流实际注入的信息量。

视觉Token剪枝领域已形成Pre-LLM与Intra-LLM两大路线，前者在视觉编码器侧压缩以尽早降低LLM输入长度，后者在LLM浅层利用注意力信号剪枝。FastV等Intra-LLM方法确立了基于注意力分数的剪枝范式，但忽略了注意力分数与Token实际功能贡献的解耦现象。同时，LLM领域的FFN稀疏化研究未延伸至VLMs，而视觉Token与文本Token在FFN中的行为差异未被充分探索。CAPA的切入点在于：注意力分数不足以区分Probability Dumps与Structural Anchors，且视觉Token在特定层FFN中呈现近线性行为，可被轻量级算子替代。

## 核心方法

### 方法参照系

CAPA属于Intra-LLM剪枝路线，标准流程为：在LLM浅层计算Token重要性分数→Top-K选择保留Token→更新KV缓存。本文关键差异在于：重要性分数从原始注意力概率升级为注意力贡献度，且新增FFN近似步骤，将优化目标从序列长度压缩扩展至计算量压缩。

### 注意力贡献度剪枝

传统剪枝方法假设注意力概率直接反映Token重要性，但高注意力Token可能仅承载概率质量而无实际信息贡献。CAPA在生成步骤$t$计算每个视觉Token$i$的注意力贡献度$C_i$，定义为Value向量投影到残差流的$\ell_2$范数：

$$C_i = \left\| \sum_{h} A_{i,h} \mathbf{x}_i \mathbf{W}_{V,h} \mathbf{W}_{O,h} \right\|_2$$

其中$A_{i,h}$为头$h$分配给Token$i$的注意力概率，$\mathbf{W}_{V,h}$、$\mathbf{W}_{O,h}$为Value与输出投影矩阵。该公式物理含义是：Token对残差流的信息注入量等于其Value向量经投影后的加权范数，而非仅由注意力路由决定。通过动态计算$C_i$并保留Top-$k$ Token，CAPA在过渡层（LLaVA: Layers 5, 12, 16）避免误删高Value幅度的语义密集Token，如TextVQA中的图像嵌入文本。

### FFN线性冗余近似

Token剪枝后，剩余计算瓶颈来自FFN。CAPA识别视觉Token在中间层FFN中呈现近线性行为，通过余弦相似度$\cos(\mathbf{x}^{[l]}, \mathbf{y}^{[l]})$度量层$l$的冗余度，其中$\mathbf{y}^{[l]} = \mathbf{x}^{[l]} + \text{FFN}(\mathbf{x}^{[l]})$。当相似度超过阈值$\eta=0.96$时，该层FFN被替换为Hadamard积近似：

$$\mathbf{y}^{[l]} \approx \mathbf{x}^{[l]} \odot \boldsymbol{\alpha}$$

其中$\boldsymbol{\alpha} \in \mathbb{R}^d$为可学习缩放向量，通过闭式OLS解$\boldsymbol{\alpha}^* = (\sum_n \mathbf{x}_n \odot \mathbf{y}_n) \oslash (\sum_n \mathbf{x}_n \odot \mathbf{x}_n)$校准。该设计将FFN计算复杂度从$O(d^2)$降至$O(d)$，且无需反向传播，保持Training-free特性。

## 实验评估

实验在LLaVA-1.5-7B、Qwen2.5-VL-7B、InternVL3-8B三个骨干上评估，基准包括VQAv2、MMBench、TextVQA、MMMU等。基线覆盖FastV、Feather等注意力剪枝方法，但缺失VisionZip、CRISP等Pre-LLM剪枝及文本引导剪枝基线，限制了跨路线对比。

| 方法 | VQAv2 (LLaVA) | TextVQA (LLaVA) | MMMU (LLaVA) |
|---|---|---|---|
| Vanilla | 76.55 | 48.64 | 34.67 |
| FastV (Late) | 75.27 | 47.38 | 35.67 |
| CAPA (Late) | 76.20 | 48.38 | 35.89 |

CAPA在Late层剪枝下VQAv2达76.20%，接近Vanilla的76.55%，而FastV仅75.27%。TextVQA上CAPA 48.38% vs FastV 47.38%，表明贡献度剪枝对OCR任务更鲁棒。

| 策略 | VQAv2 (LLaVA) | TextVQA (LLaVA) |
|---|---|---|
| Skip FFN | 74.02 | 44.10 |
| Hadamard | 75.48 | 47.15 |
| CAPA + Hadamard | 75.10 | 46.90 |

FFN消融显示：直接跳过FFN导致VQAv2从76.55降至74.02，Hadamard近似恢复至75.48。CAPA+Hadamard组合在TextVQA上46.90%，低于纯剪枝的48.38%，表明FFN近似在细粒度任务上引入轻微性能损失。

评估边界：未报告计算延迟与内存占用，仅给出78% FLOPs减少的理论值；FFN近似系数$\boldsymbol{\alpha}$基于COCO 500样本校准，未验证跨数据集稳定性；代码未公开，超参数$\eta=0.96$固定，未探索自适应阈值。

## 关联研究分析

从信号来源看，CAPA与FastV同属Intra-LLM剪枝，但FastV依赖原始注意力分数，CAPA引入Value向量幅度。这一差异源于任务特性：TextVQA等细粒度任务中，语义密集Token可能具有中等注意力但高Value幅度，FastV易误删此类Token。CAPA的贡献度度量更准确反映Token对残差流的功能影响，但计算开销增加（需投影矩阵乘法），是否抵消剪枝收益论文未量化。

从优化目标看，CAPA与ZOO-Prune同属Training-free路线，但ZOO-Prune通过零阶梯度估计Token敏感性，CAPA通过闭式OLS求解FFN近似系数。两者均避免反向传播，但ZOO-Prune针对Token选择，CAPA针对计算量压缩。CAPA的FFN近似依赖视觉Token在中间层的线性冗余特性，该特性是否在所有VLM骨干中普遍存在，论文仅在三个骨干上验证，跨架构泛化性存疑。

## 总结

CAPA解决的核心矛盾是注意力分数与Token实际功能贡献的解耦，以及视觉Token在FFN中的线性冗余未被利用。现有方法如FastV仅基于注意力概率剪枝，无法区分Probability Dumps与Structural Anchors；CAPA通过注意力贡献度度量与FFN线性近似，在保持任务性能的同时实现78% FLOPs减少。实验证明CAPA在Late层剪枝下VQAv2达76.20%，接近Vanilla的76.55%，TextVQA上48.38%优于FastV的47.38%。但FFN近似在TextVQA上引入轻微损失（46.90% vs 48.38%），且$\boldsymbol{\alpha}$校准依赖COCO数据，跨数据集稳定性未验证。当视觉Token线性冗余特性在不同分辨率或域外数据中失效时，Hadamard近似的性能边界如何变化，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.00247)