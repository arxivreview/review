# CVPR2026最新论文 ｜Training-Only Heterogeneous Image-Patch-Text Graph Supervision for Advancing Few-Shot Learning Adapters ｜训练期异构图监督的少样本视觉-语言模型适配器

作者：Mohammed Rahman Sherif Khan Mohammad、Ardhendu Behera、Sandip Pradhan 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.18101)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.18101)

> 少样本视觉-语言模型适配面临细粒度特征捕捉与推理延迟的结构性矛盾：全局特征适配器推理快但丢失局部判别信息，Patch级适配器保留细节却引入永久推理开销。TOGA 通过引入仅在训练期运行的异构图教师，将跨模态关系知识蒸馏至轻量级缓存适配器，实现了零推理开销下的细粒度性能提升。该方法在细粒度与卫星图像基准上显著优于传统适配器，但在通用大规模分类上未超越最新提示集成方法，其知识迁移的无损性仍存疑。

## 研究背景

当视觉-语言模型（VLMs）处理细粒度视觉分类（FGVC）任务时，其依赖的空间平均化全局图像描述符会抹平区分近邻类别的局部线索（如鸟喙形状或羽毛纹理），导致模型无法区分“黄腹林莺”与“灰林莺”这类细微差异。为在少样本（K-shot）场景下适配冻结的 CLIP 主干，参数高效微调（PEFT）成为主流范式，其中 Tip-Adapter 通过构建支持集的关键-值缓存实现快速原型匹配，但其核心局限在于仅基于单一全局特征向量进行推理，无法利用 Patch 级的结构信息。

现有 PEFT 路线在性能与延迟间存在不可调和的权衡。全局特征适配器（如 CLIP-Adapter）参数量极小且推理近乎零开销，但受限于语义稀释的全局特征；Patch 级适配器（如 GraphAdapter）通过图神经网络（GNN）推理 Patch 间关系，提升了细粒度敏感度，却引入了额外的 Token 计算与 GNN 遍历，造成永久性的推理延迟。此外，多数 Patch 级方法仅执行单模态（Patch↔Patch）推理，未能充分利用文本语义进行跨模态对齐。TOGA 的切入点在于打破“训练期表达能力”与“测试期推理效率”的绑定，主张将复杂的跨模态关系推理限制在训练阶段，通过非对称蒸馏将其压缩至静态缓存中，从而在保持 Tip-Adapter 推理路径不变的前提下，弥补全局特征的细粒度缺陷。

## 核心方法

### 方法参照系

本文问题归属于参数高效适配器路线，标准流程为冻结 CLIP 编码器，仅训练轻量级模块以适配少样本数据。与 Tip-Adapter 等基线仅优化全局特征映射不同，TOGA 的关键差异在于引入一个高容量、训练期专用的异构图教师，通过监督信号重构学生适配器的缓存质量，而非在推理时执行图计算。

### 异构图教师与模态感知图变换器

针对全局特征无法捕捉局部-全局层级关系的问题，TOGA 构建了一个异构图像-Patch-文本图。教师模型首先从输入图像提取多尺度 Patch（包括全局视图、3×3、2×2 网格及垂直/水平半图），与类别文本提示共同构成图节点。模态感知图变换器（MGT）在此拓扑上执行类型特定的消息传递，区分 Patch↔Patch、Patch↔Text 等边类型，通过关系特定的投影矩阵与注意力偏置，学习视觉证据与文本语义间的细粒度相关性。

$$
\tilde{A}_{s \to t}^{[h]} = \text{softmax}\left( \frac{Q_t^{[h]} (K_s^{[h]} W_{K,r}^{[h]})^T}{\sqrt{d_k}} + b_r^{[h]} \right) \cdot \mu_r^{[h]}
$$

该公式表明，MGT 通过关系缩放系数 $\mu_r^{[h]}$ 动态调整不同模态交互（如 Patch-Text 与 Patch-Patch）的重要性，使教师能显式区分视觉内部结构与跨模态对齐的贡献。

### 判别性节点过滤与非对称蒸馏

MGT 输出的节点特征若直接全局池化，背景噪声会稀释前景判别信号。TOGA 引入判别性节点过滤，通过可学习投影向量对 Patch 节点打分，仅保留 Top-N 高分节点聚合为教师视觉特征 $f_{graph}$。随后，采用双目标协同训练策略：主损失基于零样本、缓存与图教师 logits 的混合计算，梯度同时更新学生适配器 $A$ 与教师；辅助损失对教师 logits 单独应用 Focal Loss，降权易分样本，迫使教师聚焦难例，确保其作为“专家”的监督信号质量。

$$
\mathcal{L}_{Total} = \mathcal{L}_{CE}(\mathcal{L}_{train}) + \lambda \mathcal{L}_{Focal}(\mathcal{L}_{Graph})
$$

此设计动机在于防止教师“搭便车”于强零样本分支，通过 Focal Loss 的难例聚焦机制，将细粒度关系知识有效注入学生缓存，测试时丢弃教师，推理路径与 Tip-Adapter 完全一致。

## 实验评估

实验在 11 个基准数据集上进行，涵盖 FGVC-Aircraft、EuroSAT、ImageNet 等，采用 1-16 shot 协议。基线覆盖全局适配器（Tip-Adapter-F, CLIP-Adapter）、Patch 级适配器（GraphAdapter）及提示学习方法（CoOp, MaPLe）。TOGA 在细粒度与跨域任务上表现突出，例如在 FGVC-Aircraft 16-shot 达到 48.4%，显著高于 Tip-Adapter-F 的 44.2% 和 GraphAdapter 的 41.4%；在 EuroSAT 16-shot 达到 89.4%，优于 Tip-Adapter-F 的 84.5%。然而，在 ImageNet 16-shot 上，TOGA 为 82.3%，低于知识库中提示集成方法 Cluster-Aware Prompt Ensemble Learning 的 87.2%，表明其在通用大规模分类上未超越最新 SOTA。

| 数据集 | 16-shot TOGA | 16-shot Tip-Adapter-F | 16-shot GraphAdapter |
| :--- | :--- | :--- | :--- |
| FGVC-Aircraft | 48.4 | 44.2 | 41.4 |
| EuroSAT | 89.4 | 84.5 | 85.3 |
| ImageNet | 82.3 | 75.7 | 76.2 |

消融实验揭示了关键设计决策的有效性。移除 MGT 导致 EuroSAT 1-shot 性能从 67.4% 降至 61.9%，证实跨模态图推理是主要增益来源；移除 Patch-Text 边（P）同样造成显著下降，说明单模态 Patch 交互不足。Focal Loss 在低 shot 下增益明显（EuroSAT 1-shot: 67.1%→67.4%），但在高 shot 下防止了教师过拟合易例导致的梯度冲突。Top-N 过滤中，N=50% 时性能最佳，N=25% 时因丢弃相关特征而性能下降，验证了过滤强度的权衡。

评估边界方面，论文未报告置信区间，且仅在 ViT-B/16 骨干上验证，未涵盖 ViT-L/14 等更大规模骨干。代码已开源，但超参数敏感性分析仅在补充材料中提及，主文未展示。此外，实验未包含持续学习或联邦学习场景，限制了其在动态任务流下的适用性评估。

## 关联研究分析

从问题动机看，TOGA 与 GraphAdapter 均致力于解决全局特征语义稀释问题，但 GraphAdapter 将图推理置于测试期，导致推理延迟随 Patch 数量线性增长；TOGA 则将图推理限制在训练期，通过蒸馏将关系知识压缩至静态缓存。这一差异源于对“推理效率”优先级的不同取舍：GraphAdapter 假设测试时计算资源充足，而 TOGA 针对边缘部署或实时应用场景。然而，TOGA 在 ImageNet 通用分类上落后于提示集成方法，暗示其缓存机制可能缺乏文本侧的语义重加权能力，导致在类别分布均匀的大规模任务上，细粒度优势被通用语义匹配的劣势抵消。

从方法设计看，TOGA 与 Tip-Adapter 共享缓存架构，但 Tip-Adapter 仅优化全局特征映射，而 TOGA 通过异构图教师注入 Patch-Text 关系。与 MaPLe 等提示学习方法相比，TOGA 未修改文本编码器，而是通过视觉侧的图推理间接影响跨模态对齐。这种“视觉侧增强”策略在细粒度任务上有效，但在需要精细文本语义解析的任务上可能受限。TOGA 未探索将图注意力图作为可解释性指标，以诊断模型在未见域中的注意力坍塌，这是其方法框架内未开发的潜力。

## 总结

TOGA 旨在解决少样本 VLM 适配中细粒度特征捕捉与推理延迟的矛盾，通过训练期异构图教师与非对称蒸馏，将跨模态关系知识注入 Tip-Adapter 缓存，实现了零推理开销下的性能提升。实验证明其在 FGVC-Aircraft 16-shot 达到 48.4%，EuroSAT 16-shot 达到 89.4%，显著优于传统适配器。然而，其在 ImageNet 通用分类上未超越提示集成方法，且未验证在更大规模骨干或动态任务流下的表现。当支持集规模从 1-shot 增至 16-shot 时，图教师对缓存质量的边际增益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.18101)