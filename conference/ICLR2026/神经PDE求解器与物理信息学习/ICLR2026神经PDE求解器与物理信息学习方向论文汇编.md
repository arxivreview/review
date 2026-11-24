# ICLR2026 · 神经PDE求解器与物理信息学习方向论文汇编

> 本方向共 6 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【COMPHY: COMPOSING PHYSICAL MODELS - - WITH END TO END ALIGNMENT ｜ComPhy：基于模块对齐的PDE系统求解框架

作者：Alessandro Trenta、Andrea Cossu、Davide Bacciu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_16749114)

> 求解多方程耦合的偏微分方程（PDE）系统时，单一神经网络模型常因各方程残差损失间的梯度冲突而陷入优化停滞。现有物理信息神经网络（PINN）依赖损失加权或重采样缓解此问题，但缺乏针对系统结构的系统性解法。ComPhy将每个PDE分配给独立学习模块，并通过基于导数的对齐损失强制共享变量的一致性，从而将复杂系统优化分解为多个简单子问题。该框架在2D Navier-Stokes及MHD等系统上显著优于单模型基线，但其对高维空间及大规模工业几何的扩展能力尚未得到验证。

】

---

【DGNet: Discrete Green Networks for Data-Efficient Learning of Spatiotemporal PDEs ｜离散格林网络（DGNet）：基于结构先验的时空偏微分方程数据高效求解

研究机构：清华大学、印度数学科学研究所

作者：Yingjie Tan、Quanming Yao、Yaqing Wang

论文原文见 [arXiv](https://arxiv.org/abs/2603.01762)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.01762)

> 导读 时空偏微分方程（PDE）求解器旨在突破传统数值方法在高维与复杂几何下的计算瓶颈，但现有神经PDE求解器在数据稀缺场景下精度显著退化，根源在于架构未显式编码PDE固有的叠加原理等结构先验。本文切入点在于将格林函数理论转化为图上的离散算子，通过物理-神经混合架构将叠加结构硬编码进模型更新规则，从而降低对训练轨迹的依赖。该设计在仅数十条轨迹下实现了跨方程的SOTA精度，并展现出对未见源项的零样本泛化能力，但其对强非线性系统的适用性及大规模全量数据下的相对优势仍存疑。

】

---

【LOCALLY SUBSPACE-INFORMED NEURAL OPERATORS FOR EFFICIENT MULTISCALE PDE SOLVING ｜局部子空间感知神经算子用于高效多尺度PDE求解

研究机构：美国德州农工大学

作者：Alexander Rudikov、Vladimir Fanaskov、Sergei Stepanov 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_80082922)

> 多尺度偏微分方程（PDE）求解面临高对比度异质性导致的数值计算瓶颈，传统广义多尺度有限元法（GMsFEM）精度虽高但离线阶段求解局部特征值问题耗时巨大，而独立神经算子（NO）虽推理快却难以捕捉局部特征且对分布外数据鲁棒性差。本文切入点在于将NO的应用目标从直接预测PDE解降维为预测GMsFEM的局部基函数子空间，通过设计子空间对齐损失函数确保物理一致性。该方法在保持GMsFEM数值严谨性的同时，将基函数构建时间缩短60倍以上，但受限于结构化网格且未完全消除训练数据生成成本。

】

---

【ORTHOSOLVER: A NEURAL PROPER ORTHOGONAL DECOMPOSITION SOLVER FOR PDES ｜正交解耦求解器

研究机构：北京航空航天大学

作者：Ying Pang、Jingyuan Wang、Jiahao Ji 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_15924604)

> 导读 传统降阶模型在非线性流体动力学中因线性假设失效，而纯数据驱动算子又缺乏物理先验导致模态坍缩。本文切入点在于揭示经典正交分解（POD）本质上是高斯线性假设下的互信息最大化，从而将方差最大化推广为通用的互信息最大化目标。通过构建基于互信息估计的非线性基提取模块与正交正则化机制，OrthoSolver 实现了物理可解释性与非线性表达能力的统一。该框架在七个基准上超越了现有SOTA，但其对复杂几何与高维问题的适用性仍存疑。

】

---

【PHYSICS-INFORMED INFERENCE TIME SCALING FOR SOLVING HIGH-DIMENSIONAL PARTIAL DIFFERENTIAL EQUATIONS VIA DEFECT CORRECTION ｜结构保持缺陷定律驱动的高维PDE推理时校正

研究机构：北京大学、美国佐治亚理工学院

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_56518888)

> 高维半线性抛物型偏微分方程（PDE）求解长期受困于维度灾难，传统数值方法计算量指数级增长，而数据驱动代理模型虽能缓解此问题，却缺乏严谨的误差保证且难以在推理阶段进一步提升精度。现有方案要么依赖昂贵的全局重训练，要么在纯蒙特卡洛模拟中面临高方差瓶颈。本文切入点在于利用推理时计算资源，通过推导一个描述代理模型误差的新PDE（结构保持缺陷定律），并高效求解该缺陷方程来校正初始预测。SCaSML证明了最终误差为代理误差与模拟误差之积，实现了无需重训练的可证明收敛率加速，但在非线性项导致的模拟方差控制及与专用高维基线的对比上仍存疑。

】

---

【∂[∞] _ -GRID: A NEURAL DIFFERENTIAL EQUATION SOLVER WITH DIFFERENTIABLE FEATURE GRIDS ｜可微特征网格求解器

研究机构：德国马克斯·普朗克信息学研究所、印度理工学院

作者：Navami Kairanda、Shanthika Naik、Marc Habermann 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_32676271)

> 神经偏微分方程（PDE）求解器旨在突破传统数值方法在高维与复杂几何下的计算瓶颈，其核心价值在于以数据驱动范式替代昂贵的网格离散化。早期物理信息神经网络（PINNs）通过残差损失实现无网格求解，思路简洁却受制于优化困难与泛化局限。当傅里叶神经算子（FNO）将范式转向函数空间映射后，多查询推理效率显著提升，但长时程误差累积与分布外泛化成为新瓶颈。随后，Transformer架构与基础模型的引入，用大规模预训练换取跨方程的通用性，而扩散模型则通过概率生成机制处理不确定性。各路线在数据依赖度、物理嵌入深度与计算成本之间做出了不同取舍，由此形成当前多元并存的方法格局。本综述梳理这条从点态预测到通用物理模拟的因果演进链条，为读者提供一张领域认知地图。全文按问题演化与路线取舍组织，覆盖该领域从奠基到当前的主要工作。

】
