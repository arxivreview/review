# ACL-Findings2026 · 测试时适应与训练方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Generative-to-Discriminative Test-Time Adaptation via Manifold-Aware Diffusion and Bayesian Distillation ｜生成-判别式测试时适应

研究机构：浙江大学

作者：Boyun Zhang、Zequn Xie、Fangming Feng 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cb106a93019c)

> 测试时适应（Test-Time Adaptation, TTA）旨在解决模型部署后因分布偏移导致的性能衰退，其核心在于利用无标签测试数据在线修正模型参数。现有判别式方法依赖“高置信度即正确”的假设，在严重偏移下易陷入“自信但错误”的陷阱，而生成式模型虽具备鲁棒性却受限于迭代去噪的高延迟。本文提出 GD-Adapt，通过贝叶斯扩散蒸馏将生成教师的鲁棒性转移至轻量级判别学生，并引入流形估计器过滤分布外样本。该方法在跨域情感分析任务上显著提升了回归精度，但其异步适应机制对实时同步性的影响尚存疑。

】
