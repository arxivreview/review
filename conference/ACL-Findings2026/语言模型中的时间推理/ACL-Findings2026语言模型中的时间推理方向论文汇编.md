# ACL-Findings2026 · 语言模型中的时间推理方向论文汇编

> 本方向共 10 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AdapTime: Enabling Adaptive Temporal Reasoning in Large Language Models ｜自适应时间推理

研究机构：香港城市大学、西湖大学

作者：Yimin Deng、Yejing Wang、Zhenxi Lin 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.24175)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.24175)

> 时间推理任务要求模型在静态文档中解析时间约束并定位事实，但现有方法依赖固定流水线或外部工具，导致简单问题过度处理、复杂问题推理不足。AdapTime 通过 LLM Planner 动态选择“重构、重写、审查”三个推理动作，实现了无外部依赖的自适应推理。该方法在 DeepSeek-V3 上将 TempReason-L3 的 F1 从 48.3 提升至 53.2，证明了动态规划的有效性，但其性能上限仍受限于骨干模型自身的时间感知能力。

】

---

【M-TRACE: Detecting and Mitigating Time-Anchor Drift via Step-wise Conflict Checking in Temporal Reasoning ｜多智能体时间推理框架 M-TRACE：基于状态时间线的冲突检测与锚点漂移抑制

研究机构：南开大学

作者：Danyu Huang、Jiayuan Jiang、Yao Zhang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f0e7bf94e1ad)

> 时间推理的核心困境在于，大语言模型（LLM）的参数化知识是静态的，而现实世界是动态的，当模型结合外部检索证据进行多步推理时，内外部知识的时间不一致性会累积并导致推理失败。现有方法通常假设知识源在时间上是一致的，或仅将冲突视为静态事实差异，无法处理由知识演化引发的动态时间冲突。M-TRACE 通过构建独立的内部状态时间线作为参照系，逐步比对内外部证据并生成结构化冲突报告，从而显式检测并抑制时间锚点漂移。该框架在自建基准上显著提升了推理准确性，但其对骨干模型时间理解能力的强依赖，限制了其在弱模型上的泛化潜力。

】

---

【MINED: Probing and Updating with Multimodal Time-Sensitive Knowledge for Large Multimodal Models ｜多模态时间敏感知识基准与更新

研究机构：中国科学技术大学、山东大学

作者：Kailin Jiang、Ning Jiang、Yuntao Du 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.19457)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_311dbb4ef964)

> 大语言模型（LLM）与大视觉语言模型（LMM）的参数化知识是静态的，无法实时追踪现实世界事实的动态演变，导致在处理时效性查询时产生幻觉或过时输出。现有基准多聚焦于文本逻辑推理或静态视觉问答，缺乏对“视觉实体属性随时间变化”这一多模态时效性问题的系统性评估。MINED 通过构建包含 2,104 个样本、覆盖 6 个维度的基准，量化了 LMM 在时间敏感知识上的认知、感知与鲁棒性缺陷，并验证了知识编辑在单点更新场景下的可行性。该工作填补了多模态时效性评估空白，但仅验证了单点编辑效果，未解决多模态知识编辑的泛化性与长期稳定性问题。

】

---

【RAG or Learning? Understanding the Limits of LLM Adaptation under Continuous Knowledge Drift in the Real World ｜连续知识漂移下的时序一致推理

研究机构：清华大学、美国伊利诺伊大学厄巴纳-香槟分校

作者：Hanbing Liu、Lang Cao、Yang Li

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3329e3acb532)

> 大语言模型（LLM）因预训练数据截止日固定，无法感知2024年后的世界状态变化，导致在回答动态事实时出现过时或时序矛盾。现有检索增强生成（RAG）仅做静态文本匹配，缺乏对事件演化轨迹的结构化建模，难以区分同一实体在不同时间点的状态。本文提出Chronos框架，通过构建事件演化图（EEG）将检索到的时间戳事实组织为显式时序拓扑，实现无需参数更新的动态推理。该方法在自建基准上显著优于标准RAG，但依赖高质量外部知识库，且未验证在长文档非结构化场景下的泛化能力。

】

---

【Regret-Now: A Physics-Inspired Regret Framework for Temporal Knowledge Graph Question Answering with LLMs ｜基于最小势能原理的时序知识图谱问答框架

研究机构：南开大学

作者：Danyu Huang、Yao Zhang、Jun Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_69a4e4eacf29)

> 时序知识图谱问答（TKGQA）要求模型在动态演化的知识结构中执行多步推理，但大语言模型（LLM）常因中间步骤的逻辑断裂导致级联错误，且现有自校正方法依赖主观自评，缺乏客观纠错标准。Regret-Now 将推理过程类比为粒子在势能场中的运动，通过监测语义势能的异常上升实时触发回滚机制，以物理量化指标替代 LLM 的主观反思。该框架在 CronQuestions 和 MultiTQ 上取得了优于 Reflexion 等基线的性能，但其依赖外部嵌入模型计算势能，且未与最新神经符号 SOTA 对比，其通用性存疑。

】

---

【Static Models, Dynamic World: A Unified Perspective on Temporal Perception in Large Language Models ｜静态参数与动态世界的信息论解耦

研究机构：北京理工大学

作者：Chenhao Li、Dandan Song、Changzhi Zhou 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_73478210576b)

> 大语言模型（LLM）在动态世界中面临静态参数与实时事实的结构性错位，导致时间推理失效。现有综述多聚焦于特定任务（如知识图谱或检索增强），缺乏对冻结模型内在时间能力的统一理论视角。本文通过构建基于参数可达性的信息论框架，将时间查询划分为四个独立的信息域，从而系统诊断失败根源并整合缓解策略。该框架提供了清晰的诊断坐标系，但其对复合查询的适用性及外部增强机制的量化边界仍存疑。

】

---

【Temporal Token Matters: Investigating and Interpreting the Consistency of Temporal Ordering in Large Language Models ｜时间排序机制的因果验证与自适应干预

研究机构：北京理工大学

作者：Zhen Yang、Xinyue Zhang、Ping Jian 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_59ef6cabdf11)

> 大语言模型在处理简单事件排序时，常因提问措辞从“before”变为“after”而产生逻辑矛盾，暴露出内部时间推理机制的脆弱性。现有研究多聚焦于外部基准测试或端到端性能提升，缺乏对模型内部因果路径的细粒度解析。本文通过路径修补定位关键注意力头，揭示时间词与结构词的层级分工，并提出基于因果效应的自适应注意力调制方法。该方法在无需微调的情况下同时提升了准确率与一致性，但性能增益幅度有限，且仅在二元排序任务中得到验证。

】

---

【TempTool-R1: Tool-Augmented Reinforcement Learning for Temporal Knowledge Graph Question Answering ｜时序知识图谱问答中的工具增强强化学习

作者：Zicheng Huang、Yajuan Tong、Xinhui Tu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f449900610ea)

> 时序知识图谱问答（TKGQA）旨在回答涉及时间约束的复杂查询，但现有方法在处理多跳推理与隐式时间依赖时普遍失效。本文指出，传统检索增强或提示工程无法保证工具调用顺序符合时序逻辑，导致中间步骤错误累积。TempTool-R1 通过设计顺序敏感的强化学习奖励函数，训练大语言模型（LLM）在推理中显式调用时序工具。该方法在多个基准上显著提升了复杂问题的准确率，但其效果高度依赖特定的工具接口设计，泛化性存疑。

】

---

【TIME: Temporally Intelligent Meta-reasoning Engine for Context Triggered Explicit Reasoning ｜时间触发式推理策略对齐

研究机构：印度科学理工学院

作者：Susmit Das

论文原文见 [arXiv](https://arxiv.org/abs/2601.05300)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05300)

> 推理型大语言模型（LLM）常将显式思考固化为回复开头的长文本块，导致计算冗余、审计困难且无法在回答中途重新校准。现有方案将时间视为待抽取的事实内容，却忽略了时间跳跃作为交互状态突变信号对推理策略的触发作用。本文提出 Time 框架，通过引入时间戳、静默 Tick 事件与可插入的短思考块，结合四阶段课程学习，将显式推理从固定解码风格转化为由情境线索触发的动态控制策略。该框架在私有基准 TimeBench 上显著优于基线，但其对时间元数据的依赖及私有评测的封闭性限制了结论的普适性。

】

---

【Your LLM Agents are Temporally Blind: The Misalignment Between Tool Use Decisions and Human Time Perception ｜多轮代理时间盲性评估与对齐

研究机构：美国马里兰大学帕克分校

作者：Yize Cheng、Arshia Soltani Moakhar、Chenrui Fan 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.23853)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_050e4ebbcd90)

> 多轮大语言模型代理在动态环境中执行任务时，常因忽略消息间的真实时间流逝而做出错误的工具调用决策，这一现象被称为时间盲性。现有评估基准多聚焦于静态时间推理或单轮工具调用准确性，缺乏对“时间流逝如何影响决策”的系统量化，导致模型在实时交互中过度依赖过时上下文或冗余调用工具。本文构建了包含76个场景、5592个样本的TicToc数据集，通过注入ISO 8601时间戳并收集人类偏好，量化了模型工具调用决策与人类时间感知的对齐程度。该工作揭示了当前模型在时间感知上的系统性缺陷，但仅验证了后训练对齐的初步有效性，未解决模型内部时间表示的根本缺失。

】
