# ACL-Findings2026 · 混合精度神经网络量化方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CoopQ: Cooperative Game Inspired Layerwise Mixed Precision Quantization for LLMs ｜合作博弈驱动的层间混合精度量化

研究机构：美国加州大学尔湾分校

作者：Junchen Zhao、Ali Derakhshan、Jayden Kana Hyman 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.15455)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.15455)

> 大语言模型（LLM）在极低比特部署时，传统基于单层敏感度的混合精度量化因忽略层间误差传播导致精度崩塌。CoopQ 将量化建模为层间合作博弈，通过渐进量化估计 Shapley 值以捕捉交互效应，并利用混合整数线性规划求解全局最优位宽分配。该方法在 2-4 bit 区间显著降低了困惑度，但其离线计算开销与二元位宽限制构成了实际部署的边界。

】
