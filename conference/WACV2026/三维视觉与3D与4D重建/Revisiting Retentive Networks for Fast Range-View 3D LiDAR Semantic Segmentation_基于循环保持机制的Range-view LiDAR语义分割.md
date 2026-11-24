# WACV2026最新论文 ｜Revisiting Retentive Networks for Fast Range-View 3D LiDAR Semantic Segmentation ｜基于循环保持机制的Range-view LiDAR语义分割

作者：Simone Mosco、Daniel Fusaro、Wanmeng Li 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_369c075749c1)

> 自动驾驶中的LiDAR语义分割需在实时约束下实现高精度环境理解，但主流Range-view方法依赖标准Attention机制，缺乏对LiDAR传感器360°视场角引发的图像左右边界相邻这一空间拓扑结构的显式建模，且参数量庞大。本文切入点在于引入源自NLP的Retentive Network架构，并针对Range-view的环形几何特性设计Circular Retention机制，同时提出一组基于Range-view几何特性的数据增强策略。该方法在PandaSet上达到Range-view方法SOTA，但在SemanticKITTI上受限于输入分辨率，其性能边界与标准高分辨率协议下的SOTA存在差距。

## 研究背景

LiDAR点云经球面投影映射为Range-view图像后，其水平方向对应360°方位角，导致图像左边界与右边界在物理空间上相邻。这一环形拓扑结构是Range-view表示区别于普通2D图像的核心几何属性。标准卷积网络受限于感受野，难以捕捉长程依赖；而标准Self-Attention虽能建模全局关系，但其计算复杂度随序列长度平方增长，且未内嵌任何空间先验，无法利用上述环形连续性。

LiDAR语义分割的主流路线分为点基、体素基与投影基三类。点基与体素基方法（如Cylinder3D）虽能保留三维几何细节，但3D卷积计算开销大，难以满足车载嵌入式平台的实时性要求。投影基方法（如SqueezeSeg、RangeFormer）将点云映射至2D平面，复用成熟的2D视觉骨干网络，显著提升了推理速度。然而，现有投影基方法多采用CNN或标准Transformer，前者受限于局部感受野，后者虽能建模长程依赖但参数量大且缺乏空间结构约束。RangeFormer等近期工作虽引入Vision Transformer，但依赖大规模图像预训练，且标准Attention机制未考虑Range-view的环形边界，导致跨边界的空间关系建模失效。

本文旨在解决投影基方法中“计算效率”与“空间结构感知”的双重瓶颈。通过引入线性复杂度的Retentive Network替代标准Attention，并设计显式编码环形距离的衰减矩阵，本文在保持实时推理能力的同时，将Range-view的几何先验内嵌于骨干网络之中，从而在低参数量下实现长程依赖的高效建模。

## 核心方法

### 方法参照系

本文遵循投影基LiDAR分割的标准流程：球面投影生成Range-view图像，经卷积Stem提取初始特征，骨干网络处理特征图，语义头输出预测。与RangeFormer等基于PVT骨干的方法不同，本文骨干采用Retentive Network，核心差异在于将NLP中的序列保持机制改造为适配2D环形图像的Circular Retention（CiR）机制，并引入基于Range-view几何的数据增强。

### Circular Retention机制

标准Attention通过Softmax归一化计算Query与Key的相似度，缺乏对空间距离的显式建模。本文在Multi-Scale Retention模块中引入位置编码 $\Theta$ 与 $\bar{\Theta}$，并定义循环衰减矩阵 $\mathbf{D}_C$。该矩阵元素基于Token间的循环曼哈顿距离计算，公式如下：

$$
\mathbf{D}_C[i,j] = \exp\left(-\lambda \cdot \min(|x_i - x_j|, W - |x_i - x_j|) - \mu \cdot |y_i - y_j|\right)
$$

其中 $W$ 为图像宽度，$\lambda, \mu$ 为衰减系数。该公式的物理含义是：水平方向距离计算考虑了环形边界（取最小值），垂直方向为线性距离，指数衰减确保近邻Token权重高、远邻权重低。此设计解决了标准Attention无法区分“物理相邻但像素索引远”的跨边界Token的问题，使网络能显式利用360°视场角的连续性。

### Range-view几何增强

现有3D增强（如随机旋转）在投影至2D后易破坏Range-view的几何一致性。本文提出五种基于Range-view几何的增强策略：RangeBeams交换两帧图像的行以模拟激光束替换；RangePolar替换极坐标扇区并粘贴稀有类别实例；RangeCompletion利用上下行移位填充投影产生的空单元格；RangeFake随机替换标签为稀有类别；RangeInstance从源图像提取稀有实例粘贴至当前图像。这些策略直接作用于2D特征空间，避免了3D-2D投影过程中的信息丢失，针对性地缓解了类别不平衡与稀疏性问题。

## 实验评估

| 数据集 | 方法 | mIoU (%) | Params (M) | Runtime (ms) |
| :--- | :--- | :--- | :--- | :--- |
| PandaSet | RangeRet (ours) | 60.0 | 3.8 | 4.56 |
| PandaSet | RangeFormer | 49.4 | 23.7 | — |
| PandaSet | CENet | 55.4 | — | — |
| SemanticKITTI | RangeRet (ours) | 60.7 | 3.8 | 2.96 |
| SemanticKITTI | CENet | 65.7 | — | — |
| SemanticKITTI | RangeFormer | 64.8 | 23.7 | — |

实验在SemanticKITTI、PandaSet与SemanticPOSS上进行。基线覆盖SqueezeSeg、RangeNet++、RangeFormer、CENet等投影基方法，但未对比Cylinder3D等体素基SOTA。在PandaSet上，RangeRet以60.0% mIoU领先RangeFormer 10.6个百分点，且参数量仅为后者的1/6。在SemanticKITTI上，RangeRet取得60.7% mIoU，低于CENet的65.7%与RangeFormer的64.8%。需注意，本文使用64×1024分辨率，而对比方法多用2048宽度，分辨率差异是性能差距的主要归因。

| 消融项 | mIoU (%) | 增量 |
| :--- | :--- | :--- |
| Baseline (Attention) | 58.5 | — |
| Retention | 57.7 | -0.8 |
| CiR (ours) | 58.7 | +0.2 |
| CiR + Exp. Map. | 60.7 | +2.2 |
| Baseline + Range Aug. | 60.7 | +2.2 |

消融实验表明，直接替换为原始Retention机制导致性能下降0.8%，验证了NLP时序机制不适用于空间任务。引入CiR后回升至58.7%，而应用指数映射后mIoU跃升至60.7%，证明指数映射对空间关系的建模至关重要。Range-view增强策略带来2.2%的增益，其中RangeBeams与RangeInstance贡献最大，表明几何一致性增强对稀有类别识别有效。

评估边界方面，论文未报告置信区间，且SemanticKITTI结果受限于低分辨率输入，无法直接对比高分辨率SOTA。代码已开源，训练使用单张A40 GPU，超参数（如学习率调度、Dropout率）已详细披露，具备可复现性。

## 关联研究分析

从方法设计看，RangeRet与RangeFormer同属投影基路线，但骨干网络选择存在根本差异。RangeFormer依赖PVT骨干与大规模图像预训练，利用2D视觉先验弥补LiDAR数据标注不足；RangeRet则从随机初始化训练，通过CiR机制内嵌LiDAR特有的环形几何先验。这一差异源于对“先验来源”的不同假设：前者假设2D图像语义可迁移至LiDAR，后者假设LiDAR几何结构本身蕴含足够信息。RangeRet在低参数量下接近高分辨率RangeFormer的性能，暗示几何先验可能部分替代了大规模预训练的语义先验，但两者在语义丰富度上的差距需进一步验证。

从问题动机看，本文聚焦于“效率-结构”权衡，而知识库中A3POINT、Source-Only Cross-Weather LiDAR等方法聚焦于“鲁棒性-泛化”权衡。RangeRet的RangeCompletion增强虽能缓解稀疏性，但未显式建模恶劣天气下的分布偏移。相比之下，A3POINT通过离散潜在表示学习语义混淆先验，直接针对跨天气泛化。RangeRet的增强策略更偏向数据多样性而非分布鲁棒性，其在恶劣天气下的表现未经验证。这提示RangeRet的几何先验在理想数据下有效，但在传感器退化场景下，几何结构的稳定性可能受损，需结合域适应策略。

## 总结

本文核心矛盾在于投影基LiDAR分割中标准Attention的计算开销与Range-view环形几何先验缺失。RangeRet通过引入线性复杂度的Retentive Network并设计Circular Retention机制，将360°视场角的连续性内嵌于骨干网络，同时提出基于Range-view几何的增强策略。实验证明，在PandaSet上该方法以3.8M参数达到60.0% mIoU，显著优于参数量23.7M的RangeFormer；在SemanticKITTI上，受限于64×1024输入分辨率，其60.7% mIoU低于高分辨率基线。本文边界在于未验证恶劣天气下的鲁棒性，且低分辨率下的性能上限未探明。当输入分辨率提升至2048宽度时，CiR机制能否维持其相对于标准Attention的效率优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_369c075749c1)