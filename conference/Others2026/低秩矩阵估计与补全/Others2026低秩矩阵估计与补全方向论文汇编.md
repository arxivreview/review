# Others2026 · 低秩矩阵估计与补全方向论文汇编

> 本方向共 2 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Spectral Thresholds in Correlated Spiked Models and Fundamental Limits of Partial Least Squares ｜相关尖峰模型下的谱阈值与偏最小二乘极限

研究机构：瑞士洛桑联邦理工学院

作者：Pierre Mergny、Lenka Zdeborová

论文原文见 [arXiv](https://arxiv.org/abs/2510.17561)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.17561)

> 导读 多模态学习旨在从多个相关高维数据源中联合恢复低维信号结构，但偏最小二乘（Partial Least Squares, PLS）作为主流谱方法，其理论性能边界长期缺失。现有研究仅通过数值实验指出PLS阈值次优，却缺乏解析证明，导致无法量化其与贝叶斯最优估计器的差距。本文通过随机矩阵理论推导双通道相关尖峰模型的样本跨协方差矩阵谱性质，首次给出PLS的精确相变阈值。该工作确立了PLS在特定信噪比与相关性区域存在固有信息损失的理论事实，但其结论局限于高维渐近极限，未涉及有限样本下的算法修正或实际数据验证。

】

---

【东北团队新研究：超稀疏采样下的单侧矩阵补全

研究机构：美国东北大学、美国佐治亚理工学院

作者：Hongyang R. Zhang、Zhenshuo Zhang、Huy L. Nguyen 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.12213)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.12213)

> 矩阵补全旨在从部分观测中恢复高维数据的低秩结构，但传统方法在观测数低于秩存储位数时面临信息论极限。现有非凸优化与凸松弛算法均无法在每行仅观测常数个条目的超稀疏场景下恢复完整矩阵，本文切入点在于放弃恢复矩阵本身，转而估计其行空间对应的二阶矩矩阵。通过引入Hájek估计器校正非随机缺失偏差，并结合梯度下降填补缺失项，实现了在 $p=C/d$ 采样率下的无偏估计。该工作解决了Cao et al. (2023) 遗留的通用采样开放问题，但在共同均值假设与秩指定依赖上存在理论边界。

】
