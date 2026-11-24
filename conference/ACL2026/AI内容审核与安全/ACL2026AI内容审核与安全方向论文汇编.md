# ACL2026 · AI内容审核与安全方向论文汇编

> 本方向共 3 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CHAIRO: Contextual Hierarchical Analogical Induction and Reasoning Optimization for LLMs ｜基于类比归纳的规则推理优化框架

研究机构：新加坡国立大学、深圳大学

作者：Haotian Lu、Yuchen Mou、Bingzhe Wu

论文原文见 [arXiv](https://arxiv.org/abs/2604.10502)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10502)

> 内容审核系统在处理隐喻性歧视或模糊语境时，常因规则缺失或过于宽泛而失效。现有大语言模型（LLM）直接提示或静态检索增强生成（RAG）方法难以从细粒度实例中动态提炼出可解释的审核标准。CHAIRO 通过自增强类比思维链与辅助模型规则归纳的端到端联合优化，将检索、规则生成与分类决策耦合，解决了规则泛化与语境适配的矛盾。该方法在细粒度文本审核任务上显著提升了准确率与规则质量，但其对多模态隐性危害及极端长尾类别的适用性仍存疑。

】

---

【FlexGuard: Continuous Risk Scoring for Strictness-Adaptive LLM Content Moderation ｜严格度自适应的连续风险评分

研究机构：香港理工大学、Hugging Face

作者：Zhihao Ding、Jinming Li、Ze Lu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.23636)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.23636)

> 内容审核系统需在不同平台与时间维度下适应动态变化的执法标准，但现有二元分类器将安全定义固化为静态标签，导致策略切换时性能剧烈波动。本文指出这一“严格度脆弱性”被现有基准忽视，提出以连续风险分数替代固定标签的范式。通过构建FlexBench基准与FlexGuard模型，利用评分标准蒸馏与强化学习对齐分数-严重度一致性。该方法在动态严格度下显著优于基线，但其仅聚焦文本模态且依赖伪标签蒸馏，在多模态与极端边界校准上的有效性存疑。

】

---

【PluRule: A Benchmark for Moderating Pluralistic Communities on Social Media ｜多元社区规则审核基准

研究机构：美国印第安纳大学

作者：Zoher Kachwala、Bao Tran Truong、Rasika Muralidharan 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.17187)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.17187)

> 去中心化社交平台的内容治理面临规范碎片化挑战，同一内容在不同社区可能合规或违规，传统基于全局统一标准的分类器无法捕捉这种语境依赖性。现有基准多聚焦于仇恨言论等单一类别，缺乏对社区特定规则动态性的系统评估。PLURULE 将审核任务重构为多选题，要求模型在特定社区规则集下识别具体违规项，从而量化视觉语言模型在多元规范理解上的能力边界。该基准揭示了当前模型在局部规则推理上的显著缺陷，但仅评估精度而未涉及部署效率，其结论对工业级实时审核系统的适用性存疑。

】
