# ICLR2026最新论文 ｜NeRV-Diffusion: Diffuse Implicit Neural Representations for Video Synthesis ｜隐式神经表示视频扩散

研究机构：美国马里兰大学帕克分校

作者：Yixuan Ren、Hanyu Wang、Hao Chen 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.24353)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24353)

> 视频生成领域长期受困于帧级特征图带来的时序冗余与解码器计算开销，传统潜空间扩散模型需依赖跨帧注意力维持一致性，导致模型规模与推理成本激增。NeRV-Diffusion 切入这一瓶颈，提出将视频整体压缩为隐式神经表示（INR）权重，并在该权重空间执行扩散去噪，从而消除时序注意力依赖并实现实例特定解码。该范式在 UCF-101 上以 22 的 gFVD 超越多数非隐式基线，但其有效性仅在小规模短视频上得到验证，长视频下的权重容量瓶颈尚存疑。

## 研究背景

视频扩散模型通常将视频编码为逐帧特征图，这种表示忽略了帧间天然连贯性，迫使去噪网络引入跨帧注意力以约束时序一致性，进而推高模型参数量与计算足迹。与此同时，标准变分自编码器（VAE）解码器作为共享组件，在推理阶段需处理大量潜变量以渲染像素，造成显著的可视化延迟。隐式神经表示（INR）将数据拟合为单一神经网络的权重，其连续可微特性支持平滑插值，且紧凑结构天然适配资源受限场景，这为替代帧级特征图提供了理论可能。

现有主流路线中，潜空间架构优化聚焦于 VAE 压缩比提升或语义解耦，如 SemanticGen 与 VideoVAE+，但均保留帧级特征图结构，未从根本上消除时序冗余。步数蒸馏与高效注意力机制虽能降低推理延迟，却未触及表示本身的冗余问题。NeRV-Diffusion 的切入点在于：若视频可被整体表示为一组高斯分布的神经权重，则扩散过程无需处理时空结构，DiT 可简化为纯空间注意力，同时 INR 解码器仅针对单视频实例，避免共享解码器的泛化开销。这一假设将“表示重构”置于“算法加速”之前，从根源上规避 $O(N^2)$ 复杂度增长。

## 核心方法

### 方法参照系

本文问题归属于潜空间架构优化范畴，标准流程为“VAE 编码→潜空间扩散→VAE 解码”。关键差异在于：本文编码器输出非帧级特征图，而是无时空结构的 INR 权重 Token；解码器非共享 VAE，而是实例特定 INR。这一替换要求潜空间同时满足高斯分布约束（利于扩散）与高表达力（利于重建），传统 VAE 的 KL 瓶颈与帧级调制机制无法同时达成。

### 隐式视频自编码器

设计动机：FastNeRV 等超网络编码器仅优化重建性能，其权重分布未受正则化，无法直接用于扩散生成。本文在 FastNeRV 基础上引入 Multi-head Affine Mapping 与 Channel-wise Parameterization，使权重 Token 既符合高斯分布又具备足够表达力。具体而言，编码器将视频 Patch 与专用 Query Token 拼接输入 ViT，经 KL 瓶颈后，通过多头仿射层将同一组权重 Token 独立调制至 NeRV 各层。权重 Token 直接作为卷积核（而非与共享基权重相乘），并沿除输出通道外所有维度归一化。该设计使生成权重直接参与解码，最大化自由度，同时支持 INR 间平滑参数插值。

$$
\theta = E(x), \quad \mathcal{L}_{KL} = D_{KL}(q(\theta|x) \| \mathcal{N}(0, I))
$$

其中 $E(x)$ 为超网络编码器，$\theta$ 为 INR 权重 Token，KL 散度约束确保权重分布逼近标准高斯，为后续扩散提供平滑潜空间。

### 隐式扩散去噪

设计动机：NeRV 权重 Token 无时空结构，传统视频 DiT 的时序注意力模块冗余且无效；同时，早期去噪步收敛慢，误差累积严重。本文采用 vanilla DiT 作为骨干，去除时序注意力，并引入 Min-SNR-$\gamma$ 损失加权与 Scheduled Sampling。Min-SNR-$\gamma$ 通过系数 $w_t = \min\{\text{SNR}(t), \gamma\}$ 平衡各时间步损失，防止训练过度聚焦低噪声区域。Scheduled Sampling 在训练时随机用模型预测 $\hat{\theta}_{t-1}$ 替代真实输入执行二次前向，对齐训练与推理分布，缓解曝光偏差。

$$
\mathcal{L}_{denoise} = \sum_{t} w_t \left\| \epsilon - \epsilon_\phi(\theta_t, t) \right\|^2, \quad w_t = \min\left\{ \frac{\alpha_t^2}{\sigma_t^2}, \gamma \right\}
$$

该公式表明：损失加权动态调整各时间步贡献，$\gamma$ 控制最小权重，确保去噪方向在所有噪声水平下均匀下降，加速早期步收敛。

## 实验评估

实验在 UCF-101 与 Kinetics-600 上进行，均为 16 帧 128×128 分辨率，指标为 FVD。基线覆盖 GAN（DIGAN）、自回归（MAGVIT-AR）、扩散（Latte）等路线，但缺失 Sora、Wan 等大规模 DiT 基线，因协议差异（短视频 vs 长视频）无法直接对比。主结果显示，NeRV-Diffusion-L 在 UCF gFVD 达 22，显著优于 MAGVIT-AR（109）与 Latte（162），且模型参数量（55M）远小于非隐式方法（如 LARP 343M）。

| 方法 | #Params | UCF gFVD ↓ | K600 gFVD ↓ |
|---|---|---|---|
| MAGVIT-AR | 362M | 109 | 162 |
| Latte | 79M | 162 | 332 |
| NeRV-Diffusion-L | 55M | 22 | 19 |

消融实验揭示关键设计决策：Multi-head Affine Mapping 将 gFVD 从 562 降至 283，贡献最大；Channel-wise Parameterization 优于低秩交叉乘积，因直接作为卷积核最大化解码透明度；Spatiotemporal PE 尺寸 $h=w=8$ 达最优（254），过小截断空间，过大减少上采样层；Transposed Convolution 以 1/4 参数量超越 PixelShuffle；Residual Connection 优于 Skip Connection，避免多分辨率 RGB 求和伪影。Token 数量 128 达峰值，更多 Token 导致潜空间过复杂，扩散难度增加。

评估边界：仅使用 FVD 单一指标，未报告 FPS、Latency 或 VBench 多维分数；16 帧 128×128 协议无法反映长视频时序一致性；代码未公开，超参数细节仅见附录，可复现性受限。

## 关联研究分析

从问题动机看，NeRV-Diffusion 与 SemanticGen 同属潜空间优化，但前者重构表示本身（INR 权重），后者优化语义空间映射。SemanticGen 保留帧级特征图，依赖 VAE 解码器，而 NeRV-Diffusion 用实例特定 INR 替代共享解码器，根源在于任务特性：INR 的紧凑性适合单视频重建，但跨视频泛化能力未验证。从方法设计看，NeRV-Diffusion 与 Latte 同用 DiT 骨干，但 Latte 依赖时序注意力处理帧级特征，本文证明无时空结构权重亦可生成动态视频，差异源于表示结构：帧级特征需时序建模，INR 权重天然隐含时序关联。

## 总结

NeRV-Diffusion 解决的核心矛盾是帧级特征图的时序冗余与共享解码器的高计算开销。其切入点在于将视频整体表示为高斯分布的 INR 权重，使扩散过程无需时序注意力，解码器实例特定化。方法通过 Multi-head Affine Mapping 与 Channel-wise Parameterization 增强权重表达力，结合 Min-SNR-$\gamma$ 与 Scheduled Sampling 优化去噪训练。实验证明在 UCF-101 上 gFVD 达 22，参数量仅 55M，显著优于非隐式基线。边界在于：16 帧 128×128 协议无法验证长视频性能，INR 权重的记忆容量在分钟级视频下是否成为瓶颈，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24353)