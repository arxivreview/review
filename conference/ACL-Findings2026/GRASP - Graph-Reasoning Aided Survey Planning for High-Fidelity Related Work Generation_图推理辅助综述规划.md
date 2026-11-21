# ACL-Findings2026最新论文 ｜GRASP: Graph-Reasoning Aided Survey Planning for High-Fidelity Related Work Generation ｜图推理辅助综述规划

作者：Haoming Li、Jessica Ouyang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d0e072d0ec69)

> 导读 自动综述生成面临的核心挑战在于，当引用文献数量超过模型上下文窗口时，LLM难以维持跨文档的逻辑一致性并准确捕捉论文间的论证关系。现有方法多依赖线性大纲或简单的引用网络特征，导致生成的相关工作部分（Related Work Section, RWS）往往沦为孤立摘要的堆砌，缺乏对研究脉络的深度整合。GRASP提出了一种双层图结构框架，结合思维图（Graph of Thoughts, GoT）与论证-反论证规划网络（Argument-Counterargument Planning Network, ACPN），并通过Steiner树剪枝保留核心语义骨架。该框架在OARelatedWork数据集上显著提升了引用意图与话语角色的保真度，但其对稀疏引用领域的泛化能力及计算开销仍存疑。

## 研究背景

理解本文需把握两个关键概念：思维图（GoT）与论证-反论证规划网络（ACPN）。GoT将LLM的线性思维链转化为图结构，节点代表局部推理步骤，边代表逻辑依赖，旨在解决长文本生成中宏观结构松散的问题。然而，GoT仅捕捉细粒度的语义相似性，无法显式建模论文间的支持、对比等全局论证关系。ACPN则通过提取论文核心主张，构建论文级的有向图，边标签为{support, contrast, neutral}，从而显式表征研究景观中的论证动态。

学术出版量的指数级增长使得人工撰写RWS耗时且难以保持时效性。早期自动综述生成方法如AutoSurvey采用模块化流水线，虽解决了长上下文信息丢失，但牺牲了全局逻辑一致性；Liu et al. (2025) 提出的Select, Read, Write (SRW) 框架利用引用网络引导多智能体阅读，但受限于引用网络的稀疏性，仅能捕捉共引关系，无法处理未直接引用的论文间隐含联系。Li and Ouyang (2025) 虽利用引用网络提取特征，但仅将其作为间接编码输入，未直接引导生成过程。GRASP的切入点在于，将图结构从“特征载体”转变为“生成蓝图”，通过显式的拓扑剪枝，确保LLM在生成时严格遵循论文间的核心论证路径。

## 核心方法

### 方法参照系

本文问题属于自动综述生成中的“规划引导生成”路线。与AutoSurvey等分层范式不同，GRASP不依赖线性大纲，而是构建双层图结构：底层GoT捕捉细粒度语义节点，顶层ACPN捕捉论文级论证关系。关键差异在于，GRASP在生成前引入基于Steiner树的拓扑感知剪枝，过滤冗余节点，使LLM仅基于核心语义骨架进行写作。

### 双层图构建与共识节点融合

GoT层通过Chain-of-Thought提示提取每篇论文的局部推理节点，并合并语义重叠节点为“共识节点”。ACPN层提取论文核心主张，分类论文对关系。设计动机在于解决GoT无法显式建模全局论证关系、ACPN缺乏细粒度内容支撑的失效。共识节点融合公式为：

$$ C_{ij} = \text{Merge}(n_i, n_j) \quad \text{if} \quad \text{Sim}(n_i, n_j) > \tau $$

其中 $n_i, n_j$ 为来自不同论文的GoT节点，$\text{Sim}$ 为语义相似度，$\tau$ 为阈值。该机制将分散的局部推理整合为跨论文的共享论点，为后续剪枝提供关键终端节点。

### 拓扑感知剪枝与结构化生成

剪枝步骤将GoT子图 $G_i=(V_i, E_i)$ 转化为Steiner树，保留连接共识节点与高介数中心性节点的最小权重子图。设计动机在于原始GoT包含大量论文特有的细枝末节，直接输入LLM会导致生成内容冗长且偏离核心关系。Steiner树近似算法为：

$$ T^* \approx \text{MST}(\text{MetricClosure}(S)) $$

其中 $S$ 为终端节点集（共识节点+Top 20%高介数节点），$\text{MetricClosure}$ 构建终端间最短路径距离图。剪枝后的图以JSON格式序列化，结合ACPN关系标签，作为Writer模块的结构化输入。Writer采用三阶段策略：全面草稿、语义压缩、最终合并，确保信息覆盖与语言简洁的平衡。

## 实验评估

实验基于OARelatedWork数据集的1,350篇论文子集，基线包括SRW、L&O、Direct（GPT-5-mini直出）及No-graph（消融）。GRASP (pruned) 在ROUGE-1 F1 (0.771) 和BERTScore Macro (0.778) 上优于No-graph (0.747/0.764) 和L&O (0.664/0.817)，表明图结构对语义对齐有正向贡献。

| 模型 | ROUGE-1 F1 | BERTScore Macro | Citation Intent F1 |
|---|---|---|---|
| L&O | 0.664 | 0.817 | 0.731 |
| No-graph | 0.747 | 0.764 | 0.743 |
| GRASP (pruned) | 0.771 | 0.778 | 0.769 |

消融实验显示，剪枝步骤显著提升了引用意图保真度，尤其在“Differences”和“Extends”类别上，验证了ACPN显式建模论证关系的有效性。No-graph基线虽保留所有信息，但因缺乏结构引导，生成内容冗长且偏离核心关系。

评估边界方面，指标侧重引用微观结构（意图、话语角色），缺乏对长文本逻辑连贯性的深度量化。代码已开源，但实验未报告计算开销，Steiner树剪枝的实时性存疑。

## 关联研究分析

从方法设计看，GRASP与SurveyG均使用图结构，但SurveyG依赖层级引用图捕捉全局拓扑，GRASP依赖GoT+ACPN捕捉细粒度论证关系。SurveyG的图构建耗时且依赖引用网络质量，对稀疏领域效果有限；GRASP通过共识节点融合缓解稀疏性，但依赖LLM提取主张的准确性。从问题动机看，GRASP与AutoSurvey同属结构化生成，但AutoSurvey侧重模块化执行，GRASP侧重图拓扑剪枝。AutoSurvey的全局一致性不足源于缺乏显式关系建模，GRASP通过Steiner树剪枝保留核心骨架，但可能丢失非终端节点的边缘信息。

## 总结

GRASP旨在解决LLM在长文档生成中跨文档关系捕捉不足的问题，通过双层图结构与Steiner树剪枝，将图结构从特征载体转变为生成蓝图。实验证明其在引用意图与话语角色保真度上优于基线，ROUGE-1 F1达0.771。然而，其依赖LLM提取主张的准确性，且未报告计算开销，Steiner树剪枝在大规模文献集上的实时性未验证。当引用网络极度稀疏时，共识节点融合是否仍能捕捉有效关系，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_d0e072d0ec69)