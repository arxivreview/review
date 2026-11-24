# ACL-Findings2026 · 面向数据科学与分析的大语言模型智能体方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【DataSage: Multi-agent Collaboration for Insight Discovery with External Knowledge Retrieval, Multi-role Debating, and Multi-path Reasoning ｜数据洞察智能体：多角色辩论与外部知识检索

作者：Xiaochuan Liu、Yuanfeng Song、Xiaoming Yin 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.14299)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.14299)

> 数据科学智能体旨在自动化从数据清洗到洞察生成的全生命周期工作流，其核心价值在于突破传统自动机器学习仅能处理预定义管道的局限。现有问答式智能体受限于领域知识缺失、分析深度不足及代码生成易错，难以产出可行动的商业洞察。DataSage 通过引入检索增强知识生成、多角色辩论问题生成及多路径代码推理，构建了迭代式问答闭环。该框架在 InsightBench 上显著优于基线，但其对结构化表格数据的依赖及外部检索的实时性约束，限制了其在异构数据环境下的泛化能力。

】

---

【DataSeer: A Manager-Centric Collaborative Multi-Agent Framework with Multi-Branch Reasoning for Automated Insight Discovery ｜DataSeer：面向自动化洞察发现的管理者中心多智能体框架

研究机构：北京大学

作者：Suchen Liu、Yuanfeng Song、Jun Gao 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_af490e56fb73)

> 导读 数据科学智能体（Data Science Agents, DSA）旨在利用大语言模型（LLM）自动化从数据清洗到洞察生成的全生命周期工作流，其核心价值在于突破传统自动机器学习（AutoML）仅能处理预定义管道的局限。现有单体智能体在长链推理中易出现上下文碎片化与记忆衰减，且固定规划模板难以适应动态探索，导致洞察覆盖度受限。DataSeer 通过引入管理者中心协作框架与多分支推理机制，解决跨回合连贯性与单路径随机性问题。该框架在开放式洞察发现任务上显著优于基线，但其确定性调度策略对突发数据异常的自适应能力仍存疑。

】

---

【Generalization or Memorization? Multi-Agent vs. Baseline LLMs and AutoML Models for Tabular Classification ｜表格分类中多智能体LLM与AutoML的可靠性对比

研究机构：美国弗吉尼亚大学、美国圣母大学

作者：Aida Sanatizadeh、Sorouralsadat Fatemi、Reza Mousavi 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4b8691db471d)

> 表格数据驱动的高风险决策要求系统不仅准确，更需在分布偏移和困难实例上保持校准与稳定。现有LLM方法在表格分类上的表现常被预训练语料记忆所混淆，且缺乏对实例级可靠性的细粒度诊断。本文通过构建污染感知的评估协议和模块化多智能体框架（MALLM），系统性地解耦了记忆效应与泛化能力。该研究揭示了当前LLM在表格分类中作为独立预测引擎的结构性局限，但其结论的普适性仍受限于特定数据集规模和评估维度。

】

---

【InsightEval: An Expert-Curated Benchmark for Assessing Insight Discovery in LLM-Driven Data Agents ｜洞察发现基准与多维评估框架

研究机构：香港科技大学

作者：Zhenghao Zhu、Yuanfeng Song、Xin Chen 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.22884)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.22884)

> 数据科学智能体在自动化分析中常陷入“幻觉”陷阱，即生成的洞察看似合理却与底层数据事实不符，或仅重复已知信息而缺乏新颖性。现有基准如 InsightBench 存在目标模糊、数据缺失及评估指标单一（仅关注召回率）的缺陷，导致无法准确衡量智能体的真实探索能力。本文通过构建包含 1000 个高质量洞察的 InsightEval 数据集，并引入 Insight F1 与 Novelty 指标，实现了对智能体洞察发现能力的全面量化。该工作填补了细分领域的评估空白，但其依赖 LLM 作为评估器的机制可能引入新的主观偏差。

】

---

【Tree-Notebook: A Context-Aware Agent with Tree Search and Entropy-Aware Data Shadow for Interactive Data Science ｜树搜索与熵感知数据影子驱动的交互式数据科学智能体

研究机构：中国科学院大学

作者：Junkun Qiu、Min Huang、Qinghai Miao

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6832aac1ef5b)

> 数据科学智能体在长链推理中常因无法感知内存状态而陷入“静默失败”，即代码执行无错但数据已受损。现有线性框架缺乏回溯机制，导致早期错误沿任务链不可逆地传播。Tree-Notebook 将代码生成形式化为部分可观测马尔可夫决策过程（POMDP），通过树状拓扑与数据影子机制实现非线性探索与状态监控。该架构在基准测试中超越了线性基线，但其高昂的计算开销与对骨干模型能力的强依赖，限制了其在资源受限场景下的通用性。

】
