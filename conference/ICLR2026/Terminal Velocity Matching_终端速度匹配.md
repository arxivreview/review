# ICLR2026最新论文 ｜Terminal Velocity Matching ｜终端速度匹配

作者：Linqi Zhou、Mathias Parger、Ayaan Haque 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.19797)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.19797)

> 扩散模型与流匹配（Flow Matching, FM）虽能生成高质量样本，但依赖数十次前向传播，难以满足实时推理需求。现有单阶段少步生成方法多聚焦于匹配轨迹初始时间的导数，缺乏对生成分布质量的显式理论保证，且大规模训练时易因网络非Lipschitz连续性导致不稳定。TVM将导数匹配对象从初始时间转移至终端时间，通过单样本Jacobian-Vector Product（JVP）计算实现分布级对齐，并引入架构级Lipschitz约束稳定训练。该框架在ImageNet上实现了单步与少步生成的SOTA性能，但其对网络容量的依赖及CFG权重随机采样引发的性能退化，提示了少步生成中质量-多样性权衡的深层机制。

## 研究背景

当生成模型试图在单次前向传播内完成从噪声到数据的映射时，其核心困境在于如何精确拟合复杂的多模态数据分布。流匹配（Flow Matching, FM）通过构建连续时间速度场，将生成过程建模为常微分方程（ODE）的积分，为少步生成提供了连续时间框架。然而，直接学习该积分映射（即位移图）的传统方法，如一致性模型（Consistency Models, CM）和MeanFlow，主要依赖匹配轨迹在初始时间点的导数。这种逐点轨迹模仿缺乏与生成分布散度（如Wasserstein距离）的显式联系，导致模型在少步生成时易丢失高频细节，且难以从理论上保证分布保真度。

为弥补分布保证的缺失，分布匹配蒸馏（Distribution Matching Distillation, DMD）等方法通过最小化KL散度对齐分布，显著提升了保真度，但引入了模式坍缩风险，且通常依赖预训练教师模型。另一条路线如归纳矩匹配（Inductive Moment Matching, IMM）虽提供了分布级保证，但要求每个训练步使用多个粒子，限制了在大规模模型上的可扩展性。此外，现代扩散Transformer（DiT）由于缺乏Lipschitz连续性，在少步训练的高阶梯度反向传播中极易出现激活值爆炸与训练不稳定。TVM的切入点在于：能否通过改变导数匹配的时间锚点（从初始转向终端），在单样本、单阶段训练下，同时获得分布级理论保证与训练稳定性？

## 核心方法

### 方法参照系：流匹配与位移图学习

在标准流匹配框架中，给定数据分布 $p_0(\mathbf{x}_0)$ 和先验分布 $p_1(\mathbf{x}_1)$，通过线性插值 $\mathbf{x}_t = (1-t)\mathbf{x}_0 + t\mathbf{x}_1$ 构建条件速度 $\mathbf{v}_t = \mathbf{x}_1 - \mathbf{x}_0$。神经网络 $\mathbf{u}_\theta(\mathbf{x}_t, t)$ 通过回归该速度场来近似真实速度 $\mathbf{u}(\mathbf{x}_t, t)$。推理时，通过求解ODE $\frac{d}{dt}\mathbf{x}_t = \mathbf{u}(\mathbf{x}_t, t)$ 实现从先验到数据的传输。少步生成的目标是直接学习从任意时间 $t$ 到 $s$ 的位移图 $\psi(\mathbf{x}_t, t, s)$，即净位移 $\mathbf{f}(\mathbf{x}_t, t, s) = \psi(\mathbf{x}_t, t, s) - \mathbf{x}_t$。传统方法通常通过匹配 $\frac{d}{dt}\mathbf{f}_\theta$ 来约束该位移，而TVM则重构了这一约束的施加位置。

### 终端速度匹配与分布保证

TVM的核心创新在于将导数匹配从初始时间 $t$ 转移至终端时间 $s$。对于真实净位移 $\mathbf{f}(\mathbf{x}_t, t, s)$，其关于终端时间 $s$ 的导数满足终端速度条件：

$$
\frac{d}{ds}\mathbf{f}(\mathbf{x}_t, t, s) = \mathbf{u}(\mathbf{x}_s, s)
$$

该公式表明，若模型在终端时间的速度预测与真实速度场一致，则其累积位移必然匹配真实轨迹。TVM通过最小化终端速度误差来间接约束位移图，其训练目标为：

$$
\mathcal{L}_{\text{TVM}}(\theta) = \mathbb{E}_{t, s, \mathbf{x}_t} \left[ \left\| \frac{\partial}{\partial s} \mathbf{f}_\theta(\mathbf{x}_t, t, s) - \mathbf{u}_{\theta_{\text{sg}}}(\mathbf{x}_s, s) \right\|_2^2 \right]
$$

其中 $\mathbf{u}_{\theta_{\text{sg}}}$ 为停止梯度的代理网络。这一设计动机在于：匹配终端速度不仅规避了MeanFlow等初始速度匹配方法中因引入条件速度 $\mathbf{v}_t$ 带来的高方差与梯度波动，更关键的是，论文证明该目标函数的加权积分构成了数据分布与模型分布之间2-Wasserstein距离的上界。这意味着TVM在单样本训练下即可提供分布级对齐保证，无需IMM的多粒子采样开销。

### Lipschitz架构约束与JVP高效计算

终端速度匹配的理论成立依赖于速度场 $\mathbf{u}_\theta$ 的Lipschitz连续性，但标准DiT中的缩放点积注意力（SDPA）和LayerNorm（LN）破坏了这一性质，导致训练时激活值剧烈波动。TVM引入最小化架构修改以强制Lipschitz约束：将LN替换为无参数的RMSNorm，并在注意力层采用RMSNorm-based QK-Norm；对AdaLN中的调制参数 $a(t), b(t)$ 施加RMSNorm约束，防止其模长无界增长。

此外，终端速度计算涉及对网络输出关于 $s$ 的Jacobian-Vector Product（JVP），且梯度需反向传播通过JVP项。标准PyTorch自动微分对SDPA的JVP支持效率低下。TVM开发了融合JVP前向计算与反向传播的Flash Attention内核，相比标准实现提速65%并显著降低显存占用。针对CFG训练，TVM引入缩放参数化 $\mathbf{f}_\theta = (s-t)w\mathbf{F}_\theta$，使网络输出自然随CFG权重 $w$ 线性缩放，并在损失中引入 $1/w^2$ 权重防止梯度爆炸，实现了无需课程学习的稳定CFG训练。

## 实验评估

实验在ImageNet-256×256与ImageNet-512×512上进行，评估指标为FID。基线覆盖包括从零训练的轨迹匹配方法（MeanFlow, sCT）及扩散基线（DiT），但未包含DMD系列分布蒸馏方法。TVM在单步与4步生成上均展现出竞争力，尤其在4-NFE设定下超越了标准DiT基线。

| 方法 | 数据集 | NFE | FID |
| --- | --- | --- | --- |
| TVM | ImageNet-256 | 1 | 3.29 |
| MeanFlow | ImageNet-256 | 1 | 3.43 |
| TVM | ImageNet-256 | 4 | 1.99 |
| DiT | ImageNet-256 | 4 | 2.27 |
| TVM | ImageNet-512 | 1 | 4.32 |
| TVM | ImageNet-512 | 4 | 2.94 |
| DiT | ImageNet-512 | 4 | 3.04 |

消融实验揭示了CFG采样策略与参数化对性能的非线性影响。随机CFG采样虽能提升1-NFE性能，但会损害2-NFE性能，且高CFG权重下FID出现退化，表明网络容量在拟合多NFE质量时存在瓶颈。缩放参数化在 $w=2$ 时显著优于无缩放版本（1-NFE FID从3.82降至3.72），验证了输出缩放与CFG线性特性的匹配性。EMA率 $\gamma=0.99$ 为最优设置，过低或过高均导致性能下降。

| 消融项 | 配置 | 1-NFE FID | 2-NFE FID |
| --- | --- | --- | --- |
| 缩放参数化 | yes, $w=2$ | 3.72 | 3.35 |
| 缩放参数化 | no, $w=2$ | 3.82 | 3.27 |
| 缩放参数化 | yes, $w=1.5$ | 6.04 | 4.60 |
| 缩放参数化 | no, $w=1.5$ | 9.32 | 7.02 |

评估边界方面，论文未报告置信区间，且未提供代码开源链接，复现依赖对JVP Flash Attention内核的自行实现。此外，实验未评估多样性指标（如Intra-LPIPS），无法验证TVM在分布保真度提升的同时是否伴随模式坍缩。

## 关联研究分析

从导数匹配的时间锚点看，TVM与MeanFlow构成对偶关系。MeanFlow匹配初始时间导数 $\frac{d}{dt}\mathbf{f}_\theta$，需将真实速度 $\mathbf{u}(\mathbf{x}_t, t)$ 替换为条件速度 $\mathbf{v}_t$，引入额外方差；TVM匹配终端时间导数 $\frac{d}{ds}\mathbf{f}_\theta$，直接对齐边际速度场，规避了方差问题。这一差异的根源在于终端速度条件天然与FM损失在 $t=s$ 时兼容，而初始速度匹配需额外处理边界条件。TVM是否在所有数据分布下均优于初始匹配，论文未给出理论证明。

从分布保证的实现路径看，TVM与IMM目标一致但机制迥异。IMM通过多粒子采样计算Maximum Mean Discrepancy（MMD）实现分布对齐，计算开销随粒子数线性增长；TVM通过单样本JVP计算终端速度误差，间接上界Wasserstein距离。这一差异源于TVM对Lipschitz连续性的强依赖——IMM无需此假设，但TVM通过架构修改强制满足该条件，以换取单样本可扩展性。Lipschitz约束是否限制了模型拟合高度多模态分布的能力，论文未通过极端多模态数据集进行验证。

## 总结

TVM针对少步生成中分布保证缺失与训练不稳定的双重矛盾，提出将导数匹配从初始时间转移至终端时间，通过单样本JVP计算实现Wasserstein距离上界约束，并引入Lipschitz架构修改与融合JVP内核解决DiT训练稳定性问题。在ImageNet-256上，TVM实现1-NFE FID 3.29与4-NFE FID 1.99，超越MeanFlow与DiT基线。其边界在于CFG随机采样引发的多NFE性能权衡，以及Lipschitz约束对复杂分布拟合的潜在限制。当网络容量成为拟合多NFE质量的瓶颈时，终端速度匹配是否需引入容量感知的自适应CFG调度以突破当前性能上限，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.19797)