# ACL-Findings2026最新论文 ｜HTMuon: Improving Muon via Heavy-Tailed Spectral Correction ｜重尾谱修正优化器

研究机构：美国达特茅斯学院、美国国际计算机科学研究所

作者：Tianyu Pang、Yujie Fang、Zihang Liu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.10067)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.10067)

> Muon 优化器通过正交化实现谱均匀化，但其将动量矩阵所有奇异值归一化为 1 的操作抑制了权重矩阵经验谱密度（ESD）的重尾特性，违背了重尾自正则化（HT-SR）理论中“重尾谱与模型质量正相关”的结论，导致泛化性能受限。本文切入点在于识别出正交化对噪声主导方向的过度加权及谱尾部抑制效应，提出 HTMuon 通过奇异值幂次变换恢复重尾性。该方法在 LLaMA 预训练中显著降低困惑度，但 p 值选取缺乏自适应机制，且在小样本视觉任务上未超越基线，其泛化边界尚待厘清。

## 研究背景

当 LLM 训练进入千亿参数规模，优化器需平衡收敛速度与泛化质量。传统 Adam 采用逐元素自适应，忽略参数间几何耦合；Muon 引入矩阵正交化，将更新视为 Schatten-∞ 范数下的最速下降，解决了梯度病态问题。然而，正交化强制所有奇异方向权重相等，使更新谱呈轻尾分布。根据 HT-SR 理论，良好训练的网络权重 ESD 应呈重尾分布，重尾程度与模型质量强相关。Muon 的轻尾更新导致权重谱重尾性不足，限制了最终性能。

现有 Muon 变体如 NorMuon 聚焦于降低更新方差，AdaMuon 引入自适应学习率，但均未触及谱尾部结构这一根本缺陷。Chang et al. (2025) 证明了 Muon 的收敛性，但假设梯度噪声有界二阶矩，未考虑谱结构对泛化的影响。本文抓住“正交化抑制重尾谱”这一被忽略的机制，将优化目标从单纯收敛速度转向谱结构调控，提出在保留矩阵耦合能力的同时恢复重尾特性。

## 核心方法

### 方法参照系

标准 Muon 通过 Newton-Schulz 迭代近似计算动量矩阵 $\mathbf{M}_t$ 的极分解因子 $\mathbf{O}_t = \mathbf{U}_t \mathbf{V}_t^\top$，其中 $\mathbf{U}_t, \mathbf{V}_t$ 为奇异向量。该操作等价于将 $\mathbf{M}_t$ 的所有奇异值设为 1，实现谱均匀化。本文问题与该通用流程的关键差异在于：均匀化虽加速早期收敛，但抑制了权重 ESD 的重尾性，导致后期训练对噪声敏感且泛化受限。

### 奇异值幂次变换

标准 Muon 在正交化环节丢弃尺度信息，本文在此处引入幂次参数 $p \in (0,1)$，将奇异值 $\sigma_k$ 变换为 $\sigma_k^p$。设计动机是解决正交化对噪声主导方向（小奇异值）的过度加权问题，通过保留部分尺度信息恢复重尾性。

$$
\mathbf{O}_t^{HT} = \mathbf{U}_t \boldsymbol{\Sigma}_t^p \mathbf{V}_t^\top, \quad \boldsymbol{\Sigma}_t^p = \text{diag}(\sigma_1^p, \sigma_2^p, \dots, \sigma_m^p)
$$

当 $p=0$ 时退化为 Muon，$p=1$ 时退化为 SGDM。$p \in (0,1)$ 使更新谱比 Muon 更重尾，同时保留矩阵耦合能力。根据 Lemma 4.1，若动量矩阵奇异值服从 $\sigma_k = \sigma_1 k^{-s}$，则 HTMuon 更新矩阵的幂律指数 $\alpha = 1 + \frac{2}{sp}$，$p$ 越小 $\alpha$ 越大，谱越重尾。

### Schatten-q 范数等价性

HTMuon 的更新规则等价于 Schatten-$q$ 范数约束下的最速下降，其中 $q = \frac{1}{1-p}$。这一理论结果将 Muon 的 Schatten-∞ 等价性推广至有限 $q$，为谱尾修正提供了几何解释。

$$
\min_{\mathbf{G}} \nabla L(\mathbf{W})^\top \mathbf{G} \quad \text{s.t.} \quad \|\mathbf{G}\|_{S_q} \leq 1
$$

该等价性表明 HTMuon 在保持收敛速率的同时，通过调整范数约束改变了优化路径的谱分布，从而改善泛化。

## 实验评估

实验在 C4、OpenWebText、CIFAR-10/100、ImageNet-1K 上进行，基线覆盖 AdamW、Muon、NorMuon、AdaMuon、COSMOS 等，但缺失 Dion2、EF21-Muon 等分布式变体。

| 模型 | 数据集 | AdamW | Muon | HTMuon |
|---|---|---|---|---|
| LLaMA-60M | C4 | 31.85 | 28.80 | 27.88 |
| LLaMA-135M | C4 | 23.33 | 22.23 | 21.25 |
| GPT-2 small | OpenWebText | 25.19 | 22.46 | 22.20 |
| ResNet18 | CIFAR-10 | - | 95.16 | 95.63 |
| ViT-Tiny | ImageNet-1K | 67.67 | 71.02 | 71.16 |

HTMuon 在 LLaMA-60M 上比 Muon 降低 0.92 PPL，在 LLaMA-135M 上降低 0.98 PPL，验证了重尾修正对 LLM 预训练的有效性。在 CIFAR-10 上，HTMuon 比 Muon 提升 0.47% 准确率，但在 CIFAR-100 上仅提升 0.31%，且未超越知识库记录的 Muon 基线（78.57%），表明小样本视觉任务对重尾谱的敏感性较低。

消融实验显示，$p=0.125$ 为最优值，$p$ 过小（接近 0）导致谱过轻，$p$ 过大（接近 1）退化为 SGDM 失去矩阵耦合能力。HTMuon 与 NorMuon 组合可进一步降低 PPL，表明谱修正与方差缩减机制互补。

评估边界方面，论文未报告置信区间，且 p 值需网格搜索，缺乏自适应机制。代码已开源，但超参数调优依赖特定模型规模，跨规模迁移性未充分验证。

## 关联研究分析

从问题动机看，本文与 LiMuon (Huang et al., 2025) 均关注 Muon 的理论缺陷，但 LiMuon 聚焦样本复杂度，通过随机 SVD 降低计算开销，而本文聚焦谱结构对泛化的影响，通过幂次变换恢复重尾性。这一差异源于任务特性：LiMuon 针对高维非凸优化的收敛瓶颈，本文针对 LLM 预训练的泛化瓶颈。

从方法设计看，本文与 COSMOS (Liu et al., 2025b) 均产生更重尾的谱，但 COSMOS 通过修改动量更新实现，本文通过奇异值变换实现。COSMOS 的重尾性源于其特定的预条件策略，而本文的重尾性源于显式的谱修正。这一差异暗示重尾谱可能通过多种机制实现，但本文的幂次变换提供了更直接的谱控制手段。

## 总结

本文要解决的核心矛盾是 Muon 正交化导致的谱均匀化与 HT-SR 理论要求重尾谱之间的冲突。本文抓住“正交化抑制重尾性”这一被忽略的机制，通过奇异值幂次变换在保留矩阵耦合能力的同时恢复重尾特性。HTMuon 在 LLaMA-60M 上比 Muon 降低 0.92 PPL，在 LLaMA-135M 上降低 0.98 PPL，验证了重尾修正的有效性。但 p 值需手动调优，且在 CIFAR-100 上未超越基线，表明其泛化边界受任务特性限制。当模型规模扩大至千亿参数时，p 值的最优选择是否随训练阶段动态变化，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.10067)