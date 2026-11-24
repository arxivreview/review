# ACL-Findings2026 · 大语言模型引导的算法设计与优化方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Experience-Driven Reflective Co-Evolution of Prompts and Heuristics for Autonomous Algorithm Design ｜经验驱动反思协同进化

研究机构：中国人民大学、香港城市大学

作者：Yihong Liu、Junyi Li、Hongyu Lu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fcd8a64ea779)

> 自动启发式设计（AHD）旨在突破手工算法对专家知识的依赖，利用大语言模型（LLM）的语义推理能力自动发现高性能组合优化算法。现有方法多将LLM视为静态变异算子，受限于固定提示与稀疏反馈，易陷入局部最优且代码错误易在种群中传播。本文提出EvoPH，通过耦合提示词进化与启发式进化，利用执行经验动态调整变异策略，实现搜索过程的自我修正。该框架在TSP和BPP上显著优于基线，但其性能高度依赖底层LLM的规模，小模型在装箱问题上几乎失效，暴露了方法对模型能力的强耦合性。

】

---

【What Makes an LLM a Good Optimizer? A Trajectory Analysis of LLM-Guided Evolutionary Search ｜LLM进化搜索的局部精化机制

研究机构：法国国家科学研究中心

作者：Xinhao Zhang、Xi Chen、François Portet 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.19440)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_de954a204254)

> 大语言模型（LLM）作为进化算子时，其优化性能差异的根源长期被归因于基础模型能力，但零样本性能仅部分解释最终结果。现有方法关注算法发现本身，却忽略了算子内部的搜索动力学，导致无法区分“强求解器”与“强优化器”。本文通过大规模轨迹分析，揭示强LLM优化器表现为“局部精化器”，其成功依赖于高频增量改进而非高新颖性探索。这一发现挑战了传统进化算法中“探索即创新”的直觉，为模型选择提供了基于精化能力而非基础能力的评估维度，但其结论在跨域泛化性上仍受限于特定任务结构。

】
