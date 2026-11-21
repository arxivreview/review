# WACV2026最新论文 ｜Semantic Map Guided Bird's-Eye View Learning for Online HD Map Construction ｜语义地图引导的鸟瞰图学习

研究机构：美国雪城大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0dca2a6515ac)

> 在线高精地图构建依赖鸟瞰图（Bird's-Eye View, BEV）特征作为图像与矢量地图间的桥梁，但现有端到端模型仅通过最终地图重建间接优化BEV特征，导致中间表征与真值地图结构存在系统性错位。本文指出这种间接监督是精度瓶颈的根源，提出在训练阶段引入真值语义与空间信息直接对齐BEV特征的语义地图引导（Semantic Map Guidance, SMG）模块。该模块通过对比学习损失将真值嵌入与BEV局部特征拉近，推理时完全丢弃，不增加计算开销。SMG在多个基线上带来1.3%至2.6%的mAP提升，验证了直接监督的有效性，但其性能增益依赖于真值标签的可用性，且未解决长时序稳定性问题。

## 研究背景

多视角相机图像经骨干网络提取特征后，需通过BEV编码器（如BEVFormer或BEVPool v2）融合为统一的顶视图特征图 $X_{bev} \in \mathbb{R}^{H \times W \times C}$。该特征图随后输入Transformer解码器，通过查询机制预测车道线、人行横道等矢量地图元素。在这一流程中，BEV特征的质量直接决定矢量预测的几何精度，然而其优化信号仅来自最终的点位置回归与分类损失，缺乏对BEV特征本身与真值地图结构对齐的直接约束。

在线建图领域的主流路线已从栅格化语义分割转向端到端矢量预测，MapTR等架构确立了DETR-like解码范式。然而，这些方法在复杂场景下仍面临边界模糊与类别混淆问题，根源在于BEV特征在编码阶段未显式学习真值语义分布。现有改进多聚焦于解码器结构或时序记忆机制，而忽视了BEV编码阶段的监督缺失。本文切入点在于：若BEV特征在训练时能直接感知真值地图的语义与空间布局，其表征能力将显著增强，从而提升下游矢量解码的精度。

## 核心方法

### 方法参照系

本文基于MapTR架构，其标准流程为：多视角图像经BEV编码器生成 $X_{bev}$，解码器查询 $q_{dec}$ 从中提取信息，预测头输出矢量地图。该流程中，BEV编码器仅通过反向传播接收来自最终地图损失的梯度，属于间接监督。本文的关键差异在于：在BEV编码后、解码前，插入一个仅训练时生效的SMG模块，利用真值标签直接约束 $X_{bev}$ 的语义与空间分布。

### 真值语义特征提取与空间裁剪

SMG模块首先将第 $i$ 个地图实例的真值语义信息 $c_i$ 输入语义特征提取器（Semantic Feature Extractor, SFE），生成与BEV特征维度一致的嵌入 $g_i$：

$$ g_i = \text{SFE}(c_i) $$

该公式将离散类别标签映射为连续特征向量，使真值语义可参与后续对比学习。为对齐空间位置，SMG根据真值点集计算边界框，从 $X_{bev}$ 中裁剪对应区域并池化，得到实例级BEV特征 $o_i$：

$$ o_i = \text{Pool}(\text{Crop}(X_{bev}, b_i)) $$

此设计解决了此前方法中BEV特征与真值地图元素在空间上错位的问题，通过显式裁剪确保语义特征与空间区域严格对应。

### 对比学习对齐损失

SMG采用对比学习损失 $L_{SMG}$ 拉近 $g_i$ 与 $o_i$ 的距离，同时推远负样本：

$$ L_{SMG} = -\frac{1}{N} \sum_{i=1}^{N} \log \frac{\exp(\text{sim}(g_i, o_i)/\tau)}{\sum_{j=1}^{N} \exp(\text{sim}(g_i, o_j)/\tau)} - \frac{1}{N} \sum_{i=1}^{N} \log \frac{\exp(\text{sim}(o_i, g_i)/\tau)}{\sum_{j=1}^{N} \exp(\text{sim}(o_i, g_j)/\tau)} $$

其中 $\text{sim}(\cdot, \cdot)$ 为余弦相似度，$\tau$ 为温度系数。该损失在特征空间建立真值语义与BEV特征的强关联，迫使BEV编码器在训练时学习真值地图的语义布局。总损失为 $L = \lambda_1 L_{map} + \lambda_2 L_{SMG}$，其中 $\lambda_1 = \lambda_2 = 1$。SMG仅在训练时启用，推理时完全移除，不增加任何计算开销。

## 实验评估

实验在nuScenes（28,130训练样本）与Argoverse 2（1,000日志）上进行，基线覆盖MapTR、MapTRv2、StreamMapNet、BEVFormer、GKT及BEVPool v2。主实验结果如下：

| 方法 | BEV编码器 | mAP (nuScenes) | mAP (Argoverse 2) |
| :--- | :--- | :--- | :--- |
| MapTR | BEVPool v2 | 49.18 | - |
| MapTR+SMG (One-hot MLP) | BEVPool v2 | 51.49 | - |
| MapTRv2 | BEVPool v2 | 49.56 | 63.60 |
| MapTRv2+SMG (One-hot MLP) | BEVPool v2 | 52.14 | 65.20 |
| StreamMapNet | BEVPool v2 | 62.76 | 58.84 |
| StreamMapNet+SMG (One-hot MLP) | BEVPool v2 | 64.18 | 59.71 |

SMG在所有基线上均带来mAP提升，其中MapTR+SMG较基线提升2.31%，MapTRv2+SMG提升2.58%。在Argoverse 2上，MapTRv2+SMG较基线提升1.60%。消融实验显示，裁剪策略对性能影响显著：

| 裁剪策略 | mAP (nuScenes) |
| :--- | :--- |
| Point | 50.10 |
| Box | 50.23 |
| DualBox-bou | 51.49 |

双边界框裁剪较单边界框提升1.26%，较点裁剪提升1.39%，表明边界框聚合提供更强的空间线索。SMG输入格式方面，One-hot标签+MLP优于标签+点位置+MLP（51.49 vs 48.05），说明显式点坐标引入冗余，导致过拟合。对齐损失方面，对比损失（51.49）优于MSE（50.09），验证了特征空间对齐优于像素级对齐。

评估边界方面，论文未报告计算效率对比（仅MapTR-nano报告FPS 35.0），未提供置信区间，且基线未覆盖2025-2026年SOTA方法如DAMap（64.8 mAP）或GSMap（52.3 mAP）。代码未开源，超参数设置与基线一致，使用8块NVIDIA A100 GPU训练。

## 关联研究分析

从问题动机看，SMG与DAMap（Dong et al., 2025）均关注几何精度，但DAMap通过距离感知损失优化解码器定位，而SMG聚焦BEV编码阶段的语义对齐。DAMap在nuScenes上取得64.8 mAP，远高于SMG的51.49，表明解码器优化可能比编码阶段监督带来更大增益。SMG的增益依赖于真值标签的可用性，而DAMap无需额外真值输入，这暗示SMG在标注稀缺场景下泛化能力受限。

从方法设计看，SMG与StreamMapNet（Liu et al., 2023）同属时序建图路线，但StreamMapNet通过多时间点注意力增强时序稳定性，SMG则通过语义引导提升单帧精度。SMG在StreamMapNet上带来1.42% mAP提升，证明其与时序机制兼容。然而，SMG未解决长时序闪烁问题，其增益主要来自单帧几何精度，而非时序一致性。这与领域共识中“时序信息能显著提升地图稳定性”的观点形成互补，SMG可作为时序方法的补充而非替代。

## 总结

SMG针对BEV特征缺乏直接语义监督的问题，提出训练时利用真值标签对齐BEV特征的模块。该模块通过对比学习损失将真值语义嵌入与BEV局部特征拉近，推理时完全丢弃，不增加计算开销。实验显示SMG在MapTR、MapTRv2、StreamMapNet等基线上带来1.3%至2.6%的mAP提升，验证了直接监督的有效性。然而，SMG的性能增益依赖于真值标签的可用性，且未解决长时序稳定性问题。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_0dca2a6515ac)