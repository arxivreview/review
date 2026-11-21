# HuggingFace最新推荐论文 ｜VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion ｜视频多头潜在注意力

研究机构：美国弗吉尼亚理工大学

作者：Hidir Yesiltepe、Jiazhen Hu、Tuna Han Salih Meral 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.30351)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.30351)

> 流式因果视频生成面临KV缓存内存随序列长度线性增长的瓶颈，现有方法仅优化窗口内Token分布或位置编码，未触及每Token每层的密集KV布局。VideoMLA通过共享低秩内容潜变量与解耦3D-RoPE键，将每Token KV内存压缩92.7%，在保持长程生成质量的同时提升吞吐量。该方法揭示了预训练视频注意力非低秩特性下，MLA瓶颈而非频谱结构决定有效秩的机制，但仅在1.3B骨干上验证，更大规模下的扩展性存疑。

## 研究背景

因果视频扩散模型通过自回归生成帧块并维护滚动KV缓存实现分钟级流式输出，其核心约束是每Token每层的KV状态大小。在Wan-1.3B架构中，每个缓存Token存储$2 \times 12 \times 128 = 3072$个密集KV标量，21帧潜变量缓存导致总内存达6.0GB，迫使系统采用固定滑动窗口限制Token数量，但无法降低单Token的存储成本。

主流路线分为两类：一类在固定窗口内优化Token选择、位置编码或蒸馏目标（如CausVid、Self-Forcing），保留密集KV布局；另一类重构注意力计算（如SANA-Video线性注意力、SCD分层缓存），减少层数或时间维度内存，但未压缩每Token每层的KV状态。VideoMLA的切入点在于直接干预每Token的KV布局，将密集多头KV替换为共享低秩潜变量，解决固定窗口下单Token存储成本过高的问题。

## 核心方法

### 方法参照系

标准因果视频生成采用密集多头注意力，每Token存储所有头的Key和Value向量。本文问题与该通用流程的关键差异在于：不改变窗口大小或层数，而是压缩每Token每层的KV状态维度，从$2n_h d_h$降至$d_c + d_{h}^{[rope]}$。

### 共享低秩内容潜变量

密集KV布局中，每个头独立存储Key和Value，导致内存冗余。VideoMLA引入联合KV下投影$W_{\downarrow}^{[KV]} \in \mathbb{R}^{d_c \times d}$，将输入$x_t$压缩为共享潜变量$c_t^{[KV]}$：

$$c_t^{[KV]} = W_{\downarrow}^{[KV]} x_t$$

该潜变量被所有头共享，通过上投影$W_{\uparrow}^{[K]}, W_{\uparrow}^{[V]}$重建每头Key和Value。设计动机是解决密集布局中多头KV的存储冗余，使单Token缓存从3072标量降至$d_c$标量，实现内存压缩。

### 解耦3D-RoPE位置键

内容潜变量$c_t^{[KV]}$不包含位置信息，导致滑动窗口重索引时位置失效。VideoMLA将每头维度分解为$d_h = d_h^{[nope]} + d_h^{[rope]}$，其中$d_h^{[rope]}$用于存储共享的解耦3D-RoPE键$k_t^{[R]}$：

$$k_t^{[R]} = W_{R}^{[K]} c_t^{[KV]}$$

位置信息通过旋转矩阵在注意力计算时动态应用，而非存储在缓存中。设计动机是分离内容与位置，使缓存状态独立于绝对时间，支持滑动窗口重索引，同时保持长程时序一致性。

## 实验评估

实验基于Wan-2.1 T2V-1.3B骨干，使用VBench评估30s和60s生成质量，基线覆盖Self-Forcing、CausVid、LongSANA等流式方法。VideoMLA在60s整体得分0.859，动态度0.958，均优于所有基线；吞吐量23.96 FPS，延迟3.38s，较Self-Forcing提升1.23倍。

| 方法 | 60s Overall | 60s Dynamic Degree | Throughput (FPS) | Latency (s) |
| --- | --- | --- | --- | --- |
| Self-Forcing | 0.654 | 0.624 | 18.06 | 4.19 |
| LongSANA | 0.673 | 0.149 | 19.35 | 4.48 |
| VideoMLA | 0.859 | 0.958 | 23.96 | 3.38 |

消融实验显示，$d_c=192$时内存斜率从MHA的6.26 GB/batch降至0.82 GB/batch，支持8.0倍批处理扩展；$d_c=64$时质量下降，验证潜变量预算与质量的权衡。

评估边界限于1.3B骨干和单GPU，未测试14B模型或高分辨率；VBench未包含分钟级时序一致性盲测，用户研究样本量未报告。代码未开源，超参数（如$d_q=768$）未提供完整复现细节。

## 关联研究分析

从方法设计看，VideoMLA与SANA-Video形成“压缩vs消除”的架构对比：SANA-Video用线性注意力完全移除KV缓存，而VideoMLA保留注意力结构但压缩每Token状态。差异根源在于任务特性：线性注意力在长序列上内存恒定，但可能损失局部细节；MLA压缩在保持局部精度的同时降低内存，但依赖预训练算子的秩特性。VideoMLA证明即使预训练算子非低秩（99%能量秩>1300），MLA瓶颈仍能维持质量，这与语言模型中MLA依赖低秩假设的动机不同。

从问题动机看，VideoMLA与Self-Forcing共享因果生成框架，但Self-Forcing聚焦训练-测试分布对齐，VideoMLA聚焦内存效率。Self-Forcing的密集KV布局是VideoMLA的基线，后者在其上施加MLA压缩，验证了压缩对自回归稳定性的影响。差异在于Self-Forcing未考虑内存约束，而VideoMLA将内存作为核心优化目标，这是否牺牲了某些长程依赖的建模能力，论文未给出回答。

## 总结

VideoMLA解决的核心矛盾是流式视频生成中KV缓存内存随序列长度线性增长，现有方法仅优化窗口内Token分布或位置编码，未触及每Token每层的密集KV布局。VideoMLA通过共享低秩内容潜变量与解耦3D-RoPE键，将每Token KV内存压缩92.7%，在60s生成中达到0.859整体得分和23.96 FPS吞吐量。其边界在于仅在1.3B骨干上验证，未测试更大规模模型或高分辨率，且预训练算子非低秩特性下MLA的有效性机制未完全解释。当骨干规模扩展到14B时，潜变量预算$d_c$的最优值是否随模型维度线性增长，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.30351)