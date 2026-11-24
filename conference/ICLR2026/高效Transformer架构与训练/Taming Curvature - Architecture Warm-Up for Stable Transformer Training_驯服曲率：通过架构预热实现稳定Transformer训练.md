# ICLR2026最新论文 ｜Taming Curvature: Architecture Warm-Up for Stable Transformer Training ｜驯服曲率：通过架构预热实现稳定Transformer训练

作者：Sameera Ramasinghe、Ajanthan Thalaiyasingam、Hadi Mohaghegh Dolatabadi 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.16768)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.16768)

> 大模型训练常因损失尖峰或发散浪费算力，现有稳定化手段如QK-Norm仅针对注意力局部问题，缺乏对全局优化动态的监控。本文切入点在于将Edge of Stability (EoS) 理论中的曲率控制从离线分析转化为在线工程实践，通过Warm-started Power Iteration实时追踪预条件Hessian最大特征值，并据此动态调整网络有效深度。该方法在1B参数规模下显著降低了训练不稳定性，但其优势能否外推至更大规模及非递归架构仍存疑。

## 研究背景

当优化器步长与损失景观曲率的乘积超过稳定性边界时，训练过程将陷入振荡或发散。这一现象在Edge of Stability (EoS) 理论中被形式化为 $\eta \lambda_{max}(H) \approx 2$ 的临界条件，其中 $\eta$ 为步长，$\lambda_{max}(H)$ 为Hessian矩阵最大特征值。对于Adam等自适应优化器，该条件扩展为预条件曲率 $\lambda_{max}(G_t)$，其稳定性阈值与学习率成反比。然而，在十亿参数级模型中，在线估计Hessian特征值因内存与计算开销巨大而难以实现，导致EoS理论长期停留在小规模模型的理论验证阶段，无法直接指导大规模训练中的动态稳定控制。

主流稳定化策略多采用静态干预，如Softcap限制Logit幅度、QK-Norm约束点积规模，或固定学习率预热。这些方法虽能缓解局部饱和，但未能解决深层网络中曲率随深度增长导致的系统性不稳定。现有研究缺乏一种低开销、可在线执行的曲率监控机制，使得训练过程无法根据实时曲率动态调整架构状态。本文旨在填补这一空白，通过高效的在线曲率估计器，将EoS理论转化为可执行的架构控制策略，从而在保持收敛速度的同时消除损失尖峰。

## 核心方法

### 方法参照系

标准Transformer训练依赖固定架构与静态优化器配置，稳定性依赖经验性的学习率调度与注意力正则化。本文问题的关键差异在于引入“动态架构状态”作为控制变量，将网络深度视为可调节的曲率预算，而非固定超参数。

### 在线曲率追踪：Warm-started Power Iteration

传统Power Iteration需从随机向量初始化，在高维空间中收敛缓慢。本文利用Hessian特征向量在训练步间变化缓慢的特性，提出Warm-started Power Iteration。设计动机在于解决大规模模型中在线曲率估计的计算瓶颈，使每步仅需少于5次Hessian-Vector Product (HVP)。

$$
\epsilon_k = \angle(v_{1,k+1}, v_{1,k}) \leq \frac{L_H \|\theta_{k+1} - \theta_k\|}{\gamma}
$$

该公式表明，在Hessian Lipschitz连续且谱间隙 $\gamma$ 非零条件下，相邻步长主特征向量的夹角 $\epsilon_k$ 受参数变化量约束。基于此，本文证明Warm-started Power Iteration的迭代次数 $t$ 满足 $t \ll t_{rand}$，其中 $t_{rand}$ 为随机初始化所需迭代数。对于预条件Hessian $G_t = P_t^{-1/2} H P_t^{-1/2}$，由于预条件器 $P_t$ 变化缓慢，上述结论直接推广，使得在线追踪 $\lambda_{max}(G_t)$ 在十亿参数规模下成为可能。

### 架构预热：动态深度控制

基于在线曲率追踪，本文提出架构预热策略。设计动机在于解决固定学习率预热无法适应曲率动态变化的问题，通过控制有效深度来匹配稳定性阈值。

$$
\mathbf{X}_{l+1} = \mathbf{X}_l + \mathbf{W}_{p_l} \cdot \text{Block}(\mathbf{X}_l)
$$

在锁定阶段，投影权重 $\mathbf{W}_{p_l}$ 初始化为零并冻结，使得 $\text{Block}(\mathbf{X}_l)$ 对残差流的贡献为零，网络等效深度降低。当学习率开始衰减、稳定性阈值放宽时，按预定调度逐步解冻 $\mathbf{W}_{p_l}$。此过程避免了函数与梯度的不连续跳跃，确保 $\eta \lambda_{max}(G_t)$ 始终处于稳定包络内。与静态QK-Norm不同，该机制直接作用于优化几何结构，而非仅限制注意力局部行为。

## 实验评估

实验在FineWeb、DCLM和OLMo-Mix数据集上评估1B参数、16层Transformer，对比Baseline、QK-Norm、QK-Clip、Softcap及本文方法。基线覆盖了注意力正则化与优化器调整路线，但缺乏与Post-LN或µP等架构级稳定方法的直接对比。

| Dataset | Baseline | QK-Norm | QK-Clip | Softcap | Arch-Warmup |
| :--- | :--- | :--- | :--- | :--- | :--- |
| FineWeb | * | 49.88 ± 0.003 | * | 51.41 ± 0.002 | **25.02** ± **0.001** |
| DCLM | 165.62 ± 0.04 | 61.57 ± 0.012 | * | 43.38 ± 0.03 | **22.64** ± **0.002** |
| OLMo-Mix | * | * | * | * | **18.54** ± **0.001** |

在FineWeb上，Arch-Warmup困惑度25.02显著优于QK-Norm的49.88，且避免了QK-Clip的发散。在Chinchilla计算最优设置下，Arch-Warmup困惑度18.35优于QK-Norm的20.28和Softcap的32.44。

| Method | Val PPL (FineWeb) |
| :--- | :--- |
| QK-Norm | 20.28 |
| Softcap | 32.44 |
| Arch-Warmup | **18.35** |

消融实验显示，移除学习率预热仅保留架构预热时，模型仍能稳定收敛，表明架构预热本身足以提供稳定性保障。QK-Clip在多个数据集上出现NaN发散，凸显了静态裁剪策略在动态优化景观中的脆弱性。

评估边界限于1B参数规模，未验证7B以上模型的有效性。代码未公开，超参数如解冻调度间隔（500步）的敏感性仅在附录中简要提及，缺乏系统性消融。

## 关联研究分析

从问题动机看，本文与Post-LayerNorm Is Back (Chen and Wei, 2026) 均针对深层训练稳定性，但前者通过调整归一化位置改善梯度传播，本文通过动态深度控制曲率。差异根源在于：Post-LN解决的是信号衰减问题，而本文解决的是优化几何中的曲率爆炸问题。两者是否互补，即同时应用是否会产生冗余或冲突，论文未给出回答。

从方法设计看，本文与Completed Hyperparameter Transfer (Mlodozeniec et al., 2025) 均关注跨规模训练稳定性，但µP通过参数化规则实现超参数迁移，本文通过架构状态动态调整。µP假设小模型最优配置可近似迁移至大模型，而本文认为曲率动态随深度非线性变化，需实时干预。这种分歧暗示，在极端深度下，静态超参数迁移可能失效，动态架构控制成为必要补充。

## 总结

本文核心矛盾在于大规模Transformer训练中曲率动态变化与静态稳定化策略的失配。切入点在于利用Hessian特征向量慢变特性，实现低开销在线曲率追踪，从而将EoS理论转化为可执行的架构控制。方法通过Warm-started Power Iteration与架构预热，在1B规模下将FineWeb困惑度从49.88降至25.02，验证了动态深度控制的有效性。边界在于实验限于1B参数，且未与架构级稳定方法如Post-LN直接对比。当模型规模扩展至7B以上时，架构预热的计算开销与稳定性收益是否仍保持正相关，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.16768)