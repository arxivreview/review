# ICLR2026 · 非线性动力学的Koopman算子学习方向论文汇编

> 本方向共 3 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Spectral-Grassmann Wasserstein metric for operator representations of dynamical systems ｜谱-格拉斯曼最优传输度量

研究机构：印度理工学院

作者：Thibaut Germain、Rémi Flamary、Vladimir R. Kostic 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.24920)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24920)

> 动力学系统比较面临的核心难题在于，不同系统的Koopman算子定义在互不相同的函数空间上，导致直接比较在数学上无定义。现有范数距离对噪声敏感且缺乏物理可解释性，而基于谱的传输度量又局限于自伴算子。本文切入点是将算子表示为特征值与特征子空间在格拉斯曼流形上的联合分布，并定义其间的Wasserstein距离。该方法通过离散最优传输求解系统间几何距离，实现了采样频率不变性与有限样本收敛保证。其价值在于填补了算子间度量的理论空白，但实验仅覆盖线性振荡系统，对复杂非线性动力学的适用性存疑。

】

---

【Information Shapes Koopman Representation ｜信息论视角下的Koopman表示学习

研究机构：英国伦敦大学学院、英国帝国理工学院

作者：Xiaoyuan Cheng、Wenxuan Yuan、Yiming Yang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.13025)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.13025)

> 非线性动力学系统的长期预测面临误差累积与潜空间坍缩的双重困境，传统深度Koopman方法依赖重构损失与线性一致性约束，缺乏对潜空间有效维度的显式控制。本文切入点在于揭示潜空间坍缩的信息论根源，将信息瓶颈理论扩展至动态Koopman表示，证明互信息决定误差上界而冯·诺依曼熵维持有效维度。通过构建包含时间一致性、结构一致性与谱多样性的拉格朗日损失函数，本文在物理仿真与视觉控制任务上实现了更稳定的长期预测。该框架提供了通用的表示学习原则，但在强物理约束系统中的普适性仍存疑。

】

---

【LEARNING KOOPMAN REPRESENTATIONS WITH CON TROLLABILITY GUARANTEES ｜可控性保证的Koopman表示学习

研究机构：英国牛津大学、美国维拉诺瓦大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_37940700)

> 数据驱动非线性系统建模长期面临“预测准确但不可控”的结构性缺陷，导致模型预测控制（Model Predictive Control, MPC）等闭环工具无法直接应用。现有深度Koopman方法仅将可控性作为事后损失项，无法提供构造性保证。本文通过引入可控规范形参数化Koopman算子，在训练阶段强制满足Kalman秩条件，实现了预测精度与可控性的联合优化。该方法在低数据量场景下显著提升了数据效率，但其对多输入系统的扩展性及物理一致性约束的缺失仍存疑。

】
