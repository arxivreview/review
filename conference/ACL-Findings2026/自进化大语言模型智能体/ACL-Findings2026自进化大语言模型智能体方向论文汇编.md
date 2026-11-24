# ACL-Findings2026 · 自进化大语言模型智能体方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Beyond Static Toolsets: Self-Evolving LLM Tool Agents via Continual Documentation Adaptation ｜持续文档适应

研究机构：英国伦敦大学学院

作者：Bin Wu、Edgar Meij、Emine Yilmaz

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f2667bbb2c89)

> 导读 工具使用大语言模型（LLM）在部署中面临工具集动态增删导致的性能波动，现有静态文档优化方法无法应对这种环境漂移。本文提出 ContDa，通过关系引导探索与关系感知调整，在不更新模型权重的前提下持续重构工具文档。该方法在 StableToolBench 动态扩展实验中，将平均性能从基线的 8.67% 提升至 11.20%，同时控制了旧任务遗忘。其价值在于验证了文档作为轻量级进化载体的可行性，但缺乏与参数化方法的横向对比，且未量化文档更新对模型内部表征的潜在干扰。

】

---

【Mistake Notebook Learning: Batch-Clustered Failures for Training-Free Agent Adaptation ｜错误笔记本学习

作者：Xuanbo Su、Yingfang Zhang、Hao Luo 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_77668cc3f3eb)

> 导读 自进化智能体在开放环境中面临的核心矛盾是：静态权重无法适应动态任务，而纯参数微调又受限于高昂计算成本与灾难性遗忘。现有非参数化记忆方法多依赖实例级经验存储，导致记忆冗余且泛化能力弱，难以从孤立错误中提炼通用规律。MNL 提出了一种基于批量聚类错误抽象的无训练记忆框架，通过“若改进则接受”的保守更新机制，将失败轨迹蒸馏为结构化指导，从而在保持模型权重冻结的前提下实现能力迭代。该方法在数学推理与智能体任务中展示了极高的记忆效率，但其性能上限是否仍受制于非参数化机制的固有局限，尚需更长期的纵向对比验证。

】

---

【On Safety Risks in Experience-Driven Self-Evolving Agents ｜经验驱动自进化智能体的安全退化机制

作者：Weixiang Zhao、Yichen Zhang、Yingshuo Wang 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.16968)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_375a1df0ee59)

> 自进化智能体通过复用交互轨迹提升任务能力，但现有安全评估多关注参数更新或显式有害指令，忽略了纯良性经验在高风险场景下的隐性风险。本文切入点在于证明：即使经验完全源自良性任务，其“执行导向”结构仍会导致智能体在高风险场景中安全边界系统性崩塌。通过构建离线/在线双范式实验与长度匹配对照，本文量化了这一退化过程并归因于经验中的执行偏差。该研究揭示了非参数化进化的固有安全漏洞，但其在混合经验场景下的安全-效用权衡机制仍显粗糙，且未提供有效的缓解方案。

】

---

【OPT-BENCH: Evaluating the Iterative Self-Optimization of LLM Agents in Large-Scale Search Spaces ｜大语言模型迭代自优化能力评估基准

研究机构：同济大学、复旦大学

作者：Xiaozhe Li、Jixuan Chen、Xinyu Fang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.08904)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.08904)

> 现有大语言模型（LLM）评估基准多聚焦于单次响应生成或任务完成率，忽视了模型在动态环境中利用反馈进行持续改进的“迭代自优化”能力。本文切入点在于构建一个区分连续参数优化与离散组合推理的评估框架，以探测模型内在的认知适应边界。通过引入感知-记忆-推理循环的代理框架，本文量化了模型将环境信号转化为解空间搜索策略的效率。该基准揭示了强模型在连续空间中的归纳优化优势与在离散空间中的结构修复瓶颈，但受限于样本规模与基线覆盖，其结论的普适性仍存疑。

】

---

【Towards Self-Evolving Agents: Enabling Autonomy through Interactive Experience Refinement ｜记忆驱动的自我进化智能体

研究机构：中南大学、复旦大学

作者：Cheng Yang、Xuemeng Yang、Licheng Wen 等 13 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bad481343316)

> 静态大语言模型在部署后无法从过往交互中积累经验，导致其在长程生产力任务中表现受限且无法持续改进。现有非参数化反思方法多依赖线性文本存储，缺乏结构化知识组织，而参数化更新则面临高计算成本与灾难性遗忘风险。MUSE 通过分层记忆模块将原始执行轨迹蒸馏为可复用的标准作业程序，实现了无需微调的测试时学习。该框架在 TAC 基准上以轻量级模型刷新了性能纪录，但其记忆检索机制在大规模库下的扩展性仍存疑。

】
