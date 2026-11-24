# ICLR2026 · 可解释机器学习与Shapley值方向论文汇编

> 本方向共 2 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【PolySHAP: Extending KernelSHAP with Interaction-Informed Polynomial Regression ｜多项式回归扩展的Shapley值估计

研究机构：美国纽约大学

作者：Fabian Fumagalli、R. Teal Witter、Christopher Musco

论文原文见 [arXiv](https://arxiv.org/abs/2601.18608)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.18608)

> 现有Shapley值近似方法受限于线性假设，无法捕捉特征间的高阶非线性交互，导致在复杂模型中归因精度不足。KernelSHAP等主流方法仅拟合一阶线性函数，忽略了特征协同效应对预测的贡献。本文通过引入高阶多项式回归替代线性近似，并证明了配对采样策略与二阶多项式拟合的数学等价性，从而在理论层面解释了该启发式策略的有效性。该方法在低维交互显著场景下提升了估计精度，但在高维特征空间中因计算复杂度限制，其增益幅度受到制约。

】

---

【Unifying Formal Explanations: A Complexity-Theoretic Perspective ｜统一形式化解释的计算复杂性理论

研究机构：以色列耶路撒冷希伯来大学、新加坡南洋理工大学

作者：Shahaf Bassan、Xuanxiang Huang、Guy Katz

论文原文见 [arXiv](https://arxiv.org/abs/2602.18160)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.18160)

> 机器学习解释的生成常面临计算不可行性，尤其是当要求解释具备概率保证或全局覆盖时，现有算法往往陷入指数级搜索。本文指出，局部与全局解释在数学性质上存在被忽视的非对称性，通过构建统一的值函数优化框架，揭示了全局解释具备单调性与次/超模性，从而在多项式时间内可解。这一理论突破为黑盒模型的全局可解释性提供了算法可行性基础，但其工程落地与解释信息量的平衡仍存疑。

】
