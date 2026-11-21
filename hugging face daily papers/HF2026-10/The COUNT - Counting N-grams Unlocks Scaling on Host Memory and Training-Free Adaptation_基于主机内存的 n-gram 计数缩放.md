# HuggingFace最新推荐论文 ｜The COUNT: Counting N-grams Unlocks Scaling on Host Memory and Training-Free Adaptation ｜基于主机内存的 n-gram 计数缩放

研究机构：美国华盛顿大学、美国艾伦人工智能研究所

作者：Ian Magnusson、Noah A. Smith、Pang Wei Koh

论文原文见 [arXiv](https://arxiv.org/abs/2610.20456)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.20456)

> 导读 大语言模型（Large Language Model, LLM）的缩放定律长期受限于计算资源与 GPU 显存的双重瓶颈，现有方法通过增加参数或数据量提升性能，但高质量数据枯竭与显存成本高昂使得传统路径难以为继。本文提出 COUNT（Counting Offline Unlocks N-gram Transformers），将预计算的 n-gram 统计频率存储于廉价的主机内存中，通过映射至模型 Unembedding 空间作为额外输入嵌入，在不增加训练参数与计算量的前提下实现性能增益。该机制不仅突破了计算最优（Compute-Optimal）范式的限制，还允许推理时动态替换计数表以实现零训练领域自适应。这一方法为数据受限场景提供了新的资源分配维度，但其在极端分布偏移下的鲁棒性及查表延迟对实时推理的影响仍需验证。

## 研究背景

当预训练损失随模型参数 $N$、数据量 $D$ 和计算量 $C$ 的增加呈现幂律下降时，Chinchilla 定律确立了计算最优的资源分配策略，即 $N$ 与 $D$ 应等比例扩展。然而，这一范式隐含了高质量数据无限供给的假设，且要求所有参数与优化器状态驻留于昂贵的 GPU 显存中。随着互联网高质量文本接近饱和，数据受限成为核心瓶颈，而混合专家（Mixture-of-Experts, MoE）等稀疏激活架构虽能扩展参数规模，却仍受限于 GPU 显存容量。在此背景下，n-gram 嵌入作为一种稀疏扩展手段被提出，但现有方法需从头学习 n-gram 表示，其权重与优化器状态同样占用 GPU 显存，与骨干模型竞争资源。

主流缩放路线在“计算受限”与“数据受限”之间摇摆，却忽视了主机内存（Host RAM）这一廉价且未被充分利用的资源维度。传统方法试图通过增加参数或数据来换取性能，导致 GPU 显存成为扩展的硬约束。本文切入点在于将 n-gram 统计信息从“可学习参数”转化为“只读统计量”，利用主机内存存储预计算的 n-gram 计数表，从而在不增加 GPU 显存占用和训练计算量的情况下，通过查表机制扩展模型容量，实现从“参数-数据-计算”三元组向“参数-数据-计算-主机内存”四元组的扩展。

## 核心方法

### 方法参照系：稀疏嵌入与计算最优范式

在标准 Transformer 预训练中，输入嵌入 $e_t$ 由词表 $V$ 和隐藏维度 $d$ 决定的嵌入矩阵 $E \in \mathbb{R}^{|V| \times d}$ 查表获得，随后输入至 Transformer 块。现有 n-gram 嵌入方法（如 Over-Encoding）通过哈希表学习 n-gram 历史 $h_{t,j}$ 的表示 $q_t$，并将其与 $e_t$ 相加。该流程的关键差异在于，本文不引入任何可学习的 n-gram 参数，而是利用语料库统计频率构建非参数化嵌入，将存储压力从 GPU 显存转移至主机内存。

### 核心创新：基于计数分数的 Unembedding 映射

传统 n-gram 方法需训练独立的嵌入表，而 COUNT 复用骨干模型已学习的 Unembedding 矩阵 $B \in \mathbb{R}^{|V| \times d}$ 作为基向量。对于每个 n-gram 历史 $h_{t,j}$，从预计算表 $T_K$ 中检索其 Top-$K$ 高频后继词 $w_k$ 及其计数分数 $S(w_k | h_{t,j})$。COUNT 嵌入 $f_t$ 通过加权组合这些后继词的 Unembedding 向量生成：

$$
f_t = \sum_{j=1}^{J} \sum_{k=1}^{K} S(w_k | h_{t,j}) B[w_k]
$$

该公式的物理含义是：利用语料库中 n-gram 历史的后继分布，在模型自身的语义空间中构造一个“预期下一词”的向量表示。设计动机在于避免学习新参数带来的 GPU 显存开销，同时利用 Unembedding 矩阵已具备的语义对齐能力，使统计信息直接融入模型输入空间。最终输入为 $h_t^{(0)} = f_t + e_t$。

### 核心创新：Stupid Backoff 评分与零训练自适应

计数分数 $S(w | h)$ 采用 Stupid Backoff 策略计算，无需归一化：

$$
S(w | h) = \begin{cases}
C(w) / \sum_{w' \in V} C(w'), & h = \emptyset \\
C(h, w) / C(h), & h \neq \emptyset, C(h, w) > 0 \\
0.4 S(w | h[1:]), & h \neq \emptyset, C(h, w) = 0
\end{cases}
$$

该评分机制通过历史计数 $C(h)$ 和共现计数 $C(h, w)$ 估计条件概率，并在未观测时回退至短历史。设计动机在于离线预计算的低成本与推理时的灵活性。由于计数表仅存储统计量而非参数，推理时可动态替换为特定领域（如数学、法律）的计数表，通过插值 $S_\lambda(w|h) = (1-\lambda)S_{general}(w|h) + \lambda S_{domain}(w|h)$ 实现零训练领域自适应，解决了传统方法需微调才能适应新域的局限。

## 实验评估

实验在 Dolma 3 语料库上预训练 60M–1B 参数骨干模型，评估指标包括 LM 验证损失（nats）和任务损失（Bits Per Byte, BPB）。基线覆盖标准 Transformer 和 Learned n-gram Embeddings（Over-Encoding），但未直接对比 Retrieval-Augmented Generation (RAG) 或 MoE 架构。

| 方法 | 骨干参数 | D/N 比率 | 任务损失 (BPB) | 下游准确率 (%) | 等效计算增益 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Standard Transformer | 1B | 20 | 1.60 | 42.0 | - |
| COUNT | 1B | 20 | 1.59 | 42.5 | +46% ~ +89% |
| Learned n-gram | 1B | 20 | 1.61 | 41.8 | - |

*注：等效计算增益指标准 Transformer 需增加的计算量以达到 COUNT 的损失水平。*

消融实验显示，在固定总学习参数预算下，COUNT 的帕累托前沿优于 Learned n-gram，因为后者需额外 GPU 显存存储 n-gram 参数。推理时表大小从 797 GB 压缩至 17.1 GB 时，性能仍优于标准 Transformer，表明主机内存扩展具有鲁棒性。然而，评估未涵盖极端分布偏移下的查表失效风险，且未报告查表操作对推理延迟的具体影响，仅指出吞吐量保留 93.1–97.8%。

## 关联研究分析

从问题动机看，COUNT 与 Retrieval-Augmented Generation (RAG) 均利用外部非参数化知识，但 RAG 通过检索原始文本片段增加上下文长度，导致推理计算量随检索规模线性增长；COUNT 通过检索统计频率增强嵌入，推理计算量仅与查表操作相关，不增加序列长度。这一差异源于对“知识表示形式”的不同选择：RAG 保留原始语义细节，COUNT 压缩为统计分布。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

从方法设计看，COUNT 与 µP (Maximal Update Parametrization) 均旨在降低大规模训练的工程成本，但 µP 通过理论推导实现超参数跨尺度迁移，解决优化稳定性问题；COUNT 通过硬件资源异构利用（主机内存 vs GPU 显存）解决存储瓶颈。两者分别针对“优化器状态”和“模型参数”的显存占用，形成了互补的资源优化路径。

## 总结

本文针对高质量数据枯竭与 GPU 显存受限的双重约束，提出利用主机内存存储 n-gram 统计频率的非参数化扩展方法 COUNT。通过将计数分数映射至 Unembedding 空间，COUNT 在不增加训练参数与计算量的前提下，实现了等效于增加 46–89% 计算量的性能增益，并支持零训练领域自适应。然而，该方法依赖主机内存容量，在内存受限部署场景下性能可能退化，且查表操作引入的延迟在实时推理中是否可忽略，论文未提供端到端延迟数据。当主机内存与 GPU 显存比例发生剧烈变化时，该方法的帕累托最优性是否依然成立，仍需进一步验证。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.20456)