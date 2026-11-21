# CVPR2026最新论文 ｜Hyperbolic Busemann Neural Networks ｜基于Busemann函数的双曲神经网络组件

作者：Ziheng Chen、Bernhard Schölkopf、Nicu Sebe

论文原文见 [arXiv](https://arxiv.org/abs/2602.18858)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.18858)

> 双曲度量学习旨在利用恒定负曲率黎曼流形的指数体积增长特性，以更低失真编码层级与树状结构。现有双曲神经网络组件在追求几何内在性时，往往陷入参数冗余或依赖切空间近似导致的几何失真，且计算效率低下。本文切入点在于利用Busemann函数（Busemann Function）作为内积在流形上的内在推广，重构多分类逻辑回归（Multinomial Logistic Regression, MLR）与全连接层（Fully Connected, FC）。通过构建BMLR与BFC层，本文在保持几何一致性的同时实现了批处理高效计算，验证了其在图像分类与图学习任务中的有效性，但固定曲率假设限制了其在非均匀层级结构中的泛化能力。

## 研究背景

双曲空间中的测地线射线在无穷远处保持有界分离，这一性质使得Busemann函数能够作为欧氏内积在流形上的自然推广。Busemann函数的水平集称为等距球面（Horosphere），其几何性质与欧氏超平面高度对应，为构建双曲分类器提供了内在的度量基础。然而，早期双曲MLR方法依赖切空间映射或环境空间投影，导致几何失真或参数冗余，难以在保持内在性的同时实现高效计算。

双曲神经网络架构的演进始于对数值稳定性的追求，早期基于Poincaré球的双曲线性层受限于边界处的梯度爆炸，难以训练深层网络。随后，研究者转向Lorentz模型以利用Minkowski空间的数值稳定性，但现有双曲FC层多依赖切空间或环境空间线性变换，未能完全尊重内在双曲几何。本文的切入点在于直接利用Busemann函数定义内在logits，消除流形值参数，从而在Poincaré与Lorentz模型上实现统一且高效的MLR与FC层构造。

## 核心方法

### 方法参照系

双曲MLR与FC层通常通过将欧氏线性变换映射到切空间或环境空间实现，如Möbius矩阵乘法或Lorentz FC。本文问题与该通用流程的关键差异在于，本文不依赖切空间近似，而是直接利用Busemann函数在双曲空间内定义内在logits，避免映射失真。

### BMLR：基于Busemann函数的内在分类器

传统双曲MLR如Poincaré MLR依赖切空间参数，导致过参数化且缺乏批处理效率。本文设计动机在于消除流形值参数，利用Busemann函数的内在性直接定义logits。BMLR的logit定义为：

$$ u_k(x) = -\alpha_k B_{v_k}(x) + b_k $$

其中 $\alpha_k > 0$ 为幅度，$v_k \in S^{n-1}$ 为单位方向，$b_k \in \mathbb{R}$ 为偏置。该公式的物理含义是，每个类别的logit由点到等距球面的距离决定，$B_{v_k}(x)$ 提供了内在的点到超平面距离解释。这一设计消除了流形值参数，实现了紧凑参数化，并在曲率 $K \to 0^-$ 时恢复欧氏MLR，解决了此前方法在参数冗余与几何失真上的失效。

### BFC：内在双曲全连接层

BMLR提供了分类头的内在构造，但特征变换层（FC层）仍需内在化。传统Lorentz FC依赖环境空间线性变换后投影，可能扭曲内在几何。本文设计动机在于通过Busemann函数统一FC与激活层的构造，保持内在性。BFC层通过求解以下方程组确定输出 $y$：

$$ d(\bar{y}, H_{e_k, e}) = \phi(-\alpha_k B_{v_k}(x) + b_k) $$

其中 $d(\bar{y}, H_{e_k, e})$ 为点到过原点超平面的有符号距离，$\phi$ 为激活函数。该公式的算法含义是，输出空间的每个坐标由输入点到对应等距球面的距离经激活函数映射得到。这一构造在Poincaré与Lorentz模型上均有效，保持了 $O(nm)$ 复杂度，解决了此前FC层依赖切空间或环境空间近似导致的几何失真问题。

## 实验评估

实验在图像分类（CIFAR-10/100, Tiny-ImageNet, ImageNet-1k）、基因组序列学习（TEB, GUE）、节点分类（HGCN骨干）与链接预测（Disease, Airport, PubMed, Cora）上进行。基线覆盖Poincaré MLR、Lorentz MLR、Möbius FC、Poincaré FC等经典方法，但缺失混合曲率或自适应曲率基线。

| 数据集 | 方法 | 准确率/MAP |
|---|---|---|
| CIFAR-10 | BMLR-P | 95.32 ± 0.14 |
| CIFAR-10 | BMLR-L | 95.25 ± 0.02 |
| Disease | BFC-L | 78.36 ± 0.51 |
| Airport | BFC-L | 95.37 ± 0.17 |

BMLR-L在CIFAR-10上达到95.25 ± 0.02，优于Lorentz MLR的94.98 ± 0.12；BFC-L在Disease链接预测中取得78.36 ± 0.51 MAP，显著优于Lorentz FC的72.78 ± 2.04。

消融实验显示，BMLR在类别数增加时性能增益更显著，如ImageNet-1k上BMLR-L达到73.24，优于Lorentz MLR的72.46。BFC层在链接预测中一致优于Möbius与Lorentz FC，表明内在构造对层级结构捕获的有效性。

评估边界方面，论文未报告计算效率的绝对数值，仅指出BMLR-L为最快双曲MLR；代码已开源，但超参数细节未完全披露，可复现性依赖官方实现。

## 关联研究分析

从方法设计看，本文与Shimizu et al. (2021)的Poincaré FC层同属内在构造路线，但本文通过Busemann函数统一了MLR与FC层，而Shimizu et al.仅处理FC层且限于Poincaré模型。差异根源在于任务特性：Busemann函数的内在性更适合多分类与特征变换的统一框架，而切空间方法在单一模型上更简洁。

从问题动机看，本文与Chen et al. (2026)的Lorentz FC层同属Lorentz模型优化，但本文强调几何内在性，而Chen et al.依赖环境空间投影。本文的BFC层通过内在距离定义避免了投影失真，但固定曲率假设限制了其在非均匀层级结构中的适用性，查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

本文要解决的核心矛盾是双曲神经网络组件在几何内在性与计算效率之间的权衡。现有方法依赖切空间或环境空间近似，导致几何失真或参数冗余，而本文利用Busemann函数的内在性直接定义logits，实现了紧凑参数化与批处理高效计算。BMLR与BFC层在图像分类与图学习任务中验证了有效性，BMLR-L在CIFAR-10上达到95.25 ± 0.02，BFC-L在Disease链接预测中取得78.36 ± 0.51 MAP。本文的边界在于固定曲率假设，未探索自适应曲率学习，当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.18858)