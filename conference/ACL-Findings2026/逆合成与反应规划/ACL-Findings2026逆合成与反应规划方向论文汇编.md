# ACL-Findings2026 · 逆合成与反应规划方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AOT: Efficient Synthesis Planning via LLM-Empowered AND-OR Tree Search ｜基于大语言模型路径生成的AND-OR树逆合成搜索

研究机构：香港中文大学、吉林大学

作者：Xiaozhuang Song、Xuanhao Pan、Xinjian Zhao 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.20988)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.20988)

> 逆合成规划旨在将目标分子分解为可商购原料，但传统单步预测加搜索的解耦架构在长程依赖与计算效率上存在瓶颈。现有LLM方法虽能捕捉策略连贯性，却因迭代进化算法导致搜索冗余与推理成本高昂。AOT*通过原子映射LLM生成的完整合成路径至AND-OR树结构，结合检索增强生成与UCB引导的树搜索，实现了路径级连贯性与树结构复用效率的平衡。该方法在复杂分子上展现出3-5倍的搜索效率优势，但其性能高度依赖底层LLM的生成质量与RAG数据库的覆盖度，在分布外分子上的泛化能力尚存疑。

】

---

【SAFER: Advancing Safety Alignment via Efficient Ex-Ante Reasoning ｜安全对齐中的事前推理框架

研究机构：浙江大学

作者：Kehua Feng、Keyan Ding、Yuhao Wang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_49128214040b)

> 大语言模型（LLM）在应对复杂科学安全威胁时，常因缺乏显式推理而陷入“表面对齐”陷阱，导致防御失效。现有方法多依赖事后回溯或通用思维链，难以在生成前精准识别隐蔽风险。SAFER通过引入结构化的事前推理（Ex-Ante Reasoning）与步骤级偏好优化，将安全判断拆解为评估、验证与校准三阶段。该框架显著提升了模型在科学安全领域的鲁棒性，但其推理延迟与规则泛化边界仍存疑。

】
