# ICLR2026最新论文 ｜CONDITIONED INITIALIZATION FOR ATTENTION ｜条件数驱动的注意力初始化

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_45899240)

> 本文旨在解决Transformer训练初期注意力层Jacobian条件数过高导致的优化不稳定问题。现有初始化方法如Xavier或Mimetic Initialization缺乏对注意力矩阵谱结构的理论约束，导致收敛速度受限且泛化能力波动。本文提出Conditioned Initialization，通过特定谱结构初始化Query、Key、Value矩阵以降低Jacobian条件数上界。该方法在多种架构上加速收敛并提升精度，但其理论保证仅限于上界收紧，未直接证明对最终泛化误差的因果影响。

## 研究背景

Transformer自注意力机制通过Query ($W_Q$)、Key ($W_K$) 和Value ($W_V$) 矩阵的投影交互建模Token间依赖。这些投影矩阵的谱性质直接决定了注意力输出对参数扰动的敏感度，即Jacobian矩阵的条件数 $\kappa(J)$。条件数越大，梯度更新方向越不稳定，优化过程易陷入病态区域。传统初始化方案如Xavier或Kaiming仅关注权重方差保持，未考虑 $W_Q, W_K, W_V$ 在注意力公式中的代数角色差异，导致初始Jacobian条件数往往较高。

主流初始化路线分为两类：一类是随机初始化，如截断正态分布，简单但缺乏结构约束；另一类是启发式方法，如Mimetic Initialization（Trockman & Kolter, 2023）通过模仿收敛模型的统计模式引入归纳偏置，Weight Selection（Xu et al., 2023）则复用教师模型权重。这些方法虽能改善性能，但缺乏对注意力机制内部条件数的理论解释，无法保证优化轨迹的稳定性。本文切入点在于建立Jacobian条件数与 $W_Q, W_K, W_V$ 谱性质的数学联系，从而设计一种从源头控制优化稳定性的初始化策略。

## 核心方法

### 方法参照系

本文问题属于深度网络初始化策略范畴，但区别于通用的方差保持初始化，其核心差异在于针对自注意力层的Jacobian条件数进行显式优化。通用流程关注层间信号传播，而本文聚焦于单层注意力内部参数对输出的敏感度控制。

### Jacobian条件数上界推导

设计动机在于揭示 $W_Q, W_K, W_V$ 的谱结构如何决定优化稳定性。本文证明自注意力层 $A(X)$ 关于 $W_Q, W_K, W_V$ 的Jacobian $J(A(X))$ 的条件数 $\kappa(J(A))$ 受限于这三个矩阵条件数的组合。具体地，Theorem 3.1 给出上界：

$$ \kappa(J(A)) \leq C \cdot (\kappa(W_Q) \kappa(W_K) + \kappa(W_V)) $$

其中 $C$ 为与输入 $X$ 相关的常数。该公式表明，降低 $W_Q, W_K, W_V$ 的条件数可直接收紧Jacobian条件数上界，从而抑制梯度爆炸或消失。

### 条件数驱动的初始化策略

设计动机在于利用谱结构明确的矩阵族实现条件数最小化。本文提出Conditioned Initialization，将 $W_V$ 初始化为矩形单位阵 $I_{D \times d}$，保持 $\kappa(W_V)=1$ 且不扭曲输入尺度；将 $W_Q, W_K$ 初始化为半正交矩阵 $O_{D \times d}$（行或列正交），确保 $\kappa(W_Q)=\kappa(W_K)=1$。具体实现中，第 $i$ 个头的 $W_Q^{[i]}, W_K^{[i]}$ 独立采样半正交投影，形成近等距嵌入，分散Logits分布。

$$ W_V^{[i]} = I_{D \times d}, \quad W_Q^{[i]}, W_K^{[i]} \sim O_{D \times d} $$

此策略避免了随机初始化中谱分布的随机性，使初始Jacobian条件数达到理论下界附近，为优化提供稳定的起始点。

## 实验评估

实验在ImageNet-1k、COCO、GLUE及LRA基准上进行，对比Default（截断正态）、Mimetic及Conditioned Initialization。基线覆盖主流启发式方法，但缺乏对Weight Selection在大规模任务上的详细对比。主实验显示，Conditioned Initialization在所有测试架构上均优于其他两种初始化。

| 模型 | Default | Mimetic | Conditioned (ours) |
| :--- | :--- | :--- | :--- |
| ViT-B | 80.3 | 80.5 | 81.5 |
| Swin-B | 83.4 | 83.5 | 84.6 |
| XCiT-M | 82.6 | 82.6 | 83.5 |
| DaViT-B | 84.3 | 84.4 | 85.3 |

在ImageNet-1k上，ViT-B的Top-1准确率从Default的80.3%提升至81.5%，Swin-B从83.4%提升至84.6%。收敛速度方面，Conditioned Initialization比Default快20-30%达到相同精度。

| 任务 | Default | Mimetic | Conditioned (ours) |
| :--- | :--- | :--- | :--- |
| ListOps | 37.1 | 37.1 | 37.9 |
| Text | 63.8 | 64.0 | 64.9 |
| Retrieval | 79.8 | 79.9 | 80.8 |
| Image | 39.9 | 40.2 | 40.4 |

在LRA长程序列任务上，ListOps准确率从37.1%提升至37.9%，Text任务从63.8%提升至64.9%。消融实验表明，$W_V$ 的单位阵初始化对保持输入尺度至关重要，而 $W_Q, W_K$ 的半正交性对分散注意力模式起关键作用。

评估边界方面，论文未报告训练时间或内存开销，仅关注精度与收敛Epoch数。可复现性受限于未公开代码，但初始化策略描述清晰，易于实现。理论验证仅展示条件数下降，未直接关联到泛化误差的理论界。

## 关联研究分析

从问题动机看，本文与NTK（Neural Tangent Kernel）分析路线存在本质差异。Liu et al. (2022) 通过NTK条件数分析无限宽网络的收敛性，而本文聚焦有限宽Transformer的Jacobian条件数。NTK方法假设网络宽度趋于无穷，忽略了注意力层的非线性交互，而本文的Jacobian分析直接针对实际架构，但代价是理论复杂度更高且仅提供上界。这种差异源于任务特性：NTK适用于线性化近似，而Transformer的Softmax非线性使得Jacobian谱分析更为必要。

从方法设计看，本文与Mimetic Initialization形成互补而非替代关系。Mimetic通过统计匹配引入偏置，缺乏理论保证；本文通过谱结构控制提供理论驱动的设计。然而，本文未探讨Conditioned Initialization与预训练任务多样性的交互作用。在ICL理论中，任务多样性对泛化至关重要，而本文的初始化策略可能通过稳定优化间接影响模型对多任务的学习能力，但论文未验证其对归纳头涌现动力学的影响。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

本文核心矛盾在于Transformer初始化缺乏对注意力Jacobian条件数的理论约束，导致优化不稳定。现有方法如Mimetic Initialization依赖启发式统计匹配，无法保证谱结构优化。本文通过建立Jacobian条件数与 $W_Q, W_K, W_V$ 谱性质的联系，提出Conditioned Initialization，将 $W_V$ 初始化为单位阵，$W_Q, W_K$ 初始化为半正交矩阵。实验证明该方法在ImageNet-1k上ViT-B准确率提升1.2%，收敛速度加快20-30%。其边界在于理论保证仅限于条件数上界收紧，未直接证明对最终泛化误差的因果影响，且未验证对ICL任务多样性的影响。当预训练任务多样性降低时，条件数更优的初始化是否会导致模型过拟合于特定任务，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_45899240)