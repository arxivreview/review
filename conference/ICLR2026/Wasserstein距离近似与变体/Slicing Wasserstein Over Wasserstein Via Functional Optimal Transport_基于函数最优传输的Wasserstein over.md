# ICLR2026最新论文 ｜Slicing Wasserstein Over Wasserstein Via Functional Optimal Transport ｜基于函数最优传输的Wasserstein over Wasserstein切片度量

作者：Moritz Piening、Robert Beinert

论文原文见 [arXiv](https://arxiv.org/abs/2509.22138)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.22138)

> 本文旨在解决Wasserstein over Wasserstein（WoW）距离在比较分布的分布（meta-measures）时计算成本高昂且数值不稳定的问题。现有加速方案如s-OTDD依赖高阶矩，导致数值崩溃，而基于Busemann函数的方法依赖高斯近似，限制了通用性。本文切入点在于利用1D Wasserstein空间与$L_2([0,1])$函数空间的等距嵌入，将切片操作推广至无限维Banach空间，通过高斯过程参数化投影方向，定义了双重切片Wasserstein（DSW）度量。该框架在形状分类任务上实现了与Gromov-Wasserstein（GW）相当的精度，但计算速度提升数个数量级，其理论等价性在离散化场景下成立，但在高维连续空间的泛化边界尚待验证。

## 研究背景

当比较两个图像或点云分布时，直接计算像素或坐标间的欧氏距离往往忽略了几何结构的整体性，导致对微小扰动敏感。Wasserstein距离通过最优传输理论捕捉分布间的几何位移，但其精确求解涉及大规模线性规划，复杂度高达$O(n^3 \log n)$。当对象本身是概率分布（如数据集或形状库）时，问题升级为Wasserstein over Wasserstein（WoW）距离，即计算分布的分布之间的Wasserstein距离。此时，计算复杂度进一步恶化，因为需要反复评估底层分布间的Wasserstein距离，使得WoW在实际应用中几乎不可行。

主流加速路线分为两类：一是参数化方法，如针对高斯混合模型的切片加速，但缺乏通用性；二是基于矩或Busemann函数的方法。s-OTDD采用层级切片并依赖前几个矩，但高阶矩在数值上极不稳定，实际实现常限于前5个矩，导致精度损失。SWBDG/SWB1DG基于Busemann函数，其水平集作为仿射超平面的推广，但依赖高斯近似和闭式解，限制了其在一般Banach空间的应用。本文的切入点在于规避这些数值陷阱，利用1D Wasserstein空间与$L_2([0,1])$的等距嵌入，将切片操作推广至无限维Banach空间，从而定义一个可计算、数值稳定且与WoW拓扑等价的切片度量。

## 核心方法

### 无限维Banach空间的切片框架

标准切片Wasserstein距离（SWD）依赖欧氏空间中的均匀分布投影方向，但在无限维Banach空间$U$中，单位球面上不存在均匀概率测度。本文通过引入对偶空间$U^*$中的任意测度$\xi$，定义$\xi$-基于的切片Wasserstein距离：

$$
\text{SW}(\mu, \nu; \xi) = \left( \int_{U^*} W_1(\pi_v \sharp \mu, \pi_v \sharp \nu)^2 d\xi(v) \right)^{1/2}
$$

其中$\pi_v(u) = v(u)$为对偶配对。该设计动机在于解决无限维空间中投影方向采样的理论缺失问题。若$\xi$具有全支撑，该距离成为度量；若两个测度$\xi_1, \xi_2$相互绝对连续且Radon-Nikodym导数有界，则对应的SW距离度量等价。这为后续在函数空间上的切片提供了理论基础。

### 1D Wasserstein空间的量化切片

利用1D Wasserstein空间与$L_2([0,1])$的等距嵌入，将meta-measure $\boldsymbol{\mu} \in P_2(P_2(\mathbb{R}))$ 映射为量化函数空间中的测度$q \sharp \boldsymbol{\mu}$。本文定义切片量化WoW（SQW）距离：

$$
\text{SQW}(\boldsymbol{\mu}, \boldsymbol{\nu}; \xi) = \text{SW}(q \sharp \boldsymbol{\mu}, q \sharp \boldsymbol{\nu}; \xi)
$$

其中$\xi$为$L_2([0,1])$上的高斯测度，由协方差核$k_\sigma(t,s) = \exp(-|t-s|^2/2\sigma^2)$参数化的高斯过程$G$生成。该设计动机在于规避s-OTDD中高阶矩的数值不稳定，利用高斯过程的全支撑性确保SQW为度量，同时通过量化函数的闭式解（排序）实现高效计算。

### 双重切片Wasserstein（DSW）

对于多维meta-measures，直接切片Wasserstein空间缺乏Banach结构。本文提出双重切片策略：首先对底层域$\mathbb{R}^d$进行经典切片，将meta-measures映射为1D meta-measures序列；然后对每个1D meta-measure应用SQW距离。DSW定义为：

$$
\text{DSW}(\boldsymbol{\mu}, \boldsymbol{\nu}) = \left( \int_{S^{d-1}} \text{SQW}(\pi_\theta \sharp \boldsymbol{\mu}, \pi_\theta \sharp \boldsymbol{\nu}; \xi) d\theta \right)^{1/2}
$$

该设计动机在于解决多维Wasserstein空间缺乏量化映射的问题。通过层级切片，DSW避免了直接求解非凸优化，且证明了对于离散化meta-measures，DSW最小化等价于WoW最小化，提供了拓扑度量等价性保证。

## 实验评估

实验在2D Shapes、Animals、FAUST-500、FAUST-1000和MNIST-2000数据集上进行，评估KNN分类准确率与单次距离计算时间。基线包括TLB、STLB、AE和GW。SQW在FAUST-1000上准确率为42.7%±5.9，时间13.8ms±15.1ms；GW超时，STLB准确率39.4%±5.6，时间14.0ms±14.9ms。SQW在大规模数据上显著快于GW，精度略高于STLB。

| 方法 | FAUST-1000 Acc. (%) | FAUST-1000 Time (ms) | MNIST-2000 Acc. (%) | MNIST-2000 Time (ms) |
| :--- | :--- | :--- | :--- | :--- |
| SQW (Ours) | 42.7±5.9 | 13.8±15.1 | 84.8±4.7 | 48.6±2.8 |
| STLB | 39.4±5.6 | 14.0±14.9 | 84.1±5.0 | 45.1±2.8 |
| GW | 33.0±5.3 | 1048.2±357.3 | —timeout— | —timeout— |

消融实验显示，SQW与STLB在FAUST-1000上时间相近，但SQW准确率更高，表明量化切片比基于矩的切片更稳定。在MNIST-2000上，SQW准确率84.8%±4.7，STLB为84.1%±5.0，差异较小，但SQW时间略长，可能源于高斯过程采样的额外开销。

评估边界方面，实验仅覆盖离散化meta-measures，未验证连续空间下的理论等价性。代码已开源，但高斯过程核参数$\sigma$的敏感性未详细讨论。GW在FAUST-1000上超时，限制了大规模对比。

## 关联研究分析

从问题动机看，本文与s-OTDD同属WoW加速路线，但s-OTDD依赖高阶矩，导致数值不稳定，而本文利用量化函数的闭式解，规避了矩计算。这一差异源于任务特性：s-OTDD假设分布具有有限矩，而本文通过等距嵌入将问题转化为函数空间上的切片，适用于更广泛的分布类型。从方法设计看，本文与SWBDG/SWB1DG均基于Busemann函数或高斯过程，但SWBDG依赖高斯近似，而本文通过高斯过程参数化投影方向，提供了更通用的Banach空间切片框架。这一差异源于理论假设：SWBDG假设分布接近高斯，而本文仅要求全支撑性，适用于非高斯分布。

## 总结

本文要解决的核心矛盾是WoW距离计算的高成本与数值不稳定。现有方法如s-OTDD依赖高阶矩，导致数值崩溃，而SWBDG依赖高斯近似，限制了通用性。本文抓住1D Wasserstein空间与$L_2([0,1])$的等距嵌入，将切片操作推广至无限维Banach空间，通过高斯过程参数化投影方向，定义了DSW度量。实验证明，DSW在形状分类任务上实现了与GW相当的精度，但计算速度提升数个数量级，如FAUST-1000上SQW时间13.8ms，GW超时。本文的边界在于实验仅覆盖离散化meta-measures，未验证连续空间下的理论等价性，且高斯过程核参数的敏感性未详细讨论。当meta-measures的支撑集维度增加时，高斯过程采样的方差是否显著影响DSW的估计精度，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.22138)