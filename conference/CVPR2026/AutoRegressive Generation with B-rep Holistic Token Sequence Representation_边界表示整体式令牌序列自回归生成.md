# CVPR2026最新论文 ｜AutoRegressive Generation with B-rep Holistic Token Sequence Representation ｜边界表示整体式令牌序列自回归生成

研究机构：西北工业大学、新加坡国立大学

作者：Jiahao Li、Yunpeng Bai、Yongkang Dai 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.16771)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.16771)

> B-Rep 生成长期受困于几何与拓扑的解耦建模，导致序列误差累积与表示碎片化。现有方法或采用多阶段流水线，或依赖图结构，均难以直接适配 Transformer 的序列处理范式。BrepARG 提出整体式令牌序列表示，将 B-Rep 的几何与拓扑编码为单一令牌流，通过自回归模型联合学习其分布。该框架在有效性指标上显著超越基线，但其固定量化步长对复杂曲面的拟合能力存疑。

## 研究背景

B-Rep 模型由参数化面、边及顶点构成，其核心难点在于离散拓扑连接与连续几何参数的异质性耦合。这种异质性使得直接将其编码为深度学习可处理的序列变得困难，传统方法往往将几何与拓扑分离处理，导致信息碎片化。

B-Rep 生成旨在从数据中学习并复现设计逻辑，但现有主流路线存在明显瓶颈。多阶段方法如 SolidGen 和 DTGBrepGen 分别预测几何与拓扑，误差在阶段间累积，且难以保证最终模型的水密性；图扩散方法如 BrepGen 虽能处理拓扑，但图结构限制了 Transformer 等高效序列架构的应用。BrepARG 的切入点在于打破几何与拓扑的解耦，通过整体式令牌序列表示，将 B-Rep 转化为单一令牌流，使自回归模型能在单次前向传播中联合建模几何形状与拓扑连接，从而消除多阶段误差并提升生成效率。

## 核心方法

### 方法参照系

B-Rep 生成通常被建模为条件序列预测或图生成任务。标准流程涉及几何离散化、拓扑编码及生成模型训练。本文的关键差异在于摒弃了分阶段或图结构，采用单一令牌序列直接建模几何与拓扑的联合分布，适配自回归 Transformer 架构。

### 整体式令牌化

几何与拓扑的离散化是序列生成的前提。传统方法使用 VQ-VAE 量化几何特征，但包围盒的位置信息若用单一码字表示，VQ-VAE 会退化为 K-means 聚类，导致精度不足。BrepARG 引入均匀标量量化（Uniform Scalar Quantization, USQ）处理位置信息，将包围盒的六个坐标独立量化为离散索引。对于几何特征，采用共享 VQ-VAE 码本，通过最近邻搜索将 UV 采样特征映射为几何令牌。拓扑信息通过面索引令牌显式编码，每个边令牌关联两个面索引，明确表达邻接关系。

$$
k_j = \text{round}\left( \frac{\tilde{b}_j \cdot (L-1)}{1} \right), \quad \hat{b}_j = \frac{k_j}{L-1}
$$

该公式将归一化后的坐标 $\tilde{b}_j$ 映射到 $L$ 级均匀网格，实现位置信息的无损离散化，避免了 VQ-VAE 在位置量化上的退化问题。

### 拓扑感知序列构建

令牌序列的顺序直接影响自回归模型的注意力效率。随机排序会破坏 B-Rep 的局部结构，导致长距离依赖。BrepARG 设计拓扑感知排序策略：面块通过深度优先搜索（DFS）排序，优先访问低度邻居，使拓扑相邻的面在序列中邻近；边块通过最大相邻面索引升序（MAX-IDX-A）排序，确保边靠近其关联面。这种排序缩短了注意力跨度，缓解了长序列依赖问题。

$$
\mathcal{S} = \text{START} \oplus \mathcal{S}_f \oplus \text{SEP} \oplus \mathcal{S}_e \oplus \text{END}
$$

该公式定义了最终序列结构，$\mathcal{S}_f$ 和 $\mathcal{S}_e$ 分别为排序后的面块和边块序列，通过分隔符连接，形成完整的整体式令牌序列。

## 实验评估

实验在 DeepCAD 和 ABC 数据集上进行，基线包括 BrepGen、DTGBrepGen 和 BrepDiff。BrepARG 在 DeepCAD 上的 Validity 达到 87.60%，显著高于 DTGBrepGen 的 68.23% 和 BrepDiff 的 62.83%；在 ABC 上，其 Validity 为 67.54%，优于 DTGBrepGen 的 57.59%。

| 方法 | DeepCAD Validity (%) | ABC Validity (%) |
| :--- | :--- | :--- |
| BrepGen | 58.10 | - |
| DTGBrepGen | 68.23 | 57.59 |
| BrepDiff | 62.83 | - |
| BrepARG | 87.60 | 67.54 |

消融实验显示，拓扑感知排序对 Validity 提升显著。随机排序（RAND）的 Validity 为 85.43%，而 BrepARG 的排序策略达到 87.60%。面块排序中，BFS 策略的 Validity 为 85.94%，低于 BrepARG 的 87.60%，表明 DFS 优先低度邻居的策略更优。

| 排序策略 | Validity (%) |
| :--- | :--- |
| RAND | 85.43 |
| BFS | 85.94 |
| BrepARG (Ours) | 87.60 |

评估边界方面，论文未报告置信区间，且未与同期工作 AutoBrep 和 BrepGPT 进行直接对比。代码已开源，训练使用 4 块 NVIDIA H20 GPU，推理在单块 RTX 4090 上耗时约 1.5 秒，效率较高。

## 关联研究分析

从方法设计看，BrepARG 与 AutoBrep 均采用自回归序列生成，但序列构建策略不同。AutoBrep 使用专用拓扑令牌，但序列构建较为简单；BrepARG 引入拓扑感知排序，通过 DFS 和 MAX-IDX-A 优化序列顺序，提升了注意力效率。这一差异源于对序列长度与局部结构关系的深入理解，BrepARG 更关注长序列依赖的缓解。

从问题动机看，BrepARG 与 BrepGPT 均使用 VQ-VAE 进行几何离散化，但 BrepGPT 采用顶点中心令牌化以压缩序列长度，而 BrepARG 采用面/边中心令牌化并引入 USQ 处理位置。BrepGPT 的局限性在于码本大小对多样性的影响，而 BrepARG 的 USQ 虽提升了位置精度，但固定量化步长可能限制对复杂自由曲面的拟合能力。这种设计选择反映了在序列长度与几何精度之间的不同权衡。

## 总结

BrepARG 解决了 B-Rep 生成中几何与拓扑解耦导致的误差累积问题，通过整体式令牌序列表示和拓扑感知排序，实现了高效的自回归生成。实验显示，其在 DeepCAD 上的 Validity 达到 87.60%，显著优于基线。然而，USQ 的固定量化步长可能限制对复杂曲面的拟合能力，且未与同期工作 AutoBrep 和 BrepGPT 进行直接对比。当面对高度不规则拓扑或复杂自由曲面时，USQ 的量化精度是否足以保证生成模型的水密性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.16771)