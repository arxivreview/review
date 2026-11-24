# ACL-Findings2026最新论文 ｜PRA-RAG: Provably Robust Aggregation in Retrieval-Augmented Generation against Retrieval Corruption ｜可证明鲁棒检索聚合

研究机构：复旦大学、美国伍斯特理工学院

作者：Xue Tan、Yi Zheng、Chang Huo 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.00012)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.00012)

> 检索增强生成（Retrieval-Augmented Generation, RAG）系统面临外部知识库投毒攻击，导致生成结果被恶意操纵。现有防御机制依赖大语言模型（LLM）内部知识进行启发式检测，缺乏理论保证且在模型知识不足时失效。本文提出PRA-RAG，通过在嵌入空间构建最小半径球进行组合聚合，提供语义偏差的理论上界。该方法在保持高准确率的同时将攻击成功率降至1%，但组合爆炸限制了检索规模的扩展性。

## 研究背景

RAG系统通过检索外部文档增强LLM的生成能力，其核心流程包含检索与生成两个阶段。检索器将查询编码为向量，从知识库中选取Top-K最相似文档作为上下文；LLM结合查询与上下文生成回答。当攻击者向知识库注入恶意文档时，检索器可能将这些文档纳入Top-K集合，进而误导LLM生成攻击者指定的错误答案。这种检索污染攻击（Retrieval Corruption Attack）构成了RAG系统的主要安全威胁。

针对检索污染，现有防御路线主要分为两类。检测类方法如AstuteRAG和TrustRAG利用LLM的内部知识识别并过滤恶意文档，但这类方法的有效性高度依赖LLM对特定领域知识的掌握程度，在LLM知识匮乏的场景下防御能力显著下降。投票类方法如RobustRAG通过多次LLM生成并投票来过滤污染内容，虽然提供了鲁棒性保证，但需要多次调用LLM，计算开销巨大且输出聚合困难。这些方法均缺乏对RAG系统鲁棒性的量化评估框架，无法在理论上证明防御效果。

本文的切入点在于将检索污染建模为集合扰动问题，在嵌入空间而非LLM输出空间进行鲁棒聚合。通过引入组合嵌入和最小半径球概念，PRA-RAG实现了模型无关的鲁棒性保证，避免了依赖LLM内部知识的局限性，同时通过几何聚合替代多次LLM生成，显著降低了计算开销。

## 核心方法

### 方法参照系

标准RAG流程直接拼接Top-K检索文档作为LLM上下文。本文的关键差异在于：不直接使用原始文档，而是对Top-K文档的所有n元子集进行组合嵌入，在嵌入空间中寻找覆盖多数子集的最小半径球，以球心对应的子集进行加权聚合。这一设计将鲁棒性保证从LLM层面转移至检索嵌入层面。

### 组合嵌入与最小半径球

传统方法直接处理单个文档嵌入，无法有效区分干净文档与污染文档的集合差异。本文引入组合嵌入概念，将Top-K文档的所有n元子集分别编码为向量。设$S_{X,n} = \{s_1, s_2, \ldots, s_L\}$为从K个文档中抽取的所有n元子集，其中$L = \binom{K}{n}$。每个子集$s_i$的嵌入向量$v_i$由其中所有文档嵌入的拼接构成：

$$v_i = \text{Concat}([\text{Embed}(p) \mid p \in s_i])$$

这一设计动机在于：污染文档在组合嵌入中会形成离群点，而干净文档的组合嵌入会聚集在特定区域。通过寻找覆盖超过半数组合嵌入的最小半径球，可以自动识别并排除污染文档的影响。

### 鲁棒聚合与偏差认证

在确定最小半径球中心后，本文计算该球心对应子集的加权平均嵌入作为最终检索表示。权重由每个文档与查询的余弦相似度决定：

$$x^* = \sum_{p \in s_{i^*}} w_p \cdot \text{Embed}(p), \quad w_p = \frac{\cos(\text{Embed}(p), \text{Embed}(q))}{\sum_{p' \in s_{i^*}} \cos(\text{Embed}(p'), \text{Embed}(q))}$$

这一加权机制防止污染文档因与干净文档语义相似而逃避过滤。基于最小半径球半径$\hat{R}$，本文定义了可证明平均偏差（Provable Average Deviation, PAD）指标，提供语义偏差的理论上限：

$$\text{PAD} = (1 + \beta) \hat{R}$$

其中$\beta$为安全系数。PAD值越低，表明系统对投毒攻击的鲁棒性越强，同时保留了原始检索语义。

## 实验评估

实验在Natural Questions (NQ)、MS-MARCO和HotpotQA三个问答数据集上进行，测试PRA-RAG对PoisonedRAG、DoS Attack、AdvDec和CorruptRAG四种攻击的防御效果。基线方法覆盖检测类（AstuteRAG、TrustRAG、RAGForensics）和投票类（RobustRAG、InstructRAG），但未包含加密检索类方法如p2RAG，因任务侧重不同。

| 模型 | 数据集 | 攻击类型 | ACC | ASR | PAD |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Mistral-7B | MS-MARCO | PoisonedRAG | 0.63 | 0.01 | 1.37 |
| Vicuna-7B | MS-MARCO | PoisonedRAG | 0.68 | 0.01 | 1.91 |
| GPT-3.5-turbo | MS-MARCO | PoisonedRAG | 0.75 | 0.01 | 1.09 |

在MS-MARCO数据集上，PRA-RAG在20%污染率下将ASR降至0.01（1%），同时保持ACC在0.63-0.75之间，显著优于基线方法。例如，Mistral-7B在PoisonedRAG攻击下，PRA-RAG的ACC为0.63，而RobustRAG仅为0.33，AstuteRAG为0.66但ASR为0.12。

消融实验揭示了Top-K、污染规模ε和子集大小n对PAD的影响。当Top-K从8增至16时，PAD从1.23降至0.90，表明增加检索多样性可提升鲁棒性。当ε从1增至3时，PAD从1.23升至1.43，说明更多污染文档会削弱防御效果。子集大小n从3增至5时，PAD从1.74降至1.16，表明更大的子集能更好地稀释污染内容的影响。

| 数据集 | ASTUTE RAG | InstructRAG | RobustRAG | PRA-RAG |
| :--- | :--- | :--- | :--- | :--- |
| NQ | 13.68s | 6.89s | 27.01s | 5.98s |
| MS-MARCO | 13.84s | 7.15s | 26.38s | 6.20s |
| HotpotQA | 16.78s | 7.01s | 25.87s | 6.17s |

PRA-RAG的响应延迟在5.98-6.20秒之间，显著低于RobustRAG的25.87-27.01秒，与InstructRAG相当，优于AstuteRAG。这一效率优势源于几何聚合替代了多次LLM生成。

评估指标包含ACC、ASR和PAD，但未报告置信区间，数值比较需谨慎。实验未覆盖计算效率维度的详细分析，如GPU内存占用和并行化效果。论文未提供代码URL，可复现性受限，但算法描述详细，超参数设置（Top-K=8, n=3, 污染率=20%）明确。

## 关联研究分析

从问题动机看，PRA-RAG与RobustRAG均针对检索污染攻击，但RobustRAG依赖多次LLM生成和投票机制，计算开销高且输出聚合困难。PRA-RAG通过组合嵌入和最小半径球在嵌入空间进行鲁棒聚合，避免了LLM调用，将计算复杂度从$O(K \cdot T)$（T为LLM调用次数）降至$O(\binom{K}{n} \cdot d)$（d为嵌入维度）。这一差异源于任务特性：RobustRAG假设LLM能正确识别污染内容，而PRA-RAG假设污染文档在嵌入空间中形成离群点，无需LLM参与判断。

从方法设计看，PRA-RAG与AstuteRAG、TrustRAG等检测类方法存在根本差异。检测类方法依赖LLM内部知识识别恶意文档，在LLM知识不足时失效；PRA-RAG基于组合几何结构，提供分布无关的鲁棒性保证，不依赖LLM知识。然而，PRA-RAG的组合爆炸问题限制了K值的扩展性，当K=16时，子集数量$\binom{16}{3}=560$，计算开销显著增加。检测类方法在K值较大时仍保持线性复杂度，但缺乏理论保证。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

PRA-RAG解决了RAG系统检索污染攻击中缺乏理论保证和计算效率低下的核心矛盾。现有检测类方法依赖LLM内部知识，在知识不足时失效；投票类方法计算开销高。PRA-RAG通过组合嵌入和最小半径球在嵌入空间进行鲁棒聚合，提供了PAD理论保证，同时避免了多次LLM调用。实验表明，在MS-MARCO数据集上，PRA-RAG将ASR降至0.01，ACC保持0.63-0.75，延迟6.20秒，显著优于基线方法。然而，组合爆炸问题限制了Top-K的扩展性，当K增大时，子集数量呈指数增长，计算开销急剧增加。当Top-K从8增至16时，子集数量从56增至560，计算时间是否线性增长，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.00012)