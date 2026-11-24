# ICLR2026最新论文 ｜Fast Estimation of Wasserstein Distances via Regression on Sliced Wasserstein Distances ｜基于切片距离回归的 Wasserstein 距离快速估计

研究机构：美国德克萨斯大学奥斯汀分校

作者：Khai Nguyen、Hai Nguyen、Nhat Ho

论文原文见 [arXiv](https://arxiv.org/abs/2509.20508)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.20508)

> 高维 Wasserstein 距离 (WD) 的精确求解受限于 $O(n^3 \log n)$ 的线性规划复杂度，阻碍了其在大规模分布对比较中的应用。现有神经嵌入方法虽能加速，但依赖大量训练数据且仅限经验分布。本文提出一种无神经网络的线性回归框架，将多种切片 Wasserstein 距离 (SWD) 变体作为预测变量，通过最小二乘法拟合真实 WD。该方法在低数据量场景下显著优于 SOTA 神经嵌入模型，并成功加速了 Wormhole 的训练过程，但其线性假设在高维复杂几何下的泛化能力尚存疑。

## 研究背景

当生成模型或生物信息学任务需要反复计算成千上万对概率分布间的差异时，精确求解 Wasserstein 距离 (WD) 成为计算瓶颈。WD 定义为传输计划上的期望距离平方最小值，其离散形式需求解大规模线性规划，时间复杂度高达 $O(n^3 \log n)$。为突破此瓶颈，切片 Wasserstein 距离 (SWD) 利用 Radon 变换将高维投影至一维，借助一维分位数函数的闭式解将复杂度降至 $O(n log n)$，确立了“投影-计算-聚合”的标准范式。然而，标准 SWD 仅是 WD 的下界，且随机投影在低预算下方差较大，导致估计不稳定。

主流加速路线分为两类：一是直接优化计算，如 Sinkhorn 迭代或低秩近似，但前者引入正则化偏差，后者依赖特定结构；二是学习嵌入，如 Deep Wasserstein Embedding (DWE) 和 Wasserstein Wormhole，通过神经网络学习低维表示以近似 WD。这些神经方法虽有效，但训练资源消耗巨大，且在训练数据有限时性能显著退化，且受限于经验分布。本文切入点在于：既然 SWD 及其变体（如 Max-SW, EBSW, Projected Wasserstein）分别提供了 WD 的下界与上界，且计算廉价，能否通过一个简单的线性模型，从这些廉价特征中“回归”出昂贵的真实 WD，从而在低数据量下实现高效且稳健的估计？

## 核心方法

### 切片距离变体作为预测特征

本文的方法参照系是标准的 SWD 估计流程，即通过随机投影方向 $\theta \sim U(S_{d-1})$ 计算一维距离并取平均。关键差异在于，本文不直接平均，而是计算多种具有不同统计性质的 SW 变体作为特征向量。具体而言，利用随机投影 $P_\theta(x) = \langle \theta, x \rangle$，定义一维投影距离 $W_p(\mu, \nu; P_\theta)$ 为下界，以及基于提升传输计划的 lifted cost $W_p(\mu, \nu; P_\theta)$ 为上界。通过改变切片分布 $\sigma$，本文构建了六个预测变量：标准 SW、Max-SW、Energy-based SW (EBSW) 作为下界族；Projected Wasserstein (PW)、Min-SWGG、Expected Sliced Transport (EST) 作为上界族。这些变体在计算上均保持 $O(n \log n)$ 复杂度，但提供了关于真实 WD 的不同信息维度。

### 线性回归框架与约束优化

设计动机在于利用上下界夹逼特性，在固定投影预算下最小化估计误差，避免单一随机投影的方差波动。本文提出线性回归模型，以 WD 为响应变量，SW 变体为预测变量：

$$
W_p(\mu, \nu) = \omega^\top \mathbf{S}(\mu, \nu) + \epsilon
$$

其中 $\mathbf{S}(\mu, \nu)$ 是由 $K$ 个 SW 变体组成的向量，$\omega$ 为权重向量，$\epsilon$ 为噪声。为求解 $\omega$，本文采用最小二乘法，其闭式解为：

$$
\hat{\omega}_{LSE} = (\hat{\mathbf{S}}^\top \hat{\mathbf{S}})^{-1} \hat{\mathbf{S}}^\top \hat{\mathbf{W}}
$$

其中 $\hat{\mathbf{S}} \in \mathbb{R}^{M \times K}$ 为 $M$ 个分布对的 SW 特征矩阵，$\hat{\mathbf{W}} \in \mathbb{R}^{M}$ 为对应的精确 WD 向量。此外，本文引入约束模型，利用 SW 下界与上界的关系，强制权重满足 $0 \le \omega_1 \le 1$ 且 $\omega_2 = 1 - \omega_1$（针对上下界组合），从而将参数量减半，增强了模型的几何解释性与数值稳定性。

## 实验评估

实验在 MNIST 点云、ShapeNetV2、MERFISH 细胞巢穴及 scRNA-seq 数据集上进行，主要对比基线为 Wasserstein Wormhole（SOTA 神经嵌入）及精确 WD。本文未对比 ReSWD 或 Adaptive Bayesian SWD 等最新方差缩减方法，基线覆盖侧重于神经嵌入路线。

| 方法 | MNIST (100 samples) MAE | ShapeNetV2 (100 samples) MAE | MERFISH (100 samples) MAE | scRNA-seq (100 samples) MAE |
| :--- | :--- | :--- | :--- | :--- |
| Wormhole | 5.1e-1 | 1.8e-1 | 2.1e-2 | 7.8e-2 |
| RG-seo (unconstr.) | 1.5e-1 | 7.8e-2 | 1.0e-3 | 2.0e-3 |
| RG-seo (constr.) | 2.3e-1 | 1.0e-1 | 3.0e-3 | 2.0e-3 |

在低数据量（100 样本）设定下，本文方法在 MAE 指标上全面优于 Wormhole。例如，在 MNIST 上，RG-seo (unconstr.) 的 MAE 为 1.5e-1，而 Wormhole 为 5.1e-1；在 scRNA-seq 高维数据上，RG-seo (unconstr.) 的 MAE 低至 2.0e-3，显著低于 Wormhole 的 7.8e-2。这表明线性回归框架在数据稀缺时具有更强的泛化能力，而神经嵌入方法因过拟合风险导致性能退化。

消融实验显示，无约束模型 (unconstr.) 在多数数据集上略优于有约束模型 (constr.)，例如在 ShapeNetV2 上，RG-seo (unconstr.) 的 MAE 为 7.8e-2，而 RG-seo (constr.) 为 1.0e-1。然而，在 MERFISH 数据集上，两者性能接近（1.0e-3 vs 3.0e-3），表明约束条件在特定几何结构下可能引入轻微偏差。此外，RG-o（仅使用 Max-SW 和 Min-SWGG）的性能显著低于 RG-seo（使用全部六个变体），证明多源信息融合对提升估计精度至关重要。

评估边界方面，本文主要关注低数据量场景，未报告数据量充足（>1000 样本）时的性能对比，无法判断线性模型在大数据下的相对优势。代码已开源，但论文未详细披露超参数搜索过程及 GPU 资源消耗，可复现性依赖于默认配置。

## 关联研究分析

从问题动机看，本文与 ReSWD (Boss et al., 2025) 同属方差缩减路线，但路径截然不同。ReSWD 通过水库采样优化投影方向的选择，旨在降低单一 SW 估计的方差；而本文不改变投影策略，而是将多种 SW 变体作为特征，通过线性组合来逼近 WD。ReSWD 假设 WD 与 SW 存在单调关系，而本文假设存在线性可加性。这种差异源于任务特性：ReSWD 针对的是单一距离估计的稳定性，本文针对的是多对分布比较的效率与低数据泛化。若数据量充足，ReSWD 的自适应采样可能比线性回归更精确，但本文在低数据下的优势是否源于线性模型的低方差特性，而非采样策略，论文未给出直接对比。

从方法设计看，本文与 Wasserstein Wormhole (Haviv et al., 2024) 形成互补。Wormhole 使用 Transformer 学习非线性嵌入，其核心假设是 WD 可由低维欧氏距离近似；本文则假设 WD 可由 SW 变体的线性组合近似。Wormhole 的优势在于捕捉复杂非线性几何，但代价是高训练成本与数据依赖；本文的优势在于轻量级与低数据鲁棒性。两者在 RG-Wormhole 中结合，用线性回归替代 Wormhole 训练中的精确 WD 计算，证明了线性近似在作为训练信号时的有效性。然而，线性模型是否破坏了 WD 的度量公理（如三角不等式），论文未进行理论验证，这可能影响其在需要严格度量性质的下游任务中的应用。

## 总结

本文旨在解决高维 Wasserstein 距离计算昂贵且神经嵌入方法在低数据下失效的矛盾。其切入点在于利用切片距离变体的上下界特性，通过线性回归实现“以快换准”。方法上，构建了基于 SW、Max-SW、EBSW 等六种变体的线性模型，并通过最小二乘法求解权重。实验证明，在 100 样本的低数据量下，本文方法在 MNIST 上的 MAE 为 1.5e-1，显著优于 Wormhole 的 5.1e-1。本文的边界在于线性假设可能无法捕捉高维分布间的复杂非线性几何，且未验证在数据充足时的相对性能。当支持集规模从 100 增至 1000 时，线性回归的边际收益是否递减，以及其估计值是否仍满足度量公理，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.20508)