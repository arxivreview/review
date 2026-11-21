# ICLR2026最新论文 ｜FedMuon: Federated Learning with Bias-corrected LMO-based Optimization ｜联邦学习中 LMO 优化器的偏置校正与收敛性分析

研究机构：日本京都大学、日本冲绳科学技术大学院大学

作者：Yuki Takezawa、Anastasia Koloskova、Xiaowen Jiang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.26337)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.26337)

> 联邦学习场景下，直接复用 Muon 优化器会导致训练停滞，其根源在于线性最小化预言机（LMO）在异构数据分布中表现出系统性偏置。现有分布式 Muon 变体如 MuLoCo 仅适用于同质数据，缺乏理论保证。本文通过引入 SCAFFOLD 式控制变量校正 LMO 偏置，并首次量化了 Newton-Schulz 迭代次数对收敛范数的影响。该工作填补了 Muon 在联邦学习中的理论空白，但其实验规模与部分参与场景的缺失限制了结论的普适性。

## 研究背景

联邦学习要求客户端在保留本地数据隐私的前提下协同训练全局模型，其核心挑战在于客户端数据分布的非独立同分布（Non-IID）特性。为加速收敛，自适应优化器如 Adam 和 Muon 被引入，其中 Muon 通过将动量矩阵正交化至谱范数单位球，实现了比 AdamW 更高效的梯度下降。然而，Muon 依赖 LMO 求解正交化方向，这一操作在集中式训练中表现优异，但在分布式环境中，LMO 的输出并非无偏梯度估计，而是受客户端局部数据分布影响的有偏算子。

主流分布式 Muon 方案如 MuLoCo 允许客户端执行多步本地更新，但仅在客户端数据同质时有效，且在异构数据下被证明无法收敛至驻点。另一类方案如 Ahn et al. (2025) 尝试分布式求解 LMO，但通信开销巨大且不支持多步本地更新。这些方法的共同缺陷在于忽视了 LMO 算子本身的偏置特性，导致在联邦学习这一数据异构的基本场景下，优化过程停滞于初始参数附近，无法逼近全局最优解。

本文切入点在于识别 LMO 偏置是 Muon 在联邦学习中失效的根本原因，而非简单的通信瓶颈或计算开销。通过形式化证明 LocalMuon（即直接应用 Muon 的 FedAvg 变体）不收敛的下界，本文确立了必须引入偏差校正机制的理论必要性，从而将研究焦点从“如何高效通信”转向“如何消除算子偏置”。

## 核心方法

### 方法参照系

联邦学习标准流程为 FedAvg，其本地优化器通常为 SGD 或 Adam。本文问题与该通用流程的关键差异在于，本地优化器替换为基于 LMO 的 Muon。FedAvg 假设本地梯度估计是无偏的，但 LMO 输出 $\text{lmo}(\mathbf{M}_i)$ 并不满足 $\mathbb{E}[\text{lmo}(\mathbf{M}_i)] = \nabla f_i(\mathbf{X})$，导致聚合后的更新方向偏离全局梯度。

### 偏差校正机制

LocalMuon 的失效源于 LMO 的偏置性，即 $\frac{1}{n}\sum_{i=1}^n \text{lmo}(\mathbf{M}_i) \neq \nabla f(\mathbf{X})$。为消除这一偏置，FedMuon 引入控制变量 $\mathbf{C}_i^{(r)}$ 和 $\mathbf{C}^{(r)}$，分别估计客户端 $i$ 的局部梯度方向与全局梯度方向。更新规则修改为对校正后的动量进行 LMO 投影：

$$
\mathbf{X}_i^{(r,k+1)} = \mathbf{X}_i^{(r,k)} + \eta \cdot \text{lmo}\left( \mathbf{M}_i^{(r,k+1)} - \mathbf{C}_i^{(r)} + \mathbf{C}^{(r)} \right)
$$

该公式的物理含义是，先通过控制变量抵消局部数据分布引起的梯度偏差，再对无偏化的动量执行正交化。这一设计解决了 MuLoCo 在异构数据下停滞的问题，使得优化过程能够持续向全局驻点逼近，而非困于初始值。

### 非精确 LMO 的收敛性分析

精确求解 LMO 需要 SVD，计算成本极高，实践中采用 Newton-Schulz 迭代 $T$ 次近似。本文推导了 $T$ 对收敛率的影响，发现收敛范数从迹范数 $\|\cdot\|_1$ 过渡到 Schatten-$p$ 范数 $\|\cdot\|_p$，其中 $p$ 随 $T$ 增加而单调递减至 1。

$$
p = 1 + \frac{1}{\log\left( \frac{1}{1 - \kappa^{1.5T}} \right)}
$$

当 $T=0$ 时，$p=2$（Frobenius 范数）；当 $T \to \infty$ 时，$p \to 1$（迹范数）。由于 $\|\mathbf{A}\|_1 \leq \sqrt{\min(d_1, d_2)} \|\mathbf{A}\|_2$，增加 $T$ 可提升收敛速度，最大加速因子为 $\sqrt{\min(d_1, d_2)}$。这一分析揭示了近似正交化不仅可行，且精度越高，收敛越快，打破了“近似必然导致误差累积”的直觉。

## 实验评估

实验在 FashionMNIST 和 CIFAR-10 上进行，对比基线包括 FedAvg、SCAFFOLD、LocalMuon 及其 Adam 变体。基线覆盖了标准联邦学习算法和分布式 Muon 变体，但缺失 Dion2、NorMuon 等高效变体，且未包含大规模 LLM 预训练场景。

| 数据集 | 场景 | 方法 | 测试准确率 |
| :--- | :--- | :--- | :--- |
| FashionMNIST | 同质 ($\beta=10.0$) | FedMuon | 0.8 |
| FashionMNIST | 同质 ($\beta=10.0$) | SCAFFOLD | 0.6 |
| FashionMNIST | 异构 ($\beta=0.1$) | FedMuon | 0.8 |
| FashionMNIST | 异构 ($\beta=0.1$) | SCAFFOLD | 0.4 |
| CIFAR-10 | 同质 ($\beta=10.0$) | FedMuon | 0.8 |
| CIFAR-10 | 同质 ($\beta=10.0$) | SCAFFOLD | 0.5 |

在异构数据场景（$\beta=0.1$）下，FedMuon 在 FashionMNIST 上达到 0.8 的准确率，显著优于 SCAFFOLD 的 0.4 和 LocalMuon 的 0.6。这一差距验证了偏差校正机制在消除数据异构性导致的收敛偏差方面的有效性。CIFAR-10 上 FedMuon 同样优于 SCAFFOLD，但具体数值未提供，仅展示收敛曲线。

消融实验显示，Newton-Schulz 迭代次数 $T$ 对准确率有显著影响。在 FashionMNIST 上，$T=0$ 时准确率为 0.75，$T=1$ 时提升至 0.80，$T=4$ 时稳定在 0.85。这表明即使 $T=0$（即仅使用归一化梯度），FedMuon 也能收敛，但增加 $T$ 能显著提升最终精度，与理论预测的收敛范数改善一致。

评估边界方面，实验仅使用小规模图像分类数据集，未验证在大规模 LLM 预训练中的表现。协议局限在于仅测试全参与场景，部分参与下的收敛性未分析。可复现性方面，论文未提供代码 URL，超参数设置（如 $\alpha, \eta$）未在正文中详细列出，仅引用了 Newton-Schulz 的系数 $a=15/8, b=-5/4, c=3/8$。

## 关联研究分析

从问题动机看，FedMuon 与 MuLoCo 均旨在解决 Muon 的分布式扩展问题，但 MuLoCo 假设数据同质，而 FedMuon 直面异构数据这一联邦学习本质特征。MuLoCo 的失效源于其未考虑 LMO 的偏置性，而 FedMuon 通过控制变量显式校正这一偏置。这一差异并非技术细节，而是对联邦学习数据分布假设的根本性修正。MuLoCo 在异构场景下的失败是必然的，因为其优化目标与数据分布不匹配，而 FedMuon 的校正机制使其能够适应任意数据分布。

从方法设计看，FedMuon 与 SCAFFOLD 共享偏差校正框架，但 SCAFFOLD 使用欧几里得梯度，而 FedMuon 使用 LMO 正交化梯度。SCAFFOLD 的校正变量估计的是梯度本身，而 FedMuon 的校正变量估计的是 LMO 输出的偏差。这一设计差异源于 LMO 的非线性特性，使得简单的梯度校正不足以消除偏置。FedMuon 的校正机制更复杂，但更精确地针对 LMO 的几何特性，从而在矩阵参数优化中保留了 Muon 的谱均匀化优势。

## 总结

FedMuon 解决了 Muon 在联邦学习中因 LMO 偏置导致的不收敛问题，通过引入 SCAFFOLD 式控制变量校正偏置，并证明了任意 Newton-Schulz 迭代次数下均可收敛。实验表明，在异构数据下，FedMuon 在 FashionMNIST 上达到 0.8 准确率，显著优于 SCAFFOLD 的 0.4。其边界在于实验规模局限于小规模图像分类，且仅分析全参与场景。当客户端数据分布极度异构且部分参与比例较低时，控制变量的估计误差是否会抵消 LMO 的谱均匀化优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.26337)