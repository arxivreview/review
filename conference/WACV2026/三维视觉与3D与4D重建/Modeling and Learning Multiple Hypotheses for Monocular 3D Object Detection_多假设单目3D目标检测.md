# WACV2026最新论文 ｜Modeling and Learning Multiple Hypotheses for Monocular 3D Object Detection ｜多假设单目3D目标检测

作者：Hyeonjeong Park、Peixi Xiong、Pei Yu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c6e957735440)

> 单目3D检测面临深度歧义导致的病态性，传统单点预测往往回归至不可行的均值解。MonoMH通过空间RoI划分生成多假设，结合不确定性过滤，显式建模3D框的多模态分布。该方法在KITTI测试集上以29.12的Car AP3D超越现有单目SOTA，但受限于CNN架构，未验证其在Transformer范式下的通用性。

## 研究背景

单目图像缺乏视差线索，2D投影到3D空间的映射存在多解性，即深度歧义（Depth Ambiguity）。这种几何病态性导致同一2D观测可能对应多个合理的3D边界框，而现有方法通常仅输出单一预测值。当检测器面对遮挡或截断物体时，单点预测往往收敛于这些多解的均值，该均值可能对应一个物理上不存在的3D位置，从而在自动驾驶等下游任务中引入安全隐患。

单目3D检测的主流路线依赖几何先验与不确定性建模来缓解深度模糊。MonoLSS（2024）通过Laplacian不确定性加权损失提升了单点预测的鲁棒性，MonoDETR（2023）则引入Transformer架构以增强特征聚合能力。然而，这些方法均局限于单点预测范式，未能捕捉3D配置的多模态分布本质。MonoMH的切入点在于，将单点预测扩展为多假设预测，通过显式学习多个可能的3D框及其不确定性，解决单点预测在多模态分布下失效的问题。

## 核心方法

### 方法参照系

MonoMH基于常见的单目3D检测架构，包括DLA34骨干网络、2D检测头与3D提升头。标准流程中，3D头回归单一深度、尺寸与朝向，并输出Laplacian不确定性。本文的关键差异在于，将单点3D预测替换为基于RoI空间划分的多假设生成机制，并引入Best-of-Many学习策略与动态假设过滤。

### RoI空间划分与多假设生成

传统多假设方法通过增加多个独立3D头实现，但模型复杂度随假设数量线性增长，且共享输入导致假设多样性不足。MonoMH提出RoI Division，将7×7的RoI特征图划分为K个空间窗口，每个窗口通过共享卷积层预测局部深度与不确定性。第k个假设的深度 $d_k$ 由窗口 $W_k$ 内置信度加权平均计算：

$$ d_k = \frac{\sum_{i \in W_k} c_{roi}^i \cdot d_{roi}^i}{\sum_{i \in W_k} c_{roi}^i} $$

该公式表明，高置信度像素对假设深度的贡献更大，从而在保持模型规模不变的前提下，利用空间异质性特征生成多样化的3D定位假设。

### 软Best-of-Many学习与不确定性过滤

单模态真值无法直接监督多假设，MonoMH引入软Best-of-Many（Soft BoM）损失，将实例级3D框监督传播至RoI内所有窗口。损失函数定义为：

$$ \ell_{BoM} = u^* d^* - d_{gt} + \log u^* $$

其中 $u^*$ 为最优假设的不确定性，$d^*$ 为其深度。该损失鼓励模型在不确定时增大预测方差，从而生成更广泛的假设分布。推理阶段，MonoMH根据置信度阈值动态保留假设数量：高置信度物体仅保留Top-1假设，低置信度物体保留多个假设，以平衡精度与召回率。

## 实验评估

| 方法 | Car AP3D (Easy) | Car AP3D (Mod.) | Car AP3D (Hard) |
| --- | --- | --- | --- |
| MonoLSS | 26.11 | 19.15 | 16.94 |
| MonoDETR | 25.00 | 16.47 | 13.58 |
| MonoMH | 29.12 | 20.88 | 17.93 |

MonoMH在KITTI测试集Car类别上全面超越MonoLSS与MonoDETR，Easy难度下AP3D提升3.01个点。基线覆盖CNN与Transformer架构，但缺失MonoCLUE（2025）等最新SOTA，且未对比LiDAR辅助方法在纯单目协议下的表现。

| 策略 | Car AP3D (Easy) | Car AP3D (Mod.) | Car AP3D (Hard) |
| --- | --- | --- | --- |
| Baseline | 23.81 | 17.00 | 14.17 |
| Multi-head | 24.13 | 16.59 | 13.65 |
| RoI Division | 28.94 | 21.53 | 18.43 |
| Soft BoM Loss | 28.94 | 21.53 | 18.43 |

消融实验显示，RoI Division较Multi-head在Hard难度下提升4.78个点，验证了空间划分优于独立头的设计。Soft BoM损失较Hard BoM在Easy难度下提升2.65个点，表明软监督对多假设学习更优。

实验在KITTI与Waymo上进行，使用AP3D|40与APBEV|40指标。代码已开源，超参数包括KITTI 9假设（4×4窗口）与Waymo 5假设（5×5窗口）。评估协议未包含计算效率对比，且Waymo实验仅对比GUPNet等旧基线，缺乏与最新方法的直接比较。

## 关联研究分析

从问题动机看，MonoMH与MonoCLUE（2025）均针对深度歧义，但MonoCLUE通过对象感知聚类增强解码器查询，MonoMH则通过空间RoI划分生成多假设。MonoCLUE依赖Transformer架构，MonoMH基于CNN，两者在架构选择上存在根本差异。MonoMH的多假设输出提供了更丰富的3D配置信息，但MonoCLUE的聚类机制可能更擅长处理部分可见物体的语义一致性。

从方法设计看，MonoMH与MonoLSS（2024）共享Laplacian不确定性建模，但MonoLSS仅用于单点预测的置信度校准，MonoMH将其扩展至多假设生成与过滤。MonoMH的RoI Division避免了增加模型复杂度，而MonoLSS的MixUp3D增强侧重于数据层面。MonoMH的软BoM损失是核心创新，但其在Transformer架构下的有效性仅通过MonoDETR基线验证，未深入探讨与Deformable DETR等最新架构的兼容性。

## 总结

MonoMH旨在解决单目3D检测中单点预测无法捕捉多模态分布的核心矛盾。通过RoI空间划分与软BoM学习，该方法在保持模型规模不变的前提下，显式建模多个3D框假设，并在KITTI测试集上以29.12的Car AP3D超越MonoLSS的26.11。其边界在于，实验主要基于CNN架构，且在Waymo上仅对比旧基线，未验证其在Transformer范式下的通用性。当RoI划分窗口数量从9增至16时，假设多样性与计算成本的平衡点是否发生偏移，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_c6e957735440)