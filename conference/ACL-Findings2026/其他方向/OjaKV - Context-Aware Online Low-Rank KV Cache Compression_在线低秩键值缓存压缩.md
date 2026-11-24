# ACL-Findings2026最新论文 ｜OjaKV: Context-Aware Online Low-Rank KV Cache Compression ｜在线低秩键值缓存压缩

研究机构：美国伦斯勒理工学院、IBM研究院

作者：Yuxuan Zhu、David H. Yang、Mohammad Mohammadi Amiri 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.21623)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.21623)

> 长上下文推理中，键值缓存（KV Cache）随序列长度线性增长，导致显存溢出。现有低秩近似方法依赖静态离线学习的投影基，在推理时面对分布漂移会失效。OjaKV通过混合存储策略保留高误差Token的全秩表示，并利用Oja规则在线更新投影基，解决了静态基的适应性不足问题。该方法在生成任务上显著优于静态基线，但其绝对精度仍远低于量化与驱逐路线，且未与这些主流方法直接对比。

## 研究背景

自回归解码阶段，每生成一个新Token需读取整个历史KV缓存，受限于内存带宽而非算力。当处理32K Token提示时，Llama-3.1-8B模型的KV缓存占用约16 GB，与模型权重相当。这种内存压力促使研究者探索压缩策略，其中低秩近似通过将Key和Value向量投影到低维子空间，可将缓存内存减少 $(1 - r/d) \times 100\%$，例如从维度 $d=128$ 压缩至 $r=96$。然而，低秩近似的有效性依赖于投影基对数据分布的覆盖程度。

现有低秩方法主要分为权重分解与投影基两类。权重分解技术（如Palu）直接分解投影权重，但常伴随精度损失；投影基技术（如EigenAttention, StaticPCA）从校准数据学习固定正交基，假设推理提示与校准数据同分布。这一假设在实际场景中频繁失效，例如从对话任务切换到代码生成时，静态基的投影误差显著增加。OjaKV的切入点在于识别出“静态基在分布漂移下的失效”这一被忽略的问题，并提出在线自适应机制，使投影基能随推理过程动态调整，从而在保持低秩压缩优势的同时，适应不断演变的上下文分布。

## 核心方法

### 低秩KV缓存近似参照系

标准注意力机制中，Key和Value矩阵 $\mathbf{K}, \mathbf{V} \in \mathbb{R}^{n \times d_h}$ 被完整缓存。低秩近似引入正交基 $\mathbf{U}_k \in \mathbb{R}^{d_h \times r_k}$ 和 $\mathbf{U}_v \in \mathbb{R}^{d_h \times r_v}$，将 $\mathbf{K}$ 和 $\mathbf{V}$ 投影至低维空间存储，解码时重构。本文的关键差异在于：投影基 $\mathbf{U}_k, \mathbf{U}_v$ 不再是静态固定的，而是根据当前上下文在线更新，且部分高误差Token保留全秩表示。

### 基于重构误差的混合存储策略

静态低秩方法对所有Token均匀压缩，但注意力机制中少数“重击者”Token对生成质量起决定性作用，且这些Token往往在低秩重构中误差最大。OjaKV通过计算每个Key Token的重构残差 $\mathbf{r}_t = \mathbf{k}_t - \mathbf{U}_k \mathbf{U}_k^\top \mathbf{k}_t$，并利用滑动窗口内查询的注意力权重加权，识别出对注意力输出扰动最大的Token。具体地，查询加权误差分数定义为：

$$
S_t = \sum_{q \in Q_{win}} \alpha(q, t) \|\mathbf{r}_t\|_2
$$

其中 $\alpha(q, t)$ 为查询 $q$ 对Token $t$ 的注意力权重。保留误差分数最高的Top-$k$ Token为全秩表示，其余Token进行低秩压缩。这一设计解决了静态位置启发式（如保留前几个Token作为“注意力汇聚点”）无法适应动态上下文的问题，确保高误差Token作为注意力的稳定锚点，从而在理论上界定了压缩引起的注意力输出误差。

### 基于Oja规则的在线子空间适应

静态基在解码阶段无法追踪新生成Token引入的分布偏移，导致累积误差。OjaKV采用Oja规则（Oja, 1997）进行在线主成分分析，增量更新投影基。在预填充阶段，对提示中的显著Token进行批量更新；在解码阶段，每 $T$ 步对缓冲区中的新Key-Value对执行轻量级更新：

$$
\mathbf{U} \leftarrow \mathbf{U} + \eta (\mathbf{x}\mathbf{x}^\top \mathbf{U} - \mathbf{U}\mathbf{U}^\top \mathbf{x}\mathbf{x}^\top \mathbf{U})
$$

其中 $\eta$ 为学习率，$\mathbf{x}$ 为新样本。该更新可视为对迹 $\text{tr}(\mathbf{U}^\top \mathbf{C} \mathbf{U})$ 的随机梯度上升，隐含正交性约束。预填充阶段使用局部平均池化降低计算成本，解码阶段通过周期性更新平衡适应性与稳定性。这一机制使低秩子空间持续追踪演变的Key-Value分布，解决了静态基在长序列生成中精度逐渐崩溃的问题。

## 实验评估

实验在NVIDIA H100 GPU上进行，使用Llama-2-7B和Llama-3.1-8B模型，评估基准包括RULER、LongBench和AIME 2025。基线覆盖静态低秩方法（Eigen-N, StaticPCA, Palu），但缺失量化（KIVI, KVQuant）和驱逐（H2O, SnapKV）等主流强基线，限制了跨路线的公平比较。

| 方法 | RULER Avg (16K, 0.8x) | LongBench Avg (Llama-3.1-8B, 0.8x) | AIME 2025 |
| :--- | :--- | :--- | :--- |
| Full KV | 74 | 33.7 | 43.3 |
| StaticPCA | 28.37 | 29.48 | 0 |
| Palu | 44.85 | 29.81 | 0 |
| OjaKV | 54.19 | 29.81 | 13.0 |

在RULER基准上，OjaKV在0.8x压缩率下平均准确率为54.19%，显著优于StaticPCA的28.37%和Palu的44.85%，但仍低于Full KV的74%。在LongBench上，OjaKV与Palu持平（29.81%），略低于StaticPCA（29.48%），表明在长文本生成任务中，在线适应的收益有限。在AIME 2025上，所有静态基线均失败（0%），而OjaKV保持13.0%的准确率，验证了在线子空间适应对复杂推理任务的必要性。

消融实验显示，混合存储策略贡献了最大的性能增益，将RULER平均准确率从StaticPCA的38.9%提升至57%；在线Oja更新在此基础上进一步将准确率提升至60%。解码延迟方面，OjaKV在 $T=64$ 时延迟为41.38 ms/token，相比Full KV的36.48 ms/token增加约13.4%，而StaticPCA仅增加0.3%。这表明在线更新引入了可接受的计算开销，但并非零成本。

评估边界方面，论文未报告置信区间，且仅在Llama-2-7B和Llama-3.1-8B上验证，未覆盖更大规模模型。代码已开源，但超参数（如学习率 $\eta$、更新间隔 $T$）的敏感性分析未在正文中详细展示。

## 关联研究分析

从问题动机看，OjaKV与SnapKV均关注Token重要性，但选择标准不同。SnapKV基于注意力分数筛选Prompt Token，假设重要性在预填充阶段即可确定；OjaKV基于重构误差，动态识别在低秩压缩下损失最大的Token。这一差异源于任务特性：SnapKV适用于固定Prompt的长上下文问答，而OjaKV针对自回归生成中分布漂移的场景。然而，OjaKV未与SnapKV直接对比，无法量化误差驱动选择相对于注意力分数选择的增益。

从方法设计看，OjaKV与MLA（Multi-Head Latent Attention）均利用低秩特性，但MLA是架构级优化，需重训练模型；OjaKV是推理时优化，无需修改模型权重。MLA从源头减少KV生成量，而OjaKV在生成后压缩。这一差异决定了适用场景：MLA适用于新模型设计，OjaKV适用于现有预训练模型的部署。OjaKV的在线更新机制是否能在MLA架构中进一步降低低秩子空间的维度，论文未探索。

## 总结

OjaKV旨在解决静态低秩基在推理时分布漂移下的失效问题，通过混合存储策略保留高误差Token的全秩表示，并利用Oja规则在线更新投影基，实现了无需重训练的自适应压缩。实验表明，OjaKV在AIME 2025上保持13.0%的准确率，而静态基线均为0%，验证了在线适应对复杂推理任务的关键作用。然而，OjaKV在LongBench上的表现与静态基线持平，且绝对精度远低于量化和驱逐路线的SOTA，暴露了低秩压缩在长文本生成任务中的局限性。当上下文长度超过32K时，在线更新的累积误差是否会导致精度进一步下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.21623)