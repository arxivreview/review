# CVPR2026最新论文 ｜RNN as Linear Transformer: A Closer Investigation into Representational Potentials of Visual Mamba Models ｜视觉Mamba的秩结构解析与表征能力量化

研究机构：美国约翰斯·霍普金斯大学

作者：Timing Yang、Guoyizhe Wei、Alan Yuille 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.18380)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.18380)

> 视觉状态空间模型（Vision State Space Models, VSSMs）旨在以线性复杂度替代视觉Transformer（ViT）的二次方自注意力，但其内部表征机制长期缺乏理论解释。现有研究多聚焦于扫描路径优化或架构效率改进，却未回答“Mamba为何有效”这一根本问题，导致其全局感知能力仅依赖经验性消融验证。本文切入点在于将Mamba统一为矩阵变换形式，通过秩分析揭示其作为Softmax Attention低秩近似的本质，并引入Binary-AUC指标量化特征图判别力。该工作为VSSM提供了理论参照系，但其结论局限于DINO自监督预训练范式，且未对比主流视觉Mamba变体，理论普适性存疑。

## 研究背景

当高分辨率图像输入视觉Transformer时，自注意力机制的二次方计算复杂度成为扩展瓶颈，状态空间模型（State Space Models, SSMs）凭借线性复杂度提供了替代方案。然而，SSM本质是1D序列模型，将2D图像序列化为1D序列会破坏空间邻接性，导致固定扫描顺序在几何变换下性能退化。这一困境催生了选择性扫描机制，它允许模型根据输入内容动态调整状态更新，但选择性扫描是否真正赋予Mamba全局感知能力，还是仅源于深度与归一化效应，长期缺乏理论界定。

主流视觉Mamba研究沿两条路线演进：扫描策略优化（如VMamba的四向遍历、PRISMamba的部分环扫描）试图解决空间邻接断裂，架构效率改进（如HAMSA的频域SSM）试图消除串行递归瓶颈。这两条路线均假设选择性扫描是Mamba优于线性注意力的关键，但MambaOut等工作的出现揭示了选择性扫描在分类任务中的冗余性，引发对SSM视觉适用性的理论反思。本文切入点在于跳出架构改进范式，从矩阵秩角度统一Softmax Attention、Linear Attention与Mamba的数学形式，通过秩界推导建立表征能力的理论层级，并引入定量指标验证该理论预测。

## 核心方法

### 统一矩阵变换框架

本文解决的问题是Mamba表征能力的理论定义缺失，该问题与通用注意力机制分析的关键差异在于：Mamba的状态转移矩阵是数据依赖且可学习的，而非固定核函数。本文参照线性注意力的核分解范式，将三种机制统一为 $Y = MX$ 形式，其中 $M$ 为下三角矩阵，其块结构由对角块（块内计算）与非对角块（跨时间依赖）组成。

### 秩界推导与层级建立

设计动机在于突破线性注意力受限于头维度的秩瓶颈，揭示Mamba通过状态维度扩展实现更高秩的机制。本文对非对角块进行秩分析，利用Hadamard积秩界引理，推导出三种机制的非对角块秩上界：

$$
\text{rank}(M_{\text{off}}^{\text{Softmax}}) \le C, \quad \text{rank}(M_{\text{off}}^{\text{Mamba}}) \le N, \quad \text{rank}(M_{\text{off}}^{\text{Linear}}) \le D_{QK}
$$

其中 $C$ 为块大小，$N$ 为状态维度，$D_{QK}$ 为头维度。该公式的物理含义是：Softmax Attention因非线性激活保持满秩，Mamba的秩受状态维度约束，线性注意力的秩受头维度约束。在典型配置（$C=256, N=D_{QK}=64$）下，由于Mamba的 $O(LNJ)$ 复杂度允许 $N$ 高效扩展，而线性注意力的 $O(LD_{QK}^2)$ 成本限制 $D_{QK}$ 增长，实际部署中 $\text{rank}(M_{\text{off}}^{\text{Mamba}}) > D_{QK}$ 成立，确立了Softmax Attention > Mamba > Linear Attention的表征层级。

### Binary-AUC特征图量化

设计动机在于将秩分析的理论预测转化为可测量的特征图判别力指标，替代主观视觉检查。本文定义Binary-AUC指标，计算特征图激活与真实分割掩码间的ROC曲线下面积：

$$
\text{AUC} = \int_0^1 \text{TPR}(t) \, d\text{FPR}(t)
$$

其中 $\text{TPR}(t)$ 与 $\text{FPR}(t)$ 分别为阈值 $t$ 下的真正率与假正率。该公式的算法含义是：AUC=1表示特征图完美对齐前景/背景，AUC=0.5表示随机猜测。通过合并多标签为二值掩码，该指标将高维特征图质量压缩为单一标量，使Mamba的长程依赖建模能力可被客观比较。

## 实验评估

实验在ImageNet-1K、ADE20K与COCO 2017上进行，采用DINO自监督预训练范式，基线覆盖ViT-B与LinearViT-B，但遗漏VMamba、Vim等主流视觉Mamba变体，导致无法区分SSM动力学与扫描策略对表征质量的贡献。

| 任务 | 指标 | ViT-B | DinoVim-B | LinearViT-B |
|---|---|---|---|---|
| ImageNet-1K | Top-1 Acc (%) | 77.0 | 78.2 | 74.7 |
| ADE20K | mIoU (%) | 43.2 | 38.0 | 29.2 |
| COCO 2017 | Box AP (%) | 44.8 | 42.8 | 37.1 |

核心数字对比显示：DinoVim-B在ImageNet线性探测上超越ViT-B 1.2个百分点，但在ADE20K分割上落后5.2个百分点，COCO检测上落后2.0个百分点，验证了秩分析预测的层级关系——Mamba在分类任务中接近自注意力，但在密集预测任务中因秩低于Softmax而表现较弱。

消融实验揭示模型规模对特征图质量的影响：DinoVim-T/S/B的AUC分数随维度增加而提升，但DINOv2中更大模型反而产生更多高范数异常值，导致AUC下降，这与MAE掩码补丁策略相关。Register token位置分析显示，中心位置的12个均匀分布token捕获更多信息，AUC分数与线性探测准确率呈强相关，表明特征图质量可作为模型性能的代理指标。

评估边界存在显著局限：仅使用DINO自监督预训练，未对比监督预训练或自回归预训练范式；未报告置信区间，数值比较需谨慎；代码开源但超参数细节（如温度调度、权重衰减）未完整披露，可复现性依赖GitHub仓库的完整实现。

## 关联研究分析

从问题动机看，本文与MambaOut形成理论张力：MambaOut揭示选择性扫描在视觉分类中可被门控CNN替代，暗示SSM优势可能源于深度而非扫描机制；本文则通过秩分析证明Mamba的秩高于线性注意力，在密集预测任务中优于后者。这一分歧根源在于任务依赖性：分类任务对全局依赖要求较低，而分割/检测需要精细空间上下文，Mamba的中等秩结构恰好满足后者需求，但无法完全匹配Softmax的满秩能力。

从方法设计看，本文与PRISMamba等扫描优化工作形成互补：PRISMamba通过部分环扫描提升旋转鲁棒性，但假设扫描顺序是空间感知的主要来源；本文则证明即使固定扫描，Mamba的状态维度扩展已足以建立高于线性注意力的秩结构。这一差异暗示扫描策略优化与状态维度扩展可能是正交改进方向，但本文未验证两者结合的效果，查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

本文要解决的核心矛盾是Mamba全局感知能力的理论定义缺失，现有方法仅依赖经验性消融验证，无法建立表征能力的数学层级。本文抓住的切入点是Mamba状态转移矩阵的数据依赖性，通过统一矩阵变换框架与秩界推导，首次从内在视角而非注意力框架解释Mamba的表征能力。本文做了什么：建立Softmax Attention > Mamba > Linear Attention的秩层级，并引入Binary-AUC指标量化特征图判别力。证明了什么：DinoVim-B在ImageNet线性探测达78.5%，ADE20K mIoU 38.0%，验证了理论预测的实验一致性。本文的边界在于仅使用DINO自监督预训练，未对比主流视觉Mamba变体，无法区分SSM动力学与扫描策略的贡献。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.18380)