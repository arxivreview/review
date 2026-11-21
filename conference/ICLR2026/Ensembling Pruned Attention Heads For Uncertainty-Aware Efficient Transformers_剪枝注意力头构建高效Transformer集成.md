# ICLR2026最新论文 ｜Ensembling Pruned Attention Heads For Uncertainty-Aware Efficient Transformers ｜剪枝注意力头构建高效Transformer集成

作者：Firas Gabetni、Giuseppe Curci、Andrea Pilzer 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.18358)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.18358)

> 在安全关键场景中，深度神经网络常对错误预测表现出过度自信，不确定性量化（UQ）旨在通过估计认知不确定性来缓解此风险。深度集成（Deep Ensembles）虽为UQ金标准，但其线性增长的计算与内存成本使其难以部署于大规模基础模型。本文切入点在于揭示朴素剪枝虽能保持精度却会损害校准，进而提出通过结构化剪枝注意力头生成多样子网络并融合为单一模型的方法。该框架在无需从头训练的情况下实现了接近单模型的推理成本，但在极端分布偏移下的多样性保持能力仍存疑。

## 研究背景

当模型面对训练数据未覆盖的输入时，其预测分布的方差反映了参数知识不足的程度，即认知不确定性（Epistemic Uncertainty）。准确量化这一不确定性是区分模型“不知道”与“数据本身模糊”的关键，直接决定了下游任务中是否应拒绝预测或请求人工干预。然而，现有高效集成方法如BatchEnsemble通过共享骨干网络降低计算成本，却因成员独立性受限导致在分布偏移场景下校准性能显著下降，暴露了“以独立性换效率”策略的局限。

该领域的核心矛盾在于如何在保持集成成员间足够多样性的前提下，将推理成本从线性多模型前向传播压缩至单次前向传播。主流路线包括基于低秩扰动的BatchEnsemble和基于独立训练但减少表示容量的Packed-Ensembles，前者牺牲了成员独立性，后者则限制了单个成员的表达能力。针对Transformer架构，现有方法多依赖全量预训练或复杂的低秩适配，难以直接利用预训练模型的既有知识。本文抓住的切入点在于，传统剪枝方法虽能保留精度，但忽略了其对不确定性估计（特别是校准）的负面影响，且未利用Transformer注意力头的模块化特性来高效生成多样性。

## 核心方法

### 方法参照系

本文问题属于高效集成架构类别，其标准流程是通过共享参数或低秩扰动生成多个模型变体并聚合预测。与BatchEnsemble等通用方法的关键差异在于，本文不修改主干网络权重，而是通过结构化剪枝注意力头生成子网络，并利用分组全连接层（GFC）将多个子网络融合为单一Transformer，从而在单次前向传播中完成集成推理。

### 剪枝对校准的理论约束

朴素剪枝在干净数据上有效，但在含噪数据上会加剧性能退化，导致不确定性估计失效。设计动机在于揭示为何直接剪枝预训练模型不能直接用于UQ，从而为后续方法提供理论依据。设 $D_t$ 为干净测试集，$D_n$ 为含噪测试集，损失差为 $\Delta L = L_{D_n} - L_{D_t}$。若剪枝扰动 $\delta\theta$ 与含噪损失梯度非负相关，且含噪Hessian矩阵 $\mathbf{H}_n$ 与干净Hessian矩阵 $\mathbf{H}_t$ 满足 $\mathbf{H}_n - \mathbf{H}_t \succ 0$，则剪枝后的损失差满足：

$$ \Delta L(\theta) \leq \Delta L(\theta + \delta\theta) $$

该公式表明，在含噪条件下，剪枝操作会放大模型对噪声的敏感性，导致校准误差增加，因此必须采用保留功能电路的剪枝策略而非盲目移除权重。

### 注意力头剪枝与融合机制

针对剪枝损害校准的问题，本文提出基于电路提取的注意力头剪枝策略，并通过GFC层融合多个剪枝子网络。设计动机在于利用注意力头的模块化特性，使剪枝后的子网络保留关键功能电路，同时通过融合机制恢复单模型的推理效率。设 $M$ 个剪枝模型 $\{f_{\tilde{\theta}^{(m)}}\}_{m=1}^M$，每个模型在层 $\ell$ 保留 $H_\ell$ 个注意力头。融合后的MHA层通过GFC层联合计算查询、键和值：

$$ Q_\ell = \text{GFC}(W_\ell^Q, X_{i,\ell}, b_\ell^Q), \quad K_\ell = \text{GFC}(W_\ell^K, X_{i,\ell}, b_\ell^K), \quad V_\ell = \text{GFC}(W_\ell^V, X_{i,\ell}, b_\ell^V) $$

其中 $W_\ell^Q, W_\ell^K, W_\ell^V$ 为各模型对应的投影矩阵。MLP层则通过平均各模型权重实现合并：

$$ W_{\text{merge}}^{(j)} = \frac{1}{M} \sum_{m=1}^M W_{\tilde{\theta}^{(m)}}^{(j)} $$

该设计使得融合后的Transformer在处理相同数量token的同时，保留了各子网络的多样性，且无需微调即可直接用于零样本任务，显著降低了训练与推理成本。

## 实验评估

实验在ImageNet-1K、CIFAR-100、文本分类及零样本分类任务上进行，基线覆盖Deep Ensembles、BatchEnsemble、MIMO、LoRA Ensembles及MC Dropout，但缺失SVE等最新隐式集成方法。在ImageNet-1K上，Hydra Ensembles (Circuit) 的OOD检测AUROC为86.29%，FPR95为47.62%，AUPR为63.15%，优于Deep Ensembles的85.48%、50.25%、60.91%。在零样本ImageNet-1K OOD基准上，Hydra Ensembles (Circuit) 的AUROC为76.82%，FPR95为68.05%，AUPR为47.85%，超越需训练的ViLU方法（AUROC 75.38%，FPR95 71.59%，AUPR 43.81%）。

| 方法 | ImageNet-1K OOD AUROC | ImageNet-1K OOD FPR95 | ImageNet-1K OOD AUPR | Zero-Shot OOD AUROC | Zero-Shot OOD FPR95 |
|---|---|---|---|---|---|
| Deep Ensembles | 85.48 | 50.25 | 60.91 | - | - |
| Hydra Ensembles (Circuit) | 86.29 | 47.62 | 63.15 | 76.82 | 68.05 |
| ViLU | - | - | - | 75.38 | 71.59 |

消融实验显示，使用Circuit策略比Taylor策略在CIFAR-100上提升AUROC 0.54（95.46 vs 94.92），表明电路提取对保留UQ关键功能至关重要。在文本分类任务中，Hydra Ensembles (Circuit) 的NLL为0.24，优于Deep Ensembles的0.24（持平）和Taylor剪枝的0.33，验证了剪枝策略对校准的显著影响。

评估边界方面，论文未报告置信区间，且未对比SVE等基于奇异值分解的隐式集成方法。代码未公开，超参数如剪枝比例（ImageNet-1K保留89.1%参数）未提供完整列表，可复现性受限。

## 关联研究分析

从问题动机看，Hydra Ensembles与BatchEnsemble均旨在降低集成推理成本，但BatchEnsemble通过低秩扰动共享骨干，而本文通过结构化剪枝生成子网络。BatchEnsemble的成员独立性受限导致在分布偏移下校准下降，而本文通过保留注意力头电路，在零样本场景下实现了优于Deep Ensembles的OOD检测性能。这一差异源于Transformer架构的模块化特性，使得头级剪枝比权重级扰动更能保留功能多样性。

从方法设计看，Hydra Ensembles与Packed-Ensembles均使用GFC层实现融合，但Packed-Ensembles通过独立训练减少表示容量，而本文通过剪枝预训练模型生成多样性。Packed-Ensembles需全量预训练，而本文支持零样本使用，避免了昂贵的训练过程。这一设计选择使得Hydra Ensembles在大规模基础模型上更具部署可行性，但其多样性来源依赖于预训练模型中注意力头的功能分离程度，若基础模型知识分布不均，可能影响UQ性能。

## 总结

本文解决的核心矛盾是高效集成中成员多样性与推理成本的权衡，切入点在于揭示朴素剪枝损害校准的理论机制，并利用Transformer注意力头的模块化特性生成多样子网络。通过结构化剪枝与GFC融合，Hydra Ensembles在零样本ImageNet-1K OOD检测中取得76.82% AUROC，超越需训练的ViLU方法。其边界在于实验未覆盖极端分布偏移场景，且未对比SVE等最新隐式集成方法。当预训练模型中注意力头的功能分离程度较低时，剪枝生成的多样性是否足以维持有效的UQ性能，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.18358)