# ICLR2026最新论文 ｜DTP: DELTA-GUIDED TWO STAGE PRUNING FOR - MAMBA BASED MULTIMODAL LARGE LANGUAGE MODELS ｜Delta引导的两阶段剪枝

作者：Seong Yeol Park、Kwon Min Jung、XIANGHUA PIAO 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_97202001)

> 视觉Token冗余导致多模态大语言模型（MLLMs）在预填充阶段计算开销激增，而现有剪枝方法依赖Transformer的注意力分数，无法直接迁移至Mamba架构。本文切入点在于利用Mamba内部输入依赖参数 $\Delta_t$ 替代注意力信号，并基于该参数的统计分布确定剪枝层位置。具体做法是实施早期选择性保留与晚期完全移除的两阶段策略。该方案在Mamba骨干上实现了近50%的计算削减且性能损失极小，但其有效性是否依赖于特定模型深度与Token数量分布，尚需更多架构验证。

## 研究背景

多模态大语言模型通常由视觉编码器、投影层和语言模型组成。当输入高分辨率图像时，视觉Token数量远超文本Token，导致序列长度急剧增加。在Transformer架构中，自注意力机制的时间复杂度为 $O(n^2)$，使得预填充阶段成为推理瓶颈。Mamba架构基于状态空间模型（SSMs），通过递归更新隐藏状态实现线性时间复杂度，解决了解码阶段的效率问题，但预填充阶段仍需处理所有输入Token，视觉冗余依然是主要开销来源。

主流视觉Token剪枝方法如FastV和VisionZip均依赖注意力分数或显著性评分来评估Token重要性。这些方法在Transformer中有效，因为注意力权重直接反映了Token间的交互强度。然而，Mamba没有显式的注意力矩阵，其选择性机制由输入依赖参数 $\Delta_t$ 控制，导致基于注意力的剪枝策略在Mamba中失效。现有针对Mamba的Token缩减工作多局限于单模态视觉任务，未深入探索多模态场景下的剪枝策略。本文旨在解决这一架构依赖问题，提出一种无需重训练、基于Mamba内部参数的视觉Token剪枝框架。

## 核心方法

### 方法参照系

本文问题属于Training-free视觉Token剪枝范畴，但关键差异在于骨干架构从Transformer变为Mamba。通用流程通常包含信号提取、重要性排序和Top-K选择三个步骤。在Transformer中，信号提取依赖注意力分数；而在Mamba中，由于缺乏显式注意力，必须寻找替代信号源。本文的核心改动集中在信号提取与剪枝层定位两个环节。

### 基于 $\Delta_t$ 的Token重要性评估

在Mamba的选择性SSM（S6）中，输入依赖参数 $\Delta_t$ 控制状态转移矩阵的离散化，决定了每个Token对后续隐藏状态的贡献程度。$\Delta_t$ 值较大的Token引发更强的状态更新，而值较小的Token仅产生微弱变化。本文利用这一特性，将 $\Delta_t$ 作为Token重要性的直接度量。对于第 $j$ 个视觉Token，其重要性分数 $s_j$ 定义为：

$$ s_j = \frac{1}{D} \sum_{d=1}^{D} \Delta_{t,j,d} $$

其中 $D$ 为特征维度。该公式的物理含义是：通过平均各维度上的 $\Delta_t$ 值，量化该Token在时间步 $t$ 对系统状态的整体影响强度。这一设计解决了Transformer剪枝方法在Mamba中因缺乏注意力分数而无法评估Token重要性的问题，提供了架构无关且计算开销极低的替代信号。

### 基于统计分布的两阶段剪枝策略

确定重要性信号后，需选择剪枝发生的层位置。本文首先计算每层Token重要性分数的标准差 $\sigma_\ell$：

$$ \sigma_\ell = \sqrt{\frac{1}{N} \sum_{j=1}^{N} (s_{j,\ell} - \bar{s}_\ell)^2} $$

其中 $N$ 为Token数量，$\bar{s}_\ell$ 为层 $\ell$ 的均值。实验发现，在模型前25%的层中，$\sigma_\ell$ 存在一个局部峰值，该位置对应Token重要性区分度最高的区域。本文选择该层作为早期剪枝层 $k_{early}$，执行选择性剪枝，保留Top-K视觉Token。随后，在模型后部（如Cobra的第45层）执行完全剪枝，移除所有剩余视觉Token。这种两阶段策略解决了单层剪枝在早期层可能误删深层有用信息、在晚期层计算节省有限的问题，实现了效率与精度的平衡。

## 实验评估

实验在Cobra和RoboMamba两个Mamba-based MLLMs上进行，基准包括GQA、VQAv2、TextVQA、POPE、VSR、VizWiz和OKVQA。基线方法包括FastV、VTW和DART，均为Transformer剪枝方法的直接迁移或适配。缺失的强基线包括VisionZip和SparseVLM，但它们依赖注意力或文本引导，在Mamba中不可直接应用。

| 方法 | FLOPs Ratio | GQA | VQAv2 | TextVQA | POPE | Avg (Cobra) |
|---|---|---|---|---|---|---|
| Baseline | 100% | 62.3 | 77.8 | 58.2 | 88.4 | 65.8 |
| FastV (k=2, r=0.5) | 53% | 61.7 | 76.8 | 55.0 | 87.4 | 64.7 |
| VTW (k=32) | 52% | 47.1 | 54.1 | 42.6 | 74.1 | 54.0 |
| DART (r=0.44) | 48% | 61.2 | 76.1 | 55.1 | 86.3 | 64.3 |
| DTP (r=0.5) | 48% | 61.4 | 77.1 | 56.1 | 87.3 | 64.9 |

在Cobra模型上，DTP在48% FLOPs下平均准确率为64.9，仅比基线低0.9分，而FastV低1.1分，VTW低11.8分。VTW在深层剪枝时性能崩溃，表明其KL散度准则不适用于Mamba。

| 参数 | GQA (Cobra) | TextVQA (Cobra) | POPE (RoboMamba) | OKVQA (RoboMamba) |
|---|---|---|---|---|
| $y_t$ | 61.1 | 48.0 | 83.8 | 63.8 |
| $B_t$ | 60.2 | 47.4 | 82.9 | 62.6 |
| $C_t$ | 58.9 | 44.9 | 81.6 | 62.0 |
| $\Delta_t$ | 61.4 | 56.1 | 84.4 | 63.8 |

消融实验表明，$\Delta_t$ 在所有测试参数中表现最稳定，尤其在TextVQA和POPE上显著优于其他内部参数。随机剪枝和包含文本Token的Top-K策略导致性能大幅下降，验证了仅对视觉Token进行排序剪枝的必要性。

评估边界方面，实验仅在Cobra和RoboMamba两个模型上进行，未覆盖其他Mamba变体。代码未公开，超参数如剪枝层位置需针对每个模型单独分析。GPU内存使用从8.8 GB降至8.3 GB，预填充延迟降低37%，但解码延迟变化不大，表明剪枝主要优化预填充阶段。

## 关联研究分析

从信号来源看，本文与ZOO-Prune同属非注意力信号路线，但ZOO-Prune基于零阶梯度估计Token敏感性，计算开销较大；本文基于 $\Delta_t$，计算开销极低且无需额外前向传播。这一差异源于Mamba架构特性：$\Delta_t$ 是Mamba选择性机制的核心参数，天然反映Token对状态更新的影响，而梯度估计在SSM中可能因隐式状态而变得不稳定。

从剪枝策略看，本文与FastV同属Intra-LLM剪枝，但FastV依赖浅层注意力分数，本文利用 $\Delta_t$ 标准差分布确定剪枝层。FastV在Mamba中失效是因为其假设注意力分数与重要性正相关，而Mamba中 $\Delta_t$ 的分布特性与注意力不同。本文的两阶段策略中，晚期完全剪枝是否依赖早期已充分提取语义，论文未给出明确回答，但实验表明在Cobra的第45层完全剪枝后性能损失极小，暗示Mamba深层对视觉Token的依赖度较低。

## 总结

本文要解决的核心矛盾是Mamba架构中缺乏注意力分数导致现有剪枝方法失效。本文抓住的切入点是Mamba内部参数 $\Delta_t$ 天然反映Token重要性，且其统计分布可指导剪枝层选择。本文提出了基于 $\Delta_t$ 的两阶段剪枝策略，证明了在Cobra和RoboMamba上，DTP在50% FLOPs下仅损失0.9分和1.1分平均准确率，显著优于直接迁移的Transformer剪枝方法。本文的边界在于仅在两个特定Mamba模型上验证，且剪枝层位置需针对每个模型单独分析。当模型深度或Token数量分布发生变化时，基于 $\Delta_t$ 标准差的局部峰值是否仍能准确定位最优剪枝层，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_97202001)