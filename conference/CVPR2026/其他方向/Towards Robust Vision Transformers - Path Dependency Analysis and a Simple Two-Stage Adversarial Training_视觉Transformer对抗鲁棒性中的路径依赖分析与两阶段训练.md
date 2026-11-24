# CVPR2026最新论文 ｜Towards Robust Vision Transformers: Path Dependency Analysis and a Simple Two-Stage Adversarial Training ｜视觉Transformer对抗鲁棒性中的路径依赖分析与两阶段训练

作者：Seongmin Kim、Byung Cheol Song

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1eb13b877dc8)

> 视觉Transformer（ViT）在对抗训练（Adversarial Training, AT）中常出现性能退化或收敛不稳定，根源在于其内部信息流结构与卷积神经网络（CNN）存在本质差异。现有方法多直接移植CNN的鲁棒蒸馏策略，忽视了ViT中残差连接对攻击梯度的特殊贡献。本文通过梯度路径掩码（Gradient Path Masking, GPM）定位脆弱路径，并提出基于类注意力图（Class Attention Map, CAM）蒸馏的两阶段AT框架。该方法在CIFAR-10上将ViT-S的AutoAttack（AA）鲁棒性从46.37%提升至47.41%，但缺乏大规模数据集验证，其通用性存疑。

## 研究背景

对抗训练通过min-max优化提升模型对恶意扰动的稳定性，但在ViT中效果常不及CNN。这一现象源于ViT注意力模块将信息流显式解耦为查询-键（Query-Key, QK）、值（Value, V）及残差三条路径，而CNN的特征图融合是隐式的。当攻击者利用梯度信息生成对抗样本时，不同路径对决策边界的贡献度不均，导致标准AT在ViT上可能优化到次优解。

主流鲁棒性研究长期聚焦CNN，RobustBench统计显示仅13%的鲁棒性研究针对ViT。早期工作如ARD（Mo et al.）尝试随机丢弃注意力梯度，但未揭示路径间的结构性差异；其他方法如RSLAD和AdaAD依赖教师模型生成强对抗样本，但在ViT上因梯度方向失配而失效。本文切入点在于：ViT的残差路径是攻击者获取梯度信息的主要通道，而QK路径蕴含鲁棒性相关特征，这一不对称性未被现有AT框架利用。

## 核心方法

### 方法参照系

标准AT框架将对抗训练视为min-max优化：内层最大化生成对抗样本，外层最小化损失更新参数。本文问题与该通用流程的关键差异在于，ViT的梯度传播路径具有可分解性，允许在反向传播中屏蔽特定路径的梯度，从而分析各路径对攻击有效性的贡献。

### 梯度路径掩码分析

GPM在反向传播中将特定路径的梯度置零，以评估攻击者对该路径信息的依赖程度。设计动机是解决ARD随机丢弃梯度无法区分路径贡献的问题。ViT第$l$层的梯度分解为：

$$
\frac{\partial \mathcal{L}}{\partial X_{l-1}} = \frac{\partial \mathcal{L}}{\partial X_l} \frac{\partial f^{(l)}}{\partial X'_l} \left( \underbrace{1}_{\text{Residual}} + \underbrace{S_l\frac{\partial V_l}{\partial X_{l-1}}}_{\text{V}} + \underbrace{V_l\frac{\partial S_l}{\partial X_{l-1}}}_{\text{QK}} \right)
$$

其中$S_l = \text{softmax}(Q_l K_l^\top / \sqrt{d})$。GPM通过设置$\delta_R, \delta_{QK}, \delta_V \in \{0,1\}$屏蔽对应路径，实验发现屏蔽残差路径后攻击成功率从48.14%降至21.83%，而屏蔽QK路径仅降至44.59%，证实残差路径是鲁棒性瓶颈。

### 两阶段CAM蒸馏与残差门控

第一阶段训练教师模型$f_{\theta_T}$，提取其CAM作为语义先验；第二阶段通过CAM蒸馏损失引导学生模型$f_{\theta_S}$，并引入残差门控参数$r_l$抑制残差路径依赖。设计动机是解决教师梯度方向无法有效引导ViT跨越决策边界的问题。CAM蒸馏损失定义为：

$$
\mathcal{L}_{\text{distill}} = \frac{1}{HL} \sum_{l=1}^{L} \sum_{h=1}^{H} \left\| \mathcal{A}_{\text{cls}}^{(l,h)}(\theta_T, x) - \mathcal{A}_{\text{cls}}^{(l,h)}(\theta_S, x') \right\|_2
$$

其中$\mathcal{A}_{\text{cls}}^{(l,h)} = Q_{\text{cls},\theta}^{(l,h)}(x) K_{\theta}^{(l,h)}(x)^\top / \sqrt{d_h}$为softmax前的类注意力特征。残差门控修改为$X'_l = S_l V_l + r_l X_{l-1}$，总损失为$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{AT}} + \lambda \mathcal{L}_{\text{distill}}$。该设计使混合架构（如ConViT）在AA鲁棒性上平均提升2.44%，非混合架构提升1.06%。

## 实验评估

实验在CIFAR-10和ImageNette上进行，对比PGD-AT、TRADES、MART及ARD、RSLAD、AdaAD等基线。基线覆盖标准AT与鲁棒蒸馏路线，但缺失ReMoE、CAAT等2026年架构级防御方法。主结果显示，本文方法在CIFAR-10上将ViT-S的AA鲁棒性从PGD-AT的46.37%提升至47.41%，清洁精度从79.59%提升至82.01%。

| 方法 | Clean (%) | CW-20 (%) | PGD-20 (%) | AA (%) |
|---|---|---|---|---|
| PGD-AT | 79.59 | 48.22 | 50.86 | 46.37 |
| + Ldistill | 81.39 | 48.99 | 51.39 | 47.01 |
| + Residual gating | 82.01 | 49.34 | 51.59 | 47.41 |

消融实验表明，CAM蒸馏贡献了+1.8%清洁精度和+0.7% AA鲁棒性，残差门控额外贡献+0.6%清洁精度和+0.4% AA鲁棒性。混合架构（ConViT, CeiT, CvT）从该方法中获益更大，平均AA鲁棒性提升2.44%，而非混合架构仅提升1.06%，证实了AT与CNN局部偏置架构的兼容性冲突。

评估边界方面，实验仅在CIFAR-10和ImageNette上进行，缺乏ImageNet-1k大规模验证；未报告FLOPs与推理时间，无法评估计算开销；代码未公开，超参数细节（如$\lambda=1$）仅在正文提及，可复现性受限。

## 关联研究分析

从问题动机看，本文与CFT（Elisha et al., 2026）均关注语义区域对齐，但CFT通过概念引导微调对齐内部相关性，本文通过CAM蒸馏在AT过程中实现语义先验注入。差异根源在于任务阶段：CFT侧重微调阶段，本文侧重AT训练阶段，后者更直接解决AT与ViT架构的兼容性问题。

从方法设计看，本文与ReMoE（P45）均针对ViT局部敏感性，但ReMoE通过区域混合专家约束局部损坏传播，本文通过残差门控控制信息流。ReMoE是架构级修改，本文是训练策略级修改，后者更轻量但可能无法解决深层结构问题。GPM分析工具与ARD（Mo et al.）的区别在于，ARD随机丢弃梯度，GPM结构化分解路径，前者无法定位具体瓶颈，后者提供了机制解释。

## 总结

本文要解决的核心矛盾是AT在ViT中因路径依赖不对称导致的性能退化。切入点在于识别残差路径为攻击梯度主要通道，QK路径蕴含鲁棒性特征，这一发现使两阶段CAM蒸馏+残差门控成为可能。方法通过教师CAM蒸馏提供语义先验，残差门控抑制脆弱路径，在CIFAR-10上将ViT-S的AA鲁棒性提升至47.41%，清洁精度提升至82.01%。边界在于实验仅限小数据集，混合架构收益大于非混合架构暗示方法对架构类型敏感。当支持集增大到ImageNet-1k规模时，CAM蒸馏的语义先验是否仍能有效引导ViT跨越决策边界，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_1eb13b877dc8)