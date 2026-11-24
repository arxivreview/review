# ICLR2026最新论文 ｜POINT-FOCUSED ATTENTION MEETS CONTEXT-SCAN - STATE SPACE: ROBUST BIOLOGICAL VISUAL PERCEP TION FOR POINT CLOUD REPRESENTATION ｜点聚焦注意力与上下文扫描状态空间：生物视觉启发的点云表征学习

研究机构：南京大学、北京邮电大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_65402417)

> 点云表征学习长期受困于局部细粒度结构捕捉与全局长程依赖建模之间的计算效率权衡，现有局部注意力网络视野受限，而纯状态空间模型（SSM）局部感知不足。PointLearner 借鉴生物视觉的中央凹视觉与扫视机制，提出点聚焦注意力（Point-Focused Attention, PFA）与上下文扫描状态空间（Context-Scan State Space, CSSS）相结合的混合架构。该方法通过竞争归一化注意力融合局部与全局特征，并利用希尔伯特曲线引导双向 S6 进行全局推理，在多个基准上取得 SOTA 性能。其价值在于验证了生物启发混合架构的有效性，但 S3DIS 分割任务上的绝对精度仍显著低于最新专用方法，且对序列化路径的依赖限制了其在极端非规则拓扑下的泛化潜力。

## 研究背景

点云数据的无序性与稀疏性使得传统卷积操作失效，邻域聚合成为捕捉局部几何结构的核心机制，但固定半径或 K 近邻（KNN）采样策略易引入噪声或丢失关键结构。状态空间模型（State Space Model, S6）具备线性复杂度的长程建模能力，但其因果性与单向性要求输入序列化，导致全局上下文信息被压缩至历史隐藏状态，局部学习不充分。置换不变性（Permutation Invariance）是点云模型的基础约束，但序列化过程本身引入了对点顺序的依赖，这与点云的本质属性存在潜在张力。

点云表征学习的主流路线在局部注意力与全局 SSM 之间摇摆。局部注意力网络如 Point Transformer 将计算复杂度降至线性，但视野狭窄，难以建模场景内物体间的长程依赖；纯 SSM 方法如 PointMamba 虽能捕捉全局结构，但在细粒度局部特征处理上表现乏力。现有混合架构如 PoinTramba 尝试结合两者，但缺乏对局部与全局信息动态交互机制的深入设计。PointLearner 的切入点在于模拟生物视觉的“聚焦-扫描”过程，通过竞争归一化注意力实现局部细粒度感知与全局粗粒度感知的自适应融合，并利用希尔伯特曲线的局部保持特性优化 SSM 的序列化路径，从而在保持线性复杂度的同时提升局部-全局协同建模能力。

## 核心方法

### 方法参照系

PointLearner 遵循 Point Transformer 风格的编码器-解码器架构，嵌入层通过多层感知机（MLP）将点云投影至高维空间，下采样采用最远点采样（FPS），上采样采用线性插值。与标准局部注意力网络不同，本文在核心块中引入双分支点聚焦注意力与上下文扫描状态空间，旨在解决局部视野受限与全局推理不足的双重瓶颈。

### 点聚焦注意力

点聚焦注意力（PFA）模拟中央凹视觉，通过双分支设计实现细粒度局部感知与粗粒度全局感知的竞争融合。局部邻域分支（Local Neighbor Branch, LNB）基于 KNN 构建邻域，计算细粒度注意力；空间下采样分支（Spatial Downsampling Branch, SDB）利用可学习的诱导点（Inducing Points）进行自适应下采样，提取全局语义特征。两分支的注意力权重在单一 softmax 计算中竞争归一化，公式如下：

$$ \text{PFA}(\mathbf{p}_i) = \text{Split}(\text{Softmax}([\mathbf{A}_i^l, \mathbf{A}_i^s]) \cdot [\mathbf{V}_i^l, \mathbf{V}_i^s]) $$

其中 $\mathbf{A}_i^l$ 和 $\mathbf{A}_i^s$ 分别为局部与全局注意力权重，$\mathbf{V}_i^l$ 和 $\mathbf{V}_i^s$ 为对应值向量。该设计解决了简单加法融合无法模拟生物视觉中局部与全局特征动态交互的问题，使每个点能自适应选择最有效的感受野信息。

### 上下文扫描状态空间

上下文扫描状态空间（CSSS）模拟眼球扫视，利用希尔伯特曲线对 PFA 输出进行序列化，引导双向 S6 进行全局几何推理。希尔伯特曲线具有局部保持性和自相似旋转复制特性，与眼球扫视路径高度对齐，确保序列化过程中空间邻近性的高保真度。双向 S6 通过前向与后向扫描构建全局感受野，弥补单向 S6 的视野局限。该设计解决了纯 SSM 方法因序列化顺序不当导致的全局推理精度下降问题，增强了模型对复杂场景的语义结构整合能力。

## 实验评估

| 数据集 | 任务 | 方法 | 指标 | 数值 |
| :--- | :--- | :--- | :--- | :--- |
| ModelNet40 | 分类 | PointLearner | OA (%) | 94.17 |
| ModelNet40 | 分类 | PoinTramba | OA (%) | 88.9 |
| ScanObjectNN | 分类 | PointLearner | OA (%) | 89.8 |
| ScanObjectNN | 分类 | PoinTramba | OA (%) | 88.9 |
| S3DIS | 分割 | PointLearner | mIoU (%) | 74.3 |
| S3DIS | 分割 | HydraMamba | mIoU (%) | 73.6 |

实验在 ModelNet40、ScanObjectNN、ShapeNet 和 S3DIS 上进行，基线覆盖注意力（PTv3, Swin3D）和 SSM（HydraMamba, PCM）两类主流路线，但缺失纯图卷积（DGCNN）及最新拓扑方法（TACO-Net）对比。在 ModelNet40 上，PointLearner 以 94.17% OA 超越 PoinTramba 的 88.9%，但在 S3DIS 上仅达 74.3% mIoU，显著低于领域综述中提到的 Channel-Level Relation 方法的 91.6%，表明其在大规模场景分割任务上的绝对精度仍有差距。

| 消融模块 | 参数 (M) | FLOPs (G) | 吞吐量 (FPS) | OA (%) |
| :--- | :--- | :--- | :--- | :--- |
| w/o LNB | 6.57 | 0.504 | 221 | 92.11 |
| w/o SDB | 6.35 | 0.578 | 183 | 93.06 |
| Additive Fusion | 7.36 | 0.610 | 166 | 93.43 |
| Uni. S6 | 6.06 | 0.553 | 181 | 93.08 |
| Full Model | 7.36 | 0.610 | 163 | 94.17 |

消融实验显示，移除局部邻域分支（LNB）导致 OA 下降 2.06 个点，移除空间下采样分支（SDB）下降 1.11 个点，证明 LNB 对局部几何建模的贡献更大。竞争归一化融合比加法融合高 0.74 个点，双向 S6 比单向 S6 高 1.09 个点，验证了动态交互与全局扫描路径优化的必要性。

评估协议采用标准划分，指标包括 OA 和 mIoU，但未报告置信区间。代码已开源，超参数与 GPU 配置（RTX 4090）明确，可复现性良好。然而，S3DIS 上的性能差距提示骨干网络或预训练策略可能影响更大，而非单纯模块设计。

## 关联研究分析

从问题动机看，PointLearner 与 PoinTramba 同属混合架构路线，但 PoinTramba 侧重 SSM 的全局建模，而 PointLearner 强调生物视觉启发的局部-全局竞争融合。PoinTramba 在 ModelNet40 上 OA 为 88.9%，低于 PointLearner 的 94.17%，差异源于 PFA 的竞争归一化机制更有效地平衡了局部细节与全局语义。然而，PointLearner 在 S3DIS 上的 74.3% mIoU 远低于最新专用方法，暗示混合架构在大规模场景分割中可能受限于序列化路径的刚性，而专用方法如 Channel-Level Relation 可能通过更灵活的注意力机制避免了这一瓶颈。

从方法设计看，PointLearner 与 PointMamba 同用 S6，但 PointMamba 依赖轴排序或空间填充曲线序列化，而 PointLearner 采用希尔伯特曲线并引入 PFA 预处理。PointMamba 在 ModelNet40 上 OA 为 94.2%，与 PointLearner 的 94.17% 持平，但在 ScanObjectNN 上 PointLearner 以 89.8% 超越 PointMamba 的 89.3%，表明 PFA 对噪声鲁棒性的提升。希尔伯特曲线的局部保持性是否在所有非规则拓扑点云上均优于轴排序，论文未提供充分消融，这一设计选择对极端稀疏或高曲率结构的适用性存疑。

## 总结

PointLearner 旨在解决点云表征学习中局部细粒度结构与全局长程依赖的计算效率权衡矛盾，现有局部注意力网络视野受限，纯 SSM 局部感知不足，而生物视觉的“聚焦-扫描”机制提供了自然的解决方案。通过点聚焦注意力的竞争归一化融合与上下文扫描状态空间的希尔伯特曲线引导，该方法在 ModelNet40 上达到 94.17% OA，在 ScanObjectNN 上达到 89.8% OA，验证了混合架构的有效性。然而，S3DIS 上 74.3% mIoU 与最新专用方法 91.6% 的巨大差距暴露了其在大规模场景分割中的局限，且希尔伯特曲线序列化对非规则拓扑的依赖可能限制泛化能力。当点云分布极度非均匀或拓扑结构复杂时，固定序列化路径的全局推理精度是否仍能保持，论文未给出明确回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_65402417)