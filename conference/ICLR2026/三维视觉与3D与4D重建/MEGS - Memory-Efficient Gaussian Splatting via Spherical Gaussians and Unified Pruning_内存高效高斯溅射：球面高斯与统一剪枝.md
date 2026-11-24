# ICLR2026最新论文 ｜MEGS: Memory-Efficient Gaussian Splatting via Spherical Gaussians and Unified Pruning ｜内存高效高斯溅射：球面高斯与统一剪枝

研究机构：新加坡南洋理工大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_69750258)

> 3D高斯溅射（3D Gaussian Splatting, 3DGS）在边缘设备部署时面临渲染显存（VRAM）瓶颈，现有压缩方法多聚焦存储体积缩减，却忽视了解码后全量参数加载导致的显存溢出问题。MEGS²通过完全替换球谐系数（Spherical Harmonics, SH）为可剪枝球面高斯（Spherical Gaussian, SG），并将原语数量与SG瓣数剪枝统一为内存约束优化问题，实现了显存与渲染质量的联合最优。该方法在静态显存上实现8倍压缩，但牺牲了部分存储压缩比，其纯SG表示在复杂高光场景下的鲁棒性仍存疑。

## 研究背景

3DGS渲染显存消耗由两部分构成：静态显存（原语参数总量）与动态显存（投影中间数据）。静态显存直接取决于原语数量与单原语参数量的乘积，而动态显存随特定视角下的活跃原语数线性增长。球谐系数（SH）作为3DGS标准颜色表示，其全局基函数特性导致参数利用率低，高次项系数冗余严重，成为静态显存的主要占用者。

3DGS压缩领域长期聚焦存储比特率最小化，主流路线包括基于哈希网格的神经编码与基于不透明度的原语剪枝。前者如HAC、Scaffold-GS通过结构化表示提升压缩效率，但渲染前需解码全量参数，显存占用甚至超过未压缩3DGS；后者如GaussianSpa、Mini-Splatting通过移除冗余原语降低显存，但受限于保留原语数量下限，压缩比有限。MEGS²的切入点在于识别出“单原语参数冗余”这一被忽视的维度，通过替换颜色表示与统一剪枝策略，同时压缩原语数量与单原语参数量，突破传统仅优化原语数量的局限。

## 核心方法

### 方法参照系

3DGS压缩通用流程为：训练后模型→重要性评估→原语剪枝→属性量化→熵编码。MEGS²的关键差异在于将优化目标从存储比特率转向渲染显存，且将颜色表示替换与剪枝策略耦合为单一约束优化问题，而非分阶段独立处理。

### 球面高斯颜色表示替换

SH函数因全局性需高次系数建模局部高光，导致参数冗余。MEGS²采用任意朝向、可剪枝的SG瓣替代SH，每个SG瓣由轴方向 $\mu \in S^2$、锐度 $s \in \mathbb{R}^+$ 与RGB振幅 $\mathbf{a} \in \mathbb{R}^3$ 定义，颜色计算为：

$$
\mathbf{c}(\mathbf{v}) = \mathbf{c}_0 + \sum_{i=1}^{n} \mathbf{a}_i \exp\left(-\frac{1}{s_i} \ln \frac{1}{\mathbf{v} \cdot \mu_i}\right)
$$

该公式中，$\mathbf{c}_0$ 为漫反射项，$n$ 为SG瓣数。SG瓣的局部性使其仅需少量参数即可建模高光，且瓣数可动态调整，为剪枝提供天然接口。相比SG-Splatting的固定正交轴混合模型，任意朝向SG自由度更高，避免了固定轴导致的细节丢失（PSNR下降约0.6 dB）。

### 统一软剪枝框架

传统剪枝分阶段处理原语数量与属性，易陷入次优解。MEGS²将两者统一为内存约束优化问题，目标函数为：

$$
\min_{\mathbf{o}, \mathbf{s}, \Theta} L(\mathbf{o}, \mathbf{s}, \Theta) \quad \text{s.t.} \quad \rho_o \|\mathbf{o}\|_0 + \rho_s \|\mathbf{s}\|_0 \leq \kappa
$$

其中 $\mathbf{o} \in \mathbb{R}^{N \times 1}$ 为不透明度向量，$\mathbf{s} \in \mathbb{R}^{N \times 3}$ 为锐度向量，$\rho_o=11$、$\rho_s=7$ 为单原语与单SG瓣基础参数量，$\kappa$ 为总参数预算。$L_0$ 范数不可微，采用ADMM算法引入代理变量 $\tilde{\mathbf{o}}$、$\tilde{\mathbf{s}}$ 分解为梯度步与近端步。近端算子通过动态范围指标 $D_i = \|\mathbf{a}_i\|_2$ 保留最重要的 $\kappa_s$ 个SG瓣，实现全局最优内存分配。

## 实验评估

实验在Mip-NeRF 360、Tanks & Temples、Deep Blending三个数据集上评估，基线覆盖剪枝类（GaussianSpa、Mini-Splatting）与压缩类（LightGaussian、CompactGaussian）。MEGS²在Mip-NeRF 360上PSNR达27.54 dB，静态显存仅55 MB，较3DGS（648 MB）压缩11.8倍，较GaussianSpa（115 MB）压缩2.1倍；Deep Blending上PSNR 30.17 dB，静态显存54 MB，较3DGS（582 MB）压缩10.8倍。

| 方法 | Mip-NeRF 360 PSNR (dB) | Mip-NeRF 360 静态显存 (MB) | Deep Blending PSNR (dB) | Deep Blending 静态显存 (MB) |
|---|---|---|---|---|
| 3DGS | 27.48 | 648 | 29.71 | 582 |
| GaussianSpa | 27.56 | 115 | 30.00 | 104 |
| MEGS² (HQ) | 27.54 | 55 | 30.17 | 54 |

消融实验显示，SG替换SH贡献PSNR提升0.53 dB（27.01→27.54），统一剪枝较顺序剪枝提升PSNR 0.21 dB（27.33→27.54）并降低显存43 MB（328→285）。移除颜色补偿项导致PSNR下降0.08 dB，表明补偿策略对质量恢复至关重要。

评估指标包含PSNR、SSIM、LPIPS与显存，但未报告存储压缩比与解码延迟。代码承诺发表后开源，VRAM测量协议详见附录。评估边界在于未对比神经编码方法在显存维度的直接数据，且未验证纯SG表示在存储压缩比上是否劣于SH量化。

## 关联研究分析

从问题动机看，MEGS²与GaussianSpa同属剪枝路线，但GaussianSpa仅优化原语数量，MEGS²扩展至单原语参数量。这一差异源于对显存瓶颈的重新定义：GaussianSpa假设原语数量是显存主因，MEGS²指出SH参数冗余同等重要。根源在于任务特性——边缘设备显存受限，单原语参数优化比原语数量优化更具边际收益。

从方法设计看，MEGS²与SG-Splatting同用SG表示，但SG-Splatting采用固定正交轴混合SH+SG模型，MEGS²采用任意朝向纯SG模型。固定轴导致SG-Splatting在复杂视角依赖效果上PSNR下降0.6 dB，且无法与瓣剪枝兼容。MEGS²的任意朝向设计提升了表示自由度，但增加了优化难度，需依赖ADMM算法求解非凸约束。纯SG表示在存储压缩比上是否劣于SH量化，论文未给出回答。

## 总结

MEGS²解决的核心矛盾是3DGS渲染显存瓶颈与压缩方法聚焦存储比特的错位。其切入点在于识别单原语参数冗余，通过SG替换SH与统一剪枝实现显存与质量联合优化。实验证明静态显存压缩8倍、渲染显存压缩6倍，PSNR持平或提升。边界在于未优化动态显存与存储压缩比，且纯SG表示在复杂高光场景下鲁棒性未充分验证。当场景包含大量高频高光时，SG瓣数需求是否激增导致显存优势消失，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_69750258)