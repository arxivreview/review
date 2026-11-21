# HuggingFace最新推荐论文 ｜Direct3D-V3: Latent-Free Diffusion Transformers in the Native Voxel Domain ｜原生体素域无潜空间扩散生成

研究机构：南京大学

作者：Shuang Wu、Jiachen Qian、Youtian Lin 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2611.26511)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2611.26511)

> 导读：高保真三维形状生成旨在从稀疏、高噪的参考图像中合成兼具几何保真度与多视图一致性的资产，其核心矛盾在于高维数据稀缺导致的泛化受限与生成模型在单体网格输出上的固有缺陷。当前主流范式依赖变分自编码器（Variational Autoencoder, VAE）将几何压缩至潜空间，但这一过程引入了信息瓶颈与目标失配，导致细粒度几何细节在扩散模型介入前即被丢弃。Direct3D-V3 摒弃了潜空间压缩，提出在原生体素域直接对原始有符号距离场（Signed Distance Field, SDF）体素网格进行去噪扩散。该框架通过双粒度架构平衡计算效率，并引入隐式流形正则化与渲染法线监督以确保几何有效性。这一尝试挑战了“潜空间生成更高效”的领域共识，但在复杂拓扑结构上的鲁棒性仍待验证。

## 研究背景

当生成模型面对高分辨率三维几何时，直接在原始数据空间进行去噪面临立方级增长的显存开销，这促使研究转向潜空间扩散。潜空间扩散通过 VAE 将高维体素或点云压缩为紧凑的潜在表示，再由扩散模型在该低维空间中进行分布匹配。然而，这种两阶段流水线存在内在缺陷：VAE 的重建过程不可避免地丢弃高频细节，且 VAE 的重建目标与扩散模型的分布匹配目标存在失配，导致生成器受限于学习到的表示保真度。

在三维生成领域，主流方法如 TRELLIS 和 Hunyuan3D 均遵循“压缩-生成-解码”范式，尽管通过 VecSet 或稀疏体素等先进表示提升了效率，但均未突破 VAE 的信息瓶颈。早期尝试如 SDF-Diffusion 虽避免了 VAE，但受限于计算复杂度，仅能处理 $128^3$ 低分辨率。如何在去除 VAE 的同时实现高分辨率原生扩散，成为突破几何保真度上限的关键。Direct3D-V3 正是针对这一被忽略的“原生域可扩展性”问题，试图在 $1536^3$ 分辨率下验证无潜空间扩散的可行性。

## 核心方法

### 方法参照系：原生 SDF 体素扩散

标准潜空间扩散流程为“VAE 编码 -> 潜空间去噪 -> VAE 解码”。Direct3D-V3 将其替换为“原始 SDF 体素加噪 -> DiT 去噪 -> Marching Cubes 提取”。该框架将生成状态定义为均匀 SDF 体素网格 $\mathbf{X}\in\mathbb{R}^{R\times R\times R\times 1}$，其中 $R$ 为分辨率。为降低注意力机制的计算复杂度，模型将体素网格划分为大小为 $p^3$ 的非重叠补丁，生成 $(\frac{R}{p})^3$ 个补丁令牌。这一设计直接操作于几何最终被评估的信号空间，消除了重建瓶颈，但将计算效率转化为核心挑战。

### 双粒度 DiT 架构与稀疏补丁建模

为解决原生体素扩散在高分辨率下的显存爆炸问题，Direct3D-V3 采用粗到细的双粒度架构。补丁级 DiT 在稀疏补丁序列上推理全局语义与布局，而轻量级体素级 DiT 在选定补丁内恢复细粒度几何细节。这种设计利用了表面稀疏性，即最有信息量的 SDF 变化集中在零水平集附近。补丁级模型处理表面补丁，体素级模型预测补丁内的高频细节。

$$ \mathcal{L}_{\text{diff}} = \mathbb{E}_{t, \mathbf{x}_0, \epsilon} \left[ \| \epsilon - \epsilon_\theta(\mathbf{x}_t, t, \mathbf{c}) \|^2 \right] $$

该公式为标准的扩散去噪损失，其中 $\mathbf{x}_t$ 为加噪后的表面补丁 SDF 值，$\mathbf{c}$ 为 DINOv2 提取的图像条件特征。通过仅在表面补丁上运行扩散，模型将计算焦点从整个立方体体积转移至几何表面，使得 $1536^3$ 分辨率下的训练与采样成为可能。

### 隐式流形正则化与渲染法线监督

直接在原生 SDF 域预测引入了新的优化挑战：微小的 SDF 值扰动可能导致 Marching Cubes 提取出非水密表面。为抑制此类伪影，Direct3D-V3 引入隐式流形正则化（Implicit Manifold Regularization, IMR），惩罚相邻体素间 abrupt 的 SDF 不连续性。

$$ \mathcal{L}_{\text{IMR}} = \sum_{i \in \mathcal{N}} \| \mathbf{X}_i - \mathbf{X}_{\text{neighbor}} \|^2 $$

该损失项强制 SDF 场在零水平集附近保持平滑过渡，显著减少了开放边界。此外，由于模型直接输出 SDF，可通过 Marching Cubes 提取网格并渲染法线，从而施加渲染法线监督。

$$ \mathcal{L}_{\text{normal}} = \| \mathcal{R}(\text{MC}(\hat{\mathbf{X}})) - \mathcal{N}_{\text{pred}} \|^2 $$

其中 $\text{MC}$ 为 Marching Cubes 算法，$\mathcal{R}$ 为渲染操作，$\mathcal{N}_{\text{pred}}$ 为预训练模型预测的输入图像法线。这一机制允许模型在几何域直接优化表面细节，而非依赖 VAE 解码器的隐式流形先验。

## 实验评估

实验在 Objaverse-XL 子集上训练，并在 Google Scanned Objects (GSO) 及真实图像上进行评估。基线覆盖包括 Michelangelo、Hunyuan3D 2.1、TRELLIS2 等主流潜空间方法。在 GSO 重建任务中，Direct3D-V3 在 Chamfer Distance (CD) 和 F1-score 上均取得最优结果，验证了原生 SDF 扩散在几何精度上的优势。

| Method | CD $\downarrow$ | F10.95 $\uparrow$ | F10.99 $\uparrow$ | Vol. IoU $\uparrow$ |
| --- | --- | --- | --- | --- |
| TRELLIS | 0.0153 | 0.9586 | 0.5123 | 0.3315 |
| TRELLIS2 | 0.0147 | 0.9510 | 0.5934 | 0.3884 |
| Ours | 0.0131 | 0.9600 | 0.6043 | 0.3815 |

消融实验表明，双粒度架构与辅助监督信号对最终质量至关重要。仅使用补丁级 DiT 时 Normal-FID 为 92.96，加入体素级 DiT 后降至 75.80，进一步引入 IMR 和法线监督后达到 68.97。IMR 显著减少了边界边缘数量，在 $1024^3$ 分辨率下将平均边界边缘数从 25,353 降至 898。

| Patch DiT | Voxel DiT | IMR | Normal Sup. | Normal-FID $\downarrow$ |
| --- | --- | --- | --- | --- |
| $\checkmark$ | - | - | - | 92.96 |
| $\checkmark$ | $\checkmark$ | - | - | 75.80 |
| $\checkmark$ | $\checkmark$ | $\checkmark$ | - | 73.24 |
| $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | 68.97 |

评估边界方面，GSO 数据集包含相对简单的扫描物体，未能充分反映复杂拓扑结构下的重建质量。此外，尽管提供了项目主页，但未明确开源代码，且训练依赖 16 块 A800 GPU，复现门槛较高。

## 关联研究分析

从问题动机看，Direct3D-V3 与 TRELLIS2 均追求高分辨率生成，但路径截然不同。TRELLIS2 通过 O-Voxel 等结构化潜空间表示优化压缩效率，仍受限于 VAE 解码器的信息损失；Direct3D-V3 则通过双粒度架构直接处理原始 SDF，消除了解码瓶颈。这一差异源于对“计算效率”与“表示保真度”权衡的不同取舍：前者优化潜空间结构，后者优化原生域计算策略。

从方法设计看，Direct3D-V3 与 Hi3DGen 均尝试引入法线监督，但 Hi3DGen 依赖 VAE 解码进行法线渲染，内存开销限制了其分辨率至 $256^3$。Direct3D-V3 利用原生 SDF 输出直接进行 Marching Cubes 提取，突破了分辨率限制。然而，Direct3D-V3 未对比同样尝试无潜空间但分辨率较低的 SDF-Diffusion，也未在复杂场景级生成中与基于视频扩散的方法（如 GEN3C）进行对比，这限制了对其在长程依赖建模能力上的评估。

## 总结

Direct3D-V3 针对高保真三维生成中 VAE 信息瓶颈与目标失配的核心矛盾，提出在原生体素域直接对 SDF 进行扩散生成。通过双粒度 DiT 架构、隐式流形正则化及渲染法线监督，该框架在 $1536^3$ 分辨率下实现了优于主流潜空间方法的几何精度，GSO 上 CD 降至 0.0131。然而，其优势主要在简单扫描物体上得到验证，对于具有复杂拓扑或极端稀疏结构的物体，原生 SDF 扩散的收敛稳定性与细节恢复能力是否依然显著，论文未给出充分证据。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2611.26511)