# 加州大学洛杉矶分校团队新研究：连续时间Dropout的随机过程重构

研究机构：美国加州大学洛杉矶分校

作者：Jonghun Lee、YongKyung Oh、Sungil Kim 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.10446)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.10446)

> 导读 Neural Differential Equations (NDEs) 在建模连续时间动态时面临过拟合难题，而离散神经网络中核心的Dropout正则化机制无法直接迁移至连续时间框架。现有方法如Jump Diffusion或STEER要么架构受限，要么缺乏理论忠实性，导致正则化效果不稳定且无法提供原则性的不确定性量化。本文提出Continuum Dropout，基于交替更新过程（Alternating Renewal Process）将Dropout的开关机制重构为连续时间随机过程，实现了架构通用且理论自洽的正则化。该方法在时间序列与图像分类任务上显著优于现有正则化技术，但其对物理守恒律的忽略使其在长时程动力学预测中的适用性存疑。

## 研究背景

理解本文需厘清NDE与离散Dropout的本质差异。NDE通过神经网络参数化向量场 $f_\theta(h(t), t)$ 描述状态 $h(t)$ 的连续演化，其训练依赖伴随方法实现恒定内存梯度计算。然而，离散Dropout通过随机置零神经元来抑制共适应，其作用对象是离散的层间传递；在NDE中，状态是连续轨迹，直接对漂移函数施加Dropout会破坏微分方程的连续结构，导致训练不稳定或失效。

NDE在有限数据或复杂架构下极易过拟合，现有正则化方案存在明显短板。Neural SDEs 引入随机项但改变了动力学本质；Jump Diffusion 模型虽尝试连续化Dropout，但其离散化形式无法还原标准ResNet-Dropout公式，且仅适用于特定NDE变体；STEER 和 TA-BN 则针对特定架构设计，缺乏通用性。更关键的是，这些方法大多未提供原则性的不确定性量化框架。本文切入点在于：Dropout在连续时间下的忠实类比不应是添加噪声，而是对演化过程本身的随机暂停。

## 核心方法

### 方法参照系

标准NDE正则化流程通常是在损失函数中加入惩罚项（如权重衰减）或修改网络结构（如TA-BN）。本文问题与该通用流程的关键差异在于：它不改变NDE的确定性积分结构，而是在训练阶段引入一个外生的随机开关过程，使轨迹在“演化”与“暂停”之间随机切换，从而在保持NDE架构不变的前提下实现正则化。

### 交替更新过程建模

设计动机在于解决Jump Diffusion等现有方法在离散化时无法还原标准Dropout机制的理论缺陷。本文定义隐状态 $z(t)$ 的第 $i$ 个分量受一个二状态交替更新过程控制，其中活跃期长度 $X_n^{(i)} \sim \text{Exp}(\lambda_1)$，非活跃期长度 $Y_n^{(i)} \sim \text{Exp}(\lambda_2)$。动力学方程被修改为：

$$ \frac{dz_i(t)}{dt} = I_{\lambda_1, \lambda_2}(t) \cdot \gamma_\theta(z(t), t) $$

其中 $I_{\lambda_1, \lambda_2}(t)$ 为指示函数，当系统处于活跃状态时为1，否则为0。该公式的物理含义是：在非活跃期，状态 $z_i(t)$ 保持恒定（演化暂停）；在活跃期，状态按原始NDE向量场演化。这种构造确保了当时间步长趋于0时，其离散化行为严格对应于ResNet中逐层随机置零的Dropout机制，从而实现了理论上的忠实性。

### 连续时间Dropout率定义与不确定性量化

设计动机在于解决连续时间中“Dropout率”定义模糊及缺乏不确定性量化框架的问题。本文借鉴更新理论中的瞬时可用性（Instantaneous Availability），定义Dropout率 $p$ 为终端时间 $T$ 时状态处于非活跃态的概率：

$$ p = 1 - A(T) = 1 - \frac{\lambda_1}{\lambda_1 + \lambda_2} $$

结合期望更新次数 $m$，可通过非线性方程组唯一确定 $\lambda_1, \lambda_2$。在测试阶段，保留随机机制并进行 $N_{MC}$ 次蒙特卡洛前向传播，利用预测轨迹的样本均值作为点估计，样本协方差作为不确定性度量。这一设计将Dropout从单纯的正则化工具扩展为贝叶斯推断的近似框架，提供了比传统NDE更可信的概率估计。

## 实验评估

实验涵盖UEA/UCR时间序列子集（SmoothSubspace, ERing等）及图像数据集（CIFAR-10/100, STL-10, SVHN）。基线覆盖Naïve Dropout、Jump Diffusion、STEER、TA-BN，但缺失物理约束类（如HNN）及基础模型类基线。

| 数据集 | 指标 | Baseline (Neural ODE) | Jump Diffusion | STEER | TA-BN | Continuum Dropout |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SmoothSubspace | Acc | 0.569 (0.040) | 0.617 (0.043) | 0.578 (0.056) | 0.578 (0.035) | **0.629 (0.022)** |
| ERing | Acc | 0.839 (0.018) | 0.861 (0.064) | 0.850 (0.029) | 0.859 (0.023) | **0.881 (0.023)** |
| CIFAR-10 | Acc | 0.739 (0.008) | 0.750 (0.004) | 0.747 (0.008) | 0.762 (0.007) | **0.765 (0.007)** |
| CIFAR-100 | Top-5 | 0.745 (0.012) | 0.761 (0.005) | 0.756 (0.006) | 0.758 (0.003) | **0.762 (0.002)** |

Continuum Dropout在所有测试数据集上均取得最高准确率，尤其在SmoothSubspace上比最强基线Jump Diffusion高1.2个百分点。在PhysioNet Sepsis任务中，结合Continuum Dropout的Neural LSDE模型AUROC达到0.927，显著优于无Dropout版本的0.909。

消融实验显示，Continuum Dropout对多种NDE架构（Neural ODE, SDE, CDE）均有效。以Neural ODE在CIFAR-100上的表现为例，加入Continuum Dropout后准确率从0.745提升至0.762。值得注意的是，TA-BN在CIFAR-10上表现优于Jump Diffusion，但在时间序列任务上落后，表明不同正则化方法对数据类型的敏感性不同。Continuum Dropout的鲁棒性体现在其跨架构和跨数据类型的稳定增益，且对超参数 $m$ 不敏感，降低了调参成本。

评估边界方面，论文未报告计算效率的详细对比（仅提及MC采样次数影响），且未提供置信区间的统计检验细节。代码已开源，但超参数搜索范围（$p \in [0.1, 0.5], m \in [5, 100]$）可能限制了其在极端稀疏数据下的表现验证。

## 关联研究分析

从问题动机看，本文与Jump Diffusion (Liu et al., 2020) 形成直接对立。Jump Diffusion试图通过添加跳跃项模拟Dropout，但其离散化形式无法还原标准ResNet-Dropout的数学结构，导致理论上的不一致。本文通过交替更新过程，从生成机制上保证了离散极限下的忠实性，解决了Jump Diffusion在理论根基上的缺陷。这一差异源于对“Dropout本质”的不同理解：前者视为噪声注入，后者视为演化暂停。

从方法设计看，本文与物理结构嵌入路线（如Hamiltonian Neural Networks）存在根本分歧。HNN通过硬约束保证能量守恒，适用于长时程动力学预测；而Continuum Dropout采用软正则化，旨在提升泛化能力，不保证物理守恒。在缺乏物理先验的通用分类任务中，Continuum Dropout有效；但在需要长期稳定性的物理系统中，随机暂停可能破坏系统的几何结构，导致轨迹漂移。这种差异揭示了正则化目标（泛化 vs. 物理一致性）与系统特性（通用 vs. 保守）之间的权衡。

## 总结

本文核心矛盾在于NDE过拟合与离散Dropout不可迁移性。切入点在于识别Dropout在连续时间下的本质是演化过程的随机暂停，而非噪声添加。通过交替更新过程重构动力学，实现了理论忠实的连续时间Dropout。实验证明其在通用分类任务上优于现有正则化方法，如SmoothSubspace上0.629的准确率。边界在于其未验证物理守恒系统的长时程稳定性，且随机暂停可能破坏NDE的确定性流形结构。当应用于需要严格物理一致性的动力学系统时，随机暂停机制是否会导致长期轨迹偏离物理定律，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.10446)