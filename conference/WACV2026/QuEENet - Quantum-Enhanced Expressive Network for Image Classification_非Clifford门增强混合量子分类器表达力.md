# WACV2026最新论文 ｜QuEENet: Quantum-Enhanced Expressive Network for Image Classification ｜非Clifford门增强混合量子分类器表达力

研究机构：印度理工学院、爱尔兰都柏林圣三一大学

作者：Shashank Bayal、Rushikesh Govind Dawane、Komal Komal 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8daa692e761d)

> 混合量子-经典架构旨在利用经典卷积网络处理高维图像数据，同时借助参数化量子电路（PQC）在希尔伯特空间中提取非线性特征，以解决纯经典模型参数冗余及纯量子模型硬件受限的双重困境。现有混合架构多依赖Clifford门进行纠缠，受Gottesman-Knill定理限制，其状态空间可被经典高效模拟，导致表达力上限受限。本文切入点在于引入非Clifford旋转门（Rx/Rz）打破稳定子结构，提升电路对复杂数据分布的拟合能力。通过构建包含非Clifford纠缠层的QuEENet架构，在低维基准上实现了与经典模型竞争的精度，但在高维彩色图像任务上仍未超越充分调优的经典基线，其“量子优势”的归因仍存疑。

## 研究背景

当经典卷积神经网络（CNN）在图像分类中取得高精度时，其深层架构带来的参数爆炸与计算开销成为部署瓶颈。为降低资源消耗，研究转向混合量子-经典架构，将PQC嵌入经典流水线。然而，早期混合模型多采用仅含Clifford门（如CNOT、Hadamard）的电路，这类电路虽能产生纠缠，但根据Gottesman-Knill定理，其演化过程可被经典计算机多项式时间模拟，无法利用量子叠加与干涉带来的指数级状态空间覆盖。

该领域的核心矛盾在于：如何在有限的NISQ（Noisy Intermediate-Scale Quantum）硬件资源下，使量子组件真正贡献于分类性能，而非仅作为经典网络的附加模块。主流变分量子分类器（VQC）面临贫瘠高原（Barren Plateau）问题，即梯度方差随电路深度指数衰减，导致训练停滞。现有混合架构虽通过经典骨干规避了部分优化困难，但量子层的表达力往往受限于Clifford组的封闭性，难以捕捉高维数据中的复杂非线性结构。本文针对这一表达力瓶颈，提出通过引入非Clifford门扩展量子状态空间，旨在以极低的参数成本提升分类精度。

## 核心方法

### 混合架构参照系

本文方法属于混合量子-经典架构路线，其标准流程为：经典CNN骨干提取特征向量，经角度编码映射至量子态，PQC执行参数化演化，最后测量概率值输入全连接层分类。与Quanvolutional Layers等局部量子卷积不同，QuEENet采用全局PQC处理降维后的特征张量，关键差异在于纠缠层的设计：标准流程通常仅使用CNOT门建立纠缠，而本文在CNOT后串联非Clifford旋转门，以突破经典可模拟性的边界。

### 非Clifford纠缠层设计

设计动机在于解决Clifford-only电路状态空间受限导致的表达力不足问题。在PQC中，CNOT门属于Clifford群，保持稳定子结构不变。本文在纠缠层中，每个CNOT门的目标量子比特后接一个参数化旋转门 $R_x(\theta)$ 或 $R_z(\theta)$，其中 $\theta$ 为可训练参数。这一操作破坏了稳定子性质，使量子态脱离Clifford子空间，进入更稠密的希尔伯特空间区域。

$$
|\psi(\theta)\rangle = R_x(\theta)|0\rangle = \cos\left(\frac{\theta}{2}\right)|0\rangle - i\sin\left(\frac{\theta}{2}\right)|1\rangle
$$

该公式表明，$R_x(\theta)$ 作用后，状态不再被Pauli-Z算符稳定，从而验证了电路已退出Clifford域。这种非Clifford特性使得电路能够生成非稳定子态，显著增加了状态空间的覆盖度。每个量子电路包含41个可训练参数，两个并行电路共82个参数，电路深度仅为6，确保了在NISQ设备上的可行性。

### 基于KL散度的表达力评估

设计动机在于量化非Clifford门对电路表达力的具体贡献，避免仅凭分类精度反推电路特性。本文采用Kullback-Leibler (KL) 散度衡量PQC生成的保真度分布 $P(x)$ 与Haar随机态分布 $Q(x)$ 之间的差异。

$$
D_{KL}(P \| Q) = \sum_{x} P(x) \log \left( \frac{P(x)}{Q(x)} \right)
$$

$D_{KL}$ 值越低，表明电路生成的状态分布越接近Haar随机分布，即表达力越强。实验显示，仅含CNOT门的电路 $D_{KL}$ 为0.3272，而引入CNOT+Rz序列后降至0.078，证实非Clifford门显著提升了电路逼近随机态的能力，为后续分类任务提供了更丰富的特征表示基础。

## 实验评估

实验在MNIST、CIFAR-10、Fashion-MNIST、M-MNIST及FOG-1/2数据集上进行，基线涵盖经典CNN及混合模型（HQNN, HQViT, S-QCNN）。基线审计显示，论文未对比充分调优的经典SOTA（如ResNet-50在CIFAR-10上的93.33%），导致“竞争精度”的声明缺乏强基线支撑。

| 数据集 | 方法 | 参数量 (M) | 准确率 (%) |
| :--- | :--- | :--- | :--- |
| CIFAR-10 | QuEENet CNOT+Rz | 0.085 | 85.73 |
| CIFAR-10 | HQNN | 0.4 | 99.21 |
| MNIST | QuEENet CNOT+Rz | 0.085 | 99.11 |
| MNIST | HQNN | 0.4 | 99.21 |
| F-MNIST | QuEENet CNOT+Rz | 0.085 | 92.70 |
| F-MNIST | S-QCNN | - | 81.00 |

在CIFAR-10上，QuEENet（85.73%）显著低于HQNN（99.21%），但在MNIST和Fashion-MNIST上表现优于部分混合基线。消融实验表明，非Clifford门（CNOT+Rx/Rz）相比纯CNOT门在CIFAR-10上提升了2.03%的准确率（83.70% vs 85.73%），验证了表达力提升对分类性能的贡献。然而，在CIFAR-100上，随着类别数增加，QuEENet准确率从83.70%骤降至45.18%，暴露出量子电路在多类高维任务中的可扩展性瓶颈。

评估边界方面，论文仅在模拟器（PennyLane）上运行，未涉及真实硬件噪声下的性能衰减，尽管Table 7显示在1%-5%噪声下精度下降小于0.06，但缺乏硬件验证。代码未公开，超参数（如学习率0.001，150 epochs）已提供，但缺乏置信区间报告，数值比较需谨慎。

## 关联研究分析

从方法设计看，QuEENet与QCNN（Quantum Convolutional Neural Networks）存在根本差异。QCNN通过局部量子卷积层处理图像块，强调空间局部性，而QuEENet采用全局PQC处理降维特征，侧重全局非线性映射。这种差异源于任务特性：QCNN适用于保留空间结构的低维图像，而QuEENet试图通过全局纠缠捕捉非局部特征。然而，QuEENet在CIFAR-10上的性能落后于HQNN，暗示全局PQC在处理多通道彩色图像时，可能因缺乏局部感受野而丢失关键空间信息，这是论文未探索的盲区。

从问题动机看，QuEENet与量子核方法（QKM）形成对比。QKM通过计算量子态内积作为核函数，避免梯度优化，从而天然规避贫瘠高原问题，但受限于指数集中现象。QuEENet采用变分训练，虽通过非Clifford门增强表达力，但仍面临优化景观的挑战。论文未直接测量梯度方差，仅通过KL散度间接关联表达力与训练稳定性，这种间接验证是否足以证明非Clifford门在深层电路中的训练优势，缺乏直接证据。

## 总结

本文旨在解决混合量子-经典架构中量子层表达力受限于Clifford组的问题，通过引入非Clifford旋转门扩展状态空间，以极低参数成本（0.085M）提升分类精度。实验证明，在MNIST和Fashion-MNIST上，QuEENet达到了99.11%和92.70%的准确率，优于部分混合基线，验证了非Clifford门对表达力的贡献。然而，在CIFAR-10上，其85.73%的准确率远低于充分调优的经典基线，且在CIFAR-100上性能急剧下降，暴露出量子电路在高维多类任务中的可扩展性局限。当类别数从10增加到100时，量子电路的区分能力是否随比特数不足而指数衰减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_8daa692e761d)