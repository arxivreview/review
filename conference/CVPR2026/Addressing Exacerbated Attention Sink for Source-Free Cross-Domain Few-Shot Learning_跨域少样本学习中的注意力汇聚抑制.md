# CVPR2026最新论文 ｜Addressing Exacerbated Attention Sink for Source-Free Cross-Domain Few-Shot Learning ｜跨域少样本学习中的注意力汇聚抑制

研究机构：华中科技大学

作者：Shuai Yi、Yixiong Zou、Yuhua Li 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.25799)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.25799)

> 跨域少样本学习（CDFSL）旨在将预训练视觉-语言模型（VLM）适配至仅有极少标注样本的目标域，核心矛盾在于源域与目标域的巨大分布差异导致模型难以复用预训练特征。现有方法多聚焦于特征对齐或提示优化，却忽视了微调过程本身会加剧视觉注意力汇聚（Attention Sink），使模型依赖非判别性背景特征。本文发现少样本微调会放大这一现象，并提出Token Importance Recalibration（TIR）模块，通过动态重加权抑制简单token、增强判别token。该方法在四个基准上取得SOTA，但其对零样本能力的影响及深层网络依赖尚存疑。

## 研究背景

当CLIP模型从ImageNet迁移至医疗或遥感领域时，源域与目标域的分布差异导致预训练特征失效。这种分布偏移使得模型在目标域微调时，视觉注意力往往集中在非判别性区域，即注意力汇聚现象。注意力汇聚虽有助于信息聚合，但在少样本场景下会加剧虚假相关，导致模型依赖背景而非语义内容。

CDFSL的主流路线包括风格解耦（如SHED）和尾部对齐打破（如Breaking Tail Alignment），前者通过移除域质心消除风格信息，后者通过排斥低相似度token改善对齐。然而，这些方法均假设注意力汇聚是静态的，未考虑微调过程对注意力分布的动态影响。本文切入点在于揭示少样本微调本身会加剧注意力汇聚，并解释其背后的“域适应捷径”机制：模型优先学习易对齐的简单token以快速适应域偏移，牺牲了判别性token的学习。

## 核心方法

### 方法参照系

本文基于CLIP-LoRA-Vision基线，属于参数高效微调（PEFT）范畴。标准流程冻结CLIP主干，仅更新LoRA参数以最小化交叉熵损失。本文的关键差异在于，在视觉编码器深层（第8、10层后）插入TIR模块，直接干预视觉token的权重分布，而非仅调整提示或适配器参数。

### 注意力汇聚加剧机制

微调过程加剧注意力汇聚的根源在于域适应捷径。模型在目标域微调时，倾向于学习那些初始与所有目标域类别相似度较高的简单token（Sum=5），因为这些token更易对齐，从而吸收过多域信息。这种捷径学习牺牲了判别性token（Sum=1）的学习，导致注意力汇聚加剧。TIR模块通过计算视觉token与文本嵌入的余弦相似度，识别并抑制这些简单token。

$$
\text{Sum}_{b,i} = \sum_{k=1}^{K} \mathbb{I}(\text{sim}(\mathbf{v}_{b,i}, \mathbf{t}_k) \in \text{Top-}k)
$$

该公式计算每个视觉token在所有类别中的激活次数，Sum=5表示token被所有类别激活，即注意力汇聚token。

### Token Importance Recalibration

TIR模块通过线性重加权方案抑制简单token、增强判别token。对于Sum=5的token，权重设为0；对于Sum=1的token，权重设为2；其他token权重线性插值。这一设计直接解决了微调过程中模型依赖非判别性特征的问题，使模型聚焦于语义判别性模式。

$$
w_{b,i} = \begin{cases}
0 & \text{if } \text{Sum}_{b,i} = K \\
2 & \text{if } \text{Sum}_{b,i} = 1 \\
\alpha - \beta \cdot \text{Sum}_{b,i} & \text{otherwise}
\end{cases}
$$

其中$\alpha=3$，$\beta=0.5$。该公式通过条件线性重加权，平滑地分配权重，抑制注意力汇聚token并增强判别token。

## 实验评估

实验在CropDiseases、EuroSAT、ISIC2018、ChestX四个基准上进行，采用5-way 1-shot和5-shot设定。基线包括CLIP-LoRA-Vision、StepSTP等PEFT方法，但缺失SHED、DiCoOP等强域泛化方法。

| 方法 | 骨干 | Shot | ISIC | EuroSAT | CropDiseases | ChestX | Ave. |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| CLIP-LoRA-Vision | ViT/CLIP | 1 | 35.23 | 81.41 | 85.32 | 21.73 | 55.92 |
| **CLIP-LoRA-Vision + TIR** | ViT/CLIP | 1 | **39.38** | **82.53** | **86.91** | 23.98 | **58.20** |
| CLIP-LoRA-Vision | ViT/CLIP | 5 | 51.10 | 92.52 | 96.21 | 24.13 | 65.99 |
| **CLIP-LoRA-Vision + TIR** | ViT/CLIP | 5 | **56.73** | **93.49** | **97.42** | 26.12 | **68.44** |

TIR模块在1-shot和5-shot设定下均显著提升性能，尤其在ISIC和ChestX等医疗领域表现突出。

| 消融 | Inhibit | Enhance | CropDisease | EuroSAT | ISIC2018 | ChestX | Ave. |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 基线 | - | - | 96.21 | 92.52 | 51.10 | 24.13 | 65.99 |
| 仅抑制 | ✓ | - | 97.21 | 93.26 | 55.00 | 25.15 | 67.66 |
| 仅增强 | - | ✓ | 97.24 | 92.99 | 53.72 | 24.98 | 67.23 |
| 完整 | ✓ | ✓ | **97.42** | **93.49** | **56.73** | **26.12** | **68.44** |

消融实验表明，抑制和增强模块单独使用均有增益，联合使用效果最佳。抑制模块对CropDisease和ISIC贡献最大，增强模块对EuroSAT贡献显著。

评估边界方面，论文未报告置信区间，且基线缺失SHED等强域泛化方法。代码已开源，超参数（k=0.3, temper ratio=0.5）明确，但TIR模块的插入位置（第8、10层）是否依赖特定骨干网络结构未充分验证。

## 关联研究分析

从问题动机看，本文与Breaking Tail Alignment同属CDFSL，但后者通过排斥低相似度token改善对齐，而本文通过token重加权抑制注意力汇聚。差异根源在于，Breaking Tail Alignment假设对齐问题源于尾部token的干扰，而本文揭示微调过程本身会加剧注意力汇聚，需直接干预token权重分布。

从方法设计看，本文与SHED同属域泛化路线，但SHED通过风格解耦消除域信息，本文通过token重加权增强判别性。差异在于，SHED假设域信息主要存在于风格特征中，而本文发现域信息被简单token吸收，需通过抑制这些token来恢复判别性。SHED未考虑微调过程对注意力分布的动态影响，这是其未探索的盲区。

## 总结

本文核心矛盾在于少样本微调加剧注意力汇聚，导致模型依赖非判别性特征。切入点在于揭示域适应捷径机制，即模型优先学习易对齐的简单token。TIR模块通过动态重加权抑制简单token、增强判别token，在四个基准上取得SOTA，如CropDiseases 5-shot达97.42%。边界在于，TIR模块的深层网络依赖未充分验证，且对零样本能力的影响未评估。当支持集增大到5-shot时，TIR模块的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.25799)