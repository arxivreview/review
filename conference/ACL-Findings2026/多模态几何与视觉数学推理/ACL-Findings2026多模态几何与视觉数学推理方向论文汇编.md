# ACL-Findings2026 · 多模态几何与视觉数学推理方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【EDU-CIRCUIT-HW: Evaluating Multimodal Large Language Models on Real-World University-Level STEM Student Handwritten Solutions ｜大学级STEM手写解题评估基准

研究机构：美国弗吉尼亚理工大学

作者：Weiyu Sun、Liangliang Chen、Yongnuo Cai 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.00095)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.00095)

> 多模态大语言模型（MLLM）在低利害日常视觉任务中表现优异，但面对包含复杂公式、手绘图表与交织逻辑的大学级STEM手写解题时，其视觉感知可靠性面临严峻挑战。现有教育评估基准多聚焦孤立元素或低难度K-12场景，且仅通过下游自动评分结果间接评估，掩盖了上游识别错误对高精度评分的级联破坏。本文构建EDU-CIRCUIT-HW基准，通过专家验证的逐字转录与细粒度错误分类，量化识别错误对自动评分的级联影响。该工作揭示了当前MLLM在手写STEM理解上的深层缺陷，但受限于单一课程领域与特定评分标准，其结论向其他STEM学科泛化的能力尚待验证。

】

---

【GeometryZero: Advancing Geometry Solving via Group Contrastive Policy Optimization ｜几何辅助构造的条件策略学习

研究机构：复旦大学、浙江大学

作者：Yikun Wang、Yibin Wang、Dianyi Wang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_138b6be39be3)

> 导读 几何推理的核心难点在于模型常无法判断何时需要辅助线，盲目构造反而引入错误。现有强化学习方法对工具调用施加无差别正向奖励，导致模型在简单问题上过度构造。本文提出组对比策略优化（Group Contrastive Policy Optimization, GCPO），通过对比有/无辅助线两组回滚的准确率差异，动态决定辅助奖励的正负号。该方法在7B模型上实现了Geometry3K 78.81%的准确率，但其在高难度长程推理上的表现仍显著低于神经符号系统，暴露出纯语言模型在复杂几何证明中的局限。

】

---

【Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language ｜统一形式语言下的几何图解析

研究机构：中国科学院、中国科学院大学

作者：Peijie Wang、Ming-Liang Zhang、Jun Cao 等 13 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.11600)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11600)

> 多模态大模型在几何推理中常因无法准确提取图形中的点、线、面等基础元素而陷入幻觉，导致后续逻辑推导建立在错误前提之上。现有方案多聚焦平面几何或依赖端到端黑盒推理，缺乏对立体几何的严格形式化定义与可验证的解析训练机制。本文通过构建覆盖平面与立体几何的统一形式语言及大规模数据集 GDP-29K，并引入基于规则验证的强化学习，实现了高精度的图形符号化转换。该工作填补了立体几何解析的数据空白，但其作为感知前端的定位，尚未解决解析结果与复杂符号推理引擎的动态耦合问题。

】
