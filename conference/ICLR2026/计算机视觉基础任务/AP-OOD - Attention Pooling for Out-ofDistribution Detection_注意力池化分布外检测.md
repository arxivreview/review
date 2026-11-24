# ICLR2026最新论文 ｜AP-OOD: Attention Pooling for Out-ofDistribution Detection ｜注意力池化分布外检测

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_22487125)

> 导读 自然语言模型在生成任务中常因输入偏离训练分布而产生高置信度幻觉，传统基于分类头置信度的分布外检测（OOD Detection, OOD）方法无法直接应用于无分类头的自回归语言模型。现有基于Token嵌入的均值池化策略会抹平序列内部的异常结构，导致近邻分布外样本难以区分。本文提出AP-OOD，通过可学习的注意力池化机制替代均值聚合，将Mahalanobis距离的方向分解与Token级信息保留相结合，实现无监督与半监督场景下的灵活检测。该方法在文本摘要任务上将无监督FPR95从27.84%降至4.67%，但其性能增益是否源于对ID分布的过拟合，以及在高维嵌入空间中的泛化边界，仍需进一步审视。

## 研究背景

当自回归语言模型面对训练域之外的输入时，其内部Token嵌入序列的统计特性会发生偏移，但传统的序列级均值池化会将这种局部异常平滑掉。这一现象源于均值聚合对序列内部结构的丢弃：若ID序列的Token分布在特征空间的对角线上，而OOD序列的Token分布在反对角线上，两者的均值可能都集中在原点附近，导致基于均值的Mahalanobis距离无法区分二者。为解决这一问题，需要一种能够保留Token级空间关系的聚合机制，同时保持与经典距离度量框架的兼容性。

现有文本OOD检测主要依赖两类信号：基于预测的不确定性（如困惑度、熵）和基于嵌入的距离度量（如Mahalanobis、KNN）。预测类方法在翻译等低随机性任务中表现尚可，但在摘要等高随机性任务中因随机性不确定性（Aleatoric Uncertainty）干扰而失效；嵌入类方法虽能捕捉分布偏移，但Ren et al. (2023)提出的均值池化策略在处理近邻OOD时存在结构性盲区。本文的切入点在于，将注意力机制引入Mahalanobis距离的方向分解中，使检测器能够学习哪些Token方向对区分ID与OOD最为敏感，从而在不依赖大规模辅助数据的情况下提升边界区分度。

## 核心方法

### 方法参照系

本文问题属于基于嵌入空间的OOD检测，标准流程为：提取Token嵌入序列 $\mathbf{Z} \in \mathbb{R}^{D \times S}$，计算序列均值 $\bar{\mathbf{z}}$，拟合ID高斯分布 $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$，计算Mahalanobis距离 $d^2_{Maha}(\bar{\mathbf{z}}, \boldsymbol{\mu})$ 作为评分。本文的关键差异在于，用可学习的注意力池化替代均值池化，并将协方差矩阵 $\boldsymbol{\Sigma}^{-1}$ 分解为可学习的方向基向量，使聚合过程本身成为可优化的检测组件。

### 注意力池化与方向分解

传统Mahalanobis距离中，$\boldsymbol{\Sigma}^{-1}$ 是固定拟合的，无法适应Token序列的动态结构。本文将其分解为 $M$ 个可学习权重向量 $\mathbf{w}_j$，并通过注意力池化计算每个方向的局部原型：

$$
\boldsymbol{\mu}_j = \mathbf{Z} \text{softmax}(\beta \mathbf{Z}^T \mathbf{w}_j)
$$

其中 $\beta$ 为逆温度，控制注意力分布的尖锐程度。这一设计解决了均值池化在ID与OOD序列均值重叠时的失效问题：通过 $\mathbf{w}_j$ 的选择，检测器能够聚焦于序列中偏离ID分布的特定Token子集，而非被整体均值掩盖。

### 多查询扩展与半监督损失

为增强表达能力，本文将单查询扩展为 $T$ 个查询组成的矩阵 $\mathbf{W}_j \in \mathbb{R}^{D \times T}$，利用矩阵值Softmax将序列 $\mathbf{Z}$ 变换为 $\bar{\mathbf{Z}} \in \mathbb{R}^{D \times T}$，并通过Frobenius内积 $\langle \mathbf{W}_j, \bar{\mathbf{Z}} \rangle_F$ 计算评分。在无监督场景下，损失函数为ID样本距离的均值加上正则项 $-\log \|\mathbf{W}_j\|_F^2$；在半监督场景下，引入辅助数据（AUX）的二元交叉熵损失，通过 $\lambda$ 平滑过渡：

$$
\mathcal{L}_{SUP} = \frac{1}{N} \sum_{i=1}^N d^2(\mathbf{Z}_i, \tilde{\mathbf{Z}}) + \lambda \frac{1}{N'} \sum_{i=N+1}^{N+N'} \log(1 - e^{-d^2(\mathbf{Z}_i, \tilde{\mathbf{Z}})})
$$

这一设计使AP-OOD能够利用少量AUX数据优化ID-OOD边界，而无需像Outlier Exposure那样依赖大规模合成异常值。

## 实验评估

实验在PEGASUS-LARGE（XSUM摘要）和Transformer-base（WMT15英法翻译）上进行，基线覆盖Mahalanobis、KNN、Deep SVDD、困惑度、熵及MSP/EBO（仅音频任务）。在XSUM无监督输入OOD检测中，AP-OOD在CNN/DM、Newsroom、Reddit、Samsum上的平均FPR95为4.67%，显著优于Deep SVDD的27.84%和Mahalanobis的39.69%。

| 数据集 | 方法 | AUROC (%) | FPR95 (%) |
| :--- | :--- | :--- | :--- |
| CNN/DM | Deep SVDD | 75.75±0.86 | 74.20±1.60 |
| CNN/DM | AP-OOD | 97.48±0.32 | 12.88±1.68 |
| Newsroom | Deep SVDD | 91.36±0.38 | 36.05±1.71 |
| Newsroom | AP-OOD | 98.54±0.10 | 5.78±0.58 |
| Reddit | Deep SVDD | 99.71±0.08 | 0.39±0.23 |
| Reddit | AP-OOD | 99.88±0.05 | 0.00±0.00 |
| Samsum | Deep SVDD | 99.57±0.08 | 0.72±0.28 |
| Samsum | AP-OOD | 99.76±0.05 | 0.00±0.01 |

消融实验显示，$\beta=0.5$ 时输入OOD平均FPR95最低（3.96%），而 $\beta=0$ 时性能最差（58.64%），表明注意力尖锐度对检测至关重要。在M和T的扩展中，$M=12, T=2$ 时输入OOD平均FPR95达到3.61%，优于 $M=1024, T=1$ 的5.72%，提示过大的参数空间可能引入过拟合。

评估协议采用5次独立数据划分和训练运行的标准差，代码已开源。局限在于：未报告计算效率的完整对比（仅给出单批次推理时间6.58ms vs Mahalanobis 0.52ms），且AUX数据规模对性能的影响在翻译任务中未充分探索。

## 关联研究分析

从问题动机看，AP-OOD与Ren et al. (2023)的均值池化Mahalanobis方法直接竞争，但后者在CNN/DM等近邻OOD上FPR95高达92.16%，而AP-OOD降至12.88%。这一差异源于注意力池化对Token级异常的保留能力，而非简单的距离度量改进。与Deep SVDD相比，AP-OOD在半监督场景下无需预训练异常值，但其在完全无监督时的性能增益（FPR95从27.84%到4.67%）是否部分依赖于XSUM数据本身的分布特性，论文未通过跨域实验验证。

从方法设计看，AP-OOD的矩阵值Softmax与Ramsauer et al. (2021)的Hopfield网络记忆更新机制类似，但后者用于分类而非检测。AP-OOD将这一机制嵌入Mahalanobis框架，使其在 $\beta=0, M=D$ 时退化为经典Mahalanobis，保证了理论连续性。然而，与视觉领域的GEODE等基于神经坍缩的几何方法相比，AP-OOD未显式建模特征空间的流形结构，其检测信号更依赖于注意力权重的学习而非几何不变性。这种差异是否导致AP-OOD在极端长尾分布下泛化能力不足，论文未提供证据。

## 总结

本文要解决的核心矛盾是自回归语言模型缺乏分类头，导致传统置信度OOD检测失效，而均值池化又抹平了Token级异常信息。AP-OOD通过可学习的注意力池化与Mahalanobis方向分解的结合，使检测器能够自适应地聚焦于序列中的异常Token子集，从而在无监督场景下将XSUM摘要任务的FPR95从27.84%降至4.67%。这一改进验证了Token级信息保留对近邻OOD检测的关键作用，但实验仅覆盖摘要和翻译两类任务，且AUX数据规模对性能的影响在翻译任务中未充分探索。当支持集从100,000个ID样本扩展到更大规模时，注意力池化的参数空间是否会导致过拟合，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_22487125)