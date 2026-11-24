# ACL-Findings2026 · 大语言模型安全对齐与拒答训练方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【OmniCompliance-100K: A Multi-Domain, Rule-Grounded, Real-World Safety Compliance Dataset ｜规则接地真实世界合规数据集

研究机构：香港科技大学

作者：Wenbin Hu、Huihao Jing、Haochen Shi 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_270f2f3b3b34)

> 大语言模型（LLM）安全对齐长期依赖合成数据，导致模型在真实法律合规场景下泛化能力不足。现有基准如ToxicChat和WildGuard由LLM生成，缺乏真实执法案例的多样性与严谨性，无法覆盖金融、医疗等高 stakes 领域的具体法规条款。本文通过构建首个大规模、多领域、规则接地的真实世界合规数据集，填补了从“通用有害内容抑制”到“具体法规合规判断”的数据空白。该数据集揭示了现有安全护栏在合规任务上的严重失效，但其仅评估准确率而未考察合规判断对模型有用性的影响，这一局限值得警惕。

】

---

【You Only Need One Single Token to Refine Safety Alignment ｜单令牌对齐

研究机构：武汉大学、德国慕尼黑大学

作者：Wenqian Yu、Shuo Chen、Zhijiang Li 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_57097267c171)

> 安全对齐的核心矛盾在于抑制有害输出与保持模型有用性之间的参数空间冲突，过度拒绝（Over-refusal）是这一冲突在良性边界样本上的典型表现。现有免训练干预方法虽降低了训练成本，却因仅做后验修正而无法重塑模型内部的决策分布，导致安全与效用此消彼长的失衡。本文提出单令牌对齐（Single Token Alignment, STA），通过冻结骨干网络并仅优化一个4096维的前缀嵌入向量，结合硬软混合加权机制，在极小参数接口下实现决策空间的重塑。该方法在9个模型上验证了其在轻量级约束下平衡安全与效用的有效性，但其对复杂语境细微差别的捕捉能力仍存疑。

】
