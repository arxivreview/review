# ACL-Findings2026 · 自回归长视频生成方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Accelerating Training of Autoregressive Video Generation Models via Local Optimization with Representation Continuity ｜局部优化与表示连续性加速自回归视频生成训练

研究机构：澳门大学

作者：Yucheng Zhou、Jianbing Shen

论文原文见 [arXiv](https://arxiv.org/abs/2604.07402)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07402)

> 自回归视频生成面临训练成本高、时长受限的瓶颈，主流方案通过增加帧数或迭代推理提升质量，却导致误差级联与训练效率低下。本文切入点在于解耦训练序列长度与推理序列长度，通过局部窗口优化消除曝光偏差。具体做法是引入冻结上下文的局部优化策略，并基于Lipschitz连续性约束隐状态平滑性。该方法在保持推理速度不变的前提下实现2倍训练加速，但仅在短序列数据集上验证，长视频一致性未获证实。

】
