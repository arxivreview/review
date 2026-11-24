# ICLR2026最新论文 ｜DTO-KD: DYNAMIC TRADE OFF OPTIMIZATION FOR EFFECTIVE KNOWLEDGE DISTILLATION ｜动态权衡优化知识蒸馏

研究机构：澳大利亚国立大学、澳大利亚莫纳什大学

作者：Zeeshan Hayder、Ali Cheraghian、Lars Petersson 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_19462532)

> 知识蒸馏长期受困于任务损失与蒸馏损失的固定权重失衡，导致梯度冲突或单一目标主导训练。现有方法依赖启发式调参，无法适应训练中快速变化的优化动态。本文提出DTO-KD，通过闭式解动态计算每步损失权重，在梯度层面实现帕累托最优平衡。该方法在Transformer架构上显著提升了收敛速度与精度，但其对CNN异构架构的适用性尚存疑。

## 研究背景

当学生模型同时接收教师软标签与真实硬标签监督时，两个目标的梯度方向可能相互抵消，或一方范数远大于另一方导致另一方被淹没。这种梯度冲突（Gradient Conflict, GrC）与梯度主导（Gradient Dominance, GrD）是知识蒸馏（Knowledge Distillation, KD）中阻碍高效知识转移的核心病理。传统方法通过固定超参数 $\alpha_1, \alpha_2$ 线性组合损失函数，但静态权重无法应对深层网络中非凸景观下梯度的剧烈波动，导致训练震荡或收敛停滞。

早期KD研究聚焦于Logit匹配与特征对齐，如FitNets引入投影层对齐维度，UHKD利用频域变换消除架构差异。这些方法解决了“信息如何传递”的问题，却未触及“优化过程如何稳定”这一底层机制。随着Transformer架构普及，教师与学生间的表示空间差异加剧，固定权重方案在ViT等模型上表现尤为脆弱。本文切入点在于将KD重构为多目标优化（Multi-Objective Optimization, MOO）问题，不再预设权重，而是通过梯度投影技术实时求解最优权衡，从而在动态变化的优化轨迹中维持帕累托前沿。

## 核心方法

### 方法参照系

标准KD训练流程为：前向传播获取教师与学生输出，计算蒸馏损失 $\mathcal{L}_{distill}$ 与任务损失 $\mathcal{L}_{task}$，加权求和后反向传播。本文问题与该通用流程的关键差异在于，拒绝使用固定权重 $\alpha$，转而将权重视为每步迭代中需动态求解的变量，以消除梯度层面的结构性冲突。

### 梯度冲突与主导的形式化

传统加权损失 $\mathcal{L}_{tot} = \alpha_1 \mathcal{L}_{distill} + \alpha_2 \mathcal{L}_{task}$ 的梯度为 $\mathbf{g}_{tot} = \alpha_1 \mathbf{g}_{dist} + \alpha_2 \mathbf{g}_{task}$。当 $\langle \mathbf{g}_{dist}, \mathbf{g}_{task} \rangle < 0$ 时发生GrC，当 $\|\mathbf{g}_{task}\| \gg \|\mathbf{g}_{dist}\|$ 时发生GrD。设计动机在于，固定 $\alpha$ 无法感知当前步长下两个梯度的几何关系，导致更新方向偏离帕累托前沿。本文定义改进速率 $r_{dist}(\mathbf{g}^t) = -\eta \langle \mathbf{g}_{dist}, \mathbf{g}^t \rangle$，旨在量化当前更新方向对单一目标的贡献，为后续动态加权提供依据。

### 闭式解动态权衡

在Stage 2中，本文求解最小化最坏情况改进速率的min-max问题。通过引入对偶变量 $\boldsymbol{\pi} = (\pi_1, \pi_2)^\top$ 并约束于单纯形 $\Delta$，推导出闭式解：

$$
\mathbf{g}^* = \mathbf{J}^t \boldsymbol{\pi}^*, \quad \boldsymbol{\pi}^* = \frac{\mathbf{G}^{-1} \mathbf{1}}{\mathbf{1}^\top \mathbf{G}^{-1} \mathbf{1}}
$$

其中 $\mathbf{G} = \mathbf{J}^{t\top} \mathbf{J}^t$ 为Gram矩阵，$\mathbf{1}$ 为全1向量。该公式的物理含义是：最优权重 $\boldsymbol{\pi}^*$ 由两个梯度在特征空间中的夹角与范数共同决定，自动抑制冲突方向并平衡量级。相比Liu et al. (2023)的迭代求解，此闭式解每步仅需一次矩阵求逆，计算开销极低，确保了在大规模训练中实时适应梯度动态的能力。

## 实验评估

| 任务 | 模型 | 方法 | Top-1/AP | 教师 |
| :--- | :--- | :--- | :--- | :--- |
| ImageNet-1K | DeiT-Ti | DTO-KD | 79.7 | RegNetY-160 |
| ImageNet-1K | DeiT-Ti | Vk_D | 78.3 | RegNetY-160 |
| ImageNet-1K | DeiT-S | DTO-KD | 83.1 | RegNetY-160 |
| COCO | ViDT-nano | DTO-KD | 43.7 | ViDT-base |
| COCO | ViDT-nano | Vk_D | 43.0 | ViDT-base |

实验覆盖ImageNet-1K分类与COCO检测，基线包含Logit级（KD）、特征级（FitNet）及Token级（Vk_D）方法，但缺失频域对齐类强基线（如UHKD）。在ImageNet-1K上，DTO-KD以300 epochs训练即超越Vk_D 1.4个百分点，且优于训练1000 epochs的基线3.1个百分点，验证了动态权衡对收敛效率的提升。在COCO检测任务中，DTO-KD在ViDT-nano上取得43.7 AP，较Vk_D提升0.7 AP，表明该方法在复杂定位任务中有效缓解了梯度主导导致的定位误差。

消融实验显示，移除梯度裁剪（Grad. Clip）导致AP从43.7降至43.6，移除投影（Proj）降至43.1，表明投影层对特征对齐的贡献大于裁剪。值得注意的是，当教师缩小至ViDT-small时，DTO-KD仍保持43.2 AP，优于无蒸馏基线40.4 AP，证明方法对教师规模具有鲁棒性。然而，在CIFAR-100 CNN架构上，DTO-KD（72.35%）低于ReviewKD++（73.54%），暗示其优势主要依赖于Transformer架构的梯度特性，而非普适的蒸馏机制。

评估协议未报告置信区间，且代码未公开，可复现性受限。超参数设置遵循DeiT与ViDT原始配置，未针对DTO-KD单独调优，这削弱了“无需调参”主张的严谨性。GPU使用4块H100，计算资源充足，但缺乏在资源受限边缘设备上的效率对比。

## 关联研究分析

从问题动机看，DTO-KD与UHKD（Yu et al., 2025）均针对异构架构蒸馏，但UHKD聚焦于表示空间的几何对齐，通过频域变换消除拓扑差异；DTO-KD则聚焦于优化过程的动态平衡，通过梯度投影消除冲突。UHKD在ImageNet异构蒸馏中达到75.66%，而DTO-KD在CIFAR-100 CNN上仅72.35%，差异根源在于：UHKD显式处理了CNN与ViT间的特征分布差距，而DTO-KD假设梯度平衡足以弥补表示差异，这一假设在CNN架构上可能失效。

从方法设计看，DTO-KD与Liu et al. (2023)同属多目标优化框架，但Liu et al.采用迭代求解对偶问题，计算开销随维度增加而上升；DTO-KD通过Gram矩阵闭式解实现常数级计算复杂度。这一改进在大规模Transformer训练中至关重要，因为每步迭代需处理高维梯度向量。然而，闭式解假设损失函数局部二次近似，在深层网络非凸景观下，Gram矩阵的条件数可能恶化，导致 $\mathbf{G}^{-1}$ 数值不稳定，论文未对此进行理论分析或实验验证。

## 总结

DTO-KD旨在解决知识蒸馏中任务与蒸馏损失的固定权重失衡问题，通过闭式解动态计算梯度权重，实现了帕累托最优的优化路径。该方法在ImageNet-1K上以300 epochs超越1000 epochs基线3.1个百分点，在COCO检测中较Vk_D提升0.7 AP，证明了动态权衡对收敛效率与精度的双重提升。其边界在于，CIFAR-100 CNN架构上的性能低于ReviewKD++，暴露了方法对Transformer架构的依赖性。当教师与学生均为CNN且容量差距巨大时，仅靠梯度平衡能否弥补表示空间的结构性差异，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_19462532)