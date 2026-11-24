# ICLR2026 · Wasserstein距离近似与变体方向论文汇编

> 本方向共 7 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A SCALABLE CONSTANT-FACTOR APPROXIMATION ALGORITHM FOR _W_ OPTIMAL TRANSPORT _p_ ｜任意度量空间下 $W_p$ 最优传输的常数因子近似算法

研究机构：美国杜克大学、美国北卡罗来纳州立大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_67361708)

> 离散概率分布间的最优传输距离（Optimal Transport, OT）计算在精确求解时面临 $n^{2+o(1)}$ 的时间复杂度瓶颈，且现有近似方法在 $p \ge 2$ 或 $p=\infty$ 时失效或精度不足。本文切入点在于利用聚类构建有向 Spanner，将非度量成本 $d(\cdot, \cdot)^p$ 近似为图上的最短路径，从而在任意度量空间下实现二次时间复杂度的常数因子相对近似。该方法首次覆盖了 $W_\infty$ 情形，但在高维数据上的实际近似比与理论界存在差距，且未与主流统计近似方法直接对比。

】

---

【Efficient Sliced Wasserstein Distance Computation via Adaptive Bayesian Optimization ｜自适应贝叶斯优化切片 Wasserstein 距离计算

研究机构：美国范德堡大学

作者：Manish Acharya、David Hyde

论文原文见 [arXiv](https://arxiv.org/abs/2509.17405)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.17405)

> 切片 Wasserstein 距离（Sliced Wasserstein Distance, SWD）通过一维投影将高维最优传输问题降维，但其精度受限于投影方向的选择策略。传统随机或准蒙特卡洛（Quasi-Monte Carlo, QMC）采样采用任务无关的均匀覆盖，在分布动态演变的优化循环中无法聚焦高信息量区域，导致收敛效率低下。本文提出利用贝叶斯优化（Bayesian Optimization, BO）将投影方向选择建模为球面黑盒函数优化问题，通过高斯过程代理模型自适应定位高信号方向。该方法在点云插值任务中实现了与最优 QMC 基线相当的收敛速度，且方差更小，但在高维场景下的计算开销与无偏性保证仍存疑。

】

---

【Fast Estimation of Wasserstein Distances via Regression on Sliced Wasserstein Distances ｜基于切片距离回归的 Wasserstein 距离快速估计

研究机构：美国德克萨斯大学奥斯汀分校

作者：Khai Nguyen、Hai Nguyen、Nhat Ho

论文原文见 [arXiv](https://arxiv.org/abs/2509.20508)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.20508)

> 高维 Wasserstein 距离 (WD) 的精确求解受限于 $O(n^3 \log n)$ 的线性规划复杂度，阻碍了其在大规模分布对比较中的应用。现有神经嵌入方法虽能加速，但依赖大量训练数据且仅限经验分布。本文提出一种无神经网络的线性回归框架，将多种切片 Wasserstein 距离 (SWD) 变体作为预测变量，通过最小二乘法拟合真实 WD。该方法在低数据量场景下显著优于 SOTA 神经嵌入模型，并成功加速了 Wormhole 的训练过程，但其线性假设在高维复杂几何下的泛化能力尚存疑。

】

---

【REVISITING TREE-SLICED WASSERSTEIN DISTANCE THROUGH THE LENS OF THE FERMAT–WEBER PROBLEM ｜基于费马-韦伯问题的树切片 Wasserstein 距离

研究机构：新加坡国立大学

作者：Viet-Hoang Tran、Thanh Q. Tran、Thanh Chu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_94857498)

> 树切片 Wasserstein 距离（Tree-Sliced Wasserstein, TSW）旨在通过树状度量空间捕捉高维分布的局部几何结构，但现有方法在采样树系统交点时依赖启发式策略，未能充分利用位置信息。本文指出，SW 仅采样方向而 TSW 同时涉及方向与位置，且欧氏空间非紧性导致无法定义均匀位置分布，这是 TSW 性能受限的关键盲区。作者引入费马-韦伯问题，利用 Weiszfeld 算法计算数据几何中位数作为树交点采样中心，构建了数据依赖的 FW-TSW 距离。该方法在梯度流与扩散模型训练中优于现有 TSW 变体，但其缺乏显式传输映射的局限仍未解决。

】

---

【SEINT: An Efficient SE(p)-Invariant Transport Metric Driven by Polar Transport - Discrepancy Based Representation ｜SE(p)不变传输度量

研究机构：中国人民大学、北京理工大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_3976472)

> SE(p)不变传输度量旨在解决点云与分子等几何对象在旋转平移下的分布比较难题。现有方法或计算昂贵（如GW），或牺牲度量性质（如RISGW），无法兼顾效率与理论严谨性。本文通过极坐标范数分布与距离卷积提取不变特征，将其转化为1D最优传输问题。该方案在保持严格度量性质的同时实现了O(n log n)复杂度，但其在高维流形上的泛化能力尚存疑。

】

---

【Slicing Wasserstein Over Wasserstein Via Functional Optimal Transport ｜基于函数最优传输的Wasserstein over Wasserstein切片度量

作者：Moritz Piening、Robert Beinert

论文原文见 [arXiv](https://arxiv.org/abs/2509.22138)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.22138)

> 本文旨在解决Wasserstein over Wasserstein（WoW）距离在比较分布的分布（meta-measures）时计算成本高昂且数值不稳定的问题。现有加速方案如s-OTDD依赖高阶矩，导致数值崩溃，而基于Busemann函数的方法依赖高斯近似，限制了通用性。本文切入点在于利用1D Wasserstein空间与$L_2([0,1])$函数空间的等距嵌入，将切片操作推广至无限维Banach空间，通过高斯过程参数化投影方向，定义了双重切片Wasserstein（DSW）度量。该框架在形状分类任务上实现了与Gromov-Wasserstein（GW）相当的精度，但计算速度提升数个数量级，其理论等价性在离散化场景下成立，但在高维连续空间的泛化边界尚待验证。

】

---

【TREE-SLICED SOBOLEV IPM ｜树切片Sobolev积分概率度量

研究机构：新加坡国立大学

作者：Viet-Hoang Tran、Thanh Q. Tran、Thanh Chu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_35515838)

> 现有树切片Wasserstein距离（TSW）受限于一阶度量，无法提供高阶优化所需的平滑梯度，阻碍了其在生成模型等梯度驱动任务中的应用。本文切入点在于利用正则化Sobolev积分概率度量（IPM）在树空间上的闭式解，构建支持任意阶 $p \ge 1$ 的树切片距离。通过随机树系统投影与Sobolev范数约束的结合，实现了计算复杂度与优化景观的平衡。该方法在多项基准上超越了现有切片变体，但其性能增益是否完全归因于高阶凸性，还是树结构本身的几何特性，尚存疑。

】
