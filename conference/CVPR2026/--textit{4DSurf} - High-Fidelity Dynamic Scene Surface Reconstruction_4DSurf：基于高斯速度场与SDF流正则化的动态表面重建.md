# CVPR2026最新论文 ｜\\textit{4DSurf}: High-Fidelity Dynamic Scene Surface Reconstruction ｜4DSurf：基于高斯速度场与SDF流正则化的动态表面重建

研究机构：澳大利亚国立大学、美国卡内基梅隆大学

作者：Renjie Wu、Hongdong Li、Jose M. Alvarez 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.28064)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.28064)

> 动态表面重建旨在从稀疏视角视频中恢复时间一致的三维几何，以支撑数字孪生与虚拟现实应用。现有基于高斯泼溅（Gaussian Splatting, GS）的方法在处理大变形场景时，常因单一变形场无法捕捉长时运动而陷入几何抖动与不一致。本文切入点在于将SDF流约束引入高斯运动建模，并通过分段增量训练解决大变形下的误差累积。具体做法是定义高斯速度场推导SDF流，并采用重叠分段策略与低秩适配进行存储优化。该方法在Hi4D数据集上将Chamfer Distance降低49%，证明了其在稀疏视角大变形场景下的几何优势，但其分段机制是否牺牲了全局运动连续性尚存疑。

## 研究背景

理解本文需厘清两个核心概念的因果关联：有符号距离函数（Signed Distance Function, SDF）与场景流。SDF通过零水平集定义表面，其时间导数即SDF流，表征了表面随时间的演化规律。在静态场景中，SDF流为零；而在动态场景中，SDF流与场景流在表面法向上的投影直接相关。然而，传统高斯泼溅方法仅关注像素级光度一致性，忽略了SDF流这一几何约束，导致高斯基元在时间维度上的运动缺乏物理一致性，进而引发重建表面的抖动。

动态表面重建的主流路线分为基于神经辐射场（NeRF）与基于高斯泼溅（GS）两类。NeRF方法如Neural SDF-Flow虽能学习隐式场，但训练缓慢且难以扩展至长序列；GS方法如Dynamic-2DGS与GauSTAR虽实现了实时渲染，但多依赖单一变形场或密集视角先验，在处理大变形时易出现几何漂移。本文针对这一瓶颈，提出一种无需外部先验（Prior-free）的通用框架，通过显式建模高斯运动与SDF流的匹配，解决大变形场景下的时间一致性问题。

## 核心方法

### 方法参照系

本文基于2DGS构建动态表面重建框架，其标准流程为：初始化高斯基元，通过变形场预测各时间步的高斯参数，最后通过可微光栅化渲染图像并优化。与标准流程的关键差异在于，本文不直接预测绝对变形，而是引入速度场描述运动，并增加SDF流正则化项约束几何演化。

### 高斯速度场与SDF流正则化

设计动机在于解决单一变形场在大变形下无法保持几何一致性的问题。通常做法是直接预测高斯中心、旋转与尺度的偏移量，本文改为预测速度参数。给定规范空间中的高斯中心 $\mathbf{\mu}_i$ 与时间步 $t$，高斯速度场 $F_\theta$ 预测线速度 $\mathbf{v}$、角速度 $\omega$ 与膨胀速度 $\mathbf{e}$：

$$ \mathbf{v}(\mathbf{\mu}_i, t), \omega(\mathbf{\mu}_i, t), \mathbf{e}(\mathbf{\mu}_i, t) = F_\theta(\gamma(\mathbf{\mu}_i), \gamma(t)) $$

该公式将运动参数化，使得高斯在任意时间步的位姿可由速度积分得到。基于此，推导出由高斯运动诱导的SDF流 $\mathbf{f}$，其等于场景流在表面法向 $\mathbf{n}$ 上的负投影：

$$ \mathbf{f} = -\mathbf{v} \cdot \mathbf{n} - (\omega \times \mathbf{x}) \cdot \mathbf{n} $$

同时，利用渲染深度图近似几何变化产生的SDF流 $\tilde{\mathbf{f}}$。通过最小化两者差异 $\mathcal{L}_{flow} = \sum_i |\mathbf{f}_i - \tilde{\mathbf{f}}_i|$，强制高斯运动与表面演化一致，从而抑制几何抖动。

### 重叠分段与增量运动调优

设计动机在于解决长序列大变形下的误差累积与存储爆炸问题。通常做法是对整个序列使用单一变形场，本文将其划分为 $N$ 个重叠分段，每段包含 $K+1$ 个时间步，相邻段共享一个虚拟时间步。对于第 $N$ 段（$N \ge 2$），其高斯速度场参数 $\theta_N$ 不再从头训练，而是基于前一段参数 $\theta_{N-1}$ 通过低秩适配（LoRA）微调：

$$ \theta_N = \theta_{N-1} + \Delta \theta_N, \quad \Delta \theta_N = \mathbf{A}_N \mathbf{B}_N $$

其中 $\mathbf{A}_N, \mathbf{B}_N$ 为低秩矩阵。该机制仅存储增量参数 $\Delta \theta_N$，在保持运动连续性的同时显著降低存储成本，使方法可扩展至长序列。

## 实验评估

实验在CMU Panoptic与Hi4D两个数据集上进行，前者包含4个场景，后者包含6个长序列多人体场景。基线覆盖GS-based（Dynamic-2DGS, GauSTAR）与NeRF-based（Neural SDF-Flow）方法，但缺失前馈式方法（如UniSplat）及物理驱动方法（如VeloGauss）的对比，这可能影响对方法泛化能力的全面评估。

| 方法 | CMU Panoptic Overall (mm) | Hi4D Overall (cm) |
| :--- | :--- | :--- |
| Dynamic-2DGS | 16.2 | 1.07 |
| GauSTAR | 14.7 | 2.09 |
| Neural SDF-Flow | 16.1 | - |
| Ours w/o IMT | 12.2 | 0.67 |
| Ours w IMT-64 | 12.1 | 0.70 |

在Hi4D数据集上，本文方法（Ours w/o IMT）的Overall指标为0.67 cm，较次优基线Dynamic-2DGS的1.07 cm降低约37%，较GauSTAR的2.09 cm降低约68%。在CMU Panoptic上，本文方法Overall为12.2 mm，较次优的Neural SDF-Flow（16.1 mm）降低约24%。

| 组件 | Acc (cm) | Comp (cm) | Overall (cm) |
| :--- | :--- | :--- | :--- |
| GVF only | 1.75 | 1.23 | 1.49 |
| + SF-Reg | 1.18 | 0.86 | 1.02 |
| + I-Segment | 1.06 | 0.47 | 0.77 |
| + O-Segment | 0.89 | 0.45 | 0.67 |
| + IMT-64 | 0.91 | 0.48 | 0.70 |

消融实验显示，SDF流正则化（SF-Reg）使Overall从1.49降至1.02，贡献最大；重叠分段（O-Segment）进一步降至0.67。值得注意的是，引入IMT-64后Overall微升至0.70，表明低秩适配在存储优化与精度保持间存在轻微权衡，但整体性能仍优于所有基线。

评估指标仅包含Chamfer Distance，缺乏对渲染质量（如PSNR）或物理一致性的量化评估。代码未公开，但论文提供了详细的超参数设置（如LoRA rank=64，训练30K迭代），在单张RTX 3090Ti上可复现。

## 关联研究分析

从问题动机看，本文与Neural SDF-Flow均关注SDF流约束，但后者基于NeRF隐式场，而本文基于GS显式表示。差异根源在于任务特性：NeRF方法训练缓慢，难以处理Hi4D等长序列场景，而GS方法虽快但几何精度不足。本文通过引入SDF流正则化弥补了GS的几何缺陷，但牺牲了NeRF在复杂光照下的渲染保真度，这在仅评估几何的任务设定下被忽略。

从方法设计看，本文与Dynamic-2DGS同属GS框架，但后者使用单一变形场，而本文采用分段增量训练。差异根源在于大变形场景下的误差累积：单一变形场在长序列中易过拟合局部运动，导致全局几何漂移。本文的分段策略通过局部优化与虚拟时间步传递几何信息，缓解了这一问题，但分段边界处的运动连续性依赖LoRA微调，其在全局运动剧烈变化时的鲁棒性未得到充分验证。

## 总结

本文核心矛盾在于GS方法在大变形动态场景下的几何不一致性。现有方法因单一变形场无法捕捉长时运动而失效，本文通过高斯速度场推导SDF流并引入正则化，结合分段增量训练解决了这一问题。实验证明，在Hi4D数据集上，本文方法将Chamfer Distance Overall降至0.67 cm，较次优基线降低37%。其边界在于分段机制可能引入局部优化偏差，且缺乏对渲染质量与物理一致性的评估。当分段数量增加至覆盖更极端的长序列时，LoRA微调能否维持全局运动连续性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.28064)