# ICLR2026最新论文 ｜LEAP: Local ECT-Based Learnable Positional Encodings for Graphs ｜局部欧拉特征变换位置编码

研究机构：瑞士苏黎世联邦理工学院、瑞士弗里堡大学

作者：Juan Amboage、Ernst Röell、Patrick Schnider 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.00757)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.00757)

> 图神经网络在处理非欧几里得结构化数据时，常因消息传递机制的局部性而丢失全局拓扑信息，导致无法区分结构相似但位置不同的节点。现有位置编码方法多依赖单一几何或拓扑视角，且多为静态预处理，难以端到端优化。本文提出LEAP，一种基于局部欧拉特征变换的可学习位置编码，通过联合捕获几何与拓扑信息增强图表示能力。该方法在多个基准数据集上显著优于静态基线，但其对大规模节点分类任务的泛化能力尚存疑。

## 研究背景

图结构数据包含节点特征（几何信息）与边连接（拓扑信息），标准消息传递神经网络（MPNN）仅通过局部邻居聚合更新节点表示，这种机制在区分具有相同局部结构但不同全局位置的节点时存在根本局限。位置编码（Positional Encoding, PE）旨在为节点注入结构信息以弥补这一缺陷，但现有方法如拉普拉斯位置编码（LaPE）依赖全局谱分解，计算成本高且存在特征向量符号歧义；随机游走位置编码（RWPE）虽具局部性，但仅捕获拓扑信息，缺乏几何感知能力。

领域共识认为，高阶结构或拓扑不变量的引入能突破1-WL测试的表达力限制，但多数方法因计算复杂度呈立方级增长而难以扩展。Dwivedi等人（2022, 2023）提出的LaPE和RWPE虽被广泛采用，但前者为全局编码，后者为静态局部编码，均无法在端到端训练中自适应调整。本文切入点在于利用欧拉特征变换（Euler Characteristic Transform, ECT）这一几何-拓扑不变量，将其局部化并引入可学习机制，以线性复杂度实现高阶结构捕获。

## 核心方法

### 方法参照系

本文问题属于图位置编码路线，标准流程为：从图结构生成节点嵌入，作为GNN输入。与LaPE（全局谱）和RWPE（局部随机游走）的关键差异在于，LEAP基于局部$m$-hop子图的几何-拓扑不变量，且方向向量可端到端训练，而非静态预处理。

### 局部欧拉特征变换计算

设计动机：传统PE如RWPE仅捕获拓扑信息，LaPE依赖全局谱分解，无法同时利用几何与拓扑信息且计算成本高。LEAP通过计算节点$m$-hop子图的局部ECT，联合捕获几何（特征向量）与拓扑（边连接）信息。给定特征图$(G, x)$，节点$v$的$k$维LEAP编码计算如下：

$$
\text{PE}(v) = \phi(\mathbf{M}), \quad \mathbf{M}_{ij} = \text{DECT}(\mathcal{N}_m(v, G), f; \theta_i, t_j)
$$

其中$\mathcal{N}_m(v, G)$为$v$的$m$-hop子图，$f$为归一化后的节点特征，$\theta_i \in \Theta$为方向向量，$t_j \in T$为阈值，$\text{DECT}$为可微分ECT近似，$\phi$为可学习投影。该公式表明，LEAP通过在不同方向和阈值下计算子图的欧拉特征曲线，生成矩阵表示$\mathbf{M}$，再投影为低维向量。

### 可学习投影策略

设计动机：ECT矩阵$\mathbf{M}$维度高且对方向顺序敏感，直接输入GNN会导致参数爆炸和过拟合。LEAP引入五种投影策略，其中DeepSets和Attention策略通过置换不变性处理方向集合，避免对方向顺序的依赖。以DeepSets为例，投影公式为：

$$
\text{PE}(v) = \text{MLP}_2\left(\sum_{\theta \in \Theta} \text{MLP}_1(\text{ECC}_\theta)\right)
$$

其中$\text{ECC}_\theta$为方向$\theta$下的欧拉特征曲线。该设计通过集合运算消除方向顺序影响，使参数数量与$|\Theta|$无关，仅依赖$|T|$，从而在保持表达力的同时降低计算开销。

## 实验评估

实验在TU Benchmark（LETTER, FINGERPRINT等）、Alchemy和HIV数据集上进行，基线包括GCN、GAT、GIN、NoMP架构，PE基线含RWPE、LaPE。缺失高阶WL或子图聚合类基线，如PPGN或ESAN，难以评估LEAP在表达力极限上的表现。

| 数据集 | 最佳方法 | 最差基线 | 最佳准确率 (%) | 提升 (%) |
| --- | --- | --- | --- | --- |
| LETTER-H | NoMP + LEAP-L + 1D Conv | 41.6 | 81.6 | 96.2 |
| LETTER-M | NoMP + LEAP-L + 1D Conv | 57.8 | 88.5 | 53.1 |
| LETTER-L | NoMP + LEAP-L + 1D Conv | 80.4 | 98.0 | 21.9 |
| FINGERPRINT | NoMP + LEAP-L + Linear | 48.8 | 55.7 | 14.1 |
| COX2 | GAT + LEAP-L + Attn w/ PE | 77.7 | 80.1 | 3.1 |
| BZR | NoMP + LEAP-L + Linear | 78.3 | 84.7 | 8.2 |
| DHFR | GCN + LEAP-L + Attn w/ PE | 70.1 | 77.6 | 10.7 |

LEAP在LETTER系列数据集上提升显著，尤其在LETTER-H上提升96.2%，表明局部拓扑编码对结构敏感任务有效。消融实验显示，增加邻域大小$m$未提升性能，1-hop邻域已足够；学习方向（LEAP-L）在GCN和NoMP架构上优于固定方向（LEAP-F），但在GAT上3/7数据集性能略降，提示方向学习对架构的依赖性。

评估边界：论文未报告置信区间，数值比较需谨慎；未提供代码URL，可复现性受限；超参数$m$、$|\Theta|$、$|T|$的敏感性分析不足，仅显示1-hop邻域最优。

## 关联研究分析

从问题动机看，LEAP与LaPE（Maskey et al., 2022）均旨在增强GNN的全局结构感知，但LaPE依赖全局谱分解，存在特征向量符号歧义和计算高成本；LEAP采用局部$m$-hop子图，以线性复杂度实现几何-拓扑联合编码。这一差异源于任务特性：LaPE适用于小规模图分类，LEAP更适合大规模节点分类，但论文未验证LEAP在Cora等大规模节点分类任务上的表现，其局部性是否足以捕获长程依赖存疑。

从方法设计看，LEAP与RWPE（Dwivedi et al., 2022）同属局部结构编码，但RWPE仅捕获拓扑信息（随机游走），LEAP联合几何（特征向量）与拓扑（边连接）。这一改进源于ECT的注入性保证，理论上超越1-WL测试，但论文未与高阶WL方法（如PPGN）对比，无法量化LEAP在表达力极限上的优势。此外，LEAP的可学习方向机制是否导致过拟合，还是真正提升泛化，论文未给出回答。

## 总结

本文核心矛盾是标准MPNN无法区分结构相似但位置不同的节点，且现有PE方法依赖单一视角或静态预处理。LEAP抓住的切入点是利用局部ECT联合捕获几何与拓扑信息，并通过可学习投影降低计算开销。方法上，LEAP基于$m$-hop子图的DECT生成矩阵表示，再投影为低维向量。实验证明，LEAP在LETTER-H上提升96.2%，在Alchemy上R²显著优于基线。边界在于，论文仅在TU Benchmark和Alchemy/HIV上验证，未覆盖大规模节点分类任务（如Cora），且缺失高阶WL基线对比。当支持集增大到5-shot时，LEAP的局部性是否足以捕获长程依赖，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.00757)