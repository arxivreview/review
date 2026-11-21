# ACL-Findings2026最新论文 ｜HORIZON: A Benchmark for In-the-wild User Behaviour Modeling ｜HORIZON：跨域长时序用户行为建模基准

研究机构：美国卡内基梅隆大学、微软研究院

作者：Arnav Goel、Pranjal A Chitale、Bhawna Paliwal 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17259)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17259)

> 序列推荐领域长期依赖单域、短窗口的下一项预测任务，导致模型在真实多平台、长周期场景下的泛化能力被高估。现有基准如Amazon Reviews按类别隔离交互，无法捕捉跨域转移，且Leave-One-Out评估存在时间泄漏，掩盖了分布偏移下的性能衰减。HORIZON通过合并Amazon Reviews全类别构建54.51M用户的统一历史，并引入全局时间截断与用户可见性解耦的四象限评估协议，系统量化了模型在时间外推与未见用户场景下的鲁棒性边界。该基准揭示了Transformer骨干在分布偏移下的显著退化及LLM零样本建模的局限，但其评估协议对计算效率的忽视及基线覆盖的缺失，限制了其对工业部署可行性的全面判断。

## 研究背景

序列推荐的核心挑战在于从动态行为流中提炼稳定的兴趣表征，但工业级场景要求模型同时处理超长历史与跨域语义。传统方法如SASRec（Kang and McAuley, 2018）通过自注意力捕捉长程依赖，但其二次复杂度在数千项交互下导致内存爆炸，且单域训练假设与用户实际跨平台行为不符。当模型面对未见用户或时间外推时，其依赖的协同过滤信号失效，暴露出对分布偏移的脆弱性。

现有基准如MovieLens和Yelp规模小且单域，Amazon Reviews虽大但按类别分割，阻碍了跨域信号利用。PinnerFormer和USE虽涉及长时序，但数据私有不可复现。HORIZON的切入点在于将“长序列”从数据长度扩展为时间维度的分布偏移，通过开源化与结构化评估，填补了真实场景下跨域泛化能力的量化空白。

## 核心方法

### 方法参照系

序列推荐标准流程为：给定历史序列 $S_u$，预测下一项 $i_{n+1}$。本文问题与该通用流程的关键差异在于：评估不再局限于训练分布内的下一项预测，而是解耦时间位置与用户可见性，考察模型在分布偏移下的泛化边界。

### 跨域数据重构与统一历史构建

传统基准按类别隔离交互，导致模型学习碎片化的域特定表示，无法捕捉跨类别转移。HORIZON合并Amazon Reviews 2023所有类别，构建统一用户历史，其形式化表示为：

$$ H_u = [i_1, i_2, \dots, i_t] \in \mathcal{I}^t $$

其中 $\mathcal{I}$ 为跨域物品全集。这一设计消除了人工域边界，使模型能学习全局用户偏好，解决了单域模型在跨域场景下因信号稀疏导致的表示质量下降问题。

### 多轴解耦评估协议

传统Leave-One-Out评估存在时间泄漏，且无法区分时间外推与用户泛化的影响。HORIZON引入全局时间截断 $\tau=2020$ 与用户可见性维度，定义四个评估设置：

$$ \text{Eval} = \{ \text{IND/Aligned}, \text{IND/Extrap}, \text{OOD/Aligned}, \text{OOD/Extrap} \} $$

其中IND表示训练集内用户，OOD表示未见用户；Aligned表示 $\tau$ 前交互，Extrap表示 $\tau$ 后交互。该协议通过固定训练集（100K用户），独立评估模型在时间漂移与用户身份变化下的性能，揭示了单一指标无法捕捉的鲁棒性差异。

## 实验评估

实验基于HORIZON基准，基线包括GRU4Rec、SASRec、BERT4Rec和CORE，缺失生成式范式（如TIGER）及高效长序列模型（如VISTA）。在Task 1中，SASRec在IND/Aligned下NDCG@10为8.7，而在OOD/Aligned下升至17.8，这一反直觉结果可能源于OOD用户历史长度或分布特性差异，但论文未深入分析。LLM任务中，Qwen3-8B在Query Reformulation任务Recall@10为2.37，低于专用模型预期，表明零样本LLM在行为建模上存在语义鸿沟。

| 模型 | IND/Aligned NDCG@10 | OOD/Aligned NDCG@10 | IND/Extrap Recall@10 | OOD/Extrap Recall@10 |
| :--- | :--- | :--- | :--- | :--- |
| SASRec | 8.7 | 17.8 | 3.6 | 3.9 |
| BERT4Rec | 26.4 | 11.8 | 9.4 | 9.9 |
| GRU4Rec | 0.08 | 0.01 | 0.01 | 0.01 |

评估边界方面，论文未报告计算效率指标（如推理延迟、内存占用），且LLM任务依赖BLAIR嵌入，可能引入检索偏差。代码开源于`microsoft/horizon-benchmark`，但超参数配置未完全公开，可复现性受限。

## 关联研究分析

从问题动机看，HORIZON与PinnerFormer均关注长时序用户建模，但PinnerFormer依赖私有数据，HORIZON通过开源化实现了可复现的跨域评估。差异根源在于任务特性：PinnerFormer侧重多模态交互，HORIZON聚焦文本行为序列，导致后者更适用于电商场景。从方法设计看，HORIZON与SASRec等Transformer骨干的对比揭示了其在分布偏移下的局限性，而TIGER等生成式模型未纳入基线，可能因语义ID与行为ID的融合策略在跨域场景下尚未成熟。LLM在Task 2/3中表现不佳，是否因缺乏推荐领域微调，还是其语义空间与行为ID空间存在根本性鸿沟，论文未给出回答。

## 总结

HORIZON要解决的核心矛盾是现有基准无法量化模型在真实跨域长时序场景下的泛化能力。其切入点在于通过数据重构与多轴评估协议，解耦时间漂移与用户身份变化的影响。论文构建了54.51M用户的开源基准，并证明SASRec在OOD用户下NDCG@10从8.7升至17.8，而BERT4Rec从26.4降至11.8，揭示了不同架构在分布偏移下的鲁棒性差异。其边界在于未覆盖生成式模型基线，且评估协议忽视计算效率。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17259)