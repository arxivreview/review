# ACL-Findings2026 · 大型语言模型的自动化红队测试方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【GRE Score: Generative Risk Evaluation for Large Language Models ｜生成式鲁棒性评估分数

研究机构：香港中文大学、IBM研究院

作者：Zaitang LI、Pin-Yu Chen、Tsung-Yi Ho

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ae07703c30dd)

> 大语言模型（LLM）安全评估长期依赖高成本的对抗攻击迭代，且现有基准面临数据污染风险。本文提出 GRE Score，一种基于条件生成模型的鲁棒性证书，通过计算语义空间中的最小扰动下界来量化模型韧性。该方法仅需前向传播即可生成具有理论保证的评估指标，实现了与攻击成功率（ASR）的高相关性。其价值在于提供高效的替代评估方案，但语义空间扰动与真实文本对抗的等价性仍存疑。

】

---

【STAR-Teaming: A Strategy-Response Multiplex Network Approach to Automated LLM Red Teaming ｜策略-响应多层网络自动化红队测试

作者：Min Jae Jung、YongTaek Lim、Chaeyun Kim 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18976)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3fb78adea86d)

> 自动化红队测试旨在以规模化手段替代高成本人工红队，探测大语言模型（LLM）安全边界。现有策略类方法依赖嵌入相似度检索，缺乏对攻击成功因果模式的分析，导致策略过采样与可解释性缺失。STAR-Teaming 通过构建策略-响应多层网络，将策略选择转化为基于逆伊辛模型的统计优化问题，实现高效且可解释的自适应采样。该方法在黑盒场景下显著提升了攻击成功率与效率，但其单轮/少轮设定下的性能上限及社区结构对长程依赖的适应性仍存疑。

】
