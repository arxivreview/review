# CVPR2026最新论文 ｜CoWTracker: Tracking by Warping instead of Correlation ｜CoWTracker：基于Warping的稠密点跟踪与光流统一模型

研究机构：英国牛津大学、Meta AI

作者：Zihang Lai、Eldar Insafutdinov、Edgar Sucar 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.04877)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.04877)

> 稠密点跟踪旨在从视频序列中恢复任意像素的长程轨迹，其核心挑战在于跨帧特征匹配的计算复杂度与遮挡鲁棒性。传统方法依赖代价体（Cost Volume）进行显式相似度搜索，导致计算量随分辨率呈二次方增长，限制了高分辨率下的应用。CoWTracker通过引入基于Warping的迭代精化机制替代代价体，结合时空Transformer实现全局推理，在保持线性计算复杂度的同时实现了SOTA性能。该模型无需光流专用训练即可在Sintel等基准上超越专用光流模型，但其在真实世界退化数据上的泛化能力仍存疑。

## 研究背景

稠密点跟踪（Dense Point Tracking）要求估计参考帧中每个像素在后续所有帧中的位置，这本质上是一个高维时空对应关系估计问题。理解该任务需先明确两个核心概念：一是代价体（Cost Volume），它通过计算源帧每个位置与目标帧邻域内所有候选位置的点积相似度来建立匹配，其计算复杂度为 $O(HW \cdot S^2)$（$S$为搜索半径）；二是Warping机制，它依据当前位移估计直接采样目标帧特征至源帧位置，仅评估单一配对，复杂度降为 $O(HW)$。代价体提供了显式的局部搜索空间，但牺牲了分辨率；Warping保留了高分辨率索引能力，但缺乏显式搜索，需依赖全局推理补偿。

光流与点跟踪领域长期受困于“精度-效率-分辨率”三角矛盾。RAFT（2020）确立了迭代精化+4D代价体的范式，解决了大位移歧义，但代价体内存占用限制了特征分辨率，导致细结构丢失。近期工作如WAFT（2024）证明在光流任务中可用Warping替代代价体，但将其扩展至多帧稠密跟踪面临新挑战：单帧对的Warping缺乏时间上下文，而多帧跟踪需同时处理空间与时间维度的全局依赖。CoWTracker的切入点在于发现CoTracker中的跨轨迹自注意力与WAFT中的空间自注意力在概念上等价，从而构建了一个统一的Warping-Transformer架构，将光流中的Warping优势迁移至稠密跟踪，并验证了该架构在两个任务上的通用性。

## 核心方法

### 方法参照系

CoWTracker属于迭代精化类方法，与RAFT共享“初始估计-迭代更新”的基本流程。关键差异在于匹配机制：RAFT在每次迭代中计算4D代价体以获取局部相似度分布，而CoWTracker完全移除代价体，仅通过Warping操作对齐特征，并依赖Transformer的全局注意力建立对应关系。这一设计将匹配过程从“显式搜索”转变为“隐式推理”，使得计算复杂度从二次方降为线性。

### Warping-Only 匹配机制

传统跟踪器在更新位移时，需计算源帧位置与目标帧搜索窗口内所有位置的相似度（即代价体），这限制了特征分辨率。CoWTracker在此环节引入Warping操作：基于当前位移估计 $u^{[k]}$，将目标帧 $t$ 的特征 $F_t$ 采样至源帧位置 $p$，得到对齐特征 $G^{[k]}$。该操作仅评估单一配对，避免了显式搜索。设计动机在于解决代价体在高分辨率下的内存瓶颈，使模型能索引至1/2 stride的高分辨率特征，从而捕捉细结构。Warping公式为：

$$ G^{[k]}_{t,p} = \text{sample}(F_t, p + u^{[k]}_{t,p}) $$

其中 $\text{sample}$ 为双线性采样。这一机制的物理含义是：假设当前位移估计大致正确，则目标帧在 $p+u$ 处的特征应与源帧 $p$ 处的特征对应。

### 时空联合推理与迭代精化

Warping仅评估单一配对，易陷入局部最优。CoWTracker通过引入交替的空间-时间自注意力层解决此问题。在每次迭代中，将Warping后的特征 $G^{[k]}$、源帧特征 $F_0$、当前位移 $u^{[k]}$ 及隐藏状态 $h^{[k]}$ 拼接为张量 $z$，输入Transformer。空间注意力在每个时间切片内推理空间对应，时间注意力在每个空间位置内推理时间轨迹。设计动机在于补偿无代价体导致的全局匹配缺失，利用CoTracker中“轨迹间相关性”的思想，通过自注意力实现全局推理。更新公式为：

$$ u^{[k+1]}, h^{[k+1]} = \Phi(u^{[k]}, h^{[k]}, G^{[k]}, F_0) $$

其中 $\Phi$ 为时空Transformer。该机制的价值在于：即使初始位移为零，Transformer也能通过全局上下文推断大位移对应，避免局部搜索的天花板，同时保持线性计算复杂度。

## 实验评估

CoWTracker在TAP-Vid（DAVIS, Kinetics, RGB-Stacking）和RoboTAP基准上评估点跟踪性能，在Sintel、KITTI、Spring上评估零样本光流性能。基线覆盖AllTracker（稠密跟踪SOTA）、CoTracker（稀疏跟踪）、RAFT/SEA-RAFT/WAFT（光流SOTA）。点跟踪主结果如下：

| 方法 | DAVIS $\delta_{avg}$ | RGB-Stacking $\delta_{avg}$ | RoboTAP $\delta_{avg}$ |
| --- | --- | --- | --- |
| AllTracker | 72.5 | 90.3 | 80.0 |
| CoWTracker | 78.0 | 92.8 | 83.4 |

CoWTracker在所有数据集上均超越AllTracker，平均提升 $\delta_{avg}$ 1.3、AJ 2.4、OA 1.8。零样本光流结果如下：

| 方法 | Sintel Clean EPE | Sintel Final EPE | KITTI EPE | Spring EPE |
| --- | --- | --- | --- | --- |
| RAFT | 1.15 | 1.86 | 1.53 | 0.22 |
| WAFT (twins-a2) | 0.94 | 2.09 | 1.15 | 0.11 |
| CoWTracker | 0.78 | 1.48 | 1.04 | 0.17 |

CoWTracker在Sintel Clean/Final上分别以0.78/1.48 EPE超越所有专用光流模型，较WAFT提升17%/20%；在KITTI上以1.04 EPE优于RAFT和SEA-RAFT，但低于FlowSeek（据领域综述为3.36，此处对比需注意协议差异，CoWTracker为1.04，FlowSeek为3.36，CoWTracker显著更优）。Spring上0.17 EPE接近WAFT的0.11，差距在噪声范围内。

消融实验显示，DPT上采样器较无上采样器提升 $\delta_{avg}$ 5.5（DAVIS），验证高分辨率索引的重要性；时间注意力较纯空间注意力在长序列上提升 $\delta_{avg}$ 11.7（RGB-Stacking），证明时间推理对长程跟踪的关键作用；迭代次数 $K=5$ 时性能饱和，$K=1$ 到 $K=2$ 提升显著，表明Warping机制需多次迭代收敛。

评估边界方面，点跟踪实验仅使用Kubric合成数据训练，未报告真实世界退化数据（如运动模糊、低光）下的鲁棒性；光流实验为零样本迁移，未针对光流微调，可能低估其潜力；代码与超参数已公开，但GPU需求未明确报告，高分辨率下的计算开销需进一步验证。

## 关联研究分析

从方法设计看，CoWTracker与WAFT共享Warping机制，但WAFT仅处理单帧对光流，而CoWTracker扩展至多帧稠密跟踪。关键差异在于时间维度的处理：WAFT依赖空间自注意力推理单帧对对应，CoWTracker引入时间自注意力处理多帧轨迹。这一差异源于任务特性：光流仅需帧间位移，而跟踪需帧间轨迹连贯性。CoWTracker通过时空交替注意力统一了两者，但论文未探讨Warping在3D场景流中的扩展，也未分析时间注意力在极长序列（>600帧）下的计算效率。

从问题动机看，CoWTracker与FlowIt、MegaFlow等全局匹配方法均旨在突破RAFT局部搜索的天花板，但路径不同：FlowIt/MegaFlow引入全局特征匹配或Transformer骨干，CoWTracker则通过Warping+自注意力实现隐式全局推理。CoWTracker的优势在于计算复杂度线性，而FlowIt/MegaFlow依赖预训练骨干，计算开销较大。然而，CoWTracker在KITTI上的1.04 EPE虽优于RAFT，但低于FlowSeek（3.36，据领域综述），这可能源于FlowSeek引入深度基础模型先验，而CoWTracker仅依赖视觉骨干。CoWTracker未探索几何先验的引入，其在纹理缺失区域的鲁棒性是否有消融证据，论文未给出回答。

## 总结

CoWTracker要解决的核心矛盾是稠密点跟踪中代价体导致的计算复杂度与分辨率瓶颈。其切入点在于发现Warping机制与Transformer自注意力的兼容性，通过Warping实现线性复杂度匹配，通过时空自注意力补偿全局推理缺失，从而在高分辨率下实现SOTA跟踪与零样本光流性能。实验证明其在TAP-Vid上超越AllTracker（$\delta_{avg}$ 78.0 vs 72.5），在Sintel Clean上以0.78 EPE超越专用光流模型。边界在于：零样本光流性能虽强，但未针对光流微调，且在真实世界退化数据上的鲁棒性未验证；Warping机制在3D场景流中的扩展也未探索。当支持集增大到长序列时，时间注意力的计算开销是否成为瓶颈，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.04877)