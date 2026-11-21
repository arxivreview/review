# ICLR2026最新论文 ｜Spurious Correlation-Aware Embedding Regularization for Worst-Group Robustness ｜虚假相关感知嵌入正则化

研究机构：韩国延世大学

作者：Subeen Park、Joowang Kim、Hakyung Lee 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.04401)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.04401)

> 子群体偏移下的最坏群体鲁棒性优化旨在解决模型在测试分布与训练分布不一致时，对少数群体性能崩溃的问题。现有方法多通过样本重加权或特征对齐间接抑制偏差，缺乏对嵌入空间结构的直接理论约束，导致虚假相关特征在表示层面持续存在。本文提出 SCER，通过分解最坏群体误差并直接在嵌入空间施加方向性正则化，显式分离虚假特征与核心特征。该方法在多个基准上实现了最坏群体准确率的提升，但其理论推导依赖高斯分布假设，在复杂非线性数据中的普适性存疑。

## 研究背景

当分类器在训练阶段过度依赖背景、水印等与标签强相关但无因果关系的特征时，一旦测试分布中这些捷径断裂，模型性能将急剧下降。这种现象源于经验风险最小化（ERM）仅最小化平均损失，忽视了子群体间的分布不平衡，导致模型优先拟合简单但脆弱的虚假特征。为量化这种脆弱性，研究者引入最坏群体准确率（Worst-Group Accuracy），即模型在所有标签-域组合子群体中表现最差的那个群体的准确率，以此作为鲁棒性的核心指标。

子群体鲁棒性优化（Subpopulation Robustness Optimization）是该领域的主流路线，GroupDRO 通过动态调整损失权重来平衡群体性能，LISA 和 PDE 则通过数据增强或渐进式训练来缓解偏差。然而，这些方法主要作用于损失函数或数据分布层面，属于间接干预，未能显式约束嵌入空间中虚假特征的编码方式。Invariant Risk Minimization (IRM) 等不变学习方法虽旨在学习环境不变特征，但依赖显式的环境标签或复杂的双层优化，计算开销大且难以在无标注场景部署。SCER 的切入点在于，将最坏群体误差的理论分解直接映射到嵌入空间的几何结构上，通过正则化手段直接抑制模型对虚假方向的依赖，从而在无需显式群体标签的情况下实现鲁棒学习。

## 核心方法

### 方法参照系

SCER 建立在 GroupDRO 的最坏群体优化框架之上，但将干预点从损失权重移至嵌入空间。与 ElRep 等仅施加范数惩罚的方法不同，SCER 引入了基于均值差异的方向分解，显式区分虚假特征与核心特征，并量化分类器权重与这两个方向的对齐程度。

### 嵌入空间方向分解

SCER 首先计算每个标签-域对 $(y, d)$ 的均值嵌入 $\mu_{y,d}$。虚假特征方向 $\Delta_{spur}$ 定义为同一类别在不同域间均值嵌入的平均差异，核心特征方向 $\Delta_{core}$ 定义为同一域内不同类别间均值嵌入的平均差异。

$$
\Delta_{spur} = \frac{1}{k} \sum_{d \in \mathcal{D}} (\mu_{y,d} - \bar{\mu}_y), \quad \Delta_{core} = \frac{1}{m} \sum_{y \in \mathcal{Y}} (\mu_{y,d} - \bar{\mu}_d)
$$

这一设计动机在于，虚假特征源于域内的类间混淆，而核心特征源于域间的类内一致性。通过 $\Sigma$-范数 $\|v\|_\Sigma = \sqrt{v^\top \Sigma v}$ 对方向向量进行归一化，SCER 量化了虚假幅度 $\|\Delta_{spur}\|_\Sigma$ 和核心幅度 $\|\Delta_{core}\|_\Sigma$，从而在几何上区分了两种特征的强度。

### 方向对齐正则化

SCER 计算分类器权重矩阵 $\beta^*$ 与上述方向的平均相关性，即权重-虚假对齐（Weight-Spurious Alignment）和权重-核心对齐（Weight-Core Alignment）。

$$
\mathcal{L}_{SCER} = \mathcal{L}_{wge} + \lambda_{spur} \cdot \text{cor}(\beta^*, \Delta_{spur}) \|\Delta_{spur}\|_\Sigma - \lambda_{core} \cdot \text{cor}(\beta^*, \Delta_{core}) \|\Delta_{core}\|_\Sigma
$$

该损失函数通过最小化虚假对齐项来惩罚模型对域特定模式的依赖，同时通过最大化核心对齐项来强化对标签相关信号的捕捉。这一机制直接解决了 ERM 中模型因简单性偏差而过度拟合虚假特征的问题，使得决策边界在嵌入空间中更加稳定，从而提升了最坏群体准确率。

## 实验评估

SCER 在 Waterbirds、CelebA、MetaShift 和 ColorMNIST 等视觉基准，以及 CivilComments 和 MultiNLI 文本基准上进行了评估。基线涵盖了 ERM、GroupDRO、LISA、PDE、ReSample 和 ElRep 等主流方法，但缺失了 IRM 等不变学习方法的直接对比（仅在无标签实验中提及）。

| 数据集 | 方法 | Avg Acc | Worst Acc |
| :--- | :--- | :--- | :--- |
| Waterbirds | ERM | 84.1 | 69.1 |
| Waterbirds | GroupDRO | 88.8 | 78.6 |
| Waterbirds | SCER | 92.1 | **91.2** |
| CelebA | ERM | 95.1 | 62.6 |
| CelebA | GroupDRO | 91.4 | 89.0 |
| CelebA | SCER | 92.7 | **91.4** |
| ColorMNIST ($\rho=80\%$) | ERM | 38.2 | 30.9 |
| ColorMNIST ($\rho=80\%$) | GroupDRO | 73.5 | 73.1 |
| ColorMNIST ($\rho=80\%$) | SCER | 74.1 | **73.6** |

SCER 在四个视觉数据集上均取得了最高的最坏群体准确率，其中在 CelebA 上达到 91.4%，显著优于 GroupDRO 的 89.0%。在 ColorMNIST 上，随着虚假相关强度 $\rho$ 从 80% 增加到 99%，SCER 的最坏群体准确率从 73.6% 降至 56.0%，但仍优于所有基线，表明其在强偏差下的鲁棒性。

| 设置 | 方法 | Worst Acc |
| :--- | :--- | :--- |
| ColorMNIST ($\rho=95\%$, $\lambda_{core}=0.5$) | SCER | **72.2** |
| ColorMNIST ($\rho=95\%$, $\lambda_{spur}=1.0$) | SCER | **72.8** |
| ColorMNIST (One Group Omitted) | SCER | **59.6** |
| ColorMNIST (No Bias Labels) | EIIL + SCER | **72.6** |

消融实验显示，$\lambda_{core}$ 和 $\lambda_{spur}$ 的联合优化效果优于单独使用，验证了理论中虚假与核心特征互补性的假设。在极端缺失群体场景下，SCER 达到 59.6% 的最坏群体准确率，远超 GroupDRO 的 44.1%，证明了嵌入级正则化在分布外泛化上的优势。在无显式偏差标签的实验中，SCER 与 EIIL 结合后达到 72.6% 的准确率，优于 EIIL + DRO 的 68.2%，表明其模块化设计适用于无标注场景。

评估协议主要依赖最坏群体准确率和平均准确率，未报告计算开销或训练时间。代码已开源，但理论推导基于高斯分布假设，实际数据中的非高斯特性可能对正则化效果产生未量化的影响。

## 关联研究分析

从方法设计看，SCER 与 ElRep 同属嵌入空间正则化路线，但 ElRep 仅施加范数惩罚以约束表示的尺度，而 SCER 引入了方向分解与对齐度量。这一差异源于 SCER 试图显式区分虚假与核心特征，而非仅限制表示的复杂度。ElRep 的范数惩罚可能无意中抑制了核心特征的强度，而 SCER 通过最大化核心对齐项避免了这一问题，这在 CelebA 等复杂人口统计学偏差场景中表现为更高的最坏群体准确率。

从问题动机看，SCER 与 GroupDRO 均旨在优化最坏群体性能，但 GroupDRO 依赖显式的群体标签来调整损失权重，而 SCER 通过嵌入空间的结构化正则化实现类似效果。GroupDRO 在群体标签缺失或噪声较大时性能下降明显，如 Table 4 所示，而 SCER 对标签噪声具有更强的鲁棒性。这一差异表明，嵌入空间的结构信息比损失权重的动态调整更能捕捉虚假相关的本质，尤其是在群体定义模糊或动态变化的场景中。

## 总结

SCER 旨在解决子群体偏移下模型对虚假特征的过度依赖问题，其切入点在于将最坏群体误差的理论分解直接应用于嵌入空间正则化，从而在无需显式群体标签的情况下抑制虚假特征。通过分解虚假与核心方向并施加方向对齐正则化，SCER 在 Waterbirds 和 CelebA 上分别达到了 91.2% 和 91.4% 的最坏群体准确率，优于 GroupDRO 等主流方法。然而，其理论推导依赖高斯分布假设，且在 ColorMNIST $\rho=99\%$ 的极端偏差下性能仍降至 56.0%，表明在高维非线性数据中，嵌入空间的方向分解可能无法完全捕捉复杂的虚假相关结构。当数据分布严重偏离高斯假设时，$\Sigma$-范数归一化是否仍能准确量化虚假与核心特征的强度，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.04401)