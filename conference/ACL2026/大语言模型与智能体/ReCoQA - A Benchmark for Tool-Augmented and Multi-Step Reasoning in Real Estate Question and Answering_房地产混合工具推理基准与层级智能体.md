# ACL2026最新论文 ｜ReCoQA: A Benchmark for Tool-Augmented and Multi-Step Reasoning in Real Estate Question and Answering ｜房地产混合工具推理基准与层级智能体

作者：Yindong Zhang、Wenmian Yang、Yiquan Zhang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17944)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3847a457cf5c)

> 深度研究智能体在垂直领域面临的核心挑战是结构化数据库查询与动态外部API调用的严格依赖关系，现有通用基准将二者视为孤立能力，无法评估这种混合工作流。本文切入点在于构建首个大规模房地产混合工具推理基准ReCoQA，并实现层级智能体HIRE-Agent作为强基线。通过解耦意图解析、任务规划与工具执行，验证了层级协作在复杂多源推理中的必要性。其价值在于填补了垂直领域混合工作流评估空白，但API缓存机制掩盖了实时网络延迟对规划策略的影响，且缺乏通用DRA基线对照。

## 研究背景

当购房者在天河區寻找“通勤至吉之岛广场30分钟内、步行2公里内有小学、单价3-4万”的房源时，系统需同时处理语义模糊的隐含约束（如“通勤”隐含交通方式推断）与动态地理计算（实时路况）。这一过程要求智能体将非结构化自然语言映射为机器可执行参数，并协调静态数据库查询输出作为动态API输入，形成严格的依赖链。这种异构证据整合能力是传统检索增强生成（RAG）无法覆盖的，因为RAG仅依赖单次静态检索，而深度研究任务要求动态调整查询策略并维持长程目标一致性。

现有基准如Spider聚焦结构化查询，MACT依赖Pandas处理数据导致内存瓶颈，MapQA忽视地图数据的动态性，均将数据库查询与API调用视为孤立能力。这种割裂导致无法评估智能体在真实多源环境中的端到端推理能力，尤其是当数据库查询结果（如候选小区列表）必须动态作为外部验证工具（如距离计算API）输入时。本文针对这一缺口，提出ReCoQA基准与HIRE-Agent框架，旨在验证层级协作在解决垂直领域混合工作流中的必要性，并揭示当前大语言模型在长链推理中的具体瓶颈。

## 核心方法

### 方法参照系

本文问题属于“架构与规划策略”路线，但区别于通用DRA的端到端RL训练，其核心差异在于垂直领域中结构化查询与动态API的严格依赖关系。通用流程假设工具调用可独立执行，而本文要求数据库查询输出必须作为API输入，形成不可分割的执行链。

### 层级解耦架构

HIRE-Agent采用“理解-规划-执行”认知流，将意图解析、任务编排与工具执行解耦。设计动机在于解决单智能体在处理复杂多源任务时的上下文丢失与执行漂移问题。Front-end Agent通过微调BERT模型执行口语语言理解（SLU），将非结构化查询转化为结构化意图与槽位表示：

$$
\mathcal{S} = \text{BERT}_{\text{SLU}}(q) = \{i, s_1, s_2, \dots, s_k\}
$$

其中 $q$ 为用户查询，$i$ 为意图标签，$s_j$ 为槽位值。该公式将自然语言映射为机器可执行参数，确保后续SQL生成与API调用的准确性。Supervisor Agent基于思维链（CoT）提示生成执行计划，动态分解任务并分派给Specialist Agents。

### 异构证据整合机制

Specialist Agents包含Database Interaction Agent与Map Reasoning Agent，分别处理结构化查询与动态地理计算。设计动机在于解决静态数据局限与实时信息获取的矛盾。Database Interaction Agent通过表标题检索（TCR）模块与SQL生成模块协同工作，TCR模块利用LLM生成理想表标题摘要，再通过BM25检索器匹配实际表结构：

$$
\mathcal{T}^* = \arg\max_{\mathcal{T} \in \mathcal{D}} \text{BM25}(\text{LLM}_{\text{summary}}(q, i, s), \mathcal{T})
$$

其中 $\mathcal{D}$ 为数据库表集合，$\mathcal{T}^*$ 为最相关表。该公式通过语义相似度匹配解决模式链接问题，确保SQL生成的准确性。Map Reasoning Agent则调用Amap API工具，处理通勤时间、距离计算等动态查询，并将结果作为结构化证据返回Supervisor Agent进行综合。

## 实验评估

实验在ReCoQA基准上进行，包含29,270个问答对，覆盖8个中国主要城市。基线仅对比单智能体Standard（Supervisor单独处理所有任务），缺失通用DRA基线如ASearcher或ABSeeker。主实验显示，层级架构HIRE-Agent在平均准确率上比Standard高0.2024，F1高0.2021。Qwen3-30B A3B表现最佳（0.8260 Acc, 0.8294 F1），Qwen3-8B表现最差（0.6707 Acc, 0.6730 F1）。

| 模型 | 方法 | Type 1 Acc | Type 2 Acc | Type 3 Acc | Overall Acc |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Qwen2.5-72B | Standard | 0.8082 | 0.7110 | 0.3973 | 0.5855 |
| Qwen2.5-72B | HIRE-Agent | 0.8862 | 0.6581 | 0.6211 | 0.6989 |
| Qwen3-8B | Standard | 0.6878 | 0.5148 | 0.2657 | 0.4393 |
| Qwen3-8B | HIRE-Agent | 0.8188 | 0.7484 | 0.5489 | 0.6707 |
| Qwen3-30B A3B | Standard | 0.8206 | 0.6756 | 0.7270 | 0.7270 |
| Qwen3-30B A3B | HIRE-Agent | 0.8852 | 0.8796 | 0.8816 | 0.8816 |
| GLM4.5-Air | Standard | 0.9239 | 0.8839 | 0.8980 | 0.8980 |
| GLM4.5-Air | HIRE-Agent | 0.9239 | 0.8839 | 0.8980 | 0.8980 |

消融实验显示，引入SLU标签使Type 3问题平均准确率提升0.3614，验证了意图解析与执行解耦的必要性。Supervisor Agent的规划准确率对最终性能影响显著，Qwen3-30B A3B在Type 3问题上规划准确率达0.9199，而GLM4.5-Air仅为0.7741。Database Interaction Agent在Type 2和Type 3查询上pass@1达0.9593，但Type 1（Text-to-SQL）仅0.8955，表明复杂多表连接仍是瓶颈。

评估边界方面，API缓存机制确保基准可复现性，但掩盖了实时网络延迟对规划策略的影响。指标仅包含Acc与F1，缺乏过程指标如搜索效率与引用准确性。代码开源，但超参数与GPU配置未详细报告，可复现性受限。

## 关联研究分析

从问题动机看，ReCoQA与RETQA均引入SLU概念，但RETQA局限于静态数据库，而ReCoQA扩展至动态API场景。这一差异源于任务特性：房地产决策依赖实时地理信息，静态数据无法反映通勤时间与距离的动态变化。MACT虽展示复杂协作，但依赖Pandas导致内存瓶颈，ReCoQA用SQL/API替代，解决可扩展性问题。

从方法设计看，HIRE-Agent与ASearcher代表不同路线：前者侧重架构分解，后者依赖端到端RL。HIRE-Agent的层级设计在开放式报告生成中可能更具优势，因为显式规划有助于结构完整性；而ASearcher在通用基准上表现更优，因为RL能直接优化最终结果。ReCoQA使用BERT微调SLU而非纯LLM，偏离“纯LLM驱动”共识，这一混合模型设计是否违背DRA的端到端自主性定义，论文未给出回答。

## 总结

本文要解决的核心矛盾是垂直领域中结构化查询与动态API调用的严格依赖关系评估缺失。现有方法将二者视为孤立能力，无法评估混合工作流；本文凭借ReCoQA基准与HIRE-Agent框架，通过层级解耦架构验证了协作必要性。实验证明层级架构比单智能体Acc高0.2024，Qwen3-30B A3B在Type 3问题上Acc达0.8816。其边界在于API缓存掩盖实时延迟影响，且缺乏通用DRA基线对照。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_3847a457cf5c)