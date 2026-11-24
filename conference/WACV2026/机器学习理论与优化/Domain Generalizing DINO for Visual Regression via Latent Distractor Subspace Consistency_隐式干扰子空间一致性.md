# WACV2026最新论文 ｜Domain Generalizing DINO for Visual Regression via Latent Distractor Subspace Consistency ｜隐式干扰子空间一致性

研究机构：印度理工学院德里分校

作者：Nikhil Reddy、Chetan Arora、Mahsa Baktashmotlagh

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_be78663f76d5)

> 域泛化回归任务面临连续标签空间对高方差风格因子（如光照、模糊）的极端敏感性，导致模型在未见域上产生虚假相关。现有方法依赖预定义干扰项或CNN架构，无法适配视觉基础模型（VFM）且难以捕捉训练中涌现的隐式干扰。本文提出LDSC框架，通过正交子空间解耦与光度扰动下的协方差一致性正则化，在DINO骨干上实现回归域泛化。该方法在七个基准上取得SOTA，但仅依赖光度扰动，对复杂语义偏移的鲁棒性存疑。

## 研究背景

当模型从源域迁移至未见目标域时，输入分布的偏移会导致性能衰退，这一现象称为域偏移。在分类任务中，域偏移常表现为风格变化，可通过特征对齐缓解；但在回归任务中，连续标签空间对高方差、与标签无关的风格因子（如光照、背景纹理）更为敏感，这些因子易与任务相关特征纠缠，形成虚假相关，导致预测偏差。为抑制虚假相关，需识别并解耦干扰因子，但实际场景中干扰项往往隐式存在，难以通过领域知识显式定义。

域泛化（Domain Generalization, DG）旨在无目标域数据条件下实现跨域泛化。主流DG方法聚焦分类任务，采用统计对齐或因果不变性学习，但直接迁移至回归任务时面临标签空间连续性与干扰因子隐式性的双重挑战。现有回归DG方法如C-Mixup依赖标签距离混合增强，但未解耦特征空间中的干扰成分；条件独立性方法如CIRCE需预定义干扰项，无法应对训练中涌现的隐式干扰。本文切入点在于：利用视觉基础模型（Vision Foundation Model, VFM）的强语义先验，通过隐式特征-标签解耦与干扰子空间一致性正则化，在无需预定义干扰项的前提下抑制虚假相关。

## 核心方法

### 方法参照系

本文问题属于表征解耦路线在回归任务中的具体化。标准解耦流程通过正交投影分离任务相关与干扰特征，但分类任务中干扰因子常显式（如风格），而回归任务中干扰因子隐式且高方差，需额外机制识别并抑制其风格敏感性。

### 隐式特征-标签解耦

解耦环节通常依赖显式干扰项定义，本文改为通过HSIC（Hilbert-Schmidt Independence Criterion）自动识别隐式干扰。任务相关子空间$Z_{\text{task}}$最大化与标签$Y$的依赖性，干扰子空间$Z_{\text{latent}}$最大化方差同时最小化与$Y$的依赖性：

$$
U_2 = \arg\max_{\substack{U^\top U = I \\ U^\top U_1 = 0}} \operatorname{tr}\left(U^\top \Phi^\top \Phi U\right) - \mu \operatorname{tr}\left(U^\top \Phi^\top H K_Y H \Phi U\right)
$$

该公式通过HSIC项惩罚干扰子空间与标签的统计依赖，确保$Z_{\text{latent}}$捕获高方差但标签无关的方向，解决了预定义干扰项缺失导致的虚假相关抑制失效。

### 干扰子空间一致性正则化

解耦后，干扰子空间仍可能包含风格敏感成分。本文引入LDSC损失，对光度扰动（如颜色抖动）下的干扰子空间协方差进行掩码惩罚：

$$
\mathcal{L}_{\text{LDSC}} = \frac{1}{2}\left\|\Sigma^{\text{s}}_Z(x) \odot \widetilde{M}^Z\right\|_1 + \frac{1}{2}\left\|\Sigma^{\text{s}}_Z(\tau(x)) \odot \widetilde{M}^Z\right\|_1
$$

其中$\widetilde{M}^Z$为风格敏感协方差掩码。该损失仅惩罚随风格变化的协方差分量，迫使$Z_{\text{latent}}$在扰动下保持稳定，从而抑制风格依赖的虚假相关，提升跨域鲁棒性。

## 实验评估

实验在七个数据集（BIWI、RHD、dSprites、RCF-MNIST、PovertyMap、MPI3D、FisV）上进行，基线覆盖ERM、IRM、C-Mixup、RankSim等，但缺失主流分类DG方法（如BOA、DCCL）的回归适配版，限制了跨任务对比。

| 数据集 | 方法 | Avg RMSE | Worst RMSE |
| :--- | :--- | :--- | :--- |
| RCF-MNIST | C-Mixup | 0.133 | 0.146 |
| RCF-MNIST | LDSC | 0.122 | 0.134 |
| PovertyMap | C-Mixup | 0.995 | 1.113 |
| PovertyMap | LDSC | 0.774 | 0.789 |

LDSC在RCF-MNIST和PovertyMap上分别较C-Mixup提升8.27%和22.21%，验证了解耦与一致性正则化的有效性。

| 数据集 | 方法 | Avg RMSE | Worst RMSE |
| :--- | :--- | :--- | :--- |
| PovertyMap | LDSC | 0.774 | 0.789 |
| PovertyMap | w/o HSIC | 0.889 | 0.997 |
| PovertyMap | w/o LDSC | 0.991 | 1.004 |

消融显示，移除HSIC解耦或LDSC损失均导致性能显著下降，其中移除LDSC损失后Avg RMSE回升至0.991，接近C-Mixup水平，表明一致性正则化对抑制风格敏感干扰至关重要。

评估指标涵盖RMSE、MAE及公平性指标$\hat{r}_{\text{sep}}$，但缺乏计算效率维度。实验在NVIDIA H100 GPU上进行，训练时间约4.2-5.8小时/数据集，代码开源。光度扰动仅覆盖颜色抖动，未测试复杂语义偏移（如背景变化），可能限制鲁棒性评估的全面性。

## 关联研究分析

从问题动机看，本文与C-Mixup同属回归DG，但C-Mixup依赖标签距离混合增强数据多样性，未解耦特征空间中的干扰成分；本文通过隐式解耦直接抑制虚假相关，解决了C-Mixup在隐式干扰场景下的失效。差异根源在于任务特性：回归标签的连续性使干扰因子更易与任务特征纠缠，需显式解耦而非仅数据增强。

从方法设计看，本文与CIRCE同用条件独立性，但CIRCE需预定义干扰项（如保护属性），本文通过HSIC自动识别隐式干扰，消除了领域知识依赖。然而，本文仅用光度扰动验证一致性，未测试复杂语义偏移，而CIRCE在预定义干扰项下可能更稳定。光度扰动是否足以覆盖真实域偏移，论文未给出回答。

## 总结

本文核心矛盾是回归任务中隐式干扰因子导致的虚假相关抑制。现有方法依赖预定义干扰项或CNN架构，无法适配VFM且难以捕捉隐式干扰；本文利用VFM语义先验，通过HSIC解耦与光度扰动一致性正则化，在无需预定义干扰项的前提下抑制虚假相关。LDSC在PovertyMap上Avg RMSE达0.774，较C-Mixup提升22.21%。边界在于仅用光度扰动验证，未测试复杂语义偏移；DINOv3表现不如DINOv2，原因未明。当干扰因子涉及语义变化（如背景纹理）时，光度扰动一致性是否仍有效，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_be78663f76d5)