# HuggingFace最新推荐论文 ｜GroupEnsemble: Efficient Uncertainty Estimation for DETR-based Object Detection ｜GroupEnsemble：基于查询组并行的DETR不确定性估计

研究机构：德国斯图加特大学

作者：Yutong Yang、Katarina Popović、Julian Wiederer 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.01847)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.01847)

> 目标检测模型在安全关键场景中需同时量化语义与空间不确定性，但现有集成方法因多次前向传播导致高延迟，难以满足实时需求。本文利用DETR解码器的固有并行性，通过推理时并行处理多组对象查询并施加注意力掩码隔离组间交互，在单次前向传播中生成多个独立检测集。该方法在Cityscapes上以18.4ms延迟实现了21.4的PDQ，超越了53.4ms延迟的Deep Ensembles，但其校准精度（D-ECE 10.4）仍略逊于显式集成（9.8），查询组多样性对极端分布偏移的鲁棒性尚待验证。

## 研究背景

DETR将目标检测重构为集合预测问题，摒弃了非极大值抑制（NMS）与锚框等手工组件，其核心机制是通过可学习的对象查询在Transformer解码器中并行提取目标特征。然而，DETR输出的确定性边界框仅反映语义置信度，无法捕捉定位与尺寸的空间不确定性。在自动驾驶等场景中，高置信度的类别预测并不保证边界框位置的可靠性，这种语义与空间不确定性的解耦缺失，使得模型无法全面评估检测结果的可靠性。

不确定性量化（UQ）的主流路线是集成方法，通过聚合多个独立预测来近似贝叶斯后验。深度集成（Deep Ensembles）通过训练多个独立模型确立了性能基准，但其内存与计算成本随成员数线性增长，在实时应用中不可行。蒙特卡洛Dropout（MC-Dropout）虽降低了内存开销，但推理时需多次前向传播，延迟问题依然严峻。现有UQ技术多针对CNN架构设计，忽视了DETR解码器固有的并行处理能力，导致在DETR类检测器上缺乏高效且能同时量化语义与空间不确定性的专用方法。

## 核心方法

### 方法参照系

本文问题属于高效集成架构中的隐式集成分支，与BatchEnsemble等共享骨干方法一致，旨在通过参数共享降低推理成本。关键差异在于，本文不修改权重矩阵或引入低秩扰动，而是直接利用Group DETR训练时已生成的多组对象查询，将其从训练加速工具转化为推理时的集成成员，避免了额外的参数训练或架构修改。

### 多查询组并行推理

传统DETR推理仅使用第一组查询，丢弃其余组。本文在推理时保留所有 $G$ 组查询，每组包含 $N$ 个查询，总查询数 $W = G \cdot N$。为确保各组独立检测，设计自注意力掩码 $M_{SA}$ 阻断组间交互：

$$
m_{SA}^{ij} = \begin{cases} 1 & \text{if } \lfloor (i-1)/N \rfloor \neq \lfloor (j-1)/N \rfloor \\ 0 & \text{otherwise} \end{cases}
$$

该掩码允许组内查询充分交互，同时隔离不同组，使解码器能并行处理所有查询组，在单次前向传播中生成 $G$ 个独立检测集 $\mathcal{Y} = \{\mathbf{Y}_1, \dots, \mathbf{Y}_G\}$。这一设计解决了MC-Dropout与Deep Ensembles因串行多次前向传播导致的高延迟问题，将推理时间从线性增长压缩至常数级。

### 跨组聚类与不确定性聚合

各检测集存在显著重叠，需通过聚类聚合生成最终检测与不确定性估计。采用基本顺序算法（BSAS）对检测进行聚类，每个簇包含高IoU且同类别的检测。对于簇内检测，最终边界框为均值，空间不确定性由坐标协方差矩阵捕捉；语义不确定性通过缩放最大置信度计算：

$$
c_{final} = c_{max} \cdot \frac{n_{det}}{G}
$$

其中 $n_{det}$ 为簇内检测数。该聚合策略解决了确定性检测无法量化空间不确定性、而简单平均置信度导致过度自信的问题，通过簇大小隐式编码不确定性，使置信度与检测可靠性对齐。

## 实验评估

实验在Cityscapes、Foggy Cityscapes与COCO上进行，基线覆盖确定性DETR、MC-Dropout与Deep Ensembles，但缺失BatchEnsemble、SVE等最新隐式集成方法对比。主实验结果显示，MC-GroupEnsemble在Cityscapes上PDQ达21.4，超越Deep Ensembles的19.3，且延迟仅为18.4ms（Deep Ensembles为53.4ms）；在Foggy Cityscapes域偏移场景下，PDQ 19.1亦优于Deep Ensembles的17.5。

| 数据集 | 方法 | PDQ (thr. 0.3) | D-ECE (thr. 0.3) | mAP | 延迟 (ms) | 参数量 (M) |
|---|---|---|---|---|---|---|
| Cityscapes | Deep Ensembles | 19.3 | 9.8 | 38.8 | 53.4 | 89.27 |
| Cityscapes | MC-GroupEnsemble | 21.4 | 10.4 | 39.2 | 18.4 | 43.48 |
| Foggy Cityscapes | Deep Ensembles | 17.5 | 12.1 | 26.4 | 53.4 | 89.27 |
| Foggy Cityscapes | MC-GroupEnsemble | 19.1 | 14.0 | 26.6 | 18.4 | 43.48 |

消融实验表明，查询组数量从1增至5时，PDQ从9.4提升至18.8，但增至9时仅微升至19.7，显示边际收益递减；延迟从10.68ms增至26.55ms，呈线性增长。置信度聚合策略中，缩放最大置信度（Max Conf. w/ Scaling）在PDQ（18.8）与D-ECE（10.4）上均优于均值（16.2/14.1）与未缩放最大值（15.9/13.4），验证了簇大小编码不确定性的有效性。

评估协议存在局限：未报告置信区间，数值比较需谨慎；Foggy Cityscapes仅测试150m能见度单一条件，未覆盖多域偏移；代码已开源，但超参数（如BSAS阈值 $\theta=0.7$）的敏感性分析缺失，可复现性依赖特定实现细节。

## 关联研究分析

从问题动机看，本文与Hydra Ensembles（Gabetni et al., 2025）同属高效集成路线，但Hydra通过注意力头剪枝生成变体模型，依赖预训练模型容量损失换取单次前向传播，而GroupEnsemble利用Group DETR训练时已存在的多查询组，无需修改架构或损失部分容量。这一差异源于任务特性：DETR的查询机制天然支持多集合预测，而Transformer分类任务需通过剪枝或低秩扰动人为生成多样性，导致Hydra在ImageNet-1k上OOD检测准确率（57.12%）与Deep Ensembles持平，但GroupEnsemble在检测任务上实现了PDQ超越，暗示查询组多样性在空间不确定性估计中更具优势。

从方法设计看，本文与SVE（Turkoglu et al., 2026）均基于预训练模型，但SVE冻结奇异向量仅训练奇异值，依赖预训练知识子空间的正交性，而GroupEnsemble直接利用训练时随机初始化带来的查询组多样性，无需额外参数训练。SVE在Flowers102上校准性能与Deep Ensembles相当，但GroupEnsemble在D-ECE上略逊（10.4 vs 9.8），可能源于BSAS聚类对置信度的平滑效应，而非查询组多样性不足。这一差异提示，隐式集成的校准性能可能受聚合策略影响，而非仅取决于成员独立性。

## 总结

本文核心矛盾是DETR检测中语义与空间不确定性解耦缺失与集成方法高延迟的冲突。切入点在于利用DETR解码器固有并行性，将Group DETR的多查询组从训练工具转化为推理集成成员，通过注意力掩码隔离组间交互实现单次前向传播的多集合预测。方法上，GroupEnsemble并行处理 $G$ 组查询，MC-GroupEnsemble结合MC-Dropout增强随机性，在Cityscapes上以18.4ms延迟实现21.4 PDQ，超越Deep Ensembles的19.3 PDQ与53.4ms延迟。边界在于D-ECE 10.4略高于Deep Ensembles的9.8，且Foggy Cityscapes仅测试单一能见度条件，查询组多样性在极端分布偏移下的鲁棒性未充分验证。当BSAS聚类阈值 $\theta$ 从0.7变化时，D-ECE是否随簇大小分布变化而显著波动，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.01847)