# ACL-Findings2026 · 基于大语言模型的优化建模方向论文汇编

> 本方向共 4 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Escaping the Sisyphus Dilemma: Experience Replay for Robust Text-to-Optimization Modeling ｜经验回放优化建模

研究机构：中国科学技术大学

作者：Wantong Xie、Yinghao Chen、Yi-Xiang Hu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b30a4b95ed54)

> 导读 LLM 优化建模面临“西西弗斯困境”：模型在结构相似问题上重复相同错误，且现有检索增强生成（RAG）仅能提供静态代码参考，无法传递纠错逻辑。EOM 通过引入因果修正映射与结构感知检索，将瞬时的试错过程转化为持久化的诊断知识。该框架在复杂基准上提升准确率 8.45%，同时降低 28.65% 的 Token 消耗，验证了“一次纠错，多次复用”的可行性，但其对显式求解器反馈的依赖限制了其在静默语义错误场景下的适用性。

】

---

【OptiVerse: A Comprehensive Benchmark towards Optimization Problem Solving ｜OptiVerse：面向多域优化求解的大语言模型基准与审计机制

作者：Xinyu Zhang、Boxuan Zhang、Yuchen Wan 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c13100191701)

> 大语言模型（LLM）在优化建模中面临的核心挑战并非代码语法错误，而是语义逻辑偏离题意导致的静默失败。现有基准多局限于数学规划与组合优化，无法全面评估模型在随机、动态及博弈等复杂领域的泛化能力，且缺乏对模型内部逻辑一致性的有效验证。本文构建了覆盖六大优化领域的OptiVerse基准，并提出双视角审计智能体（Dual-View Auditor Agent, DVA-Agent），通过盲审代码与需求交叉比对来检测并修复语义偏差。该工作揭示了当前LLM在Hard难度问题上的严重性能瓶颈，但其审计机制的有效性依赖于特定骨干模型，且未解决跨范式验证的理论完备性问题。

】

---

【Reasoning in a Combinatorial and Constrained World: Benchmarking LLMs on Natural-Language Combinatorial Optimization ｜自然语言组合优化基准

研究机构：荷兰埃因霍温理工大学、新加坡南洋理工大学

作者：Xia Jiang、Jing Chen、Cong Zhang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.02188)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.02188)

> 组合优化（Combinatorial Optimization, CO）要求在高维离散空间中寻找满足硬约束的最优解，但现有大语言模型（LLM）评估多聚焦于算术或逻辑推理，缺乏对复杂约束下决策能力的系统测试。主流优化基准往往依赖代码生成或外部求解器，混淆了模型内部推理与外部工具的性能。NLCO通过构建43个情境化CO任务的四层分类体系，强制LLM在无工具辅助下直接输出离散解，从而隔离评估其原生组合推理极限。该基准揭示了模型性能随实例规模急剧衰减的规律，但受限于中等规模实例与标准化文本，其结论向真实工业场景的外推性仍存疑。

】

---

【Solver-Independent Automated Problem Formulation via LLMs for High-Cost Simulation-Driven Design ｜求解器无关的自动化问题建模

研究机构：西安电子科技大学、新西兰惠灵顿维多利亚大学

作者：Yuchen Li、Handing Wang、Bing Xue 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.18682)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_62def8db4b69)

> 高成本仿真驱动设计面临的核心矛盾是：将模糊的自然语言需求转化为可执行数学模型的过程高度依赖专家，而验证模型正确性的求解器反馈因仿真成本过高无法用于数据筛选。现有提示工程方法在复杂约束下易产生语义偏差，微调方法则受限于缺乏低成本的数据质量过滤机制。本文提出 APF 框架，通过测试实例排序一致性替代求解器反馈进行数据筛选，并结合数据增强对开源大语言模型进行监督微调。该框架在特定工业场景下实现了小模型超越大模型提示的效果，但其验证机制的通用性与理论边界尚待检验。

】
