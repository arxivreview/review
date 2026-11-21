# CVPR2026最新论文 ｜Decompose, Mix, Adapt: A Unified Framework for Parameter-Efficient Neural Network Recombination and Compression ｜统一参数重组框架：压缩与微调的协同优化

研究机构：美国波士顿大学

作者：Nazia Tasnim、Shrimai Prabhumoye、Bryan A. Plummer

论文原文见 [arXiv](https://arxiv.org/abs/2603.27383)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.27383)

> 参数重组（Parameter Recombination, PR）旨在通过重构权重结构以适配下游任务或缩减模型体积，但现有方法将参数高效微调（PEFT）与模型压缩（MC）视为孤立系统，导致组合部署时出现兼容性断裂与参数冗余。CRISP 提出了一种基于共享基矩阵与门控混合矩阵的统一重参数化方案，将压缩与适配映射至同一分解结构。该框架在保持极低可训练参数量的同时，实现了压缩率与任务性能的双重提升，但其动态权重生成机制在极端资源受限场景下的推理开销仍需审慎评估。

## 研究背景

当边缘设备部署大模型时，存储容量与任务适配需求构成一对矛盾：模型压缩（MC）通过剪枝或量化减少参数量，而参数高效微调（PEFT）通过注入少量可训练参数适应新任务。然而，PEFT 方法如 LoRA 通常增加总参数量，若先压缩再微调，适配器参数可能抵消压缩收益，甚至破坏压缩后的权重结构。这种“先压缩后适配”的串行流程缺乏统一的参数预算控制，导致在资源受限场景下无法同时满足存储限制与性能要求。

PR 方法的核心在于定义一个变换函数 $T$，将少量可训练参数 $\theta$ 映射为完整权重矩阵 $W$。主流路线如 LoRA 采用低秩分解 $W = W_0 + AB$，冻结主干 $W_0$ 仅训练 $A, B$；而 Basis Sharing 等方法则通过共享基矩阵实现压缩。然而，现有方法往往针对单一目标优化：PEFT 方法忽略存储约束，MC 方法忽略适配灵活性。CRISP 的切入点在于识别出压缩与适配在参数重组层面的同构性——两者均可通过控制基矩阵尺寸与混合矩阵复杂度来实现，从而在单一框架内统一处理这两个看似对立的目标。

## 核心方法

### 方法参照系

PR 方法通常将预训练权重 $W_p$ 与可训练参数 $\theta$ 结合生成目标权重 $W$。LoRA 的变换为 $W = W_p + A_r B_r$，其中 $A_r, B_r$ 为低秩矩阵；Basis Sharing 则通过 $W = B_r A_r$ 实现压缩，其中 $B_r$ 为共享基矩阵。CRISP 的关键差异在于引入非线性门控机制，并解耦基矩阵的共享策略与混合矩阵的层特异性，使得同一结构既能通过缩减 $B$ 实现压缩，又能通过微调 $A$ 实现适配。

### 基矩阵共享与压缩机制

CRISP 将预训练权重分解为共享基矩阵 $B'_{i,r} \in \mathbb{R}^{u \times r}$ 与层特异性混合矩阵 $A'_{i,r,s} \in \mathbb{R}^{r \times s}$，其中 $u = d_{in} \times s \times d_{out}$。压缩通过减少基矩阵维度 $r$ 或增加共享层数实现，而适配通过冻结 $B$ 并微调 $A$ 完成。这一设计解决了 Basis Sharing 中混合矩阵 $A$ 过大导致压缩率受限的问题，同时避免了 LoRA 中适配器参数独立于主干导致的存储冗余。

$$
W_i = \text{reshape}\left( \sigma(A'_{i,r,s} \odot B'_{i,r}) , d_{out}, d_{in} \right)
$$

该公式表明，权重生成过程包含对混合矩阵 $A$ 的 SiLU 门控（$\sigma$ 为 sigmoid，$\odot$ 为逐元素乘法），随后与基矩阵 $B$ 相乘并重塑为目标维度。SiLU 门控作为内置正则化，抑制了混合矩阵的过拟合倾向，无需额外超参数。

### 门控混合矩阵与适配机制

CRISP 的核心创新在于将混合矩阵从 RECAST 的向量形式扩展为矩阵形式，并引入 SiLU 门控。RECAST 限制 $a_r$ 为向量，导致其仅在极小参数预算（<200）下有效；CRISP 通过 $A'_{i,r,s}$ 的矩阵结构，在更广泛的参数预算范围内保持性能优势。SiLU 门控 $\sigma(A) \odot A$ 提供了平滑的非线性约束，相比 ReLU 避免了权重稀疏化导致的性能崩溃，相比 L2 正则化无需调整超参数。

$$
\mathcal{L}_{\text{retrofit}} = \sum_{i=1}^{N} \ell_{\text{smooth-L1}}(W_i, W_{p,i}) + \lambda \cdot \mathcal{L}_{\text{distill}}(M_{\text{teacher}}, M_{\text{student}})
$$

该损失函数用于 Retrofitting 阶段，第一项通过 Smooth-L1 损失重构预训练权重，第二项通过蒸馏损失引导压缩模型学习教师模型的特征表示。这一两阶段策略解决了直接压缩导致的初始化困难，确保基矩阵与混合矩阵在压缩后仍能保持有效的表达能力。

## 实验评估

CRISP 在 VTAB-1K、CIFAR-100 等视觉基准及 LLaMA3.2-1B 的常识推理任务上进行了评估，基线覆盖 LoRA、DoRA、RECAST、SVD 等主流 PEFT 与 MC 方法，但缺失 QLoRA 等量化感知基线。在 VTAB-1K 上，CRISP 以 59.2% 的整体准确率超越 SOTA 1.5%，且可训练参数仅占基础模型的 0.5%（5×10⁻³ %），低于 LoRA 的 0.7%（7×10⁻³ %）。在 ViT-B/16 的 50% 压缩率下，CRISP 平均准确率为 83.3%，比 DGMR 高 1.4 个点，且仅使用 2% 的 ImageNet 数据进行蒸馏，显著优于使用全量数据的基线。

| 方法 | VTAB-1K Overall (%) | ViT-B/16 50% 压缩 Avg (%) | LLaMA3.2-1B 30% 压缩 Avg (%) |
|---|---|---|---|
| LoRA | 55.8 | 87.1 | - |
| DoRA | 52.8 | - | - |
| RECAST | 55.3 | 83.7 | - |
| DGMR | - | 81.9 | - |
| CRISP | 59.2 | 83.3 | 38.0 |

消融实验显示，SiLU 门控在 CUB-Birds、CIFAR100 和 FGVC-Aircraft 上的平均准确率为 82.2%，高于无正则化的 81.8% 和 L2 正则化的 82.0%，而 ReLU 导致性能崩溃至 61.5%。混合矩阵维度 $s$ 对性能的影响显著大于 $r$：固定 $r=16$ 时，$s$ 从 8 增至 32 使参数从 6.1M 增至 22.1M，准确率同步提升；而固定 $s=16$ 时，$r$ 从 8 增至 64 导致准确率崩溃，表明基矩阵容量是性能的主要驱动因素。

CRISP 在 NVIDIA L40S 上的推理吞吐量为 657 samples/s，延迟 1.52 ms，优于 LoRA（575 samples/s, 1.74 ms）但低于 DoRA（726 samples/s, 1.38 ms）。代码已开源，但论文未报告置信区间，且 LLM 实验仅覆盖 1B 参数模型，缺乏对更大规模模型的验证。

## 关联研究分析

从问题动机看，CRISP 与 RECAST 同属模板混合路线，但 CRISP 将混合系数从向量扩展为矩阵，解决了 RECAST 仅在极小参数预算下有效的问题。这一差异源于任务特性：RECAST 假设任务适配可通过少量系数完成，而 CRISP 承认复杂任务需要更丰富的混合结构。然而，CRISP 的 SiLU 门控是否在所有任务类型上均优于线性混合，论文未提供跨模态的对比证据，查询侧增强在数据充足时是否仍有增益，论文未给出回答。

从方法设计看，CRISP 与 Basis Sharing 同属共享基矩阵路线，但 CRISP 引入了两阶段 Retrofitting 策略，通过教师-学生蒸馏解决压缩后的初始化问题。这一设计解决了 Basis Sharing 在 ViT 架构上失效的问题，但增加了计算开销。相比之下，LoRA 等加法式方法无需 Retrofitting，但无法实现压缩。CRISP 的统一框架在压缩+PEFT 联合任务上优于串行组合，但其动态权重生成机制在推理时的计算开销是否抵消了压缩带来的加速，论文未提供边缘设备上的实测数据。

## 总结

CRISP 旨在解决 PEFT 与 MC 在参数重组层面的兼容性断裂问题，通过共享基矩阵与门控混合矩阵的统一框架，实现了压缩率与任务性能的双重优化。该方法在 VTAB-1K 上以 59.2% 的准确率超越 SOTA 1.5%，在 ViT-B/16 的 50% 压缩率下比 DGMR 高 1.4 个点。然而，CRISP 的推理延迟 1.52 ms 高于 DoRA 的 1.38 ms，且 LLM 实验仅覆盖 1B 参数模型，缺乏对更大规模模型的验证。当模型规模扩展至 7B 以上时，Retrofitting 阶段的蒸馏开销是否成为瓶颈，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.27383)