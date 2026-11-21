# HuggingFace最新推荐论文 ｜3DZip: Spatial-Aware Feature Diversity-Guided Token Compression for 3D Question Answering ｜3D视觉语言模型中的空间感知特征多样性Token压缩

作者：Changwoo Baek、Kyeongbo Kong

论文原文见 [arXiv](https://arxiv.org/abs/2608.01185)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.01185)

> 投影式3D VLM通过多视图特征提升生成海量几何Token，导致推理延迟与显存占用激增，现有2D压缩方法因忽略3D空间结构而失效。本文指出单纯空间聚合无法消除物体级Token冗余，提出3DZip三阶段压缩框架，结合体素化、特征多样性锚点选择与空间约束合并。该方法在128 Token预算下保留94.7%原始性能并实现1.92倍加速，但其对动态场景及细粒度空间关系推理的鲁棒性尚待验证。

## 研究背景

投影式3D VLM将多视图2D视觉特征通过深度图与相机位姿反投影至世界坐标系，并附加3D位置编码生成几何感知Token。这一过程使Token数量随视图数线性增长（$N=M \times N_{2D}$），例如LLaVA-3D在单场景生成1410个Token，造成显著的注意力计算开销与KV缓存压力。为降低部署成本，Token压缩成为关键，但现有方法多基于2D图像-文本场景设计，依赖LLM注意力分数或CLS Token选择，未显式建模3D空间结构。

3D VLM中的冗余具有双重特性：点级冗余源于多视图对同一物理表面的重复观测，物体级冗余则因单一物体在不同视角下产生空间分离的Token簇。现有2D压缩方法如FastV、VisionZip在3D场景中导致Token向大物体或背景区域集中，物体覆盖率仅51%。DTC虽引入深度信息，但仍局限于2D多视图设置，未解决物体级不平衡。本文切入点在于揭示空间聚合无法消除物体级冗余，需引入特征空间多样性选择以平衡物体覆盖。

## 核心方法

### 方法参照系

本文问题属于3D VLM推理加速中的Token压缩子类。通用流程为：从密集3D Token集$\mathcal{V}$中筛选子集$\mathcal{V}'$，使语言模型$g(\mathcal{V}, t) \approx g(\mathcal{V}', t)$。与2D压缩的关键差异在于，3D Token携带显式空间坐标，冗余结构包含几何一致性约束，单纯语义相关性选择会破坏空间结构。

### 体素化与特征多样性锚点选择

设计动机：解决多视图投影导致的点级冗余与物体级Token不平衡。Stage 1通过体素化消除点级冗余，将空间划分为大小$\delta$的轴对齐体素，对每个体素内Token进行均值池化：

$$\mathbf{f}_k = \frac{1}{|G_k|} \sum_{v_i \in G_k} \mathbf{f}_i, \quad \mathbf{p}_k = \frac{1}{|G_k|} \sum_{v_i \in G_k} \mathbf{p}_i$$

该操作将密集Token集$\mathcal{V}$压缩为体素Token集$\mathcal{V}_{\text{vox}}$，保留粗粒度空间结构。Stage 2针对物体级冗余，采用行列式点过程（DPP）在特征空间选择锚点。归一化体素特征后构造余弦相似度核$L_{kl} = \hat{\mathbf{f}}_k^\top \hat{\mathbf{f}}_l$，通过最大化$\det(L_A)$选择$K$个锚点。DPP鼓励特征空间多样性，避免Token集中于大物体表面，将物体覆盖率从51%提升至70%。

### 空间约束Token合并

设计动机：保留非锚点Token的互补上下文信息，同时维持几何一致性。Stage 3将非锚点Token分配至特征空间最近的锚点，仅当空间距离$d_g(j, a) \leq \tau_g$时执行合并：

$$\mathbf{f}'_a = \frac{\mathbf{f}_a + \sum_{j \in \mathcal{S}_a} \mathbf{f}_j}{1 + |\mathcal{S}_a|}, \quad \mathbf{p}'_a = \mathbf{p}_a$$

该公式将锚点特征更新为自身与分配Token的均值，位置坐标保持不变。空间约束$\tau_g$确保合并的Token在几何上邻近，避免跨物体信息混淆。不满足约束的Token被丢弃，因其可能对应孤立观测。最终压缩集$\mathcal{V}'$仅含$K$个Token，显著降低计算开销。

## 实验评估

实验在SQA3D、ScanQA、OpenEQA三个3D QA基准上进行，基线覆盖2D压缩方法（FastV、SparseVLM、VisionZip、VisPruner）与3D感知方法（DTC、Voxelization）。缺失Geo3DPruner等最新3D专用压缩方法对比。

| 方法 | SQA3D EM (128 Tokens) | ScanQA EM (128 Tokens) | OpenEQA Avg (128 Tokens) | 相对性能保留率 |
|---|---|---|---|---|
| LLaVA-3D (1410 Tokens) | 55.7 | 26.5 | 60.3 | 100.0% |
| DTC | 51.3 | 22.1 | 54.8 | 88.8% |
| VisionZip | 51.5 | 22.2 | 56.2 | 89.8% |
| 3DZip | 53.2 | 24.2 | 58.6 | 94.7% |

3DZip在128 Token预算下SQA3D EM达53.2，较DTC提升1.9点，保留94.7%原始性能。效率方面，推理延迟从342ms降至178ms，FLOPs从9.18T降至0.90T，KV缓存从722MB降至101MB。

| 消融配置 | SQA3D EM (64 Tokens) | SQA3D EM (32 Tokens) |
|---|---|---|
| 完整3DZip | 52.8 | 51.1 |
| 无体素化 | 51.8 | 50.2 |
| 空间距离DPP | 50.1 | 49.0 |
| 无合并步骤 | 52.5 | - |

消融显示，移除体素化导致性能下降1.0点（64 Tokens），证实点级冗余需先消除。使用空间距离替代特征距离进行DPP选择，性能下降2.7点，验证特征多样性优于几何分散性。无合并步骤性能下降0.3点，表明空间约束合并对保留互补上下文至关重要。

评估边界：指标仅含EM与LLM-Match，未覆盖细粒度空间关系推理。协议未报告置信区间，数值比较需谨慎。代码未公开，超参数（$\delta=0.2m$, $\tau_g=5$）固定，可复现性受限。

## 关联研究分析

从问题动机看，3DZip与DTC均针对3D VLM Token冗余，但DTC仅利用深度信息进行空间聚合，未解决物体级不平衡。3DZip引入特征多样性DPP，根源在于多视图投影导致同一物体表面Token空间分离，单纯空间聚合无法区分物体实例。这一差异是否源于任务特性（3D QA需物体级理解）还是方法设计选择，论文未明确区分。

从方法设计看，3DZip与VisionZip同属Token合并框架，但VisionZip依赖CLS注意力选择，在3D场景中导致Token向背景集中。3DZip采用DPP特征多样性选择，根源在于3D Token的空间结构使语义相关性选择失效。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

3DZip解决的核心矛盾是投影式3D VLM中多视图Token冗余与推理效率的冲突。现有2D压缩方法因忽略3D空间结构导致物体覆盖不均，本文通过体素化消除点级冗余、DPP特征多样性选择平衡物体覆盖、空间约束合并保留几何一致性，实现128 Token下94.7%性能保留与1.92倍加速。其边界在于静态场景假设，动态物体可能导致体素分配失效；细粒度空间关系推理能力未充分验证。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.01185)