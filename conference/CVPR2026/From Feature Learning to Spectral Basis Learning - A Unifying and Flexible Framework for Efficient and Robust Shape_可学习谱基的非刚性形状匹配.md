# CVPR2026最新论文 ｜From Feature Learning to Spectral Basis Learning: A Unifying and Flexible Framework for Efficient and Robust Shape Matching ｜可学习谱基的非刚性形状匹配

研究机构：浙江大学

作者：Feifan Luo、Hongyang Chen

论文原文见 [arXiv](https://arxiv.org/abs/2603.23383)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.23383)

> 非刚性3D形状匹配旨在建立两个网格间的密集点对应，其核心难点在于如何在非等距变形与拓扑噪声下保持几何一致性。现有深度功能映射方法仅优化特征描述符，而将拉普拉斯谱基视为固定组件，导致在强变形场景下匹配精度受限且计算开销高。本文提出Advanced Functional Maps框架，通过引入可学习的抑制函数动态调整谱基，并构建无监督端到端训练流程，首次实现特征与基函数的联合优化。该方法在SMAL等基准上超越了依赖外蕴基的现有方法，但在SCAPE等近等距任务上仍略逊于SOTA，其理论等价于谱卷积的洞察为后续研究提供了新视角，但极端非等距下的鲁棒性仍有待验证。

## 研究背景

非刚性形状匹配通常形式化为求解形状流形上的双射映射，其数学基础依赖于拉普拉斯-贝尔特拉米算子（Laplace-Beltrami Operator, LBO）的特征分解。LBO特征基提供了形状的内蕴几何表示，使得功能映射（Functional Maps）能够以紧凑的线性算子形式表达形状间的对应关系。然而，传统方法假设变形过程保持内蕴几何不变（即等距假设），当面对真实世界中的非等距变形或拓扑噪声时，固定的LBO基函数无法自适应地捕捉局部几何变化，导致匹配结果出现系统性偏差。

功能映射框架自2012年提出以来，已成为非刚性匹配的主流范式，其核心优势在于将高维点对应问题转化为低维谱空间的线性算子估计。随着深度学习兴起，FMNet等方法通过神经网络学习鲁棒特征描述符，取代了手工设计描述符，实现了端到端优化。然而，这些方法仅关注特征表示的学习，而忽视了谱基本身的优化潜力。现有SOTA方法如ULRSSM和HybridFMaps依赖复杂的辅助损失和迭代线性求解器，不仅训练范式复杂，且计算效率低下。本文的切入点在于指出谱基是功能映射管道中被忽视的关键组件，提出通过数据驱动方式优化基函数，从而在保持几何纯度的同时提升匹配精度与计算效率。

## 核心方法

### 方法参照系

标准深度功能映射流程包含特征提取、功能映射计算、损失约束及映射恢复四个阶段。其中，特征提取通常采用DiffusionNet等骨干网络，功能映射通过求解线性系统或谱投影计算，损失函数则施加正交性或双射性约束。本文的关键差异在于将固定的LBO特征基替换为可学习的自适应基函数，并在训练过程中联合优化特征与基函数，而非仅优化特征。

### 可学习谱基表示

传统方法中，LBO特征基 $\Phi_k$ 是固定的，无法适应特定形状的几何特性。本文引入抑制函数 $G = \text{diag}\{g_1, g_2, \dots, g_k\}$，其中 $g_i: \mathbb{R} \to (0, 1]$，定义可学习谱基为：

$$ \Psi_k = \Phi_k G $$

该公式的物理含义是：抑制函数作为滤波器，选择性地抑制不同频率的谱分量，从而增强基函数的表达能力。这一设计解决了固定基函数在非等距变形下无法自适应调整的问题，使得基函数能够根据数据分布动态调整，保留低频结构信息的同时增强高频细节的判别力。

### 无监督谱基学习

基于可学习谱基，本文提出无监督谱基学习方法，通过多分辨率无监督谱损失联合监督点映射、功能映射及基函数。损失函数定义为：

$$ \mathcal{L} = \mathcal{L}_{\text{pointwise}} + \mathcal{L}_{\text{functional}} + \mathcal{L}_{\text{basis}} $$

其中，$\mathcal{L}_{\text{pointwise}}$ 约束点映射的双射性，$\mathcal{L}_{\text{functional}}$ 约束功能映射的正交性，$\mathcal{L}_{\text{basis}}$ 则通过热扩散模块优化基函数。该设计摒弃了传统方法中昂贵的功能映射求解器和辅助损失，实现了端到端优化。热扩散模块采用多尺度、特征值无关的策略，通过指数滤波器 $f(\lambda) = e^{-t\lambda}$ 生成基函数，避免了单一扩散时间尺度对多尺度表示能力的限制。

## 实验评估

实验在FAUST、SCAPE、SMAL、TOPKIDS等标准基准上进行，对比方法覆盖谱方法优化路线（如ULRSSM、HybridFMaps、DiffZO）及部分几何度量方法，但缺失语义引导类方法（如UniMatch、GLASS）。

| 数据集 | 方法 | MGE |
|---|---|---|
| FAUST | Ours | 1.8 |
| FAUST | ULRSSM | 1.6 |
| SCAPE | Ours | 2.3 |
| SCAPE | RINO | 1.5 |
| SMAL | Ours | 2.6 |
| SMAL | Coarse-to-Fine Hybrid Self-Supervised | 2.9 |
| TOPKIDS | Ours | 4.9 |
| TOPKIDS | Coarse-to-Fine Hybrid Self-Supervised | 4.9 |

在FAUST上，本文MGE为1.8，略高于ULRSSM的1.6；在SCAPE上，本文MGE为2.3，显著高于RINO的1.5；在SMAL上，本文MGE为2.6，低于Coarse-to-Fine Hybrid Self-Supervised的2.9；在TOPKIDS上，本文MGE为4.9，与Coarse-to-Fine Hybrid Self-Supervised持平。这些结果表明，本文方法在非等距任务（SMAL）上表现优异，但在近等距任务（FAUST、SCAPE）上略逊于SOTA，可能源于缺乏外蕴弹性基的辅助。

消融实验显示，热扩散模块的多尺度策略对性能提升贡献最大，单一扩散时间尺度导致SMAL上MGE增加0.5。此外，绕过功能映射求解器使训练时间减少40%，但推理时间增加15%，表明计算效率的权衡主要存在于训练阶段。

评估指标仅使用MGE，缺乏PCK曲线或IoU等多维度指标；评估协议未统一控制预训练模型版本，不同方法使用的DiffusionNet骨干可能存在差异；代码已开源，但超参数配置未详细披露，可复现性受限。

## 关联研究分析

从方法设计看，本文与HybridFMaps的核心差异在于基函数的来源：HybridFMaps结合内蕴与外蕴弹性谱基，而本文仅使用可学习内蕴基。这一差异源于任务特性：HybridFMaps通过外蕴基补偿非等距畸变，而本文通过数据驱动的内蕴基优化实现类似效果。然而，在SCAPE等近等距任务上，本文性能低于HybridFMaps，暗示外蕴基在特定场景下仍具优势。从问题动机看，本文与ULRSSM均关注无监督匹配，但ULRSSM依赖测试时适应性，而本文通过基函数学习提升泛化能力。在跨数据集泛化实验中，本文在SHREC'19上MGE为5.9，优于ULRSSM的14.5，验证了基函数学习对泛化能力的提升。

## 总结

本文要解决的核心矛盾是固定谱基在非等距变形下的适应性不足与计算效率低下。现有方法仅优化特征，忽视基函数优化，导致性能受限；本文通过引入可学习抑制函数，首次实现特征与基函数的联合无监督优化。实验证明，该方法在SMAL上MGE为2.6，优于Coarse-to-Fine Hybrid Self-Supervised的2.9，但在SCAPE上MGE为2.3，高于RINO的1.5。本文的边界在于仅使用内蕴基，在极端非等距变形下可能失效，且缺乏语义先验解决跨类别歧义。当支持集增大到5-shot时，可学习基函数的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.23383)