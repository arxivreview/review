# HuggingFace最新推荐论文 ｜Token Sparse Attention: Efficient Long-Context Inference with Interleaved Token Selection ｜Token稀疏注意力

研究机构：韩国首尔大学

作者：Dongwon Jo、Beomseok Kang、Jiwon Song 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.03216)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.03216)

> 长上下文推理中，Prefill阶段的二次方计算复杂度是核心瓶颈，现有稀疏方法因Block级粒度或Token驱逐的不可逆性，无法适应层间与头间的动态重要性变化。本文提出Token稀疏注意力（Token Sparse Attention, TSA），通过“压缩-解压”机制在注意力计算前动态筛选Token，并在输出后恢复序列维度，使被忽略的Token在后续层可被重新评估。该方法作为正交插件与现有稀疏内核组合，在128K上下文下实现最高3.23倍加速且精度损失小于1%。其价值在于以极小开销解锁了Token级粒度的动态稀疏，但实验仅覆盖Prefill阶段，未验证其在Decoding阶段对KV Cache读取的潜在优化作用。

## 研究背景

长上下文推理面临Prefill阶段计算量随序列长度 $L$ 呈 $O(L^2)$ 增长的瓶颈。FlashAttention通过IO感知优化降低了内存访问开销，但未改变算法本身的二次方复杂度。为突破此限制，稀疏注意力成为主流路线，其核心思想是跳过注意力矩阵中低重要性区域的计算。然而，现有方法多采用Block级稀疏以兼容硬件内核执行模式，导致同一Block内的低信息量Token被强制保留，造成稀疏率次优。另一类Token级方法（如FastKV）在早期层筛选重要Token后永久驱逐其余Token，但Token重要性在深层会发生显著漂移，这种不可逆决策导致后续层无法重新评估早期被误删的关键信息，形成精度-速度权衡的短板。

稀疏注意力的有效性高度依赖于稀疏模式对动态注意力分布的适应能力。静态或基于早期层决策的模式无法捕捉层间与头间的特异性变化，这在长序列中尤为致命。本文切入点在于解决Token级稀疏的“不可逆性”问题：不永久删除Token，而是通过临时压缩与恢复机制，让每个注意力头在每一层都能独立选择其关注的Token子集，从而在保持硬件兼容性的同时实现细粒度的动态稀疏。

## 核心方法

### 方法参照系

本文问题属于稀疏注意力加速范畴，与FlexPrefill等Block级动态稀疏方法同属“跳过低重要性计算”的通用流程。关键差异在于粒度与可逆性：标准流程在Block级施加静态或动态掩码，或Token级永久驱逐；本文改为Token级动态选择，并通过“压缩-解压”设计确保被忽略的Token在后续层可被重新访问，避免了早期决策的永久性约束。

### 压缩-解压机制

该机制解决了Token驱逐方法中“早期层决策锁定后续层”的失效问题。在Stage 1，每个头 $h$ 独立选择Token子集 $S_h$，将 $Q, K, V$ 压缩至 $\hat{Q}, \hat{K}, \hat{V}$，注意力计算复杂度从 $O(L^2 d)$ 降至 $O(L'^2 d)$。Stage 2将压缩输出 $\hat{O}$ 散射回零初始化的 $L \times d$ 张量，未选位置保持零值。这一设计的关键在于：零值填充与残差连接结合，使得未选Token的信息通过残差流保留，而非被彻底丢弃。公式表达为：

$$ O_{t} = \begin{cases} \hat{O}_{t} & \text{if } t \in S_h \\ 0 & \text{otherwise} \end{cases} $$

物理含义是：当前层仅对选中的Token进行上下文聚合，未选Token的表示由上一层残差直接传递，从而在下一层可被重新评分与选择。

### 动态Token覆盖率

该策略解决了固定稀疏率无法适应不同层重要性分布的问题。通过轻量级代理注意力图 $\hat{A}$ 计算Token级分数 $s_h$，再聚合为层级分布 $s_l$。稀疏预算 $k_{sparse}$ 由累积重要性阈值 $\tau$ 动态确定：

$$ k_{sparse} = \arg\min_{k \in \{0,\dots,L\}} \sum_{j=1}^{k} s_{l}[I_j] \geq \tau $$

其中 $I$ 为按升序排列的Token索引。该公式意味着：从最不重要的Token开始累加，直到累积贡献超过阈值 $\tau$，从而自适应地确定每层应跳过的Token数量。这种基于分布的预算分配比固定比例更精准地匹配了长序列中注意力噪声的长尾特性，实现了结构化的正则化效果。

## 实验评估

实验在LLaMA-3.1-8B-Instruct与Mistral-Nemo-12B-Instruct上验证，基线覆盖FlashAttention（稠密）、Minference（结构化稀疏）、FlexPrefill（Block级动态稀疏）及FastKV/GemFilter（Token驱逐）。主结果显示，TSA作为插件与FlexPrefill组合时，在RULER基准上保持87.27%平均准确率不变，而128K上下文加速比从2.44倍提升至2.76倍。

| 方法 | RULER Avg (%) | 128K Speedup |
| :--- | :--- | :--- |
| FlexPrefill | 87.27 | ×2.44 |
| FlexPrefill + TSA | 87.27 | ×2.76 |
| FlashAttention | 87.01 | ×1.00 |
| FlashAttention + TSA | 87.02 | ×1.36 |

消融实验表明，动态稀疏在相同加速比下显著优于固定稀疏。当加速比匹配为×1.51时，动态稀疏准确率为86.84%，而固定稀疏仅为85.43%。这一差距在高稀疏率下更为明显，验证了基于注意力分数分布分配预算的有效性。此外，TSA的额外开销（Token评分与索引）在128K上下文下占总注意力延迟的比例低于11%，确证了其轻量级特性。

评估边界方面，实验仅覆盖Prefill阶段，未测试Decoding阶段对KV Cache的影响。超参数 $\tau$ 在LLaMA与Mistral上分别设为0.005与0.008，但未提供跨模型的系统性调参协议。代码已开源，但实验仅在单卡A100上进行，未验证多卡并行下的扩展性。

## 关联研究分析

从问题动机看，TSA与FlexPrefill同属动态稀疏路线，但前者聚焦Token级粒度，后者限于Block级。FlexPrefill的Block级稀疏受硬件内核执行模式约束，无法在Block内部进一步剔除低信息量Token；TSA通过压缩-解压机制解耦了稀疏粒度与硬件兼容性，使得Token级选择成为可能。这一差异的根源在于：Block级稀疏是硬件友好的妥协，而TSA证明了在保持硬件兼容的前提下，细粒度稀疏可通过算法设计实现。

从方法设计看，TSA与FastKV等Token驱逐方法形成鲜明对比。FastKV在早期层永久删除Token，假设重要性稳定；TSA则通过残差流保留未选Token信息，允许后续层重新评估。这一设计选择源于对层间重要性漂移的观察：Figure 2(a)显示相邻层Top-1% Token重叠率随层距增加而快速下降。TSA的可逆性设计直接针对这一失效模式，而FastKV的不可逆性则导致其在长序列中精度-速度权衡劣于TSA。

## 总结

本文核心矛盾在于：Token级稀疏的细粒度优势与早期决策不可逆性之间的冲突。TSA通过“压缩-解压”机制解决了这一矛盾，使每个头在每层都能独立选择Token，同时通过残差流保留未选信息。实验证明，与FlexPrefill组合后，在128K上下文下实现2.76倍加速且精度无损。其边界在于：实验仅覆盖Prefill阶段，未验证TSA在Decoding阶段对KV Cache读取的优化潜力；且动态稀疏预算 $\tau$ 的设定依赖经验值，缺乏理论指导。当序列长度超过128K时，动态稀疏的累积误差是否会显著影响长程依赖捕捉，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.03216)