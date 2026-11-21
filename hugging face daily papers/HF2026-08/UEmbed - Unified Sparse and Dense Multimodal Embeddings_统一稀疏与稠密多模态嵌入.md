# HuggingFace最新推荐论文 ｜UEmbed: Unified Sparse and Dense Multimodal Embeddings ｜统一稀疏与稠密多模态嵌入

研究机构：阿里巴巴集团、中国科学院大学

作者：Tingyu Song、Mingxin Li、Yanzhao Zhang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2608.02583)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.02583)

> 现有学习稀疏检索（LSR）方法受限于双向编码器架构，无法直接利用因果大语言模型（LLM）的高效推理栈，且多模态扩展依赖辅助模块。本文指出因果注意力下的单Token投影存在信息瓶颈，提出在解码器末尾追加可学习特殊Token并划分词表子集，实现稀疏与稠密表示的统一生成。该方法在公开数据训练的多模态稀疏检索中达到当前最优，但其文本检索性能与专有数据训练的强基线仍有差距，且未报告标准文本嵌入基准成绩。

## 研究背景

检索系统依赖词项匹配或语义向量计算相关性。传统BM25依赖精确词项重叠，缺乏语义泛化能力；学习稀疏检索（LSR）通过神经模型重加权词项并扩展语义相关词，提升了检索质量。然而，主流LSR方法如SPLADE基于BERT等双向编码器，其Max-Pooling机制依赖全局上下文可见性。因果LLM的单向注意力屏蔽了未来Token，导致直接复用Max-Pooling失效，且双向化改造破坏了vLLM等高效推理框架的兼容性。

多模态检索进一步加剧了这一矛盾。现有方法通常引入辅助跨模态模块处理图像或视频，限制了新模态的扩展性。同时，稀疏检索的实际部署优势（如倒排索引支持、低延迟）在学术评估中常被忽视。本文切入点在于：不改变因果架构，通过结构化的词表分区投影，在单一前向传播中同时生成稀疏与稠密表示，并原生支持多模态输入。

## 核心方法

### 方法参照系

标准LSR流程基于双向编码器，对每个Token隐藏状态进行词表投影并Max-Pooling。本文问题在于：因果LLM无法访问未来Token，Max-Pooling失效；且单Token（如EOS）投影至高维词表存在表示容量瓶颈。本文差异在于保留因果掩码，通过追加特殊Token与词表分区解决信息瓶颈。

### 词表分区与稀疏头

针对单Token投影容量不足的问题，UEmbed在输入序列末尾追加$N=16$个可学习特殊Token。首先通过K-means聚类将压缩后的词表$V$划分为$N$个不相交子集$V_1, \dots, V_N$。每个特殊Token$\langle s_k \rangle$仅负责预测其对应子集$V_k$中的词项权重。稀疏权重计算公式为：

$$ w_t^{(k)} = \log \left( 1 + \text{ReLU}(W_t^{(k)\top} h_{s_k} + b_t^{(k)}) \right), \quad \forall t \in V_k $$

其中$h_{s_k}$为第$k$个特殊Token的最终隐藏状态。最终稀疏向量由所有子集向量拼接而成。这一设计将高维投影任务分解为$N$个低维子任务，每个特殊Token在因果注意力下总结前序输入，避免了单Token的信息瓶颈，同时保持了因果结构的完整性。

### 统一训练目标

UEmbed通过联合损失函数同时优化稠密与稀疏表示。稠密嵌入取自特殊Token前的EOS隐藏状态。统一目标函数为：

$$ \mathcal{L} = \mathcal{L}_{\text{InfoNCE}}^{\text{dense}} + \lambda \mathcal{L}_{\text{InfoNCE}}^{\text{sparse}} + \alpha_q \mathcal{L}_{\text{FLOPS}}^q + \alpha_d \mathcal{L}_{\text{FLOPS}}^d $$

其中$\mathcal{L}_{\text{InfoNCE}}^{\text{dense}}$使用余弦相似度，$\mathcal{L}_{\text{InfoNCE}}^{\text{sparse}}$使用内积。FLOPS正则项惩罚词项权重的平方均值，鼓励稀疏性。该设计动机在于：稀疏与稠密表示共享骨干网络，联合训练可促进特征互补，且FLOPS正则化确保稀疏向量在倒排索引中的高效检索。

## 实验评估

实验基于Qwen3.5骨干，在MMEB-v2（多模态）与BEIR（文本）上评估。基线覆盖SPLADE-v3、Echo-Mistral-SPLADE（稀疏）及GME-7B、Qwen3-VL-Embedding（稠密）。缺失ColBERT等多向量基线，且未报告MTEB English总分，限制了与领域标准基准的直接对比。

| 模型 | MMEB-v2 Dense | MMEB-v2 Sparse | BEIR Avg (Dense) | BEIR Avg (Sparse) |
| :--- | :--- | :--- | :--- | :--- |
| UEmbed-9B | 71.8 | 71.0 | 56.3 | 55.2 |
| UEmbed-4B | 70.4 | 69.7 | 56.0 | 53.6 |
| UEmbed-2B | 66.5 | 65.5 | 53.6 | 52.3 |
| Qwen3-VL-Embedding-8B | 77.8 | - | 55.5 | - |
| SPLADE-v3 | - | - | - | 50.5 |
| Echo-Mistral-SPLADE | - | - | - | 55.2 |

UEmbed-9B在MMEB-v2稠密模式得分71.8，低于Qwen3-VL-Embedding-8B的77.8，但后者使用专有数据。在公开数据训练的模型中，UEmbed-9B领先RzenEmbed-V2-7B（71.1）。稀疏模式得分71.0，与稠密模式差距仅0.8分，且在VisDoc任务上表现稳定（79.1 vs 79.2）。BEIR文本检索中，UEmbed-9B稀疏平均55.2，与Echo-Mistral-SPLADE持平，但低于其稠密模式56.3。

消融实验显示，联合训练优于单模式训练。在MMEB-v1图像子集上，UEmbed-2B稠密模式64.5，稀疏模式63.4，均显著高于双向SPLADE基线（61.3）。词表分区策略中，语义聚类（K-means）优于随机与最大距离分区，平均得分63.4 vs 63.0/63.2。特殊Token数量$N$对性能影响较小，表明分区策略的鲁棒性。

评估边界方面，论文未报告置信区间，且MMEB-v2与BEIR的评估协议未统一。代码与超参数已公开，但训练数据规模（3.94M样本）与Qwen3-VL的专有数据规模差异巨大，直接性能对比需谨慎。

## 关联研究分析

从方法设计看，UEmbed与LLM2Vec形成鲜明对比。LLM2Vec通过移除因果掩码实现双向注意力，牺牲了推理效率以换取全局语义捕获；UEmbed保留因果掩码，通过词表分区解决信息瓶颈，优先保证部署兼容性。这一差异源于任务特性：稀疏检索依赖词项激活，分区投影天然适配因果结构，而稠密检索更依赖全局上下文聚合。UEmbed证明在稀疏任务中，因果结构并非绝对障碍，但其在稠密模式下的性能（71.8）仍低于双向化模型，暗示因果注意力在稠密语义捕获上仍有局限。

从问题动机看，UEmbed与SPLADE系列同属LSR路线，但SPLADE依赖双向编码器，UEmbed将其适配至因果LLM。与多模态嵌入模型如GME-7B相比，GME仅生成稠密表示，UEmbed统一稀疏与稠密，并原生支持多模态。GME-7B在BEIR稠密模式得分53.5，低于UEmbed-9B的56.3，但GME在MMEB-v2稠密模式得分57.3，远低于UEmbed的71.8。这一差距可能源于UEmbed的多模态数据混合策略，但论文未详细分析数据贡献，仅指出使用Qwen3-VL-Embedding-8B挖掘硬负例。

## 总结

UEmbed解决的核心矛盾是因果LLM的高效推理与稀疏检索的全局语义需求之间的冲突。其切入点在于利用词表分区将高维投影分解为低维子任务，在保留因果结构的同时突破单Token信息瓶颈。方法上，通过追加特殊Token与K-means词表分区，联合训练稀疏与稠密表示。实验证明，UEmbed-9B在MMEB-v2稀疏模式得分71.0，稠密模式71.8，在公开数据训练的多模态稀疏检索中达到SOTA，且稀疏与稠密性能差距小于1分。边界在于，其文本检索性能（BEIR 55.2）与专有数据训练的Qwen3-VL-Embedding（55.5）接近，但多模态性能差距较大（71.8 vs 77.8），且未报告MTEB标准基准成绩。当词表分区数量$N$增加时，稀疏表示的细粒度是否进一步提升，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.02583)