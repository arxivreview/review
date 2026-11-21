# AAAI2026最新论文 ｜XLinear: A Lightweight and Accurate MLP-Based Model for Long-Term Time Series Forecasting with Exogenous Inputs ｜外生变量驱动的高效时序预测

作者：Xinyang Chen、Huidong Jin、Yu Huang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.09237)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.09237)

> 长时程时间序列预测（MTSF）在农业与环境监测场景中常面临内生变量受外生因素单向驱动的问题，传统Transformer架构因二次方复杂度与置换不变性导致效率与精度失衡。现有轻量级模型虽解决了效率瓶颈，却缺乏对外生因果信息的有效融合机制。本文提出XLinear，通过全局令牌（Global Token）与MLP门控机制实现外生信息的高效注入。该模型在12个数据集上验证了其在精度与效率上的双重优势，但高维变量下的可扩展性仍存疑。

## 研究背景

实际预测任务中，目标变量（内生）往往受环境或管理因素（外生）单向影响，如作物生长受气象驱动。这种非对称因果结构要求模型区分内生动态与外生驱动，而传统多变量预测假设变量间双向依赖，导致噪声传播。为处理非平稳性，实例归一化（RevIN）成为标准预处理，但其静态特性难以适应外生变量的动态变化。

主流路线分为两类：Transformer变体（如TimeXer）通过自注意力捕捉长程依赖，但计算开销大且对局部波动敏感；轻量级线性模型（如DLinear）以线性复杂度取胜，却忽略外生变量信息。TimeXer虽引入外生变量，但其Patch机制限制了细粒度时序建模，且Cross-Attention效率低下。本文切入点在于：利用MLP门控替代注意力机制，通过全局令牌作为外生-内生交互枢纽，在保持线性复杂度的同时实现因果信息的高效传递。

## 核心方法

### 方法参照系

本文问题属于“高效架构与线性扩展”类别，但关键差异在于显式建模外生变量。标准流程仅处理内生序列，而本文需同时融合外生驱动信息，且要求计算复杂度保持线性。

### 全局令牌与门控机制

设计动机：解决TimeXer中Cross-Attention效率低且Patch机制丢失局部时序细节的问题。XLinear引入可学习全局令牌 $X_{glob}$，作为内生变量与外生变量交互的枢纽。时间门控模块（TGM）通过MLP提取内生时序特征，生成门控权重 $g_t$：

$$
g_t = \sigma(\text{MLP}_t(X_{1:T}))
$$

其中 $\sigma$ 为Sigmoid函数，$X_{1:T}$ 为RevIN处理后的内生序列。该公式通过Sigmoid约束权重范围，实现时序特征的选择性过滤，抑制噪声。变量门控模块（VGM）利用全局令牌与外生序列交互，提取跨变量依赖：

$$
g_c = \sigma(\text{MLP}_c(\text{Concat}_c(X_{glob}, E_{1:T})))
$$

其中 $E_{1:T}$ 为外生序列，$\text{Concat}_c$ 表示通道维度拼接。该设计将外生信息映射至全局令牌，避免直接交叉注意力的计算开销，同时保持外生-内生因果链的完整性。

### 预测头与多变量扩展

设计动机：解决单变量预测中特征融合不充分的问题。预测头将TGM与VGM输出拼接后映射至目标序列：

$$
\hat{Y}_{T+1:T+S} = \text{Linear}(\text{Concat}_t(g_t \odot X_{1:T}, g_c \odot X_{glob}))
$$

其中 $\odot$ 为逐元素乘法。在多变量预测中，每个变量既作为内生变量预测，又作为外生变量提供信息，TGM与VGM参数共享，确保跨变量依赖的一致性。该机制通过全局令牌解耦时序与变量维度，避免高维空间中的噪声传播。

## 实验评估

实验覆盖7个标准基准（ETT, Weather, Electricity, Traffic）与5个外生变量数据集（Crop, DO, GTD）。基线包括Transformer（TimeXer, iTransformer）、线性模型（DLinear, RLinear）及GNN，但缺失SSM类（Mamba）及最新Mixer类（MSMixer）。

| 数据集 | 预测步长 | XLinear MSE | TimeXer MSE | DLinear MSE |
| :--- | :--- | :--- | :--- | :--- |
| Electricity | 96 | 0.138 | 0.140 | 0.153 |
| Weather | 96 | 0.149 | 0.157 | 0.163 |
| ETTh1 | 96 | 0.369 | 0.382 | 0.375 |
| Traffic | 96 | 0.432 | 0.428 | 0.462 |

XLinear在Electricity、Weather、ETTh1上均优于TimeXer与DLinear，但在Traffic上略逊于TimeXer（0.432 vs 0.428），表明高维变量下全局令牌机制可能失效。

| 配置 | ETTh1 MSE | Weather MSE | GTD_S MSE |
| :--- | :--- | :--- | :--- |
| XLinear (完整) | 0.369 | 0.149 | 0.012 |
| ES (仅内生) | 0.370 | 0.175 | 0.014 |
| GT (仅全局令牌) | 0.382 | 0.153 | 0.012 |

消融实验显示，仅使用全局令牌（GT）在GTD_S上与完整模型持平（0.012），但在ETTh1上劣于完整模型（0.382 vs 0.369），表明外生信息贡献随数据集特性变化。

评估指标包含MSE、MAE、NSE、KGE、MAPE，覆盖精度与物理一致性。代码开源（https://github.com/Zaiwen/XLinear.git），超参数固定（学习率衰减因子0.9，Batch Size 4-256），GPU为V100/RTX 8000。局限：未报告FLOPs与参数量，无法量化效率优势；Traffic数据集结果暴露高维变量下的性能瓶颈。

## 关联研究分析

从问题动机看，XLinear与TimeXer均聚焦外生变量融合，但TimeXer依赖Patch机制与Cross-Attention，导致局部时序细节丢失且计算开销大。XLinear通过MLP门控与全局令牌解耦时序与变量维度，避免了Patch的粒度限制，但牺牲了全局注意力的长程依赖捕捉能力。这一差异源于任务特性：外生变量驱动场景下，局部时序波动比全局依赖更关键，MLP门控的选择性过滤更适配此类数据。

从方法设计看，XLinear与DLinear同属轻量级路线，但DLinear仅处理内生序列，忽略外生信息。XLinear引入全局令牌作为外生-内生交互枢纽，实现了因果信息的高效传递。然而，DLinear在Traffic等强相关数据集上表现更优，表明全局令牌机制在变量间强耦合场景下可能引入噪声。这一冲突暗示：外生变量融合的有效性依赖于变量间的因果结构稀疏性，当外生变量与内生变量存在强双向依赖时，全局令牌机制可能失效。

## 总结

XLinear旨在解决外生变量驱动场景下效率与精度的矛盾，通过全局令牌与MLP门控机制实现外生信息的高效注入。该模型在Electricity与Weather数据集上MSE分别达0.138与0.149，优于TimeXer与DLinear，验证了其在因果信息融合上的有效性。然而，Traffic数据集上XLinear（0.432）略逊于TimeXer（0.428），暴露了高维变量下全局令牌机制的局限性。当变量间存在强双向依赖时，全局令牌的选择性过滤是否仍能有效抑制噪声，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.09237)