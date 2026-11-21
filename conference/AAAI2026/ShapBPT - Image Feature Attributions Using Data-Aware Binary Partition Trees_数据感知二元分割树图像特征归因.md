# AAAI2026最新论文 ｜ShapBPT: Image Feature Attributions Using Data-Aware Binary Partition Trees ｜数据感知二元分割树图像特征归因

作者：Muhammad Rashid、Elvio G. Amparore、Enrico Ferrari 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.07047)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.07047)

> 图像分类模型的黑盒决策机制难以通过像素级重要性分数直观还原，传统基于轴对齐网格的Shapley值计算方法因忽略图像形态学结构导致收敛缓慢且定位模糊。ShapBPT通过引入数据感知的二元分割树层级结构替代固定网格，将Shapley系数计算与图像内在形态对齐，从而在保持理论保证的同时显著提升收敛效率。该方法在多个视觉任务上优于现有Shapley类及梯度类解释器，并获20名受试者偏好验证，但其对纹理复杂或抽象图像的泛化能力尚存疑。

## 研究背景

理解图像分类器为何做出特定预测，需量化每个像素对输出的边际贡献。这一任务通常通过特征移除（Masking）实现：将部分像素替换为背景值，观察模型输出变化。Shapley值（SHapley Additive exPlanations）基于合作博弈论，为每个特征分配满足局部准确性、一致性和缺失性公理的贡献分数，成为行业标准基线。然而，精确计算Shapley值复杂度为#P-hard，对含数千像素的图像不可行。

现有主流方案采用层级近似策略。SHAP Partition Explainer使用轴对齐（Axis-Aligned, AA）网格，将图像递归划分为矩形区域，通过Owen公式在层级结构上计算近似Shapley值。该方法虽降低了计算成本，但AA网格是数据无关的几何划分，无法适应图像中物体的实际轮廓，导致需大量递归评估才能定位关键区域。LIME（Local Interpretable Model-agnostic Explanations）虽利用预定义分割识别相关区域，但其分割固定且不可细化，缺乏反馈机制。ShapBPT的切入点在于：将层级结构从固定的AA网格替换为数据感知的二元分割树（Binary Partition Tree, BPT），使分割边界对齐图像形态学特征，从而减少达到相同解释精度所需的模型评估次数。

## 核心方法

### 层级联盟结构与Owen近似

ShapBPT基于层级联盟结构（Hierarchical Coalition Structures, HCS）计算Shapley值。在HCS中，图像像素被组织为递归划分的树结构，每个节点代表一个联盟（Coalition）。对于二元HCS，Owen近似公式通过递归组合子联盟计算联盟价值 $\Omega_i(T)$。该公式的核心在于，当联盟 $T$ 可进一步划分为 $T_1$ 和 $T_2$ 时，玩家 $i$ 的价值由其所在子联盟的边际贡献加权决定。这一设计动机在于：精确Shapley值计算不可行，而层级结构允许通过分组特征大幅降低计算成本，同时保留Shapley值的公理性质。

### 数据感知BPT层级构建

ShapBPT的核心创新在于BPT层级的构建方式。不同于AA网格沿最长轴均匀分割，BPT采用自底向上的合并策略，从单个像素开始，迭代合并相邻分区。合并准则由数据感知的距离函数决定：

$$
d(T_i, T_j) = \text{clr}_2(T_i, T_j) \times \text{area}(T_i, T_j) \times \text{pr}(T_i, T_j)
$$

其中 $\text{clr}_2$ 为合并后区域所有颜色通道的颜色范围平方和，$\text{area}$ 和 $\text{pr}$ 分别为面积和周长。该公式的物理含义是：优先合并颜色均匀、形状连贯且面积适中的相邻区域，以最大化感知区域的一致性。这种数据感知特性解决了AA网格无法适应物体轮廓的问题，使得BPT层级在较少递归步骤内即可定位关键区域，从而在相同评估预算下获得更清晰的显著性图。

## 实验评估

实验在ImageNet-S50、MS-COCO、CelebA、MVTec等数据集上，使用ResNet50、SwinViT、Yolo11s等模型进行评估。基线覆盖Shapley类（SHAP-AA、LIME）和梯度类（GradCAM、LRP、IDG、GradShap），但未对比最新的ViT专用归因方法（如RFEM）或形式化方法（FAME）。论文报告了响应型指标（AUC）和真值型指标（IoU），其中AUC-IoU衡量解释与模型行为的一致性，max-IoU衡量与地面真值的匹配度。

| 方法 | 数据集 | 模型 | AUC-IoU | max-IoU |
|---|---|---|---|---|
| BPT-1000 | ImageNet-S50 | ResNet50 | 0.1844 | 0.85 |
| AA-1000 | ImageNet-S50 | ResNet50 | 0.1409 | 0.72 |
| LIME-1000 | ImageNet-S50 | ResNet50 | 0.1174 | 0.65 |
| GradCAM | ImageNet-S50 | ResNet50 | 0.1146 | 0.60 |

BPT-1000在AUC-IoU上较AA-1000提升0.0435，较LIME-1000提升0.0670，较GradCAM提升0.0698。在SwinViT实验（E3）中，BPT生成的显著性图比所有其他方法更聚焦于分类物体，背景噪声显著减少。消融实验显示，BPT在相同预算下比AA需要更少的Owen公式递归应用，收敛速度更快。

评估边界方面，论文未报告置信区间，数值比较需谨慎。基线选择为均匀灰色，未探讨基线敏感性。代码已开源，但BPT构建依赖颜色/形状先验，在纹理复杂或抽象图像上的泛化能力未充分验证。

## 关联研究分析

从问题动机看，ShapBPT与SHAP Partition Explainer同属Shapley类方法，但后者使用AA网格，前者使用BPT。差异根源在于：AA网格是几何划分，无法适应图像形态学结构，导致收敛慢；BPT是数据感知划分，对齐图像内在结构，从而提升效率。这一差异并非任务特性决定，而是论文对“层级结构应如何构建”这一关键设计选择的探索。

从方法设计看，ShapBPT与LIME均利用图像分割，但LIME分割固定且不可细化，BPT分割自适应且可递归细化。差异根源在于：LIME缺乏反馈机制，分割错误无法纠正；BPT通过Shapley值分布指导分割，实现自适应细化。这一差异揭示了“固定分割”与“自适应分割”在解释质量上的本质区别，但BPT对颜色/形状先验的依赖是否限制其在抽象图像上的泛化，论文未给出回答。

## 总结

ShapBPT要解决的核心矛盾是Shapley值计算在图像数据上的收敛效率与解释精度之间的权衡。现有方法如SHAP-AA因使用数据无关的AA网格，无法适应图像形态学结构，导致收敛慢且定位模糊；ShapBPT通过引入数据感知的BPT层级，使分割边界对齐图像内在结构，从而在相同评估预算下获得更清晰的显著性图。该方法在ImageNet-S50上AUC-IoU达0.1844，较AA-1000提升0.0435，并在20名受试者偏好研究中获认可。其边界在于：BPT构建依赖颜色/形状先验，在纹理复杂或抽象图像上的泛化能力未充分验证；未对比最新ViT专用归因方法，无法证明其在Transformer架构下的绝对优势。当图像缺乏明显颜色/形状结构时，BPT层级的数据感知特性是否仍能保持解释质量，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.07047)