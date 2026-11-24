# Others2026 · 算法公平性与群体公平性方向论文汇编

> 本方向共 1 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Fairness-aware PageRank via Edge Reweighting ｜基于边权重加权的公平PageRank

研究机构：瑞典皇家理工学院

作者：Honglian Wang、Haoyun Chen、Aristides Gionis

论文原文见 [arXiv](https://arxiv.org/abs/2512.08055)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.08055)

> 图链接分析算法在排序与社区检测中广泛应用，但随机游走过程往往因网络同配性导致特定群体获得不成比例的PageRank分数，引发群体公平性问题。现有方法如FairWalk和CrossWalk通过强制局部转移概率均匀来消除偏差，但往往导致图结构发生剧烈扭曲，且难以处理多组场景。本文切入点在于放弃“每步局部公平”的刚性约束，转而通过投影梯度下降优化全局公平损失，仅对现有边权进行有限重加权。该方法在保持图拓扑不变的前提下，以极小的结构扰动实现了显著的全局公平性提升，但其效果依赖于目标分布的预设，且在动态图演化场景下的鲁棒性尚未验证。

】
