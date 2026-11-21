# CVPR2026最新论文 ｜EgoPoseFormer v2: Accurate Egocentric Human Motion Estimation for AR/VR ｜自中心人体运动估计

研究机构：沙特阿拉伯阿卜杜拉国王科技大学、德国马克斯·普朗克智能系统研究所

作者：Zhenyu Li、Sai Kumar Dwivedi、Filip Maric 等 14 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.04090)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.04090)

> 头戴式相机视野受限且标注稀缺，导致现有自中心姿态估计方法在遮挡与快速运动下产生抖动且泛化能力差。EgoPoseFormer v2 通过端到端时空Transformer架构与大规模半监督自动标注系统，解决了实时性与数据规模的双重瓶颈。该方法在EgoBody3M基准上实现了4.02cm的MPJPE，但仅验证了特定硬件场景下的性能，跨设备泛化能力仍存疑。

## 研究背景

自中心视角下，头戴式相机仅覆盖部分身体且频繁发生自遮挡，导致单帧回归方法难以恢复平滑的3D姿态。为缓解深度歧义，早期方法依赖时序平滑，但缺乏对3D几何关系的显式建模。当引入Transformer架构时，计算复杂度随关节数量线性增长，且非端到端设计阻碍了梯度回传，限制了模型在边缘设备上的实时部署能力。

自中心3D运动估计旨在从多目头戴相机输入中恢复世界坐标系下的全身姿态，其核心挑战在于受限视野下的几何推理与稀疏标注下的数据扩展。主流路线包括基于热图回归的单帧方法、基于LSTM的时序平滑方法以及基于Transformer的几何对齐方法。EgoPoseFormer（EPFv1）通过变形注意力实现投影引导的特征提取，但存在每关节独立查询导致的计算冗余、两阶段架构的梯度阻断以及缺乏时序建模等缺陷。EPFv2 的切入点在于重构为全端到端可微架构，并引入自动标注系统以利用海量无标签数据，从而在保持实时性的同时提升精度与鲁棒性。

## 核心方法

### 方法参照系

EPFv2 基于 EPFv1 的“粗估计+投影引导细化”两阶段范式，但将 EPFv1 的 MLP+Transformer 混合架构替换为两个架构相同的 Transformer 解码器。关键差异在于 EPFv2 使用单一整体查询（Holistic Query）替代每关节独立查询，并引入因果时间注意力与不确定性头，实现了从单帧精度优化到时空联合推理的转变。

### 单一整体查询与条件化注意力

EPFv2 摒弃了 EPFv1 中关节数量与查询数量一一对应的设计，转而使用一个由辅助信息（如用户身份、头显姿态）初始化的单一整体查询 token $\mathbf{q}_t \in \mathbb{R}^C$ 来聚合全身状态。这一设计解耦了计算复杂度与身体表示，使得模型能灵活支持关键点或参数化人体模型。在条件化多视角交叉注意力中，EPFv2 使用标准多头注意力替代变形注意力，通过编码相机身份 $\xi_v$ 与投影后的2D关键点坐标 $\mathbf{o}_{t,j}^{[v]}$ 构建条件嵌入 $\sigma_t^{[v]}$，引导特征提取：

$$
\mathbf{q}'_t = \text{MHA}(\hat{\mathbf{q}}_t, \{\mathbf{k}_v, \mathbf{v}_v\}_{v=1}^V) + \sigma_t
$$

其中 $\hat{\mathbf{q}}_t$ 为查询，$\mathbf{k}_v, \mathbf{v}_v$ 为第 $v$ 个视角的键值对。该设计解决了 EPFv1 中变形注意力难以在边缘设备部署的问题，同时通过2D投影条件实现了类似立体视觉的几何推理，提升了遮挡区域的定位精度。

### 因果时间注意力与不确定性蒸馏

为解决时序抖动问题，EPFv2 引入因果时间注意力，使当前帧查询 $\mathbf{q}_t$ 能关注过去窗口 $w$ 内的历史查询，利用 KV-Cache 实现高效推理：

$$
\mathbf{q}_t = \text{RoPE}(\mathbf{q}_t) \cdot \text{Attn}(\mathbf{q}_t, \{\mathbf{q}_{t-i}\}_{i=1}^w)
$$

此外，模型预测每个关节的6D不确定性参数 $s \in \mathbb{R}^6$，对应协方差矩阵 $\Sigma = LL^T$ 的 Cholesky 因子。在自动标注系统（ALS）中，教师模型生成伪标签，学生模型通过不确定性引导的蒸馏损失 $\mathcal{L}_{uncertainty}$ 进行训练，该损失基于 Student-t 分布，对不可靠伪标签赋予较低权重：

$$
\mathcal{L}_{uncertainty} = \frac{1}{2} (\hat{\mathbf{p}}_j - \mathbf{p}_j)^T \Sigma^{-1} (\hat{\mathbf{p}}_j - \mathbf{p}_j) + \log |\Sigma|
$$

这一机制使模型能识别并降权低质量伪标签，从而有效利用70M帧的无标签野外数据，提升了跨环境泛化能力。

## 实验评估

EPFv2 在 EgoBody3M 基准上进行了定量评估，该数据集包含3.4M帧真实域数据，使用4个同步单色全局快门相机。基线包括 UnrealEgo、EgoBody3M 和 EgoPoseFormer，覆盖了热图回归、LSTM时序平滑与Transformer几何对齐三条路线，但缺乏与通用单目SOTA（如 SasMamba）的对比，因任务场景不同不可直接比较。

| 方法 | Overall MPJPE (cm) | Overall MPJVE (cm) | Wrists MPJPE (cm) |
| :--- | :--- | :--- | :--- |
| UnrealEgo | 7.41 | 1.27 | - |
| EgoBody3M | 5.18 | 0.54 | 6.14 |
| EgoPoseFormer | 4.75 | 0.87 | 6.01 |
| EPFv2 w/o ALS | 4.17 | 0.42 | 5.74 |
| EPFv2 with ALS | 4.02 | 0.42 | 4.99 |

EPFv2 的 Overall MPJPE 为 4.02cm，较 EgoPoseFormer 提升 15.4%，较 EgoBody3M 提升 22.4%。MPJVE 降低 51.7%（对比 EgoPoseFormer），表明因果时间注意力显著提升了时序一致性。手腕关节 MPJPE 从 6.01cm 降至 4.99cm，验证了投影条件化注意力在遮挡区域的有效性。

消融实验显示，移除时间注意力导致精度大幅下降，证实时序建模对自中心场景至关重要。移除投影条件使细化阶段退化为通用注意力，失去空间锚定能力。引入 ALS 后，手腕 MPJPE 进一步降低 11.7%，表明半监督学习对轻量级模型（如 MobileNetV4-S）的增益更为显著。

评估边界方面，论文仅报告了 EgoBody3M 基准上的结果，未提供置信区间或多次运行的统计显著性检验。代码未公开，但提供了详细的超参数与训练步骤。0.8ms 的 GPU 延迟未包含预处理时间，边缘设备实测延迟可能更高。

## 关联研究分析

从问题动机看，EPFv2 与 SasMamba 均关注高效时序建模，但 SasMamba 针对通用视频序列，依赖扫描策略保留空间结构，而 EPFv2 针对头戴式多目几何约束，利用投影条件实现空间锚定。EPFv2 的单一查询设计在复杂交互姿态（如双手交叉）下可能限制细粒度表达，因为所有关节共享同一查询向量，无法独立建模局部运动模式。

从方法设计看，EPFv2 与 DreamPose3D 均处理不确定性，但 DreamPose3D 采用扩散模型进行多假设采样，推理速度慢，适合静态帧；EPFv2 采用确定性回归加 Student-t 不确定性头，推理速度快，适合实时应用。EPFv2 的不确定性头仅用于训练时的伪标签加权，未用于推理时的多假设生成，这在严重遮挡下可能仍产生伪影，因为确定性回归无法表达多模态分布。

## 总结

EPFv2 解决了自中心姿态估计中实时性与数据稀缺的矛盾，通过端到端Transformer架构与半监督自动标注系统，在 EgoBody3M 上实现了 4.02cm 的 MPJPE 和 0.8ms 的推理延迟。其边界在于仅验证了特定硬件（4个同步相机）下的性能，且单一查询设计可能限制复杂交互姿态的表达。当支持集增大到 5-shot 时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.04090)