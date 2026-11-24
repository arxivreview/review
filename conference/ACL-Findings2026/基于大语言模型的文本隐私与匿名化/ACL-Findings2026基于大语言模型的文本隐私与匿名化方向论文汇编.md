# ACL-Findings2026 · 基于大语言模型的文本隐私与匿名化方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Adaptive Text Anonymization: Learning Privacy-Utility Trade-offs via Prompt Optimization ｜自适应文本匿名化：基于进化提示优化的隐私-效用权衡探索

研究机构：法国国家科学研究中心

作者：Gabriel Loiseau、Damien Sileo、Damien Riquet 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.20743)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b0659f29ad99)

> 导读 文本匿名化旨在平衡敏感信息去除与下游任务效用，但现有方法依赖静态规则或手动提示，难以适应多变的隐私-效用需求。本文提出将匿名化建模为多目标提示优化问题，利用进化算法自动发现适应特定任务的匿名化指令。该方法在开源模型上实现了接近闭源SOTA的性能，并揭示了隐私-效用权衡前沿的多样性。其价值在于实现了策略的自动化适配，但依赖少量标注数据且评估环节仍部分依赖闭源模型，限制了其完全本地化部署的潜力。

】

---

【Look Twice before You Leap: A Rational Framework for Localized Adversarial Text Anonymization ｜理性本地化对抗匿名化

研究机构：电子科技大学、中国人民大学

作者：Donghang Duan、Xu Zheng、Yuefeng He 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2c9d987e9e08)

> 本地小模型部署下的文本匿名化面临效用崩溃困境，现有贪心对抗策略在缺乏形式化保证的前提下，因模型幻觉导致过度编辑。本文切入点在于将匿名化过程重构为经济交易问题，通过引入仲裁者验证泄露有效性，从架构层面阻断非理性迭代。该方法以零样本、免训练的方式实现了隐私-效用帕累托前沿的优化，但其缺乏差分隐私等数学边界，合规性存疑。

】
