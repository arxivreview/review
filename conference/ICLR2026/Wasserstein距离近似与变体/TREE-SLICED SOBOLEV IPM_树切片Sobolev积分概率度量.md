# ICLR2026最新论文 ｜TREE-SLICED SOBOLEV IPM ｜树切片Sobolev积分概率度量

研究机构：新加坡国立大学

作者：Viet-Hoang Tran、Thanh Q. Tran、Thanh Chu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_35515838)

> 现有树切片Wasserstein距离（TSW）受限于一阶度量，无法提供高阶优化所需的平滑梯度，阻碍了其在生成模型等梯度驱动任务中的应用。本文切入点在于利用正则化Sobolev积分概率度量（IPM）在树空间上的闭式解，构建支持任意阶 $p \ge 1$ 的树切片距离。通过随机树系统投影与Sobolev范数约束的结合，实现了计算复杂度与优化景观的平衡。该方法在多项基准上超越了现有切片变体，但其性能增益是否完全归因于高阶凸性，还是树结构本身的几何特性，尚存疑。

## 研究背景

当生成模型训练需要稳定的梯度信号时，一阶Wasserstein距离（$p=1$）的次可微性导致优化过程震荡。为克服此瓶颈，研究者转向高阶度量（$p>1$），因其具备严格凸性与更平滑的梯度。然而，精确计算高阶Wasserstein距离涉及昂贵的线性规划，且树切片Wasserstein距离（TSW）虽通过树空间投影获得了一阶闭式解，却缺乏 $p>1$ 时的解析表达，形成了“高效但低阶”与“高阶但低效”的矛盾。

切片Wasserstein距离（SWD）通过一维投影将复杂度降至 $O(n \log n)$，但一维切片难以捕捉高维数据的复杂几何结构。TSW通过引入树度量空间作为切片域，利用树上一阶Wasserstein的闭式解，在保持高效性的同时提升了结构表达能力。然而，TSW的闭式解仅适用于 $p=1$，限制了其在需要严格凸性的优化场景中的适用性。Le et al. (2025) 提出的正则化Sobolev IPM在树上具有任意 $p \ge 1$ 的闭式解，为突破TSW的阶数限制提供了数学基础。本文旨在将这一闭式解嵌入树切片框架，构建兼具高效性与高阶优化优势的度量。

## 核心方法

### 树切片框架与Sobolev IPM基础

本文方法建立在两个核心组件之上：树系统（Tree Systems）投影框架与正则化Sobolev IPM。树系统将欧氏空间 $\mathbb{R}^d$ 中的测度投影至连续树度量空间，利用树的一阶Wasserstein闭式解实现高效计算。正则化Sobolev IPM则通过约束批评函数于Sobolev范数单位球内，定义测度间的距离，其在树上具有任意 $p \ge 1$ 的闭式解。本文的关键差异在于，不再使用一阶Wasserstein作为切片内的距离核，而是替换为正则化Sobolev IPM，从而继承其高阶优化特性。

### TS-Sobolev距离定义

TS-Sobolev距离通过随机采样树系统，计算投影后测度在树上的正则化Sobolev IPM并取期望。对于两个测度 $\mu, \nu \in \mathcal{P}(\mathbb{R}^d)$，TS-Sobolev距离定义为：

$$
D_{TS-Sobolev}^p(\mu, \nu) = \mathbb{E}_{T \sim \sigma} \left[ \sup_{f \in B(p')} \left| \int f d\mu_T - \int f d\nu_T \right| \right]
$$

其中 $T$ 为随机树系统，$\mu_T, \nu_T$ 为投影后的测度，$B(p')$ 为Sobolev范数单位球。该公式的物理含义是：在随机生成的树结构上，寻找能最大程度区分两个投影测度的Sobolev约束函数，并平均所有树结构上的区分度。这一设计解决了TSW仅限 $p=1$ 的失效，使得 $p>1$ 时的梯度随误差幅度缩放，而非恒定，从而提供更平滑的优化路径。

### 球面扩展与优化优势

为处理非欧氏数据，本文定义了球面树切片Sobolev IPM（STS-Sobolev），将树系统投影至球面 $S^{d-1}$。其优化优势体现在两方面：一是 $p>1$ 带来的严格凸性，确保梯度流收敛稳定；二是权重函数 $\hat{w}(x) = 1 + \omega(\Lambda(x))$ 对根节点附近的全局梯度进行降权，使优化聚焦于叶节点的局部精细结构。这一机制在标准 $p$-Wasserstein中不存在，是TS-Sobolev独有的几何感知优化特性。

## 实验评估

实验在8 Gaussians、Gaussian 30d、CIFAR-10、BBC/M10等基准上进行，基线覆盖SW、TSW、Db-TSW及球面切片方法，但缺失神经嵌入类基线（如Wormhole）。在8 Gaussians梯度流任务中，TS-Sobolev1.2最终距离为 $8.88 \times 10^{-7}$，优于Db-TSW的 $2.50 \times 10^{-6}$；在CIFAR-10 DDGAN训练中，TS-Sobolev2-DD的FID为2.277，优于Db-TSW-DD⊥的2.530。

| 方法 | 8 Gaussians (2500 iter) | Gaussian 30d (2500 iter) | CIFAR-10 FID |
| :--- | :--- | :--- | :--- |
| Db-TSW | 2.50e-6 | 1.78 | 2.530 |
| TS-Sobolev1.2 | 8.88e-7 | 1.40 | — |
| TS-Sobolev2 | 3.50e-6 | 1.51 | 2.277 |

消融实验显示，$p$ 值从1.2增至2时，8 Gaussians最终距离从 $8.88 \times 10^{-7}$ 增至 $3.50 \times 10^{-6}$，表明高阶并非单调收益，存在最优 $p$ 区间。球面SSL任务中，STS-Sobolev2准确率为80.6%，略优于STSW的80.53%，提升幅度有限，暗示球面几何中高阶凸性的增益可能被树结构本身主导。

评估边界方面，论文未报告训练时间与内存开销，仅提及“可比”；超参数（如树系统数量、Sobolev正则化系数）未在正文详述，可复现性依赖附录。代码已开源，但缺乏对树系统采样分布 $\sigma$ 敏感性的分析，该选择可能影响 $p>1$ 时的收敛稳定性。

## 关联研究分析

从问题动机看，TS-Sobolev与Db-TSW（Tran et al., 2025a）同属树切片路线，但Db-TSW聚焦于动态支持测度下的距离定义，而TS-Sobolev聚焦于优化景观的平滑性。Db-TSW通过距离矩阵不变量提升结构捕捉能力，TS-Sobolev则通过Sobolev范数约束提升梯度质量。二者差异根源在于任务特性：Db-TSW适用于结构对齐，TS-Sobolev适用于梯度驱动优化。若数据分布高度多模态，Db-TSW的结构优势可能超过TS-Sobolev的优化优势，论文未对此进行对比。

从方法设计看，TS-Sobolev与Le et al. (2025)的正则化Sobolev IPM共享闭式解基础，但后者仅适用于静态树测度，前者通过树系统投影扩展至欧氏/球面动态测度。这一扩展的关键在于分裂映射（Splitting Maps）的设计，其将欧氏点分配至树的不同分支。与标准SWD相比，TS-Sobolev的投影域从一维直线变为树结构，增加了几何复杂度，但闭式解的存在抵消了计算开销。树系统采样分布 $\sigma$ 的选择是否影响 $p>1$ 时的收敛稳定性，论文未给出回答。

## 总结

本文核心矛盾是树切片距离的高效性与高阶优化需求之间的冲突。TSW因缺乏 $p>1$ 闭式解而受限，Le et al. (2025) 的正则化Sobolev IPM提供了数学工具，但仅适用于静态树测度。本文通过将Sobolev IPM嵌入树切片框架，构建了支持任意 $p \ge 1$ 的TS-Sobolev距离，在8 Gaussians上实现 $8.88 \times 10^{-7}$ 的最终距离，在CIFAR-10上取得2.277的FID。其边界在于球面任务中增益有限，且未分析树系统采样分布对高阶收敛的影响。当树系统数量从100增至1000时，TS-Sobolev的FID是否进一步下降，论文未提供数据。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_35515838)