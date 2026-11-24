# ACL-Findings2026最新论文 ｜Momoka-RAG: MCTS-Organized Mapping of Knowledge Associations for Long-Document Retrieval Augmented Generation ｜Momoka-RAG：基于蒙特卡洛树搜索的长文档检索增强生成

研究机构：华南理工大学

作者：Wenyu Tao、Xiaofen Xing、Zeliang Li 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3baf3e966179)

> 长文档检索增强生成（Retrieval-Augmented Generation, RAG）旨在解决大语言模型（LLM）在处理超长文本时因上下文窗口限制与噪声干扰导致的事实幻觉问题。现有主流框架如RAPTOR与GraphRAG依赖固定规则或统计特征构建知识结构，仅能捕捉表层关联，无法挖掘跨段落的深层语义依赖。Momoka-RAG将蒙特卡洛树搜索（MCTS）从检索阶段迁移至索引阶段，以语义补全为目标主动探索Chunk间的最优信息路径，并在检索时通过混合粒度扩展与重排序获取精准上下文。该框架在长文档任务上实现了精度与召回率的平衡，但其预计算路径机制牺牲了对特定查询的动态适应性，且未验证跨文档场景下的有效性。

## 研究背景

长文档RAG的核心困境在于固定长度分块（Chunking）破坏了文本的逻辑连贯性。当文档被切分为独立片段时，指代消解所需的上下文丢失，导致检索模型难以定位跨段落的信息依赖。为解决此问题，研究界引入了结构化知识组织策略，试图在Chunk间建立显式或隐式连接。

主流方案分为两类：一类以RAPTOR为代表，采用高斯混合模型对Chunk进行自底向上的聚类并生成摘要，构建层级树结构；另一类以GraphRAG为代表，利用LLM提取实体与关系构建全局知识图谱。然而，这两种方法均陷入“机械”与“被动”的局限：RAPTOR基于向量相似度进行无差别聚类，忽视了Chunk在逻辑链中的不同角色；GraphRAG在固定窗口内进行无差别的实体抽取，缺乏由解题目标驱动的主动扩展。它们依赖统计特征（如向量距离、实体共现）生成关联，仅能捕捉表层联系，难以发现深层的因果或推理线索。Momoka-RAG的切入点在于，将MCTS引入索引阶段，以“语义补全”为奖励信号，主动探索Chunk间的深层语义路径，从而在静态预计算中保留动态推理的深度。

## 核心方法

### 方法参照系

标准RAG流程包含分块、嵌入、检索与生成四个阶段。本文问题与通用流程的关键差异在于：传统方法在检索时仅基于静态向量相似度匹配，而Momoka-RAG在索引阶段即通过搜索算法预构建Chunk间的语义关联路径，将“动态规划”转化为“静态预计算”，以平衡实时性与语义深度。

### Momoka-Map：基于MCTS的语义路径构建

Momoka-Map将每个LLM分块的Chunk视为节点，利用MCTS探索其语义补全路径。设计动机在于解决RAPTOR等基于固定规则聚类无法捕捉逻辑链的问题。选择阶段采用上置信界（UCT）公式平衡探索与利用：

$$ UCT(i) = \frac{R_i}{N_i} + C \sqrt{\frac{\ln N_p}{N_i}} $$

其中 $R_i$ 为节点 $i$ 的累计奖励，$N_i$ 为访问次数，$N_p$ 为父节点访问次数，$C$ 为探索常数。扩展阶段随机选择未探索节点作为子节点，防止循环路径。模拟阶段引入LLM作为“语义裁判”，对当前路径上下文与新Chunk的逻辑延续性进行二元判断，并计算奖励：

$$ r = I_{LLM}(c_i, c_{new}) + \alpha \cdot |p_i - p_{new}| + \beta \cdot |s_i - s_{new}| + \gamma + \delta $$

该公式确保奖励 $r$ 同时捕捉深层语义关联（$I_{LLM}$）与文档结构逻辑（段落/句子位置差），使MCTS能发现非相邻但逻辑连贯的Chunk组合。

### Momoka-Trail Retriever：混合粒度扩展与重排序

基于Momoka-Map预计算的路径模型，Momoka-Trail Retriever执行“检索-扩展-重排”流水线。设计动机在于解决静态检索候选池语义贫乏的问题。首先，通过向量相似度检索初始 $2 \times k$ 个Chunk；随后，执行混合粒度扩展策略，保留原始Chunk、拼接完整路径形成全局上下文，并纳入路径中单个节点及“原始Chunk+节点”的成对组合，以捕捉宏观叙事与微观实体关联；最后，采用交叉编码器（Cross-Encoder）重排序器替代LLM进行细粒度评分，避免LLM在长输入下的“迷失在中间”现象与高延迟，从而从富语义候选池中筛选最精准上下文。

## 实验评估

实验在Dragonball、SQUAD、NFCORPUS、SCI-DOCS、HotpotQA和TriviaQA六个数据集上进行，对比基线包括LightRAG、RAPTOR、Meta-Chunking-PPL/MSP、Dense X Retrieval和Late-Chunking。基线覆盖了聚类、图谱、命题分解与长上下文嵌入等主流路线，但未包含KBQA专用的智能体框架（如ToG），因任务对象为文本而非结构化知识图谱。

| 数据集 | 方法 | ROUGE-L | BLEU-1 | BLEU-2 | BLEU-3 | BLEU-4 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Dragonball | LightRAG | 0.2315 | 0.1651 | 0.1101 | 0.0794 | 0.0601 |
| Dragonball | PPL | 0.3313 | 0.1425 | 0.1048 | 0.0802 | 0.0630 |
| Dragonball | PPL (+Momoka-RAG) | 0.3053 | 0.1892 | 0.1436 | 0.1124 | 0.0896 |
| Dragonball | RAPTOR | 0.2751 | 0.1925 | 0.1334 | 0.0995 | 0.0773 |
| TriviaQA | LightRAG | 0.0132 | 0.0214 | 0.0191 | 0.0184 | 0.0183 |
| TriviaQA | PPL | 0.0181 | 0.1018 | 0.1221 | 0.1332 | 0.1393 |
| TriviaQA | PPL (+Momoka-RAG) | 0.0133 | 0.0219 | 0.0197 | 0.0192 | 0.0191 |
| SQUAD | LightRAG | 0.1075 | 0.0576 | 0.0477 | 0.0402 | 0.0355 |
| SQUAD | LLM-Chunk (+Momoka-RAG) | 0.1061 | 0.0630 | 0.0542 | 0.0475 | 0.0429 |

在Dragonball上，PPL (+Momoka-RAG)的BLEU-1至BLEU-4均显著高于LightRAG与RAPTOR，但ROUGE-L低于PPL基线（0.3053 vs 0.3313），表明MCTS路径扩展提升了局部词匹配精度，但可能牺牲了整体摘要的流畅性。在TriviaQA上，Momoka-RAG的ROUGE-L（0.0133）低于PPL基线（0.0181），显示在事实密度极高的问答任务中，路径扩展可能引入噪声。

消融实验显示，在Dragonball上，从Base到MM（仅Momoka-Map）再到Momoka（完整框架），Recall从31.62提升至36.14再降至35.60，Precision从59.71提升至91.89再升至121.60。这表明Momoka-Map通过注入全局标题显著降低了误报率，而Momoka-Trail Retriever的路径扩展在叙事性数据上进一步提升了证据完整性，但在NFCORPUS等知识点高度独立的数据集上，强制建立MCTS路径可能连接无关概念，导致Recall下降（277.64至272.94），呈现负迁移效应。

评估边界方面，论文未报告置信区间，且MCTS迭代次数（100）与Rollout长度（5）的敏感性分析显示，在浅层模拟下增加迭代次数带来Recall的质变，但深层模拟下性能呈非单调变化，暗示搜索树规模与模拟深度存在兼容性区间。代码未公开，超参数（$\alpha=3, \beta=2$）固定，限制了可复现性。

## 关联研究分析

从问题动机看，Momoka-RAG与GraphRAG均旨在解决长文档中Chunk间语义断裂问题，但根源差异显著。GraphRAG依赖实体共现构建显式知识图谱，其局限在于实体抽取的局部性与表面性，无法捕捉无实体支撑的因果或推理线索；Momoka-RAG则通过MCTS的奖励机制（LLM语义判断+结构先验）隐式构建路径，其优势在于以“语义补全”为目标驱动探索，能发现非相邻Chunk间的深层逻辑。然而，Momoka-RAG的路径是预计算的，不随查询变化，而GraphRAG的图谱虽静态，但检索时可基于查询动态遍历子图。这种“预计算深度”与“动态适应性”的取舍，是两者在长文档场景下的核心分歧。

从方法设计看，Momoka-RAG与MCTS-RAG（Hu et al., 2025）均使用MCTS，但应用阶段截然不同。MCTS-RAG将检索步骤视为节点，在推理时动态优化检索路径，实时性强但延迟高；Momoka-RAG将Chunk视为节点，在索引时预计算路径，检索时仅做静态匹配，牺牲了查询特异性以换取效率。这一设计选择源于长文档RAG对实时性的严苛要求，但也暴露了其在查询高度特异性场景下的潜在失效：当用户查询涉及文档中罕见的逻辑分支时，预计算路径可能未覆盖该分支，导致检索失败。

## 总结

Momoka-RAG旨在解决长文档RAG中固定分块导致的跨段落语义断裂问题，其切入点是现有框架（如RAPTOR、GraphRAG）依赖固定规则与统计特征，仅能捕捉表层关联，无法主动挖掘深层语义依赖。通过将在索引阶段应用MCTS构建语义补全路径，并在检索时执行混合粒度扩展与重排序，该框架在Dragonball上实现了BLEU-1 0.1892、BLEU-4 0.0896的性能，显著优于LightRAG与RAPTOR。然而，实验暴露了其边界：在TriviaQA等高事实密度任务上，ROUGE-L低于基线，且在NFCORPUS上出现Recall负迁移，表明预计算路径在知识点高度独立或查询高度特异性的场景中可能引入噪声或遗漏关键分支。当用户查询涉及文档中未预计算的罕见逻辑分支时，Momoka-RAG的检索性能是否必然劣于动态检索框架，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_3baf3e966179)