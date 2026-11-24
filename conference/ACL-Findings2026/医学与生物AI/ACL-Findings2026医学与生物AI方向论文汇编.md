# ACL-Findings2026 · 医学与生物AI方向论文汇编

> 本方向共 40 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Behavior-Aware Item Modeling via Dynamic Procedural Solution Representations for Knowledge Tracing ｜行为感知题目建模

研究机构：瑞士苏黎世联邦理工学院

作者：Jun Seo、Sangwon Ryu、Heejin Do 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.08260)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.08260)

> 知识追踪（KT）旨在通过历史交互预测学生未来表现，但现有方法多将题目视为静态向量，忽略了求解过程中的动态认知需求。本文指出，静态嵌入无法区分同一知识点下不同解题阶段的难度差异，导致模型在重复作答时缺乏适应性。BAIM 利用推理语言模型（RLM）离线提取题目在Polya四阶段解题过程中的嵌入轨迹，并通过上下文条件路由机制动态选择关键阶段。该框架在XES3G5M数据集上实现了83.21 AUC，显著优于预训练基线，但其依赖离线RLM推理的假设是否适用于实时交互场景仍存疑。

】

---

【Benchmarking LLMs on Authentic Cases from Medical Journals ｜临床诊断推理基准

研究机构：电子科技大学、香港中文大学

作者：Wanlong Liu、Junying Chen、Yunjin Yang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9a3f076a4085)

> 临床AI评估长期受困于基准饱和与场景失真，现有考试题导向的基准无法区分模型在复杂真实病例中的推理能力。本文切入点在于将权威医学期刊中的真实病例转化为高难度多选题，强制模型整合长上下文证据而非依赖参数化知识。通过构建覆盖11个专科、含多模态版本的ClinBench，并引入人类专家对照，量化了LLM与专家在专科深度与广度上的能力边界。该基准有效揭示了当前SOTA模型在真实临床场景下的性能瓶颈，但其选择题格式是否掩盖了开放式诊断推理的真实缺陷，仍存疑。

】

---

【Beyond Benchmarks: A Capability-Based Maturity Model for Systematic AI Integration in Hospitals ｜医院AI成熟度模型

作者：Rui Li、Xiaofen WU、Mingqian Liu 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_346f6758424c)

> 医疗大语言模型在标准化考试中的高分与真实临床工作流中的低效之间存在显著断层，现有评估体系仅聚焦于知识召回与单步推理，忽视了医院系统治理、合规约束及多轮交互能力。本文切入点在于将评估维度从模型内部推理扩展至医院系统级成熟度，提出分层能力模型。通过构建L0-L4真实临床场景基准并对比开源模型，验证了学术分数与临床效用的非线性关系。该框架为医院AI部署提供了系统性路径，但其对高阶治理任务的评估标准泛化性仍存疑。

】

---

【Beyond the Individual: Virtualizing Multi-Disciplinary Reasoning for Clinical Intake via Collaborative Agents ｜虚拟多学科团队驱动的门诊初诊智能体

研究机构：浙江大学

作者：Huangwei Chen、Wu Li、Junhao Jia 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.08927)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.08927)

> 门诊初诊阶段，医生需在有限时间内将患者非结构化叙述转化为结构化SOAP笔记，单一视角易受锚定偏差影响导致证据遗漏。现有大语言模型（LLM）智能体多聚焦于静态诊断或通用多智能体辩论，缺乏对初诊信息收集过程的显式状态建模与动态专家调度机制。Aegle提出一种同步虚拟多学科团队（MDT）框架，通过结构化临床状态分离证据收集与诊断推理，并由元认知编排器按需激活专家代理进行解耦并行推理。该框架在ClinicalBench与RAPID-IPN数据集上显著提升了文档质量与诊断准确率，但其动态拓扑在极端信息缺失场景下的鲁棒性仍需验证。

】

---

【BioVLM: Routing Prompts, Not Parameters, for Cross-Modality Generalization in Biomedical VLMs ｜生物医学视觉语言模型中的动态提示路由

研究机构：美国卡内基梅隆大学、印度理工学院孟买分校

作者：Mainak Singha、Tanisha Gupta、Ankit Jha 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17629)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17629)

> 生物医学视觉语言模型在跨模态泛化时，常因单一提示向量无法覆盖多模态下的视觉多样性而失效。现有提示学习方法多依赖静态平均或固定阈值，难以在少样本与分布偏移场景下动态筛选高置信度语义。BioVLM 通过构建多提示池并引入基于熵的动态选择机制，结合 LLM 属性蒸馏，实现了冻结骨干下的自适应路由。该框架在 2D 医学影像上提升了泛化性能，但其对 3D 体数据空间稀疏性的适用性仍存疑。

】

---

【CANDICE: Agentic Causal Disentanglement with Class Conditional Knowledge Integration for Long Tailed Domain Generalization ｜代理式因果解耦与类条件知识集成

研究机构：美国亚利桑那州立大学

作者：Midhat Urooj、Ayan Banerjee、Sandeep Gupta

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cf21ec35ecd8)

> 医学影像模型在跨中心部署时面临域泛化（Domain Generalization, DG）与长尾识别（Long-Tailed, LT）的双重挑战，传统方法难以同时保持域不变性与稀有类判别力。现有数据驱动范式将类身份与不稳定伪相关纠缠，而人工知识集成又受限于高昂的工程成本。本文提出 CANDICE，通过 LLM 代理自动构建因果解耦管道，在决策层分离域不变特征与类特异性信号。该框架在 10 个数据集上平均提升 10.3%，但依赖 LLM 推理开销且缺乏与主流频率解耦方法的直接对比。

】

---

【ClinAlign: Scaling Healthcare Alignment from Clinician Preference ｜从医生验证的评分标准到可复用原则：医疗大模型对齐的规模化路径

研究机构：香港中文大学、北京大学

作者：Shiwei Lyu、Xidong Wang、Lei Liu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.09653)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.09653)

> 医疗大语言模型在开放临床场景中难以对齐细粒度的医生偏好，通用强化学习人类反馈（RLHF）目标过于粗糙，而自动生成的评分标准（Rubric）又缺乏临床严谨性且难以扩展。本文切入点在于将医生验证的实例级评分标准蒸馏为可复用的场景化原则，实现从“逐条标注”到“原则驱动”的范式转换。通过构建医生验证数据集与原则库，结合强化学习与推理时自我修正，该方法在资源受限条件下实现了超越前沿大模型的对齐效果。其价值在于提供了可扩展的临床对齐基线，但原则蒸馏过程中的信息损失与推理时扩展的饱和效应仍存疑。

】

---

【ClinicalMC: A Benchmark for Multi-Course Clinical Decision-Making with Large Language Models ｜多课程临床决策基准

研究机构：中国科学院

作者：Ruihui Hou、Siyi Zhu、Ziyue Huai 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.03157)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.03157)

> 医疗大语言模型（LLM）在复杂临床决策中可靠性受限，核心矛盾在于现有评估体系与真实诊疗流程的错位。主流基准多聚焦单轮知识召回或单课程诊断，无法捕捉患者病情动态演变下的持续调整能力，导致模型在真实场景中表现失真。本文切入点为构建覆盖入院至出院完整周期的多课程临床决策基准，通过多智能体框架模拟病情迭代与诊疗反馈。该工作填补了动态评估空白，但受限于模拟环境噪声与模型基线能力，其评估效度仍需真实临床数据验证。

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

【Decoding the Multimodal Mind: Generalizable Brain-to-Text Translation via Multimodal Alignment and Adaptive Routing ｜多模态脑信号文本解码与自适应路由

研究机构：中国科学院、中国科学院大学

作者：Chunyu Ye、Yunhao Zhang、Jingyuan Sun 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b72ef32cf6f7)

> 脑-文解码旨在从神经信号中还原语言内容，但现有方法多依赖单一模态表示，忽略了大脑对视觉、听觉与语言信息的联合激活。本文切入点在于利用多模态大语言模型（MLLM）构建共享语义空间，并通过自适应路由机制动态融合不同模态的脑特征。具体做法是引入辅助模块进行多模态指令微调，再经投影器融合后驱动LLM生成文本。该框架在fMRI基准上取得SOTA性能，但其跨被试泛化能力与路由机制的神经生理学解释尚存疑。

】

---

【Dissecting Clinical Reasoning in Natural Language Inference for Large Language Models ｜临床自然语言推理中的提示结构效应与参数高效适配

研究机构：英国曼彻斯特大学、英国谢菲尔德大学

作者：Mael Jullien、Andre Freitas、Marco Valentino 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_df251efafe77)

> 临床自然语言推理（CTNLI）旨在从临床试验报告中提取逻辑蕴含关系，但现有研究常混杂模型架构与提示策略变量，导致无法归因性能差异。本文通过控制变量实验，首次量化了提示结构对推理性能的独立贡献，并验证了低秩适配（LoRA）在小模型上的泛化能力。其核心发现是提示结构解释了44%的性能方差，但这一结论局限于静态单轮任务，未触及动态临床决策中的因果一致性难题。

】

---

【Dr. Assistant: Enhancing Clinical Diagnostic Inquiry via Structured Diagnostic Reasoning Data and Reinforcement Learning ｜临床诊断推理数据与强化学习驱动的问诊智能体

作者：Yue Guo、Fanfu Wang、Jianwei Lv 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.13690)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_802240fc05eb)

> 临床决策支持系统（CDSS）需辅助医生在信息缺失下通过多轮问诊缩小诊断假设空间，但传统规则引擎难以处理非结构化文本与动态交互。现有大语言模型（LLM）在静态问答中表现优异，却在动态问诊中缺乏专业诊断推理逻辑，导致询问方向偏离。本文提出临床诊断推理数据（CDRD）结构及两阶段训练策略，将指南逻辑结构化并作为强化学习（RL）约束。该方案在自建基准上验证了逻辑约束对问诊准确性的提升，但其单智能体架构在复杂共病场景下的泛化能力存疑。

】

---

【EMSDialog: Synthetic Multi-person Emergency Medical Service Dialogue Generation from Electronic Patient Care Reports via Multi-LLM Agents ｜基于多智能体规则约束的急救对话合成与流式诊断预测

研究机构：美国弗吉尼亚大学

作者：Xueren Ge、Sahil Murtaza、Anthony Cortez 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.07549)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07549)

> 对话式诊断预测要求模型在证据不完整的流式交互中实时决定何时提交诊断，现有医疗语料多为双人异步对话，缺乏多角色协作与任务对齐标注，导致模型在动态场景下预测波动大且过早自信。本文切入点在于利用电子患者护理报告（ePCR）作为事实锚点，构建包含确定性规则检查器的多智能体生成管道，产出符合急救流程逻辑的多角色合成数据。该方法通过迭代批判-精炼机制强制事实接地与话题流合规，显著提升了小模型在真实急救对话上的预测准确性与稳定性。其价值在于验证了规则约束合成数据对流式诊断任务的增益，但规则覆盖范围与临床变体适应性仍存疑。

】

---

【Enrich, Aggregate, and Generate: Three-stage Biomedical Data-to-Text Generation Using Large Language Models in Low-resource Scenarios ｜生物医学数据到文本生成中的三阶段微规划框架

研究机构：复旦大学

作者：Yupian Lin、Guangya Yu、Yuang Bian 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_39b92517c57f)

> 生物医学数据到文本生成（D2T）旨在将结构化药物信息转化为流畅且准确的自然语言描述，但受限于医疗数据隐私与稀缺性，标注数据极度匮乏。传统预训练语言模型（PLM）依赖大量监督数据，而大语言模型（LLM）直接进行少样本生成时，常因输入实体的语义稀疏导致数值误读与事实错误。本文提出EAG框架，通过语义丰富、显式聚合与生成三阶段流程，在低资源场景下利用LLM的上下文学习能力解决上述问题。该框架在BioLeaflets数据集上显著优于基线，但其对输入数据预处理质量的依赖及缺乏幻觉率量化指标，限制了其在高风险临床场景的直接部署。

】

---

【Evaluating Large Vision Language Models on Bangla Medical Visual Question Answering ｜孟加拉语医学视觉问答基准与模型评估

作者：Rafid Ahmed、Intesar Tahmid、Mir Sazzat Hossain 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f75f5373d5a3)

> 现有医学视觉问答（Med-VQA）基准严重依赖英语，导致低资源语言场景下的多模态推理能力无法被有效量化。通用大视觉语言模型（LVLM）在缺乏领域适配时，面对非英语医学影像常出现严重的视觉-语言对齐失效。本文通过构建包含7,000对临床验证问答的BanglaMedVQA数据集，并系统评估九种主流LVLM在零样本、思维链（CoT）及低秩适应（LoRA）微调下的表现，揭示了模型在细粒度诊断推理上的显著短板。该工作填补了孟加拉语医学VQA的空白，但其依赖LLM翻译生成的数据管线可能引入系统性偏差，且未解决模型在专业诊断类别上的根本性推理缺陷。

】

---

【Experience is the Teacher: Reusing Atomic Thoughts from LLMs to Improve Medical Dialogue ｜原子思维蒸馏框架

作者：Guangya Yu、Hui Luo、Qi Ye 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_acf880749a9b)

> 多轮医疗对话中，静态专家模板僵化且测试时扩展冗余，导致推理既不够灵活也不够高效。本文切入点是将推理过程拆解为可复用的“原子思维”单元，通过教师模型提取并蒸馏至小模型。具体做法是构建基于嵌入去重的经验库，指导生成推理轨迹并微调学生模型。该方法在同等参数量级下显著提升了临床逻辑与准确性，但绝对性能仍低于顶级大模型，且依赖教师模型的质量。

】

---

【GraphDx: A Cost-Aware Knowledge-Enhanced Multi-Agent Framework for Sequential Diagnosis ｜基于成本感知知识图谱的多智能体诊断框架

作者：Shaoting Tan、Ning Liu、Yuntao Du 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f67819f3e03a)

> 临床顺序诊断要求智能体在信息缺失与资源约束下平衡准确率与成本，现有大语言模型（LLM）因缺乏显式领域模型常陷入“防御性医疗”式过度检查。本文指出LLM存在“知识-推理差距”，即虽具备医学知识却无法在成本约束下进行系统性假设检验。GraphDx通过自动化构建含定量属性的医学诊断知识图谱（MDKG），并设计感知、推理、决策三代理协作架构，将复杂推理卸载至符号引擎。该方法在MedQA与MIMIC-IV上将成功率提升至79%-93%并降低20%-54%成本，但其对图谱覆盖范围的依赖及小模型下的泛化边界仍需进一步验证。

】

---

【HeteroRAG: A Heterogeneous Retrieval-Augmented Generation Framework for Medical Vision Language Tasks ｜异构检索增强生成框架

作者：Zhe Chen、Yusheng Liao、Zhiyuan Zhu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2508.12778)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_022f07e10b76)

> 医学大型视觉语言模型（Med-LVLMs）在临床诊断中面临事实性错误与输出不可靠的严峻挑战，直接威胁诊疗安全。现有单模态或单一来源的检索增强生成（RAG）系统无法有效处理缺乏直接视觉语义且语言风格多样的异构医学语料，导致检索结果与查询特征错位。本文通过构建多模态报告库与多源文本语料库，提出包含模态特定检索器、多语料查询生成器及异构知识偏好调优的闭环框架。该框架在11个基准上实现了SOTA性能，但其在极端分布外（OOD）场景下的泛化边界及检索数据泄露风险仍需进一步审视。

】

---

【Learning Dynamic Representations and Policies from Multimodal Clinical Time-Series with Informative Missingness ｜多模态临床时序中的信息性缺失建模与离线策略学习

研究机构：美国埃默里大学、美国麻省理工学院

作者：Zihan Liang、Ziwen Pan、Ruoxuan Xiong

论文原文见 [arXiv](https://arxiv.org/abs/2604.21235)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.21235)

> 临床电子健康记录（EHR）中的观测缺失并非随机噪声，而是由患者病情严重度与医生决策共同驱动的信息性信号，但现有方法多将其视为需填补的干扰项。本文指出，忽略观测过程的时间动态与模态差异会导致患者状态表示丢失关键临床信息，进而阻碍离线强化学习中的长期决策优化。通过构建融合结构化缺失特征与文本文档过程因子的多模态编码器，并结合动作条件变分推断，框架实现了从“处理缺失”到“利用缺失”的范式转换。该框架在重症监护室（ICU）脓毒症治疗策略优化中显著超越临床行为基线，但其对高严重度子群的依赖性及跨机构泛化能力仍存疑。

】

---

【MDTeamGPT: Mitigating Context Collapse and Enabling Self-Evolution in Medical Multi-Agent Reasoning ｜医疗多智能体协作中的上下文崩塌与自进化机制

作者：Kai Chen、Xinfeng Li、Tianpei Yang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_11744cfa0b0d)

> 多智能体医疗会诊面临长程推理中的上下文崩塌与经验复用低效两大瓶颈。现有方法依赖全量历史传递或简单投票，导致信息稀释与错误累积，无法将诊断轨迹转化为可迁移策略。本文提出MDTeamGPT，通过Lead Physician结构化压缩与双知识库检索实现上下文稳定与自进化。该框架在静态问答基准上表现领先，但其有效性局限于文本推理场景，缺乏动态交互验证。

】

---

【MedDCR: Learning to Design Agentic Workflows for Medical Coding ｜医学编码智能体工作流自动优化

研究机构：澳大利亚悉尼大学

作者：Jiyang Zheng、Islam Nassar、Thanh Vu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.13361)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.13361)

> 医学编码需将非结构化笔记映射为ICD代码，传统判别式模型受限于长尾分布，而现有智能体框架依赖人工设计固定流程，难以捕捉复杂规则间的协同效应。MedDCR将工作流设计形式化为迭代搜索问题，通过Designer-Coder-Reflector闭环与记忆档案自动发现最优工具组合。该方法在MDACE上取得0.51 Micro-F1，较次优基线提升6.2%，但绝对精度仍低于微调型判别式SOTA，其通用LLM骨干在缺乏领域微调时的性能上限存疑。

】

---

【MedErrBench: A Fine-Grained Multilingual Benchmark for Medical Error Detection and Correction with Clinical Expert Annotations ｜医疗错误检测与修正的多语言基准

作者：Congbo Ma、Yichun Zhang、Yousef Al-Jazzazi 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a9764404fad5)

> 医疗大语言模型在生成临床文本时易产生事实性错误，现有评估体系缺乏针对错误细粒度定位与修正的多语言标准。本文通过构建包含十类专家定义错误、覆盖英中阿三语的MedErrBench，系统评估了通用、语言专用及医疗专用模型在错误检测、定位与修正上的表现。实验揭示了非英语场景下模型性能的显著衰减，以及医疗专用模型在纠错任务上未超越通用模型的现状。该基准填补了多语言医疗纠错评估空白，但数据构建依赖错误注入法，其分布与真实临床错误的一致性存疑。

】

---

【MedKInstruct: A Multimodal Knowledge Graph Based Framework for Multi-Hop and Hard-Negative Instruction Data Synthesis in MedVQA ｜多模态医学知识图谱驱动的指令数据合成

作者：Yinan Wu、Jihang Jin、Xuhao Bao 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7a59a8ff9b3b)

> 医学视觉问答（Med-VQA）的核心瓶颈在于通用大视觉语言模型（LVLM）缺乏深层医学知识推理能力，导致生成答案常脱离病理逻辑。现有指令数据合成方法仅基于图像描述生成视觉属性问答，无法覆盖疾病因果、系统归属等知识级推理，限制了模型在复杂临床场景下的表现。本文提出 MedKInstruct，通过引入多模态医学知识图谱（MMKG）指导 LVLM 合成多跳与硬负例指令数据，并设计基于 MMKG 路径的强化学习奖励函数，使模型在训练阶段显式学习中间医学知识。该方法在 Slake 和 VQA-RAD 上分别提升 4.16% 和 4.50%，但 MMKG 的静态结构与实体对齐误差可能引入知识偏差，其鲁棒性边界尚待检验。

】

---

【MedLayBench-V: A Large-Scale Benchmark for Expert-Lay Semantic Alignment in Medical Vision Language Models ｜医学视觉-语言模型中的专家-通俗语义对齐基准

作者：Han Jang、Junhyeok Lee、Heeseong Eum 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.05738)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_010726e88ede)

> 医学视觉-语言模型（Med-VLMs）在诊断影像解读上已具备专家级能力，但其训练数据局限于专业术语，导致模型无法将视觉证据转化为患者可理解的通俗语言。现有文本简化研究虽已成熟，但缺乏多模态场景下的平行数据与评估标准，使得模型在通俗语域上的表现无法被量化。本文通过构建结构化概念接地精炼（SCGR）管线生成79,793对专家-通俗平行数据，填补了这一空白。该基准揭示了当前主流VLM在通俗对齐上的显著性能缺口，但其评估协议对生成质量的捕捉仍显单薄。

】

---

【MedQPA-Gen: Medical Question Proposing and Answering for Report Generation ｜基于问答推理的医学报告事实性评估与生成

研究机构：美国伊利诺伊大学厄巴纳-香槟分校

作者：Weijie Liang、Xiyue Zhu、Ruike Zhu 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0e03d5127c45)

> 导读 医学报告生成（RRG）的核心痛点在于模型常生成流畅但事实错误的文本，传统BLEU等指标无法捕捉这种临床失效。现有强化学习（RL）方法依赖昂贵的人类偏好标注或不可靠的LLM自由评判，缺乏结构化的事实验证机制。MedQPA通过“问题提出与回答”（QPA）框架，将评估转化为规则引导的问答一致性打分，并以此作为RL奖励信号优化生成模型。该方法在事实正确性对齐上优于传统指标，但受限于小模型骨干与单一模态，其临床泛化边界尚待大规模多模态验证。

】

---

【MEDSYN: Benchmarking Multi-EviDence SYNthesis in Complex Clinical Cases for Multimodal Large Language Models ｜多模态临床证据合成基准

作者：Boqi Chen、Xudong Liu、Jiachuan Peng 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_370697df9301)

> 现有医疗多模态大语言模型（MLLMs）基准多聚焦单图问答，无法模拟真实临床中多源异构证据的综合诊断流程。本文指出模型在生成鉴别诊断（DDx）与确定最终诊断（FDx）间存在巨大能力断层，根源在于对文本证据的过度依赖及跨模态校准失真。通过构建包含多类型视觉证据的多语言基准MEDSYN，并引入证据敏感性指标量化跨模态利用差距，揭示了视觉理解瓶颈。该基准填补了复杂临床工作流评估空白，但缺乏对检索增强方法的对比，且未解决小模型在中文任务上的性能地板效应。

】

---

【MI-CXR: A Benchmark for Longitudinal Reasoning over Multi-Interval Chest X-rays ｜多间隔纵向推理基准

研究机构：韩国首尔大学

作者：Sunghwan Steve Cho、Yunseok Han、Jaeyoung Do

论文原文见 [arXiv](https://arxiv.org/abs/2605.15574)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.15574)

> 临床胸片解读依赖跨多次就诊的时序对比以评估疾病进展，但现有视觉-语言模型（VLM）评测多局限于单图或双图对比，无法捕捉全局一致性约束下的长时序推理能力。MI-CXR 将纵向解读形式化为时间事件定位、间隔变化推理与全局轨迹总结三类任务，构建五选一的标准化基准。通过阶段式诊断探针分离局部感知与全局决策，该基准揭示了当前 VLM 在时序结构化决策上的系统性瓶颈。其价值在于提供了细粒度的错误归因框架，但 29.3% 的低准确率是否完全归因于推理缺陷而非视觉感知局限，仍需进一步解耦验证。

】

---

【MultiDx: A Multi-Source Knowledge Integration Framework towards Diagnostic Reasoning ｜多源知识整合诊断推理框架

研究机构：香港城市大学、西湖大学

作者：Yimin Deng、Zhenxi Lin、Yejing Wang 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.24186)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.24186)

> 临床诊断推理要求模型不仅给出正确病名，还需生成符合医学逻辑的可验证推理链，但现有大语言模型（LLM）依赖内部参数化知识或静态知识库，导致在罕见病或知识更新场景下出现推理断裂与幻觉。本文切入点在于将诊断过程解耦为“多源证据生成”与“跨源鉴别诊断”两个阶段，通过并行检索网络、结构化病例及数据库，弥补单一知识源的时效性与覆盖度缺陷。MultiDx 采用两阶段流水线，先由 SOAP 格式化、BM25 检索及 Web 搜索生成候选病列表，再通过投票与鉴别诊断整合出最终预测。该方法在 MedCaseReasoning 基准上实现了 H@1 0.420 的准确率，优于基线模型，但其性能高度依赖外部检索质量，且未验证在纯离线或高噪声环境下的鲁棒性。

】

---

【Multimodal Dual-Path Decoding for Medical Report Generation ｜多模态双路径大模型解码用于放射学报告生成

研究机构：厦门大学、北京大学

作者：Jinghan Sun、Dong Wei、Zhihong Zhu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a6f825379f32)

> 放射学报告生成（RRG）旨在从医学图像自动产生结构化临床文本，其核心价值在于缓解影像检查量激增与放射科医生短缺之间的结构性矛盾。现有方法多依赖大型视觉语言模型（LVLM）或大型语言模型（LLM）单一路径，前者视觉接地强但缺乏细粒度临床知识，后者语义丰富但易产生幻觉。本文提出在解码阶段对LVLM与LLM进行token级概率加权融合，并引入多标签分类提示以增强LLM的临床约束。该框架在MIMIC-CXR上提升了临床实体指标，但缺乏对融合权重动态调整机制的探索，且未解决3D体积数据的空间连续性难题。

】

---

【ProtoCycle: Reflective Tool-Augmented Planning for Text-Guided Protein Design ｜文本引导蛋白质设计的反思式工具增强规划

研究机构：上海交通大学、中国科学技术大学

作者：Yutang Ge、Guojiang Zhao、Sihang Li 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.16896)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16896)

> 文本引导蛋白质设计旨在将自然语言功能需求直接转化为满足特定生物属性的氨基酸序列，但现有端到端模型依赖海量配对数据且存在“计划-执行差距”，即模型能生成合理的文本规划却难以将其转化为高质量的残基序列。ProtoCycle 将设计过程重构为多轮“规划-工具调用-评估-反思”循环，由大语言模型（LLM）担任高层规划器，将序列生成委托给轻量级专用工具，并通过监督微调与强化学习优化规划策略。该方法以极少的训练数据实现了与大规模端到端模型相当甚至更优的语言对齐性能，但其依赖外部工具环境的架构是否限制了序列生成的全局探索能力，仍需进一步审视。

】

---

【RAG-KT: Cross-platform Explainable Knowledge Tracing with Multi-view Fusion Retrieval Generation ｜检索增强跨平台知识追踪

作者：Zhiyi Duan、Hongyu Yuan、Rui Liu

论文原文见 [arXiv](https://arxiv.org/abs/2604.10960)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10960)

> 知识追踪（Knowledge Tracing, KT）旨在从历史交互中预测学生未来表现，但传统深度模型受限于封闭标识符与黑盒隐状态，难以跨平台迁移且缺乏教学可解释性。现有大语言模型（LLM）方案在提示工程中易产生幻觉，在微调中则加剧对源平台分布的依赖，无法同时满足泛化与可靠性需求。RAG-KT通过构建多源异构图并引入多视图融合检索，将LLM推理锚定在结构化外部知识上，实现了零样本下的跨平台预测与归因解释。该方法在冷启动场景下显著优于基线，但其推理延迟与外部知识库构建成本是否抵消了精度收益，仍缺乏量化验证。

】

---

【ReMedi: Reasoner for Medical Clinical Prediction ｜临床结局预测中的困难样本自优化框架

研究机构：新加坡南洋理工大学、新加坡国立大学

作者：Yushi Cao、Yiming Chen、Hongchao Jiang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.01474)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a070b414830a)

> 临床结局预测要求模型从电子健康记录（EHR）中推断死亡、再入院等离散标签，但通用大语言模型（LLM）在缺乏外部知识检索时，常因内部知识局限而陷入随机猜测。现有微调方法如KARE依赖专有教师模型蒸馏，限制了部署灵活性，而直接应用自改进算法STaR在临床任务中增益微弱。ReMedi通过引入“困难样本再生成”机制，将模型预测错误的案例转化为高价值训练数据，结合监督微调（SFT）与直接偏好优化（DPO）实现端到端自优化。该方法在MIMIC-IV基准上显著提升了预测精度，但其对开放临床推理任务的适用性仍存疑。

】

---

【Scaling is Not All You Need: Clinical-Oriented Reinforcement Learning Makes Parameter-Efficient Clinical Reasoning ｜临床导向强化学习（CORL）：参数高效的可验证推理管线

作者：Chi Liu、Yan Shu、Mengzhuo Chen 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fa0cdf5dfc01)

> 导读 临床推理要求模型在不确定性下构建可审计的逻辑链，而非仅输出正确结论，但现有方法依赖海量人工标注的思维链数据或超大模型规模，导致训练与部署成本高昂。本文指出效率瓶颈源于数据策略缺乏可验证性且训练流程未考虑模型学习容量，提出临床导向强化学习（CORL）管线，通过知识图谱拓扑采样合成数据、思维链冷启动及两阶段课程强化学习，在7B和32B规模上实现了接近或超越更大模型的专家级推理性能。该管线验证了精心设计的训练流程比单纯扩大模型规模更具参数效率，但其对教师模型偏差的依赖及多模态场景的缺失仍构成应用边界。

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

【Semi-Supervised Diseased Detection from Speech Dialogues with Multi-Level Data Modeling ｜多粒度层级半监督语音病理检测框架

研究机构：上海交通大学

作者：Xingyuan Li、Mengyue Wu

论文原文见 [arXiv](https://arxiv.org/abs/2601.04744)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.04744)

> 导读 临床语音病理检测面临标注稀缺、标签噪声及会话级弱监督与帧级特征粒度失配的三重约束。现有方法常将长录音切分为独立片段，隐含“症状均匀表达”的错误假设，导致关键病理片段被忽略。本文提出一种单阶段端到端框架，通过会话、片段、帧三级层级建模，动态生成伪标签以对齐远端监督信号。该方法在极低标注率下实现了接近全监督的性能，但其对预训练编码器的冻结策略限制了模型对特定病理声学特征的适应性。

】

---

【STELLA: A Multimodal LLM for Protein Functional Annotation via Unified Sequence-Structure Encoding ｜蛋白质功能注释的多模态大语言模型

研究机构：北京大学、中国人民大学

作者：Hongwang Xiao、Wenjun Lin、Xi Chen 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4782ac22af63)

> 蛋白质功能注释面临结构数据爆发但功能标签滞后的矛盾，现有纯序列语言模型缺乏高分辨率结构信息，分离式多模态架构又引入冗余融合开销。STELLA 切入点在于利用统一编码的 ESM3 替代分离编码器，直接对接 LLM 生成自然语言功能描述。其核心做法是构建“ESM3 编码器 + 线性投影 + Llama-3.1-8B”的两阶段指令微调框架。该方案在酶反应预测上刷新了 SOTA，但功能描述生成的语义鲁棒性仍受限于 NLP 指标的代理性质，且对分布外结构的泛化能力尚未完全解决。

】

---

【TheraAgent: Self-Improving Therapeutic Agent for Precise and Comprehensive Treatment Planning ｜治疗规划智能体

研究机构：清华大学、新加坡国立大学

作者：Junkai Li、Yunghwei Lai、Tianyi Zhu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.05963)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.05963)

> 导读 临床治疗规划要求将诊断结论转化为具体、安全且完整的用药方案，但现有大语言模型（LLM）依赖单次生成，常导致剂量错误、覆盖不全或安全隐患。本文指出单次生成缺乏显式验证机制是核心瓶颈，提出 TheraAgent 框架，通过“生成-反思-精炼”的迭代闭环与临床对齐的 TheraJudge 评估模块实现自我纠错。该框架在 HealthBench 治疗子集上取得 48.94 分，并在专家盲评中以 86% 胜率超越人类医生，但其高计算成本与对骨干模型推理能力的依赖仍存疑。

】

---

【Tracing Mathematical Proficiency Through Problem-Solving Processes ｜基于解题过程的知识追踪

研究机构：韩国延世大学、韩国首尔大学

作者：Jungyang Park、Suho Kang、Jaewoo Park 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.00311)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.00311)

> 知识追踪（Knowledge Tracing, KT）旨在通过历史交互预测学生未来表现，但传统方法仅依赖二值正确率，无法区分粗心与概念误解，导致教学干预缺乏针对性。现有深度模型虽提升了精度，却因黑盒性质难以提供错误归因，且冷启动场景下预测不稳定。本文提出KT-PSP任务与STATUSKT框架，利用三阶段大语言模型（LLM）流水线从手写解题过程中提取数学能力（Mathematical Proficiency, MP）信号作为辅助输入。该方案在自建数据集上验证了过程信号对预测精度与可解释性的双重增益，但受限于数据规模与单一学科领域，其跨平台泛化能力尚存疑。

】

---

【Travel on the ICD Tree: Benchmarking Agentic Reasoning for ICD Coding from Chinese Electronic Medical Records ｜基于树搜索的中文ICD叶节点编码智能体框架

研究机构：复旦大学

作者：Xinjie Xu、Yongqi Fan、Shuang-shuang Chen 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3a7b05c497ee)

> 临床编码自动化长期受困于英文基准的粗粒度标注与中文细粒度场景的缺失，导致现有模型在复杂规则推理与叶节点定位上表现不佳。本文切入点在于构建首个中文全电子病历叶节点级基准Code4Detail，并设计ToT-ICD框架将编码重构为ICD树上的导航与回溯过程。该方法通过集成检索增强与规则验证，在复杂场景下优于传统检索重排范式。其价值在于揭示了LLM在层级推理中的能力边界，但缺乏与判别式基线的直接对比，且未量化树搜索相对于线性工作流的效率代价。

】

---

【X-ray Made Simple: Lay Radiology Report Generation and Robust Evaluation ｜通俗化放射学报告生成与语义鲁棒评估

研究机构：美国匹兹堡大学、英国杜伦大学

作者：Kun Zhao、Chenghao Xiao、Sixing Yan 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_38dfcadccf97)

> 放射学报告生成（RRG）长期受困于专业术语导致的患者理解障碍与词汇重叠指标引发的评估失真。现有方法通过优化编码器-解码器架构提升流畅性，却忽视了报告模板化对模型语义泛化的负面约束。本文切入点在于将“患者可及性”与“评估鲁棒性”视为同源问题，通过构建通俗化数据集并引入基于嵌入的语义匹配指标，验证语言风格对模型训练动态的影响。该框架在语义一致性上表现稳健，但未解决视觉证据接地的核心临床难题。

】
