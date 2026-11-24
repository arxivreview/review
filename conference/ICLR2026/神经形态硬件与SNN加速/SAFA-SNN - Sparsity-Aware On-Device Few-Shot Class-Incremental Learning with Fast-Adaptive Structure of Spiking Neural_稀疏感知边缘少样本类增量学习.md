# ICLR2026最新论文 ｜SAFA-SNN: Sparsity-Aware On-Device Few-Shot Class-Incremental Learning with Fast-Adaptive Structure of Spiking Neural Network ｜稀疏感知边缘少样本类增量学习

研究机构：浙江大学、新加坡国立大学

作者：Huijing Zhang、Muyang Cao、Linshan Jiang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.03648)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.03648)

> 边缘设备在动态环境中需持续学习新类别，但受限于内存与算力，无法部署依赖大规模预训练模型的传统人工神经网络（ANN）少样本类增量学习（Few-Shot Class-Incremental Learning, FSCIL）方案。现有脉冲神经网络（Spiking Neural Network, SNN）研究多聚焦于静态推理或离线训练，缺乏在资源受限设备上应对灾难性遗忘与过拟合的在线增量机制。SAFA-SNN通过稀疏感知动态阈值、零阶优化与原型子空间投影，实现了SNN在通用边缘设备上的端到端FSCIL。该方法在Mini-ImageNet上较最强基线提升4.01%，且实际能耗降低20%，但其对深度网络与不平衡数据流的适应性仍存疑。

## 研究背景

边缘设备面临数据长期积累与算力受限的双重约束。当监控系统需识别新生成的异常行为时，传统FSCIL依赖冻结预训练大模型进行参数高效微调（Parameter-Efficient Fine-Tuning, PEFT），但4–12 GB的内存限制使其无法在边缘端部署。SNN利用离散脉冲通信，仅在神经元发放时触发计算，其单比特稀疏矩阵乘法天然适配边缘设备的内存与功耗预算。然而，SNN训练面临脉冲发放函数不可微的障碍，传统代理梯度（Surrogate Gradient）方法虽解决了反向传播问题，但引入了近似误差，且在增量学习场景下未考虑神经元动态对知识保持的影响。

现有SNN研究多集中于专用神经形态硬件上的静态推理或离线训练，忽视了边缘设备在实时数据流中持续更新模型的需求。ANN-based FSCIL方法（如CEC, WARP）虽在精度上表现良好，但其密集浮点运算在边缘设备上导致内存不可行。SAFA-SNN的切入点在于将SNN的稀疏性优势与FSCIL的稳定性-可塑性平衡需求结合，通过算法层面的神经元动态控制与优化策略，实现无需专用硬件的通用边缘FSCIL。

## 核心方法

### 方法参照系

FSCIL的标准流程包含基础会话训练与增量会话适应，通常冻结特征提取器，仅更新分类器原型以平衡稳定性与可塑性。本文问题与该通用流程的关键差异在于：SNN的脉冲不可微性阻断了梯度流，且神经元动态本身可作为稳定性控制机制，而非仅依赖参数冻结。

### 稀疏感知神经元动态

传统FSCIL通过冻结大部分参数防止遗忘，但SNN中神经元发放率直接影响特征表示。SAFA-SNN引入通道级掩码 $\mathbf{M}$，将神经元分为稳定与活跃两类，通过动态阈值 $\Theta$ 对齐稳定神经元的发放行为，使其与基础任务保持一致。设计动机在于：直接冻结参数在SNN中会导致脉冲稀疏性失衡，而动态阈值允许神经元在保持基础类表示的同时，为增量类保留适应性。

$$
\bar{r}_n = \frac{1}{T} \sum_{t=0}^{T} \mathbf{S}_t^{(n)}, \quad \bar{r}_b = \frac{1}{T} \sum_{t=0}^{T} \mathbf{S}_t^{(b)}
$$

该公式计算增量任务与基础任务的平均发放率，通过调整阈值使稳定神经元的 $\bar{r}_b$ 保持恒定，从而抑制新任务对基础类特征的干扰。

### 零阶优化与原型子空间投影

SNN反向传播中 $\partial U_t / \partial S_t$ 不可微，代理梯度引入误差。SAFA-SNN采用零阶优化（Zeroth-Order Optimization, ZOO），通过采样扰动点 $z_i \sim \mathcal{N}(0,1)$ 估计梯度，避免对不可微函数的直接求导。设计动机在于：ZOO仅需函数值评估，计算开销低于代理梯度的多次前向传播，且无需近似函数选择，更适合边缘设备的有限算力。

$$
\hat{\nabla} g(x) = \frac{1}{2\delta S} \sum_{i=1}^{S} g_i \cdot |z_i|
$$

该公式通过 $S$ 个随机扰动点的函数值差异估计梯度，$\delta$ 为扰动步长，$g_i$ 为指示函数，确保仅当扰动导致脉冲状态变化时贡献梯度。

增量推理中，原型均值易受少量样本偏差影响。SAFA-SNN构建基础类子空间投影矩阵 $\mathbf{G}$，将新类原型 $\tilde{\mathbf{C}}$ 映射至基础子空间，通过 $\tilde{\mathbf{P}}_{proj} = \tilde{\mathbf{C}}\mathbf{G}$ 校准预测偏差。设计动机在于：子空间投影利用基础类丰富的结构信息约束新类原型，缓解过拟合，提升泛化能力。

## 实验评估

实验在CIFAR100、Mini-ImageNet、CIFAR-10-DVS、DVS128gesture及N-Caltech101上进行，采用Spiking VGG/ResNet/Former骨干，对比CEC、WARP、TEEN等9种SNN-FSCIL基线。基线覆盖ANN-FSCIL的SNN移植版本，但缺失NEXUS等位精确等价方法，因任务目标不同（FSCIL vs 静态分类）。

| 数据集 | 方法 | Avg. (%) | Lst. (%) |
|---|---|---|---|
| Mini-ImageNet | WARP (SNN) | 38.26±1.36 | 21.30±3.96 |
| Mini-ImageNet | CLOSER (SNN) | 36.75±1.33 | 21.30±3.96 |
| Mini-ImageNet | SAFA-SNN | 59.45±0.67 | 48.70±0.67 |
| CIFAR-10-DVS | TEEN | 40.57±1.02 | 34.60±0.79 |
| CIFAR-10-DVS | SAFA-SNN | 47.56±0.94 | 36.96±0.38 |
| DVS128gesture | WARP | 35.41±1.76 | 13.02±1.25 |
| DVS128gesture | SAFA-SNN | 86.74±0.69 | 77.91±0.63 |

SAFA-SNN在Mini-ImageNet上Avg. 59.45%较WARP的38.26%提升21.19%，Lst. 48.70%较WARP的21.30%提升27.40%，表明稀疏感知动态机制显著缓解了灾难性遗忘。

消融实验显示，仅使用稀疏感知动态（SA）时性能最差，加入子空间投影（SP）后显著提升，加入零阶优化（ZOO）后达到最优。SP的边际收益最大，表明原型校准对增量学习精度的贡献超过神经元动态控制。ZOO相比代理梯度未提供直接对比数据，但其计算效率优势在Jetson Orin AGX实测中体现为20%能耗降低。

评估边界：实验假设每会话固定N-way K-shot，未测试不平衡数据流；深度网络（如Spiking ResNet-34）性能下降，暗示训练轮数不足；代码未公开，超参数（如 $\eta=0.5$, $\delta=0.5$）未提供敏感性分析，可复现性受限。

## 关联研究分析

从问题动机看，SAFA-SNN与ReckOn同属边缘SNN在线学习方向，但ReckOn依赖专用FPGA硬件实现e-prop局部学习，而SAFA-SNN在通用GPU（Jetson Orin）上通过算法优化实现增量学习。这一差异源于任务特性：ReckOn针对固定任务的持续适应，SAFA-SNN针对新类别的少样本学习，后者对原型更新机制的依赖更强，故采用子空间投影而非局部学习规则。

从方法设计看，SAFA-SNN与SpikePack均关注SNN在通用硬件上的部署效率，但SpikePack通过修改神经元模型提升GPU兼容性，SAFA-SNN通过稀疏掩码控制神经元活跃度以平衡稳定性与可塑性。SpikePack未涉及增量学习，其稀疏性优化仅针对推理阶段；SAFA-SNN的稀疏感知动态是训练-推理联合设计，其动态阈值机制在增量会话中持续调整，这一设计在数据充足时是否仍有增益，论文未给出回答。

## 总结

SAFA-SNN解决的核心矛盾是SNN在边缘设备上实现FSCIL时，稀疏性优势与增量学习稳定性-可塑性平衡的冲突。现有ANN-FSCIL方法因内存限制无法部署，而SNN静态推理缺乏在线更新能力。SAFA-SNN通过稀疏感知动态阈值、零阶优化与原型子空间投影，在通用边缘设备上实现了端到端FSCIL。实验证明其在Mini-ImageNet上Lst.精度48.70%较WARP提升27.40%，实际能耗降低20%。其边界在于固定N-way K-shot假设与深度网络性能下降，当支持集增大到5-shot时，子空间投影的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.03648)