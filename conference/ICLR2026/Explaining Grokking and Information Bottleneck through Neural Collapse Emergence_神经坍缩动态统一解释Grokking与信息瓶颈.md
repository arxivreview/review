# ICLR2026最新论文 ｜Explaining Grokking and Information Bottleneck through Neural Collapse Emergence ｜神经坍缩动态统一解释Grokking与信息瓶颈

研究机构：日本东京大学

作者：Keitaro Sakamoto、Issei Sato

论文原文见 [arXiv](https://arxiv.org/abs/2509.20829)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.20829)

> 过参数化网络在训练后期常出现Grokking（测试性能在训练损失平台期后突然提升）与信息瓶颈（IB）压缩（丢弃无关输入信息）现象，但二者机制及关联长期缺乏统一解释。现有理论多孤立分析参数压缩或复杂度指标，未能揭示表示空间几何结构在时间维度上的演化规律。本文通过推导类内方差收缩与泛化误差、冗余信息的显式上界，证明神经坍缩（Neural Collapse, NC）动态是驱动这两种后期现象的共同几何机制。该框架提供了定量时间尺度分析，但实验验证局限于MLP架构，缺乏与SOTA Grokking加速方法的直接数值竞争。

## 研究背景

理解本文需把握三个概念的因果链：过参数化网络在训练初期往往完美拟合训练集但泛化失败，这一记忆状态由表示空间中类内方差（Within-class Variance）较大导致，即同类样本特征分散，难以线性分离。当训练继续，若类内方差收缩，特征聚类变紧，泛化能力随之涌现，这一几何过程称为神经坍缩。然而，类内方差收缩的时间尺度与训练损失收敛的时间尺度是否同步，决定了泛化是否延迟发生，这正是Grokking现象的核心机制。

Grokking与IB动态均属于训练后期现象，但现有解释路线存在瓶颈。Grokking研究多聚焦参数压缩（Liu et al., 2023a）或复杂度度量（Nanda et al., 2023），IB研究则依赖互信息（MI）估计（Shwartz-Ziv & Tishby, 2017），但MI在确定性网络中可能无穷大，且未反映网络参数动态。Jacot et al. (2025) 建立了权重正则化下NC收敛的理论基础，但未将其与泛化误差或IB压缩阶段显式关联。本文切入点在于：将类内方差作为统一度量，通过推导其与泛化误差、冗余信息的关系，并分析其在梯度下降下的时间尺度，从而桥接几何动态与信息论/泛化理论。

## 核心方法

### 方法参照系

本文问题属于“Grokking机制解析”路线，但区别于参数压缩或复杂度视角，聚焦表示空间几何。标准流程是分析训练损失收敛与测试误差的关系，本文差异在于引入类内方差作为中间变量，建立“几何收缩→泛化提升”的因果链，并量化其时间滞后性。

### 类内方差作为泛化与压缩的统一度量

设计动机：现有Grokking解释未区分“拟合训练集”与“泛化”的几何条件，IB解释缺乏对压缩阶段的定量刻画。本文定义尺度不变的总体类内方差（Population Within-class Variance）：

$$
\mathbb{E}_{Y} \left[ \frac{1}{B_g^2} \mathbb{E}_{X|Y} \left[ \| \tilde{g}(X) - \mathbb{E}_{X|Y}[\tilde{g}(X)] \|^2_2 \right] \right]
$$

其中 $\tilde{g}(X) = g(X)/B_g$ 为归一化特征，$B_g = \sup_{x \in \mathcal{X}} \|g(x)\|_2$ 为输出尺度。该公式物理含义是：在消除输出尺度影响后，同类样本特征围绕类均值的平均平方距离。Theorem 3.2 证明泛化误差上界由该方差与类均值-分类器对齐度共同决定；Theorem 3.4 证明IB压缩阶段丢弃的冗余信息（$I(Z;X) - I(Z;Y)$）被该方差上界控制。这解决了此前方法中“几何收缩”与“泛化/压缩”之间缺乏定量联系的问题，使得类内方差成为可测量的统一指标。

### 神经坍缩动态的时间尺度分离

设计动机：Theorem 3.2/3.4 表明类内方差收缩有益，但未解释为何收缩滞后于训练损失收敛，导致Grokking的“延迟”特性。本文基于Jacot et al. (2025) 的权重正则化动力学，推导重缩放NC1（RNC1）与训练损失的时间尺度关系：

$$
\tau_1 = O\left(\frac{1}{\eta} \log \frac{1}{\epsilon_1}\right), \quad \tau_2 = O\left(\frac{1}{\eta \lambda} \log \frac{1}{\epsilon_2}\right)
$$

其中 $\tau_1$ 为训练损失收敛至 $\epsilon_1$ 的时间，$\tau_2$ 为RNC1收敛至 $\epsilon_2$ 的时间，$\eta$ 为学习率，$\lambda$ 为权重衰减。该公式揭示：训练损失收敛时间 $\tau_1$ 与 $\lambda$ 无关，而RNC1收敛时间 $\tau_2$ 与 $\lambda$ 成反比。当 $\lambda$ 较小时，$\tau_2 \gg \tau_1$，即神经坍缩显著滞后于拟合，这正是Grokking中“先记忆后泛化”的几何根源。此结果将Grokking的延迟从经验现象转化为可预测的时间尺度函数，并解释了IB压缩阶段为何发生在训练后期。

## 实验评估

实验在MNIST、CIFAR-10和Modular Arithmetic上验证理论，使用4层MLP（[784, 200, 200, 200, 10]，ReLU激活）。基线审计：对比不同权重衰减系数 $\lambda$ 下的RNC1、测试准确率、互信息动态，但未对比Liu et al. (2023a) 的参数压缩方法或Nanda et al. (2023) 的复杂度度量方法，缺乏与SOTA Grokking加速策略的直接竞争。该论文实验数据不可得，未提供实验表格。

消融聚焦权重衰减 $\lambda$ 对时间尺度的影响。当 $\lambda$ 减小时，RNC1收敛时间 $\tau_2$ 显著延长，测试准确率提升滞后于训练损失平台期，符合Theorem 4.3 预测。反直觉发现：在Modular Arithmetic任务中，即使训练损失已收敛，RNC1仍持续下降，且下降速率与 $\lambda$ 成反比，验证了时间尺度分离机制。边际收益：增大 $\lambda$ 可加速NC涌现，但可能损害拟合精度，存在权衡。

评估边界：指标完备性方面，RNC1作为代理指标在非线性深层网络中的普适性未验证；评估协议局限在于仅使用MLP架构，未测试Transformer或ResNet；可复现性方面，代码已开源（https://github.com/keitaroskmt/collapse-dynamics），但超参数细节（如 $\epsilon_1, \epsilon_2$ 具体值）未在正文中完整列出。

## 关联研究分析

从问题动机看，本文与Liu et al. (2022b) 的表示学习视角Grokking解释同源，但差异在于：Liu et al. 强调“结构化表示”的涌现，未量化其时间尺度；本文通过RNC1提供可测量的几何指标，并证明其收敛时间由 $\lambda$ 控制。根源在于Liu et al. 聚焦静态表示性质，而本文关注动态训练过程，这决定了后者能解释“延迟”现象，前者不能。

从方法设计看，本文与Shwartz-Ziv & Tishby (2017) 的IB框架同属信息论视角，但差异在于：Shwartz-Ziv 将压缩阶段归因于SGD的扩散分量，缺乏几何解释；本文将压缩阶段量化为类内方差收缩，建立几何-信息论桥接。根源在于Shwartz-Ziv 依赖MI估计，而MI在确定性网络中定义困难，本文通过添加小高斯噪声 $E \sim \mathcal{N}(0, \sigma^2 I)$ 使MI良定义，但引入了噪声参数 $\sigma$ 的敏感性，论文未讨论 $\sigma$ 对结论的影响。

## 总结

本文要解决的核心矛盾是Grokking与IB动态机制的孤立性与缺乏统一几何解释。现有方法做不到是因为参数压缩或复杂度指标未捕捉表示空间几何的时间演化，本文凭类内方差作为统一度量，并基于Jacot et al. (2025) 的动力学结果，推导出RNC1收敛时间与权重衰减 $\lambda$ 的反比关系。本文证明了当 $\lambda$ 较小时，$\tau_2 \gg \tau_1$，即神经坍缩滞后于拟合，解释了Grokking的延迟特性。边界在于实验仅验证MLP架构，且未对比SOTA Grokking加速方法，RNC1在Transformer等复杂架构中的有效性未知。当支持集增大或架构变为深层残差网络时，类内方差收缩是否仍由 $\lambda$ 主导时间尺度，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.20829)