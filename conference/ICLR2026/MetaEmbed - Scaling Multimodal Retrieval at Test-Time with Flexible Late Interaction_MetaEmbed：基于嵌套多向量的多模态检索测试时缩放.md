# ICLR2026最新论文 ｜MetaEmbed: Scaling Multimodal Retrieval at Test-Time with Flexible Late Interaction ｜MetaEmbed：基于嵌套多向量的多模态检索测试时缩放

研究机构：美国莱斯大学

作者：Zilin Xiao、Qi Ma、Mengting Gu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.18095)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.18095)

> 多模态检索面临单向量表示丢失细粒度语义与多向量表示计算成本过高的双重困境。现有方法要么将查询与候选压缩为单一向量导致信息瓶颈，要么保留数百个Token级向量导致索引膨胀与延迟激增，且无法支持图像到图像的检索。本文提出MetaEmbed，通过引入少量可学习Meta Tokens并采用Matryoshka Multi-Vector Retrieval (MMR) 训练策略，实现了检索精度与计算预算在测试时的动态权衡。该方法在MMEB和ViDoRe基准上取得了SOTA性能，但其对骨干模型能力的依赖及Meta Tokens的语义可解释性仍存疑。

## 研究背景

多模态检索的核心挑战在于异构输入的统一表示。当查询与候选涉及图像、文本或其组合时，模型需将不同模态映射至共享空间。传统单向量方法（如CLIP）通过对比学习对齐模态，但将复杂指令或细粒度视觉细节压缩为单一向量时，语义信息发生不可逆丢失。为解决此问题，ColBERT等延迟交互（Late Interaction, LI）方法保留Token级嵌入，通过MaxSim计算细粒度相关性，但每张图片产生数百个Patch嵌入，导致索引存储与检索延迟呈线性增长，且在图像-图像检索中因Token数量乘积效应变得不可行。

多模态嵌入领域的主流路线分为单向量与多向量两类。单向量方法（如VLM2Vec、MoCa）依赖VLM骨干提取全局表示，虽部署简单但受限于表达力上限；多向量方法（如ColPali、ColQwen）保留细粒度信息但缺乏灵活性，无法在精度与效率间动态调整。现有工作未解决多向量检索中“向量数量固定”导致的资源浪费或性能不足问题。本文切入点在于借鉴Matryoshka Representation Learning (MRL) 的嵌套思想，将向量数量作为可调节变量，通过训练时并行优化不同粒度的嵌套组，实现测试时根据计算预算选择检索精度，从而突破多模态检索的效率瓶颈。

## 核心方法

### 方法参照系

标准多模态检索流程包含编码、索引与评分三阶段。单向量方法将输入编码为固定维度向量，通过内积评分；多向量方法（如ColBERT）保留Token级向量，通过MaxSim聚合相似度。本文问题与通用流程的关键差异在于：传统多向量方法向量数量固定且无层级结构，无法在测试时动态调整计算资源，而本文旨在构建一种支持“粗到细”粒度切换的灵活多向量表示。

### Meta Tokens 与紧凑多向量表示

**设计动机**：解决Token级嵌入数量过多导致的索引膨胀与计算爆炸问题，同时保留细粒度语义。
在VLM输入序列末尾追加少量可学习的Meta Tokens（查询侧 $M_q \in \mathbb{R}^{R_q \times D}$，候选侧 $M_c \in \mathbb{R}^{R_c \times D}$）。VLM处理后，提取这些Token的最后层隐藏状态作为Meta Embeddings，并进行L2归一化。

$$
\mathbf{E}^{(meta)}_q = \text{Normalize}(F_\theta(z^{(0)})[P+n+1 : P+n+R_q])
$$

该公式表明，Meta Embeddings并非原始Patch或Token的简单平均，而是经过VLM全上下文交互后的压缩表示，以极少的向量数量（如16或64个）替代数百个Patch嵌入，大幅降低索引规模。

### Matryoshka Multi-Vector Retrieval (MMR)

**设计动机**：解决固定向量数量无法适应不同计算预算的问题，实现测试时缩放。
将Meta Embeddings划分为 $G$ 个前缀嵌套组。对于第 $g$ 组，查询侧使用前 $r_{q,g}$ 个向量，候选侧使用前 $r_{c,g}$ 个向量。训练时并行优化所有组的对比损失，确保每个前缀组自身具有判别力。

$$
\mathcal{L}_{MMR} = \sum_{g=1}^{G} w_g \mathcal{L}_{InfoNCE}(\mathbf{E}^{(q,g)}, \mathbf{E}^{(c,g)}, \mathbf{E}^{(c,-)})
$$

其中 $\mathcal{L}_{InfoNCE}$ 为基于MaxSim的InfoNCE损失。此设计使得模型在测试时可根据延迟约束选择组大小 $(r_{q,g}, r_{c,g})$：小前缀组用于快速粗筛，大前缀组用于精细排序，无需重训练即可调整精度-效率权衡。

## 实验评估

实验在MMEB（36任务）和ViDoRe v2（7任务）上进行，基线覆盖单向量（CLIP, MoCa, mmE5）与多向量（ColPali, ColQwen）方法。MetaEmbed-32B在MMEB Overall达到78.7，显著优于MoCa-7B（71.5）和mmE5（69.8）；在ViDoRe v2上，MetaEmbed-7B平均NDCG@5为61.3，优于MoCa-7B（58.8）和ColQwen2（57.5）。

| 模型 | 规模 | MMEB Overall | ViDoRe Avg NDCG@5 |
| :--- | :--- | :--- | :--- |
| MoCa-7B | 7B | 71.5 | 58.8 |
| mmE5 | 11B | 69.8 | 50.5 |
| ColQwen2 | 2B | - | 57.5 |
| MetaEmbed-7B | 7B | 76.6 | 61.3 |
| MetaEmbed-32B | 32B | 78.7 | - |

消融实验显示，检索预算从(1,1)增加到(16,64)时，MetaEmbed-7B的MMEB分数从71.2提升至76.6，增益随模型规模增大而扩大。32B模型在(16,64)预算下达到78.7，而3B模型仅69.1，表明MMR机制在大规模模型上能更有效地利用嵌套结构。然而，Llama-3.2-Vision骨干的MetaEmbed-11B在VQA任务上得分仅为42.1，远低于Qwen2.5-VL骨干的74.2，暴露出骨干模型生成能力对嵌入性能的强依赖。

评估边界方面，论文未报告置信区间，且ViDoRe v2结果未包含32B模型数据。代码已开源，训练使用32块H100 GPU，LoRA秩为32，温度系数0.03。多语言性能虽在ViDoRe中表现良好，但未在MMEB中单独量化，且未对比纯文本SOTA模型（如Qwen3-Embedding）作为跨模态参照。

## 关联研究分析

从问题动机看，MetaEmbed与ColBERT同属延迟交互范式，但ColBERT保留所有Token嵌入导致多模态场景下计算不可行，而MetaEmbed通过Meta Tokens将向量数量压缩至可控范围。这一差异源于多模态输入（尤其是图像）的Token数量远超文本，直接应用ColBERT会导致索引爆炸。MetaEmbed的嵌套设计借鉴了MRL在单向量维度上的压缩思想，但将其扩展至向量数量维度，解决了多向量检索中“全有或全无”的资源分配问题。

从方法设计看，MetaEmbed与MoCa等单向量VLM嵌入方法共享对比学习训练框架，但MoCa依赖单向量全局表示，缺乏细粒度匹配能力。MetaEmbed通过MMR模块在训练时并行优化多粒度表示，使得测试时能根据任务需求动态选择精度。这种设计使得MetaEmbed在ViDoRe v2的多语言与生物医学领域表现优于MoCa，尽管未使用多语言训练数据，暗示VLM骨干的跨语言能力通过多向量结构得到了更充分的利用。

## 总结

MetaEmbed旨在解决多模态检索中单向量信息丢失与多向量计算成本过高的矛盾。其切入点在于将向量数量作为可调节变量，通过Meta Tokens压缩表示并采用MMR训练策略实现测试时缩放。实验证明，该方法在MMEB和ViDoRe v2上取得SOTA性能，32B模型Overall分数达78.7，7B模型ViDoRe平均NDCG@5为61.3。然而，论文暴露出骨干模型能力对嵌入性能的强依赖，Llama-3.2-Vision骨干在VQA任务上的显著劣势表明，Meta Tokens本身可能不具备独立的语义鲁棒性，而是高度依赖VLM的预训练知识。当骨干模型在特定领域（如VQA）表现较弱时，MetaEmbed能否通过多向量结构弥补这一缺陷，而非仅仅继承其弱点，论文未给出明确回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.18095)