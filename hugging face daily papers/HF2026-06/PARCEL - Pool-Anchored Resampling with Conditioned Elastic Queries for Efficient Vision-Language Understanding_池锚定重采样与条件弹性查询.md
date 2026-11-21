# HuggingFace最新推荐论文 ｜PARCEL: Pool-Anchored Resampling with Conditioned Elastic Queries for Efficient Vision-Language Understanding ｜池锚定重采样与条件弹性查询

研究机构：德国马克斯·普朗克信息学研究所、德国慕尼黑工业大学

作者：Selim Kuzucu、Alessio Tonioni、Vasile Lup 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.30126)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.30126)

> 视觉语言模型（Large Vision-Language Models, LVLMs）在高分辨率输入下面临二次方注意力计算瓶颈，现有静态压缩方法迫使部署者在效率与精度间做一次性取舍。Matryoshka范式虽实现“一次训练多预算部署”，但刚性空间池化引发频谱混叠，纯查询重采样则丢失空间锚定，导致极端压缩下性能骤降。PARCEL通过池化锚点与条件查询的分工机制，在27个基准上优化了性能-效率帕累托前沿。该架构在空间定位任务上优势显著，但其对训练成本的高依赖及未覆盖的量化协同效应，限制了其作为通用压缩方案的普适性。

## 研究背景

LVLMs将视觉输入映射为密集Token序列，其自注意力计算成本随Token数量呈二次方增长。为降低推理开销，研究界引入了弹性推理（Elastic Inference）范式，旨在通过单次训练支持多种视觉Token预算（如16至256个），实现“一次训练，随处部署”。这一范式依赖于Matryoshka表示学习（Matryoshka Representation Learning, MRL）思想，即通过嵌套结构在单一模型中编码多粒度信息，使模型在截断序列时仍能保持功能完整性。

当前弹性压缩主要分化为两条路线：基于刚性空间下采样的Matryoshka Multimodal Models（M3）和基于非局部查询重采样的Matryoshka Query Transformer（MQT）。M3通过多级平均池化构建嵌套Token结构，但其刚性下采样行为类似不完美低通滤波器，在高频语义细节（如图表推理、文本识别）上产生频谱混叠。MQT利用嵌套Dropout的查询Token替代显式空间网格，虽具备弹性，却牺牲了空间对齐关系，导致密集定位能力退化。PARCEL的切入点在于识别这两种机制在频域上的互补缺陷，提出通过架构层面的“分工”而非单一机制的优化来解决压缩中的表示冲突。

## 核心方法

### 方法参照系

本文问题属于Pre-LLM视觉连接器层的Token压缩，与Training-free剪枝（如FastV）的关键差异在于：PARCEL不依赖推理时的启发式评分，而是通过端到端训练的混合架构，在视觉编码器后、语言模型前完成确定性空间锚定与可学习语义探索的联合优化，以支持推理时的动态预算切换。

### 池化锚定与频谱解耦

刚性池化在压缩时导致频谱泄漏，模糊了高频细节。PARCEL引入“2D Anchor”池化Token $P \in \mathbb{R}^{N_p \times D}$，通过预算感知的平均池化（如2×2或4×4）提取低频几何布局。

$$
P = \text{AvgPool}(X_v, k)
$$

其中 $X_v$ 为视觉编码器输出，$k$ 为池化核大小。这一设计动机在于：显式保留低频空间结构，避免纯查询机制中空间锚点的缺失，为后续高频细节恢复提供稳定的几何基底。

### 池条件查询重采样（PCQR）

纯查询Token需同时编码布局与细节，负担过重。PARCEL引入Pool-Conditioned Query Resampling（PCQR），使查询Token $Q_{IN}$ 先与池化锚点 $P$ 进行自注意力交互，再与原始视觉特征 $X_v$ 进行交叉注意力。

$$
Q_{SE} = \text{CrossAttn}(Q_{PA}, X_v, X_v)
$$

其中 $Q_{PA}$ 是 $Q_{IN}$ 与 $P$ 自注意力后的池感知查询Token。该公式的物理含义是：查询Token在获取粗粒度空间布局信息后，作为“语义探索者”从原始特征中检索互补的高频细节，而非重复编码已存在的低频信息。这种条件化机制解决了MQT中查询Token缺乏空间引导导致的定位模糊问题，实现了频谱上的解耦。

## 实验评估

实验基于PaliGemma-2 3B骨干，在27个基准上评估，对比M3和MQT。基线覆盖Matryoshka范式的两种主流架构，但未包含Training-free方法（如VisionZip），因协议不同（训练式vs免训练）无法直接对比。

| 基准组 | 预算 | M3 | MQT | PARCEL |
|---|---|---|---|---|
| Video (Mean Retention) | 256 | 92.9% | 94.4% | 98.0% |
| Video (Mean Retention) | 64 | 92.5% | 93.5% | 97.9% |
| RefCOCO (Mean Retention) | 256 | 86.4% | 90.6% | 90.8% |
| RefCOCO (Mean Retention) | 64 | 84.9% | 90.8% | 90.8% |
| Resolution-Sensitive (Mean Retention) | 256 | 94.8% | 96.3% | 96.7% |
| Resolution-Sensitive (Mean Retention) | 64 | 92.3% | 94.1% | 95.7% |

PARCEL在视频理解和密集定位任务上优势显著，尤其在64 Token预算下，RefCOCO保留率90.8%高于MQT的90.8%（持平）和M3的84.9%。在分辨率敏感任务上，PARCEL在64 Token下达到95.7%，优于MQT的94.1%和M3的92.3%。

消融实验显示，固定路由策略（如仅用4×4池化）在16 Token下性能下降至83.1%，而动态路由保持88.3%，证明预算感知路由对极端压缩的必要性。移除Query-Pool自注意力（仅用ViT交叉注意力）导致256 Token下保留率从95.6%降至95.2%，表明条件化步骤对高频细节恢复有边际贡献。

评估边界方面，论文未报告计算延迟与内存占用的实测数据，仅提供理论FLOPs和KV缓存估算。高斯分辨率（448×448）实验仅报告单种子结果，缺乏统计显著性检验。代码未公开，且训练需256个TPUv4芯片，复现门槛极高。

## 关联研究分析

从问题动机看，PARCEL与Training-free剪枝方法（如FastV、VisionZip）存在根本差异。后者依赖推理时的注意力分数或显著性评分进行后处理剪枝，属于“评分-选择”范式，无法支持多预算弹性部署。PARCEL通过端到端训练的嵌套结构，将预算选择内化为架构特性，解决了Training-free方法在动态效率-性能权衡中缺乏梯度对齐学习的问题。然而，PARCEL的高训练成本（100M样本中间预训练）是其相对于Training-free方法的主要劣势，后者即插即用，部署成本低。

从方法设计看，PARCEL与VisionSelector等端到端学习剪枝方法同属学习式路线，但设计哲学不同。VisionSelector侧重可学习评分器的重要性评估，属于“决策优化”；PARCEL侧重空间池化与查询重采样的架构分工，属于“表示解耦”。PARCEL的PCQR机制通过显式条件化查询Token，避免了VisionSelector中可微分Top-K选择的数值不稳定性，但引入了额外的注意力计算开销。这种架构级分工是否比评分器级优化更具泛化性，论文未提供跨模型或跨任务的零样本泛化证据。

## 总结

PARCEL旨在解决弹性视觉Token压缩中空间锚定与高频细节保留的结构性冲突。现有M3和MQT分别因频谱混叠和空间缺失而在极端压缩下失效，PARCEL通过池化锚点与条件查询的分工机制，在27个基准上优化了帕累托前沿，在64 Token下RefCOCO保留率达90.8%，视频理解达97.9%。其边界在于：高训练成本限制了部署灵活性，且未验证与量化等加速技术的协同效应。当视觉Token预算低于16时，池化锚点的空间分辨率是否足以支撑密集定位任务，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.30126)