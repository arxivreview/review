# ACL-Findings2026最新论文 ｜MDTeamGPT: Mitigating Context Collapse and Enabling Self-Evolution in Medical Multi-Agent Reasoning ｜医疗多智能体协作中的上下文崩塌与自进化机制

作者：Kai Chen、Xinfeng Li、Tianpei Yang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_11744cfa0b0d)

> 多智能体医疗会诊面临长程推理中的上下文崩塌与经验复用低效两大瓶颈。现有方法依赖全量历史传递或简单投票，导致信息稀释与错误累积，无法将诊断轨迹转化为可迁移策略。本文提出MDTeamGPT，通过Lead Physician结构化压缩与双知识库检索实现上下文稳定与自进化。该框架在静态问答基准上表现领先，但其有效性局限于文本推理场景，缺乏动态交互验证。

## 研究背景

多智能体医疗会诊模拟多学科团队（MDT）协作，通过角色分工与迭代讨论提升复杂病例诊断准确性。然而，随着交互轮次增加，轨迹token迅速累积，迫使系统压缩历史上下文。这一过程常导致粗粒度摘要，丢失细粒度患者信息与关键证据，引发上下文崩塌（Context Collapse），进而 destabilize 推理效率与准确性。同时，现有系统通常仅归档原始诊断历史，缺乏对成功轨迹的结构化蒸馏或对错误案例的深度反思，限制了系统从数据中提炼可迁移策略的能力，阻碍了自进化与泛化。

现有研究如MedAgents（Tang et al., 2023）与SeM-Agents（Chen et al., 2025）虽确立了多智能体协作范式，但前者依赖简单共识投票，易陷入“共识陷阱”；后者虽引入经验积累，却忽视上下文维护策略，无法应对长程交互中的信息稀释。本文切入点在于解决长程推理中的状态一致性与经验演化效率问题，通过引入上下文工程机制与结构化记忆模块，将静态辩论转化为动态、可自进化的诊断流程。

## 核心方法

### 方法参照系

标准多智能体医疗会诊流程包含专家选择、多轮讨论与共识形成。通常做法是将全量历史对话直接传递给后续轮次的专家，或通过简单投票聚合观点。本文问题与该通用流程的关键差异在于：全量传递导致上下文窗口过载与崩塌，简单投票无法整合冲突证据，且缺乏对历史经验的结构化利用。

### Lead Physician与Residual Context机制

针对上下文崩塌问题，本文在每轮讨论后引入Lead Physician角色，执行代理式上下文工程。该机制将专家输出结构化为六个维度：一致性（Consistency）、冲突（Conflict）、独立性（Independence）、整合（Integration）、工具使用（Tools Usage）与长期记忆（Long-Term Memory）。随后，系统采用Residual Context架构，仅保留最近两轮的压缩摘要供后续专家参考，而非全量历史。

$$
S_{i+2} = \text{LLM}_{\text{Specialist}}(C, Q, S^6_i, S^6_{i+1})
$$

其中 $S^6_i$ 表示第 $i$ 轮经Lead Physician处理后的六维结构化摘要。该公式表明，第 $i+2$ 轮专家仅基于最近两轮的结构化信息更新其立场，通过滑动窗口限制记忆深度，防止早期噪声干扰当前推理，从而维持token消耗稳定在约10,000以内，避免崩塌。

### 双知识库驱动的自进化

针对经验复用低效问题，本文构建CorrectKB与ChainKB双知识库。CorrectKB存储正确案例的JSON记录，包含问题、答案及最终轮结构化摘要；ChainKB存储错误案例的反思摘要，包含初始假设、分析过程、最终结论及错误原因反思。新案例到来时，系统通过余弦相似度检索Top-K（K=5）相似案例，增强专家提示。

$$
\text{Retrieval}(Q, C) = \text{TopK}(\{v \in \text{CorrectKB} \cup \text{ChainKB} \mid \cos(v, Q) > \tau\}, K=5)
$$

该机制将原始历史归档升级为可迁移策略蒸馏。正确案例提供正向推理范式，错误案例提供避坑指南，两者共同增强专家在相似场景下的推理鲁棒性，实现从数据到策略的转化。

## 实验评估

实验在MedQA与PubMedQA上进行，使用gpt-4-turbo作为骨干模型，对比MedAgents、SeM-Agents等基线。基线覆盖多智能体协作路线，但缺乏单智能体RAG强基线（如SEMA-RAG）的对比，可能高估多智能体架构的相对优势。

| 方法 | MedQA Acc (%) | PubMedQA Acc (%) | Average Acc (%) |
| :--- | :--- | :--- | :--- |
| Single-Agent | 77.4 ± 1.8 | 75.3 ± 2.0 | 76.4 |
| MedAgents | 83.9 ± 1.1 | 77.2 ± 1.4 | 80.6 |
| SeM-Agents | 89.2 ± 0.8 | 83.1 ± 1.1 | 86.2 |
| MDTeamGPT | 90.9 ± 0.6 | 84.4 ± 0.8 | 87.7 |

MDTeamGPT在MedQA上达到90.9%，超越SeM-Agents 1.7个百分点，表明结构化上下文工程与双知识库机制的有效性。

消融实验显示，单独使用Residual Context或Lead Physician提升有限，但两者结合后性能显著跃升。例如，仅启用Residual Context时MedQA准确率为76.9%，仅启用Lead Physician时为78.2%，而两者结合后达到84.3%。进一步加入CorrectKB后提升至88.9%，加入ChainKB后达到90.9%。这表明上下文稳定是经验复用的前提，而双知识库的协同作用最大化了自进化效果。

评估边界方面，实验仅覆盖静态文本问答，未验证动态交互场景（如EHR工具调用）。指标仅报告准确率与F1，缺乏推理步骤质量或安全性评估。代码已开源，但超参数（如K=5）的敏感性分析仅在附录中简要提及，主文未详细讨论。

## 关联研究分析

从问题动机看，本文与SeM-Agents（Chen et al., 2025）均关注经验积累，但SeM-Agents仅存储正确经验，且未解决上下文崩塌问题。本文通过ChainKB引入错误反思，并通过Residual Context解决长程推理稳定性，根源在于SeM-Agents假设上下文窗口足够大，而本文直面长程交互中的资源限制。从方法设计看，本文与Reflexion（Shinn et al., 2023）均利用反思机制，但Reflexion针对单智能体规划，本文将其扩展至多智能体协作，并通过Lead Physician结构化整合冲突观点，解决了单智能体反思无法处理多视角分歧的问题。

## 总结

MDTeamGPT旨在解决多智能体医疗会诊中的上下文崩塌与经验复用低效矛盾。现有方法因全量历史传递与简单归档无法应对长程推理，本文通过Lead Physician结构化压缩与双知识库检索实现上下文稳定与自进化。实验证明其在MedQA上达到90.9%准确率，超越基线。然而，其有效性局限于静态文本场景，缺乏动态交互验证。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_11744cfa0b0d)