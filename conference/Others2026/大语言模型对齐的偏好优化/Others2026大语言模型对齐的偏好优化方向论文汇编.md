# Others2026 · 大语言模型对齐的偏好优化方向论文汇编

> 本方向共 1 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Towards Disentangled Preference Optimization Dynamics Beyond Likelihood Displacement ｜解耦偏好优化动态：从似然位移到奖励校准

研究机构：华南理工大学、日本理化学研究所

作者：Wei Chen、Yubing Wu、Junmei Yang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18239)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18239)

> 偏好优化旨在将人类价值观内化至大语言模型，但主流基于边际的目标函数（如DPO）常导致获胜响应概率与落败响应同步下降，即“似然位移”。现有解耦方法虽能缓解此问题，但缺乏统一理论解释其动力学差异，且无法直接应用于已部署的纠缠目标。本文通过激励-分数分解揭示目标函数仅通过标量系数控制更新方向，进而提出解耦带（DB）作为可测试条件，并设计即插即用的奖励校准（RC）以重平衡梯度。该框架在理论上统一了纠缠与解耦目标，但在高维非局部纠缠及在线设置下的有效性尚未验证。

】
