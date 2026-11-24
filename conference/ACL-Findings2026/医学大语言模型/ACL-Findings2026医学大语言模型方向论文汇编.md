# ACL-Findings2026 · 医学大语言模型方向论文汇编

> 本方向共 8 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Beyond Benchmarks: A Capability-Based Maturity Model for Systematic AI Integration in Hospitals ｜医院AI成熟度模型

作者：Rui Li、Xiaofen WU、Mingqian Liu 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_346f6758424c)

> 医疗大语言模型在标准化考试中的高分与真实临床工作流中的低效之间存在显著断层，现有评估体系仅聚焦于知识召回与单步推理，忽视了医院系统治理、合规约束及多轮交互能力。本文切入点在于将评估维度从模型内部推理扩展至医院系统级成熟度，提出分层能力模型。通过构建L0-L4真实临床场景基准并对比开源模型，验证了学术分数与临床效用的非线性关系。该框架为医院AI部署提供了系统性路径，但其对高阶治理任务的评估标准泛化性仍存疑。

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

【Dissecting Clinical Reasoning in Natural Language Inference for Large Language Models ｜临床自然语言推理中的提示结构效应与参数高效适配

研究机构：英国曼彻斯特大学、英国谢菲尔德大学

作者：Mael Jullien、Andre Freitas、Marco Valentino 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_df251efafe77)

> 临床自然语言推理（CTNLI）旨在从临床试验报告中提取逻辑蕴含关系，但现有研究常混杂模型架构与提示策略变量，导致无法归因性能差异。本文通过控制变量实验，首次量化了提示结构对推理性能的独立贡献，并验证了低秩适配（LoRA）在小模型上的泛化能力。其核心发现是提示结构解释了44%的性能方差，但这一结论局限于静态单轮任务，未触及动态临床决策中的因果一致性难题。

】

---

【MedErrBench: A Fine-Grained Multilingual Benchmark for Medical Error Detection and Correction with Clinical Expert Annotations ｜医疗错误检测与修正的多语言基准

作者：Congbo Ma、Yichun Zhang、Yousef Al-Jazzazi 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a9764404fad5)

> 医疗大语言模型在生成临床文本时易产生事实性错误，现有评估体系缺乏针对错误细粒度定位与修正的多语言标准。本文通过构建包含十类专家定义错误、覆盖英中阿三语的MedErrBench，系统评估了通用、语言专用及医疗专用模型在错误检测、定位与修正上的表现。实验揭示了非英语场景下模型性能的显著衰减，以及医疗专用模型在纠错任务上未超越通用模型的现状。该基准填补了多语言医疗纠错评估空白，但数据构建依赖错误注入法，其分布与真实临床错误的一致性存疑。

】

---

【MEDSYN: Benchmarking Multi-EviDence SYNthesis in Complex Clinical Cases for Multimodal Large Language Models ｜多模态临床证据合成基准

作者：Boqi Chen、Xudong Liu、Jiachuan Peng 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_370697df9301)

> 现有医疗多模态大语言模型（MLLMs）基准多聚焦单图问答，无法模拟真实临床中多源异构证据的综合诊断流程。本文指出模型在生成鉴别诊断（DDx）与确定最终诊断（FDx）间存在巨大能力断层，根源在于对文本证据的过度依赖及跨模态校准失真。通过构建包含多类型视觉证据的多语言基准MEDSYN，并引入证据敏感性指标量化跨模态利用差距，揭示了视觉理解瓶颈。该基准填补了复杂临床工作流评估空白，但缺乏对检索增强方法的对比，且未解决小模型在中文任务上的性能地板效应。

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

【Scaling is Not All You Need: Clinical-Oriented Reinforcement Learning Makes Parameter-Efficient Clinical Reasoning ｜临床导向强化学习（CORL）：参数高效的可验证推理管线

作者：Chi Liu、Yan Shu、Mengzhuo Chen 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fa0cdf5dfc01)

> 导读 临床推理要求模型在不确定性下构建可审计的逻辑链，而非仅输出正确结论，但现有方法依赖海量人工标注的思维链数据或超大模型规模，导致训练与部署成本高昂。本文指出效率瓶颈源于数据策略缺乏可验证性且训练流程未考虑模型学习容量，提出临床导向强化学习（CORL）管线，通过知识图谱拓扑采样合成数据、思维链冷启动及两阶段课程强化学习，在7B和32B规模上实现了接近或超越更大模型的专家级推理性能。该管线验证了精心设计的训练流程比单纯扩大模型规模更具参数效率，但其对教师模型偏差的依赖及多模态场景的缺失仍构成应用边界。

】
