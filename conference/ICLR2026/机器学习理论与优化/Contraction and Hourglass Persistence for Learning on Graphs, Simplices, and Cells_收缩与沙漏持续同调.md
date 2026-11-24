# ICLR2026最新论文 ｜Contraction and Hourglass Persistence for Learning on Graphs, Simplices, and Cells ｜收缩与沙漏持续同调

研究机构：美国宾夕法尼亚大学、芬兰阿尔托大学

作者：Mattie Ji、Indradyumna Roy、Vikas Garg

论文原文见 [arXiv](https://arxiv.org/abs/2604.17548)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17548)

> 图神经网络（GNN）在处理高阶拓扑信号时，传统前向持续同调（Forward PH）存在“循环永死”与度量不可定义的缺陷。现有方法仅通过包含操作构建滤波，无法捕获拓扑特征的消失过程，导致表达力受限。本文引入拓扑收缩（Contraction）作为反向操作，提出前向-后向（FB）持续同调与沙漏持续同调（Hourglass Persistence），通过交错包含与收缩赋予拓扑特征有限寿命。该方法在理论表达力上严格优于单向PH，但在标准基准上未超越基于子图聚合的SOTA，其价值在于提供了更完备的拓扑描述符生成机制，而非整体架构的性能突破。

## 研究背景

理解本文需厘清持续同调（Persistent Homology, PH）在图学习中的角色。PH通过跟踪拓扑特征（如连通分量、循环）在滤波过程中的出生与死亡，提取全局结构信息。然而，标准PH依赖包含（Inclusion）操作，即逐步添加节点和边。这种单向过程导致一个关键缺陷：在图结构中，一旦循环形成，它在前向滤波中永远不会消失，只能标记为“永久特征”（death = $\infty$）。这使得不同图之间的瓶颈距离（Bottleneck Distance）可能因永久特征数量不同而变为无穷大，破坏了度量的有效性。

GNN表达力受限于1维Weisfeiler-Lehman（1-WL）测试，高阶结构增强是突破该限制的主流路线。现有PH增强方法（如RePHINE）虽能学习滤波函数，但仍局限于前向包含，无法区分那些前向PH相同但拓扑演化历史不同的图。本文切入点在于引入拓扑收缩（Contraction），即逐步移除子结构，作为包含的对偶操作。通过结合前向包含与反向收缩，本文构建了双向拓扑描述符，旨在解决前向PH中特征寿命无限及度量失效的问题。

## 核心方法

### 方法参照系

标准PH增强GNN流程为：定义滤波函数 $f$ → 构建包含序列 $G_{-1} \subset G_0 \subset \dots \subset G_n$ → 计算持续图（Persistence Diagram）→ 编码为向量输入GNN。本文的关键差异在于：将单一的包含序列扩展为包含与收缩的交错序列，并重新定义中间复形（Intermediate Complexes）作为收缩的基本单元。

### 反向持续同调与FB-Persistence

传统方法仅计算包含序列的持续图，导致循环特征无法“死亡”。本文定义反向持续同调（Backward PH, BH），通过收缩中间复形 $IC_i(G)$ 来消除拓扑特征。$IC_i(G)$ 定义为 $G_i - G_{i-1}$ 的闭包。反向序列为 $G \to G/IC_n \to G/(IC_n \cup IC_{n-1}) \to \dots \to \ast$。

前向-后向持续同调（FB-Persistence）将包含序列与收缩序列拼接：

$$
\text{PD}_{FB} = \text{PD}_{Forward}(G_{-1} \subset \dots \subset G_n) \oplus \text{PD}_{Backward}(G \to \dots \to \ast)
$$

该公式的物理含义是：前向部分记录特征如何出现，后向部分记录特征如何消失。FB-Persistence严格优于前向与后向PH的简单组合，因为它能区分前向和反向PH均相同但拓扑演化顺序不同的图。

### 沙漏持续同调与通用框架

FB-Persistence固定了“先全包含后全收缩”的顺序，限制了灵活性。沙漏持续同调（Hourglass Persistence）允许包含与收缩以任意顺序交错，唯一约束是某子结构必须先被包含才能被收缩。这提供了运行时与拓扑信息量的权衡。

为统一扩展持续同调（Extended Persistence）与FB-Persistence，本文提出 $(f, g)$-FB Persistence框架：

$$
\text{PD}_{(f,g)} = H_k(G^f_{-1} \to \dots \to G^f_n \to G^g_0 \to \dots \to G^g_m)
$$

其中 $G^f$ 为滤波函数 $f$ 诱导的包含序列，$G^g$ 为滤波函数 $g$ 诱导的收缩序列。该框架证明了FB-Persistence与Extended Persistence不等价（Proposition 5），确立了其独立的表达力空间。

## 实验评估

实验在NCI109, PROTEINS, IMDB-BINARY, NCI1, ZINC, MOLHIV六个数据集上进行，使用GIN和GCN作为骨干网络。基线包括标准PH、RePHINE（学习滤波+0D增强）、Fwd-only（仅学习前向滤波）、Bwd-only（仅学习收缩顺序）。

| 数据集 | 骨干 | PH | RePHINE | Fwd-only | Bwd-only | Ours |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| NCI109 (Acc.%) | GIN | 76.76 | 77.89 | 77.00 | 76.35 | **77.89** |
| PROTEINS (Acc.%) | GIN | 69.35 | 69.94 | 70.24 | 70.54 | **73.51** |
| ZINC (MAE) | GIN | 0.43 | 0.41 | 0.62 | 0.61 | **0.40** |
| MOLHIV (AUC%) | GIN | **74.34** | 72.88 | 70.00 | 70.59 | 72.34 |

在GIN骨干下，本文方法在NCI109、PROTEINS、ZINC上取得最佳或次佳结果，但在MOLHIV上低于标准PH。RePHINE在ZINC和MOLHIV上表现强劲，提示其0D增强策略在捕获早期连接结构上可能比全局拓扑收缩更关键。

消融实验显示，Fwd-only和Bwd-only均优于标准PH，但两者之间无显著差异，表明前向滤波学习与反向收缩学习各自独立贡献信息。然而，完整模型（Ours）几乎总是优于两个消融变体，证实包含与收缩编码了互补的结构信息。值得注意的是，在GCN骨干下，RePHINE在NCI109上取得79.50%的最高准确率，高于本文的75.87%，表明骨干网络的选择对拓扑描述符的效用有显著影响。

评估边界方面，论文未报告运行时间，尽管声称算法具有线性复杂度，但沙漏持续同调的交错顺序可能导致实际计算开销增加。代码已开源，但超参数设置未详细披露，限制了可复现性。此外，实验未包含大规模图（如OGBN-Products），无法验证方法在大规模数据上的可扩展性。

## 关联研究分析

从问题动机看，本文与RePHINE（Immonen et al., 2023）均旨在增强PH在GNN中的表达力，但路线截然不同。RePHINE通过学习顶点/边滤波函数并添加0D增强来改进前向PH，而本文通过引入反向收缩来扩展PH的拓扑维度。RePHINE在ZINC和MOLHIV上的优势暗示，局部连接信息的显式编码可能比全局拓扑演化历史更直接有效。本文的收缩机制虽在理论上更完备，但在特定分子数据集上未能超越RePHINE，这可能源于分子图中局部化学键结构的重要性高于全局拓扑循环。

从方法设计看，本文与Extended Persistence（Yan et al., 2022）存在理论竞争。Extended Persistence通过前向包含与反向超水平集收缩实现双向描述，而本文使用中间复形收缩。Proposition 5证明两者不等价，本文方法在区分某些嵌入图时更具表达力。然而，Extended Persistence在GNN中已有广泛应用，本文未将其作为基线进行直接对比，仅通过理论证明区分。这一缺失使得读者难以判断在实际GNN任务中，两种双向机制的性能差异是否显著。

## 总结

本文核心矛盾在于前向PH无法捕获拓扑特征的消失过程，导致度量失效与表达力受限。切入点在于引入拓扑收缩作为包含的对偶操作，通过FB-Persistence和Hourglass Persistence构建双向描述符。方法上，定义了中间复形收缩序列，并证明了其表达力严格优于单向PH。实验证明，在PROTEINS上，本文方法（73.51%）优于RePHINE（69.94%），验证了双向机制的有效性。边界在于，在MOLHIV上本文方法（72.34%）低于标准PH（74.34%），且未报告运行时间，沙漏机制的实际计算开销存疑。当图规模扩大至百万级节点时，沙漏持续同调的交错顺序是否会导致计算复杂度从线性退化为多项式级，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17548)