# ACL-Findings2026 · 大语言模型评估框架与基准方向论文汇编

> 本方向共 4 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Curriculum Learning based Hierarchical Scoring and Analysis Framework for Question Answering Task Evaluation ｜课程学习层级化问答评估框架

研究机构：北京大学、新加坡国立大学

作者：Qiong Wu、Tan Yue、Jianxin Liang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f6d62580fd63)

> 大语言模型在问答任务中的评估面临成本高昂与错误诊断缺失的双重困境，现有规则匹配方法语义理解不足，而通用大模型评判器虽准确但延迟高且无法定位具体错误类型。HiEval 通过两阶段课程学习训练一个 4B 参数的小模型，先掌握三级评分能力，再扩展至五类错误归因，以零 API 成本和 25 倍于 GPT-5 的推理速度实现了超越大模型的细粒度诊断精度。该框架验证了小模型在特定评估子任务上替代大模型的可行性，但其泛化边界与标注一致性仍需更严格的跨域验证。

】

---

【STaD: Scaffolded Task Design for Identifying Compositional Skill Gaps in LLMs ｜脚手架任务设计

研究机构：IBM研究院

作者：Sungeun An、Swanand Ravindra Kadhe、Shailja Thakur 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18177)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18177)

> 现有LLM评估依赖聚合准确率，掩盖了模型在组合推理中的具体失败点，导致无法区分“缺乏单一技能”与“技能协调失效”。STaD通过引入认知科学中的脚手架机制，将基准任务分解为子任务并逐步提供中间答案，以定位模型的最小支持需求。该方法在三个推理基准上揭示了不同模型具有截然不同的技能瓶颈分布，但缺乏与统计测量模型的直接对标，其诊断结论的泛化性仍存疑。

】

---

【Stop Guessing When to Stop Testing: Efficient Model Evaluation with Just Enough Data ｜序贯测试驱动的自适应模型评估

研究机构：IBM研究院

作者：Ofir Arviv、Kristjan Greenewald、Yotam Perlitz 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.08522)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.08522)

> 大语言模型与视觉语言模型（VLM）评估面临固定样本量导致的计算浪费或统计效力不足的双重困境，传统静态基准无法动态匹配不同评估目标的可靠性需求。本文切入点在于引入临床试验中的组序贯测试（Group Sequential Testing, GST）范式，通过动态停止规则在统计显著性与计算成本间实现透明权衡。该方法利用Pocock消耗函数校正多重比较误差，支持单模型评分、成对比较及排名任务。其价值在于提供了无需历史数据校准的严格统计保证，但实验仅局限于VLM基准，未验证其在纯文本LLM或动态生成基准上的泛化能力。

】

---

【When and What to Ask: AskBench and Rubric-Guided RLVR for LLM Clarification ｜交互澄清能力评估与训练

作者：Jiale Zhao、Ke Fang、Lu Cheng

论文原文见 [arXiv](https://arxiv.org/abs/2602.11199)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.11199)

> 大语言模型在医疗、教育等高风险场景中常面临用户输入信息缺失或包含错误前提的困境，但现有基准仅评估单轮静态问答，无法衡量模型“何时问”与“问什么”的交互决策能力。传统提示工程框架依赖特定任务启发式，难以泛化且缺乏对澄清质量的细粒度监督。本文提出 AskBench 基准与基于评分标准的强化学习（Rubric-Guided RLVR）训练方案，将标准问答对转化为带显式检查点的多轮交互任务，通过奖励机制引导模型在回答前主动获取关键信息或纠正错误前提。该方法在提升澄清覆盖率的同时保持了单轮问答性能，但评估协议依赖单一裁判模型且未提供统计置信区间，其泛化边界尚待验证。

】
