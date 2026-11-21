# CVPR2026最新论文 ｜FMPose3D: monocular 3D pose estimation via flow matching ｜基于流匹配的单目3D姿态估计

研究机构：瑞士洛桑联邦理工学院

作者：Ti Wang、Xiaohang Yu、Mackenzie Weygandt Mathis

论文原文见 [arXiv](https://arxiv.org/abs/2602.05755)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.05755)

> 单目3D姿态估计受限于深度歧义，确定性回归易陷入平均化伪影，而扩散模型虽能生成多假设但推理耗时过长。FMPose3D利用流匹配学习确定性速度场，以极少步数高效采样3D姿态分布，并通过重投影误差加权聚合多假设。该框架在保持生成多样性的同时实现了实时推理，但在绝对精度上仍落后于最新的确定性回归架构，其跨物种泛化能力提供了新的应用维度。

## 研究背景

单目图像中同一2D投影对应无限多3D姿态，这种物理多解性使得直接回归单一坐标必然产生模糊结果。为量化不确定性，研究者引入多假设生成策略，早期混合密度网络（Mixture Density Network, MDN）受限于固定候选数与低多样性，近期扩散模型通过迭代去噪提升了样本质量，但其随机微分方程（Stochastic Differential Equation, SDE）求解过程需10-15步甚至更多，导致推理延迟难以满足实时交互需求。

该领域主流路线在精度与效率间存在显著权衡：确定性方法如SasMamba凭借线性复杂度架构在Human3.6M上取得36.42mm MPJPE，但无法表征分布不确定性；生成式方法如DiffPose虽能捕捉多解性，却因多步去噪导致FPS低至3.36。FMPose3D的切入点在于替换生成内核，利用普通微分方程（Ordinary Differential Equation, ODE）驱动的流匹配（Flow Matching, FM）机制，将姿态估计重构为条件分布传输问题，旨在以确定性轨迹的高效积分替代随机去噪，从而在保留多假设生成优势的同时突破实时性瓶颈。

## 核心方法

### 条件分布传输范式

本文遵循2D-to-3D提升范式，将3D姿态估计从确定性回归转变为条件分布传输。不同于扩散模型逐步去除噪声，FM学习一个连续的速度场，将标准高斯先验直接传输至给定2D观测下的3D姿态分布。这一设计解决了扩散模型在实时场景下因迭代步数过多导致的延迟问题，同时保留了通过不同噪声种子生成多样假设的能力。

### 流匹配训练与采样

训练阶段，模型学习预测从噪声到目标姿态的瞬时速度。给定2D条件 $c$ 和3D目标 $x_1$，采样噪声 $x_0 \sim \mathcal{N}(0, I)$ 和时间 $t \sim U[0,1)$，构造线性插值中间状态：

$$ x_t = (1-t)x_0 + t x_1 $$

网络 $v_\theta(x_t, t, c)$ 被训练以最小化预测速度与目标速度 $v_t = x_1 - x_0$ 之间的均方误差。推理时，仅需3步欧拉积分即可从噪声采样得到3D姿态，相比扩散模型的50步去噪，计算复杂度大幅降低，使得生成40个假设仍能达到145.59 FPS。

### 重投影后验期望聚合

多假设生成后需融合为单一预测。本文提出重投影后验期望聚合（Reprojection-based Posterior Expectation Aggregation, RPEA），基于贝叶斯决策理论，将2D重投影误差作为似然代理。对于第 $j$ 个关节的 $N$ 个候选位置，首先过滤出重投影损失最低的Top-K候选，然后计算加权平均：

$$ \hat{X}_{RPEA, j} = \frac{\sum_{i \in H_{K,j}} w_i H_{i,j}}{\sum_{i \in H_{K,j}} w_i} $$

其中权重 $w_i$ 由重投影误差的指数函数决定。该设计避免了简单平均对低质量假设的稀释，也克服了逐关节选择最佳候选导致的解剖结构断裂，理论上更接近最小均方误差（MMSE）估计器。

## 实验评估

| 方法 | 假设数 N | Human3.6M MPJPE (mm) | MPI-INF-3DHP PCK (%) |
| :--- | :--- | :--- | :--- |
| DiffPose | 5 | 49.7 | - |
| FMPose3D | 2 | 49.3 | 85.9 |
| FMPose3D | 40 | 47.3 | - |
| FMPose3D | 20 | - | 86.4 |

实验在Human3.6M和MPI-INF-3DHP上进行，基线覆盖确定性回归（SimpleBaseline, PerturbPE）与概率生成（CVAE, DiffPose）两类方法，但缺失SasMamba等最新Mamba架构基线。FMPose3D在Human3.6M上以47.3mm MPJPE优于DiffPose的49.7mm，在MPI-INF-3DHP跨域测试中PCK达86.4%，优于UGRN的84.1%。

| 聚合策略 | 假设数 N | Human3.6M MPJPE (mm) |
| :--- | :--- | :--- |
| Mean | 40 | 48.2 |
| JPMA (Joint-wise) | 40 | 47.8 |
| RPEA (Joint-wise) | 40 | 47.3 |

消融实验显示，RPEA相比Mean策略降低0.9mm MPJPE，且随假设数增加性能提升更显著。并行GCN+Attention骨干优于串行结构，MPJPE从50.5mm降至49.3mm。推理速度测试表明，FMPose3D在3步积分下达到160.11 FPS，而DiffPose即使使用DDIM加速也仅为27.15 FPS，效率差距显著。

评估指标涵盖MPJPE、P-MPJPE、PCK与AUC，但未报告置信区间。代码已开源，超参数如温度 $\alpha$ 与Top-K值在补充材料中提供。动物数据集Animal3D与CtrlAni3D上的SOTA结果验证了框架的跨物种适应性，但缺乏与专用动物姿态方法的直接对比。

## 关联研究分析

从生成机制看，FMPose3D与DiffPose的核心差异在于SDE与ODE的求解路径。DiffPose依赖随机去噪，每一步引入随机性以探索分布，但累积误差与计算开销随步数线性增长；FMPose3D利用FM的确定性轨迹，仅需3步积分即可收敛，这得益于速度场学习的平滑性。然而，这种确定性也限制了分布探索的深度，当2D观测极度模糊时，FM生成的假设多样性可能低于扩散模型，论文未提供极端遮挡场景下的定量对比。

从聚合策略看，RPEA与DiffPose采用的Mean聚合存在本质区别。Mean假设所有假设同等可靠，忽略了重投影误差的差异；RPEA引入似然加权，理论上更优。但RPEA依赖重投影误差作为似然代理，这一假设隐含了相机内参精确且2D检测无噪声的前提。在野外场景中，2D检测误差可能主导重投影损失，导致权重分配失真，论文在MPI-INF-3DHP上使用真值2D姿态，掩盖了这一潜在风险。

## 总结

FMPose3D旨在解决生成式姿态估计中精度与实时性的矛盾，通过流匹配将多步随机去噪替换为少步确定性积分，并以RPEA实现鲁棒的多假设融合。实验证明其在Human3.6M上以47.3mm MPJPE超越DiffPose，推理速度提升近6倍。然而，其绝对精度仍落后于SasMamba等确定性回归方法，且RPEA对2D检测质量的依赖在野外场景中未被充分验证。当2D输入包含显著检测噪声时，重投影误差作为似然代理的有效性是否依然成立，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.05755)