# HuggingFace最新推荐论文 ｜Kronecker Delta Rule for Long Context Linear Attention ｜基于Kronecker Delta Rule的线性注意力架构

作者：Anamaria-Roberta Hartl、Levente Zólyomi、Michael List 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.26834)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.26834)

> 导读：长上下文处理面临二次方计算复杂度与线性内存增长的双重瓶颈，线性注意力通过固定大小矩阵内存实现线性复杂度，但面临内存干扰与数值不稳定问题。现有线性注意力方法如DeltaNet在长序列中因向量残差修正导致存储值相互干扰，而xLSTM依赖归一化状态控制内存规模却引发数值不稳定。本文提出Kronecker Delta Rule，通过标量残差修正沿单一方向更新内存，减少对其他存储值的干扰，并证明内存动态收敛至稳态且期望范数有界。该架构在长上下文检索任务上显著优于DeltaNet家族，但纯线性模型在绝对检索精度上仍受限于架构本身，混合架构是否仍是长上下文最佳实践有待验证。

## 研究背景

当Transformer处理超长序列时，自注意力机制的计算复杂度随序列长度呈二次方增长，键值缓存（KV Cache）内存占用线性膨胀，导致推理成本急剧上升。线性注意力（Linear Attention）通过移除Softmax函数并将注意力转化为递归过程，将计算复杂度降至线性，同时保持恒定内存占用。然而，线性注意力将上下文压缩至固定大小的矩阵内存中，随着序列增长，内存中存储的关联信息相互干扰，导致检索精度下降。

早期线性注意力方法如Hebbian规则采用加性更新，内存随序列增长且无法修正已存储值。DeltaNet家族引入Delta Rule，通过向量残差修正内存，但修正方向依赖当前内存内容，导致重叠键的存储值相互扰动。xLSTM通过归一化状态控制内存规模，但基于大数量比值的归一化在大型网络中引发数值不稳定。本文聚焦于线性注意力中的内存干扰与稳定性平衡，提出最小侵入式内存修正机制，解决长序列下存储值相互干扰的问题。

## 核心方法

### 线性注意力内存更新机制

线性注意力将上下文压缩至矩阵内存 $S \in \mathbb{R}^{d_v \times d_k}$，通过键值对 $(k_t, v_t)$ 更新内存，查询时通过 $h_t = S_t q_t$ 检索信息。传统Hebbian规则采用加性更新 $S_{t+1} = S_t + v_t k_t^\top$，内存随序列增长且无法修正已存储值。Delta Rule通过向量残差修正内存：

$$S_{t+1} = S_t - \beta_t (S_t k_t - v_t) k_t^\top$$

该更新沿 $(S_t k_t - v_t) k_t^\top$ 方向修正，方向依赖当前内存内容，导致重叠键的存储值相互扰动。本文问题与DeltaNet的关键差异在于：DeltaNet修正向量残差，本文修正标量残差，仅沿单一方向更新内存。

### Kronecker Delta Rule

本文提出Kronecker Delta Rule，通过标量残差修正内存，修正方向仅由输入对 $(k_t, v_t)$ 决定，不依赖内存内容：

$$S_{t+1} = S_t - \beta_t (v_t^\top S_t k_t - c_t) v_t k_t^\top$$

其中 $v_t^\top S_t k_t$ 测量内存对 $(k_t, v_t)$ 的关联强度，$c_t$ 为目标值。该更新沿 $v_t k_t^\top$ 方向修正，仅影响键值对 $(k_t, v_t)$ 的关联，对其他存储值的干扰由值重叠与键重叠的乘积控制。相比DeltaNet的向量残差修正，Kronecker Delta Rule的标量修正更精确地定位目标关联，减少对其他存储值的扰动。

### KronLSTM架构

Kronecker Delta Rule嵌入门控线性注意力混合器，形成KronLSTM架构。架构包含三个门控机制：向量遗忘门 $F_t$ 控制内存衰减，擦除门 $\beta_t$ 控制修正强度，写入门 $c_t$ 控制目标值。更新公式为：

$$S_{t+1} = S_t F_t - \beta_t (v_t^\top S_t F_t k_t) v_t k_t^\top + c_t v_t k_t^\top$$

遗忘门 $F_t = \text{diag}(f_t)$ 作用于键维度，保留每个键方向的信息；擦除门 $\beta_t$ 和写入门 $c_t$ 为标量门控，通过输入依赖的sigmoid函数计算。该架构无需归一化状态或稳定化状态，通过Kronecker Delta Rule的数学性质保证内存动态收敛至稳态且期望范数有界。

## 实验评估

实验在FineWeb-Edu数据集上预训练1.5B参数模型，训练上下文长度为8k，评估上下文长度覆盖4k至32k。基线覆盖Gated DeltaNet (GDN)、Kimi Delta Attention (KDA)、Mamba-3、Gated DeltaNet-2 (GDN-2) 和mLSTM，覆盖主流线性注意力方法。

| 模型 | Avg-6 ↑ | LMBppl↓ | SWDE | SQD | FDA | TQA | NQ | DROP | Recallavg↑ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GDN-2 | 58.75 | 8.36 | 29.61 | 36.39 | 19.60 | 60.19 | 14.54 | 19.36 | 29.95 |
| KronLSTM | 60.19 | 7.66 | 31.68 | 39.88 | 18.15 | 60.37 | 15.36 | 21.03 | 31.08 |

KronLSTM在32k上下文扩展后，Avg-6达到60.19，LAMBADA困惑度降至7.66，Recall平均准确率31.08，均优于GDN-2。在RULER NIAH任务上，KronLSTM在16k和32k上下文长度上显著优于GDN-2，尤其在S3和MV任务上优势明显。

消融实验验证了Kronecker Delta Rule各组件的贡献。移除 $\ell_2$ 归一化或耦合擦除与写入门对语言建模影响较小（0.3准确率点内），但固定目标值导致1.6准确率点下降。在NIAH任务上，解耦的擦除与写入门对检索精度至关重要，4k上下文时基础模型比耦合变体高12.6准确率点。

评估协议存在局限：实验未覆盖混合架构中Full Attention层的贡献，纯线性模型在RULER上的绝对精度（16k NIAH最高约17.6%）远低于混合/稀疏SOTA（64.43%），但任务类型和模型规模不同，不可直接比较。代码开源但未提供具体URL，可复现性受限。

## 关联研究分析

从方法设计看，KronLSTM与Gated DeltaNet-2 (GDN-2) 同属DeltaNet家族，均解耦擦除与写入操作。GDN-2通过通道级门控控制擦除与写入，而KronLSTM通过标量残差修正减少内存干扰。GDN-2的向量残差修正方向依赖内存内容，导致长序列中干扰累积；KronLSTM的标量修正方向仅由输入决定，干扰由键值重叠乘积控制。这一差异在16k和32k上下文上体现为KronLSTM的显著优势，但GDN-2在S1任务上仍保持领先，表明标量修正对重复噪声句子的处理存在局限。

从问题动机看，KronLSTM与xLSTM家族共享矩阵内存结构，但xLSTM依赖归一化状态控制内存规模，而KronLSTM通过Kronecker Delta Rule的数学性质保证内存稳定性。xLSTM的归一化基于大数量比值，在大型网络中引发数值不稳定；KronLSTM的内存范数有界性由理论证明保证，无需额外归一化机制。这一差异使KronLSTM在训练稳定性上优于mLSTM，但xLSTM的指数门控机制在状态追踪任务上可能具有优势，论文未充分对比。

## 总结

本文针对线性注意力在长序列中的内存干扰与数值不稳定问题，提出Kronecker Delta Rule，通过标量残差修正沿单一方向更新内存，减少对其他存储值的干扰。该架构在1.5B参数模型上验证，32k上下文扩展后Avg-6达到60.19，LAMBADA困惑度降至7.66，在RULER NIAH任务上显著优于GDN-2。然而，纯线性模型在绝对检索精度上仍受限于架构本身，16k NIAH最高约17.6%，远低于混合/稀疏SOTA的64.43%。论文未探索混合架构中Full Attention层对检索精度的决定性作用，当支持集增大到更长上下文时，纯线性模型的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.26834)