# ACL-Findings2026最新论文 ｜What Factors Affect LLMs and RLLMs in Financial Question Answering? ｜金融问答中推理大语言模型性能瓶颈的系统性归因

研究机构：安徽大学、华中科技大学

作者：Peng Wang、Xuesi Hu、Jiageng Wu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2507.08339)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7c95ec277c91)

> 金融问答任务要求模型在复杂语境下执行多步数值推理，传统大语言模型（LLM）常因推理链过短导致计算错误。现有提示工程与智能体框架虽能提升LLM表现，但对已具备长思维链能力的推理大语言模型（RLLM）增益有限，且多语言对齐策略在RLLM上甚至产生负迁移。本文通过控制变量实验，系统解构提示方法、智能体框架与多语言对齐对LLM/RLLM性能的影响机制，揭示长思维链是区分两类模型性能瓶颈的核心变量。该研究厘清了推理时策略的适用边界，但未能验证训练式微调能否替代推理时策略解决数值幻觉问题。

## 研究背景

金融问答涉及输入问题 $Q$、选项集 $O$ 及上下文 $C$，输出答案 $A$。对于选择题，模型需执行 $A_{choice} = \text{Model}_{choice}(Q, O, C)$；对于开放题，则执行 $A_{open} = \text{Model}_{open}(Q, C)$。这一形式化定义揭示了任务对模型语义理解与数值计算的双重依赖。当模型面对非结构化金融文本时，若缺乏深层逻辑探索，极易陷入表面语义匹配而忽略底层数值关系，导致推理错误。

金融领域长期依赖基于统计的量化模型，但难以处理非结构化信息且缺乏可解释性。随着LLM在自然语言处理上的突破，研究重心从信号提取转向自主决策，但回测中普遍存在的前视偏差与记忆污染问题，暴露了概率生成机制与金融审计确定性要求之间的冲突。现有方法多聚焦于提升LLM在金融领域的特定性能，却未系统探究影响其问答能力的根本因素。本文切入点在于区分LLM与RLLM在推理时策略下的表现差异，揭示长思维链（Long CoT）作为性能瓶颈的关键作用。

## 核心方法

### 方法参照系

本文问题属于金融问答中的推理时优化范畴，与通用提示工程流程一致，但关键差异在于引入了RLLM作为对照组，以隔离长思维链对推理时策略有效性的影响。

### 提示与智能体框架的模拟长思维链机制

提示方法通过修改思维提示词引导模型生成更长推理过程。零样本思维链（Zero-shot CoT）使用“let’s think step by step”刺激推理，而计划与求解（Plan-and-Solve）通过“Let’s first understand the problem and devise a plan... Then, let’s carry out the plan...”的两步分解提升推理质量。智能体框架如Self-Refine通过同一LLM迭代反馈优化答案，S3 Agent则通过表层表达、语义信息与情感表达三个智能体协作解锁模型潜力。这些方法本质上模拟长思维链，其性能增益可表示为：

$$
\Delta P_{LLM} = f(L_{CoT}, P_{prompt})
$$

其中 $L_{CoT}$ 为推理链长度，$P_{prompt}$ 为提示策略。设计动机在于解决LLM因推理链过短导致的计算错误，通过延长推理过程提升数值精确性。

### 多语言对齐的推理长度扩展机制

多语言对齐方法通过显式提示或翻译提升LLM在非英语任务上的表现。翻译至英语（Translate-en）将本地语言问题与上下文转换为英语，防止因多语言能力不足导致的性能下降。跨语言提示（CLP）通过两阶段对齐：(1) 跨语言对齐提示，(2) 任务特定求解提示，增强推理能力。其性能增益可表示为：

$$
\Delta P_{ML} = g(L_{CoT}, C_{lang})
$$

其中 $C_{lang}$ 为语言复杂度。设计动机在于解决LLM在训练语料中非英语比例低导致的性能偏差，通过延长推理长度弥补多语言能力不足。

## 实验评估

实验基于FAMMA基准的Basic Txt数据集（1,945条），涵盖英语、中文和法语。基线覆盖Direct、Zero-shot CoT、Plan-and-Solve、Self-Refine、S3 Agent、Translate-en和CLP，但缺失神经符号验证（如VERAFI）和RAG基线。主实验结果显示，O4-mini在Direct方法下取得65.29% Overall Acc，显著高于DeepSeek-V3的58.86%。

| 模型 | 方法 | Overall Acc (%) |
| --- | --- | --- |
| O4-mini | Direct | 65.29 |
| DeepSeek-V3 | Direct | 58.86 |
| Qwen-3-14B | Direct | 56.76 |
| GPT-OSS-20B | Direct | 53.57 |

消融实验揭示，Plan-and-Solve在LLM上表现最优，但在RLLM上性能下降。例如，DeepSeek-R1-Distill-Qwen-32B在Plan-and-Solve下Overall Acc为53.26%，低于Direct的53.41%。多语言对齐中，CLP对LLM增益显著（如Meta-Llama-3.1-8B-Instruct从16.22%提升至21.69%），但对RLLM无效（DeepSeek-R1-Distill-Qwen-32B从48.67%降至47.97%）。

评估边界方面，指标仅采用Overall Acc，未区分算术与非算术任务；评估协议为单次运行，未报告置信区间；代码已开源，但超参数与GPU配置未详细披露。

## 关联研究分析

从问题动机看，本文聚焦推理时策略对LLM/RLLM性能的影响，而VERAFI（Akinfaderin and Subramanian, 2025）通过神经符号策略生成实现验证性智能金融智能，其94.70% Factual Correctness远高于本文最高65.29% Overall Acc。差异根源在于任务特性：VERAFI针对静态数值推理，强调合规性与精确性；本文针对动态多语言问答，强调推理链长度与多语言对齐。本文未测试神经符号方法，是否遗漏了关键对比？

从方法设计看，本文采用纯推理时策略，而Trading-R1（Xiao et al., 2025）结合强化学习对齐交易行为，其7.42% CR优于GPT-4.1的3.15%。差异根源在于技术路线：本文依赖模型内部知识，Trading-R1通过奖励机制优化交易决策。本文未使用RL，仅用推理时策略，代表不同技术路线。推理时策略能否替代训练式微调以解决数值幻觉，论文未给出回答。

## 总结

本文要解决的核心矛盾是LLM与RLLM在金融问答中性能瓶颈的差异归因。现有方法未系统区分两类模型在推理时策略下的表现，本文通过控制变量实验揭示长思维链是关键变量。本文做了什么：系统评估提示方法、智能体框架与多语言对齐对LLM/RLLM的影响。证明了什么：O4-mini Direct取得65.29% Overall Acc，Plan-and-Solve在RLLM上性能下降。本文的边界在于未验证训练式微调能否替代推理时策略解决数值幻觉。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_7c95ec277c91)