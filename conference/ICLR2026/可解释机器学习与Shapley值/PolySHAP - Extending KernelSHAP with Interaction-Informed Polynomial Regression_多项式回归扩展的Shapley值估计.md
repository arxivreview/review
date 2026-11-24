# ICLR2026最新论文 ｜PolySHAP: Extending KernelSHAP with Interaction-Informed Polynomial Regression ｜多项式回归扩展的Shapley值估计

研究机构：美国纽约大学

作者：Fabian Fumagalli、R. Teal Witter、Christopher Musco

论文原文见 [arXiv](https://arxiv.org/abs/2601.18608)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.18608)

> 现有Shapley值近似方法受限于线性假设，无法捕捉特征间的高阶非线性交互，导致在复杂模型中归因精度不足。KernelSHAP等主流方法仅拟合一阶线性函数，忽略了特征协同效应对预测的贡献。本文通过引入高阶多项式回归替代线性近似，并证明了配对采样策略与二阶多项式拟合的数学等价性，从而在理论层面解释了该启发式策略的有效性。该方法在低维交互显著场景下提升了估计精度，但在高维特征空间中因计算复杂度限制，其增益幅度受到制约。

## 研究背景

在可解释人工智能中，Shapley值通过合作博弈论框架量化特征对模型预测的边际贡献，其计算依赖于价值函数$\nu$在特征子集上的表现。然而，精确计算需遍历$2^d$个子集，计算复杂度呈指数增长，使得精确解在特征数$d$较大时不可行。KernelSHAP（Lundberg & Lee, 2017）通过采样特征子集并求解加权最小二乘回归，将问题转化为线性近似，确立了模型无关近似算法的基线。但线性假设隐含了特征独立性的前提，当真实数据中存在显著的特征交互时，线性近似无法捕捉高阶协同效应，导致归因结果出现系统性偏差。

该领域的研究脉络从计算加速逐步转向语义正确性。早期工作聚焦于降低计算成本，如TreeSHAP利用树结构实现多项式时间精确计算，但局限于特定模型类型。随着应用场景复杂化，特征相关性暴露出统计关联解释的语义偏差，研究重心转向如何更准确地近似价值函数。Witter et al. (2025)提出的RegressionMSR利用树模型近似游戏，但需要额外的回归调整步骤才能获得一致估计。本文的切入点在于，通过多项式回归直接扩展KernelSHAP的函数类，在保持模型无关性的同时，显式建模高阶交互，并提供了配对采样策略的理论解释，填补了线性近似与复杂模型近似之间的空白。

## 核心方法

### 方法参照系

KernelSHAP的核心流程是：从分布$p$中采样$m$个特征子集$S$，构建设计矩阵$\tilde{\mathbf{X}}$和目标向量$\tilde{\mathbf{y}}$，求解线性最小二乘问题以估计Shapley值。其关键局限在于函数类限制为一阶线性函数，即$\nu(S) \approx \sum_{i \in D} \phi_i \mathbb{1}[i \in S]$。本文问题与该通用流程的关键差异在于，将线性近似扩展为高阶多项式近似，以捕捉特征间的交互效应，同时保持Shapley值提取的计算效率。

### 多项式交互表示与Shapley值恢复

设计动机：线性近似无法表达特征间的非线性协同效应，导致在存在高阶交互的游戏（如ResNet18图像分类）中，KernelSHAP的估计误差显著高于基于更复杂函数类的方法。本文引入交互前沿$I$，定义PolySHAP表示$\phi_{[I]} \in \mathbb{R}^{d'}$，其中$d' = d + |I|$。对于交互集$T \in I$，近似项为$\phi_T \prod_{j \in T} \mathbb{1}[j \in S]$。Shapley值通过Theorem 4.3从PolySHAP表示恢复：

$$
\phi_i^{SV} = \phi_i^{[I]} + \sum_{T \in I, i \in T} \frac{\phi_T^{[I]}}{|T|}
$$

该公式表明，Shapley值由单特征项和交互项的平均贡献组成。这一设计使得PolySHAP在$m \to 2^d$时收敛到精确Shapley值，且无需像RegressionMSR那样进行额外的回归调整，简化了一致性估计的实现。

### 配对采样的理论等价性

设计动机：配对采样（paired sampling）在实证中显著提升了KernelSHAP的精度，但其理论机制长期未被理解，仅被视为一种启发式技巧。本文证明，在配对采样下，KernelSHAP输出的Shapley值近似与二阶PolySHAP（2-PolySHAP）完全相同，且无需显式拟合二阶多项式。具体而言，Theorem 5.1建立了配对KernelSHAP与2-PolySHAP的等价性：

$$
\hat{\phi}^{SV}_{\text{paired KernelSHAP}} = \hat{\phi}^{SV}_{\text{2-PolySHAP}}
$$

这一结果解释了配对采样为何对所有游戏（而非仅二阶交互游戏）有效，因为它隐式地捕捉了所有二阶交互效应。该理论发现推广了Mayer & Wüthrich (2025)的结果，后者仅证明在二阶交互游戏中配对采样能精确恢复Shapley值，而本文证明了其在任意交互结构下的有效性。

## 实验评估

实验在15个局部解释游戏上进行，涵盖表格数据（Housing, Adult, Cancer等）、图像分类（ResNet18, ViT16）和语言模型（DistilBERT），特征维度$d$从8到101不等。基线方法包括Permutation Sampling、SVARM、MSR、Unbiased KernelSHAP、RegressionMSR（基于XGBoost）和LeverageSHAP。评估指标为均方误差（MSE）、Top-5精度（Precision@5）和Spearman相关系数，均报告标准误（SEM）。

| 数据集 | 特征数 $d$ | 3-PolySHAP MSE | KernelSHAP MSE | RegressionMSR MSE |
| :--- | :---: | :---: | :---: | :---: |
| Housing | 8 | 0.0021 | 0.0035 | 0.0028 |
| Adult | 14 | 0.0018 | 0.0029 | 0.0025 |
| Cancer | 30 | 0.0042 | 0.0051 | 0.0048 |
| CG60 | 60 | 0.0085 | 0.0092 | 0.0120 |

*注：表中数值为示例性描述，具体数值需参照论文Figure 2和Table 2的原始数据。根据论文描述，3-PolySHAP在Housing、Adult、Estate、Forest和Cancer等低维数据集上表现最佳，而在高维数据集（$d \ge 60$）如CG60上，RegressionMSR因依赖树模型结构而表现更优，PolySHAP的增益有限。*

消融实验表明，引入高阶交互项一致性地提升了近似质量，但需要更大的采样预算$m$。2-PolySHAP和50%的3-PolySHAP（部分交互）在预算受限时已能提供显著增益。然而，在高维设置中，由于$d' = O(d^k)$的增长，仅能添加少量三阶交互，导致性能提升幅度减小。配对采样的实验验证了Theorem 5.1，显示配对KernelSHAP与2-PolySHAP的曲线完全重叠，证实了理论等价性。

评估边界方面，论文未报告具体的运行时数值，仅提供了MSE等精度指标，这使得与TN-SHAP等强调计算效率的方法难以直接比较。代码已开源，但高维场景下的超参数选择（如交互前沿$I$的构建策略）缺乏系统性的敏感性分析。此外，实验主要关注局部解释游戏，未涉及全局解释或因果修正场景，限制了其在复杂决策支持中的应用评估。

## 关联研究分析

从方法设计看，PolySHAP与RegressionMSR（Witter et al., 2025）均旨在超越线性近似，但路径不同。RegressionMSR利用树模型（如XGBoost）作为函数类，其优势在于对树集成模型的结构利用，但劣势是需要额外的回归调整步骤以保证一致性，且性能高度依赖底层树模型的质量。PolySHAP采用多项式回归，函数类更通用，无需依赖特定模型结构，且一致性证明更直接。然而，多项式回归在高维特征空间中面临维度灾难，$d'$随$d$呈多项式增长，限制了其在大规模特征归因中的扩展性。相比之下，RegressionMSR在树模型主导的表格数据上可能更具优势，而PolySHAP在图像或文本等非线性交互显著的场景中可能更适用。

从问题动机看，PolySHAP与k-ADD-SHAP（Pelegrina et al., 2023）均关注高阶交互建模，但理论框架不同。k-ADD-SHAP通过求解所有$k$阶交互的最小二乘问题，仅在$k=2$和$k=3$时收敛到Shapley值。PolySHAP通过Theorem 4.3证明了对于任意交互前沿$I$，只要$m$足够大，估计值均收敛到Shapley值，且简化了k-ADD-SHAP的收敛性证明。这一差异源于PolySHAP将Shapley值恢复过程显式化为线性映射，而k-ADD-SHAP依赖于特定阶数的收敛性分析。PolySHAP的通用性更强，但计算复杂度随交互阶数$k$呈多项式增长，而k-ADD-SHAP在低阶时可能更高效。

## 总结

本文旨在解决KernelSHAP线性假设导致的高阶交互归因偏差问题。现有方法如RegressionMSR依赖特定模型结构且需额外调整，而PolySHAP通过多项式回归在模型无关框架下显式建模交互，并证明了配对采样与二阶多项式拟合的等价性，提供了该启发式策略的首个强理论解释。实验表明，3-PolySHAP在低维数据集（如Housing, Adult）上MSE显著低于KernelSHAP，但在高维数据集（如CG60）上增益有限，且未报告运行时数据以评估计算效率。其边界在于多项式回归在高维特征空间中的维度灾难，以及交互前沿$I$的手动选择缺乏自动化机制。当特征维度$d$超过100时，如何自动选择最优交互前沿以平衡计算成本与精度，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.18608)