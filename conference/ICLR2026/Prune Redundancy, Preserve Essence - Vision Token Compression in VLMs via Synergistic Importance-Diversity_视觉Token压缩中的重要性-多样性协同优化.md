# ICLR2026最新论文 ｜Prune Redundancy, Preserve Essence: Vision Token Compression in VLMs via Synergistic Importance-Diversity ｜视觉Token压缩中的重要性-多样性协同优化

研究机构：哈尔滨工业大学

作者：Zhengyao Fang、Pengyuan Lyu、Chengquan Zhang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.09480)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.09480)

> 视觉语言模型在处理高分辨率图像时，视觉Token数量的激增导致二次方注意力计算成本与内存占用成为部署的核心障碍。现有剪枝方法在保留语义显著区域与维持信息多样性之间难以兼顾，导致极端压缩率下性能崩塌。PRUNESID通过主成分语义分析聚类与组内非极大值抑制去重，实现了任务无关的Token压缩。该方法在无需训练的前提下提升了压缩效率，但其缺乏文本引导机制在细粒度任务上的表现存疑。

## 研究背景

视觉语言模型将图像编码为视觉Token序列，但高分辨率输入导致Token数量从数百激增至数千，引发二次方注意力计算成本和内存瓶颈。这一问题的根源在于Transformer架构对长序列的处理效率低下，而视觉Token中存在的空间冗余为压缩提供了理论可能。2020年Masked Autoencoders（MAE）证明仅使用25%的视觉Token即可成功重建图像，确立了视觉冗余存在的客观基础，促使研究范式从“全量处理”转向“稀疏处理”。

该领域要解决的核心矛盾是：在保持视觉-语言语义对齐与任务关键信息完整性的前提下，以最低的计算开销动态确定视觉Token的最优保留子集与数量。主流路线分为注意力引导与重复感知两类，前者保留高注意力Token但忽略背景上下文，后者通过相似度去重但可能丢弃语义关键区域。PRUNESID的切入点在于指出这两类方法均未能同时优化重要性保留与信息多样性，提出通过语义聚类与组内去重的协同机制解决这一权衡。

## 核心方法

### 方法参照系

本文问题属于Pre-LLM剪枝路线，即在视觉编码器后、LLM前执行压缩。与FastV等Intra-LLM方法不同，Pre-LLM剪枝旨在尽早降低LLM输入长度，最大化计算节省，但面临信号来源仅依赖视觉内部结构、缺乏文本引导的挑战。

### 主成分语义分析（PSCA）

PSCA将Token维度本身作为语义轴，通过低秩PCA分解识别全局语义方向，将Token聚类为语义连贯的组。设计动机是解决注意力引导方法中多个高注意力Patch捕获相似物体片段导致的冗余保留问题。

$$
\mathbf{X}_{ctr} = \mathbf{X} - \frac{1}{T}\sum_{i=1}^{T}\mathbf{x}_i
$$

该公式计算零均值Token矩阵，消除全局偏差，为后续PCA分解提供基础。

### 组内非极大值抑制（NMS）

NMS在每个语义组内基于选择分数排序，仅当Token与已选Token的最大相似度低于阈值$\tau$时保留。设计动机是解决重复感知方法中忽略Token级语义重要性、可能丢弃高注意力关键区域的问题。

$$
\tau = \lambda \cdot \rho, \quad \rho = \frac{1}{T(T-1)}\sum_{i \neq j} \frac{\mathbf{x}_i^T \mathbf{x}_j}{\|\mathbf{x}_i\|\|\mathbf{x}_j\|}
$$

该公式定义自适应阈值，其中$\rho$为全局冗余度，$\lambda$由Token预算$N$决定，确保高冗余图像执行更强抑制。

## 实验评估

实验在LLaVA-1.5、LLaVA-NeXT、Mini-Gemini及Video-LLaVA上进行，覆盖GQA、MME、POPE等11个基准。基线包括FastV、SparseVLM、VisionZip、HiRED等Pre-LLM与Intra-LLM方法，但缺失VisionSelector等端到端学习类强基线。

| 方法 | 保留Token数 | GQA | MME | POPE | VQAv2 | Avg. |
|---|---|---|---|---|---|---|
| VisionZip | 64 | 55.1 | 1690 | 77.0 | 69.0 | 92.5% |
| PRUNESID | 64 | 57.1 | 1733 | 83.8 | 67.8 | 96.3% |
| VisionZip | 160 | 55.5 | 1630 | 74.8 | 68.3 | 90.3% |
| PRUNESID | 160 | 58.9 | 1704 | 76.9 | 67.1 | 92.8% |

在LLaVA-1.5保留64 Token时，PRUNESID平均准确率96.3%，超越VisionZip的92.5%达3.8个百分点；在LLaVA-NeXT保留5.6% Token时，PRUNESID达到92.8%，较VisionZip提升2.5个百分点。

消融实验显示，PSCA聚类优于随机分组与KMeans，在保留64 Token时GQA准确率提升0.9个百分点。动态压缩率机制在MMMU等高信息方差基准上带来1.0%的性能提升，验证了自适应预算的有效性。

评估边界方面，论文未报告置信区间，数值比较需谨慎；代码已开源，但超参数$\lambda=32/N$为经验设定，缺乏理论推导；GPU使用NVIDIA A800-80GB，推理时间数据完整。

## 关联研究分析

从问题动机看，PRUNESID与VisionZip同属Pre-LLM剪枝，但VisionZip依赖显著性评分与上下文合并，而PRUNESID采用PCA聚类与NMS去重。差异根源在于VisionZip假设显著性区域包含关键信息，而PRUNESID认为语义连贯组能更好地平衡重要性-多样性，但两者均未引入文本查询信号，导致在细粒度任务上可能失效。

从方法设计看，PRUNESID的动态预算机制与Dynamic-LLaVA相似，但Dynamic-LLaVA使用轻量级预测器评估图像复杂度，而PRUNESID基于视觉冗余度$\rho$计算信息分数。差异根源在于Dynamic-LLaVA依赖外部预测器，可能引入额外计算开销，而PRUNESID利用内部结构，但$\rho$的计算需全量Token两两相似度，复杂度较高。

## 总结

PRUNESID要解决的核心矛盾是视觉Token压缩中重要性保留与信息多样性的权衡。现有方法要么保留显著区域但丢失背景，要么去重但丢弃关键语义，PRUNESID通过PSCA聚类与NMS去重的协同机制，在无需训练的前提下实现了任务无关的压缩。实验证明其在LLaVA-1.5保留64 Token时达到96.3%准确率，在LLaVA-NeXT保留5.6% Token时达到92.8%。本文的边界在于缺乏文本引导机制，论文自身实验显示在查询聚焦特定视觉细节时，极端压缩下可能忽略相关Token。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.09480)