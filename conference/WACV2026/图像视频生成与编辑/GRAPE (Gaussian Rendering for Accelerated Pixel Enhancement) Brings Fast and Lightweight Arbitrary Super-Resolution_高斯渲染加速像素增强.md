# WACV2026最新论文 ｜GRAPE (Gaussian Rendering for Accelerated Pixel Enhancement) Brings Fast and Lightweight Arbitrary Super-Resolution ｜高斯渲染加速像素增强

研究机构：韩国高丽大学

作者：Jung In Jang、Kyong Hwan Jin

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_99b3390a3ef1)

> 任意尺度超分辨率（ASSR）的核心矛盾在于连续表示的灵活性与其推理延迟随输出分辨率线性增长之间的冲突。隐式神经表示（INR）因逐坐标查询而低效，查找表（LUT）受限于离散尺度，既有高斯泼溅（GS）方法则依赖重型解码器导致内存与速度瓶颈。GRAPE 通过单层点卷积直接回归各向异性 2D 高斯参数，以单次光栅化替代复杂解码网络，在保持重建质量竞争力的同时实现数量级速度提升。其价值在于验证了轻量 GS 解码在高效 SR 中的可行性，但缺乏感知质量指标与固定尺度 SOTA 的直接对比，限制了其在“质量-效率”帕累托前沿上的精确定位。

## 研究背景

当用户在手机或桌面编辑器中自由缩放图像时，系统需即时响应任意倍率的重建请求。固定尺度模型（如 EDSR）为每个倍率训练独立网络，导致内存与维护成本随尺度数量线性增加；LUT 方法虽推理极快，但仅支持预设离散尺度，未见尺度需离线重算或低效插值。INR 通过 MLP 预测任意坐标 RGB 值解决了尺度连续性问题，但每个目标像素需独立查询网络，计算量与输出分辨率成正比，高分辨率下延迟不可接受。

ASSR 领域的主流路线在 INR 与 GS 间分化。INR 路线（如 LIIF）受限于逐点查询的并行性缺失，无法像卷积那样批量处理区域；GS 路线（如 GSASR、ContinuousSR）通过稀疏高斯集合单次光栅化消除逐坐标计算，但依赖重型解码器将深度特征映射至高斯参数，导致内存占用大、训练不稳定。GRAPE 的切入点在于识别出 GS 方法中解码器是性能瓶颈而非高斯表示本身，通过移除复杂解码网络、直接回归最小参数集，将计算重心从“特征到参数的复杂映射”转移至“参数到图像的轻量光栅化”。

## 核心方法

### 2D 高斯表示与光栅化参照系

GSASR 等既有方法将 LR 特征经多层解码器映射为高斯参数，再光栅化生成 HR 图像。本文问题与该通用流程的关键差异在于：解码器参数量大、计算图复杂，且高斯密度增加以提升质量会进一步加剧内存与延迟负担。GRAPE 采用 2D 各向异性高斯 $G(\mu, \Sigma, \tilde{c})$，其中均值 $\mu \in \mathbb{R}^2$、协方差 $\Sigma \in \mathbb{R}^{2\times2}$、颜色 $\tilde{c} \in \mathbb{R}^3$。为保持 $\Sigma$ 半正定，采用旋转-缩放分解 $\Sigma = (RS)(RS)^\top$，其中 $R(\theta)$ 为旋转矩阵，$S = \text{diag}(s_1, s_2)$ 为缩放矩阵。光栅化时，像素颜色 $C_i$ 为所有重叠高斯的加权和：

$$ C_i = \sum_{n \in \mathcal{N}} \tilde{c}_n w_n, \quad w_n = \exp\left(-\frac{1}{2} d_n^T \Sigma_n^{-1} d_n\right) $$

该公式表明，像素值由距离加权的高斯核决定，权重随距离平滑衰减，无需深度排序或透明度混合，简化了 3D GS 的 $\alpha$-blending 过程。

### 轻量高斯头与集成机制

设计动机在于解决既有 GS 方法中解码器参数量大、计算冗余的问题。GRAPE 将解码阶段压缩为单层 $1 \times 1$ 卷积，独立作用于每个网格点，避免空间耦合计算。输入特征图经 $\times 4$ 上采样与 $\times 2$ PixelUnshuffle 后形成 $N = 4hw$ 个高斯原语网格。高斯头输出 $E \in \mathbb{R}^{B \times 9K \times H/2 \times W/2}$，每组 9 通道编码 8 个高斯参数（3 RGB、1 旋转、2 缩放、2 偏移）与 1 个混合 logit。为增强局部统计编码能力，引入高斯集成（Ensemble）机制：每个网格点预测 $K$ 个高斯，通过 softmax 归一化混合权重 $w_{i,k}$，最终参数为加权平均：

$$ g_i = \sum_{k=1}^{K} w_{i,k} g_{i,k}, \quad w_{i,k} = \frac{\exp(\tilde{a}_{i,k})}{\sum_{\ell=1}^{K} \exp(\tilde{a}_{i,\ell})} $$

该机制在光栅化前解析混合，确保每个网格点仅输出一个高斯，保持计算复杂度不变。参数激活采用非线性约束：$\theta_i = 2\pi \sigma(\tilde{\theta}_i)$，$s_i = 0.5 \sigma(\tilde{s}_i)$，$\delta_i = \tanh(\tilde{\delta}_i)$，其中 $\sigma(\cdot)$ 为 sigmoid 函数。RGB 值 $\tilde{c}_i$ 不加约束，因正权重内核天然保证像素强度有界。此设计使解码器参数量降至 1.56 M，峰值 GPU 内存仅 1.10 GB，光栅化步骤复杂度线性于高斯数量 $N$ 与平均命中瓦片数 $k_{\text{tile}}$ 的乘积。

## 实验评估

实验在 Set5、Set14、BSD100、DIV2K 和 Urban100 上进行，使用 EDSR 作为统一编码器骨干，训练采用 L1 损失与 Adam 优化器，1000 轮迭代，batch size 16，单卡 RTX 3090。基线覆盖 LUT（SR-LUT、MuLUT、LeRF）、INR（LIIF）和 GS（GaussianSR、GSASR）三条路线，缺失固定尺度 SOTA（如 SwinIR、HAT）的直接对比，因任务定义不同（ASSR vs. 固定尺度）。主实验显示，Urban100 ×4 下 GRAPE 达 69.33 FPS / 25.87 dB，GSASR 为 0.22 FPS / 27.00 dB，LIIF 为 3.06 FPS / 26.15 dB，GaussianSR 为 6.19 FPS / 26.19 dB。GRAPE 速度较 GSASR 提升 315 倍，较 LIIF 提升 22.6 倍，PSNR 较 GSASR 低 1.13 dB，较 LIIF 低 0.28 dB。

| 方法 | Urban100 ×4 FPS | Urban100 ×4 PSNR (dB) | 参数量 (M) | 内存 (GB) |
|---|---|---|---|---|
| LIIF | 3.06 | 26.15 | 1.58 | 8.26 |
| GaussianSR | 6.19 | 26.19 | 1.84 | 16.15 |
| GSASR | 0.22 | 27.00 | 20.45 | 7.89 |
| GRAPE | 69.33 | 25.87 | 1.56 | 1.10 |

消融实验聚焦训练 patch 大小、集成大小 $K$ 与核类型。Patch 从 48² 增至 256² 提升有效感受野，PSNR 从 25.79 dB 升至 25.86 dB；$K$ 从 1 增至 4，PSNR 从 25.79 dB 升至 25.86 dB；各向异性核替换为各向同性核，PSNR 从 25.84 dB 降至 25.70 dB，表明方向建模对边缘重建至关重要。效率分析显示，×4 上采样 1920×1080 图像耗时 40.88 ms，编码器占 85.1%（35.71 ms），高斯头与光栅化分别耗时 2.34 ms 与 2.49 ms，峰值内存 2.12 GB。

评估边界存在显著局限：仅报告 PSNR 与 FPS，未提供 SSIM、LPIPS 等感知质量指标，无法验证“感知质量有竞争力”的主张；Urban100 ×4 下 PSNR 25.87 dB 低于固定尺度 SOTA（如 SwinIR-light 32.76 dB），但任务定义不同，直接比较无效；代码开源（github.com/mulkkog/GRAPE），超参数完整，可复现性良好。

## 关联研究分析

从问题动机看，GRAPE 与 LIIF 同属 ASSR 路线，但 LIIF 依赖 INR 逐坐标查询，计算量随输出分辨率线性增长，而 GRAPE 采用显式 GS 光栅化，复杂度线性于高斯数量 $N$ 而非像素总数 $HW$。这一差异源于任务特性：INR 需为每个像素独立求解 MLP 输出，无法批量处理；GS 通过稀疏高斯集合单次渲染，天然支持 GPU 并行。GRAPE 的轻量高斯头进一步将解码开销降至最低，但 1.13 dB 的 PSNR 差距暗示，移除重型解码器可能损失了高频细节的精细建模能力，这在 Urban100 等纹理丰富数据集上尤为明显。

从方法设计看，GRAPE 与 GSASR 同属 GS 路线，但 GSASR 采用前馈高斯生成器，参数量 20.45 M，解码器复杂度高；GRAPE 用单层 $1 \times 1$ 卷积替代，参数量 1.56 M，解码器开销占比仅 33%。这一差异源于设计哲学：GSASR 追求重建质量上限，通过增加高斯密度与解码器容量提升 PSNR；GRAPE 追求效率下限，通过最小化参数集与计算图简化实现速度突破。GRAPE 的高斯集成机制（$K$ 个高斯加权平均）是 GSASR 未采用的创新，旨在增强局部统计编码能力，但消融显示 $K$ 从 1 到 4 仅提升 0.07 dB，边际收益有限，暗示当前架构下集成机制的潜力未充分释放。

## 总结

GRAPE 要解决的核心矛盾是 ASSR 中连续表示的推理延迟与输出分辨率的正相关关系。既有 INR 方法因逐坐标查询而低效，GS 方法因重型解码器而内存与速度受限，GRAPE 通过单层点卷积直接回归各向异性 2D 高斯参数，以单次光栅化替代复杂解码网络，在 Urban100 ×4 下实现 69.33 FPS / 25.87 dB，速度较 GSASR 提升 315 倍，内存降至 1.10 GB。其边界在于：仅报告 PSNR 与 FPS，缺乏感知质量指标验证；PSNR 低于固定尺度 SOTA，但任务定义不同；高斯集成机制边际收益有限。当输出分辨率从 1080p 提升至 4K 时，光栅化步骤的线性复杂度是否仍能保证实时性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_99b3390a3ef1)