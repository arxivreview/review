# HuggingFace最新推荐论文 ｜Training-free Latent Inter-Frame Pruning with Attention Recovery ｜潜空间帧间剪枝与注意力恢复

研究机构：美国德克萨斯大学奥斯汀分校

作者：Dennis Menn、Yuedong Yang、Bokun Wang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.05811)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.05811)

> 视频生成模型在单卡上难以达到30 FPS的实时交互标准，主要瓶颈在于Transformer对每个Token分配固定计算量，忽略了内容中的时空冗余。现有Token合并方法因训练-推理差异导致伪影，且仅作用于部分层。LIPAR通过识别潜空间中的冗余帧间Patch并执行端到端剪枝，同时引入注意力恢复机制近似未剪枝序列的输出，以消除伪影。该方法在保持视觉质量的前提下实现了1.45倍加速，但其加速幅度仍不足以独立满足高帧率实时需求。

## 研究背景

视频生成依赖潜在扩散模型（LDM）在紧凑潜空间执行去噪，其计算复杂度随Token数量呈二次增长。传统视频压缩利用像素域的帧间冗余跳过重复块，但LDM的潜空间是否保留这种冗余性缺乏理论保证，导致现有加速方法无法直接复用像素域策略。

当前加速路线分为减少去噪步数（如CausVid）和减少Token数量（如ToMe）两类。减少步数受限于蒸馏质量，而Token合并方法（ToMe, IDM）通过匹配相似Token降低计算量，但存在两个缺陷：一是确定相似Token的开销大且仅限特定层，二是直接合并破坏了因果注意力骨干的训练分布，引发视觉伪影。LIPAR的切入点在于验证潜空间与像素空间的时间变化强相关性，从而将“帧间压缩”概念迁移至潜空间，并通过数学近似解决剪枝带来的分布偏移。

## 核心方法

### 方法参照系

本文问题属于推理加速中的Token剪枝范畴。标准流程为：在Transformer各层识别冗余Token并合并或丢弃，以降低$O(N^2)$注意力计算量。本文与通用剪枝的关键差异在于：剪枝对象限定为时间轴上的冗余Patch，且必须保证剪枝后的注意力输出近似于完整序列，而非仅保留语义重要Token。

### 潜空间帧间剪枝（LIF Pruning）

设计动机：解决现有Token合并方法因逐层计算相似度带来的高开销，以及仅作用于部分层导致的全局加速受限问题。LIPAR在潜空间执行端到端剪枝，利用像素空间与潜空间时间变化的Pearson相关性（WAN 2.2 VAE为0.77），直接比较相邻帧同一空间位置的Patch差异。当$L_1$范数小于阈值$\tau$时，标记该Patch为冗余并跳过计算。该操作将序列长度$N$缩减，使所有后续层均受益，避免了逐层匹配的计算负担。

### 注意力恢复（Attention Recovery）

设计动机：解决直接剪枝导致的训练-推理差异，即剪枝序列的自注意力输出与完整序列不一致，引发伪影。LIPAR提出M-Degree Approximation与Noise-Aware Duplication机制。核心公式为近似自注意力输出：

$$
\hat{A} \approx \sum_{j \in M} \exp\left(\frac{q^T k_j}{\sqrt{D}}\right) v_j
$$

其中$M$为与查询$q$距离最近的$m$个保留Token索引。该公式通过从KV-Cache中复制时间对应Token的Key和Value向量，确保$m$个最近邻Token未被剪枝，从而在数学上近似完整序列的注意力分布。同时，Noise-Aware Duplication仅复制“干净”Token（无独立噪声扰动），避免违反扩散模型的I.I.D.噪声假设，防止注意力分数中的二次噪声项导致方差爆炸。

## 实验评估

实验基于DAVIS数据集的51个视频-文本对，在NVIDIA A6000 GPU上评估。基线覆盖Self-Forcing（因果注意力骨干）、StreamV2V、StreamDiffusion及ControlVideo等实时视频编辑模型，以及ToMe、IDM等训练-free剪枝方法。LIPAR在吞吐量上达到12.2 FPS，较Self-Forcing的8.4 FPS提升1.45倍，GPU显存占用从26.24 GB降至18.56 GB（减少29%）。

| 方法 | 吞吐量 (FPS) | 加速比 | 显存 (GB) |
|---|---|---|---|
| Self-Forcing | 8.4 | 1.00 × | 26.24 |
| LIPAR | 12.2 | 1.45 × | 18.56 |
| StreamV2V | 5.9 | 2.07 × | — |
| StreamDiffusion | 9.1 | 1.34 × | — |

在质量评估中，14名参与者的双盲测试显示，LIPAR与未剪枝Self-Forcing的Win-Tie率为86.4%（18.4%胜，68.3%平，13.3%负），优于StreamV2V（92.4% Win Rate）和ControlVideo（84.9% Win Rate）。消融实验表明，仅使用M-Degree Approximation会引入噪声图案，结合Noise-Aware Duplication后伪影消失。

评估边界：实验仅覆盖480×832分辨率和72帧视频，未测试更高分辨率或长视频下的稳定性。代码未公开，且未报告不同剪枝率（10%-32%）下的详细质量-速度权衡曲线，仅定性指出32%剪枝率下质量保持最佳。

## 关联研究分析

从问题动机看，LIPAR与FlowCodec等生成式压缩方法均利用LDM先验，但目标函数不同：压缩优化率失真（以计算换带宽），LIPAR优化推理延迟（以计算换时间）。LIPAR的剪枝策略本质是空间-时间维度的稀疏化，而FlowCodec通过单步流匹配减少时间步数。两者在数学上均涉及信息丢弃，但LIPAR的丢弃基于内容冗余，FlowCodec的丢弃基于噪声调度，前者对内容动态敏感，后者对模型架构敏感。

从方法设计看，LIPAR与ToMe同属Token剪枝路线，但ToMe依赖二分匹配确定相似Token，计算开销大且仅限Self-Attention层；LIPAR利用帧间时序冗余，剪枝决策在潜空间前置，且通过Attention Recovery解决跨层一致性。ToMe的合并操作破坏了Token的独立性，而LIPAR的剪枝保留了保留Token的完整上下文，通过KV-Cache复制实现近似，这在因果注意力骨干中更为关键，因为因果掩码使得后续Token依赖前序Token的完整状态。

## 总结

LIPAR针对视频生成中固定计算量导致的实时性瓶颈，利用潜空间与像素空间的时序相关性，将传统帧间压缩迁移至潜空间，并通过注意力恢复机制消除剪枝伪影。该方法在A6000上实现12.2 FPS（1.45倍加速）和86.4% Win-Tie率，证明了训练-free剪枝在保持质量下的可行性。其边界在于加速幅度仍低于30 FPS实时标准，且依赖KV-Cache复制，对长序列显存占用敏感。当视频帧数增加至数百帧时，KV-Cache的复制开销是否会抵消剪枝带来的计算节省，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.05811)