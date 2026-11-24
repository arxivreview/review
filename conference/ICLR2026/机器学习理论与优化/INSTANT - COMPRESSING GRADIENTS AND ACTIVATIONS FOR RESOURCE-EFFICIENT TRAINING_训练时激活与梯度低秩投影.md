# ICLR2026最新论文 ｜INSTANT: COMPRESSING GRADIENTS AND ACTIVATIONS FOR RESOURCE-EFFICIENT TRAINING ｜训练时激活与梯度低秩投影

作者：Tuan-Kiet Doan、Trung-Hieu Tran、Enzo Tartaglione 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_74522863)

> 深度学习训练受限于反向传播的高内存占用与计算开销，现有激活压缩方法因SVD计算成本或固定子空间误差累积而难以兼顾效率与精度。INSTANT通过周期性校准构建自适应正交基，将激活与输出梯度同时投影至低秩子空间，在反向传播中执行低秩矩阵乘法。该方法在保持精度损失低于1%的前提下，实现了15倍计算量与32倍内存的压缩，但其校准机制在超大规模模型中的可扩展性尚未得到验证。

## 研究背景

Transformer模型训练时，反向传播需存储全秩激活张量以计算权重梯度，导致内存消耗与序列长度、通道维度呈线性增长。为降低开销，研究界转向张量分解技术，利用激活与梯度的内在低秩特性，将其投影至低维子空间。然而，直接对每个训练步执行奇异值分解（SVD）的 $O(n^3)$ 计算复杂度使得训练时间不降反升，而基于固定子空间的方法（如ESPACE）则因无法适应训练中激活分布的漂移而产生误差累积。

现有方案在“计算效率”与“近似精度”之间存在根本矛盾：高频SVD保证精度但拖慢训练，低频固定投影加速训练但牺牲精度。LBP-WHT（Yang et al., 2023b）依赖图像低频特性，在NLP任务上失效；GaLore（Zhao et al., 2024）仅压缩优化器状态，未触及反向传播的核心计算瓶颈。INSTANT的切入点在于解耦投影基的构建与使用：通过低成本校准获取自适应正交基，并在训练过程中周期性更新，从而在避免高频SVD开销的同时，动态捕捉激活与梯度的低秩结构变化。

## 核心方法

### 低秩反向传播参照系

传统反向传播中，权重梯度 $\mathbf{g}_w = \mathbf{g}_y \mathbf{x}^\top$ 与输入梯度 $\mathbf{g}_x = \mathbf{g}_y \mathbf{w}$ 均涉及全秩矩阵乘法，FLOPs为 $4 \cdot L \cdot C_x \cdot C_y$。本文参照系为“激活感知低秩近似”，但关键差异在于：不压缩权重矩阵 $W$，而是压缩训练过程中的中间变量（激活 $\mathbf{x}$ 与梯度 $\mathbf{g}_y$），且投影基随训练动态更新。

### 自适应校准与能量截断

设计动机：固定子空间无法适应训练中激活分布的漂移，导致误差累积。INSTANT在每 $N_t$ 步执行一次校准，计算激活自相关矩阵 $\mathbf{C}_X = \mathbb{E}[\mathbf{x} \mathbf{x}^\top]$ 的SVD，获取左奇异向量 $\mathbf{U}$。为平衡精度与维度，引入能量阈值 $\epsilon$ 与过采样参数 $p$：

$$
\sum_{i=1}^{k} \sigma_i^2 \ge \epsilon \cdot \|\mathbf{C}_G\|_F^2, \quad R_y = k + p
$$

其中 $k$ 为满足能量保留的最小秩，$p$ 为过采样向量数。该公式表明，投影基 $\mathbf{Q}$ 的维度由能量保留率与冗余缓冲共同决定，过采样机制补偿了训练过程中核心基向量变化带来的信息损失。

### 低秩反向传播计算

设计动机：全秩乘法是计算瓶颈，需在低维空间完成梯度计算。利用投影性质 $\mathbf{x} \approx \mathbf{P}^\top \mathbf{P} \mathbf{x}$，权重梯度近似为：

$$
\tilde{\mathbf{g}}_w = \hat{\mathbf{g}}_{y1} \cdot \hat{\mathbf{x}}, \quad \hat{\mathbf{g}}_{y1} = \mathbf{P} \mathbf{g}_y, \quad \hat{\mathbf{x}} = \mathbf{P} \mathbf{x}
$$

输入梯度则通过三步低秩乘法计算：$\hat{\mathbf{g}}_{y2} = \mathbf{Q} \mathbf{g}_y$，$\hat{\mathbf{g}}_x = \hat{\mathbf{g}}_{y2} \mathbf{w}$，$\tilde{\mathbf{g}}_x = \mathbf{Q}^\top \hat{\mathbf{g}}_x$。此过程将FLOPs从 $4 L C_x C_y$ 降至 $2(R_x + R_y)(C_x C_y + L C_x + L C_y)$，当 $R_x, R_y \ll \min(L, C_x, C_y)$ 时，计算量呈数量级下降。

## 实验评估

实验在ImageNet预训练的EfficientFormer、SwinV2及BERT/DistilBERT上进行，基线包括Vanilla、LBP-WHT、Gradient Filter及GaLore。缺失Prehab、SLORR等训练时正则化方法对比，因任务目标不同（训练效率 vs 压缩精度），直接比较缺乏公平性。

| 模型 | 方法 | MFLOPs↓ | Mem (MB)↓ | mAcc↑ |
|---|---|---|---|---|
| EfficientFormer-L1 | Vanilla | 1484 | 1.95 | 79.28 |
| EfficientFormer-L1 | INSTANT-5 | 475 | 0.38 | 78.65 |
| EfficientFormer-L1 | INSTANT-7 | 544 | 0.45 | 79.01 |
| BERT | Vanilla | 14495 | 13.50 | 83.92 |
| BERT | INSTANT-15 | 1018 | 0.42 | 73.06 |

INSTANT-5在EfficientFormer-L1上实现3.1倍FLOPs与5.1倍内存压缩，精度仅降0.63%；BERT全微调中，INSTANT-15实现17.2倍FLOPs与32.1倍内存压缩，精度降1.17%。

| 方法 | p | MFLOPs↓ | Mem (MB)↓ | mAcc↑ |
|---|---|---|---|---|
| INSTANT (compress gy) | 5 | 1069 | 1.95 | 79.00 |
| INSTANT (compress x) | 5 | 885 | 0.33 | 78.99 |
| INSTANT (both) | 5 | 475 | 0.38 | 78.65 |

消融显示，仅压缩梯度（gy）虽降低计算量，但内存未减（需存储全秩激活）；仅压缩激活（x）虽大幅减内存，但计算量降幅有限（反向传播仍含全秩乘法）。联合压缩在计算与内存上均获最优，但精度略低于单侧压缩，表明低秩投影误差在双向传播中累积。

评估边界：未报告置信区间，0.63%的精度下降统计显著性未知；校准开销（每200/50步）在千亿参数模型中是否成为瓶颈未验证；代码已开源，但超参数 $\epsilon=0.95$ 固定，未探索自适应调整。

## 关联研究分析

从问题动机看，INSTANT与ESPACE（Sakr & Khailany, 2024）均针对训练内存瓶颈，但ESPACE仅压缩激活且使用固定子空间，导致误差累积；INSTANT扩展至梯度压缩并引入自适应校准，根源在于梯度分布比激活分布更动态，固定投影无法捕捉其低秩结构变化。从方法设计看，INSTANT与GaLore（Zhao et al., 2024）同属低秩训练范式，但GaLore压缩优化器状态以节省内存，INSTANT压缩激活与梯度以节省计算与内存，二者正交可组合；差异在于GaLore依赖权重梯度的低秩性，而INSTANT依赖激活与输出梯度的低秩性，后者在NLP任务上更稳健，因LBP-WHT的低频假设在语言数据上失效。

## 总结

INSTANT解决的核心矛盾是训练时反向传播的计算与内存开销，其切入点在于解耦投影基构建与使用，通过周期性校准自适应捕捉激活与梯度的低秩结构。方法通过能量截断与过采样机制，在低秩子空间完成反向传播，证明了15倍计算与32倍内存压缩下精度损失低于1%。边界在于校准机制依赖固定能量阈值，未探索超大规模模型中校准开销的可扩展性，且过采样参数 $p$ 的选取依赖数据分布，能否实现自适应调整，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_74522863)