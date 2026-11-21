# CVPR2026最新论文 ｜MoECLIP: Patch-Specialized Experts for Zero-shot Anomaly Detection ｜混合专家机制下的补丁级零样本异常检测

研究机构：韩国延世大学

作者：Jun Yeong Park、JunYoung Seo、Minji Kang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.03101)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.03101)

> 零样本异常检测（Zero-Shot Anomaly Detection, ZSAD）旨在利用视觉-语言模型（Vision-Language Model, VLM）的预训练知识，在缺乏目标类别训练数据的情况下识别工业或医疗图像中的缺陷。现有基于CLIP的ZSAD方法普遍采用“补丁无关”设计，对所有图像区域施加统一适配，忽视了不同区域（如部件与背景）在结构和语义上的异质性，导致细粒度定位能力受限。本文提出MoECLIP，通过在CLIP视觉编码器中嵌入混合专家（Mixture of Experts, MoE）模块，实现基于补丁特征的动态路由与差异化适配。该框架在14个基准数据集上取得了SOTA性能，但其专家路由机制对推理效率的影响及跨域泛化的边界条件仍存疑。

## 研究背景

工业质检与医疗诊断中，缺陷样本的极度稀缺使得无监督异常检测（Unsupervised Anomaly Detection, UAD）成为主流，但UAD仍依赖充足的目标域正常样本。当新品类频繁更替时，重新提取特征并构建记忆库的成本不可承受，这催生了ZSAD范式。ZSAD利用CLIP等VLM的全局语义对齐能力，通过计算图像补丁嵌入与文本提示的相似度来检测异常，从而摆脱对目标域数据的依赖。然而，CLIP预训练目标偏向全局语义理解，其视觉特征对局部细微缺陷（如划痕、污渍）的敏感性不足，直接应用会导致像素级分割精度低于有监督方法。

为弥补CLIP的局部感知短板，近期研究聚焦于参数高效微调（Parameter-Efficient Fine-Tuning, PEFT）策略。PromptAD和AnomalyCLIP通过修改注意力机制或引入可学习提示词来增强局部特征；AdaCLIP和AA-CLIP则引入适配器（Adapter）或提示Token，在冻结CLIP骨干的前提下提升检测性能。这些方法虽然提升了图像级分类精度，但均遵循“补丁无关”设计，即对所有补丁施加相同的线性变换或提示注入。这种统一适配忽略了图像中不同区域（如物体组件、背景、纹理）具有截然不同的结构特征，导致模型无法针对特定区域进行精细化调整，成为制约ZSAD细粒度定位精度的核心瓶颈。

## 核心方法

### 方法参照系

本文问题归属于基于CLIP的ZSAD任务，标准流程为：冻结CLIP视觉编码器提取补丁特征，通过文本编码器获取正常/异常文本嵌入，计算余弦相似度生成异常分数。与通用流程的关键差异在于，本文不采用单一适配器或提示词，而是引入MoE架构，将特征适配过程从“全局统一”转变为“补丁级动态路由”，以解决统一适配无法区分局部语义异质性的问题。

### 补丁级动态路由与低秩适配

在CLIP视觉编码器的第6、12、18、24层输出端，MoECLIP插入MoE模块。每个补丁特征 $F_i^{[l]}$ 通过线性路由器 $R$ 计算路由分数，激活Top-2个专家。专家由低秩适配（Low-Rank Adaptation, LoRA）模块实现，其权重更新 $\Delta W = BA$ 中，$A \in \mathbb{R}^{r \times d_2}$ 和 $B \in \mathbb{R}^{d_1 \times r}$ 为可训练矩阵，秩 $r \ll \min(d_1, d_2)$。MoE输出经 $\ell_2$ 归一化后，以残差形式与原特征融合：

$$ F_{i,[l]}^{\text{MoE}} = F_i^{[l]} + \lambda_{\text{MoE}} \frac{F_{i,[l]}^{\text{expert}}}{\|F_{i,[l]}^{\text{expert}}\|_2 + \epsilon} \|F_i^{[l]}\|_2 $$

该设计动机在于：单一适配器对所有补丁施加相同变换，无法区分“部件”与“背景”的特征需求；通过动态路由，不同补丁可选择最适合其语义特征的专家，从而在保持CLIP泛化能力的前提下实现细粒度适配。

### 专家功能分化机制

朴素LoRA专家易陷入功能冗余，即多个专家学习相似函数。为强制专家分化，MoECLIP引入冻结正交特征分离（Frozen Orthogonal Feature Separation, FOFS）和简单等角紧框架（Simplex Equiangular Tight Frame, ETF）损失。FOFS将输入特征空间 $d$ 维分解为 $K$ 个正交子空间，第 $n$ 个专家的LoRA矩阵 $A_n$ 仅在第 $n$ 个子空间列填充随机正交矩阵 $Q_n$，其余为零，确保 $A_n A_m^T = 0$ ($n \neq m$)。在输出端，ETF损失 $L_{\text{etf}}$ 约束专家输出向量 $\hat{e}_{i,n}$ 的Gram矩阵逼近理想等角矩阵 $G_{\text{ideal}}$：

$$ L_{\text{etf}} = \frac{1}{L} \sum_{i=1}^L \| G_i^{[l]} - G_{\text{ideal}} \|_F^2 $$

其中 $G_i^{[l]}$ 为第 $i$ 个补丁在层 $l$ 的专家输出Gram矩阵。FOFS在输入端通过正交子空间物理隔离专家关注区域，ETF在输出端通过几何约束最大化专家间角度差异，两者协同解决了功能冗余问题，使专家能够专注于不同的特征子空间。

## 实验评估

实验在14个数据集上进行，包括5个工业数据集（MVTec-AD, VisA, BTAD, RSDD, DTD-Synthetic）和9个医疗数据集（Brain MRI, Head CT, Liver CT, Retina OCT, 5个结肠息肉数据集）。基线覆盖WinCLIP、AnomalyCLIP、AdaCLIP、AA-CLIP等主流ZSAD方法，但缺失PatchCore等有监督/无监督记忆库基线，因任务设定不同（ZSAD vs. 有监督）。

| 数据集 | 方法 | 图像级 AUROC | 图像级 AP | 像素级 AUROC | 像素级 AP |
| :--- | :--- | :--- | :--- | :--- | :--- |
| MVTec-AD | WinCLIP | 91.8 | 95.1 | 85.1 | 18.0 |
| MVTec-AD | MoECLIP | **93.9** | **96.8** | **92.5** | 45.7 |
| VisA | WinCLIP | 78.1 | 77.5 | 79.6 | 5.0 |
| VisA | MoECLIP | **86.8** | **89.3** | **95.6** | 26.1 |
| Brain MRI | WinCLIP | 45.1 | 80.3 | 95.4 | 23.5 |
| Brain MRI | MoECLIP | **88.5** | **97.1** | **97.3** | **61.3** |

MoECLIP在MVTec-AD图像级AUROC达93.9%，较WinCLIP提升2.1%；在VisA像素级AUROC达95.6%，较WinCLIP提升16.0%。医疗数据集Brain MRI图像级AUROC从45.1%跃升至88.5%，表明补丁级路由在跨域泛化中显著优于统一适配。

消融实验显示，移除FOFS或ETF损失均导致性能下降，验证了两者互补性。移除PAA（补丁平均聚合）模块在医疗数据集上性能显著降低，说明多尺度上下文聚合对复杂医学影像至关重要。专家数量 $K=4$ 时性能最优，$K>4$ 时出现功能冗余，表明专家数量需平衡专业化与冗余风险。

评估协议采用AUROC和AP指标，未报告计算效率（GFLOPs、推理延迟）。代码已开源，超参数（LoRA rank $r=8$, $\lambda_{\text{MoE}}=0.1$）明确，但MoE路由的推理开销未量化，可能影响边缘部署可行性。

## 关联研究分析

从方法设计看，MoECLIP与AdaCLIP同属PEFT路线，但AdaCLIP采用统一适配器，而MoECLIP引入MoE实现补丁级路由。这一差异源于对“补丁异质性”的建模深度：AdaCLIP假设所有补丁共享相同的适配需求，而MoECLIP认为不同区域需差异化处理。根源在于任务特性：工业缺陷往往局限于特定部件，统一适配无法区分“缺陷区域”与“正常背景”，而MoE路由允许专家专注于特定子空间，从而提升定位精度。

从问题动机看，MoECLIP与AnomalyVFM（基于DINOv2的纯视觉ZSAD）形成对比。AnomalyVFM放弃文本模态，依赖视觉基础模型的内在表征；MoECLIP保留CLIP的文本-视觉对齐，通过MoE增强局部感知。两者代表不同骨干路线：AnomalyVFM证明纯视觉模型在零样本下的潜力，而MoECLIP证明在CLIP框架下，通过架构改进可缩小与有监督方法的精度差距。MoECLIP的局限在于依赖CLIP的文本提示，而AnomalyVFM无需文本，可能在无文本标注场景更具优势。

## 总结

MoECLIP旨在解决ZSAD中统一适配导致的细粒度定位不足问题，其切入点在于利用MoE架构实现补丁级动态路由，克服了现有PEFT方法“补丁无关”的设计局限。通过FOFS和ETF损失强制专家分化，MoECLIP在14个数据集上取得SOTA性能，MVTec-AD图像级AUROC达93.9%，VisA像素级AUROC达95.6%。然而，论文未量化MoE路由的推理延迟，且专家数量 $K=4$ 的最优性仅在特定数据集上验证，跨域泛化的边界条件（如极端光照变化）未充分测试。当支持集增大或分布偏移加剧时，MoE路由的稳定性是否仍能保持，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.03101)