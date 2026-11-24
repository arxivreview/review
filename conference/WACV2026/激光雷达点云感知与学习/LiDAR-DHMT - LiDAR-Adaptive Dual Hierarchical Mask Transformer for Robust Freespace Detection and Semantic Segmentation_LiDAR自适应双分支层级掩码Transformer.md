# WACV2026最新论文 ｜LiDAR-DHMT: LiDAR-Adaptive Dual Hierarchical Mask Transformer for Robust Freespace Detection and Semantic Segmentation ｜LiDAR自适应双分支层级掩码Transformer

作者：Siyu Chen、Ting Han、Changshe Zhang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_77d547bf4aa8)

> 自由空间检测旨在从交通场景中识别可行驶区域，其精度直接决定自动驾驶系统的安全性。现有RGB-LiDAR融合方法多将点云投影为深度图，导致3D几何信息丢失，或在特征末端进行刚性融合，缺乏对复杂空间结构的适应性。LiDAR-DHMT通过引入3D相对位置偏置与动态偏置注意力，将LiDAR几何先验直接注入Transformer注意力机制，并结合层级掩码交互增强上下文建模。该方法在多个基准上取得SOTA性能，但其对LiDAR点云质量与密度的依赖程度，以及在不同传感器配置下的泛化能力，仍需进一步验证。

## 研究背景

自由空间检测的核心挑战在于如何从多模态数据中构建空间一致的语义表示。LiDAR点云提供精确的3D几何信息，而RGB图像富含语义细节，但两者在特征空间存在显著差异。早期融合方法将点云投影为2D深度图，虽简化了处理流程，却丢失了点云固有的稀疏性与不规则性，导致在复杂城市场景中空间一致性下降。晚期融合方法虽保留3D特征，但仅在末端进行固定模块融合，缺乏对中间层空间关系的动态建模，难以适应多尺度几何结构。

RGB-LiDAR融合领域的主流路线围绕计算效率与精度权衡展开。CMX、CMNeXt等方法采用双分支架构，但融合机制较为固定，未能充分利用LiDAR的3D几何先验。DiPFormer等近期工作虽引入深度特征作为位置编码，但仍依赖2D深度图，未直接利用原始点云几何。LiDAR-DHMT的切入点在于，将3D点云几何直接转化为可学习的相对位置偏置，注入Transformer注意力计算，同时通过掩码交互机制增强图像token的上下文建模能力，从而在保持计算效率的前提下提升空间一致性。

## 核心方法

### 方法参照系

RGB-LiDAR融合的标准流程通常包括：分别提取RGB与LiDAR特征，通过早期或晚期融合模块整合，最后进行语义分割。本文的关键差异在于，不采用固定的融合模块，而是将LiDAR几何信息转化为3D相对位置偏置，动态注入Transformer注意力机制，实现特征级的空间感知融合。

### 3D相对位置偏置与动态偏置注意力

传统Transformer位置编码仅考虑2D像素坐标，无法捕捉LiDAR提供的深度信息。LiDAR-DHMT设计3D相对位置偏置，利用像素坐标$(x_i, y_i)$与深度$d_i$计算token对之间的相对偏移：

$$
b_{ij} = f(\Delta x_{ij}, \Delta y_{ij}, \Delta d_{ij})
$$

其中$f(\cdot)$为共享MLP，$b_{ij}$作为偏置矩阵$B$加入注意力计算。这一设计解决了2D位置编码无法区分深度差异相近但空间位置不同的token的问题，使模型能更精确地建模复杂几何关系。动态偏置注意力（DBA）进一步通过空间降采样Key/Value降低计算量，同时保留3D几何先验，实现43.6M参数下的高精度。

### 层级掩码交互与双分支Transformer

为增强图像token的上下文建模，LiDAR-DHMT引入层级掩码交互（MI）模块。在每个骨干网络阶段，对输入图像进行随机掩码，并通过交叉注意力重建被掩码区域：

$$
F_{S_{i+1}} = F_{S_i} + f_M
$$

其中$f_M$为掩码交互特征。这一机制迫使模型学习token间的潜在位置关系与上下文信息，提升对小目标与遮挡区域的特征表达。双分支Transformer（DBFormer）并行计算全局注意力与窗口注意力，通过可学习参数$\alpha, \beta$自适应融合：

$$
F_{S_i} = \alpha f_G + \beta f_W
$$

全局分支捕捉长程上下文，窗口分支聚焦局部细节，两者协同增强语义丰富度与空间一致性。

## 实验评估

| 方法 | 模态 | 参数量(M) | 时间(s) | KITTI Road MaxF(%) | KITTI-360 mIoU(%) | Cityscapes mIoU(%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| CMX | RGB-L | 66.7 | 0.307 | 93.45 | 64.31 | 82.4 |
| CMNeXt | RGB-L | 58.7 | 0.111 | 94.55 | 65.26 | 82.5 |
| DiPFormer | RGB-D | 56.3 | 0.029 | 96.10 | 68.74 | 83.4 |
| LiDAR-DHMT | RGB-L | 43.6 | 0.023 | 97.59 | 69.45 | 84.4 |

实验在KITTI Road、KITTI-360与Cityscapes上进行，覆盖RGB、RGB-D与RGB-L基线。LiDAR-DHMT在KITTI Road取得97.59% MaxF，KITTI-360 mIoU 69.45%，Cityscapes mIoU 84.4%，均优于现有SOTA。值得注意的是，其参数量仅为CMX的65%、CMNeXt的74%，推理时间0.023s，显著低于CMX的0.307s，验证了动态偏置注意力在效率上的优势。

| 配置 | 模态 | MaxF(%) | PRE(%) | REC(%) |
| :--- | :--- | :--- | :--- | :--- |
| Baseline | RGB | 87.00 | 85.77 | 88.27 |
| + DBFormer | RGB | 91.62 | 91.04 | 92.20 |
| + Mask Interaction | RGB | 93.03 | 92.15 | 93.94 |
| + Dynamic Bias Attention | RGB-L | 91.61 | 91.04 | 92.20 |
| ++ DBFormer | RGB-L | 96.09 | 96.73 | 95.46 |
| ++ Mask Interaction | RGB-L | 96.33 | 95.87 | 96.79 |
| LiDAR-DHMT | RGB-L | 97.59 | 97.33 | 97.84 |

消融实验显示，DBFormer在RGB基线上带来+4.62% MaxF提升，引入LiDAR后进一步提升至96.09%。掩码交互与动态偏置注意力的协同作用贡献了最终性能。辅助监督策略优于知识蒸馏，在自由空间检测与语义分割任务上均取得更高性能，且收敛更快。

评估协议基于标准数据集划分，指标包括MaxF、mIoU与R. IoU。论文未提供代码与完整超参数，但详细描述了训练设置（4×NVIDIA 4090，batch size 6，AdamW优化器）。评估边界在于，实验仅覆盖静态场景，未测试动态物体或恶劣天气下的鲁棒性；LiDAR点云质量与密度的影响未单独消融，可能限制结论的普适性。

## 关联研究分析

从方法设计看，LiDAR-DHMT与CMX、CMNeXt等RGB-LiDAR融合方法的核心差异在于融合机制。CMX采用固定模块融合，而LiDAR-DHMT通过3D相对位置偏置在注意力层动态注入几何先验。这一差异源于对LiDAR几何信息利用深度的不同：CMX将点云视为辅助模态，LiDAR-DHMT则将其作为空间锚点。然而，LiDAR-DHMT对点云密度的依赖可能更高，在稀疏点云场景下性能是否下降，论文未给出回答。

从问题动机看，LiDAR-DHMT与DiPFormer等RGB-D方法均关注空间一致性，但DiPFormer依赖2D深度图，LiDAR-DHMT直接利用3D点云。这一选择避免了深度图投影的信息损失，但增加了3D特征提取的计算开销。LiDAR-DHMT通过动态偏置注意力降低计算量，但其效率优势是否在所有LiDAR配置下保持，仍需验证。与VFM蒸馏方法相比，LiDAR-DHMT未利用视觉基础模型的语义先验，其语义丰富度是否受限于LiDAR几何信息，是另一潜在盲区。

## 总结

LiDAR-DHMT解决的核心矛盾是RGB-LiDAR融合中3D几何信息丢失与计算效率的权衡。其切入点在于将LiDAR点云几何转化为3D相对位置偏置，直接注入Transformer注意力，避免了深度图投影的信息损失，同时通过动态偏置注意力降低计算开销。方法通过3D相对位置偏置、动态偏置注意力与层级掩码交互的协同，在KITTI Road取得97.59% MaxF，KITTI-360 mIoU 69.45%，参数量仅为CMX的65%。边界在于，实验仅覆盖静态场景，未测试动态物体或恶劣天气；LiDAR点云质量与密度的影响未单独消融，可能限制结论的普适性。当LiDAR点云密度降低或存在噪声时，3D相对位置偏置的稳定性是否受影响，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_77d547bf4aa8)