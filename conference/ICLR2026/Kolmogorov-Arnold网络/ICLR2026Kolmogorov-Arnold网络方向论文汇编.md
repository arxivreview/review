# ICLR2026 · Kolmogorov-Arnold网络方向论文汇编

> 本方向共 6 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Graph Meta-Network for Learning on Kolmogorov-Arnold Networks ｜图元网络学习柯尔莫哥洛夫-阿诺德网络

研究机构：以色列理工学院、以色列内盖夫本-古里安大学

作者：Guy Bar-Shalom、Ami Tavory、Itay Evron 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.16316)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.16316)

> 权重空间模型旨在直接从神经网络参数预测其属性，但现有方法多针对标量权重设计的多层感知机（MLP），无法处理柯尔莫哥洛夫-阿诺德网络（KAN）中函数型边缘参数。本文切入点在于证明KAN具备与MLP相同的神经元置换对称性，并据此构建将B样条系数映射为边特征的KAN-graph。通过在该图上运行图神经网络（GNN），WS-KAN实现了单次前向传播下的精度预测与剪枝。该架构在低维任务上显著优于结构无关基线，但在高维图像任务上性能衰减明显，其对称性假设在复杂拓扑下的泛化边界尚存疑。

】

---

【Improving Set Function Approximation with Quasi-Arithmetic Neural Networks ｜准算术神经网络

研究机构：加拿大多伦多大学、加拿大向量研究所

作者：Tomas Tokar、Scott Sanner

论文原文见 [arXiv](https://arxiv.org/abs/2602.04941)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.04941)

> 集合函数近似面临的核心矛盾是：固定池化操作（如求和、最大）迫使编码器为特定聚合方式定制特征，导致表示缺乏通用性与迁移能力。现有可学习聚合方法（如HPDS）仅参数化幂平均指数，表达力受限，且未解决梯度传播中的维度坍缩问题。本文通过引入逆神经网络实现可学习的柯尔莫哥洛夫均值，将池化操作从固定算子升级为可训练的非线性变换，在理论上证明了对Wasserstein度量下连续函数的通用逼近性，并实证了编码器迁移性的显著提升。其价值在于解耦了编码器与聚合算子的绑定，但sum-decomposable函数的近似误差随集合大小线性增长的局限，限制了其在大规模计数任务中的适用性。

】

---

【INITIALIZATION SCHEMES FOR KOLMOGOROV ARNOLD NETWORKS: AN EMPIRICAL STUDY ｜样条 KAN 的初始化策略：方差保持与幂律缩放

研究机构：美国加州理工学院

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_19591112)

> 柯尔莫哥洛夫-阿诺德网络（Kolmogorov-Arnold Networks, KANs）在深层堆叠时面临信号方差逐层衰减或爆炸的训练不稳定问题，现有文献仅针对 Chebyshev 变体提供了初始化方案，标准样条架构缺乏系统性研究。本文切入点在于将 MLP 领域的方差保持理论适配至样条基函数，并引入经验幂律缩放作为补充。通过推导基于样条期望值的方差保持公式及网格搜索确定的幂律指数，本文在函数拟合与偏微分方程（PDE）基准上验证了初始化对收敛速度的决定性影响。该工作填补了样条 KAN 初始化的空白，但其结论受限于低维任务，高维场景下的有效性存疑。

】

---

【Initialization Schemes for Kolmogorov-Arnold Networks: An Empirical Study ｜柯尔莫哥洛夫-阿诺德网络初始化策略的系统性实证研究

研究机构：美国加州理工学院

作者：Spyros Rigas、Dhruv Verma、Georgios Alexandridis 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.03417)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.03417)

> 柯尔莫哥洛夫-阿诺德网络（Kolmogorov-Arnold Networks, KANs）在科学计算任务中展现出超越多层感知机（MLP）的精度，但其训练稳定性长期受限于权重初始化的随意性。现有文献主要沿用原始论文中的简单高斯分布初始化，缺乏针对B样条基函数特性的理论推导与大规模实证验证。本文通过推导方差保持初始化公式并引入经验幂律缩放，系统评估了不同初始化策略对KAN训练动力学的影响。该研究填补了标准样条KAN初始化研究的空白，但其在高维视觉任务上的泛化能力及与特定架构变体的兼容性仍存疑。

】

---

【Lookup multivariate Kolmogorov-Arnold Networks ｜查找表多变量柯尔莫哥洛夫-阿诺德网络

研究机构：瑞士洛桑联邦理工学院

作者：Sergey Pozdnyakov、Philippe Schwaller

论文原文见 [arXiv](https://arxiv.org/abs/2509.07103)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.07103)

> 现代深度学习模型的推理成本主要由高维线性映射主导，其计算量与参数量均随层宽呈二次方增长，限制了大模型的部署效率。现有KAN变体虽通过可学习边缘函数提升了逼近精度，但普遍依赖De Boor迭代或密集基函数，导致推理开销高昂且难以在GPU上高效并行。本文提出lmKANs，将标准KAN的一元函数替换为二阶B样条参数化的二维多元函数，并实现为静态百分位网格上的查找表，从而在保持通用逼近性的同时实现O(1)推理。该架构在推理FLOPs-精度平面上展现出Pareto最优性，但其效率增益高度依赖任务维度，且在大规模视觉任务中尚未超越成熟CNN架构。

】

---

【ON THE CONVERGENCE OF TWO-LAYER - KOLMOGOROV-ARNOLD NETWORKS WITH FIRST LAYER TRAINING ｜两层柯尔莫哥洛夫-阿诺德网络单层训练收敛性分析

研究机构：伊朗谢里夫理工大学

作者：Seyed Mohammad Eshtehardian、Mohammad Hossein Yassaee、Babak HosseinKhalaj

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_74745429)

> 过参数化神经网络的优化理论长期依赖宽度与样本量的多项式关系，但现有针对柯尔莫哥洛夫-阿诺德网络（Kolmogorov-Arnold Networks, KANs）的全层训练分析未能揭示其参数效率优势。本文切入点在于将训练约束简化为仅更新第一层系数，从而在更严格的条件下推导收敛保证。通过构建KAN切线核（KAN Tangent Kernel, KAN-TK）并分析其谱结构，证明了梯度下降在宽度 $O(n^2)$ 下即可收敛至全局最小值。该工作填补了KAN优化理论的空白，但其结论局限于单层训练与RBF基函数，对深层或混合基函数的适用性存疑。

】
