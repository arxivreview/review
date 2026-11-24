# ACL-Findings2026 · 通过自我对弈与自我修正实现语言模型的自我改进方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Easy Samples Are All You Need: Self-Evolving LLMs via Data-Efficient Reinforcement Learning ｜易样本引导的自进化强化学习

研究机构：北京大学、南开大学

作者：Zhiyin Yu、Bo Zhang、Qibin Hou 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18639)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18639)

> 大语言模型（LLMs）在数学推理等可验证任务上的能力突破长期受限于高质量人工标注数据的稀缺与成本瓶颈，现有监督强化学习（RL）依赖昂贵标注，无监督方法则易陷入模型坍缩或奖励作弊。EasyRL 借鉴维果茨基最近发展区（ZPD）理论，提出“易样本知识迁移+难样本分治伪标签+难度渐进自训练”框架，以 10% 易标注数据驱动模型向难样本自进化。该方法在数据效率上表现突出，但其自进化能力是否真正突破基础模型采样分布边界，仍存疑。

】

---

【Polaris: A Gödel Agent Framework for Small Language Models through Experience-Abstracted Policy Repair ｜POLARIS：基于经验抽象的小语言模型递归策略修复

作者：Aditya Kakade、Vivek Srivastava、Shirish Karande

论文原文见 [arXiv](https://arxiv.org/abs/2603.23129)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.23129)

> 递归自我改进旨在让智能体通过检查自身策略与执行轨迹来持续优化能力，但现有框架如 Gödel Agent 依赖大模型容量，在 7B 参数的小语言模型（SLM）上因上下文膨胀导致内存溢出（OOM）而失效。POLARIS 通过“经验抽象”机制，将失败案例压缩为最小代码补丁，在资源受限条件下实现可追溯的策略持久化更新。该方法证明了 SLM 具备递归改进的可行性，但其性能增益依赖于特定骨干模型的元推理能力，且缺乏对补丁泛化性的量化评估。

】
