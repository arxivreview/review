# CVPR2026最新论文 ｜LiREC-Net: A Target-Free and Learning-Based Network for LiDAR, RGB, and Event Calibration ｜LiREC-Net：面向LiDAR、RGB与事件相机的无目标三模态联合标定

研究机构：德国人工智能研究中心、丰田研究所

作者：Aditya Ranjan Dash、Ramy Battrawy、René Schuster 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.21754)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.21754)

> 多传感器融合感知要求LiDAR、RGB相机与事件相机在统一坐标系下空间对齐，但现有学习基标定方法仅支持双模态独立训练，导致三传感器系统存在冗余计算与对齐不一致风险。LiREC-Net通过共享LiDAR特征分支与成对代价体机制，在单一端到端网络中同时回归LiDAR-RGB与LiDAR-Event外参，实现了三模态联合标定。该方法在DSEC数据集上取得了1.18cm/0.07°的LiDAR-Event标定精度，验证了统一框架的可行性，但其依赖RGB与事件相机预标定的假设限制了全自主部署的潜力。

## 研究背景

多传感器标定需解决异构数据在时空域的对齐问题。LiDAR提供稀疏3D几何结构，RGB相机提供密集纹理与色彩信息，事件相机则以异步高时间分辨率捕捉动态场景。三者外参估计依赖于跨模态特征匹配，而自然场景中缺乏人工标定板，使得基于几何约束的显式优化难以直接应用。深度学习通过端到端回归外参，摆脱了对特定几何特征的依赖，成为无目标标定的主流范式。

现有学习基标定方法如LCCNet、CalibNet及MULiEv均针对单一传感器对设计，分别处理LiDAR-RGB或LiDAR-Event标定。这种双模态独立架构导致三传感器系统需部署两个独立网络，不仅增加计算开销，更因各网络独立优化而引入跨模态对齐的不一致性。LiREC-Net的切入点在于构建统一三模态框架，通过共享LiDAR表示消除冗余，并在单一网络中同时优化两对传感器外参，解决多模态扩展中的效率与一致性矛盾。

## 核心方法

### 方法参照系

LiREC-Net继承LCCNet的代价体（Cost Volume）与迭代细化机制，但将双模态独立架构扩展为三模态统一框架。关键差异在于引入共享LiDAR分支，使同一LiDAR特征同时服务于LiDAR-RGB与LiDAR-Event两条标定路径，而非为每对传感器构建独立编码器。

### 共享LiDAR特征融合

传统双模态方法中，LiDAR特征需为每对传感器独立编码，导致参数冗余与计算重复。LiREC-Net采用点云与深度图双路编码策略，通过Point-Transformer-V3提取3D点云几何结构，同时利用Mobile-Vision-Transformer-V2处理投影深度图。两路特征经缩放投影（SDP/SFP）对齐分辨率后，通过通道拼接融合为统一LiDAR嵌入：

$$\mathbf{F}_{Li} = \text{Concat}(\text{SFP}(\mathbf{F}_{point}), \text{SDP}(\mathbf{F}_{depth}))$$

该融合策略解决了稀疏点云在弱纹理场景下特征歧义问题，点云特征提供精细几何结构，深度图特征补充稠密空间上下文，二者互补提升了外参估计的鲁棒性。

### 成对代价体与迭代细化

在共享LiDAR嵌入基础上，LiREC-Net为LiDAR-RGB与LiDAR-Event分别构建代价体，通过通道归一化内积计算跨模态相似度：

$$C(p, \Delta) = \frac{\mathbf{F}_{Li}(p) \cdot \mathbf{F}_{Cam}(p + \Delta)}{\|\mathbf{F}_{Li}(p)\| \|\mathbf{F}_{Cam}(p + \Delta)\|}$$

代价体经DenseNet风格上下文模块细化后，由预测头回归平移向量与四元数旋转。迭代细化机制通过多阶段训练，从大扰动范围逐步缩小至小扰动，模拟在线校准的渐进收敛过程，解决了大初始扰动下梯度优化易陷入局部最优的问题。

## 实验评估

| 数据集 | 方法 | LiDAR-RGB 平移/旋转 (cm/°) | LiDAR-Event 平移/旋转 (cm/°) |
|---|---|---|---|
| KITTI | LiREC-Net | 1.80 / 0.11 | 1.82 / 0.12 |
| KITTI | PseudoCal | 1.18 / 0.05 | — |
| DSEC | LiREC-Net* | 2.51 / 0.14 | 1.18 / 0.07 |
| DSEC | MULiEv_△ | — | 0.81 / 0.10 |

LiREC-Net在KITTI上LiDAR-RGB平移误差1.80cm，略高于PseudoCal的1.18cm，但旋转误差0.11°优于后者的0.05°；在DSEC上LiDAR-Event精度1.18cm/0.07°，优于MULiEv的0.81cm/0.10°。基线覆盖学习基双模态方法，但缺失几何显式优化类基线如RAVES-Calib，限制了与不同技术路线的公平对比。

| 消融组件 | LiDAR-RGB 平移/旋转 (cm/°) | LiDAR-Event 平移/旋转 (cm/°) |
|---|---|---|
| 完整模型 | 2.51 / 0.14 | 1.18 / 0.07 |
| 仅点云特征 | 14.43 / 0.70 | 14.05 / 0.64 |
| 仅深度特征 | 2.97 / 0.70 | 2.16 / 0.60 |
| 无SDP/SFP | 3.37 / 0.34 | 3.35 / 0.30 |

消融实验显示，移除点云或深度特征任一分支均导致性能急剧下降，证实双路融合的必要性；去除缩放投影机制使LiDAR-Event旋转误差从0.07°升至0.30°，表明投影精度对特征对齐的关键作用。MViTV2骨干优于ResNet，全局特征建模对跨模态对齐具有显著增益。

评估指标仅包含平移与旋转误差，未报告下游任务性能如3D检测mAP，无法直接验证标定精度对感知任务的影响。KITTI数据集使用V2E合成事件数据，其分布与真实事件相机存在差异，可能高估LiDAR-Event标定精度。论文未提供代码与完整超参数，可复现性受限。

## 关联研究分析

从方法设计看，LiREC-Net与LCCNet共享代价体与迭代细化机制，但LCCNet针对LiDAR-RGB双模态优化，而LiREC-Net通过共享LiDAR分支实现三模态统一。这一差异源于任务特性：三传感器系统需保证LiDAR与两个相机的对齐一致性，独立网络无法强制跨模态约束。然而，共享分支是否限制了各模态独立优化空间，论文未给出消融验证。

从问题动机看，LiREC-Net与RLCNet均关注在线校准，但RLCNet采用加权移动平均应对漂移，而LiREC-Net依赖多阶段静态细化。RLCNet的在线机制更适合长期部署中的持续漂移补偿，LiREC-Net的迭代细化更适用于大初始扰动下的快速收敛。两者在实时性与鲁棒性间做出不同取舍，LiREC-Net未评估帧级实时性，其多阶段推理耗时0.33s，可能不满足L4级自动驾驶的实时要求。

## 总结

LiREC-Net解决的核心矛盾是三传感器系统中双模态独立标定导致的冗余计算与对齐不一致。其切入点在于共享LiDAR特征分支，通过单一网络同时优化LiDAR-RGB与LiDAR-Event外参，避免了独立网络的参数重复与跨模态冲突。该方法在DSEC上实现1.18cm/0.07°的LiDAR-Event精度，验证了统一框架的有效性。然而，论文假设RGB与事件相机预标定，未联合估计相机间相对位姿，限制了全自主部署能力。当移除预标定假设后，共享LiDAR分支是否仍能维持跨模态一致性，论文未提供实验证据。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.21754)