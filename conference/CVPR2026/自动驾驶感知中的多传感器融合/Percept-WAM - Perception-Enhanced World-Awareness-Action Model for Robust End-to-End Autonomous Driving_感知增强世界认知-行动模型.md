# CVPR2026最新论文 ｜Percept-WAM: Perception-Enhanced World-Awareness-Action Model for Robust End-to-End Autonomous Driving ｜感知增强世界认知-行动模型

研究机构：复旦大学

作者：Jianhua Han、Meng Tian、Jiangtong Zhu 等 19 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.19221)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.19221)

> 自动驾驶感知面临的核心矛盾是视觉语言模型（VLM）具备逻辑推理能力但缺乏精确几何定位，导致长尾场景下决策脆弱。现有方法或依赖问答式监督导致定位间接且置信度失真，或采用扩散解码器牺牲了LLM的推理优势。Percept-WAM通过引入编码度量坐标与校准置信度的World-PV/BEV令牌，在单一VLM内隐式统一2D/3D感知。该方法在nuScenes BEV 3D检测中取得58.9 mAP，NAVSIM规划任务中PMDS达90.2，验证了感知增强对端到端驾驶的有效性，但其绝对精度仍低于专用检测器，且流式推理下的长程依赖建模能力存疑。

## 研究背景

当VLM处理驾驶场景时，其空间理解往往停留在语义层面，无法输出精确的3D坐标或置信度，这种几何能力的缺失导致检测偏差在闭环决策中累积。为解决此问题，研究者引入了鸟瞰图（Bird's-Eye-View, BEV）表示作为统一空间接口，但传统BEV方法依赖刚性几何投影，在传感器标定误差下易产生鬼影物体。同时，视觉语言-行动（Vision-Language-Action, VLA）模型试图将动作监督注入VLM以提升控制能力，但现有VLA框架多采用问答式监督，仅提供间接定位信号，且缺乏对检测置信度的显式校准，导致拥挤场景下重复检测与误报频发。

该领域的主流路线存在根本张力：模块化系统通过显式中间表示保证可解释性，但误差在流水线中累积；端到端系统减少误差累积，但纯黑盒方法在长尾场景缺乏安全兜底。Percept-WAM的切入点在于打破“感知”与“推理”的二元对立，不再将空间理解视为问答任务，而是将其重构为可重建的世界状态表示。通过在世界令牌中嵌入度量坐标与置信度，模型既能保留VLM的逻辑推理能力，又能提供局部化、可复用的几何证据，从而在单一骨干网络内实现从感知到行动的闭环优化。

## 核心方法

### 方法参照系

Percept-WAM属于端到端驾驶系统类别，其标准流程通常包含独立的多模态编码器、BEV特征融合模块及轨迹预测头。本文与通用流程的关键差异在于摒弃了独立的检测头与刚性投影，转而利用VLM的自注意力机制，通过可学习的网格令牌隐式建模从透视视图（Perspective-View, PV）到BEV空间的映射，并将感知任务统一为序列生成问题。

### World-PV/BEV令牌与网格条件预测

传统VLA方法将空间理解转化为问答，导致定位信号间接且置信度饱和。Percept-WAM在VLM骨干（InternVL2-8B）中引入World-PV与World-BEV令牌，每个令牌编码度量坐标与校准置信度。World-BEV令牌通过交叉注意力查询World-PV特征，以纯数据驱动方式将2D证据提升至3D空间。其核心创新在于网格条件预测头，将图像特征切分为$H \times W$网格，每个网格位置作为局部查询预测对齐的边界框或掩码。该设计解决了密集多目标推理中的重复检测问题，通过并行自回归解码（Parallel AR Decoding）在保持吞吐量的同时提升长尾场景稳定性。

$$
\mathcal{L}_{det} = \sum_{i} \left( \mathcal{L}_{cls}(y_i, \hat{y}_i) + \mathcal{L}_{box}(b_i, \hat{b}_i) + \mathcal{L}_{conf}(c_i, \hat{c}_i) \right)
$$

其中，$\mathcal{L}_{conf}$为基于IoU的置信度损失，$\hat{c}_i$为预测的IoU分数。该公式显式校准检测置信度，避免softmax概率在模糊检测中饱和导致的误报。

### IoU感知置信度与流式推理

针对大语言模型系统性过度自信的问题，Percept-WAM引入IoU感知评分目标。训练时，利用中间阶段模型在训练集上的预测生成置信度调优数据集，将IoU离散化为20个bin，并通过损失掩码策略区分GT样本与调优样本：GT样本仅监督类别与框，调优样本仅监督置信度。推理时，最终检测分数定义为类别置信度与预测IoU的乘积。此外，为降低延迟，模型采用流式KV缓存机制，通过双重计算缓解训练-推理范式不匹配导致的分布漂移，将单帧延迟从2700 ms降至707 ms。

## 实验评估

Percept-WAM在nuImages、nuScenes、COCO及NAVSIM等基准上进行评估，基线涵盖Mask R-CNN、PointPillars、BEVFusion及DiffusionDrive等专用检测器与规划器。实验设置采用两阶段课程学习，先巩固PV/BEV感知，再进行端到端微调。

| 任务 | 数据集 | 指标 | Percept-WAM | 基线 (PointPillars/DiffusionDrive) |
|---|---|---|---|---|
| BEV 3D Det | nuScenes | mAP | 58.9 | 52.3 |
| 2D Det | COCO | mAP | 51.7 | 47.5 (LMM-Det) |
| Trajectory | NAVSIM | PMDS | 90.2 | 88.1 |
| Trajectory | nuScenes | L2-avg | 0.35 | 0.37 (UniAD) |

在nuScenes BEV 3D检测中，Percept-WAM以58.9 mAP超越PointPillars的52.3 mAP，但在NAVSIM规划任务中，其90.2 PMDS仅比DiffusionDrive高2.1分，表明感知增强对规划的边际收益有限。

| 消融项 | nuScenes mAP | nuScenes NDS | 变化 |
|---|---|---|---|
| Baseline (Camera) | 25.0 | 25.7 | - |
| + Lidar Encoder | 33.2 | 32.2 | +8.2 / +6.5 |
| + Data Augmentation | 41.3 | 39.2 | +8.1 / +7.0 |
| + Number of Sampling Grids | 50.4 | 46.6 | +9.1 / +7.4 |
| + MLP Parallel (16× speedup) | 50.4 | 43.7 | 0 / -2.9 |

消融实验显示，LiDAR编码器与数据增强对mAP贡献最大（各提升约8分），而增加采样网格数量进一步提升9.1分。值得注意的是，MLP并行解码虽带来16倍加速，但NDS下降2.9分，暗示并行机制可能牺牲了部分长程依赖建模能力。

评估边界方面，论文未报告置信区间，且nuScenes BEV检测的58.9 mAP低于领域综述中HENet++的63.7 NDS（协议不同，NDS为综合指标，不可直接比mAP，但绝对精度差距显著）。代码未公开，流式推理的双重计算机制细节仅在附录提及，可复现性受限。

## 关联研究分析

从问题动机看，Percept-WAM与UFO（Unfolding the Future of Object detection）共享网格查询思路，但UFO依赖外部检测头，而Percept-WAM将检测内嵌于VLM序列生成中。这一差异源于任务特性：UFO旨在提升检测精度，而Percept-WAM需同时保留VLM的推理能力以支持规划。然而，Percept-WAM的隐式对齐策略在极端标定误差下是否比BEVFusion的显式几何投影更鲁棒，论文未提供对比实验，仅通过LiDAR初始化World-BEV令牌间接缓解几何偏差。

从方法设计看，Percept-WAM与DiffusionDrive同属端到端范式，但后者采用扩散解码器生成轨迹，缺乏LLM推理能力。Percept-WAM通过World-Action令牌对齐感知特征，实现了推理与控制的统一。然而，其并行自回归解码机制在NAVSIM上的性能提升（2.1 PMDS）远小于感知精度的提升（6.6 mAP），暗示VLM骨干在轨迹预测中的几何精度仍受限于其预训练分布，而非感知模块的增强。

## 总结

Percept-WAM旨在解决VLM几何定位弱与端到端驾驶鲁棒性之间的矛盾，其切入点在于将空间理解重构为可重建的世界状态表示，而非问答任务。通过引入编码度量坐标与置信度的World-PV/BEV令牌，模型在单一VLM内统一了2D/3D感知与轨迹预测。实验证明，该框架在nuScenes BEV 3D检测中达到58.9 mAP，NAVSIM规划任务中PMDS达90.2，验证了感知增强对端到端性能的提升。然而，其绝对精度仍低于专用检测器，且并行解码导致的NDS下降暗示了效率与精度的权衡。当LiDAR输入缺失或标定误差增大时，隐式对齐策略的鲁棒性是否优于显式投影，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.19221)