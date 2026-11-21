# ICLR2026最新论文 ｜ACTIONS SPEAK LOUDER THAN PROMPTS: A LARGE SCALE STUDY OF LLMS FOR GRAPH INFERENCE ｜代码生成优于提示：LLM图推理交互模式的大规模实证研究

研究机构：英国牛津大学、微软研究院

作者：Ben Finkelshtein、Silviu Cucerzan、Sujay Kumar Jauhar 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_52109733)

> 文本属性图（TAGs）节点分类任务中，大语言模型（LLMs）缺乏原生图结构感知能力，传统序列化提示（Prompting）在长文本或高密度图上因Token预算耗尽而失效。现有ReAct工具调用范式受限于固定动作集，无法灵活组合结构查询。本文提出Graph-as-Code交互模式，允许LLM生成并执行Python代码直接操作图数据表，实现结构、特征与标签的按需组合访问。该范式在长文本与高异质图上显著优于提示与固定工具调用，但仅验证了静态图上的推理性能，未涉及训练过程或跨域泛化能力。

## 研究背景

当LLM处理引文网络或社交图谱时，节点文本长度与邻域规模常超出上下文窗口限制。这一瓶颈源于图数据的非欧几里得拓扑特性：节点间关系需通过边连接显式表达，而LLM仅能处理线性序列。为注入结构信息，早期方法将邻域序列化为文本提示，但高平均度（如ogbn-arxiv的13.64）或长文本（如wiki-cs的3215.56 tokens）导致Token预算迅速耗尽，迫使模型截断关键邻域信息。

LLM-GNN融合领域的主流路线分为外部投影与原生架构修改两类。外部投影方法（如GraphGPT）将图节点映射至LLM嵌入空间，但序列化过程造成信息损失；原生架构方法（如NAG）修改自注意力机制以强制拓扑依赖，但训练复杂度极高。这两类方法均假设LLM需深度参与图结构建模，却忽视了LLM作为代码生成器的潜力。本文切入点在于：不修改LLM架构或预训练参数，仅通过改变交互协议，让LLM生成代码动态查询图数据，从而在推理阶段实现结构感知的灵活性与效率。

## 核心方法

### 交互模式参照系

本文评估三种LLM-Graph交互模式：Prompting（单轮提示）、GraphTool（ReAct式固定工具调用）与Graph-as-Code（代码生成执行）。参照系为ReAct范式（Yao et al., 2023），其标准流程为“思考-行动-观察”循环，但行动空间受限于预定义工具集。本文的关键差异在于：Graph-as-Code将行动空间扩展为任意Python代码，允许LLM自主设计查询逻辑，而非从固定菜单中选择。

### Graph-as-Code机制

Graph-as-Code将图数据表示为类型化表格，包含节点ID、特征文本、邻居列表与标签列。LLM生成紧凑程序，执行后获取结果并继续推理，直至输出最终标签。该设计解决了固定工具调用在多跳查询中的步骤冗余问题：例如，获取2-hop邻域特征在GraphTool中需多次调用，而在Graph-as-Code中可单条代码完成。形式化地，设图 $G=(V, E, X, Y)$，LLM $\theta$ 生成代码 $c_t$，执行环境返回结果 $r_t = \text{Exec}(c_t, G)$，状态更新为 $s_{t+1} = \text{Concat}(s_t, r_t)$，直至 $\theta(s_T)$ 输出标签 $\hat{y} \in C$。此过程将多步工具序列压缩为单次查询，显著降低Token开销。

### 依赖解耦分析

为量化各模式对特征、结构与标签的依赖，本文引入2D热力图分析：独立截断文本特征、删除边或移除已知标签，观察准确率变化。该设计动机在于揭示Prompting的脆弱性根源——其性能高度依赖完整邻域上下文，而Graph-as-Code可通过代码选择性访问信息，避免Token溢出。例如，在Photo数据集（平均文本长度797.82，平均度10.36）上，2-hop Prompting因Token限制准确率骤降，而Graph-as-Code通过按需检索维持稳定性能。

## 实验评估

实验覆盖12个数据集，涵盖引文（Cora, PubMed, Arxiv）、电商（Products, Computers, Photo）、网页（Cornell, Texas, Washington, Wisconsin, Wiki-CS）与社交（Reddit, Instagram）领域，结构上区分同质性（Homophily > 50%）与异质性（Homophily < 20%）。基线包括Random、Majority Label与Label Propagation，但未对比GNN基线（如GCN/GAT）或训练式LLM-GNN方法（如TAG-DLM）。

| 数据集 | 类型 | Prompting (2-hop) | GraphTool+ | Graph-as-Code |
| :--- | :--- | :--- | :--- | :--- |
| Cora | 短文本同质 | 83.43±2.25 | 81.40±3.08 | **85.16**±1.47 |
| Arxiv | 短文本同质 | 70.00±5.82 | 78.50±3.43 | **82.70**±2.66 |
| Cornell | 长文本异质 | 84.17±1.43 | 91.13±2.97 | **92.70**±2.35 |
| Photo | 长文本同质 | TokenLimit | 81.30±0.97 | **86.40**±2.65 |
| Wiki-CS | 长文本同质 | TokenLimit | 80.50±3.10 | **82.20**±3.63 |

Graph-as-Code在所有数据集上均取得最高准确率，尤其在长文本或高平均度场景（如Arxiv、Photo）优势显著。在异质性数据集（如Cornell，Homophily 11.55%）上，所有LLM交互模式均优于Label Propagation，挑战了“LLM在低同质性图上失效”的既有假设。消融实验显示，当边完全删除但特征完整时，Graph-as-Code保持高准确率，而Prompting性能崩溃，证实代码生成对结构缺失的鲁棒性。

评估边界受限于Training-free设定，未报告计算效率指标（如推理时间、GPU内存），且未对比训练式方法。代码执行的安全性审计与幻觉风险控制未在实验中量化，仅定性描述为“透明可审计”。

## 关联研究分析

从问题动机看，本文与GraphGPT（Wu et al., 2023）形成鲜明对比。GraphGPT通过多阶段指令微调将图节点投影至LLM嵌入空间，属于“LLM-as-Predictor”范式，依赖训练过程对齐图结构与语言语义；本文则采用“LLM-as-Enhancer”思路，保持LLM参数冻结，仅通过交互协议优化推理效率。这一差异源于任务特性：GraphGPT针对静态图分类，需深度结构建模；本文聚焦长文本图，核心瓶颈是Token预算而非结构理解深度。

从方法设计看，本文的Graph-as-Code与NAG（Gong et al., 2026）代表两条截然不同的结构注入路径。NAG修改LLM自注意力机制以强制拓扑依赖，属于架构级原生融合；本文保持LLM架构不变，通过外部代码执行实现结构感知。NAG的优势在于结构保真度高，但训练复杂度高；本文的优势在于零训练成本与推理灵活性，但依赖LLM的代码生成能力。这种差异暗示：结构感知的实现路径并非唯一，架构修改与交互优化可能在不同场景下互补。

## 总结

本文核心矛盾在于LLM处理图数据时的Token预算限制与结构感知需求之间的冲突。切入点在于利用LLM的代码生成能力，将图查询从固定工具调用扩展为动态程序执行，从而在推理阶段实现信息的按需组合。方法上，Graph-as-Code通过生成Python代码操作图数据表，将多步查询压缩为单次执行。实验证明，该模式在Cora上达到85.16%准确率，在Photo上避免Token限制导致的性能崩溃。边界在于仅验证了静态图上的推理性能，未涉及训练过程、跨域泛化或计算效率量化。当图规模扩展至百万级节点时，代码生成的执行延迟与LLM推理成本是否成为新的瓶颈，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_52109733)