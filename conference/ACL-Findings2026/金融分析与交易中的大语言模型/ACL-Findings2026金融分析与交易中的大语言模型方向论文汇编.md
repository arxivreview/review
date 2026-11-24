# ACL-Findings2026 · 金融分析与交易中的大语言模型方向论文汇编

> 本方向共 8 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Are Large Language Models Reliable Reviewers? A Benchmark for Error Detection in Financial Documents ｜金融文档错误检测基准

研究机构：复旦大学、中国人民大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_447dfe7c1661)

> 金融文档中的细微错误会导致巨额经济损失与合规风险，但现有大语言模型（LLMs）在长文本跨段落逻辑一致性检测上表现极不稳定。传统基准聚焦于短文本语法或通用问答，无法评估模型在复杂金融语境下的深层推理能力，本文通过构建首个针对长文档金融错误检测的基准FinED-Bench填补这一空白。该基准采用半自动错误注入管道，涵盖973份真实文档与4123个标注错误实例，实验表明即便最强模型GPT-4o的整体F1仅为48.34%，且随文档长度增加性能急剧衰减。这一发现揭示了当前LLM在金融审计场景下的可靠性瓶颈，但其错误注入机制是否完全模拟真实人类错误分布仍存疑。

】

---

【BizCompass: Benchmarking the Reasoning Capabilities of LLMs in Business Knowledge and Applications ｜商业大模型基准 BizCompass：从学科知识到角色应用的映射诊断

作者：Jianing Hao、Yuhe Wu、Yuanjian Xu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17305)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7a37c1cedee5)

> 现有金融大模型基准多聚焦于单一数值推理或孤立问答，无法诊断模型在真实商业场景中失效的根本原因。BizCompass 通过构建覆盖金融、经济、统计与运营管理的四学科知识层，并映射至分析师、交易员、顾问三类角色应用层，建立了理论能力与实践表现的诊断桥梁。其核心做法是提取学术文献中的方程、命题等知识单元，经六步流水线生成可溯源的评估任务。该基准揭示了模型规模与商业表现的非线性关系，但缺乏对动态市场实时性的模拟，其静态评估结论在高频交易场景下的有效性存疑。

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

【RealFin: How Well Do LLMs Reason About Finance When Users Leave Things Unsaid? ｜金融大语言模型逻辑完备性评估

研究机构：英国纽卡斯尔大学

作者：Yuyang Dai、Yan Lin、Zhuohan Xie 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.07096)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.07096)

> 金融决策的核心风险不仅在于计算错误，更在于在信息缺失时强行给出结论。现有金融基准普遍假设问题前提完备，导致模型“过度承诺”行为无法被检测。本文通过系统性移除题目关键前提，构建双语基准 REALFIN，评估模型识别逻辑欠定问题的能力。该工作揭示了通用模型在中文场景下的严重退化及金融专用模型的多步推理盲区，但缺乏对模型内部决策机制的归因分析。

】

---

【Same Claim, Different Judgment: Benchmarking Scenario-Induced Bias in Multilingual Financial Misinformation Detection ｜场景诱导偏差基准：多语言金融虚假信息检测中的行为稳定性审计

研究机构：英国曼彻斯特大学、美国史蒂文斯理工学院

作者：Zhiwei Liu、Yupeng Cao、Yuechen Jiang 等 25 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9aaf551fa549)

> 金融虚假信息检测旨在区分真实与虚假的财经声明，但现有基准多局限于单一语言与静态语境，无法捕捉模型在复杂市场角色、地域文化及身份背景下的判断漂移。主流方法将检测简化为二分类任务，忽视了场景提示对决策边界的系统性扭曲，导致模型在零售投资者或新兴市场语境下出现显著的行为偏差。本文构建了 MFMD-Scen 基准，通过注入角色、地域与身份三维场景变量，量化 22 个主流大语言模型（LLM）在四国语言下的判断偏移。该工作揭示了模型在识别真实陈述时的保守倾向及低资源语言下的偏差放大效应，但场景注入是否完全隔离了语言难度与认知偏差的混淆效应，仍存疑。

】

---

【What Factors Affect LLMs and RLLMs in Financial Question Answering? ｜金融问答中推理大语言模型性能瓶颈的系统性归因

研究机构：安徽大学、华中科技大学

作者：Peng Wang、Xuesi Hu、Jiageng Wu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2507.08339)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7c95ec277c91)

> 金融问答任务要求模型在复杂语境下执行多步数值推理，传统大语言模型（LLM）常因推理链过短导致计算错误。现有提示工程与智能体框架虽能提升LLM表现，但对已具备长思维链能力的推理大语言模型（RLLM）增益有限，且多语言对齐策略在RLLM上甚至产生负迁移。本文通过控制变量实验，系统解构提示方法、智能体框架与多语言对齐对LLM/RLLM性能的影响机制，揭示长思维链是区分两类模型性能瓶颈的核心变量。该研究厘清了推理时策略的适用边界，但未能验证训练式微调能否替代推理时策略解决数值幻觉问题。

】
