# HuggingFace最新推荐论文 ｜GeoPair: Geometry-Preserving Cross-Layer Factorization for Training-Free Transformer Compression ｜跨层几何保持的无训练Transformer压缩

作者：Baher Mohammad、Ammar Ali、Stamatios Lefkimmiatis

论文原文见 [arXiv](https://arxiv.org/abs/2609.25963)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.25963)

> 后训练压缩旨在降低Transformer部署时的内存与计算开销，但现有方法多孤立处理各层权重或依赖启发式分组，忽略了层间激活分布的几何差异，导致高压缩率下精度骤降。GeoPair通过全局最优匹配识别结构兼容的层对，并在各自白化空间内求解共享字典，实现了无微调的亚线性存储缩放。该方法在Llama-3 1B模型40%压缩率下保留了45.6%的平均准确率，显著优于启发式基线，但其优势是否随模型规模扩大而衰减，以及稀疏系数对长序列推理的影响，仍存疑。

## 研究背景

Transformer权重矩阵的压缩通常基于截断奇异值分解（SVD），其数学等价于对权重列空间进行主成分分析（PCA）。然而，SVD假设激活统计是各向同性的，忽略了前向传播中输入依赖的缩放效应。为纠正这一几何失配，数据感知方法引入校准集构建经验Gram矩阵 $G = X^TX$，并通过Cholesky分解 $G_\eta = L^TL$ 获得白化变换 $L$，将压缩目标转化为白化空间下的激活重建误差最小化。

主流压缩路线分为独立因子分解与跨层共享两类。独立方法如SVDLLM逐层优化，虽保留了层特异性但无法利用深层网络中普遍存在的跨层冗余。跨层共享方法如Basis Sharing尝试通过固定相邻层分组学习共享基，但其依赖全局协方差平均，扭曲了层特定的激活几何，且固定相邻规则忽略了非局部结构对齐。CoSpaDI等字典学习方法虽引入了稀疏系数，但仍局限于逐层优化或启发式更新调度。GeoPair的切入点在于：如何在保持各层独立白化几何的前提下，通过优化驱动的全局匹配与精确字典更新，实现跨层共享字典学习。

## 核心方法

### 白化空间下的激活重建框架

标准后训练压缩流程将权重 $W \in \mathbb{R}^{d \times d_{out}}$ 近似为低秩分解，但直接SVD忽略了输入分布。本文沿用数据感知范式，定义校准激活 $X \in \mathbb{R}^{N \times d}$ 并构建正则化Gram矩阵 $G_\eta = X^TX + \eta I$，确保其正定性。压缩目标被形式化为白化空间下的重构误差最小化：

$$ \arg \min_{\hat{W}} \| L(W - \hat{W}) \|_F^2 $$

其中 $L$ 为 $G_\eta$ 的Cholesky因子。这一等价变换表明，最小化白化空间误差等同于在原始空间最小化激活重建误差，从而将压缩问题锚定在功能保真度而非单纯的参数范数上。

### 全局最优层匹配与Sylvester方程求解

针对Basis Sharing固定相邻分组导致的非局部冗余遗漏，GeoPair将层配对建模为最大权匹配问题。定义形状无关的列空间对齐度量 $\delta(W_i, W_j) = \min_{0 \le k \le d_j-d_i} \| L_j W_j[:, k:k+d_i] - L_i W_i \|_F$，利用Edmonds’ Blossom算法求解全局最优配对，替代启发式相邻规则。对于配对层 $W_1, W_2$，共享字典 $D$ 的更新不再依赖协方差平均，而是求解广义Sylvester方程：

$$ D_t = \left( \sum_i L_i^T L_i D_{t-1} C_{i,t-1} C_{i,t-1}^T D_{t-1}^T + \epsilon I \right)^{-1} \left( \sum_i L_i^T L_i W_i C_{i,t-1}^T D_{t-1}^T \right) $$

该闭式解精确尊重了各层独立的白化变换 $L_i$，避免了全局平均对层特定几何的扭曲，确保了共享基在结构兼容性上的最优性。

### HTP稀疏系数优化

为进一步提升压缩率，本文引入硬阈值追踪（HTP）对系数矩阵 $C_i$ 施加 $\ell_0$ 约束。在交替最小化框架中，系数更新通过梯度下降步与支撑集选择迭代完成：

$$ C_{i,t} = \text{HTP}_{k_i} \left( C_{i,t-1} + \mu (L_i^T L_i W_i - L_i^T L_i D_{t-1} C_{i,t-1}) \right) $$

其中 $\mu$ 为步长，$k_i$ 为稀疏预算。HTP与共轭梯度求解器结合，在固定内层迭代次数下实现了非凸子问题的稳定收敛，相比迭代硬阈值（IHT）以更少迭代次数达到更优重构保真度。

## 实验评估

实验在Llama-3 1B/8B、Qwen-3 32B等模型上验证，基准涵盖WikiText-2、MMLU、HellaSwag等。基线覆盖Basis Sharing、CoSpaDI、SVDLLM及剪枝方法（WANDA、LoRAShear），但缺失ROCKET、COMPOT等最新字典学习方法的对比。

| 模型 | 方法 | CR | Avg. Acc. (%) | Lambada PPL |
| :--- | :--- | :--- | :--- | :--- |
| Llama3.2 1B | Baseline | – | 57.61 | 5.73 |
| Llama3.2 1B | Basis Sharing | 0.2 | 33.11 | 239.30 |
| Llama3.2 1B | GeoPair (Full) | 0.2 | 54.09 | 6.74 |
| Llama3 8B | Baseline | – | 70.36 | 3.09 |
| Llama3 8B | Basis Sharing | 0.2 | 53.47 | 14.84 |
| Llama3 8B | GeoPair (Full) | 0.2 | 68.17 | 3.25 |

在20%压缩率下，GeoPair在Llama-3 8B上保留了68.17%的平均准确率，仅比基线低2.19个百分点，而Basis Sharing准确率骤降至53.47%。Lambada困惑度从3.09升至3.25，表明生成质量损失极小。

消融实验显示，Sylvester求解器相比全局白化（GW）带来显著精度恢复，最优分组（OG）进一步提升了零样本性能。HTP稀疏化在CR=0.4时，KS=2.5配置下WikiText-2 PPL为34.26，优于KS=2.0的48.51。校准数据选择中，FineWeb在Lambada PPL上显著优于WikiText-2（21.69 vs 39.02），验证了大规模网络语料对生成质量保持的优势。

评估边界方面，论文未报告置信区间，仅通过5个随机种子验证Llama-1B CR=0.4的稳定性（45.85% ± 0.19%）。代码与超参数在补充材料中提供，实验基于4×A100 GPU，32B模型压缩耗时约19,906秒。缺乏与最新稀疏字典方法的全面对比，且未评估长序列推理场景下的性能衰减。

## 关联研究分析

从问题动机看，GeoPair与Basis Sharing均针对跨层冗余，但根源差异在于对“几何一致性”的定义。Basis Sharing假设相邻层激活分布相似，通过协方差平均强制统一白化空间，这在层间分布漂移大时导致精度崩塌。GeoPair则承认层间几何差异，通过Sylvester方程在各自白化空间内求解共享基，其优势源于对非局部结构对齐的捕捉，而非简单的相邻性。这一设计选择暗示，深层Transformer中结构相似的层可能并非物理相邻，而是功能同构。

从方法设计看，GeoPair与CoSpaDI同属字典学习范式，但优化目标不同。CoSpaDI逐层独立优化字典与系数，缺乏跨层参数共享，导致存储缩放为线性。GeoPair通过全局匹配引入跨层共享，实现了亚线性存储缩放。然而，GeoPair的Blossom算法计算复杂度随层数增长，在超大规模模型中可能成为瓶颈。此外，GeoPair的HTP稀疏化是后处理步骤，而CoSpaDI的稀疏性内嵌于字典学习过程，两者在稀疏预算分配机制上存在本质差异，前者依赖固定KS比率，后者可能更灵活。

## 总结

GeoPair旨在解决后训练压缩中层间激活几何不一致导致的精度损失问题。现有方法如Basis Sharing依赖启发式相邻分组与协方差平均，扭曲了层特定几何；CoSpaDI虽引入稀疏性但缺乏跨层共享。GeoPair通过全局最优匹配识别结构兼容层对，并利用Sylvester方程在独立白化空间内求解共享字典，实现了无微调的精确压缩。实验证明，在Llama-3 8B 20%压缩率下，其平均准确率保留率达68.17%，显著优于Basis Sharing的53.47%。然而，论文未评估Blossom算法在超大规模模型中的计算开销，且HTP稀疏化对长序列推理的影响未知。当模型规模扩展至百亿参数时，全局匹配的计算成本是否会抵消压缩带来的推理加速，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.25963)