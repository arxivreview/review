# ICLR2026最新论文 ｜Improving Set Function Approximation with Quasi-Arithmetic Neural Networks ｜准算术神经网络

研究机构：加拿大多伦多大学、加拿大向量研究所

作者：Tomas Tokar、Scott Sanner

论文原文见 [arXiv](https://arxiv.org/abs/2602.04941)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.04941)

> 集合函数近似面临的核心矛盾是：固定池化操作（如求和、最大）迫使编码器为特定聚合方式定制特征，导致表示缺乏通用性与迁移能力。现有可学习聚合方法（如HPDS）仅参数化幂平均指数，表达力受限，且未解决梯度传播中的维度坍缩问题。本文通过引入逆神经网络实现可学习的柯尔莫哥洛夫均值，将池化操作从固定算子升级为可训练的非线性变换，在理论上证明了对Wasserstein度量下连续函数的通用逼近性，并实证了编码器迁移性的显著提升。其价值在于解耦了编码器与聚合算子的绑定，但sum-decomposable函数的近似误差随集合大小线性增长的局限，限制了其在大规模计数任务中的适用性。

## 研究背景

处理无序集合数据时，模型必须满足置换不变性，即输出不随输入元素顺序改变。DeepSets（Zaheer et al., 2017）与PointNet（Qi et al., 2017a）确立了“编码器-池化-估计器”的Janossy池化框架，其中池化操作被固定为求和或最大。这种固定性将近似负担完全压给编码器，使其必须同时学习任务语义与适配特定池化算子的特征，限制了嵌入的通用性。

集合函数学习的主流路线分为Janossy池化与非Janossy方法。Janossy方法通过固定池化保证置换不变性，但表达力受限于池化算子的选择；非Janossy方法如Slot Attention（Locatello et al., 2020）通过注意力机制实现软聚合，但计算复杂度随集合大小平方增长，且缺乏对聚合算子数学性质的理论刻画。Kimura et al. (2024) 提出的HPDS通过引入可学习幂平均指数，首次尝试参数化池化操作，但仅覆盖了幂平均这一狭窄函数族，无法表达几何均值、调和均值等更广泛的中心趋势度量。本文的切入点在于：将池化操作推广为基于逆神经网络的柯尔莫哥洛夫均值，从而在保持置换不变性的同时，获得对任意连续生成函数的逼近能力。

## 核心方法

### Janossy池化框架与固定池化局限

Janossy池化将集合函数近似分解为编码器$\phi$、池化操作pool与估计器$\rho$的复合。标准形式为$\hat{F}(\mathbf{X}) = \rho(\text{pool}(\{\phi(\mathbf{x}_i)\}_{i=1}^n))$，其中pool为固定算子（如sum、max）。该框架的关键差异在于：pool不可训练，导致编码器$\phi$必须为特定pool定制特征，无法在下游任务中复用。本文问题与该通用流程的关键差异在于：将pool替换为可学习的逆神经网络，使聚合操作本身成为模型参数的一部分。

### 神经化柯尔莫哥洛夫均值（NKM）

设计动机：固定池化无法表达几何均值、中位数等非线性中心趋势，导致编码器被迫学习补偿性特征，降低迁移性。本文在Janossy框架的pool位置引入可学习生成函数$\psi$，实现神经化柯尔莫哥洛夫均值。NKM定义为：

$$
M_{\psi}(\mathbf{X}) = \psi^{-1}\left(\frac{1}{n}\sum_{i=1}^n \psi(\phi(\mathbf{x}_i))\right)
$$

其中$\psi$为逆神经网络（实验中使用RevNet）。该公式的物理含义是：先将每个元素嵌入$\phi(\mathbf{x}_i)$通过$\psi$映射到“均值空间”，在该空间执行线性平均，再通过$\psi^{-1}$映射回原始空间。由于$\psi$可学习，NKM能逼近任意连续生成函数对应的均值，突破了固定池化的表达瓶颈。

### QUANN架构与维度坍缩预防

设计动机：可学习池化可能引入梯度传播不稳定，导致编码器特征维度坍缩。QUANN-1采用NKM作为一元池化，QUANN-2将$\phi$扩展为二元注意力编码以捕获元素间交互。关键改进在于：$\psi$的逆函数性质保证了柯尔莫哥洛夫均值的导数非奇异。具体而言，$\partial M_{\psi,\phi}/\partial \phi(\pi)$ 的Jacobian矩阵在$\psi$局部单调时为正半定，确保反向传播中每个维度信息不被压缩至零。这一机制防止了维度坍缩，使编码器能学习更结构化的潜在表示，提升其在非集合任务中的迁移能力。

## 实验评估

实验在MNIST、Omniglot、ModelNet40与QM9四个基准上进行，基线覆盖DeepSets、PointNet、Normalized DeepSets、HPDS（Janossy路线）及SetTransformer、Slot Attention、FSPool、LAF（非Janossy路线）。遗漏了SetBERT等基于Transformer的最新集合模型，可能低估了QUANNs在大规模集合任务中的相对性能。

| 数据集 | 任务 | QUANN-1 | DeepSets | PointNet | HPDS | SetTransformer |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MNIST | mean (MSE↓) | **0.023** | 0.095 | 0.128 | 0.047 | 0.020 |
| MNIST | max (MSE↓) | **0.067** | 0.120 | 0.079 | 0.071 | 0.099 |
| Omniglot | n_max=10 (ACC↑) | **0.734** | 0.579 | 0.566 | 0.610 | 0.525 |
| QM9 | homo (MSE↓) | **160.345** | 179.423 | 153.419 | 212.237 | 165.998 |

QUANN-1在MNIST mean任务上MSE 0.023优于DeepSets 0.095，但在max任务上0.067略逊于PointNet 0.079；在Omniglot n_max=10上ACC 0.734显著优于SetTransformer 0.525。QM9 homo任务中QUANN-1 MSE 160.345优于DeepSets 179.423，但PointNet 153.419仍保持领先，表明QUANNs在分子属性预测中未全面超越经典架构。

消融实验显示，移除逆神经网络（Ablation 1）导致MNIST mean MSE从0.023升至0.099，验证了NKM的核心贡献。Ablation 2（匹配参数量但无逆函数）MSE 0.079，表明性能提升源于逆函数结构而非参数量。Ablation 3（移除归一化）MSE 0.027，接近QUANN-1，说明归一化对性能影响有限。反直觉发现：QUANNs在ModelNet40点云分类中被FSPool与PointNet超越，原因是点云几何特征依赖极值检测（max/min），而NKM作为均值型聚合对极值不敏感。

评估边界：论文未报告FLOPs与推理延迟，无法量化逆神经网络的计算开销；未提供代码与超参数细节，可复现性受限；QM9任务中PointNet仍领先，表明QUANNs在特定几何任务中并非最优。

## 关联研究分析

从问题动机看，QUANNs与HPDS（Kimura et al., 2024）均旨在解决固定池化的表达力局限，但HPDS仅参数化幂平均指数$w$，而QUANNs学习整个逆函数$\psi$。这一差异源于任务特性：HPDS假设目标函数属于幂平均族，而QUANNs假设目标函数可由任意连续生成函数逼近。当目标函数偏离幂平均族时，HPDS性能退化，而QUANNs保持鲁棒。论文未探索$\psi$的函数族限制，当生成函数高度非光滑时，RevNet的逼近能力是否仍足够，缺乏实证。

从方法设计看，QUANNs与Slot Attention（Locatello et al., 2020）均实现可学习聚合，但Slot Attention通过注意力权重实现软聚合，计算复杂度$O(n^2)$，而QUANNs通过逆函数实现硬聚合，复杂度$O(n)$。这一差异源于置换不变性的实现方式：Slot Attention依赖元素间交互，QUANNs依赖元素独立编码后的非线性聚合。当集合大小$n$超过1000时，Slot Attention的平方复杂度成为瓶颈，而QUANNs的线性复杂度更具扩展性。但QUANNs对sum-decomposable函数的近似误差随$n$线性增长，这一局限在Slot Attention中不存在，因为注意力机制可自适应调整元素权重。

## 总结

QUANNs解决的核心矛盾是固定池化对编码器表达的束缚，其切入点是引入逆神经网络实现可学习柯尔莫哥洛夫均值，在理论上证明了对Wasserstein度量下连续函数的通用逼近性，并实证了编码器迁移性的提升。MNIST mean任务MSE 0.023与Omniglot ACC 0.734验证了其在中心趋势聚合任务中的优势。但sum-decomposable函数的近似误差随集合大小线性增长，导致其在ModelNet40点云分类中被PointNet超越，暴露了均值型聚合对极值不敏感的局限。当目标函数同时依赖中心趋势与极值时，QUANNs的单一聚合机制是否足以兼顾两者，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.04941)