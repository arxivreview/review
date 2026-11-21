# HuggingFace最新推荐论文 ｜Glance Forcing: Making Bidirectional Diffusion Autoregressive at a Glance ｜单样本轨迹解耦蒸馏：Glance Forcing

研究机构：武汉大学、电子科技大学

作者：Zhuobai Dong、Junchao Yi、Hu Jian Guo 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.20220)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.20220)

> 自回归视频扩散模型在实时流式生成中面临训练成本高昂的瓶颈，现有方法依赖大规模概率流常微分方程（PF-ODE）轨迹进行初始化，导致计算与存储开销巨大。本文发现单样本轨迹足以完成轨迹几何拉直，但高/低噪声阶段的曲率差异导致单模型拟合失效。Glance Forcing 通过双 LoRA 专家解耦高/低噪声阶段，并引入阶段特定损失函数，在单样本监督下实现高效蒸馏。该框架以极低数据成本超越现有基线，但其有效性是否依赖于特定骨干网络的强先验，仍需进一步验证。

## 研究背景

当自回归（Autoregressive, AR）视频生成模型试图通过因果滚动实现流式输出时，其核心挑战在于如何将预训练的双向扩散模型高效转化为少步因果学生模型。现有主流范式如 Causal Forcing 采用三阶段蒸馏流程：多步 AR 训练、因果 ODE 初始化、分布匹配蒸馏（Distribution Matching Distillation, DMD）。其中，因果 ODE 初始化阶段通常需要收集数千条 PF-ODE 轨迹以监督学生模型学习从噪声到数据的映射路径。这一过程不仅消耗数千 GPU 小时，还需存储 TB 级数据，构成了严重的预处理瓶颈。

尽管减少轨迹数量能降低开销，但激进地缩减至单样本会导致严重的性能崩溃。本文通过轨迹几何分析发现，扩散轨迹的曲率分布极不均匀：超过 92.5% 的累积轨迹曲率集中在高噪声区域，该区域主导语义布局与运动合成；而低噪声区域则负责细节纹理细化。这两种截然不同的优化行为若由单一模型拟合，会产生严重的表示干扰。因此，如何在极稀疏监督下避免这种干扰，成为突破蒸馏效率瓶颈的关键。

## 核心方法

### 方法参照系：三阶段蒸馏流程

Glance Forcing 建立在 Causal Forcing 的三阶段蒸馏框架之上，该框架旨在将双向教师模型转化为少步 AR 学生模型。标准流程中，第二阶段“因果 ODE 初始化”利用教师模型生成的 PF-ODE 轨迹，通过一致性蒸馏（Consistency Distillation）损失监督学生模型，使其能够直接映射噪声状态至数据端点。本文的关键差异在于，将这一阶段所需的监督数据从大规模轨迹集压缩至单样本轨迹，并针对单样本拟合中的几何冲突引入解耦机制。

### 单样本轨迹的几何充分性

传统观点认为，ODE 初始化需要大量数据以覆盖数据分布。本文提出假设：ODE 初始化的主要功能是重塑长步扩散轨迹的几何形状，使其变为平滑的少步流，而非完全建模数据分布。为验证此假设，本文定义轨迹直度（Trajectory Straightness）$S$ 与步间余弦相似度（Step-wise Cosine Similarity）作为几何度量：

$$ S = \frac{\|z_T - z_0\|_2}{\sum_{t=1}^T \|z_t - z_{t-1}\|_2} $$

$$ CosSim_t = \frac{v_t \cdot V_{total}}{\|v_t\|_2 \|V_{total}\|_2} $$

实验表明，仅使用单样本轨迹进行 ODE 初始化，其生成的轨迹几何指标与使用 3K 样本轨迹的结果差异微小。这证实了单样本轨迹已提供足够的几何监督以建立平滑流，而分布质量的精修可交由后续的 DMD 阶段完成。这一发现打破了“大规模轨迹监督必要”的隐含共识，将数据依赖从分布覆盖转向几何覆盖。

### 双 LoRA 专家解耦与阶段特定损失

尽管单样本轨迹在几何上充分，但单一学生模型难以同时拟合高曲率的高噪声阶段与低曲率的低噪声阶段。为此，本文引入双 LoRA（Low-Rank Adaptation）架构，将去噪过程解耦为 Slow-LoRA 与 Fast-LoRA 两个专家。Slow-LoRA 专攻高噪声阶段（$t \ge t_\kappa$），负责语义布局与运动合成；Fast-LoRA 专攻低噪声阶段（$t < t_\kappa$），负责细节纹理细化。

针对各专家的功能特性，本文设计了阶段特定损失函数。对于 Slow-LoRA，引入时间频率谱损失（Temporal Frequency Spectrum Loss, $L_{TFS}$），通过一维离散傅里叶变换（1D-DFT）对齐时间域能量分布，抑制高频闪烁并保留运动动态：

$$ L_{TFS} = \||\mathcal{F}_{1D-DFT}(\hat{x}_{t_0})| - |\mathcal{F}_{1D-DFT}(x_{t_0})|\|_2^2 $$

对于 Fast-LoRA，引入空间高通损失（Spatial High-Pass Loss, $L_{HP}$），利用固定 2D 拉普拉斯算子提取空间高频边缘，强化纹理清晰度：

$$ L_{HP} = \|H(\hat{x}_{t_0}) - H(x_{t_0})\|_2^2 $$

该解耦架构通过分离冲突的优化目标，解决了单模型在极稀疏监督下的表示干扰问题，实现了在单样本条件下的高质量蒸馏。

## 实验评估

实验在 VBench 与 VisionReward 基准上进行，基线覆盖双向模型（Wan2.1, LTX）、AR 模型（SkyReels-V2, MAGI-1）及蒸馏 AR 模型（CausVid, Self Forcing, Causal Forcing）。主结果如表 1 所示，Glance Forcing 在单样本（1 sample）设置下即超越 Causal Forcing（3k samples），VBench Total 得分从 82.01 提升至 82.09，且动态度（Dynamic Degree）与指令遵循（Instruction Following）显著改善。当训练预算扩展至 25k 样本时，Glance Forcing 达到 84.33 的 VBench Total 得分，优于 Causal Forcing 的 84.04。

| Model | Data | Total ↑ | Quality ↑ | Semantic ↑ | Dyn. ↑ | Vision. ↑ | Instruct. ↑ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Causal Forcing | 3k | 82.01 | 82.59 | 79.73 | 64 | 0.603 | 50 |
| Glance Forcing | 3k | 82.69 | 83.33 | 80.11 | 63 | 2.310 | 52 |
| Glance Forcing | 1 | 82.09 | 83.68 | 75.72 | 70 | 0.489 | 30 |
| Causal Forcing | 25k | 84.04 | 84.59 | 81.84 | 68 | 6.326 | 56 |
| Glance Forcing | 25k | 84.33 | 85.01 | 81.64 | 78 | 6.921 | 69 |

消融实验验证了双专家解耦的有效性。如表 2 所示，仅使用 Slow 专家或 Fast 专家均导致性能下降，而组合两者（Slow+Fast）在 VBench Total 上达到 84.33，显著优于单一模型变体。此外，人类偏好研究显示，Glance Forcing 对 Self Forcing 和 Causal Forcing 的胜率分别为 91.3% 和 63.3%，证实了感知质量的提升。

| Model | Total ↑ | Quality ↑ | Semantic ↑ | Dynamic ↑ | Vision ↑ | Instruct ↑ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| S2–F2 (Ours) | 84.33 | 85.01 | 81.64 | 78 | 6.921 | 69 |
| S1–F3 | 83.92 | 84.65 | 81.00 | 76 | 2.865 | 41 |
| S3–F1 | 84.01 | 85.05 | 79.85 | 68 | 4.210 | 55 |
| S4 | 83.42 | 84.80 | 77.90 | 55 | 2.450 | 43 |
| F4 | 83.15 | 84.20 | 78.95 | 72 | 1.310 | 31 |

评估边界方面，实验主要基于 Wan2.1-1.3B 骨干网络，未在其他架构上验证单样本初始化的普适性。此外，单样本研究指出，低运动与开放域样本更利于初始化，而高运动与特定域样本会导致更大性能退化，表明单样本策略对样本特性敏感。

## 关联研究分析

从问题动机看，Glance Forcing 与 Causal Forcing 同属 AR 视频蒸馏路线，但二者对 ODE 初始化功能的理解存在根本分歧。Causal Forcing 视 ODE 初始化为分布建模的关键步骤，因此依赖大规模轨迹；Glance Forcing 则将其重新定义为几何拉直过程，认为单样本即可满足几何覆盖需求。这一差异源于对轨迹曲率分布的实证分析，揭示了高噪声区域曲率主导性这一被忽略的几何特性。

从方法设计看，Glance Forcing 与 Self Forcing 均致力于解决训练-推理分布不一致问题，但路径不同。Self Forcing 通过自展开训练对齐分布，但仍需大量数据；Glance Forcing 通过双 LoRA 解耦优化目标，在极稀疏数据下实现高效拟合。双 LoRA 架构是否比动态调整单模型注意力权重更具泛化性，论文未给出跨骨干网络的对比证据。

## 总结

本文针对 AR 视频蒸馏中 PF-ODE 轨迹收集成本高昂的问题，提出 Glance Forcing 框架。通过发现单样本轨迹足以完成几何拉直，并引入双 LoRA 专家解耦高/低噪声阶段的优化冲突，实现了在单样本监督下的高质量蒸馏。实验证明，该方法在 VBench Total 上达到 84.33，超越 Causal Forcing 基线，且训练成本降低数个数量级。然而，单样本策略对样本运动动态与域特异性敏感，且仅在 Wan2.1 骨干上验证。当骨干网络先验较弱或视频内容高度动态时，单样本轨迹的几何充分性是否依然成立，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.20220)