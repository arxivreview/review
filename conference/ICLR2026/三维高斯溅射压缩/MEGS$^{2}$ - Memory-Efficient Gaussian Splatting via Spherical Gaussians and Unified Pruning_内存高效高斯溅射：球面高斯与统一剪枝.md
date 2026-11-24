# ICLR2026最新论文 ｜MEGS$^{2}$: Memory-Efficient Gaussian Splatting via Spherical Gaussians and Unified Pruning ｜内存高效高斯溅射：球面高斯与统一剪枝

研究机构：新加坡南洋理工大学

作者：Jiarui Chen、Yikeng Chen、Yingshuang Zou 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.07021)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.07021)

> 3D高斯溅射（3DGS）在边缘设备部署时面临渲染显存（VRAM）瓶颈，现有存储压缩方法虽能减小文件体积，却因需全量解码导致运行时内存反而膨胀。MEGS² 指出渲染内存由原语总数与单原语参数量共同决定，通过完全替换球谐系数（SH）为可剪枝的球面高斯（SG），并将原语剪枝与Lobe剪枝统一为单一内存约束优化问题，同时压缩两个维度。该方法在保持渲染质量的同时实现了显著的VRAM压缩，但其对复杂高光场景的拟合能力及动态VRAM优化仍存疑。

## 研究背景

3DGS通过数百万个各向异性高斯原语实现实时新视角合成，每个原语包含位置、协方差、不透明度及视角相关颜色模型。原始3DGS采用球谐函数（Spherical Harmonics, SH）建模视角相关颜色，但SH是全局基函数，需高阶系数才能表达局部高频细节（如锐利高光），导致参数利用率低且难以压缩。渲染时，显存消耗分为静态部分（加载的原语参数总和）和动态部分（投影后的2D参数及Tile-Depth表），两者均与原语数量及单原语参数量强相关。

3DGS压缩研究长期聚焦于存储压缩，即通过剪枝、量化或神经编码减小文件体积以加速一次性数据传输。然而，基于哈希网格或向量量化的方法（如CompactGaussian、EAGLES）在渲染前必须解码全量参数，其运行时VRAM甚至超过未压缩的3DGS。另一类基于原语剪枝的方法（如GaussianSpa、Mini-Splatting）虽能降低VRAM，但为维持质量需保留大量原语，压缩比受限。MEGS² 的切入点在于：现有方法仅优化原语数量或仅优化存储格式，未同时压缩“原语数量”与“单原语参数量”这两个决定VRAM的核心因子。

## 核心方法

### 方法参照系

MEGS² 属于后训练压缩路线，但摒弃了量化与熵编码环节。与GaussianSpa等仅将原语剪枝建模为约束优化的方法不同，MEGS² 将颜色表示替换为球面高斯，并将原语剪枝与Lobe剪枝统一为单一内存预算约束问题，直接操作显式参数以最小化运行时VRAM。

### 球面高斯颜色表示

传统SH基函数全局且参数固定，难以高效表达局部高光。MEGS² 引入任意方向、可剪枝的球面高斯（Spherical Gaussian, SG）完全替代SH。SG由多个Lobe组成，每个Lobe由轴方向 $\mu \in S^2$、锐度 $s \in \mathbb{R}^+$ 和RGB振幅 $\mathbf{a} \in \mathbb{R}^3$ 定义。视角相关颜色计算为：

$$
c(\mathbf{v}) = c_0 + \sum_{i=1}^{n} \mathbf{a}_i \exp\left(-s_i (1 - \mathbf{v} \cdot \mu_i)\right)
$$

其中 $c_0$ 为漫反射颜色。SG的局部性使其仅需少量Lobe即可拟合高频细节，且Lobe数量直接控制参数量，为剪枝提供了天然接口。相比SG-Splatting的固定正交轴混合模型，任意方向SG具有更高自由度，避免了固定轴在复杂视角依赖效应下的质量下降。

### 统一软剪枝框架

原语剪枝与Lobe剪枝通常串行执行，易陷入次优解。MEGS² 将两者统一为内存约束优化问题，以总参数预算 $\kappa$ 为约束：

$$
\min_{\mathbf{o}, \mathbf{s}, \Theta} L(\mathbf{o}, \mathbf{s}, \Theta) \quad \text{s.t.} \quad \rho_o \|\mathbf{o}\|_0 + \rho_s \|\mathbf{s}\|_0 \leq \kappa
$$

其中 $\mathbf{o}$ 为不透明度向量，$\mathbf{s}$ 为锐度向量，$\rho_o=11$、$\rho_s=7$ 分别为单原语和单Lobe的基础参数量。由于 $L_0$ 范数不可微，采用ADMM-inspired算法求解：引入代理变量 $\tilde{\mathbf{o}}, \tilde{\mathbf{s}}$，通过近端算子将参数投影至约束空间。锐度投影基于动态范围指标 $D_i = \|\mathbf{a}_i\|_2$ 保留最重要的Lobe。优化后，移除零不透明度原语与零锐度Lobe，并通过颜色补偿项 $\Delta c_0$ 恢复被移除Lobe的能量，最后微调恢复质量。

## 实验评估

实验在Mip-NeRF 360、Tanks & Temples、Deep Blending三个真实场景数据集上进行，评估PSNR、SSIM、LPIPS及静态/渲染VRAM。基线覆盖剪枝类（GaussianSpa、Mini-Splatting）、SH压缩类（Reduced3DGS）及存储压缩类（LightGaussian、CompactGaussian等），但缺失前馈压缩类方法（如CodecSplat）及动态场景基线。

| 方法 | Mip-NeRF 360 PSNR | Mip-NeRF 360 VRAM (Stat./Rend.) | Deep Blending PSNR | Deep Blending VRAM (Stat./Rend.) |
|---|---|---|---|---|
| 3DGS | 27.48 | 648 / 1717 | 29.71 | 582 / 1569 |
| GaussianSpa | 27.56 | 115 / 448 | 30.00 | 104 / 372 |
| MEGS² (HQ) | 27.54 | 55 / 265 | 30.17 | 54 / 243 |
| MEGS² (LM) | 27.21 | 40 / 224 | 30.01 | 33 / 193 |

MEGS² HQ版在Deep Blending上PSNR达30.17 dB，较3DGS提升0.4 dB，静态VRAM仅54 MB，为3DGS的9.3%；渲染VRAM 243 MB，为3DGS的15.5%。相比SOTA剪枝方法GaussianSpa，MEGS² HQ静态VRAM降低52%，渲染VRAM降低37%，质量持平或略优。

消融实验验证了SG替代SH及统一剪枝的有效性。固定轴SG导致PSNR下降约0.6 dB，证实任意方向SG的必要性。统一剪枝（unified→seq.）较串行剪枝（soft→hard）PSNR提升0.10 dB，VRAM降低40 MB，表明联合优化避免了次优解。移除颜色补偿（w/o color comp.）导致PSNR下降0.08 dB，说明补偿策略对质量恢复至关重要。

评估仅覆盖静态场景，未报告动态VRAM或移动端实测帧率（尽管摘要提及WebGL演示）。PSNR指标无法捕捉压缩导致的闪烁或几何不稳定，缺乏LPIPS与主观评估的联合分析。代码声明将在发表后发布，当前未提供超参数细节及VRAM测量协议的具体实现，可复现性依赖附录补充。

## 关联研究分析

从问题动机看，MEGS² 与GaussianSpa同属剪枝路线，但GaussianSpa仅将原语剪枝建模为约束优化，未触及单原语参数量。MEGS² 引入SG后，Lobe剪枝成为可能，从而将优化维度从“原语数量”扩展至“总参数预算”。这一差异源于SG的局部性与可剪枝性，而SH的全局性使其难以类似压缩。GaussianSpa在Mip-NeRF 360上PSNR 27.56 dB，MEGS² HQ为27.54 dB，质量几乎持平，但VRAM显著更低，表明SG+统一剪枝在内存效率上具有结构性优势。

从方法设计看，MEGS² 与SG-Splatting均使用SG，但SG-Splatting采用固定正交轴与SH混合模型，MEGS² 则完全摒弃SH并支持任意方向。SG-Splatting的固定轴在复杂视角依赖效应下质量下降约0.6 dB，且与Lobe剪枝不兼容。MEGS² 的任意方向SG提供了更高自由度，使其能更灵活地拟合局部高光，同时Lobe数量直接控制参数量，为统一剪枝提供了基础。这一设计选择解决了SG-Splatting在高频细节表达与压缩兼容性上的双重局限。

## 总结

MEGS² 针对3DGS在边缘设备上的渲染VRAM瓶颈，指出存储压缩不等于内存效率，现有方法仅优化原语数量或存储格式，未同时压缩原语数量与单原语参数量。通过完全替换SH为任意方向可剪枝SG，并将原语剪枝与Lobe剪枝统一为内存约束优化问题，MEGS² 在Deep Blending上实现30.17 dB PSNR与54 MB静态VRAM，较3DGS压缩9.3%。其边界在于仅优化静态VRAM，未处理动态VRAM，且对复杂高光场景的拟合能力未充分验证。当场景包含大量非局部、高频高光时，SG的局部性假设是否仍成立，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.07021)