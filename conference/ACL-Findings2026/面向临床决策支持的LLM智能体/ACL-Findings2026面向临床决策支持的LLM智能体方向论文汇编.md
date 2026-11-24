# ACL-Findings2026 · 面向临床决策支持的LLM智能体方向论文汇编

> 本方向共 7 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Beyond the Individual: Virtualizing Multi-Disciplinary Reasoning for Clinical Intake via Collaborative Agents ｜虚拟多学科团队驱动的门诊初诊智能体

研究机构：浙江大学

作者：Huangwei Chen、Wu Li、Junhao Jia 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.08927)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.08927)

> 门诊初诊阶段，医生需在有限时间内将患者非结构化叙述转化为结构化SOAP笔记，单一视角易受锚定偏差影响导致证据遗漏。现有大语言模型（LLM）智能体多聚焦于静态诊断或通用多智能体辩论，缺乏对初诊信息收集过程的显式状态建模与动态专家调度机制。Aegle提出一种同步虚拟多学科团队（MDT）框架，通过结构化临床状态分离证据收集与诊断推理，并由元认知编排器按需激活专家代理进行解耦并行推理。该框架在ClinicalBench与RAPID-IPN数据集上显著提升了文档质量与诊断准确率，但其动态拓扑在极端信息缺失场景下的鲁棒性仍需验证。

】

---

【Compartmentalised Agentic Reasoning for Clinical NLI ｜临床自然语言推理的分室代理架构

研究机构：英国曼彻斯特大学、英国谢菲尔德大学

作者：Maël Jullien、Lei Xu、Marco Valentino 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.10222)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.10222)

> 临床自然语言推理（Clinical NLI, CTNLI）要求模型在前提与陈述间判定蕴含、矛盾或中立，但大语言模型（LLM）常因复用通用启发式而违反特定逻辑约束。现有思维链（Chain-of-Thought, CoT）提示无法区分因果、组合、认知与风险等异构推理模式，导致系统性错误。本文提出分室代理推理框架（Compartmentalised Agentic Reasoning for Clinical NLI, CARENLI），通过路由、求解、验证与修正四阶段流水线强制逻辑对齐。该方法在CTNLI基准上平均提升34%准确率，但组合推理场景仍近乎失效，其临床部署价值受限于静态文本边界。

】

---

【Dr. Assistant: Enhancing Clinical Diagnostic Inquiry via Structured Diagnostic Reasoning Data and Reinforcement Learning ｜临床诊断推理数据与强化学习驱动的问诊智能体

作者：Yue Guo、Fanfu Wang、Jianwei Lv 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.13690)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_802240fc05eb)

> 临床决策支持系统（CDSS）需辅助医生在信息缺失下通过多轮问诊缩小诊断假设空间，但传统规则引擎难以处理非结构化文本与动态交互。现有大语言模型（LLM）在静态问答中表现优异，却在动态问诊中缺乏专业诊断推理逻辑，导致询问方向偏离。本文提出临床诊断推理数据（CDRD）结构及两阶段训练策略，将指南逻辑结构化并作为强化学习（RL）约束。该方案在自建基准上验证了逻辑约束对问诊准确性的提升，但其单智能体架构在复杂共病场景下的泛化能力存疑。

】

---

【GraphDx: A Cost-Aware Knowledge-Enhanced Multi-Agent Framework for Sequential Diagnosis ｜基于成本感知知识图谱的多智能体诊断框架

作者：Shaoting Tan、Ning Liu、Yuntao Du 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f67819f3e03a)

> 临床顺序诊断要求智能体在信息缺失与资源约束下平衡准确率与成本，现有大语言模型（LLM）因缺乏显式领域模型常陷入“防御性医疗”式过度检查。本文指出LLM存在“知识-推理差距”，即虽具备医学知识却无法在成本约束下进行系统性假设检验。GraphDx通过自动化构建含定量属性的医学诊断知识图谱（MDKG），并设计感知、推理、决策三代理协作架构，将复杂推理卸载至符号引擎。该方法在MedQA与MIMIC-IV上将成功率提升至79%-93%并降低20%-54%成本，但其对图谱覆盖范围的依赖及小模型下的泛化边界仍需进一步验证。

】

---

【MDTeamGPT: Mitigating Context Collapse and Enabling Self-Evolution in Medical Multi-Agent Reasoning ｜医疗多智能体协作中的上下文崩塌与自进化机制

作者：Kai Chen、Xinfeng Li、Tianpei Yang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_11744cfa0b0d)

> 多智能体医疗会诊面临长程推理中的上下文崩塌与经验复用低效两大瓶颈。现有方法依赖全量历史传递或简单投票，导致信息稀释与错误累积，无法将诊断轨迹转化为可迁移策略。本文提出MDTeamGPT，通过Lead Physician结构化压缩与双知识库检索实现上下文稳定与自进化。该框架在静态问答基准上表现领先，但其有效性局限于文本推理场景，缺乏动态交互验证。

】

---

【SEMA-RAG: A Self-Evolving Multi-Agent Retrieval-Augmented Generation Framework for Medical Reasoning ｜自进化多智能体检索增强生成

研究机构：香港中文大学、武汉大学

作者：Yongfeng Huang、Ruiying Chen、James Cheng

论文原文见 [arXiv](https://arxiv.org/abs/2605.17101)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.17101)

> 医学问答中的检索增强生成（Retrieval-Augmented Generation, RAG）长期受限于单轮静态检索，无法匹配临床推理中“解释-探索-裁决”的多阶段特性，导致证据链断裂与幻觉。本文指出单链推理的认知过载是根本病因，提出SEMA-RAG框架，通过角色解耦与充分性驱动的自进化检索实现证据收敛。该框架在五个基准上平均提升最强基线6.46个百分点，验证了任务解耦的有效性，但其静态问答边界与推理成本仍制约向动态临床场景的迁移。

】

---

【TheraAgent: Self-Improving Therapeutic Agent for Precise and Comprehensive Treatment Planning ｜治疗规划智能体

研究机构：清华大学、新加坡国立大学

作者：Junkai Li、Yunghwei Lai、Tianyi Zhu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.05963)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.05963)

> 导读 临床治疗规划要求将诊断结论转化为具体、安全且完整的用药方案，但现有大语言模型（LLM）依赖单次生成，常导致剂量错误、覆盖不全或安全隐患。本文指出单次生成缺乏显式验证机制是核心瓶颈，提出 TheraAgent 框架，通过“生成-反思-精炼”的迭代闭环与临床对齐的 TheraJudge 评估模块实现自我纠错。该框架在 HealthBench 治疗子集上取得 48.94 分，并在专家盲评中以 86% 胜率超越人类医生，但其高计算成本与对骨干模型推理能力的依赖仍存疑。

】
