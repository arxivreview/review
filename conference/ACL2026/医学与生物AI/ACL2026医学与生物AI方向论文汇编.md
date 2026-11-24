# ACL2026 · 医学与生物AI方向论文汇编

> 本方向共 26 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Act as you think: Reinforcing Consistent Reasoning in Medical Visual Question Answering ｜多一致性奖励机制下的医学视觉问答强化学习

研究机构：浙江大学、清华大学

作者：Songtao Jiang、Yuan Wang、Ruizhe Chen 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_745af1c99a21)

> 医学视觉问答（Med-VQA）在引入强化学习从可验证奖励（RLVR）以增强推理能力时，面临模型生成看似合理但脱离视觉证据的推理，以及最终答案与推理过程逻辑断裂的双重失效。现有标准RLVR仅奖励答案正确性，导致模型在缺乏高质量思维链（CoT）数据的医学域中，通过忽略图像细节来“猜”出正确答案，而非真正理解影像。本文通过构建覆盖30种模态的Med-Zero-17K数据集，并提出多一致性奖励（MCR）框架，将感知-认知一致性与认知-决策一致性纳入奖励函数，强制模型依赖视觉特征并保持逻辑连贯。该框架在分布外（OOD）基准上显著优于监督微调（SFT），但在开放域长文本生成任务上仍未达到当前最优水平，其奖励机制对极端噪声场景的鲁棒性存疑。

】

---

【Benchmarking Egocentric Clinical Intent Understanding Capability for Medical Multimodal Large Language Models ｜基于眼动信号的自我中心临床意图理解基准

研究机构：深圳大学、美国斯坦福大学

作者：Shaonan Liu、Guo Yu、Xiaoling Luo 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.06750)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.06750)

> 医疗多模态大语言模型（Med-MLLMs）在真实临床部署中需从第一人称视角理解医生操作背后的意图，但现有基准仅评估“发生了什么”而非“为什么这么做”。本文提出 MedGaze-Bench，利用临床医生注视点作为“认知光标”，构建空间、时间、标准三维意图评估框架，并引入对抗性陷阱问答机制测试模型可靠性。该基准揭示了当前模型在因果归因与安全拒答上的严重缺陷，但其评估结果受限于零样本设定与特定场景覆盖，能否泛化至动态多轮交互尚存疑。

】

---

【Beyond Surface Features: Advancing Medical Vision-Language Alignment via Dynamic Evidence-Guided Preference Optimization ｜动态证据引导偏好优化

研究机构：西湖大学、中国科学院大学

作者：Zixuan Huang、Zhihong Zhu、Xiaolong Liu 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a5f8b0914e74)

> 医学大视觉语言模型（Med-LVLMs）在生成临床报告时，常因模态错位而产生看似流畅但事实错误的幻觉。现有基于直接偏好优化（DPO）的方法依赖静态偏好对，导致模型过拟合表面语言线索，且奖励信号出现伪收敛，无法持续抑制新出现的幻觉。DEPO 通过多模态证据扰动与负样本动态重采样，在训练过程中动态调整输入与负样本，迫使模型依赖视觉证据而非语言捷径。该框架在多个基准上显著优于现有方法，但其对冻结定位器先验的依赖及计算开销，限制了其在资源受限场景下的直接部署。

】

---

【CAMEC: Complexity-Aware Multi-Expert Collaboration for Reliable Chinese Medical Question Answering ｜复杂度感知多专家协作

作者：Yukang Wu、Xiyuan Jia、Jiayi Wu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0dbdb47ad85a)

> 导读 中文医疗问答面临的核心矛盾是单模型推理在复杂病例下的幻觉与逻辑断裂，而现有检索增强或静态多智能体方案缺乏对查询难度的自适应响应与质量闭环控制。CAMEC 通过引入基于查询复杂度的动态路由机制，将思维链、检索增强与知识图谱封装为并行专家，并由统一裁判模块迭代精炼，解决了静态协作策略在简单查询上的算力浪费与在复杂查询上的验证缺失问题。该方法在四个中文基准上超越基线，但评估仍局限于静态选择题，未触及动态临床交互中的鲁棒性验证。

】

---

【CPR-RAG: Clinical Prior-Regularized Retrieval for Anatomy-Aware 3D CT Report Generation ｜临床先验正则化检索增强生成

研究机构：韩国光州科学技术院

作者：Sungkyu Yang、Kang-Min Kim、Mansu Kim

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2d9aa6952e55)

> 3D CT报告生成面临的核心困境是视觉-语义对齐失效：高维体积压缩为单一全局嵌入后，细粒度病灶特征被正常解剖结构淹没，导致模型产生“正常性偏差”或幻觉。现有RAG方法仅依赖视觉相似度检索，常引入形态相似但病理不同的噪声案例，且全报告检索会稀释关键异常信号。本文切入点在于将临床共现统计引入检索重排序，并过滤模板化正常描述，以器官为中心提升证据信息密度。该框架在冻结骨干上显著提升了临床召回率，但其静态先验矩阵能否捕捉动态疾病进展，以及验证集测试是否高估泛化能力，仍存疑。

】

---

【CT-FineBench: A Diagnostic Fidelity Benchmark for Fine-Grained Evaluation of CT Report Generation ｜CT-FineBench：基于细粒度属性问答的CT报告评估基准

研究机构：阿里巴巴集团、复旦大学

作者：Ruifeng Yuan、Wanxing Chang、Weiwei Cao 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.24001)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.24001)

> 放射学报告生成（Radiology Report Generation, RRG）的评估长期受困于词汇重叠指标与临床事实脱节的矛盾。现有实体匹配或大语言模型整体打分方法无法捕捉CT报告中病灶大小、位置等细粒度属性的错误，导致“语言流畅但临床错误”的报告获得高分。本文提出CT-FineBench，将评估重构为针对临床属性的问答（QA）事实核查任务，通过属性级答案比对量化报告准确性。该基准在CT-RATE上实现了与专家判断0.622的Pearson相关性，显著优于现有指标，但其数值误差阈值的临床验证缺失及跨模态泛化能力仍存疑。

】

---

【EchoVLM: Dynamic Mixture-of-Experts Vision-Language Model for Universal Ultrasound Intelligence ｜超声专用视觉语言模型 EchoVLM

研究机构：西北工业大学、中山大学

作者：Chaoyin She、Ruifang Lu、Lida Chen 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.14977)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.14977)

> 超声诊断长期依赖医师经验，导致主观性强且效率低下，而通用视觉语言模型（VLM）缺乏超声特异性知识，无法直接应用于临床。现有医疗VLM多采用全量微调，易破坏预训练表征且难以覆盖多器官异构任务。本文提出EchoVLM，通过构建大规模多器官数据集与双路径混合专家（Dual-path MoE）架构，在保留基座模型通用能力的前提下注入超声领域知识。该工作验证了参数高效微调在超声多任务场景的有效性，但其评估仅依赖文本相似度指标，未触及空间定位准确性这一临床核心痛点。

】

---

【Enhancing Reinforcement Learning for Radiology Report Generation with Evidence-aware Rewards and Self-correcting Preference Learning ｜证据感知自校正强化学习

研究机构：浙江大学

作者：Qin Zhou、Guoyan Liang、Qianyi Yang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.13598)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.13598)

> 放射学报告生成（RRG）的核心矛盾在于模型生成的文本常与图像视觉证据脱节，导致临床幻觉。现有强化学习（RL）方法依赖报告级奖励，缺乏细粒度视觉接地指导，且无自我修正机制。本文提出ESC-RL框架，通过组别感知的视觉证据奖励与自校正偏好学习，实现疾病特异性的证据对齐与噪声过滤。该框架在2D胸片任务上取得SOTA性能，但其对3D体积数据的泛化能力及LLM重构带来的推理延迟尚未验证。

】

---

【Evo-PI: Aligning Medical Reasoning via Evolving Principle-Guided Supervision ｜进化原则引导的医疗多模态推理对齐

研究机构：新西兰奥克兰大学、北京邮电大学

作者：Xianda Zheng、Huan Gao、Meng-Fen Chiang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.31800)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.31800)

> 医疗多模态大语言模型（MLLMs）在临床影像问答中常因静态监督信号无法适应模型能力增长，导致推理逻辑固化与泛化瓶颈。现有强化学习（RL）方法依赖固定标量奖励，仅优化最终答案正确性，难以塑造中间推理过程。Evo-PI 将领域知识外化为可迭代的“推理原则库”，通过原则引导的强化学习与原则自进化闭环，实现监督信号与模型能力的协同演化。该方法在八种医学影像模态上平均提升准确率 24.59%，但缺乏与最新文本推理方法的跨模态公平对比，其原则库的自动化生成边界尚待验证。

】

---

【From Answers to Arguments: Toward Trustworthy Clinical Diagnostic Reasoning with Toulmin-Guided Curriculum Goal-Conditioned Learning ｜基于图尔敏论证模型的临床诊断推理课程学习

作者：Chen Zhan、Xiaoyu Tan、Gengchen Ma 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.11137)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11137)

> 临床大语言模型常陷入“答案正确但推理错误”的陷阱，现有评估仅关注结果准确率，训练则依赖不稳定的强化学习，导致模型缺乏可解释性与鲁棒性。本文切入点在于将图尔敏论证模型同时作为评估标尺与训练目标，通过三阶段课程目标条件学习（Curriculum Goal-Conditioned Learning, CGCL）替代在线强化学习。该方法以离线模仿学习构建结构化诊断论证，在3B小模型上以更低计算成本达到与强化学习相当的推理质量。其价值在于提供了稳定且可解释的训练范式，但7B模型上性能略低于强化学习基线，且评估依赖大语言模型裁判，泛化边界尚存疑。

】

---

【HOPE: Hybrid Optimized Parallel Encoding with Supervised and Unsupervised Semantic Fusion for Depression Symptom Detection ｜混合优化并行编码（HOPE）：直推式监督-无监督融合框架

研究机构：瑞士洛桑大学

作者：Tu-Phuong Mai、Minh-Ha H. Le、Duc-Luong Tran 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9bbbe4f0ec19)

> 导读 社交媒体抑郁症状检测面临标注数据稀缺与训练-测试分布时间域偏移的双重困境，纯监督模型难以泛化至大规模无标签测试集。HOPE 框架通过直推式设定，将无标签测试集视为无监督聚类输入，结合监督特征提取与临床知识初始化质心，实现细粒度症状识别。该方法在 eRisk 2025 排名任务中 MAP 达 72.76%，显著优于传统监督基线，但其依赖测试集分布的直推式假设在真实部署中的泛化边界尚存疑。

】

---

【How Much Would a Clinician Edit This Draft? Evaluating LLM Alignment for Patient Message Response Drafting ｜临床消息回复草稿的编辑负载评估与主题驱动适配

研究机构：美国达特茅斯学院

作者：Parker Seegmiller、Joseph Gatto、Sarah E. Greer 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.11344)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.11344)

> 患者门户消息回复草稿旨在通过LLM生成初稿以减轻医生异步沟通负担，但现有评估多依赖主观反馈或通用文本相似度指标，无法量化医生实际修改工作量。本文切入点在于将“对齐”具体化为“编辑负载”，提出双维度EditJudge框架与主题驱动DPO适配策略。其核心是通过主题分类作为中间层，约束模型在特定临床意图上的生成行为。该方法在本地小模型上实现了接近前沿商用模型的编辑效率，但个体医生偏好差异导致的性能天花板仍显著存在。

】

---

【ICDAGENT: Empowering Agentic Large Language Models for Explainable Medical Coding ｜可解释ICD编码的双智能体协同验证框架

研究机构：美国石溪大学

作者：Ziyi Yin、Yuanpu Cao、Ting Wang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ec0ce4b23add)

> 临床自然语言处理中的医学编码长期面临“黑盒预测”与“临床信任”的矛盾，传统判别式模型虽精度高但无法提供可验证的证据链，而通用大语言模型（LLM）直接提示则易产生幻觉且缺乏专用编码知识。ICDAGENT通过构建编码智能体与批判智能体的对抗协作机制，引入基于推理质量感知的强化学习奖励函数，解决了初步解释中证据伪造与逻辑断裂的问题。该框架在MIMIC-IV数据集上实现了优于商用LLM的解释完整性与指南对齐度，但其纯编码精度仍略低于最新知识增强判别式模型，且依赖外部模型进行推理质量评分，其泛化边界尚待验证。

】

---

【Interleaved Tool-Call Reasoning for Protein Function Understanding ｜工具增强蛋白质功能理解智能体

作者：Chuanliu Fan、Zicheng Ma、Huanran Meng 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.03604)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03604)

> 蛋白质功能理解任务要求从序列推断生物角色，但纯文本推理模型受限于参数化知识，无法获取外部生物学证据，导致预测缺乏可验证性。本文指出强化学习仅能提升正确轨迹的采样概率，无法弥补领域知识缺失，因此提出PFUA框架，通过动态调用计算生物学工具实现接地推理。该范式在四个基准上显著优于纯文本推理基线，但其性能高度依赖工具池的覆盖度与质量，且未与专用蛋白质语言模型进行公平对比。

】

---

【Is EEG-to-Text Feasible in Real-World Scenarios? An In-Depth Analysis Using a Neuropsychology-Inspired Benchmark ｜基于神经心理学范式的EEG2Text基准与无教师强制评估

研究机构：哈尔滨工业大学、南京大学

作者：Zihan Zhang、Yu Bao、Xiao Ding 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.18749)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.18749)

> EEG2Text旨在从非侵入性脑电中解码内部语言意图，但现有评估依赖教师强制，掩盖了真实场景下的暴露偏差，导致性能虚高与可行性争议。本文指出，既有基准忽略EEG信号在时间上的不稳定性，使得模型无法在无真实历史token的条件下生成有效文本。通过构建包含被试内重复的COFETT数据集，并采用向量对齐替代BLEU作为评估指标，本文实现了无教师强制的可靠评估。该工作提供了EEG含可解码语言信息的实证证据，但其结论受限于当前数据规模下信噪比极低的物理约束。

】

---

【LearnerCoMPASS: Intelligent Tutoring System with Dynamic Cognitive Diagnosis and Multi-Model Path Planning ｜学习者罗盘：基于动态认知诊断与多模型路径规划的自适应学习系统

研究机构：华中科技大学、武汉大学

作者：Ziji Sheng、Guiyao Tie、Weidong Wang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d8efcc70ef42)

> 自适应学习系统需在逻辑严谨的STEM领域同时实现深度个性化、动态适应与内容可信，但现有LLM规划器面临诊断僵化、事实幻觉与规划短视三大瓶颈。本文切入点在于将离线训练的认知诊断重构为推理时的实时状态估计，并通过混合知识图谱与多智能体搜索闭环解决上述矛盾。其核心做法是构建一个包含动态知识图谱、多智能体编码器-解码器诊断模块及AB-MCTS-M路径规划引擎的端到端框架。该框架在STEM路径规划质量上显著优于基线，但其依赖静态知识图谱的冷启动成本与多智能体推理延迟是否满足实时辅导要求，仍存疑。

】

---

【Looking at Radiology Report Generation through a Causal Lens: A Survey ｜放射学报告生成的因果推断视角

研究机构：印度理工学院孟买分校

作者：Satyam Kumar、Kaustubh Shivshankar Shejole、Pushpak Bhattacharyya

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6e36d78c227b)

> 放射学报告生成（RRG）旨在将医学影像转化为结构化临床文本，但现有系统常因数据偏差与模型幻觉产生临床错误。主流方法侧重于优化语言流畅性或视觉对齐，却忽视了影像特征与诊断结论之间虚假相关的因果本质。本文通过构建结构因果模型（SCM），将RRG形式化为因果推断问题，提出数据、模型、评估三层干预框架以消除混杂偏差。该工作填补了RRG领域因果视角的空白，但缺乏端到端实证验证，其理论框架在真实临床场景中的有效性仍存疑。

】

---

【MARCH: Multi-Agent Radiology Clinical Hierarchy for CT Report Generation ｜多智能体放射学临床层级框架

研究机构：澳大利亚西澳大学、美国佛罗里达大学

作者：Yi Lin、Yihao Ding、Yonghui Wu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.16175)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16175)

> 3D CT报告生成面临的核心困境是单模型黑盒机制导致的临床幻觉与可解释性缺失。现有视觉-语言模型虽提升了流畅度，但缺乏人类放射科层级审查中的迭代验证机制，导致细微病理遗漏与事实错误难以纠正。MARCH通过模拟住院医师-专科医师-主治医生的三级协作流程，引入检索增强与共识辩论机制，将生成过程转化为可审计的多轮推理。该框架在RadGenome-ChestCT上实现了临床效度与语言质量的同步提升，但其对通用大语言模型骨干的依赖及缺乏纵向记忆机制，限制了其在真实临床闭环中的泛化潜力。

】

---

【MedEinst: Benchmarking the Einstellung Effect in Medical LLMs through Counterfactual Differential Diagnosis ｜医疗大语言模型中的思维定势效应（Einstellung Effect）基准与因果推理智能体

研究机构：美国斯坦福大学、深圳大学

作者：Wenting Chen、Zhongrui Zhu、Guolin Huang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.06636)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.06636)

> 导读 临床诊断依赖对细微鉴别证据的敏感捕捉，但大语言模型（LLM）常陷入“思维定势效应”，即过度依赖统计捷径而忽略患者特异性证据，导致非典型病例误诊。现有基准仅评估静态知识或标准流程，无法暴露这种在反事实场景下的推理失效。本文构建首个反事实诊断基准 MedEinst，并提出基于循证医学（EBM）的因果推理智能体 ECR-Agent，通过结构化证据验证抑制统计偏差。该工作揭示了前沿模型“能力越强、盲点越深”的悖论，但其单智能体架构在复杂多病共存场景下的泛化能力仍存疑。

】

---

【MediEval: A Unified Medical Benchmark for Patient-Contextual and Knowledge-Grounded Reasoning in LLMs ｜医疗大语言模型事实-上下文解耦评估与风险感知微调

作者：Zhan Qu、Michael Färber

论文原文见 [arXiv](https://arxiv.org/abs/2512.20822)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.20822)

> 医疗大语言模型在临床部署中面临的核心矛盾是“知道”医学事实与“安全使用”这些事实之间的鸿沟，现有基准要么孤立测试知识召回，要么仅评估患者数据提取而忽略医学正确性。本文切入点在于将事实正确性与上下文支持性解耦为四个正交维度，构建基于真实电子健康记录与生物医学本体图的统一评估框架。通过引入非对称惩罚的偏好优化方法，该工作旨在抑制将正确知识误植于错误患者或将错误信息包装为有效证据的安全关键错误。其价值在于提供了细粒度的安全审计视角，但四象限分类是否足以捕捉临床推理的连续性与模糊性仍存疑。

】

---

【MicroC-KT: Modeling Community Effect via Learning Micro-Environment for Evidence-Grounded Explainable Knowledge Tracing ｜基于学习微观环境的证据锚定知识追踪

研究机构：吉林大学

作者：Zhiyi Duan、Zixing Shi、Bing Jia 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_35fa1596feaf)

> 知识追踪（KT）旨在从历史交互中预测学生表现，但现有LLM方法依赖个体稀疏历史，易产生幻觉且缺乏可验证的解释。本文切入点在于引入“学习微观环境”，通过超图聚类识别学生社区，将群体统计特征转化为文本证据，为LLM提供推理锚点。该方法在零样本设置下，通过双粒度摘要与同伴检索，实现了预测精度与解释可靠性的同步提升。其价值在于证明了群体结构对缓解个体数据稀疏的有效性，但超图静态构建与LLM推理延迟的矛盾仍存疑。

】

---

【ProMedical: Hierarchical Fine-Grained Criteria Modeling for Medical LLM Alignment via Explicit Injection ｜医疗大语言模型对齐中的细粒度标准显式注入

作者：He Geng、Yangmin Huang、Lixian Lai 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.08326)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.08326)

> 医疗大语言模型（Medical LLMs）在临床部署中面临训练信号粗粒度与评估标准细粒度之间的结构性错位，导致模型难以内化复杂的安全与推理逻辑。现有基于二元偏好的对齐范式无法捕捉临床陷阱的长尾分布，ProMedical 通过构建包含医师定义评分标准（Rubrics）的偏好数据集，并训练多维奖励模型（RARM）驱动组相对策略优化（GRPO），将安全约束从软惩罚升级为硬否决。该框架在自建基准上实现了准确率与安全合规性的显著提升，但其对自建评估协议的依赖及缺乏与最新强化学习可验证奖励（RLVR）方法的直接对比，限制了其泛化能力的验证。

】

---

【Protein-STORY: Semantic Text-Oriented Representation Yields biologically meaningful Protein embeddings ｜蛋白文本叙事语义压缩

作者：Nabil Ibtehaz、Daisuke Kihara

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a2c71547beea)

> 现有蛋白语言模型（PLM）依赖序列自监督学习，忽略了数十年积累的专家策展文本知识，导致表征缺乏功能与结构的深层语境。Protein-STORY 提出一种多阶段架构，将异构的生物文本描述压缩为统一向量，并投影至自然语言语义空间。该方法实现了零样本文本提示蛋白检索，在下游任务中显著优于序列基线。其价值在于打通了文本知识与蛋白表征的壁垒，但受限于文本源单一及固定长度嵌入瓶颈，通用性仍存疑。

】

---

【Region-Grounded Report Generation for 3D Medical Imaging: A Fine-Grained Dataset and Graph-Enhanced Framework ｜区域接地式3D PET/CT报告生成：VietPET-RoI数据集与HiRRA框架

作者：Cong Huy Nguyen、Son Dinh Nguyen、Guanlin Li 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18145)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18145)

> 3D PET/CT报告生成面临高维体积数据直接映射文本导致的临床幻觉与低资源语言标注缺失双重困境。现有端到端VLM忽略放射科医生“识别感兴趣区域-评估属性-综合诊断”的层级工作流，导致报告缺乏空间接地性与可解释性。本文通过构建首个越南语3D PET/CT区域级标注数据集VietPET-RoI，并提出融合双模态编码与图神经网络的层级框架HiRRA，将全局模式匹配转化为局部临床发现推理。该工作填补了低资源语言下细粒度接地监督的空白，但在跨模态泛化与图结构超参数敏感性上仍存疑。

】

---

【When Background Matters: Breaking Medical Vision Language Models by Transferable Attack ｜医学视觉语言模型的可转移对抗攻击

研究机构：印度理工学院、印度理工学院坎普尔分校

作者：Akash Ghosh、Subhadip Baidya、Sriparna Saha 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17318)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17318)

> 医学视觉语言模型（Medical VLMs）在临床诊断中的部署面临对抗攻击下的安全性风险，现有通用攻击在医学灰度图像上产生显著视觉失真，而医学专用攻击缺乏隐蔽性与可转移性。本文切入点在于利用模型视觉注意力机制的跨架构共享特性，通过约束扰动于非诊断背景区域并引入注意力转移损失，实现隐蔽且可转移的多模态对抗攻击。该方法在六个医学模态上验证了对多种开源与闭源VLM的有效性，揭示了当前临床AI系统在分布偏移下的严重脆弱性，但其对推理模型鲁棒性的挑战及防御机制的缺失仍存疑。

】

---

【When Correct Beliefs Collapse: Epistemic Resilience of LLMs under Clinical Pressure ｜临床压力下的信念崩塌：医疗大语言模型的多轮鲁棒性评估与干预

研究机构：哈尔滨工业大学

作者：Boyu Xiao、Xiuqi Tian、Xuwen Song 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.23932)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.23932)

> 医疗大语言模型在静态基准上表现优异，但在多轮临床交互中常因社会压力放弃正确诊断，即“临床谄媚”。现有评估聚焦单轮准确性或固有幻觉，忽视了持续对抗压力下的信念稳定性，导致模型在真实会诊场景中失效。本文提出MED-STRESS框架模拟多轮压力，并设计RBED与R-FT两种干预策略，揭示了知识能力与鲁棒性的解耦现象。该研究填补了动态临床交互评估的空白，但R-FT对模型通用能力的潜在影响及RLHF安全对齐的副作用机制仍需进一步厘清。

】
