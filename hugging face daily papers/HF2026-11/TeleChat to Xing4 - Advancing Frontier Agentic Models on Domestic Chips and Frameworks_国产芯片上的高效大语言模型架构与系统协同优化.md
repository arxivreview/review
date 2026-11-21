# HuggingFace最新推荐论文 ｜TeleChat to Xing4: Advancing Frontier Agentic Models on Domestic Chips and Frameworks ｜国产芯片上的高效大语言模型架构与系统协同优化

作者：Xingchen AGI Lab、:、Baotian Hu 等 140 人

论文原文见 [arXiv](https://arxiv.org/abs/2611.22115)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2611.22115)

> 导读：高效大语言模型（Efficient LLM）架构研究旨在突破 Transformer 自注意力机制的二次方计算复杂度与内存瓶颈，其核心驱动力源于模型规模扩张与硬件物理极限之间的张力。现有方法多基于 GPU 硬件特性进行算法层面的稀疏化或线性化近似，往往忽略了异构硬件（如 Ascend）中矩阵计算与向量计算、内存带宽之间的结构性失衡。本文提出 Xing 4 系列模型，通过架构与系统的协同设计，在 Ascend 芯片上实现了高效训练与推理。该工作验证了非 GPU 硬件上高效 LLM 的可行性，但仿真结果与真实部署的差距是否影响结论泛化性，仍需进一步验证。

## 研究背景

当大语言模型（Large Language Model, LLM）的上下文窗口向百万级 Token 迈进时，Softmax 注意力在计算 Query-Key 相似度时的 $O(N^2)$ 复杂度，以及键值缓存（KV Cache）随序列长度线性增长的内存占用，成为制约模型部署的核心物理瓶颈。这一矛盾在国产芯片（如 Ascend）上尤为突出：Ascend 910C 提供强大的 Cube 矩阵计算能力，但 Vector 计算和 HBM 带宽相对受限。若直接沿用基于 GPU 特性设计的架构，过深的网络会放大非矩阵计算开销（如归一化、路由、索引），导致 Cube 利用率低下，无法发挥硬件潜力。

领域内的高效架构研究经历了从算法加速到系统-架构协同设计的转变。早期工作如 Longformer 和 Linear Transformer 试图通过稀疏化或线性化降低复杂度，但牺牲了长程依赖精度。FlashAttention 确立了内存感知计算范式，证明了在不改变算法逻辑的前提下挖掘硬件潜力的价值。随着 Mamba 等状态空间模型（State Space Model, SSM）的出现，研究重心转向混合架构，试图在保留精确检索能力的同时实现线性复杂度推理。然而，现有共识多基于 GPU 硬件特性，Ascend 的 Cube/Vector 异构特性如何具体改变架构设计权衡，仍是未被充分探索的盲区。本文针对 Ascend 硬件特性，提出“宽而浅”拓扑与无流水线并行（Pipeline Parallelism, PP）的系统优化方案，填补了这一空白。

## 核心方法

### 方法参照系：长上下文注意力与系统瓶颈

本文解决的问题属于“训练推理系统”与“新型骨干架构”的交叉领域。在标准的高效 LLM 架构中，通常采用 Multi-head Latent Attention (MLA) 压缩 KV 表示，结合稀疏注意力减少历史 KV 访问。然而，在 Ascend 硬件上，长上下文推理仍面临两大瓶颈：一是 MLA 虽减少 KV Cache 大小，但超长上下文下主注意力仍需访问大量历史 KV 状态，导致解码延迟随上下文长度增加；二是过深网络放大非矩阵计算开销，降低 Cube 利用率。本文通过引入 DeepSeek Sparse Attention (DSA) 与 IndexShare，并调整深度-宽度拓扑，解决上述问题。

### 核心创新：稀疏注意力与跨层索引复用

在长上下文注意力设计中，标准做法是使用 MLA 压缩 KV 表示，但主注意力仍需访问大量历史 KV 状态。本文引入 DSA，使用 lightning indexer 为每个查询选择 Top-$K$ 历史 KV 状态，使主注意力仅关注稀疏子集。为进一步减少重复索引计算，本文提出 IndexShare，跨层复用稀疏索引。这一设计解决了 DSA 在长上下文和高并发解码工作负载中索引计算冗余的问题。

$$
\text{Attention}(Q, K, V) = \text{Softmax}\left(\frac{Q K_{\text{Top-}K}^T}{\sqrt{d}}\right) V_{\text{Top-}K}
$$

该公式表示主注意力仅对 Top-$K$ 历史 KV 状态进行计算，显著降低了 HBM 访问压力。IndexShare 通过跨层复用这些 Top-$K$ 索引，进一步减少了 Vector 计算瓶颈，提升了 Cube 利用率。

### 核心创新：宽而浅拓扑与无流水线并行

在深度-宽度权衡中，标准做法是通过增加层数提升模型容量，但这在 Ascend 上会放大非矩阵计算开销。本文采用“宽而浅”拓扑，将层数从 60 层减少至 45 层，同时增加专家中间层大小和每 Token 激活专家数。这一设计增加了每层矩阵乘法的规模，提升了 Cube 利用率，减少了跨层调度和通信开销。

在系统层面，标准做法是使用流水线并行（PP）缓解内存压力，但 PP 引入了结构性流水线气泡。本文提出拓扑感知的混合分片数据并行（Hybrid Sharded Data Parallelism, HSDP），在 SuperPoD 内部进行 FSDP 分片，跨 SuperPoD 进行复制。这一设计将频繁的权重收集和梯度同步限制在高带宽的 SuperPoD 内部，消除了 PP 气泡。

$$
\text{Bubble Fraction} = \frac{p-1}{m+p-1}
$$

该公式表示 1F1B 调度下的理论气泡比例，其中 $p$ 为流水线阶段数，$m$ 为微批次大小。HSDP 通过消除 PP（$p=1$），将气泡比例降至 0，显著提升了训练吞吐量。

## 实验评估

### 实验设置与主结果

本文在 Ascend 910C 集群上评估了 Xing 4 系列模型的推理效率与训练吞吐量。基线覆盖包括 MLA、MLA+DSA、MLA+DSA+IndexShare，以及 MTP3 和 DSpark 推测解码方法。缺失知识库中常见的纯 SSM（如 Mamba）或线性注意力基线对比。

| Architecture | KV HBM Access | Index Computation | Relative TTFT | Relative TPOT | Prefill Throughput | Decode Throughput |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MLA | 1.00 $\times$ | None | 1.00 $\times$ | 1.00 $\times$ | 1.00 $\times$ | 1.00 $\times$ |
| MLA + DSA | 0.85 $\times$ | Per-DSA-layer | 0.37 $\times$ | 0.84 $\times$ | 2.67 $\times$ | 1.18 $\times$ |
| MLA + DSA + IndexShare | 0.80 $\times$ | Cross-layer | 0.21 $\times$ | 0.79 $\times$ | 4.68 $\times$ | 1.27 $\times$ |

MLA+DSA+IndexShare 在 Prefill 吞吐量上达到 MLA 基线的 4.68 倍，Decode 吞吐量为 1.27 倍，验证了稀疏注意力与跨层索引复用的有效性。

### 消融与设计决策验证

本文对比了 Base、MTP3 和 DSpark 在六个基准上的解码吞吐量。DSpark 在所有基准上均优于 MTP3，最大增益出现在 HumanEval 上。

| Benchmark | Output Throughput (tokens/s) | MTP3/Base | DSpark/Base | DSpark/MTP3 |
| :--- | :--- | :--- | :--- | :--- |
| GSM8K | 35.4 / 63.7 / 115.8 | $1.80\times$ | $3.28\times$ | $1.82\times$ |
| MATH-500 | 36.8 / 70.0 / 128.1 | $1.90\times$ | $3.49\times$ | $1.83\times$ |
| HumanEval | 35.7 / 64.1 / 134.7 | $1.80\times$ | $3.77\times$ | $2.10\times$ |
| MBPP | 37.1 / 70.0 / 132.0 | $1.89\times$ | $3.56\times$ | $1.89\times$ |
| AIME25 | 37.0 / 71.5 / 109.2 | $1.93\times$ | $2.95\times$ | $1.53\times$ |
| LiveCodeBench | 35.6 / 64.5 / 95.2 | $1.81\times$ | $2.67\times$ | $1.48\times$ |

DSpark 在 HumanEval 上达到 Base 的 3.77 倍，MTP3 的 2.10 倍，表明块级草稿模型与轻量级 Markov 头在 Ascend 上具有显著优势。

### 评估边界与可复现性

本文主要使用仿真模型评估推理效率，仿真结果可能比全端到端部署测量更乐观。代码方面，开源了 Xing4.0-29B-A4B 模型，但未提供完整训练框架（MindSpore HyperParallel）的开源代码，可复现性受限。

## 关联研究分析

从问题动机看，本文与 DeepSeek-V2/V3 直接相关，均针对长上下文推理瓶颈。DeepSeek 提出 MLA 与 DSA，本文在此基础上引入 IndexShare 跨层复用索引，并针对 Ascend 硬件特性调整深度-宽度拓扑。这一差异源于 Ascend 的 Vector 算力瓶颈，而非架构本质，表明硬件特性对架构设计具有决定性影响。

从方法设计看，本文与 FlashAttention 同属系统级优化路线。FlashAttention 通过 IO 感知的分块计算优化 GPU 内存带宽利用率，本文则通过 HSDP 消除 PP 气泡，并针对 Ascend SuperPoD 带宽层级进行拓扑感知分片。这一差异表明，系统级优化需紧密结合具体硬件架构，通用 GPU 架构设计的普适性在异构硬件上受到挑战。

## 总结

本文要解决的核心矛盾是 Ascend 硬件上高效 LLM 架构与系统协同设计的缺失。本文抓住 Ascend Cube/Vector 异构特性这一被忽略的点，通过“宽而浅”拓扑与无 PP 系统优化，实现了高效训练与推理。本文提出了 MLA+DSA+IndexShare 注意力设计与 HSDP 系统方案，证明了在 Ascend 上 Prefill 吞吐量可达 MLA 基线的 4.68 倍，DSpark 解码吞吐量可达 Base 的 3.77 倍。本文的边界在于仿真结果与真实部署的差距，以及未提供完整训练框架代码。当支持集增大到 5-shot 时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2611.22115)