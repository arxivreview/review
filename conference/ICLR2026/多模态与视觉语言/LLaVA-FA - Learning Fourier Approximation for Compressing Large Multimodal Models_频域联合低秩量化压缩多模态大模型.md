# ICLR2026最新论文 ｜LLaVA-FA: Learning Fourier Approximation for Compressing Large Multimodal Models ｜频域联合低秩量化压缩多模态大模型

研究机构：电子科技大学、哈尔滨工业大学

作者：Pengcheng Zheng、Chaoning Zhang、Jiarong Mo 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.00135)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.00135)

> 多模态大模型（LMMs）的权重矩阵存在显著冗余，但现有压缩方法将低秩分解与量化独立处理，导致误差累积。本文切入点在于利用傅里叶变换的解相关与共轭对称特性，在频域执行联合低秩加量化近似，以更低参数量实现更紧凑的权重表示。该方法通过极坐标量化与可选对角校准，在2B规模模型上实现了优于传统SFT/RLHF基线的幻觉抑制能力，但其对高分辨率图像细节保留的影响及频域SVD的计算开销尚未得到充分验证。

## 研究背景

多模态大模型（LMMs）的权重矩阵因训练过程中视觉与语言语义的强相关性而呈现低秩结构，这一特性为参数高效压缩提供了基础。低秩自适应（LoRA）通过引入低秩矩阵 $\mathbf{L}_1 \mathbf{L}_2$ 近似预训练权重 $\mathbf{W}$，已成为参数高效微调（PEFT）的主流范式。然而，当结合量化技术时，若低秩分解与量化步骤独立执行，秩选择阶段无法感知量化噪声，导致最终重建误差显著增加。

现有LMM压缩路线主要聚焦于视觉Token剪枝或通用权重剪枝。LLaVA-PruMerge通过注意力分数保留关键Token，将Token数量减少至原来的1/14；UPop则通过渐进幅度剪枝移除40%的权重，精度损失小于1%。这些方法要么改变输入序列长度，要么依赖空域权重分布假设，未能充分利用频域特性。本文的核心切入点是：频域中权重矩阵的奇异值分布比空域更紧凑，且傅里叶变换的共轭对称性允许存储一半的复数系数，从而在相同秩下实现更小的Frobenius误差和更少的可学习参数。

## 核心方法

### 频域联合低秩量化分解

本文方法参照系为Saha et al.提出的空域联合低秩量化框架，其核心差异在于将分解空间从实数空域迁移至复数频域。空域方法直接对 $\mathbf{W} \in \mathbb{R}^{d_1 \times d_2}$ 进行分解，而本文首先通过2D离散傅里叶变换（DFT）将其映射为 $\mathbf{W}^{\mathbb{C}} \in \mathbb{C}^{d_1 \times d_2/2}$，利用频域解相关特性最小化谱冗余。

$$
\mathbf{W}^{\mathbb{C}} \approx \mathbf{Q}^{\mathbb{C}} + \mathbf{L}_1^{\mathbb{C}} \mathbf{L}_2^{\mathbb{C}}
$$

该公式表示在频域中，原始权重矩阵被近似为量化残差矩阵 $\mathbf{Q}^{\mathbb{C}}$ 与低秩复数矩阵乘积之和。设计动机在于解决空域分解中奇异值分布松散导致的秩选择盲目性，频域能量集中特性使得相同秩下保留更多有效信息。

### PolarQuant极坐标量化与ODC校准

针对复数矩阵量化难题，本文设计PolarQuant编码器，将复数系数分离为幅度 $r$ 和相位 $\theta$ 进行独立离散化。共轭对称性允许仅存储 $d_2/2$ 个系数，相比空域节省近半参数。

$$
\mathbf{Q}^{\mathbb{C}} = \text{PolarQuant}(\mathbf{W}^{\mathbb{C}} - \mathbf{L}_1^{\mathbb{C}} \mathbf{L}_2^{\mathbb{C}}, b_r, b_\theta)
$$

该公式描述了PolarQuant对残差矩阵进行幅度-相位双路量化的过程，$b_r$ 和 $b_\theta$ 分别为幅度和相位比特宽度。设计动机在于传统实数量化无法保持复数结构，导致低比特重建不稳定；极坐标分离量化能更好地保留相位信息，提升低比特下的重建质量。

可选对角校准（ODC）方案用行/列均值近似完整Hessian矩阵，消除对大规模校准数据的依赖。ODC通过 $\mathbf{D}_{\text{row}}$ 和 $\mathbf{D}_{\text{col}}$ 对角矩阵加权SVD分解，实现无校准数据部署。

## 实验评估

实验在GQA、VisWiz、ScienceQA、TextVQA、MME、MMBench等基准上评估LLaVA-FA-2B（基于Qwen-2.5-7B压缩）和LLaVA-FA-1B（基于Qwen-2.5-3B压缩）。基线覆盖LLaVA-1.5、MiniCPM-V、Bunny-2B等SFT模型及RLHF-V等强化学习模型，但缺失MASQuant、SpikeMLLM等频域/脉冲对比方法。

| 模型 | LLM骨干 | 可训练参数 | GQA | VisWiz | MMBench | 幻觉率(Resp) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| LLaVA-FA-2B | Qwen-2.5-7B | 2.2B | 62.1 | 41.7 | 60.9 | 11.2 |
| MiniCPM-V-2 | MiniCPM-2.4B | 2.8B | 64.4 | 60.2 | 68.5 | 14.5 |
| RLHF-V | Vicuna-13B | 13B | - | - | - | 12.2 |

LLaVA-FA-2B在幻觉抑制上表现突出，Resp幻觉率11.2%优于MiniCPM-V-2的14.5%和RLHF-V的12.2%，但在综合理解能力上（MMBench 60.9）低于MiniCPM-V-2的68.5。

消融实验显示，秩从64增至256时，LLaVA-FA-2B平均准确率提升1.9%，LLaVA-FA-1B提升1.3%，表明大模型对秩更敏感。比特宽度从2增至4时，准确率提升4.6%，压缩比11.2x，幻觉率降至11.2%；超过4比特后收益平台化。

评估边界方面，论文未报告置信区间，且缺乏跨硬件（如NPU/边缘设备）的能效验证。代码未公开，训练使用8块NVIDIA RTX 4090 GPU，超参数细节有限。频域SVD的计算开销仅提及占TTFT的3.2%，但未提供详细分解。

## 关联研究分析

从问题动机看，LLaVA-FA与MASQuant均针对跨模态量化误差，但MASQuant通过模态感知平滑处理激活离群值，而LLaVA-FA依赖频域解相关特性，未显式建模视觉/语言模块的量化敏感性差异。这一差异源于LLaVA-FA假设频域特性对异构模块通用有效，而MASQuant承认模态间分布不一致需差异化处理。LLaVA-FA的统一频域压缩是否掩盖了模块级量化敏感性差异，论文未给出回答。

从方法设计看，LLaVA-FA与LLaVA-PruMerge分别聚焦权重压缩和Token剪枝，二者可组合使用但本文未验证组合效果。LLaVA-PruMerge通过注意力分数减少输入序列长度，LLaVA-FA通过频域分解减少权重参数，前者改变计算图结构，后者保持架构不变。LLaVA-FA的校准-free部署特性使其成为权重剪枝的即插即用替代方案，但在高分辨率图像场景下，频域压缩对细节保留的影响与Token剪枝的分辨率损失存在何种交互作用，缺乏实验证据。

## 总结

LLaVA-FA要解决的核心矛盾是LMM权重压缩中低秩分解与量化独立执行导致的误差累积。本文抓住频域解相关与共轭对称特性，通过PolarQuant极坐标量化和ODC对角校准，在频域实现联合低秩量化分解。实验证明LLaVA-FA-2B在幻觉抑制上优于SFT/RLHF基线（Resp幻觉率11.2% vs 14.5%），且仅需5M训练样本和2.2B可训练参数。本文边界在于缺乏跨硬件能效验证、未报告置信区间，且频域SVD计算开销仅部分量化。当支持高分辨率图像输入时，频域压缩对视觉细节保留的影响与Token剪枝的分辨率损失是否存在协同或冲突，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.00135)