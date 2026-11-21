# ICLR2026最新论文 ｜Persistence Spheres: Bi-continuous Representations of Persistence Diagrams ｜持续球：持续图的双连续函数表示

作者：Matteo Pegoraro

论文原文见 [arXiv](https://arxiv.org/abs/2509.16999)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.16999)

> 持续图（Persistence Diagrams, PDs）作为拓扑数据分析的核心输出，其空间在 Wasserstein 距离下呈现高度非线性几何，导致均值计算等基础统计操作难以直接应用。现有向量化方法如持续图像（Persistence Images, PIs）和持续景观（Persistence Landscapes, PLs）虽能嵌入线性空间，但缺乏对 Wasserstein 几何的严格保真保证，且部分方法存在稳定性缺陷。本文提出持续球（Persistence Spheres, PSs），通过 Lift Zonoid 的支撑函数将 PDs 映射为球面标量场，实现了前向与逆向映射的双连续性。该表示在多个回归与分类基准上匹配或超越主流方法，但其逆映射的存在性依赖于权重函数的有效性条件，在极端稀疏图下的几何保真度仍需进一步验证。

## 研究背景

持续同调通过追踪数据在不同尺度下连通分量、环和空洞的出生与死亡，生成 PDs 以描述数据形状。然而，PDs 之间的比较通常依赖基于部分最优传输定义的 Wasserstein 距离，该距离赋予 PDs 空间非凸、非线性的几何结构。这种几何特性使得直接计算 PDs 的均值（即 Wasserstein 重心）计算密集且可能无唯一解，严重限制了标准统计工具在拓扑机器学习中的应用。

为克服这一局限，研究界发展了多种将 PDs 嵌入线性空间的向量化方法，包括基于描述统计、代数表示和函数表示的显式嵌入，以及利用核技巧的隐式特征映射。其中，函数表示通过为每个图关联定义域上的标量场来保持几何信息，但早期工作如 Gotovac Dogaš and Mandarić (2025) 采用的权重函数 $\omega(p) = y-x$ 不满足稳定性条件，导致映射在远离对角线时失效。本文旨在构建一种既具备 Lipschitz 稳定性又拥有连续逆映射的函数表示，以建立 Wasserstein 空间与线性函数空间之间最强的几何对应关系。

## 核心方法

### 方法参照系

PDs 向量化通常遵循“离散点集 $\rightarrow$ 线性空间向量/函数”的流程。主流方法如 PIs 通过高斯核平滑和像素化将 PDs 转为图像，PLs 通过分层函数提取多尺度特征。本文的关键差异在于不采用像素化或分层结构，而是利用凸分析工具，将 PDs 视为离散测度，通过 Lift Zonoid 构造凸集，再取其支撑函数作为表示，从而在理论上保证几何保真度。

### Lift Zonoid 与支撑函数构造

设计动机在于解决传统向量化方法中几何信息丢失的问题。给定 PD $\mu_D = \sum_{p \in D} c_p \delta_p$ 和权重函数 $\omega: \mathbb{R}^2 \rightarrow (0, 1]$，首先定义加权测度 $\mu_D^\omega = \sum_{p \in D} \omega(p) c_p \delta_p$。Lift Zonoid $Z_{\mu_D^\omega}$ 定义为：

$$
Z_{\mu_D^\omega} = \bigoplus_{p \in D} \omega(p) c_p [0, (1, p)]
$$

其中 $[0, (1, p)]$ 是原点与提升点 $(1, x, y)$ 之间的线段，$\oplus$ 表示 Minkowski 和。持续球 $\phi_{\mu_D}^\omega$ 定义为该凸集在单位球面 $S^2$ 上的支撑函数：

$$
\phi_{\mu_D}^\omega(u) = \sup_{v \in Z_{\mu_D^\omega}} \langle u, v \rangle, \quad u \in S^2
$$

这一构造利用了支撑函数的线性性质，将 PDs 的加法结构映射为函数的加法结构，使得相似图产生相似函数，且函数差异可反向推断图差异。

### 双连续性证明

设计动机在于确保表示的稳定性与可逆性，避免信息损失。本文证明，若权重函数 $\omega$ 满足稳定提升权重条件（即 $\Gamma_\omega(p) = \omega(p)(1, p)$ 是 Lipschitz 连续且满足特定衰减不等式），则映射 $\mu_D \mapsto \phi_{\mu_D}^\omega$ 关于 1-Wasserstein 距离是 Lipschitz 连续的。同时，若 $\omega$ 是有效权重（控制无穷远处行为），则逆映射在其定义域上是连续的。这一双连续性意味着 PSs 是 PDs Wasserstein 空间到函数空间的最优几何嵌入，因为已知不存在双 Lipschitz 嵌入（Carrière and Bauer, 2019）。

## 实验评估

实验涵盖 10 个数据集，包括函数数据（Tecator, NOx, Growth）、点云（Eyeglasses, DYN SYS）、图（ENZYMES JACC）、时间序列（POWER）和 3D 网格（SHREC14, Human Poses, McGill 3D Shapes）。基线包括 PIs、PLs 和切片 Wasserstein 核（SWK），模型采用 SVM 和惩罚线性/逻辑回归。PSs 在多数任务上表现最优，例如在 Tecator 回归任务中，PSs-Lin 达到 0.960，优于 PIs-Lin 的 0.922 和 PLs-Lin 的 0.837；在 Growth 分类任务中，PSs-Lin 准确率为 0.889，显著高于 PIs-Lin 的 0.536。

| 数据集 | 任务类型 | PSs-SVM | PSs-Lin | PIs-SVM | PIs-Lin | PLs-SVM | PLs-Lin | SWK |
|---|---|---|---|---|---|---|---|---|
| Tecator | 回归 | 0.962 (0.004) | 0.960 (0.007) | 0.928 (0.029) | 0.922 (0.018) | 0.939 (0.016) | 0.837 (0.048) | 0.953 (0.010) |
| Growth | 分类 | 0.871 (0.064) | 0.889 (0.045) | 0.525 (0.095) | 0.536 (0.086) | 0.782 (0.051) | 0.767 (0.107) | 0.768 (0.058) |
| NOx | 分类 | 0.877 (0.034) | 0.826 (0.035) | 0.803 (0.073) | 0.563 (0.102) | 0.794 (0.047) | 0.751 (0.040) | 0.840 (0.055) |
| SHREC14 | 分类 | 0.885 (0.057) | 0.926 (0.019) | 0.905 (0.029) | 0.897 (0.024) | 0.914 (0.021) | 0.931 (0.013) | 0.886 (0.092) |

PSs 在 McGill 3D Shapes 数据集上表现不佳，PIs-SVM 以 0.678 优于 PSs-SVM 的 0.383，这可能源于该数据集每类样本量有限导致的变异性。PSs 的计算复杂度线性依赖于点数和网格大小，可高效并行化，优于 PIs 的积分过程和 PLs 的 $O(n \log n + nN)$ 复杂度。

评估边界方面，实验未报告置信区间，仅给出 10 次运行的标准差；未对比基于深度学习的最新 TDA 集成方法；代码未公开，超参数选择依赖网格搜索，可复现性受限。

## 关联研究分析

从问题动机看，PSs 与 PIs 和 PLs 均旨在解决 PDs 非线性几何导致的统计工具受限问题，但 PSs 强调几何保真度而非计算便捷性。PIs 通过像素化牺牲了精确的 Wasserstein 距离保持，PLs 通过分层函数丢失了部分多尺度信息，而 PSs 通过 Lift Zonoid 构造保留了凸集结构，从而在理论上实现了双连续性。这一差异源于 PSs 对凸分析工具的深度利用，而非简单的核平滑或分层聚合。

从方法设计看，PSs 与 SWK 同属基于 Wasserstein 几何的方法，但 SWK 通过核技巧隐式定义特征映射，而 PSs 提供显式函数表示。SWK 在 SHREC14 上表现略优于 PSs-SVM，但 PSs-Lin 在多数任务上更优。PSs 的显式表示允许直接应用函数数据分析工具，如置信集和假设检验，而 SWK 仅支持核方法。这种差异表明，显式表示在需要复杂统计推断的场景中更具优势，而核方法在计算效率上可能更优。

## 总结

本文旨在解决 PDs Wasserstein 空间非线性几何导致统计工具应用受限的问题，通过 Lift Zonoid 支撑函数构造持续球，实现了前向与逆向映射的双连续性。实验表明，PSs 在 Tecator 回归任务中达到 0.960，在 Growth 分类任务中准确率为 0.889，匹配或超越 PIs、PLs 和 SWK。然而，PSs 在 McGill 3D Shapes 数据集上表现不佳，且逆映射的存在性依赖于权重函数的有效性条件，在极端稀疏图下的几何保真度未充分验证。当支持集增大到 5-shot 时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.16999)