# PR-XAI：将Transformer建模为分层有向图，利用PageRank算法捕捉Token间间接依赖，解决长文本归因失效问题

作者：Behrooz Azarkhalili、Linyi Li、Maxwell Libbrecht

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6b462b79d451)

> 现有Transformer归因方法多将注意力权重直接作为重要性分数，或仅做单层聚合，忽略了跨层信息流动与Token间的间接依赖效应，导致长文本解释失效。本文切入点在于将Transformer架构显式建模为分层有向图，利用PageRank算法在图上进行重要性传播，从而捕捉直接和间接的Token贡献。具体做法是构造由注意力权重及其梯度张量加权的转移矩阵，求解特征向量得到Token级归因分数。该方法在长文本数据集上显著优于基线，但其图结构假设是否完全匹配Transformer前向传播的确定性机制，仍存疑。

## 研究背景

Transformer模型中，信息通过多头自注意力机制在Token间流动，注意力权重$A$反映了前向传播中Token间的直接关联。然而，仅关注单层注意力无法解释深层网络中信息如何跨层累积并影响最终预测，这被称为“混合效应”（mixing effect）。为量化这种跨层依赖，特征归因方法需超越局部梯度或单层注意力聚合，建立能反映全局信息流路径的度量框架。

Transformer解释领域的主流路线分为两类：基于注意力的方法（如Rollout）直接聚合各层注意力矩阵，计算高效但忽略前馈网络及梯度信号，导致解释与模型实际决策逻辑脱节；基于梯度的方法（如Integrated Gradients, IG）通过路径积分满足完备性公理，但通常将Transformer视为通用神经网络，未利用其分层结构特性，且在长序列中梯度噪声累积严重。现有方法共同瓶颈在于无法同时兼顾架构感知（architectural awareness）与长程依赖建模，导致在IMDB等长文本数据集上解释质量显著下降。

本文针对上述瓶颈，提出PR-XAI框架。其核心假设是：Transformer中的信息流动可被建模为分层有向图上的随机游走，其中边权由注意力权重及其梯度共同决定。通过引入PageRank算法，该方法能够递归地传播重要性分数，从而捕捉Token间的间接依赖效应，解决传统方法在长文本中解释碎片化的问题。

## 核心方法

### 方法参照系

本文问题属于“架构感知归因”范畴，与标准梯度类方法（如IG）的关键差异在于：IG在输入-输出空间进行路径积分，而PR-XAI在Transformer内部的分层Token图上执行重要性传播。标准流程通常将Transformer视为黑盒或通用DNN，而本文显式利用其$l$层注意力结构构建图拓扑。

### 信息张量构造

设计动机在于解决纯注意力方法忽略梯度信号、纯梯度方法忽略注意力结构的双重缺陷。本文定义信息张量$\bar{A} \in \mathbb{R}^{l \times t \times t}$，其中$l$为层数，$t$为序列长度。对于PR-AG变体，采用引导反向传播思想，计算注意力权重$A$与其梯度$\nabla A$的逐元素乘积并取正部：

$$ \bar{A} := E_h(\lfloor A \odot \nabla A \rfloor^+) $$

该公式物理含义为：仅当注意力权重高且其对输出的敏感度（梯度）也为正时，才认为该Token对预测有正向贡献。$E_h$表示对多头维度取平均，$\lfloor \cdot \rfloor^+ = \max(\cdot, 0)$确保只保留正向影响，这与Grad-CAM的原理一致，但应用于Token级而非像素级。

### 分层转移矩阵与PageRank求解

设计动机在于解决单层聚合方法无法捕捉跨层间接依赖的问题。本文构建一个维度为$(t \cdot (l+1)) \times (t \cdot (l+1))$的分层有向图，节点$v_{\ell, i}$表示第$\ell$层的第$i$个Token。边权由信息张量$\bar{A}$决定，形成列随机转移矩阵$P$。随后，求解个性化PageRank特征向量问题：

$$ Mx = x, \quad M = \alpha P + (1-\alpha)ve^T $$

其中$\alpha=0.85$为阻尼系数，$v$为个性化向量。该公式的物理含义是：Token的重要性不仅取决于其直接接收到的注意力信号，还取决于其上游节点（前层Token）的重要性传递。通过幂迭代求解，$x$即为最终的Token级归因分数，其收敛性由Theorem 4.1保证，收敛率为$\alpha$。

## 实验评估

实验在SST2、IMDB、Amazon、Yelp、AG News五个文本分类数据集上进行，使用BERT、DistilBERT、RoBERTa三种架构。基线覆盖注意力类（RawAtt, Rollout）、梯度类（Grads, IG, CAT）、混合类（AttCAT）及博弈论类（LIME, KernelShap）。值得注意的是，基线中未包含最新的2025-2026年视觉归因方法（因领域不同），也未包含针对Transformer的特定SHAP变体，但覆盖了主流NLP归因基准。

| 方法 | IMDB AOPC (Top) | IMDB LOdds (Top) | Amazon AOPC (Top) | Amazon LOdds (Top) |
|---|---|---|---|---|
| PR-AG | 0.380* | -1.725* | 0.443* | -2.110* |
| AttCAT | 0.371 | -1.642 | 0.427 | -2.041 |
| KernelShap | 0.367 | -1.423 | 0.374 | -1.717 |
| IG | 0.350 | -1.443 | 0.434 | -2.024 |

PR-AG在IMDB和Amazon数据集的AOPC（Area Under the Precision-Recall Curve for Perturbation）和LOdds（Log-Odds）指标上均显著优于AttCAT和KernelShap，尤其在Amazon数据集上，PR-AG的AOPC达到0.443，较AttCAT提升0.016。*表示在ASO检验下具有统计显著性。

消融实验显示，PR-AG（注意力×梯度）优于PR-A（仅注意力）和PR-G（仅梯度），验证了混合信号的必要性。在长文本分层分析中，PR-AG在Q100（最长序列）子集上的AOPC保持最高且方差最小，而RawAtt在长序列上性能急剧下降。OTF（Original Text Focus）实验表明，当插入中性前缀/后缀时，PR-AG在Extended Context下的OTF分数为0.71（k=10%），高于AttCAT的0.68和RawAtt的0.61，证明其在长程依赖建模上的优势。

评估边界方面，论文未报告计算效率的具体数值（仅给出复杂度$O(nl^2t^2)$），未提供代码仓库链接，且未讨论基线选择（如零向量掩码）对结果的敏感性。此外，实验仅覆盖编码器架构，未验证在解码器或混合架构上的有效性。

## 关联研究分析

从方法设计看，PR-XAI与Attention Rollout的核心差异在于图结构的构建方式。Rollout直接对单层注意力矩阵进行幂运算或求和，假设信息流是各层独立的线性叠加；而PR-XAI构建分层图，显式引入层间边，允许重要性分数在层间递归传播。这一差异源于对Transformer信息流动机制的不同理解：Rollout假设注意力是静态的权重分布，而PR-XAI假设注意力是动态的图结构，其重要性受上游节点影响。根源在于Rollout未考虑前馈网络和层间交互，而PR-XAI通过信息张量$\bar{A}$间接编码了这些交互。

从问题动机看，PR-XAI与Integrated Gradients（IG）均追求忠实度，但路径不同。IG在输入-输出空间进行线性插值积分，假设模型行为在路径上是平滑的；而PR-XAI在内部表示空间进行图遍历，假设信息流遵循图拓扑。IG在长文本中失效的原因可能是梯度噪声在长路径上累积，而PR-XAI通过PageRank的阻尼机制（$\alpha=0.85$）抑制了噪声传播。然而，PR-XAI的随机游走假设是否忽略了Transformer前向传播的确定性，论文未给出回答。

## 总结

本文要解决的核心矛盾是Transformer归因方法在长文本中解释质量下降的问题，根源在于现有方法未能捕捉跨层Token间的间接依赖效应。本文抓住的切入点是Transformer的分层图结构，通过构造由注意力及其梯度加权的转移矩阵，利用PageRank算法进行重要性传播，从而在架构感知的基础上实现长程依赖建模。实验证明，PR-AG在IMDB和Amazon数据集上的AOPC分别达到0.380和0.443，显著优于AttCAT和KernelShap。本文的边界在于仅验证了编码器架构，且未报告计算效率的具体数值，其图结构假设是否完全匹配Transformer前向传播的确定性机制，仍存疑。当序列长度进一步增加至8k tokens时，PageRank的迭代次数是否会导致计算成本不可接受，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_6b462b79d451)