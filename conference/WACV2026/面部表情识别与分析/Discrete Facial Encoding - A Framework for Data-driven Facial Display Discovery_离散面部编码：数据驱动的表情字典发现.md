# WACV2026最新论文 ｜Discrete Facial Encoding: A Framework for Data-driven Facial Display Discovery ｜离散面部编码：数据驱动的表情字典发现

研究机构：美国南加州大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_WACV_2026_12969482)

> 面部表情分析长期依赖面部动作编码系统（FACS），但其手动标注成本高且覆盖有限，难以应对野外复杂场景。现有自动检测系统精度受限且缺乏对细微肌肉运动的完整捕捉，而传统数据驱动方法又难以解耦身份与姿态干扰。本文提出离散面部编码（Discrete Facial Encoding, DFE），利用残差向量量化变分自编码器（RVQ-VAE）在三维可变形模型（3DMM）特征上学习可解释的离散表情Token。该方法在压力、人格和抑郁预测任务上优于FACS及自监督模型，但其对连续表情强度的离散化损失及跨域泛化能力仍存疑。

## 研究背景

当研究者试图量化面部表情时，面部动作编码系统（FACS）将面部行为分解为动作单元（AUs），每个AU对应特定肌肉群的激活。然而，FACS依赖专家手动标注，成本高昂且覆盖范围有限，导致自动化检测系统在野外条件下F1分数通常仅约70%。为突破这一瓶颈，研究者转向数据驱动方法，如Facial Basis，它通过Gabor相位或3DMM特征学习线性基函数组合。但Facial Basis在2D像素空间难以解耦身份、姿态和光照等混淆因素，且其连续基系数缺乏离散化带来的直观可解释性。

面部表情编码的核心矛盾在于：如何在消除身份混淆的前提下，建立从底层肌肉运动到高层心理状态的映射。主流路线包括基于监督的AU分类和基于线性代数的基学习，前者受限于标注成本和泛化能力，后者受限于非线性表达和可解释性。本文的切入点在于，利用深度生成模型在3DMM表情参数上进行无监督离散量化，构建一个无需专家标注、具备空间局部性且可视觉化的面部表情字典，从而在心理任务预测中提供比FACS更精细、比自监督模型更可解释的特征表示。

## 核心方法

### 方法参照系

本文问题属于面部动作单元编码路线，但关键差异在于：标准流程多为监督式AU分类或线性基学习，而本文采用无监督RVQ-VAE在3DMM特征上进行离散量化，旨在发现超越预定义AU组合的完整表情模板。

### 3DMM特征提取与解耦

设计动机在于解决2D像素空间方法无法有效分离表情与身份、姿态混淆因素的问题。本文使用EMOCA模型提取3DMM表情参数 $\psi$，其公式为 $\mathbf{M} = W(\mathbf{T} + B_s(\boldsymbol{\beta}) + B_e(\boldsymbol{\psi}), J(\boldsymbol{\beta}), \boldsymbol{\theta})$，其中 $\boldsymbol{\beta}$ 为形状，$\boldsymbol{\psi}$ 为表情，$\boldsymbol{\theta}$ 为姿态。该公式通过线性混合蒙皮将表情变形独立于身份和姿态，确保后续编码仅关注表情相关的几何变化，为离散Token的纯净性奠定基础。

### RVQ-VAE离散量化与正则化

设计动机在于克服线性基组合难以捕捉非线性复杂表情且缺乏离散可解释性的局限。本文将 $\psi$ 重塑为序列，经Transformer编码器映射至潜空间 $\mathbf{z}_0$，再通过 $L$ 阶段残差量化生成离散Token序列。总损失函数为 $\mathcal{L} = \|\psi - \hat{\psi}\|_2^2 + \beta \|\text{sg}[\mathbf{z}_0] - \mathbf{e}_{k_1}\|_2^2 + \lambda_{orth} \|\mathbf{E}^T\mathbf{E} - I\|_F^2 + \lambda_{sparse} \|\mathbf{E}\|_1$，其中正交损失 $\lambda_{orth}$ 确保码本嵌入多样性，L1稀疏损失 $\lambda_{sparse}$ 促进Token的空间局部性。该设计使每个Token对应特定的面部区域变形，通过变形热图可视化，实现了从黑盒向量到空间可解释组件的转化。

## 实验评估

实验在AffectNet上预训练，评估涵盖Aff-Wild2、SmileStimuli、StressID、AVEC 2019和ChaLearn数据集。基线包括AU (LibreFace)、Facial Basis、MAE-Face、VideoMAE和MARLIN，覆盖了监督AU、线性基和自监督表示学习路线，但缺失最新MLLM或因果发现方法对比。

| 任务 | 指标 | AU (LibreFace) | Facial Basis | Ours (VQ-VAE) |
| :--- | :--- | :--- | :--- | :--- |
| StressID (Binary) | F1 | 70.0 | 72.2 | **73.3** |
| StressID (Multiclass) | F1 | 55.0 | 58.5 | **61.1** |
| AVEC 2019 (Regression) | RMSE | 8.3 | 7.5 | **7.2** |
| AVEC 2019 (Classification) | AUC | 62.4 | 60.0 | **63.3** |
| ChaLearn (Extraversion) | CCC | 45.7 | 46.7 | **53.8** |

在StressID二分类上，本文F1 73.3%较AU提升3.3个百分点；在ChaLearn外向性预测上，CCC 53.8%较Facial Basis提升7.1个百分点，表明离散Token在捕捉细微心理线索上具有优势。

消融实验未在正文详细展开，但超参数设置（$\lambda_{orth}=1.0, \lambda_{sparse}=0.1$）暗示正交性与稀疏性对Token局部性至关重要。若移除正交损失，码本可能坍缩，导致Token冗余；若L1惩罚过强，可能丢失细微表情信息。

评估边界方面，本文未报告FER分类准确率，仅关注心理任务预测；评估协议依赖3DMM重建质量，若EMOCA提取误差大，将直接影响Token质量；代码已开源，但预训练数据AffectNet存在标签噪声，可能影响泛化性。

## 关联研究分析

从问题动机看，本文与Facial Basis [36] 均旨在数据驱动发现面部模板，但Facial Basis使用线性基组合，受限于非线性表达和2D混淆因素；本文通过3DMM解耦和RVQ-VAE离散化，解决了身份混淆和可解释性问题。差异根源在于任务特性：Facial Basis侧重连续强度建模，适合渐进表情分析；本文侧重离散模板发现，适合复杂混合表情。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

从方法设计看，本文与MAE-Face [22] 均利用自监督学习，但MAE-Face关注通用图像表示，缺乏空间可解释性；本文通过3DMM约束和离散量化，实现了表情特定的可解释编码。差异根源在于目标函数：MAE-Face优化像素重建，本文优化表情参数重建并加入正交稀疏正则。若采用MAE-Face骨干，是否能在保持可解释性的同时提升泛化能力，论文未探索。

## 总结

本文要解决的核心矛盾是FACS标注成本高与野外表情复杂性之间的冲突。本文抓住的切入点是利用3DMM解耦身份姿态，并通过RVQ-VAE在表情参数上学习离散Token，从而构建无需专家标注且空间可解释的面部字典。本文证明了在StressID上F1 73.3%和ChaLearn外向性CCC 53.8%优于基线。本文的边界在于，离散量化可能丢失连续表情强度信息，且预训练数据AffectNet的标签噪声可能影响Token的纯净性。当支持集增大或表情强度连续变化时，离散Token的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_WACV_2026_12969482)