# CVPR2026最新论文 ｜Rethinking Token Reduction for Large Vision-Language Models ｜多轮对话视觉Token压缩

研究机构：浙江大学、新加坡国立大学

作者：Yi Wang、Haofei Zhang、Qihan Huang 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.21701)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.21701)

> 视觉语言模型在多轮问答中面临视觉Token冗余与未来查询不可预测的双重约束，现有基于单轮Prompt的剪枝策略会误删后续轮次所需信息，而纯视觉启发式方法又缺乏理论最优性。本文切入点在于将Token压缩重构为与Prompt无关的可学习线性映射，通过数据驱动方式直接优化响应分布一致性。该方法在三个多轮基准上显著优于FastV等启发式基线，但其固定压缩率与单图像训练范式限制了在动态分辨率与视频场景下的泛化能力。

## 研究背景

多轮视觉问答（Multi-Turn Visual Question Answering, MT-VQA）要求模型在保持同一图像上下文的前提下，连续回答多个语义无关的问题。与单轮VQA不同，MT-VQA中后续问题的相关区域在首轮完全不可知，这导致基于当前文本Prompt的注意力引导剪枝（如FastV）产生系统性偏差：首轮聚焦前景时，背景Token被剪除，导致后续背景相关问题的回答能力崩塌。同时，主流视觉语言模型（LVLMs）采用多尺度视觉塔生成数千个Token，二次方注意力计算使得全量处理在资源受限设备上不可行。

现有Token压缩方法分为Prompt依赖与Prompt无关两类。Prompt依赖方法（如FastV、FitPrune）利用文本引导识别冗余，但无法适应多轮场景的动态性；Prompt无关方法（如PruMerge）仅基于图像内部注意力或相似度合并Token，虽技术上适用于多轮，但依赖人工先验的启发式准则，缺乏理论最优性保证，且在多尺度视觉塔架构下兼容性差。本文针对这一空白，提出一种学习式、Prompt无关的压缩框架，旨在通过数据驱动方式替代启发式规则，解决多轮对话中Token保留策略与未来查询解耦的问题。

## 核心方法

### 压缩映射统一框架

视觉Token压缩可统一表述为对视觉序列 $X_{IMG} \in \mathbb{R}^{n \times d}$ 的线性投影，即 $\tilde{X}_{IMG} = P X_{IMG}$，其中 $P \in \mathbb{R}^{m \times n}$ ($m \ll n$) 为稀疏压缩矩阵。该框架将剪枝（Pruning）与合并（Merging）视为同一映射的特例：剪枝对应 $P$ 的行选择，合并对应 $P$ 的加权组合。本文的关键差异在于，$P$ 不再是基于注意力分数或相似度阈值的手工设计结果，而是作为可学习参数，通过最小化压缩前后LLM响应分布的KL散度进行端到端优化，从而摆脱对中间注意力矩阵的依赖，兼容FlashAttention等不回传注意力图的高效推理机制。

### 元压缩矩阵生成器

为解决不同分辨率输入导致 $P$ 维度变化的问题，本文设计了一个轻量级元生成器 $P_{meta}$，仅以图像序列 $X_{IMG}$ 为条件生成自适应形状的压缩矩阵。其核心机制是计算空间下采样后的查询向量与原始键向量的加权内积：

$$ P = \sigma(D_q \text{Pool}(X_{IMG} + E_{pos}) \cdot \omega \cdot D_k X_{IMG}) $$

其中 $\text{Pool}(\cdot|k, s)$ 为平均池化，$D_q, D_k$ 为低秩投影矩阵，$\omega$ 为可学习对角矩阵，$\sigma$ 为行级Softmax。该设计动机在于，直接为每种分辨率训练独立矩阵既低效又缺乏泛化性，而通过低秩内积机制，$P_{meta}$ 能够以极少参数（$d_c \ll d$）动态生成任意 $m \times n$ 的压缩矩阵，同时保持计算开销与 $O(n)$ 线性增长，避免了全连接矩阵的内存爆炸。

### 数据高效训练目标

训练过程通过最小化压缩前后LLM输出分布的KL散度 $L_{pred} = D_{KL}(p(y) \| p(\tilde{y}))$ 与压缩矩阵行熵正则项 $L_{entropy} = \frac{1}{m}\sum_{i=0}^m H(P_{i,:})$ 的加权和来优化 $P_{meta}$ 参数。熵正则项防止压缩矩阵退化为单行独大，确保保留Token的空间多样性。该目标函数的设计直接回应了启发式方法“注意力高即重要”的假设失效问题：实验表明，学习到的最优保留Token与[CLS]或Prompt注意力分数无显著相关性，证明数据驱动的分布一致性优化比单一信号引导更鲁棒。

## 实验评估

实验在MT-VQA-v2、MT-GQA和ConvBench三个多轮基准上进行，对比基线包括Random、Sample、FastV和PruMerge。基线覆盖审计显示，本文缺失VisionZip、SparseVLM等单轮SOTA方法的直接对比，但鉴于这些方法均为Prompt依赖或单轮设计，在MT-VQA场景下不适用，故以FastV（Prompt依赖代表）和PruMerge（Prompt无关启发式代表）作为主要对照是合理的。

| 模型 | 方法 | MT-GQA Avg | ConvBench Avg |
|---|---|---|---|
| LLaVA-1.5-7b | Base | 63.73 | 4.16 |
| LLaVA-1.5-7b | FastV | 45.66 | 3.99 |
| LLaVA-1.5-7b | PruMerge | 57.54 | 4.16 |
| LLaVA-1.5-7b | Ours | 58.43 | 4.16 |
| LLaVA-NeXT-7b | Base | 66.15 | 7.28 |
| LLaVA-NeXT-7b | FastV | 50.31 | 5.60 |
| LLaVA-NeXT-7b | Ours | 62.70 | 7.28 |

在90%压缩率下，MetaCompress在MT-GQA上达到58.43%（LLaVA-1.5-7b），显著高于FastV的45.66%和PruMerge的57.54%；在ConvBench上，MetaCompress与Base持平（4.16%），而FastV降至3.99%，验证了Prompt无关学习式压缩在多轮场景下的优势。消融实验表明，仅使用 $L_{collapse}$ 会导致训练发散，需引入梯度裁剪；$L_{entropy}$ 权重在0.5-1.5范围内性能波动小于0.5个百分点，显示方法对超参数不敏感。

评估边界方面，本文未报告置信区间，且ConvBench基准仅包含3个子集，统计显著性有限。代码已开源，但训练数据规模与GPU资源未在正文中明确量化，可复现性依赖附录细节。

## 关联研究分析

从问题动机看，MetaCompress与VisionSelector同属学习式压缩路线，但VisionSelector侧重单轮任务对齐，其可学习评分器依赖文本Prompt引导，而MetaCompress通过Prompt无关设计解决多轮场景下未来查询不可预测的问题。这一差异根源在于任务特性：单轮VQA中Prompt是静态且完整的，而MT-VQA中Prompt是动态且局部的，导致基于Prompt的评分器在多轮中产生系统性偏差。

从方法设计看，MetaCompress与PruMerge均采用Pre-LLM位置，但PruMerge依赖图像内部注意力启发式合并，而MetaCompress使用可学习内积生成压缩矩阵。PruMerge的启发式准则源于人类对视觉显著性的先验，而MetaCompress通过KL散度优化直接对齐LLM响应分布，避免了启发式规则在分布外数据上的失效。然而，MetaCompress的固定压缩率（90%/70%）与PruMerge类似，未实现自适应动态预算，这限制了其在图像复杂度差异极大场景下的性能上限。

## 总结

本文核心矛盾在于多轮对话中视觉Token压缩策略与未来查询解耦的必要性，现有Prompt依赖方法因首轮偏差失效，启发式Prompt无关方法缺乏理论最优性。MetaCompress通过可学习压缩矩阵生成器与KL散度优化，实现了数据驱动的Prompt无关压缩，在MT-GQA上以58.43%准确率超越FastV的45.66%。其边界在于固定压缩率无法适应动态复杂度，且训练范式依赖单图像分布，未验证在视频或极端压缩率下的鲁棒性。当图像复杂度从简单场景跃升至密集细节场景时，固定90%压缩率是否导致关键信息不可逆丢失，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.21701)