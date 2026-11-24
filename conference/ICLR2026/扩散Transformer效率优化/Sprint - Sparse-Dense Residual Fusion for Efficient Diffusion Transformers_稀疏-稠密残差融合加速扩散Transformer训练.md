# ICLR2026最新论文 ｜Sprint: Sparse-Dense Residual Fusion for Efficient Diffusion Transformers ｜稀疏-稠密残差融合加速扩散Transformer训练

研究机构：韩国高丽大学、韩国科学技术院

作者：Dogyun Park、Moayed Haji-Ali、Yanyu Li 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.21986)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.21986)

> 扩散Transformer（DiT）训练成本随序列长度呈二次方增长，导致大规模预训练在算力与内存上不可承受。现有Token丢弃方法在高丢弃率下表示退化严重，且难以与外部监督信号兼容。本文提出SPRINT，通过将DiT解耦为稠密浅层路径与稀疏深层路径并引入残差融合，在75% Token丢弃率下保持生成质量，并衍生出Path-Drop Guidance（PDG）推理加速机制。该方法在训练效率上取得显著突破，但其静态丢弃策略在动态场景中的泛化能力存疑。

## 研究背景

DiT架构中，注意力计算复杂度与Token数量 $N$ 呈 $O(N^2)$ 关系，这使得高分辨率图像或长视频生成时的训练开销急剧上升。为降低计算量，一种直观策略是减少参与计算的Token数量，即Token丢弃。然而，直接随机丢弃Token会导致特征图出现大面积空洞，破坏局部连续性，使得模型在推理时面对完整Token输入时泛化能力大幅下降。此外，深层网络中Token特征往往包含大量冗余的局部细节，对全局语义建模贡献有限，但标准DiT的均匀架构迫使所有层处理全量Token，造成计算资源浪费。

现有Token丢弃方法如MDTv2、MaskDiT和Tread主要支持中等丢弃率（≤50%），在激进设置（如75%）下性能显著退化。这些方法要么引入额外参数（如MicroDiT的patch-mixer），要么增加推理成本（如MaskDiT的辅助解码器），且难以与表示对齐损失（如REPA）结合使用。SPRINT的切入点在于利用浅层与深层网络的互补特性：浅层擅长捕捉局部细节，深层擅长建模全局语义。通过架构重构，让浅层处理全量Token以保留局部信息，深层仅处理稀疏Token以聚焦全局结构，并通过残差连接融合两者，从而在高丢弃率下维持表示鲁棒性。

## 核心方法

### 方法参照系

本文问题属于“训练加速与架构改进”路线，核心差异在于：不同于推理时的动态稀疏注意力，SPRINT在训练阶段引入静态稀疏-稠密双路径结构，通过架构解耦而非算法调度来消除计算冗余。

### 稀疏-稠密残差融合架构

传统DiT中所有层处理全量Token，导致深层计算冗余。SPRINT将DiT划分为编码器 $f_\theta$（前2块）、中间块 $g_\theta$ 和解码器 $h_\theta$（后2块）。编码器处理全量Token生成稠密浅层特征 $\mathbf{f}_t$，随后丢弃比例 $r$（通常75%）的Token，仅保留稀疏子集输入中间块 $g_\theta$ 生成稀疏深层特征 $\mathbf{g}_{t}^{drop}$。为对齐维度，将丢弃位置填充为固定[MASK] token $\mathbf{M}$，得到 $\mathbf{g}_{t}^{pad}$。最终通过通道拼接与投影融合稠密浅层特征与稀疏深层特征：

$$
\mathbf{z}_t = \text{Proj}([\mathbf{f}_t; \mathbf{g}_{t}^{pad}])
$$

该公式的物理含义是：将保留局部细节的稠密特征与聚焦全局语义的稀疏特征在通道维度上合并，使解码器能同时获取两种互补信息。这一设计解决了此前方法在高丢弃率下因局部信息丢失导致的表示退化问题，实现了75%丢弃率下的稳定训练。

### Path-Drop Guidance (PDG)

标准Classifier-Free Guidance (CFG) 需两次完整前向传播（条件与无条件），推理成本翻倍。SPRINT的双路径结构天然包含一个“弱网络”：仅使用稠密浅层路径而绕过中间块 $g_\theta$。PDG利用此特性，无条件估计仅通过稠密浅层路径计算：

$$
v_\theta(\mathbf{x}_t, \emptyset) = h_\theta(\text{Fusion}(\mathbf{M}, f_\theta(\mathbf{x}_t, \emptyset)), \emptyset)
$$

该公式表明：无条件速度场仅依赖编码器特征与[MASK] token，无需执行计算密集的中间块。这一创新将推理FLOPs降低近50%，同时因避免了深层噪声干扰，生成质量反而优于标准CFG。

## 实验评估

| 方法 | Epochs | Training TFLOPs (×10⁶) | Inference TFLOPs | FDD ↓ | FID ↓ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| SiT-XL† | 400 | 122.2 | 0.474 | 79.5 | 2.04 |
| +SPRINT | 200 | 43.7 | 0.477 | 79.0 | 2.01 |
| +SPRINT | 400 | 65.1 | 0.477 | 75.4 | 1.96 |
| +SPRINT_PDG | 400 | 65.1 | 0.274 | 58.4 | 1.62 |
| +SPRINT_PDG‡ | 400 | 65.1 | 0.263 | 54.9 | 1.55 |

实验在ImageNet-1K 256×256上进行，基线覆盖SiT、REPA、MDTv2、MaskDiT、Tread等主流方法，但未对比推理加速类方法（如SpargeAttention）。SPRINT在200 epochs即达到与SiT 400 epochs相当的FDD（79.0 vs 79.5），400 epochs时FDD降至75.4，训练TFLOPs仅为SiT的53%。引入PDG后，推理TFLOPs降至0.274，FID进一步降至1.62，结合guidance schedule后FID达1.55，显著优于基线。

| Drop Ratio r | FID ↓ |
| :--- | :--- |
| 0% | 54.1 |
| 25% | 43.2 |
| 50% | 32.3 |
| 75% | 27.5 |
| 87.5% | 50.2 |

消融实验显示，丢弃率从0%增至75%时，FID从54.1持续降至27.5，表明适度稀疏促进浅层与深层的互补交互。然而，87.5%丢弃率下FID反弹至50.2，说明过度稀疏限制了模型表达能力。此外，结构化分组采样（Structured）比随机采样（Random）FID低2.6（27.5 vs 30.1），验证了局部覆盖的重要性。

评估指标包含FDD、FID、IS、Precision、Recall，协议完备。但实验仅覆盖图像生成，未验证视频或高分辨率场景；代码未公开，超参数细节有限，可复现性依赖附录。

## 关联研究分析

从问题动机看，SPRINT与REPA（Yu et al., 2024）均旨在加速DiT收敛，但REPA依赖外部DINOv2特征对齐，可能引入训练不稳定性（Wang et al., 2025指出对齐信号与扩散目标冲突），而SPRINT通过架构内部稀疏-稠密解耦实现加速，无需外部监督，且与REPA互补（组合后FDD提升17.8）。这一差异源于任务特性：REPA适用于有强预训练视觉编码器可用的场景，SPRINT则更通用，适用于缺乏外部监督或需保持架构简洁的场景。

从方法设计看，SPRINT与Tread（Krause et al., 2025）同属Token丢弃路线，但Tread通过绕过部分Token优化全去噪损失，仅支持中等丢弃率；SPRINT通过残差融合保留局部信息，支持75%高丢弃率。根源在于Tread未显式建模浅层与深层的特征互补性，而SPRINT通过架构解耦强制浅层专注局部、深层专注全局，从而在高稀疏度下维持表示完整性。

## 总结

SPRINT解决的核心矛盾是DiT训练成本随序列长度二次方增长与高丢弃率下表示退化的冲突。其切入点在于利用浅层与深层网络的互补特性，通过稀疏-稠密残差融合架构，在75% Token丢弃率下保持生成质量，并衍生出PDG推理加速机制。实验证明，SPRINT在ImageNet-1K上实现9.8×训练成本降低，FID达1.55（结合PDG与guidance schedule），显著优于基线。其边界在于静态丢弃策略未考虑内容动态性，且在87.5%丢弃率下性能骤降，表明稀疏度存在上限。当输入内容具有高度时空动态性（如视频）时，静态75%丢弃率是否仍能维持局部-全局互补性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.21986)