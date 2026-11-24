# ICLR2026最新论文 ｜CDBRIDGE: A CROSS OMICS POST TRAINING BRIDGE - STRATEGY FOR CONTEXT AWARE BIOLOGICAL MODELING ｜跨组学后训练桥接策略

研究机构：西湖大学、浙江大学

作者：Chang Yu、Siyuan Li、Zicheng Liu 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_58157616)

> 基因组DNA序列如何映射为组织特异的定量表达，是计算生物学的核心难题。现有单组学模型忽略组织上下文，而专用表达模型则受限于预裁剪片段或静态平均，无法处理全长DNA与多异构体间的复杂映射。CDBridge通过冻结预训练DNA与蛋白模型，引入剪接启发的自适应Token合并与组织条件解码器，实现了跨模态对齐与定量预测。该框架在自建GTEx-Benchmark上验证了跨组织泛化能力，但其绝对性能仍低于专用表达模型，且依赖高质量异构体注释。

## 研究背景

理解基因表达需同时捕捉序列上下文与环境上下文。序列上下文指非编码区调控剪接，使单一基因产生多异构体；环境上下文指组织类型改变表达水平。这种双重依赖性导致DNA到蛋白的映射呈现一对多特征，传统模型难以兼顾。

主流路线分为两类：单组学基础模型（如DNABERT-2、Evo2）擅长序列特征提取但缺乏组织感知；专用表达模型（如Enformer、Isoformer）能预测表达但依赖预裁剪片段或TSS对齐，无法处理全长基因组及异构体复用。多组学模型（如LucaOne）虽统一了DNA/RNA/蛋白空间，但多聚焦定性功能转移，忽视定量表达的组织特异性。CDBridge的切入点在于：不重训练骨干，而是通过后训练桥接策略，利用跨模态注意力与自适应压缩解决长度失配，同时注入组织嵌入实现条件化表达预测。

## 核心方法

### 跨组学连接器与自适应Token合并

CDBridge基于冻结的DNA编码器（如Evo）与蛋白模型，核心差异在于引入可学习的蛋白Token字典 $T_{prot} \in \mathbb{R}^{M \times d}$ 作为交叉注意力的键值对，将DNA嵌入投影至功能蛋白空间。为解决DNA序列（~$10^4$ tokens）与蛋白序列（~$10^2$ tokens）的长度失配，采用ToMe机制进行剪接启发的压缩。

$$
\tilde{\mathbf{x}}_i = \frac{\mathbf{x}_i + \mathbf{x}_{j^*(i)}}{2}, \quad \text{where } j^*(i) = \arg\max_{j \in B} \cos(\mathbf{x}_i, \mathbf{x}_j) > \tau
$$

该公式通过余弦相似度阈值 $\tau$ 动态选择合并对，保留高相似性Token并丢弃冗余信息。设计动机在于：固定分词或均匀裁剪会切断外显子功能单元，而ToMe基于内容相似度的合并能自动聚焦编码区，模拟生物剪接过程，从而在压缩长度的同时保留功能信号。

### 组织条件解码器

Stage 1输出压缩后的DNA-蛋白融合特征，Stage 2引入组织字典 $T_{Envir} \in \mathbb{R}^{C \times M \times d}$ 作为条件输入。解码器以组织向量为查询，对压缩DNA特征执行交叉注意力，输出异构体感知蛋白嵌入及定量表达标量。

$$
\mathbf{h}_{out} = \text{CrossAttn}(Q=T_{tissue}, K=V=\tilde{\mathbf{X}}_{DNA})
$$

此设计解决了专用模型无法零样本泛化至未见组织的问题。通过条件化解码，同一DNA序列在不同组织嵌入下产生差异化表达预测，实现了环境上下文的显式建模。消融实验证实，移除组织条件导致 $R^2$ 从 0.387 降至 0.020，验证了该模块对定量预测的关键作用。

## 实验评估

实验基于GTEx v8构建GTEx-Benchmark，涵盖40种人类组织，采用80/10/10基因ID划分防止泄漏。基线覆盖单组学模型（DNABERT-2, Evo2, LucaOne）与专用表达模型（Enformer, AlphaGenome, Isoformer），但缺失HyenaDNA等长序列SOTA模型。

| 模型 | Brain $R^2$ | Brain Spearman | Average $R^2$ | Average Spearman |
|---|---|---|---|---|
| DNABERT-2 | -0.004 | 0.317 | -0.004 | 0.317 |
| Enformer | 0.139 | 0.124 | 0.127 | 0.122 |
| Isoformer (w/o TSS) | -0.328 | 0.301 | -0.315 | 0.309 |
| **CDBridge** | **0.421** | **0.708** | **0.387** | **0.618** |

CDBridge在所有组织上均优于单组学基线与未对齐的Isoformer，平均 $R^2$ 达 0.387，Spearman 相关系数 0.618。消融显示，ToMe合并与可学习蛋白聚类共同提升分割AUC至 0.993，而组织条件化是表达预测性能跃升的核心驱动。

评估边界方面，GTEx-Benchmark为自建基准，缺乏与Enformer等专用模型在相同协议下的直接对比（Isoformer官方结果依赖TSS对齐，不可比）。论文未报告计算复杂度与训练资源，且仅使用人类数据，跨物种泛化能力未验证。代码未公开，超参数细节有限，可复现性存在障碍。

## 关联研究分析

从问题动机看，CDBridge与Isoformer均针对表达预测，但Isoformer依赖TSS对齐的预裁剪片段，而CDBridge处理全长DNA并显式建模异构体复用。这一差异源于任务设定：Isoformer假设表达主要由启动子区域决定，而CDBridge认为全长序列中的剪接调控对异构体选择至关重要。然而，CDBridge在绝对性能上（$R^2$ 0.387）仍低于Isoformer官方结果（0.530），暗示全长序列引入的噪声可能抵消了异构体建模的收益，或专用模型在局部特征提取上仍具优势。

从方法设计看，CDBridge借鉴ToMe的自适应压缩，与MergeDNA的动态令牌合并思路一致，但CDBridge将其应用于跨模态对齐而非单纯序列压缩。与LucaOne等统一多组学模型相比，CDBridge采用后训练桥接策略，避免了全模型重训练的高昂成本，但牺牲了RNA模态的直接建模。这种“冻结骨干+轻量连接器”的设计在计算效率上占优，但可能限制了模型对RNA中间态的精细捕捉，其在全长序列上的性能瓶颈是否源于缺乏RNA显式建模，论文未给出回答。

## 总结

CDBridge旨在解决DNA序列到组织特异定量表达的映射难题，切入点是利用后训练桥接策略融合冻结的DNA与蛋白模型，通过ToMe自适应合并处理长度失配，组织条件解码器实现环境感知。实验表明，其在GTEx-Benchmark上平均 $R^2$ 达 0.387，Spearman 0.618，显著优于单组学基线。然而，其性能仍低于专用表达模型Isoformer的官方结果，且依赖高质量异构体注释与组织表达图谱，跨物种泛化能力未验证。当支持集增大或引入RNA中间态建模时，全长序列桥接策略的性能上限是否会被突破，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_58157616)