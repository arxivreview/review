# ACL2026最新论文 ｜Comparative Analysis of the Intrinsic Metrics for Tokenizers and their effect on Downstream Tasks for Hindi and Marathi ｜基于视觉单元的分词策略对印地语与马拉地语模型性能的影响

作者：Shagun Dwivedi、Kaushik Gopalan

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ea53b4eaa304)

> 主流子词分词器在处理 Devanāgari 等元音附标文字时，因 Unicode 码点与视觉单元不对齐导致语义碎片化，进而损害语言模型在问答与发音任务上的表现。现有统计驱动的分词算法（如 BPE）无法感知字符组合规则，造成低资源语言计算成本与性能的双重劣势。本文提出一种基于规则匹配的视觉单元分词器，将辅音与附着元音合并为单一 token，并系统对比了六种分词策略在内在指标与下游任务上的表现。该工作验证了视觉结构约束对 Devanāgari 语言建模的必要性，但其规则驱动的静态设计在形态极复杂场景下的泛化能力存疑。

## 研究背景

Devanāgari 文字系统采用元音附标（Abugida）结构，一个视觉字符（Grapheme Cluster）通常由辅音、组合字符及附着元音（mātrā）共同构成。在 Unicode 编码中，单个视觉单元可能需要多达 10 个码点表示，例如单词 वाक्य 在视觉上由两个字符组成，但在 Unicode 中由 5 个码点构成。这种编码与视觉结构的错位导致基于 Unicode 码点的分词器将同一视觉单元拆分为多个 token，破坏了语言的压缩性与语义完整性。

多语言大模型在非英语语言上的性能滞后已被广泛证实，其中分词器的选择是常被忽视的关键因素。主流分词算法如 Byte Pair Encoding (BPE) 和 Unigram 依赖统计频率合并字符，在形态丰富的印地语和马拉地语中，这种纯统计驱动的方式往往切断辅音与元音的绑定关系，产生大量无意义的子词片段。尽管已有研究提出引入形态学约束或转写预处理，但缺乏针对 Devanāgari 视觉结构的系统性对比评估，尤其是内在分词指标与下游任务性能之间的关联机制尚不明确。

本文切入点在于将分词边界从“统计高频对”转向“视觉可识别单元”。通过设计一种无需外部语言学资源、仅依赖 Unicode 组合标记规则的分词器，本文旨在量化视觉结构完整性对语言模型理解能力的影响，并探索 Rényi Efficiency 等内在指标能否有效预测下游任务表现。

## 核心方法

### 方法参照系

标准子词分词流程通常包含预分词（Pre-tokenization）与词汇表构建两个阶段。BPE 和 Unigram 等算法在预分词阶段仅按空白符切分，随后基于语料频率迭代合并或剪枝字符序列。本文问题与该通用流程的关键差异在于：Devanāgari 文字的语义单元并非由频率决定，而是由固定的字符组合规则（如辅音+元音+组合标记）决定，统计合并无法保证视觉单元的完整性。

### 视觉单元分词算法

针对 BPE 切断 mātrā 与辅音导致语义断裂的问题，本文提出 Grapheme Cluster Tokenizer。该算法遍历输入字符串，维护一个临时缓冲区 `temp`，当遇到非组合标记字符时，若 `temp` 非空且不以 halanta（元音抑制符号）结尾，则将 `temp` 作为一个独立的 grapheme cluster 输出；否则将当前字符追加至 `temp`。若当前字符为组合标记，则直接追加至 `temp`。该过程确保每个输出的 token 包含完整的辅音-元音组合。

$$
\text{Token}_i = \begin{cases}
\text{temp} & \text{if } c_i \notin C_{comb} \land \text{temp} \neq \emptyset \land \text{temp} \not\text{endswith}(halanta) \\
\text{temp} + c_i & \text{if } c_i \in C_{comb} \lor \text{temp} \text{endswith}(halanta)
\end{cases}
$$

其中 $C_{comb}$ 为 Devanāgari 组合标记集合。该公式的物理含义是：只有当遇到新的辅音起始且当前缓冲区已构成完整视觉单元时，才切断 token，从而保证每个 token 对应一个人类可识别的视觉字符。对于词汇表外的 grapheme cluster，算法采用从左至右的最长匹配策略，仅对无对应 token 的子串输出 `<unk>`，而非整个 cluster，以保留部分语义信息。

### 预分词与转写变体

为验证预分词步骤对下游性能的影响，本文引入 ITR+BPE 变体。在 BPE 分词前，先将 Devanāgari 文本转写为 ITRANS ASCII 格式。ITRANS 是一种无损转写方案，不使用特殊字符，可完全还原为原始文本。该设计动机在于测试“字符编码基础”而非“分词算法本身”对模型性能的影响。若 ITR+BPE 表现优于原生 BPE，则说明 Unicode 码点碎片化是主要瓶颈；若表现更差，则说明转写引入的语义混淆抵消了编码统一带来的收益。

## 实验评估

实验基于 T5-small 架构，在 Hindi、Marathi 和 English 上进行单语与多语问答（QA）、图素到音素转换（G2P）及转写任务评估。基线覆盖 BPE、Unigram、WordPiece、GPE 及 ITR+BPE，但缺失 MorphBPE 等形态感知强基线。内在指标使用 FLORES-101 子集计算，下游任务使用 XQuAD、MahaSQuAD 及 TyDiQA。

| Tokenizer | Hindi Fertility (↓) | Hindi Rényi Eff. (↑) | XQuAD Hindi Acc. (%) | MahaSQuAD Marathi Acc. (%) |
| :--- | :--- | :--- | :--- | :--- |
| GraphemeCluster | 2.432 | 0.651 | 41.60 | 47.74 |
| BytePairEncoding | 2.890 | 0.261 | 10.10 | 16.46 |
| WordPiece | 3.353 | 0.604 | 39.60 | 50.82 |
| Unigram | 3.478 | 0.621 | 34.60 | 44.03 |

Grapheme Cluster 在 Hindi QA 任务上以 41.60% 的准确率显著优于 BPE 的 10.10%，且 Rényi Efficiency 高达 0.651，远高于 BPE 的 0.261。这表明视觉单元完整性不仅降低了 Fertility，更通过优化 token 频率分布提升了模型学习效率。在 Marathi 任务上，WordPiece 以 50.82% 略高于 Grapheme Cluster 的 47.74%，显示在特定语言上统计合并仍具竞争力。

消融实验显示，ITR+BPE 在 Hindi QA 中仅得 15.71%，远低于原生 BPE 的 10.10% 之外的其他基线，甚至低于 BPE。这反直觉地表明，转写预处理并未解决碎片化问题，反而因引入 ASCII 字符的语义模糊性加剧了模型困惑。GPE 在 Marathi 上表现优于 Grapheme Cluster，但在 Hindi 上落后，暗示基于图对编码的方法对语言特异性敏感。

评估边界方面，本文使用 T5-small 骨干，可能限制了分词器优势的充分展现；代码已开源，但超参数配置（如 dropout 0.1, d_model 512）固定，未探索不同模型规模下的鲁棒性。Rényi Efficiency 与 QA 性能高相关，但与 G2P 任务相关性弱，提示不同任务可能需要不同的分词评估指标。

## 关联研究分析

从问题动机看，本文与 MorphBPE 同属形态感知分词路线，但二者对“形态知识”的依赖程度存在根本差异。MorphBPE 依赖外部词素边界标注或语言学资源来约束 BPE 合并过程，而本文仅利用 Unicode 组合标记这一编码层面的元数据。这种差异源于 Devanāgari 文字的视觉单元与词素边界高度重合的特性，使得纯规则匹配即可近似形态切分。然而，对于形态更复杂的语言（如土耳其语），视觉单元与词素边界可能错位，本文方法是否仍有效，论文未给出回答。

从方法设计看，本文与 GPE（Velayuthan & Sarveswaran, 2025）均针对 Devanāgari 优化，但 GPE 基于图对编码修改 BPE 的合并逻辑，而本文直接替换分词单元定义。GPE 在 Marathi 上优于本文方法，可能因其保留了子词统计特性，而本文的视觉单元在混合英语数据时 Fertility 上升（3.537 vs GPE 3.258），导致多语场景下效率下降。这暗示视觉单元分词在多语混合语料中可能存在适应性局限，而统计驱动的方法在跨语言泛化上更具弹性。

## 总结

本文核心矛盾在于 Unicode 码点碎片化与 Devanāgari 视觉语义完整性的冲突。现有 BPE 等统计分词器无法感知字符组合规则，导致低资源语言性能受损。本文通过规则匹配的视觉单元分词器，将辅音与元音绑定为单一 token，证明了视觉结构完整性对模型性能的显著提升。实验显示，Grapheme Cluster 在 Hindi QA 任务上准确率 41.60%，Rényi Efficiency 0.651，均大幅优于 BPE。其边界在于规则驱动的静态设计在混合语言场景下效率下降，且未探索动态分词机制。当语料中 Devanāgari 与拉丁文字比例变化时，视觉单元分词器的 Fertility 波动是否会导致模型训练不稳定，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ea53b4eaa304)