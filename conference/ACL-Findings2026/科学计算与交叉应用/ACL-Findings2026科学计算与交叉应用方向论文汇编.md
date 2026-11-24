# ACL-Findings2026 · 科学计算与交叉应用方向论文汇编

> 本方向共 31 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AI Agents for the Science of Science: A Survey of Tasks, Architectures, Evaluations, and Challenges ｜AI代理在科学之科学中的双重角色：模拟与工具

研究机构：美国东北大学

作者：Yixuan Liu、Yicheng Zhang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f5e239c6d4b3)

> 科学之科学（Science of Science, SciSci）旨在通过大规模文献计量数据揭示科学知识生产、评估与转化的规律，但传统统计与网络分析方法难以处理跨学科广度及动态交互过程。现有基于大语言模型（LLM）的代理系统多聚焦于执行具体科研任务，缺乏对科学过程本身的机制性建模与元分析能力。本文提出以“模拟”与“工具”为核心的任务分类法，系统梳理了AI代理在引用网络建模、同行评审动态及假设生成中的架构与评估现状。该综述厘清了AI代理作为科学研究对象时的自反性偏差，但其在偏好优化与人类判断对齐上的技术缺口仍未解决。

】

---

【Are Large Language Models Reliable Reviewers? A Benchmark for Error Detection in Financial Documents ｜金融文档错误检测基准

研究机构：复旦大学、中国人民大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_447dfe7c1661)

> 金融文档中的细微错误会导致巨额经济损失与合规风险，但现有大语言模型（LLMs）在长文本跨段落逻辑一致性检测上表现极不稳定。传统基准聚焦于短文本语法或通用问答，无法评估模型在复杂金融语境下的深层推理能力，本文通过构建首个针对长文档金融错误检测的基准FinED-Bench填补这一空白。该基准采用半自动错误注入管道，涵盖973份真实文档与4123个标注错误实例，实验表明即便最强模型GPT-4o的整体F1仅为48.34%，且随文档长度增加性能急剧衰减。这一发现揭示了当前LLM在金融审计场景下的可靠性瓶颈，但其错误注入机制是否完全模拟真实人类错误分布仍存疑。

】

---

【AutoUE: Automated Generation of 3D Games in Unreal Engine via Multi-Agent Systems ｜基于多智能体协同的虚幻引擎3D游戏自动生成

研究机构：北京理工大学、北京交通大学

作者：Lei Yin、Wentao Cheng、Zhida Qin 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4b4091b8b899)

> 在商业游戏引擎中端到端生成可玩的3D游戏，核心难点在于资产检索、场景布局与代码逻辑的跨子系统一致性。现有方法多聚焦单一组件或依赖人工检查，缺乏对动态游戏行为的自动化验证。AutoUE通过五个协同智能体，结合检索增强生成（RAG）与模块化代码框架，实现了从自然语言描述到可测试3D游戏的完整闭环。该工作验证了多智能体架构在复杂引擎工作流中的可行性，但其评估基准的规模与跨引擎泛化能力仍存疑。

】

---

【BizCompass: Benchmarking the Reasoning Capabilities of LLMs in Business Knowledge and Applications ｜商业大模型基准 BizCompass：从学科知识到角色应用的映射诊断

作者：Jianing Hao、Yuhe Wu、Yuanjian Xu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17305)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7a37c1cedee5)

> 现有金融大模型基准多聚焦于单一数值推理或孤立问答，无法诊断模型在真实商业场景中失效的根本原因。BizCompass 通过构建覆盖金融、经济、统计与运营管理的四学科知识层，并映射至分析师、交易员、顾问三类角色应用层，建立了理论能力与实践表现的诊断桥梁。其核心做法是提取学术文献中的方程、命题等知识单元，经六步流水线生成可溯源的评估任务。该基准揭示了模型规模与商业表现的非线性关系，但缺乏对动态市场实时性的模拟，其静态评估结论在高频交易场景下的有效性存疑。

】

---

【Can LLMs Estimate Student Struggles? Human-AI Difficulty Alignment with Proficiency Simulation for Item Difficulty Prediction ｜人机难度对齐诊断：LLM解题能力与认知感知的解耦分析

研究机构：美国卡内基梅隆大学、美国纽约州立大学布法罗分校

作者：Ming Li、Han Chen、Yunze Xiao 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.18880)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.18880)

> 教育评估中的冷启动问题要求在新题缺乏真实作答数据时估计其难度参数。现有直接回归方法受限于表面语言特征与深层认知负荷的解耦，而基于大语言模型（LLM）的模拟作答虽符合项目反应理论（Item Response Theory, IRT）假设，却面临模型自身高解题能力与人类低能力学生认知局限之间的系统性偏差。本文切入点在于解构“解题能力”与“难度感知”的内在关联，通过双视角实证检验零样本LLM能否忠实模拟人类认知挣扎。其价值在于揭示了通用LLM在难度预测上的系统性失效机制，但零样本诊断结论是否适用于微调后的专用模型仍存疑。

】

---

【CheMM-R1: Enhancing Chemical Structure Recognition and Elucidation with Reasoning Multimodal Large Language Models ｜化学多模态推理基准与强化学习模型

研究机构：澳大利亚悉尼科技大学、澳大利亚新南威尔士大学

作者：Liting Huang、Zhihao Zhang、Shoujin Wang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9a89518a2571)

> 化学结构解析需整合2D结构图与多种光谱数据，但现有模型要么仅处理单一模态，要么缺乏显式推理步骤，导致无法可靠地从光谱反推分子结构。本文切入点在于构建首个要求多步视觉推理与五类光谱联合解析的基准CheMM-Bench，并基于此训练专用模型。方法上，采用冷启动知识注入结合领域适配的Group Relative Policy Optimization (GRPO) 强化学习框架。该工作验证了领域专用多模态大语言模型在复杂化学推理上的有效性，但其对光谱图像直接处理的鲁棒性及与专用化学模型的公平对比仍存疑。

】

---

【Chinese Court Simulation with LLM-Based Agents System ｜全流程庭审模拟与双维评估框架

研究机构：清华大学

作者：Kaiyuan Zhang、Jiaqi Li、Yueyue Wu 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_17c3e52839ed)

> 法律判决预测长期面临“黑盒判决”与“程序合规”的割裂，现有方法仅模拟辩论片段，缺乏对完整审判流程的还原及过程质量的量化标准。SimCourt 基于中国刑事审判法定程序，构建包含调查、举证、辩论等五阶段的多智能体模拟框架，并引入记忆与策略模块以维持角色一致性。该框架通过生成完整庭审记录而非直接输出判决，实现了判决预测与过程评估的双重目标。实验表明其判决命中率优于基线，但样本量局限与通用模型依赖使其在复杂法域泛化能力上存疑。

】

---

【Datasets for Scientific Literature Understanding: A Survey ｜科学文献理解数据集综述

研究机构：中国科学院、中国科学院大学

作者：Yuanzhe Zhang、Xun Zhao、Maodi Hu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2b37f13faa67)

> 科学文献理解旨在将非结构化学术产出转化为可计算的知识基础设施，但现有资源分散且缺乏统一分类标准，导致模型训练与评估缺乏系统性参照。本文切入点在于构建首个覆盖结构、文本、多模态及预训练指令微调的四层数据集分类体系，系统梳理了从底层感知解析到高层语义推理的数据资源全景。该工作通过静态属性映射而非动态性能评测，为领域提供了数据选型的概念脚手架。其价值在于填补了资源索引的空白，但缺乏对数据集间依赖关系及动态演化能力的量化评估，难以直接指导智能体工作流的数据构建。

】

---

【EvoMD-LLM: Learning the Language of Species Evolution in Reactive Molecular Dynamics ｜演化分子动力学大语言模型

研究机构：上海交通大学

作者：Zhichen Tang、Zhengzheng Dang、Yulin Chen 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.29394)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.29394)

> 现有大语言模型擅长处理静态分子结构，却难以捕捉反应体系中随时间演化的动力学因果逻辑。主流方法依赖外部模拟器或数值回归，无法在离散符号空间内内化连续物理过程的“语法”。EvoMD-LLM 将分子动力学轨迹重构为包含时长信息的符号事件序列，通过自回归语言建模实现反应路径预测。该框架在单一反应体系上展示了有效的时序推理能力，但其泛化边界与物理机制的可解释性仍存疑。

】

---

【Feedback to Reasoning: LLM-Assisted Molecular Optimization with Domain Feedback and Historical Reasoning ｜反馈驱动推理与历史知识积累

作者：Wenhan Gao、Xiran Fan、Chin-Chia Michael Yeh 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_138783dcf576)

> 分子优化是一个依赖专家迭代反馈的经验驱动过程，但现有LLM辅助方法要么忽略历史经验，要么仅传递静态动作指令，导致模型无法从失败中反思并复用化学洞察。F2R通过引入领域反馈驱动的自我反思机制与动态结构-活性关系（SAR）知识库，将LLM从被动生成器转变为能积累推理经验的智能体。该方法在16个单目标小分子优化任务中，使用GPT-4.1时于15个任务取得最高成功率。其价值在于证明了反馈推理优于动作引导，但SAR提取的准确性与错误知识的累积风险仍是未解之题。

】

---

【Fin-Bias: Comprehensive Evaluation for LLM Decision-Making under human bias in Finance Domain ｜金融长文本决策中的人类偏见从众行为评估与去偏

研究机构：美国罗格斯大学、加拿大多伦多大学

作者：Xiaoyu Hu、Jinman Zhao

论文原文见 [arXiv](https://arxiv.org/abs/2605.09106)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e321e457d9a6)

> 金融决策依赖长文本分析，但现有基准多聚焦短期价格预测或短文本情感，忽视了分析师报告中系统性乐观偏见对大语言模型（LLM）独立判断的干扰。本文切入点在于量化 LLM 在长上下文中的“从众效应”，即模型倾向于采纳显式人类观点而非独立推理。通过构建包含 8,868 份长报告的数据集，并引入评级移除与伪造评级扰动，结合词典过滤与直接偏好优化（DPO）进行去偏。该工作揭示了前沿模型在金融决策中缺乏独立性的风险，但受限于单智能体架构，其结论在多智能体协作场景下的普适性尚存疑。

】

---

【Fin-STAR: Structure-as-Semantics to Resolve Implicitness in Financial Retrieval ｜结构语义化金融检索

作者：Yu Zou、Yan Chen、Lida He 等 15 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_796cedbf2523)

> 金融文档中的关键事实往往依赖全局层级结构而非局部文本，导致传统检索增强生成（RAG）系统因切断片段与层级的联系而产生语义歧义。现有方法要么通过摘要牺牲精度，要么忽略层级容器语义，无法在高风险场景下保证事实一致性。Fin-STAR 通过将文档层级转化为内在语义知识，利用双门控语义单元构建与虚拟节点合成，在索引阶段显式化隐含线索。该框架在 FinTierQA Gold 基准上验证了结构注入对数值精度的必要性，但其对上游解析准确性的依赖及跨市场泛化能力仍存疑。

】

---

【FinMaster: A Holistic Benchmark for Full-Pipeline Financial Management with Large Language Models ｜全流水线财务管理工作流基准

研究机构：香港理工大学、香港中文大学

作者：Junzhe Jiang、Chang Yang、Aixin Cui 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2538b47c868f)

> 现有金融大语言模型（LLM）评估基准多局限于静态报表分析，无法覆盖从原始交易到报表生成的完整工作流，导致模型在记账与审计环节的能力盲区未被量化。FinMaster 通过构建符合通用会计准则（GAAP）的合成数据模拟器与 183 项任务套件，首次实现了对财务全流水线能力的端到端自动评估。实验揭示 LLM 在基础任务上准确率超 90%，但在复杂多步推理中骤降至 40%，暴露了数值精度与逻辑一致性的结构性缺陷。该基准填补了工作流级评估空白，但合成数据对真实长尾异常模式的覆盖度仍存疑。

】

---

【FinSafetyBench: Evaluating LLM Safety in Real-World Financial Scenarios ｜金融大语言模型安全红队基准

研究机构：北京航空航天大学、南方科技大学

作者：Yutao Hou、Yihan Jiang、Yuhan Xie 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a24b4b2b7061)

> 金融大语言模型（Large Language Models, LLMs）在部署中面临被诱导生成非法操作指南的合规风险，现有通用安全基准缺乏金融场景的细粒度覆盖，且依赖合成数据导致评估失真。FINSAFETYBENCH 基于真实司法案例与 CFA 伦理题构建双语红队基准，通过三种越狱攻击量化模型拒绝非法请求的能力。该基准揭示了开源模型在金融越狱下的极高脆弱性，但提示级防御的失效边界仍需更深层机制解释。

】

---

【GLA: Grounding Large Language Models in Molecular Hierarchy for Chemical Understanding ｜几何语言对齐

作者：Yingxu Li、Jingjie Zeng、Zekun Wang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e970a4c75939)

> 分子-文本对齐长期受困于线性序列丢失拓扑层级，导致模型无法区分药效团核心与侧链修饰。现有方法将分子压缩为单一欧氏嵌入，造成“几何同质化”，混淆了结构语义。GLA通过混合曲率编码器解耦骨架与侧链，利用双视图对比学习实现细粒度对齐。该方法在检索与描述任务上验证了几何解耦的有效性，但其对大规模属性预测的增益有限，且未解决3D构象缺失问题。

】

---

【H-MAS: Hierarchical Multi-Agent Scheduling for Multi-Tenant LLM Serving ｜分层多智能体调度

研究机构：北京师范大学、东南大学

作者：Yuhan Liu、Cong Xu、Qi Jia 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4f086419b3f5)

> 多租户大语言模型服务（MaaS）面临非平稳负载下的服务质量（QoS）不稳定问题，现有固定策略调度器无法同时应对毫秒级突发、分钟级漂移与小时级结构变化。本文指出单一策略在时间尺度上的错配是QoS波动的根源，提出H-MAS分层多智能体调度器，通过解耦慢速策略选择与快速执行调节实现自适应控制。该架构在Azure生产轨迹上验证了Goodput提升1.2×–3.0×的有效性，但其LLM决策延迟与保形校准的泛化边界尚存疑。

】

---

【JudgeMeNot: Personalizing Large Language Models to Emulate Judicial Reasoning in Hebrew ｜法官推理个性化大语言模型

研究机构：以色列内盖夫本-古里安大学

作者：Itay Razumenko、Arnon Sturm、Nir Grinberg

论文原文见 [arXiv](https://arxiv.org/abs/2604.18041)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a7626f12bbf2)

> 法律判决预测长期将法官视为可互换的决策黑盒，忽略了司法推理中个体化的逻辑偏好与修辞结构。现有生成式模型虽能输出判决结果，却难以复现特定法官的“认知指纹”，且缺乏针对低资源语言的个性化验证。本文通过合成-有机对齐管道生成指令数据，结合链式LoRA微调，在希伯来语低资源场景下实现了法官级推理模拟。该框架证明了参数高效微调在捕捉个体推理风格上的可行性，但作者识别准确率的随机性暴露了风格模仿与身份区分之间的深层张力。

】

---

【Less is More: Knowledge-Aware Compression for Long Legal Judgment Prediction ｜知识感知压缩

研究机构：南开大学、哈尔滨工业大学

作者：Fanghao Lou、Qiqi Wang、Guanyu Chen 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cdb84f613065)

> 法律判决预测（Legal Judgment Prediction, LJP）在处理长文本案件事实时，常因大语言模型（LLM）的二次方计算复杂度与关键法律要素稀释而失效。现有架构优化或通用文本压缩方法难以兼顾法律逻辑连贯性与推理效率。本文提出知识感知压缩（Knowledge-Adaptive Compression, KAC）框架，利用法条知识引导语义单元筛选，实现高效长文档推理。该方法在跨法域数据集上显著提升了预测精度并降低了计算成本，但其对法律知识库静态性的依赖及阈值设定的普适性仍存疑。

】

---

【LLMs as Lab Engineers: A Benchmark for Analytical Method Lifecycle Management ｜分析化学全生命周期评估基准

研究机构：美国印第安纳大学、美国伍斯特理工学院

作者：Xiaoyi Chen、Mahsa Monshizadeh、Chaoqi Zhang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_890015eda920)

> 现有LLM化学基准多聚焦于静态知识问答或分子性质预测，无法覆盖实验室仪器故障诊断等动态、开放式的实操场景。本文通过构建涵盖仪器就绪、系统适用性、方法开发与故障排除的分析化学全生命周期基准，并引入专家Rubric评估，发现通用大模型在复杂诊断任务中表现优于专用微调模型，且检索增强生成（RAG）与人类引导思维链（CoT）能显著提升性能。这一发现挑战了“领域专用预训练必然更优”的直觉，但受限于小样本规模与单一仪器类型，其结论的普适性仍需更大规模验证。

】

---

【MCLE-Mol: Empowering LLM with Molecular Comprehension and Low-Cost Continual Evolution for Interpretable Property Prediction ｜分子性质预测中的语义鸿沟与可解释性：MCLE-Mol 框架

作者：Zhili Pu、Lantian Zhang、Hao Duan 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f4f0ce91506f)

> 导读 分子性质预测（Molecular Property Prediction, MPP）旨在从分子结构推断生物活性或毒性，是AI辅助药物发现的核心环节。图神经网络（Graph Neural Networks, GNNs）虽精度高但缺乏可解释性，而大语言模型（Large Language Models, LLMs）虽能生成解释却常因语义鸿沟导致幻觉与性能下降。MCLE-Mol通过注入机器学习（Machine Learning, ML）模型产生的子结构归因值，并引入上下文校准子结构归因规则（Context-Calibrated Substructure Attribution Rules, CCSAR）动态修正统计偏差，实现了性能与可解释性的平衡。该框架在BACE和BBBP上超越了部分专用GNN模型，但在HIV等大规模数据集上仍落后于全量训练的专家模型，其规则库的长期演化稳定性尚待验证。

】

---

【MolSafeEval: A Benchmark for Uncovering Safety Risks in AI-Generated Molecules ｜分子生成安全基准

研究机构：浙江大学、英国牛津大学

作者：Tong Xu、Xinzhe Cao、Zhihui Zhu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.00464)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.00464)

> 现有分子生成基准聚焦于新颖性与性质优化，却系统性地忽视了生成物可能携带的毒性或化学危害。这一盲区源于安全数据分散于监管标准与毒理数据库，难以被单一预测器覆盖。MolSafeEval 通过构建整合 83,925 个危险化合物的知识图谱，结合大语言模型（Large Language Model, LLM）推理，首次实现了跨任务类型的系统性安全评估。该框架填补了安全维度的空白，但其依赖已知危险分子相似性的机制，对全新毒性机制的捕捉能力存疑。

】

---

【MotifAgent: Learning Molecular Assembly through Multi-Agent Collaboration for Chemical Language Understanding ｜基团组装多智能体强化学习框架

研究机构：中国人民大学

作者：Jinjia Feng、Wenda Wang、Zhewei Wei

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9408604be095)

> 现有LLM处理分子时，将SMILES视为字符序列进行静态模式匹配，无法理解基团间动态连接规则，导致生成结构缺乏化学有效性。本文切入点在于将分子组装重构为多智能体协商问题，通过共享LLM骨干的基团代理在集中式训练与分布式执行框架下显式学习连接规则。具体做法是结合Set-based行为克隆与拓扑感知奖励塑形，使模型在重建与生成模式下均能动态构建2D拓扑。该框架在通用LLM基线上超越了专用模型，但其性能上限受限于2D拓扑输入，未验证3D构象约束下的泛化能力。

】

---

【RealFin: How Well Do LLMs Reason About Finance When Users Leave Things Unsaid? ｜金融大语言模型逻辑完备性评估

研究机构：英国纽卡斯尔大学

作者：Yuyang Dai、Yan Lin、Zhuohan Xie 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.07096)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.07096)

> 金融决策的核心风险不仅在于计算错误，更在于在信息缺失时强行给出结论。现有金融基准普遍假设问题前提完备，导致模型“过度承诺”行为无法被检测。本文通过系统性移除题目关键前提，构建双语基准 REALFIN，评估模型识别逻辑欠定问题的能力。该工作揭示了通用模型在中文场景下的严重退化及金融专用模型的多步推理盲区，但缺乏对模型内部决策机制的归因分析。

】

---

【REAP: Towards Effective Training-Free Chemical Reasoning with Explicit Atomic Priors ｜显式原子先验驱动的无训练化学推理

研究机构：香港科技大学、南京大学

作者：Mingxu Zhang、Dazhong Shen、Qi Zhang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b7f337270ce0)

> 大语言模型（LLM）在分子科学中面临的核心困境是缺乏细粒度化学先验，导致推理依赖表面结构启发式而非物理化学约束。现有训练式方法将知识固化于参数中，存在更新僵化与通用能力丧失的风险，而传统检索增强生成（RAG）仅依赖粗粒度实例匹配，缺乏证据支撑。REAP通过构建首个原子级文本知识库，并设计任务感知的先验选择与证据获取机制，使冻结LLM能够基于显式物理化学属性进行推理。该框架在性质预测任务上超越了无训练基线并逼近训练式模型，但其推理忠实度与复杂生成任务的适用性仍存疑。

】

---

【Same Claim, Different Judgment: Benchmarking Scenario-Induced Bias in Multilingual Financial Misinformation Detection ｜场景诱导偏差基准：多语言金融虚假信息检测中的行为稳定性审计

研究机构：英国曼彻斯特大学、美国史蒂文斯理工学院

作者：Zhiwei Liu、Yupeng Cao、Yuechen Jiang 等 25 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9aaf551fa549)

> 金融虚假信息检测旨在区分真实与虚假的财经声明，但现有基准多局限于单一语言与静态语境，无法捕捉模型在复杂市场角色、地域文化及身份背景下的判断漂移。主流方法将检测简化为二分类任务，忽视了场景提示对决策边界的系统性扭曲，导致模型在零售投资者或新兴市场语境下出现显著的行为偏差。本文构建了 MFMD-Scen 基准，通过注入角色、地域与身份三维场景变量，量化 22 个主流大语言模型（LLM）在四国语言下的判断偏移。该工作揭示了模型在识别真实陈述时的保守倾向及低资源语言下的偏差放大效应，但场景注入是否完全隔离了语言难度与认知偏差的混淆效应，仍存疑。

】

---

【SciImpact: A Multi-Dimensional, Multi-Field Benchmark for Scientific Impact Prediction ｜科学影响力多维预测基准

研究机构：美国德州农工大学、加拿大滑铁卢大学

作者：Hangxiao Zhu、Yuyu Zhang、Ping Nie 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17141)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a699f1ab3923)

> 科学文献影响力长期被简化为引用计数，导致对奖项、专利及代码采纳等关键维度的评估缺失。现有单一指标预测模型无法捕捉跨领域、多模态证据下的复杂影响机制，且缺乏统一的多维评估环境。本文构建了覆盖19个学科、7个影响维度的对比对基准，并通过多任务指令微调验证了小模型在该任务上的有效性。该工作填补了多维影响力评估的空白，但其对比对构建策略可能引入选择偏差，且缺乏与传统机器学习基线的直接对比。

】

---

【Seeing Beyond Words: MatVQA for Challenging Visual-Scientific Reasoning in Materials Science ｜材料科学多模态视觉推理基准 MatVQA

研究机构：加拿大蒙特利尔大学、加拿大魁北克人工智能研究所

作者：Sifan Wu、Huan Zhang、Yizhan Li 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c7ffc0b3def7)

> 现有材料科学基准多依赖纯文本问答，无法评估模型对显微图像、衍射图谱等视觉证据的细粒度解析能力，导致模型可能通过阅读图注而非观察图像本身来回答科学问题。MatVQA 通过自动化流水线从 arXiv 论文中提取推理链，并迭代消除语言与图注捷径，强制模型依赖低层视觉感知。该基准揭示了当前多模态大语言模型在科研级视觉推理上的显著短板，但其自动化生成流程是否引入新的偏差，以及领域微调模型失效的根本原因，仍需进一步验证。

】

---

【SudokuFill: A Multi-Agent Progressive Filling Framework for Document-Level Scientific Information Extraction ｜科学信息抽取的渐进式多智能体填充框架

研究机构：中国科学院、中国科学院大学

作者：Yang Li、Yajiao Wang、Yu Zhang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_83812d28955b)

> 科学文献挖掘旨在将非结构化文本转化为可计算的知识基础设施，但传统“局部抽取后组装”范式在长文档中因字段隔离导致全局关联断裂。现有方法依赖静态知识图谱或单次生成，难以利用高置信度结果作为内部监督来约束后续不确定字段。本文提出 SudokuFill，将文档级科学信息抽取重构为类似数独的渐进填充问题，通过全局状态复用与多智能体辩论实现约束传播。该框架在疫苗佐剂基准上达到 51.83% 的整体准确率，并验证了 7B 模型超越 GPT-4o 的架构补偿效应，但其泛化性受限于自建基准的领域特异性。

】

---

【Take Out Your Calculators: Estimating the Real Difficulty of Question Items with LLM Student Simulations ｜基于LLM学生模拟的数学题难度估计

研究机构：美国马里兰大学帕克分校

作者：Christabel Acquaye、Yi Ting Huang、Marine Carpuat 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_86445c9bd9ce)

> 教育评估中题目难度校准依赖高昂的现场测试，而直接文本回归方法无法捕捉认知负荷与作答者能力的交互效应。本文切入点在于利用开源大语言模型（LLM）扮演不同能力水平的学生，通过生成个体化响应数据来重构项目反应理论（IRT）参数。具体做法是提示LLM模拟“课堂”作答，拟合IRT模型以估计难度，并验证其与真实NAEP数据的对齐度。该工作证明了零样本模拟在纯文本数学题上可达到0.82的相关性，但其对低能力学生错误模式的模拟保真度及身份标识的作用机制仍存疑。

】

---

【ToxReason: A Benchmark for Mechanistic Chemical Toxicity Reasoning via Adverse Outcome Pathway ｜基于不良结局通路的毒性机理推理基准

研究机构：韩国高丽大学

作者：Jueon Park、Wonjune Jang、Chanhwi Kim 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.06264)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.06264)

> 现有分子毒性预测模型仅关注结构到标签的映射，忽略了毒性产生的生物因果链条，导致预测结果缺乏可解释性与可靠性。本文切入点在于引入不良结局通路（Adverse Outcome Pathway, AOP）框架，将毒性评估从结果预测转化为从分子启动事件到器官级不良结局的因果推理任务。通过整合AOP-Wiki、ChEMBL与CTD数据构建193个化合物的推理基准，并采用强化学习优化因果一致性，使4B参数模型在预测与推理上超越更大规模模型。该工作验证了机理推理对毒性预测的增益，但受限于AOP覆盖范围与LLM评估的主观性，其结论在复杂真实场景中的普适性仍存疑。

】

---

【What Factors Affect LLMs and RLLMs in Financial Question Answering? ｜金融问答中推理大语言模型性能瓶颈的系统性归因

研究机构：安徽大学、华中科技大学

作者：Peng Wang、Xuesi Hu、Jiageng Wu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2507.08339)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7c95ec277c91)

> 金融问答任务要求模型在复杂语境下执行多步数值推理，传统大语言模型（LLM）常因推理链过短导致计算错误。现有提示工程与智能体框架虽能提升LLM表现，但对已具备长思维链能力的推理大语言模型（RLLM）增益有限，且多语言对齐策略在RLLM上甚至产生负迁移。本文通过控制变量实验，系统解构提示方法、智能体框架与多语言对齐对LLM/RLLM性能的影响机制，揭示长思维链是区分两类模型性能瓶颈的核心变量。该研究厘清了推理时策略的适用边界，但未能验证训练式微调能否替代推理时策略解决数值幻觉问题。

】
