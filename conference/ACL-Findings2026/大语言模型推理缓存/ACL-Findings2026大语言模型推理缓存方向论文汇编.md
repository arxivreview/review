# ACL-Findings2026 · 大语言模型推理缓存方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Efficient and Effective Internal Memory Retrieval for LLM-Based Healthcare Prediction ｜内部键值检索框架 K2K

研究机构：美国康涅狄格大学

作者：Mingchen Li、Jiatan Huang、Zonghai Yao 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.07659)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_23d7f957db6e)

> 临床LLM部署面临外部检索延迟高与知识幻觉的双重瓶颈，传统RAG管线因长上下文注入导致推理成本激增。K2K将检索目标从外部文档库转向模型内部FFN权重矩阵，通过LoRA注入领域知识并构建激活引导探针，实现无外部搜索的知识访问。该方法在MIMIC-III/IV医疗预测任务上优于KARE等外部检索基线，但其依赖固定层选择且仅在生物医学域验证，通用性存疑。

】
