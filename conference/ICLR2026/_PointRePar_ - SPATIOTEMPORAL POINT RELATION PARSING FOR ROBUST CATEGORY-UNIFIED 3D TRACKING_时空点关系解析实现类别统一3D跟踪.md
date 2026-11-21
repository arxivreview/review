# ICLR2026最新论文 ｜_PointRePar_ : SPATIOTEMPORAL POINT RELATION PARSING FOR ROBUST CATEGORY-UNIFIED 3D TRACKING ｜时空点关系解析实现类别统一3D跟踪

作者：Juntao Liu、Zikun Zhou、Zhuotao Tian 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_88415066)

> 3D单目标跟踪（3D SOT）旨在从稀疏LiDAR点云流中持续估计目标位姿，其核心难点在于远距离下的特征缺失与长时程误差累积。现有主流方法采用逐类训练范式以换取单类精度，却牺牲了跨类别泛化能力与训练效率，而早期类别统一尝试因特征可分性差与时间建模不足而性能落后。PointRePar通过Mamba架构解析多尺度空间点关系，并引入Box级长期轨迹校正与条件高斯扰动，在联合训练下逼近甚至超越最佳逐类方法。该工作验证了类别统一范式在稀疏场景下的鲁棒性优势，但其平均性能仍略低于顶级逐类基线，且缺乏对Mamba扫描顺序敏感性的深入探讨。

## 研究背景

LiDAR点云在远距离或遮挡下极度稀疏，导致传统基于外观匹配的孪生网络（Siamese Network）难以提取稳定的目标特征。为应对这一物理约束，研究者引入运动建模与记忆机制，但多数方法仍依赖逐类训练（Category-Specified Training）范式，即针对每个物体类别单独优化模型。这种范式虽能降低单类拟合复杂度，却阻碍了模型学习跨类别的通用几何模式，且在部署时需维护多个独立模型，效率低下。

3D SOT领域长期存在“精度-泛化”权衡：逐类方法如SiamMo在KITTI数据集上取得了72.3%的Success指标，但无法直接迁移至新类别；而首个类别统一方法CUTrack因PointNet++骨干的特征空间混淆及缺乏有效时间建模，其Mean Success仅为40.41%，远低于逐类基线。PointRePar的切入点在于识别出此前方法失败的根源并非范式本身，而是特征提取器未能同时解决单帧空间可分性与帧间时间一致性问题。通过重构骨干网络并引入显式的时空关系解析模块，该工作试图在保持联合训练效率的同时，弥补类别统一范式在特征质量上的短板。

## 核心方法

### 方法参照系

PointRePar遵循粗到细（Coarse-to-Fine）的两阶段跟踪框架，这与M2-Track和SeqTrack3D等主流方法一致。第一阶段利用轻量级SegPointNet生成粗略边界框，第二阶段通过交叉注意力解码器进行精细化定位。与通用流程的关键差异在于，其精炼阶段的特征编码器摒弃了传统的PointNet++或Transformer，转而采用基于状态空间模型（State Space Model, SSM）的Mamba架构，以线性复杂度处理无序点云序列。

### 多尺度空间关系解析

传统PointNet++骨干在单帧编码中难以区分前景与背景点，导致特征空间混淆。PointRePar引入U形空间关系解析Mamba（USRPM）与动态特征聚合（Dynamic Feature Aggregation, DFA）模块。DFA通过为每个点生成偏移量与权重，动态调整感受野以增强几何感知。其核心公式为：

$$ \hat{f}_i = \sum_{k=1}^{K} w_{ik} \cdot \text{IDW}(p_i + \Delta p_{ik}) $$

其中IDW为逆距离加权插值。该设计使模型能自适应不同尺度目标的形状细节，显著提升了单帧内目标与背景的特征可分性，解决了CUTrack中AdaFormer骨干的特征混淆问题。

### 长期时间关系解析与条件扰动

仅靠空间特征不足以应对长时程漂移，PointRePar在点级时间建模基础上，新增Box级长期运动轨迹校正（LMTR）模块。该模块将历史边界框序列转化为Token，通过Mamba块捕捉长程1D序列依赖，并聚合为解码器查询。同时，针对稀疏场景下检测误差更大的特性，提出条件高斯扰动（CGP）：

$$ \epsilon_x = \beta_x \cdot e^{-c \cdot r} \cdot \mathcal{N}(0,1) $$

其中$r$为场景稀疏度比率，$c$控制噪声衰减。该机制在训练时动态模拟真实检测误差分布，增强了模型在低密度点云下的鲁棒性，弥补了传统均匀噪声注入忽视场景复杂度的缺陷。

## 实验评估

| 方法 | 范式 | KITTI Mean Suc | KITTI Mean Prec | NuScenes Mean Suc | NuScenes Mean Prec |
| :--- | :--- | :--- | :--- | :--- | :--- |
| SiamMo | 逐类 | 72.3 | 90.1 | 60.31 | 72.68 |
| MoCUT | 统一 | 65.8 | 85.0 | 51.19 | 64.63 |
| PointRePar | 统一 | 72.0 | 89.1 | 64.15 | 76.81 |

PointRePar在KITTI和NuScenes上均显著超越类别统一基线MoCUT，其中NuScenes Mean Success提升15.57%。在KITTI上，其Mean Success（72.0%）与顶级逐类方法SiamMo（72.3%）持平，但在NuScenes稀疏场景下，PointRePar（64.15%）反超SiamMo（60.31%），验证了类别统一范式在跨域稀疏数据上的泛化优势。

| 模块 | KITTI Mean Suc | 增益 |
| :--- | :--- | :--- |
| Baseline (无DFA/USRPM/LMTR/CGP) | 65.7 | - |
| + DFA | 68.9 | +3.2 |
| + USRPM | 69.9 | +1.0 |
| + LMTR | 68.6 | -1.3 |
| + CGP | 68.7 | +0.1 |
| Full Model | 72.0 | +6.3 |

消融实验显示，DFA模块贡献最大（+3.2%），证实空间特征可分性是性能瓶颈。LMTR单独引入时性能下降，表明其需依赖DFA提供的优质空间特征才能发挥时间校正作用，体现了模块间的强耦合依赖。CGP的增益较小但稳定，说明其主要在极端稀疏场景下发挥作用。

实验在KITTI、NuScenes及WOD上进行，采用One Pass Evaluation协议。代码未公开，训练使用单卡RTX 3090，推理速度36.6 FPS。评估指标仅包含Success与Precision，缺乏HOTA等多目标跟踪常用指标，且未报告置信区间。WOD测试仅用于验证KITTI预训练模型的跨域泛化，未提供独立训练结果。

## 关联研究分析

从问题动机看，PointRePar与CUTrack同属类别统一范式，但CUTrack依赖可变形分组向量注意力，而PointRePar采用Mamba解析点关系。差异根源在于特征提取器的选择：CUTrack的AdaFormer在单帧编码中特征可分性差，而PointRePar的DFA通过动态感受野显式增强几何细节，这解释了为何PointRePar在稀疏场景下大幅领先。从方法设计看，PointRePar与MambaTrack3D均引入SSM，但MambaTrack3D聚焦帧间传播以解决时间冗余，而PointRePar将Mamba用于空间U-Net结构以解决空间混淆。这种差异反映了SSM在无序点云处理中的两种应用路径：序列建模与空间结构解析，后者对扫描顺序的敏感性尚未被充分探讨。

## 总结

PointRePar旨在解决3D SOT中逐类训练范式导致的泛化能力缺失与效率低下问题。其切入点在于识别出特征空间可分性与时间一致性是类别统一失败的根源，并通过DFA与LMTR模块协同解决。实验证明，该模型在NuScenes稀疏场景下Mean Success达64.15%，超越逐类SOTA SiamMo的60.31%，但在KITTI密集场景下（72.0% vs 72.3%）仍略逊于SiamMo。这一边界揭示了类别统一范式在数据充足且类别特征差异大时，可能因共享参数而牺牲单类极致性能。当支持集规模进一步扩大或类别间几何差异显著时，联合训练是否仍能保持对逐类方法的竞争力，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_88415066)