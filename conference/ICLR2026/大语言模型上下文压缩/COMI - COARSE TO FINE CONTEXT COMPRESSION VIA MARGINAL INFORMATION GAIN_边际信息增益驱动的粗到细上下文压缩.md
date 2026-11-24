# ICLR2026最新论文 ｜COMI: COARSE TO FINE CONTEXT COMPRESSION VIA MARGINAL INFORMATION GAIN ｜边际信息增益驱动的粗到细上下文压缩

研究机构：清华大学、中山大学

作者：Jiwei Tang、Shilei Liu、ZHICHENG ZHANG 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_81721224)

> 长上下文推理面临计算成本与冗余信息的双重瓶颈，现有任务感知压缩方法仅依据查询相关性筛选内容，导致保留的语义高度重叠，误导模型生成错误输出。COMI 引入边际信息增益（Marginal Information Gain, MIG）指标，在保留相关性的同时惩罚语义冗余，通过粗粒度组重分配与细粒度 Token 合并实现自适应压缩。该方法在 32 倍高压缩比下显著优于基线，但其对多跳推理中结构化依赖的捕捉能力仍受限于线性统计机制，未完全解决复杂逻辑链断裂问题。

## 研究背景

当检索增强生成（Retrieval-Augmented Generation, RAG）将外部文档注入大语言模型（Large Language Models, LLMs）时，输入序列长度激增。Transformer 自注意力机制的二次方复杂度使得长序列推理延迟激增，且冗余内容会稀释关键信息，降低模型性能。为缓解此问题，上下文压缩旨在精简输入，但直接剔除 Token 易造成语义断裂。软提示压缩（Soft Prompt Compression）将文本映射为连续向量，虽保留语义完整性，但缺乏可解释性，且在高压缩比下易丢失关键细节。

主流压缩路线分为任务无关与任务感知两类。任务无关方法（如 ICAE）保留整体语义，但在高压缩比下无法区分查询相关与无关信息，导致关键内容被稀释。任务感知方法（如 LongLLMLingua）引入查询引导压缩，但仅以相关性为准则，忽视了自然语言固有的冗余性。实验表明，查询相关 Token 之间往往高度相似（最低余弦相似度超过 0.6），这种“相关但冗余”的内容累积会误导 LLM 产生错误输出。现有动态压缩率分配机制或遵循线性规则，或仅基于相关性，均未考虑压缩单元间的语义冗余，导致信息多样性受损。COMI 的切入点在于：如何在保留查询相关信息的同时，识别并消除压缩表示中的语义冗余，以联合优化相关性与多样性。

## 核心方法

### 方法参照系

COMI 基于编码器-解码器架构，继承自 GMSA 的跨层语义对齐（Layer Semantic Alignment, LSA）模块，用于对齐编码器高层摘要与解码器低层语义。与标准软压缩流程不同，COMI 摒弃了均匀压缩或单一相关性筛选，转而采用基于边际信息增益（MIG）的自适应粗到细策略，动态调整不同语义区域的压缩率。

### 边际信息增益计算

传统任务感知压缩仅计算 Token 与查询的余弦相似度，忽略了 Token 间的语义重叠。COMI 引入 MIG 指标，定义为 Token 对查询的相关性减去其与上下文中其他 Token 的最大语义冗余。该设计解决了仅基于相关性筛选导致的高冗余内容累积问题，确保保留的信息既相关又独特。

$$G(x_i, q, X) = \text{sim}(x_i, q) - \max_{x_j \in X, j \neq i} \text{sim}(x_i, x_j)$$

其中 $\text{sim}$ 表示余弦相似度。MIG 值越高，表明该 Token 对查询贡献大且与其他 Token 差异显著，应被优先保留。

### 粗粒度组重分配

在编码器提取隐藏状态后，COMI 将上下文划分为等长非重叠段。针对固定压缩率导致的信息价值分布不均问题，COMI 计算每段的 MIG，并据此动态分配压缩预算。高 MIG 段被赋予更低的压缩率（即保留更多 Token），低 MIG 段则被更激进地压缩。

$$L_i = \frac{P_i}{\sum_{k=1}^m P_k} L_{org}$$

其中 $P_i$ 为基于 MIG 逆序排列的分配权重，$L_{org}$ 为原始序列长度。此机制确保压缩资源向高信息价值区域倾斜，避免关键语义在均匀压缩中被稀释。

### 细粒度 Token 合并

在确定各段目标长度后，COMI 在段内执行 Token 合并。为消除段内冗余，COMI 计算每个 Token 的组内 MIG，并通过 Softmax 加权融合生成单一压缩 Token。高 MIG Token 对合并表示的贡献更大，从而在有限长度内最大化信息密度。

$$\tilde{h}_i = \sum_{k=1}^{|S_i|} w_k h_k, \quad w_k = \frac{\exp(G(h_k, S_i))}{\sum_{j=1}^{|S_i|} \exp(G(h_j, S_i))}$$

该加权融合机制确保关键语义单元被保留，同时避免“相关但冗余”内容的累积，提升压缩表示的语义互补性。

## 实验评估

实验在 NaturalQuestions、HotpotQA、2WikiMQA、NarrativeQA 和 MultiNews 上进行，基线覆盖硬压缩（LongLLMLingua）、软压缩（ICAE, GMSA）及 KV 缓存压缩（SnapKV, Activation Beacon）。在 32 倍压缩约束下，COMI 在 Qwen2-7B-Instruct 骨干上表现突出。

| 方法 | NaturalQuestions EM | 2WikiMQA EM | HotpotQA EM |
| :--- | :--- | :--- | :--- |
| Activation Beacon | 22.26 | 28.91 | 11.28 |
| LongLLMLingua | 24.63 | 21.54 | 10.94 |
| GMSA | 27.81 | 35.45 | 24.90 |
| COMI | 49.15 | 48.89 | 40.46 |

COMI 在 NaturalQuestions 上较次优基线 GMSA 提升 21.34 点，在 2WikiMQA 上提升 13.44 点，验证了 MIG 在高压缩比下的有效性。

| 消融变体 | NaturalQuestions EM | 2WikiMQA EM |
| :--- | :--- | :--- |
| Default (COMI) | 56.31 | 52.13 |
| w/o Coarse-Grained Reallocation | 54.54 | 49.82 |
| w/o Fine-Grained Merging | 50.81 | 47.88 |
| w/o Coarse-Grained Redundancy | 54.59 | 50.14 |
| w/o Fine-Grained Redundancy | 50.82 | 49.50 |

消融实验显示，移除细粒度 Token 合并导致性能下降最显著（NaturalQuestions 降 5.50 点），表明组内冗余消除对高压缩比下的语义保真度至关重要。移除粗粒度重分配次之，说明动态预算分配优于均匀压缩。

评估边界方面，论文未报告置信区间，且仅在 32K 以内序列测试。代码已开源，训练使用 8 张 NVIDIA H20 GPU，超参数（学习率 1e-5，批量大小 64）已公开，具备可复现性。

## 关联研究分析

从问题动机看，COMI 与 TopoCompress 均针对高压缩比下的信息丢失，但路径迥异。TopoCompress 引入图结构捕捉长距离依赖，适用于多跳推理中复杂的逻辑链；而 COMI 依赖线性 MIG 统计，虽在单跳问答（NaturalQuestions）上表现优异，但在多跳任务（HotpotQA）上落后 TopoCompress 约 10 点。这一差距暗示，统计冗余消除无法替代结构化依赖建模，COMI 的线性假设在处理非均匀密集依赖时存在盲区。

从方法设计看，COMI 与 ICAE 同属软压缩，但 ICAE 侧重自编码重构，追求全局语义完整性；COMI 则侧重查询相关性与冗余度平衡，牺牲部分全局信息以换取任务针对性。COMI 继承 GMSA 的 LSA 模块，但将压缩核心从静态池化升级为动态 MIG 引导，这一改动解决了 GMSA 在高压缩比下关键信息稀释的问题，但未解决跨层语义对齐在极长序列中的稳定性问题。

## 总结

COMI 旨在解决任务感知压缩中“相关但冗余”内容累积导致的模型误导问题。通过引入 MIG 指标，COMI 在保留查询相关性的同时惩罚语义冗余，实现了粗粒度预算分配与细粒度 Token 合并的自适应压缩。实验证明，在 32 倍压缩比下，COMI 在 NaturalQuestions 上较基线提升 25 点，显著优于 GMSA 和 ICAE。然而，其在 HotpotQA 多跳推理上的表现落后于结构化方法 TopoCompress，暴露了线性统计机制在捕捉复杂逻辑依赖上的局限。当上下文依赖结构从线性序列转向图状网络时，MIG 的冗余消除能力是否足以弥补结构化建模的缺失，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_81721224)