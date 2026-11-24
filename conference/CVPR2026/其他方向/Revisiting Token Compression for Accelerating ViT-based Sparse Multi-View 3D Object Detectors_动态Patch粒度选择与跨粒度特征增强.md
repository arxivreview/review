# CVPR2026最新论文 ｜Revisiting Token Compression for Accelerating ViT-based Sparse Multi-View 3D Object Detectors ｜动态Patch粒度选择与跨粒度特征增强

研究机构：南京大学

作者：Mingqian Ji、Shanshan Zhang、Jian Yang

论文原文见 [arXiv](https://arxiv.org/abs/2604.14563)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14563)

> 稀疏多视角3D目标检测器依赖Vision Transformer（ViT）提取高质量图像特征，但密集Token处理导致推理延迟高企，阻碍了实时部署。现有Token压缩策略如剪枝、合并或简单扩大Patch Size，在3D检测任务中会丢失背景负样本线索或破坏细粒度语义，导致精度显著下降。SEPatch3D通过基于时空Query分布动态调整Patch粒度，并利用熵值筛选信息丰富区域进行跨粒度特征融合，在保持检测精度的同时大幅降低计算开销。该方法在nuScenes上实现了57%的推理加速，但其在不同分辨率下的泛化能力及对非ViT骨干的适用性仍存疑。

## 研究背景

稀疏Query检测器通过可学习Query直接关联图像特征，避免了稠密鸟瞰图（BEV）构建的计算冗余，因此与表征能力强的ViT骨干高度适配。然而，ViT的计算复杂度随Token数量呈二次方增长，当输入分辨率较高时，骨干网络的推理延迟成为系统瓶颈。这种延迟在需要实时处理的自动驾驶场景中尤为致命，迫使研究者寻找在不牺牲精度的前提下压缩Token数量的策略。

主流Token压缩路线包括Token剪枝、Token合并和Patch Size扩大。Token剪枝基于启发式规则移除低重要性Token，但可能丢弃对Hard Negative学习至关重要的背景区域；Token合并通过聚合相似Token减少数量，但非规则聚合会破坏上下文一致性；Patch Size扩大虽能保留整体语义，但过大的Patch会丢失物体识别所需的细粒度细节。SEPatch3D的切入点在于，将压缩策略从静态的“一刀切”转变为动态的“时空自适应”，即根据场景中物体的距离和运动趋势调整Patch粒度，并通过特征增强机制弥补粗粒度Patch带来的信息损失。

## 核心方法

### 方法参照系

本文问题属于ViT加速中的Token压缩范畴，但区别于传统的结构化剪枝或固定比例合并。标准流程通常在Patch嵌入阶段后执行静态压缩，而本文的关键差异在于将压缩决策前移至Patch嵌入阶段，并引入跨粒度特征交互，使压缩过程具备时空感知能力。

### 时空感知Patch Size选择

传统方法固定Patch Size或基于单一深度阈值调整，忽略了物体运动导致的场景动态变化，导致相邻帧间Patch粒度突变或细节丢失。SEPatch3D利用前一帧的物体Query深度均值 $\bar{D}_{T-1}$ 及其线性回归斜率变化 $\Delta S_{T-1}$ 动态决定当前帧的Patch Size $P_T$。

$$ P_T = \begin{cases} P_l & \text{if } \bar{D}_{T-1} > \theta \text{ and } \Delta S_{T-1} > 0 \\ P_s & \text{if } \bar{D}_{T-1} < \theta \text{ and } \Delta S_{T-1} < 0 \\ P_{T-1} & \text{otherwise} \end{cases} $$

该公式表明，当物体远离且深度趋势增大时，使用大Patch $P_l$ 以降低背景计算量；当物体靠近且深度趋势减小时，使用小Patch $P_s$ 以保留细节；否则保持上一帧设置以确保时序稳定性。这种设计解决了静态策略无法适应物体运动轨迹的问题，实现了计算资源在前景与背景间的动态分配。

### 信息丰富Patch选择与跨粒度增强

仅扩大Patch Size会导致纹理丰富区域的信息丢失，而简单的Top-K选择无法适应场景复杂度的变化。SEPatch3D首先通过运动对齐的历史Query增强当前Patch特征，然后计算归一化特征的熵 $H_j$ 来识别信息丰富区域。

$$ H_j = -\sum_{c=1}^{C} \frac{\tilde{F}_{j,c}}{\|\tilde{F}_j\|_2} \log \left( \frac{\tilde{F}_{j,c}}{\|\tilde{F}_j\|_2} \right) $$

熵值高的Patch对应浅层纹理丰富或边缘区域，这些区域在粗粒度嵌入中易丢失细节。模块选择熵值高于场景平均值的Patch，并通过交叉注意力将细粒度Patch特征注入对应的粗粒度Patch。这一机制弥补了动态Patch Size选择带来的细节损失，确保了关键语义信息的完整性。

## 实验评估

实验在nuScenes和Argoverse 2验证集上进行，基线包括StreamPETR、ToC3D等稀疏检测器。对比方法覆盖了Token剪枝（ToC3D）和解码器加速（tgGBC）路线，但缺乏与通用ViT压缩方法（如DynamicViT）在3D检测任务上的直接对比，限制了方法通用性的评估。

| 方法 | 骨干 | NDS (%) | mAP (%) | 推理时间 (ms) |
|---|---|---|---|---|
| StreamPETR | ViT-L | 61.2 | 52.1 | 317.0 |
| ToC3D-faster | ViT-L | 60.5 | 51.3 | 237.2 |
| SEPatch3D-fast | ViT-L | 61.2 | 52.1 | 250.2 |
| SEPatch3D-faster | ViT-L | 60.3 | 51.6 | 194.3 |

在320×800分辨率下，SEPatch3D-faster相比StreamPETR推理时间减少38.7%，NDS仅下降0.9%；相比ToC3D-faster，推理时间快17.6%且NDS高0.8%。在640×1600高分辨率下，SEPatch3D-faster推理时间减少57.7%，NDS保持62.4%，显著优于ToC3D-faster的61.1%和817.7ms。

| 模块 | NDS (%) | 推理时间 (ms) | 参数量 (M) |
|---|---|---|---|
| Baseline | 61.2 | 317.0 | 316.62 |
| + SPSS | 58.8 | 189.1 | 318.77 |
| + CGFE | 60.4 | 209.6 | 325.58 |
| + IPS | 60.3 | 194.3 | 328.13 |

消融实验显示，SPSS模块单独使用时NDS下降2.4%，但推理时间大幅降低；加入CGFE后NDS恢复至60.4%，验证了特征增强对精度损失的补偿作用。IPS模块进一步微调NDS至60.3%，参数量增加3.6%，表明熵值选择机制在精度与效率间取得了平衡。

评估指标涵盖NDS、mAP及推理时间，但未报告内存占用和能耗数据，限制了边缘部署场景的评估。代码已开源，超参数如深度阈值 $\theta=0.6$ 和Query数量 $M=64$ 在论文中明确给出，实验在单张RTX 3090 GPU上完成，具备可复现性。

## 关联研究分析

从问题动机看，SEPatch3D与ToC3D均旨在加速ViT稀疏检测器，但ToC3D依赖静态Patch剪枝，而SEPatch3D采用动态粒度选择。ToC3D的静态策略在物体距离变化剧烈时易导致细节丢失，而SEPatch3D通过时空Query分布自适应调整，更好地平衡了前景细节与背景计算量。这一差异源于3D检测任务对物体距离敏感的特性，静态方法无法捕捉这种动态变化。

从方法设计看，SEPatch3D与DynamicViT同属动态推理范畴，但DynamicViT基于注意力权重进行Token剪枝，而SEPatch3D基于时空Query深度进行Patch粒度调整。DynamicViT的剪枝策略可能丢弃背景负样本，而SEPatch3D通过保留背景区域并增强前景细节，更适合3D检测任务。这种设计差异反映了任务特性对压缩策略的约束：分类任务可容忍背景丢失，而检测任务需保留负样本线索。

## 总结

SEPatch3D解决了ViT稀疏3D检测器中Token压缩导致的精度-效率失衡问题。现有静态压缩策略无法适应物体运动引起的场景动态变化，而SEPatch3D通过时空感知Patch Size选择和跨粒度特征增强，实现了动态计算分配与细节保留的统一。实验表明，该方法在nuScenes上实现了57%的推理加速，NDS仅下降0.9%。然而，论文仅在ViT-L骨干上验证了方法有效性，未探索其在ViT-B或CNN骨干上的泛化能力。当骨干网络从ViT-L缩小到ViT-B时，动态Patch Size选择的精度保持能力是否依然稳健，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14563)