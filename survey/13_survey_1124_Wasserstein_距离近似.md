# A Survey of Wasserstein Distance Approximations and Variants ｜Wasserstein 距离近似与变体方法综述 ｜arxivreview

综述原文见 [ArxivReview](https://www.arxivreview.com/surveys/Wasserstein%20Distance%20Approximations%20and%20Variants)

## 导读

Wasserstein 距离（Wasserstein Distance, WD）通过最小传输成本量化概率分布间的几何差异，其核心价值在于为生成模型与统计推断提供具备几何解释性的相似度度量。精确求解 WD 涉及大规模线性规划，时间复杂度高达 O(n^3 log n)，且受维度灾难制约，严重阻碍了其在高维与实时场景中的应用。为突破这一瓶颈，早期研究引入切片 Wasserstein 距离（Sliced Wasserstein Distance, SWD），利用一维闭式解将复杂度降至 O(n log n)，确立了可扩展计算范式。随着应用深入，研究重心从单纯加速转向统计一致性与几何结构保持，衍生出方差缩减、非欧空间扩展及神经嵌入等多元路线。各路线在计算效率、估计精度与几何保真度之间做出了不同取舍，由此形成当前方法并存的格局。本综述梳理这条从数值加速到几何重构的因果演进链条，为读者提供一张领域认知地图。全文按问题演化与路线取舍组织，覆盖该领域从奠基到当前的主要工作。

## 1. 研究背景、问题结构与演进脉络

Wasserstein 距离作为最优传输理论的核心产物，定义了概率分布间的最小传输成本，是衡量分布相似性的几何度量。在生成对抗网络、域适应及统计推断中，WD 能够捕捉分布的位移与形状变化，优于基于矩或密度的传统度量。然而，精确计算 WD 需求解大规模线性规划问题，时间复杂度高达 O(n^3 log n)，且高维数据下的收敛速率随维度指数恶化，即维度灾难。这一计算瓶颈使得 WD 在大规模或实时场景中几乎不可用，驱动了领域向近似与变体方向的范式转变。

问题的形式化通常涉及两个概率测度 $\mu, \nu$ 在度量空间 $(\mathcal{X}, d)$ 上的比较。在欧氏空间 $\mathbb{R}^d$ 中，$W_2(\mu, \nu)$ 定义为传输计划 $\pi$ 上的期望距离平方最小值。当样本有限时，经验测度 $\hat{\mu}_n, \hat{\nu}_n$ 与真实分布间的偏差成为核心挑战。子问题间存在严格依赖：高维计算复杂度是基础瓶颈，其解决催生了方差与偏差权衡问题；非欧几里得扩展依赖于对几何结构保持的理论突破；而可微分性则是将上述距离应用于深度学习端到端优化的前提。

2012 年至 2018 年是奠基期，核心假设是数据位于欧氏空间且样本充足。Sliced Wasserstein Distance (SWD) 的提出通过 Radon 变换将高维分布投影至一维子空间，利用一维 OT 的闭式解规避高维线性规划，确立了可扩展计算范式。随后，Sliced Wasserstein Barycenters 解决了高维质心求解难题，为生成模型提供了基础几何工具。这一时期的方法以牺牲部分高维几何细节为代价，换取了 O(n log n) 的计算效率。

2020 年至 2023 年，研究重心转向统计一致性。随着 SWD 在低数据量场景下暴露出估计不稳定性，学者开始关注有限样本偏差校正与方差缩减。ReSWD 结合水库采样降低方差，Adaptive Bayesian Optimization SWD 利用高斯过程自适应选择投影方向。这一阶段的方法不再单纯追求速度，而是试图在固定计算预算下最大化估计精度，解决了随机投影在低样本下的波动问题。

2024 年至 2026 年，领域进入几何重构阶段。Wasserstein Wormhole 等神经嵌入方法通过学习低维表示加速距离计算，而 Gromov-Wasserstein (GW) 及其切片变体开始处理图、形状等非欧数据。Busemann 函数的引入拓展了切片操作在非紧流形上的理论适用性，可观测 Wasserstein 距离则填补了非向量数据上的应用空白。当前形态表现为：欧氏空间内追求可微与并行化，非欧空间内追求结构保持与可扩展性。

**如果用一个核心问题概括该领域，那便是：如何在保持 Wasserstein 距离几何解释性与统计一致性的前提下，突破维度灾难与计算复杂度的限制，实现高维及非欧几里得空间下分布差异的高效、可微且稳健的估计。**

## 2. 方法体系

- 2012：Sliced Wasserstein Distance——确立高维分布比较的可扩展计算范式

- 2015：Sliced Wasserstein Barycenters——解决高维质心求解难题

- 2019：Wassmap——基于几何结构的图像嵌入

- 2021：Inner Product Gromov-Wasserstein——降低异质空间对齐复杂度

- 2024：Wasserstein Wormhole——基于嵌入空间的距离近似基线

- 2025：ReSWD——结合水库采样的方差缩减算法

- 2026：Tree-Sliced Sobolev IPM——增强局部几何敏感性的切片变体

这条时间线勾勒了该领域方法演进的代表性节点：从 2012 年的 Sliced Wasserstein Distance 奠定该领域方法基线，经 2015 年 Sliced Wasserstein Barycenters 的推进，到 2026 年的 Tree-Sliced Sobolev IPM 代表当前前沿。各节点对应的技术路线、取舍与关联，详见后续小节。

### 2.1 切片距离高效计算

切片距离路线起源于对高维 OT 计算瓶颈的直接回应。2012 年提出的 SWD 通过随机投影将高维问题转化为一维子问题的平均，利用一维分位数函数的闭式解大幅降低复杂度。这一范式确立了“投影-计算-聚合”的标准流程，但引入了投影方向采样的方差问题。2025 年，ReSWD（Boss et al., 2025, P7）针对随机投影在低预算下的方差波动，结合水库采样动态维护方向集合，通过自适应选择代表性方向降低估计误差，在保持计算效率的同时提升了分布匹配精度。与早期静态随机采样不同，ReSWD 将方向选择与距离估计解耦，放弃了独立同分布采样的简单性，换取了数值稳定性。

为进一步提升采样效率，Adaptive Bayesian Optimization SWD（Acharya and Hyde, 2025, P2）将切片方向视为球面黑盒函数，利用高斯过程代理模型与 UCB 采集函数自适应选择投影方向。该方法以较少的投影数量达到与随机采样相当甚至更优的精度，核心取舍在于引入 GP 后验求解的额外计算开销，换取了信息增益最大化。与此同时，Repulsive Monte Carlo on the Sphere（Petrovic et al., 2025, P1）引入负相关性采样，通过确定点过程使方向在球面均匀分布，改进了中心极限定理的收敛速率。这些方差缩减技术共同构成了切片路线的精度增强层，与基础 SWD 形成互补。

在几何结构保持方面，Tree-Sliced Wasserstein Distance (TSW) 系列方法利用树状结构捕捉局部几何。FW-TSW（ICLR 2026, P28）基于 Fermat-Weber 问题优化投影方向分布，将位置信息纳入采样过程，提升了树结构数据的估计精度。Tree-Sliced Sobolev IPM（ICLR 2026, P26）则引入 Sobolev 内积度量，增强了对局部几何结构的敏感性，适用于多模态数据与扩散模型训练。此外，Busemann Functions in Wasserstein Space（Bonet et al., 2025, P8）将 Busemann 函数引入切片操作，为非紧流形上的投影提供了几何完备性保证，拓展了理论适用性。这些方法在保留切片高效性的同时，弥补了随机投影在复杂几何结构下的不足。

| 方法类别 | 核心思想 | 计算复杂度 | 主要优势 | 主要局限 | 代表方法 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 切片距离高效计算 | 随机/自适应投影至一维 | O(n log n) | 可扩展性强，可微 | 方差依赖投影数，几何细节丢失 | SWD, ReSWD, TSW |
| 神经近似与嵌入学习 | 学习低维嵌入映射 | 训练高，推理低 | 推理速度快，支持大规模嵌入 | 依赖训练数据，泛化性挑战 | Deep Kuratowski, Wormhole |
| 广义距离变体研究 | 内在几何结构对齐 | O(n^4) 或更高 | 捕捉非欧结构，无需共享坐标 | 计算昂贵，非凸优化困难 | GW, Sliced IGW, SE(p) |
| 分布学习与统计推断 | 误差界与高斯近似 | 中等 | 提供统计保证，可解释性强 | 理论假设严格，计算复杂 | RW2 Angle, Efficient Dist. Learning |
| Wasserstein空间优化 | 测度空间梯度流/DC | 高 | 处理非凸泛函，保留几何结构 | 收敛速度波动，实现复杂 | RCD, DC Programming, WGF |

### 2.2 神经近似与嵌入学习

神经近似路线旨在通过数据驱动方法替代昂贵的精确 OT 求解。2019 年的 Wassmap 将图像视为像素分布，通过计算成对 WD 矩阵并应用 Isomap 进行降维，揭示了分布空间中的流形结构。然而，成对距离矩阵的 O(N^2) 计算开销阻碍了大规模应用。2024 年的 Wasserstein Wormhole 提出基于嵌入空间的近似模型，通过学习低维表示加速距离计算，成为当前 SOTA 的 Wasserstein 嵌入基线。

Deep Kuratowski Embedding Neural Networks（He, 2026, P17）利用神经 ODE 学习 Kuratowski 嵌入映射，将 WD 计算转化为低维欧氏空间中的距离度量。该方法通过 CNN 编码器提取特征，利用连续深度嵌入避免线性规划求解，核心取舍在于以神经 ODE 的训练复杂度换取推理速度与几何保真度。与 Wassmap 的无监督几何降维不同，Deep Kuratowski 引入了参数化映射，增强了模型对复杂分布结构的拟合能力。

Recovering Wasserstein Distance Matrices（Rana et al., 2025, P3）利用 Nyström 方法从少量测量中恢复完整距离矩阵，基于低秩假设近似未观测条目。该方法特别适用于高维数据，通过随机采样平衡精度与效率，但受限于低秩假设在内在维度较高时的近似误差。Geometry-Aware Optimal Transport Estimation（Genans and Wintenberger, 2026, P14）结合内在维度估计与 WD 计算，自适应调整采样策略，揭示了数据内在结构与传输成本的关系。这些方法共同构成了神经嵌入路线的核心，与切片路线形成竞争与互补：切片路线提供无模型解释性，神经路线提供推理速度与大规模处理能力。

### 2.3 广义距离变体研究

广义距离变体路线致力于解决非欧几里得空间（如图、形状）上的分布比较问题。Gromov-Wasserstein (GW) 距离比较两个度量测度空间内部几何结构的相似性，无需共享坐标，是处理异质数据的关键工具。然而，传统 GW 计算复杂度高达 O(n^4)，且涉及非凸优化。2021 年提出的 Inner Product Gromov-Wasserstein (IGW) 引入内积成本，使得高斯边缘分布下存在闭式解，显著降低了计算复杂度。

Sliced Inner Product Gromov-Wasserstein（Gong et al., 2026, P18）结合切片策略与 IGW，通过一维投影聚合降低非凸二次问题的求解难度，实现了异质概率空间对齐的可扩展统计距离。该方法在保留 IGW 几何解释性的同时，解决了大规模数据上的计算瓶颈。Distance-Matrix Gromov-Wasserstein（Xu and Wu, 2026, P20）提出基于距离矩阵的 GW 统计量，通过随机距离矩阵不变量实现可扩展学习，适用于图分类与两样本检验。

Gromov-Wasserstein Quantization and Clustering（Beier and Eckstein, 2026, P24）研究 GW 量化与聚类，通过近似大型对象为小型代表点集加速计算，提供了量化误差的先验界。SE(p)-Invariant Transport Metric（ICLR 2026, P27）利用极坐标传输差异构建 SE(p) 不变度量，解决点云配准中的几何不变性问题。这些方法在放弃欧氏坐标对齐假设的同时，换取了对内在几何结构的捕捉能力，与切片路线在欧氏空间形成互补，共同覆盖了从向量数据到非向量数据的完整谱系。

### 2.4 分布学习与统计推断

分布学习与统计推断路线关注从有限样本中高效重建或近似未知概率分布，并提供严格的理论保证。Efficient Distribution Learning with Error Bounds（Figueiredo et al., 2026, P15）提出基于数据依赖置信区间的误差界，通过 Clopper-Pearson 区间自动选择量化区域，避免了最坏情况假设，提升了有限样本下估计的紧致性。

Relative Wasserstein Angle and W2-Nearest Gaussian（Wang and Wei, 2026, P13）定义相对 Wasserstein 角度以量化分布的非高斯性，通过锥几何结构找到 W2 最近高斯分布。该方法将高斯近似问题转化为几何投影问题，提供了高斯近似的几何解释与高效算法。On the Information Processing of 1D Wasserstein Distances（Jang et al., 2025, P12）分析一维 WD 在有限样本下的信息处理能力，利用 Poisson 过程解析速率与支持差异的编码机制，为统计推断提供了理论依据。

Metrics for Parametric Families of Networks（Gómez et al., 2025, P6）提出参数化测度网络框架，利用 GW 距离比较不同参数空间上的测度网络，适用于分析动态网络与随机过程。这些方法在放弃无模型假设的同时，换取了统计一致性与可解释性，与优化路线形成互补：优化路线关注算法收敛，统计推断路线关注估计精度与不确定性量化。

### 2.5 Wasserstein空间优化

Wasserstein 空间优化路线研究在概率测度空间上的非凸优化问题。Random Coordinate Descent on Wasserstein Space（Xu and Li, 2026, P16）提出随机坐标下降算法，通过随机选择坐标进行传输更新，降低高维优化负担。Difference of Convex Programming in Wasserstein Space（Bonet et al., 2026, P21）提出 DC 规划算法，通过交替梯度下降与 JKO 步骤求解非凸泛函，如 MMD 优化。

Neural Local Wasserstein Regression（Girshfeld and Chen, 2025, P11）提出基于 Wasserstein 几何的非参数回归模型，利用局部核平滑估计器捕捉分布间的位移与形状变化。Wasserstein Regression via Bernstein Basis（Maslov et al., 2025, P10）提出基于 Bernstein 基的参数化回归方法，通过最小化 WD 构建平滑概率轨迹，适用于不确定性估计与轨迹预测。Wasserstein Gradient Flows for Barycenter Computation（Montesuma et al., 2025, P9）提出基于梯度流的正则化质心计算方法，通过离散化梯度流方程实现高效质心求解。这些方法在保留 Wasserstein 几何结构的同时，提供了处理非凸优化的算法框架，与切片路线在生成模型训练中形成紧密协作。

### 2.6 跨任务与多领域应用

上述方法路线已在多个领域得到验证。在生成模型中，ReSWD 与 Tree-Sliced Sobolev IPM 被用于扩散模型引导，提升了 FID 分数与训练稳定性。在网络科学中，Sliced IGW 与 Distance-Matrix GW 被用于图分类与聚类，显著提升了 ARI 指标。在生物信息学中，1D Wasserstein 距离被用于蛋白质结构分析，揭示了传输距离对点密度与支持结构的编码机制。在域适应中，Wasserstein Barycenter 与梯度流方法被用于 Office-31 与 Office-Home 数据集，提升了跨域分类准确率。这些应用表明，Wasserstein 近似方法已从理论工具演变为解决复杂数据分布比较问题的通用范式。

## 3. 关键共识、分歧与开放问题

### 3.1 领域共识

领域共识首先体现在对精确 WD 计算瓶颈的认同上。所有路线均承认 O(n^3 log n) 复杂度与维度灾难是核心驱动力，因此寻找可扩展近似方法是共同目标。SWD 作为最广泛使用的可扩展替代方案，其高效性基于一维闭式解，这一理论基础被约 25 篇论文共同支持。在有限样本下，经验 WD 估计存在偏差，特别是在高维和重尾分布情况下，需要专门的统计校正或调整，这一共识在 Adjusted SWD MDS 与 Efficient Distribution Learning 中均得到体现。

与此相关的另一个共识是 Gromov-Wasserstein 距离在处理非对齐空间比较中的关键作用。由于 GW 关注内在几何结构而非外部坐标，它成为图、形状等异质数据比较的首选工具。方差缩减技术对于提高 SWD 蒙特卡洛估计的精度至关重要，尤其是在投影方向数量有限时，ReSWD 与 Repulsive Monte Carlo 均验证了这一点。Wasserstein 空间独特的几何结构为设计基于梯度的优化算法提供了理论基础，这一共识在 RCD 与 DC Programming 中均得到应用。

### 3.2 观点分歧

投影方向的选择策略是领域内最显著的分歧。观点 A 认为随机 i.i.d. 采样足够且简单，随着维度增加，随机方向已能覆盖主要几何特征；观点 B 认为智能采样（贝叶斯、排斥、学习投影）能显著降低方差，在有限预算下精度更高。现有证据偏向观点 B，实验显示在投影数量 < 1000 时，智能采样方法的 MAE 显著低于随机采样。然而，证据强度受限于高维（>50 维）下的对比实验较少，且智能采样的额外计算开销在高维下可能抵消精度收益。这一分歧的背后，是“方差-计算成本”最优权衡点随数据分布特性变化，缺乏普适结论。

欧氏近似与内在几何的适用边界是另一个根本争论。观点 A 认为 SWD 在欧氏空间数据上已足够，GW 计算太慢，仅用于小规模特殊任务；观点 B 认为 GW 及其变体能捕捉 SWD 忽略的内在结构，是图/形状比较的唯一正确选择。证据偏向观点 B 在异质数据上，SYNTHIE 网络聚类实验中 GW 变体 ARI 显著高于基于属性的 W1。但在 MNIST 等欧氏数据上，SWD 与 GW 性能差异不大，且 SWD 速度快 10 倍以上。缺乏大规模异质数据上的 GW 可扩展性验证，使得这一争论尚未定论。

### 3.3 其他开放问题

最紧迫的工程问题是高维数据下的可扩展性优化。当前 SWD 与 GW 在高维空间中计算复杂度指数增长，难点在于投影方向选择的维度灾难与采样效率。潜在技术路径包括自适应贝叶斯优化投影、低秩协方差近似及随机坐标下降算法。最根本的研究问题是理论保证与统计收敛率分析。建立 WD 估计器在有限样本下的偏差、方差及收敛速率的严格理论界，难点在于非凸优化景观与高维统计误差的耦合。潜在技术路径包括利用内在维度估计进行去偏、分析控制变量法及矩匹配方法的渐近性质。

已知—争议—未知认知图谱显示：已知 SWD 的高效性与 GW 的结构捕捉能力；争议在于智能采样与欧氏近似的优劣权衡；未知在于非欧空间下的理论完备性与大规模可扩展性。发展趋势将从“单一距离估计”转向“几何感知的分布学习”，核心问题是如何在非欧几里得、低数据量及高维场景下，平衡计算效率、统计一致性与几何保真度。

## 4. 总结与展望

Wasserstein 距离近似领域的核心矛盾在于几何精确性与计算可扩展性之间的张力。从 2012 年 SWD 的提出到 2026 年 Tree-Sliced Sobolev IPM 的涌现，研究路线经历了从数值加速到统计校正，再到几何重构的演进。核心瓶颈已从工程实现转向理论保证与极端场景下的稳健性，特别是在非欧几里得空间与低数据量 regime 下，如何平衡计算效率、统计一致性与几何保真度仍是未解之谜。

未来可能突破的方向包括：高维数据下的自适应采样策略，结合贝叶斯优化与低秩近似，解决维度灾难；非欧几里得空间的理论完备性，通过 Busemann 函数与 SE(p) 不变度量，拓展切片操作至一般度量空间；生成模型中的可微分正则化，利用 Tree-Sliced Sobolev IPM 等变体，提升扩散模型训练稳定性。对于进入者，最值得做的一件事是在统一骨干与统一预训练条件下，系统评测智能采样策略在高维非欧数据上的“精度-效率”权衡，填补当前评测体系的空白。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/surveys/Wasserstein%20Distance%20Approximations%20and%20Variants)