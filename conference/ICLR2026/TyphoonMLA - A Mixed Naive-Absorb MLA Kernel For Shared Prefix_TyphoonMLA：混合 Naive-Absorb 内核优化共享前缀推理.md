# ICLR2026最新论文 ｜TyphoonMLA: A Mixed Naive-Absorb MLA Kernel For Shared Prefix ｜TyphoonMLA：混合 Naive-Absorb 内核优化共享前缀推理

作者：Ahmet Caner Yüzügüler、Ahmet Çelik、Jiawei Zhuang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.21081)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.21081)

> 导读 大语言模型推理中，Multi-Head Latent Attention (MLA) 架构因低秩压缩 KV 缓存而成为前沿模型标配，但其现有内核在存在共享前缀（如系统提示词）时无法充分利用数据复用机会。现有 Absorb 实现虽节省带宽却受限于计算瓶颈，Naive 实现虽计算高效却内存开销大，两者均无法在共享与非共享区域同时达到最优。TyphoonMLA 通过动态混合两种实现，在计算受限区域使用 Naive 公式，在内存受限区域使用 Absorb 公式，实现了数学等价下的性能突破。该方法在 NPU 和 GPU 上分别将注意力吞吐量提升最高 3× 和 3.24×，但仅针对 MLA 架构，且加速效果高度依赖共享前缀长度与批处理大小的匹配。

## 研究背景

当推理服务处理大量并发请求时，系统提示词（System Prompt）往往长达数万 Token，这些共享前缀在多个查询间重复出现，构成了显著的数据复用机会。然而，MLA 架构的 Absorb 实现将 KV 缓存压缩至低秩潜空间，虽降低了内存带宽需求，却因查询侧的额外投影操作导致计算量激增，使得共享前缀的复用无法转化为实际加速。相反，Naive 实现保持 KV 缓存未压缩，计算量较低但内存访问量大，在批处理较小时因内存带宽瓶颈而性能受限。

MLA 架构源于 DeepSeek-v2 等模型，其核心创新在于通过低秩联合压缩机制减少 KV 缓存大小，并允许两种功能等价但计算特性不同的内核实现：Naive（计算高效，内存密集）与 Absorb（内存高效，计算密集）。在训练和预填充阶段，Naive 实现因计算受限而占优；在解码阶段，Absorb 实现因内存带宽受限而占优。然而，当存在共享前缀时，现有内核未能利用这一特性：Absorb 内核因计算瓶颈无法从数据复用中获益，Naive 内核则因内存开销在批处理较小时性能下降。TyphoonMLA 的切入点在于识别出共享前缀区域属于计算受限场景，非共享区域属于内存受限场景，从而为两种实现提供了协同工作的理论基础。

## 核心方法

### 方法参照系

MLA 内核优化的标准流程通常针对 MHA 或 GQA 架构，通过 IO 感知分块或分页管理降低内存带宽瓶颈。本文问题的关键差异在于 MLA 特有的双实现特性：Naive 与 Absorb 在计算与内存特性上互补，且共享前缀的存在使得单一实现无法在所有区域达到最优。

### 动态混合内核设计

TyphoonMLA 的核心创新在于将注意力计算划分为共享与非共享两部分，分别应用 Naive 与 Absorb 公式。在解码阶段，查询向量 $Q$ 被拆分为 $Q_N$ 和 $Q_R$，其中 $Q_R$ 应用旋转位置编码。共享 KV 缓存 $C_K, C_V$ 以未压缩形式存储，非共享缓存 $C_N, C_R$ 以潜空间形式存储。Naive 分量计算为：

$$ O_N, l_N = \text{softmax}(Q_K C_K^\top) C_V $$

Absorb 分量计算为：

$$ O_A, l_A = \text{softmax}(Q_A C_N^\top + Q_R C_R^\top) C_N $$

其中 $Q_A = Q_N W_{KVb1}$。最终输出通过 LSE 合并：

$$ O = \text{combine}(O_N, O_A, l_N, l_A) $$

这一设计解决了 Absorb 内核在共享前缀区域因计算瓶颈导致的性能损失，同时避免了 Naive 内核在非共享区域因内存带宽瓶颈导致的性能下降。

### 动态回退机制

为防止小批处理下 Naive 实现的内存开销超过收益，TyphoonMLA 引入基于批处理大小的动态回退机制。当批处理大小 $B$ 低于阈值 $B_\theta$ 时，系统自动切换至纯 Absorb 内核。阈值 $B_\theta$ 由硬件参数（吞吐量 $T$ 和 HBM 带宽 $M$）与架构参数决定，对于 DeepSeek-v3 在 Ascend NPU 上，$B_\theta = 61$。该机制确保了在小批处理场景下不产生性能惩罚，实现了全批处理范围的高效性。

## 实验评估

实验在 Ascend NPU（376 TOPS/s，1.8 TB/s HBM）和 GPU（1 PetaFLOPS/s，3.3 TB/s HBM）上进行，使用 MMLU、GSM8K 和 SimpleQA 数据集，批处理大小为 64 至 1024。基线包括 FlashMLA、FlashInfer（Absorb-only）和 PagedAttentionMLA。TyphoonMLA 在所有数据集、系统提示词和批处理大小上均优于基线，NPU 上加速 1.2×-3×，GPU 上最高 3.24×。

| 硬件 | 模型 | 数据集 | 提示词 | 批处理 | TyphoonMLA TGR (kToken/s) | FlashMLA TGR (kToken/s) | 加速比 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| NPU | DeepSeek-v3 | MMLU | A | 128 | 1.48 | 1.01 | 1.46 |
| NPU | DeepSeek-v3 | MMLU | B | 128 | 2.37 | 2.04 | 1.16 |
| NPU | DeepSeek-v3 | MMLU | C | 128 | 2.56 | 2.33 | 1.10 |
| GPU | Kimi K2 | MMLU | A | 1024 | 3.24× | - | 3.24 |

消融实验显示，系统提示词长度对加速比影响显著：Prompt A（26472 Token）的加速比最高，因其共享比例最大。Kimi K2 的加速比高于 DeepSeek-v3，因其注意力头数较少（64 vs 128），对数据复用更敏感。

评估边界方面，论文未报告置信区间，且仅在 MLA 架构上验证，缺乏跨架构通用性测试。代码已开源，但超参数（如 $B_\theta$）需根据硬件调整，可复现性依赖于特定硬件配置。

## 关联研究分析

从问题动机看，TyphoonMLA 与 FlashAttention 和 PagedAttention 同属系统级优化路线，但针对 MLA 特有的双实现特性。FlashAttention 通过 IO 感知分块优化 MHA/GQA 内核，PagedAttention 通过分页管理解决 KV 缓存碎片问题，两者均未考虑 MLA 的 Naive/Absorb 混合潜力。TyphoonMLA 的创新在于识别出共享前缀区域属于计算受限场景，从而为 Naive 实现提供了应用空间，这是现有内核未探索的盲区。

从方法设计看，TyphoonMLA 与 ProxyAttn 和 STILL 等动态路由方法有相似之处，均通过动态选择计算路径优化性能。但 ProxyAttn 在头间协同稀疏化，STILL 在层内混合注意力分支，而 TyphoonMLA 在 MLA 内核层面混合 Naive 与 Absorb 实现。这种差异源于任务特性：MLA 的双实现特性使得内核层面的混合比架构层面的路由更直接有效。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

TyphoonMLA 解决了 MLA 架构在共享前缀场景下无法充分利用数据复用机会的问题，其切入点在于识别出共享区域属于计算受限、非共享区域属于内存受限，从而为 Naive 与 Absorb 实现提供了协同工作的理论基础。该方法通过动态混合两种实现，在 NPU 和 GPU 上分别将注意力吞吐量提升最高 3× 和 3.24×，且仅增加 3% 的 HBM 开销。其边界在于仅针对 MLA 架构，且加速效果高度依赖共享前缀长度与批处理大小的匹配，当共享比例较低或批处理较小时，收益显著下降。当共享前缀长度缩短至数千 Token 时，Naive 实现的内存开销是否仍能被计算收益抵消，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.21081)