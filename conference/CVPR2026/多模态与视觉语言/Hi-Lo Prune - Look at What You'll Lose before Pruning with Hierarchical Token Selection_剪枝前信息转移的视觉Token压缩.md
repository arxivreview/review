# CVPR2026最新论文 ｜Hi-Lo Prune: Look at What You'll Lose before Pruning with Hierarchical Token Selection ｜剪枝前信息转移的视觉Token压缩

研究机构：浙江大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bf1c557b254c)

> 高分辨率视觉输入导致多模态大语言模型（MLLMs）中视觉Token数量激增，引发二次方注意力计算瓶颈。现有Training-free剪枝方法在浅层直接丢弃Token，导致模型无法充分吸收被移除Token的信息，在高压缩率下性能显著退化。Hi-Lo Prune提出“剪枝前信息转移”原则，通过层级选择确定保留与融合Token集合，并在剪枝层之前利用注意力机制将待剪Token的视觉上下文显式转移至保留Token。该方法在Qwen系列模型上实现了90%剪枝率下超过93%的基线准确率保持，但其固定预算策略与单层剪枝架构限制了其在动态场景下的泛化能力。

## 研究背景

多模态大语言模型（MLLMs）通过视觉编码器将图像映射为Token序列，再经投影层对齐至语言模型嵌入空间。当输入为高分辨率图像时，视觉Token数量 $N$ 远超文本Token长度 $L$，导致Transformer自注意力计算复杂度呈 $O(N^2)$ 增长。视觉Token中存在大量空间冗余，但直接丢弃会丢失细粒度语义信息，这构成了压缩效率与语义保真度之间的核心矛盾。

视觉Token剪枝旨在从 $N$ 个Token中选出子集 $\hat{V}$，使得模型输出差异最小化。主流Training-free方法分为两类：基于重要性的方法（如FastV）利用浅层注意力分数筛选Token，但受位置偏差影响且无法区分视觉显著性与任务相关性；基于多样性的方法（如DivPrune）通过聚类保留互补Token，但忽略了Token间的信息依赖关系。这些方法的共同缺陷在于：它们在剪枝决策时仅考虑Token自身的特征，而未考虑被剪Token对保留Token的信息贡献。Hi-Lo Prune的切入点在于，将剪枝过程重构为“先转移后移除”的两阶段过程，通过修改早期层的注意力机制，确保被剪Token的关键信息在移除前已融入保留Token的表示中。

## 核心方法

### 层级Token选择

视觉Token剪枝的标准流程是在视觉编码器输出后，基于单一信号（注意力或距离）选择保留子集。本文的关键差异在于引入层级选择策略，结合像素级纹理特征与语义级嵌入特征，分别识别冗余区域与关键语义单元。

### 剪枝感知融合（PA-Fusion）

PA-Fusion机制作用于LLM的前几层，在目标剪枝层之前修改注意力权重，以增强保留Token $K$ 与融合Token $F$ 之间的信息流动。设 $A \in \mathbb{R}^{q \times k}$ 为第 $\ell$ 层的注意力Logits，对于查询位置 $i \notin K$（保留Token及文本Token）和键位置 $j \in F$（待剪Token），修改后的注意力权重 $\tilde{A}_{ij}$ 定义为：

$$
\tilde{A}_{ij} = A_{ij} + \lambda \cdot A_{ij} \cdot \mathbb{1}\left[\text{softmax}(A)_{ij} > \tau \wedge j \in \text{Top-}k_i\right]
$$

其中 $\lambda$ 为融合强度，$\tau$ 为自适应阈值，$\mathbb{1}[\cdot]$ 为指示函数。该公式的物理含义是：仅当待剪Token $j$ 对查询Token $i$ 的原始注意力权重超过阈值且位于Top-k时，才按比例 $\lambda$ 增强其连接强度。这一设计解决了早期剪枝导致的信息不可恢复问题——通过选择性增强高亲和性Token对的连接，确保被剪Token的视觉上下文在移除前被保留Token充分吸收，从而在激进压缩下维持预测分布的稳定性。

## 实验评估

实验在Qwen2-VL-2B、Qwen2.5-VL-7B、Qwen3-VL-8B及LLaVA 1.5-7B上进行，覆盖SQA、POPE、MME等9个基准。基线包括FastV、DART、DivPrune、CDPruner等Training-free方法，以及PyramidDrop、SparseVLM等多层剪枝方法。

| 模型 | 方法 | 剪枝率 | SQA | POPE | MME | Avg. |
|---|---|---|---|---|---|---|
| Qwen2.5-VL-7B | Vanilla | 0% | 84.38% | 88.38% | 2245.20 | 100.00% |
| Qwen2.5-VL-7B | FastV | 90% | 72.73% | 74.46% | 1517.59 | 82.61% |
| Qwen2.5-VL-7B | DivPrune | 90% | 75.36% | 83.22% | 1906.50 | 92.42% |
| Qwen2.5-VL-7B | Hi-Lo Prune | 90% | 77.40% | 83.72% | 1948.78 | 93.51% |

在90%剪枝率下，Hi-Lo Prune在Qwen2.5-VL-7B上的平均相对准确率为93.51%，高于DivPrune的92.42%和FastV的82.61%。PA-Fusion机制对基线方法具有普适增益：在Qwen3-VL-8B上，为DivPrune添加PA-Fusion后，MME分数从1896.92提升至1964.84，ScienceQA从65.29%提升至73.13%。

消融实验表明，PA-Fusion通过减少Logit分布的L2距离（4.09%–12.29%）和增加余弦相似度（0.18%–1.38%），有效缓解了剪枝引起的分布偏移。ChartQA上的改进幅度最小（L2距离仅减少4.09%），暗示复杂视觉推理任务对视觉内容的依赖更强，PA-Fusion的信息转移能力在此类任务上存在局限。

评估协议存在局限：所有实验均在固定剪枝层（单层为第2层，多层为第4、8、16层）和固定剪枝率（10%/20%）下进行，未测试动态预算分配。代码已开源，但论文未报告GPU型号、显存占用及推理延迟的绝对值，仅提供了相对FLOPs减少比例（43.75%）和预填充时间减少比例（49.79%），限制了跨硬件的可复现性比较。

## 关联研究分析

从问题动机看，Hi-Lo Prune与SparseVLM的核心差异在于信息处理时序。SparseVLM在剪枝后通过文本引导的层自适应稀疏化策略恢复部分信息，属于“事后补偿”；Hi-Lo Prune则在剪枝前通过PA-Fusion转移信息，属于“事前预防”。这一差异源于对注意力信号稳定性的不同假设：SparseVLM依赖深层注意力进行任务相关性评估，而Hi-Lo Prune认为浅层注意力虽不稳定，但可通过融合机制弥补其信息丢失。然而，PA-Fusion的融合强度 $\lambda$ 和阈值 $\tau$ 为固定超参数，未随任务复杂度动态调整，这可能限制了其在极端压缩率下的鲁棒性。

从方法设计看，Hi-Lo Prune与DivPrune同属多样性导向的剪枝框架，但Hi-Lo Prune引入了层级选择机制。DivPrune仅基于语义级嵌入的余弦距离选择Token，而Hi-Lo Prune先利用像素级特征进行粗粒度冗余过滤，再基于语义级特征进行细粒度选择。这一设计假设纹理冗余与语义冗余存在层级对应关系，但论文未验证该假设在低分辨率或抽象图像上的有效性。此外，PA-Fusion仅作用于前两层，若剪枝层较深，信息转移的累积效应可能不足，这在多层剪枝实验中未得到充分探索。

## 总结

Hi-Lo Prune针对Training-free剪枝方法在高压缩率下因信息丢失导致的性能退化问题，提出了“剪枝前信息转移”原则。通过层级选择确定保留与融合Token集合，并利用PA-Fusion机制在剪枝前增强待剪Token与保留Token的注意力连接，该方法在Qwen2.5-VL-7B上实现了90%剪枝率下93.51%的基线准确率保持，显著优于FastV（82.61%）和DivPrune（92.42%）。其边界在于固定预算策略与单层剪枝架构，未探索动态Token数量调整及多层剪枝下的PA-Fusion累积效应。当输入图像复杂度剧烈变化时，固定融合强度 $\lambda$ 是否会导致信息转移不足或过度，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_bf1c557b254c)