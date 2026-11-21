# ICLR2026最新论文 ｜SeeDNorm: Self-Rescaled Dynamic Normalization ｜自缩放动态归一化

研究机构：北京航空航天大学

作者：Wenrui Cai、Defa Zhu、Qingjie Liu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.22777)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.22777)

> 归一化层在稳定训练的同时丢弃了输入范数信息，限制了模型在分布偏移下的表达力。现有静态归一化无法适应数据变化，而饱和激活函数虽保留范数却导致梯度消失。SeeDNorm 通过引入输入依赖的动态缩放系数，在保留 RMSNorm 梯度自适应优势的同时恢复范数信息。该方法在大规模语言模型预训练中实现了收敛加速与性能提升，但其收益幅度及长期稳定性仍存疑。

## 研究背景

深层 Transformer 训练面临数值稳定性与表示能力的双重约束。Batch Normalization (BN) 依赖批次统计量，在序列建模中失效；Layer Normalization (LN) 虽消除批次依赖，但其均值中心化步骤增加了计算开销。Root Mean Square Normalization (RMSNorm) 通过移除均值中心化，仅保留基于均方根（RMS）的缩放，成为大语言模型的标准配置。然而，RMSNorm 将向量约束在单位超球面上，随后通过静态可学习参数 $\gamma$ 进行缩放。这种静态机制丢弃了输入向量的原始范数信息，导致模型在处理零样本泛化或分布偏移场景时，无法根据输入尺度动态调整表示，从而限制了网络的有效容量。

归一化层的研究重心已从单纯的优化稳定性转向几何本质对模型容量的影响。主流 Pre-Norm 架构虽解决了梯度消失，但深层表示退化的“深度诅咒”依然存在。饱和激活函数如 Dynamic Tanh (DyT) 试图通过约束输出范围来保留范数，但其导数在极端值处趋近于零，导致反向传播中梯度消失，优化效率低下。SeeDNorm 的切入点在于解决这一两难困境：既需要 RMSNorm 的梯度自适应能力以维持训练稳定，又需要保留输入范数信息以增强表达力。

## 核心方法

### 方法参照系

SeeDNorm 基于 RMSNorm 架构，其标准形式为 $y = \frac{x}{\text{RMS}(x)} \odot \gamma$。该流程的关键差异在于，SeeDNorm 将静态缩放因子 $\gamma$ 替换为输入依赖的动态矩阵，从而在归一化过程中保留范数信息。

### 动态缩放机制

传统 RMSNorm 的 $\gamma$ 是静态且输入无关的，无法适应数据分布变化。SeeDNorm 引入自缩放参数 $\beta$ 和调节参数 $\alpha$，构建动态缩放矩阵。其前向传播公式为：

$$ y = \frac{x}{\text{RMS}(x)} \odot [\sigma(x \cdot \beta^T) \cdot \alpha + \gamma] $$

其中 $\sigma(\cdot)$ 为 tanh 激活函数。该设计动机在于解决静态 $\gamma$ 在分布偏移下的表达力瓶颈。通过 $x \cdot \beta^T$ 计算输入与参数的点积，并经 tanh 约束在 $[-1, 1]$ 区间，SeeDNorm 实现了输入范数的保留。当输入 $x$ 尺度变化时，动态项 $\sigma(x \cdot \beta^T) \cdot \alpha$ 随之调整，使得输出不仅包含方向信息，还隐含了原始输入的尺度特征。

### 多头方差抑制

在高维空间中，点积 $x \cdot \beta^T$ 的方差随维度 $D$ 线性增长，可能导致训练不稳定。SeeDNorm 采用多头机制，将 $x$ 和 $\beta$ 拆分为多个子向量，分别计算点积后拼接。这一设计动机在于降低非极端条件下的梯度方差。通过减小每个点积的维度，SeeDNorm 抑制了 $\sigma(x \cdot \beta^T)$ 项的波动，从而在保持动态调整能力的同时，增强了反向传播中梯度的稳定性。

## 实验评估

| 模型 | 训练 Tokens (B) | c4_en PPL ↓ | ARC-C ↑ | HellaSwag ↑ | MMLU-Var ↑ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| OLMoE-1.3B | 500 | 18.63 | 32.3 | 55.2 | 32.4 |
| OLMoE-1.3B-DyT | 500 | 19.45 | 30.4 | 53.2 | 30.5 |
| OLMoE-1.3B-SeeDNorm | 500 | 18.12 | 34.5 | 56.8 | 33.2 |
| OLMoE-7B | 1000 | 14.07 | 40.8 | 71.2 | 38.8 |
| OLMoE-7B-SeeDNorm | 1000 | 13.88 | 44.5 | 71.8 | 40.2 |

实验在 OLMoE 和 OLMo2 架构上进行，基线包括 RMSNorm 和 DyT。SeeDNorm 在 OLMoE-1.3B 上将 PPL 从 18.63 降至 18.12，显著优于 DyT 的 19.45。在 7B 模型中，SeeDNorm 同样实现了 PPL 从 14.07 到 13.88 的降低，并在下游任务如 ARC-C 上取得 44.5% 的准确率，高于基线的 40.8%。

| 消融变体 | c4_en PPL ↓ | ARC-C ↑ | HellaSwag ↑ |
| :--- | :--- | :--- | :--- |
| SeeDNorm ($\alpha \leftarrow 1$) | 18.12 | 34.5 | 56.8 |
| SeeDNorm ($\alpha \leftarrow 0.1$) | 18.39 | 31.2 | 55.6 |
| SeeDNorm (scalar $\alpha$) | 23.42 | 27.8 | 43.0 |
| SeeDNorm (w/o $\beta$) | 18.33 | 32.1 | 56.5 |

消融实验显示，$\alpha$ 的初始化对性能影响显著，$\alpha=1$ 优于 $\alpha=0.1$。将 $\alpha$ 设为标量导致 PPL 飙升至 23.42，表明逐元素动态调整至关重要。移除 $\beta$ 后性能略有下降，验证了自缩放机制的有效性。

评估协议主要关注预训练损失和零样本下游任务，未报告计算开销或推理延迟。代码未公开，超参数如 $\alpha$ 的初始化值（1）和 $\beta$ 的零初始化策略是复现的关键。缺乏置信区间报告，PPL 的微小提升（如 0.51）是否统计显著存疑。

## 关联研究分析

从问题动机看，SeeDNorm 与 TaperNorm 均旨在解决归一化层在推理阶段的效率或表达力问题，但路线截然不同。TaperNorm 通过门控机制在推理时将归一化折叠为线性映射，侧重计算效率；SeeDNorm 则通过动态缩放保留范数信息，侧重表示能力。SeeDNorm 未探索推理加速，其动态计算可能增加推理成本，这是其与 TaperNorm 的核心差异。

从方法设计看，SeeDNorm 与 DyT 同属“去归一化”或“激活替代”路线，但 SeeDNorm 保留了 RMSNorm 的归一化结构，仅修改缩放因子。DyT 完全替换归一化层，导致梯度消失；SeeDNorm 通过 $\sigma(x \cdot \beta^T)$ 项引入非线性，同时保留 $\text{RMS}(x)$ 的梯度自适应特性。这种混合设计使得 SeeDNorm 在稳定性上优于 DyT，但在参数复杂度上高于标准 RMSNorm。

## 总结

SeeDNorm 旨在解决归一化层丢弃输入范数信息导致的表达力限制。通过引入输入依赖的动态缩放矩阵，它在保留 RMSNorm 梯度自适应优势的同时，恢复了范数信息。实验表明，在 OLMoE-1.3B 上，SeeDNorm 将 PPL 从 18.63 降至 18.12，显著优于 DyT 基线。然而，其收益幅度较小，且多头机制的计算开销未量化。当训练数据量从 500B 增加至 1T 时，SeeDNorm 的相对优势是否持续扩大，论文未给出明确回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.22777)