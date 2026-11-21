# HuggingFace最新推荐论文 ｜InstantFusion: A Shared Latent Interface for Heterogeneous Image Generators ｜异构生成模型的共享潜空间接口

研究机构：复旦大学、上海交通大学

作者：Xuanlang Dai、Jiazi Bu、Yujie Zhou 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.13944)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.13944)

> 导读 扩散模型与流匹配模型已成为图像生成的主流范式，但不同模型在潜空间表示、网络架构及训练配方上存在显著异构性，导致模型间无法直接共享中间状态或去噪动态。现有跨模型对齐方法多聚焦于静态潜状态的线性映射，忽略了去噪轨迹的动态兼容性，且通常依赖成对映射，难以扩展至多模型场景。本文提出 InstantFusion，通过轻量级潜自编码器（LAE）将异构生成器的中间状态映射至共享潜空间，并同步局部去噪速度，实现无需成对映射的跨模型状态迁移与动态同步。该接口在生成加速、多偏好组合及跨架构蒸馏中展现出有效性，但其依赖共享 VAE 及多模型同时加载的局限性，限制了其在资源受限场景下的通用性。

## 研究背景

当现代图像生成模型在潜空间中进行去噪时，不同模型（如 SD3、FLUX.1、Qwen-Image）虽最终映射至相似的自然图像分布，但其内部潜空间表示、时间参数化及去噪向量场存在根本差异。这种异构性导致模型间无法直接交换中间去噪状态，即便在相同噪声水平下，一个模型的中间状态输入另一个模型也会产生严重伪影。为解决此问题，跨模型潜空间对齐（Cross-Model Latent Alignment）方法尝试建立不同模型潜状态间的对应关系，但现有方法多局限于静态状态对齐，未考虑去噪动态的兼容性，且通常需为每对模型训练专用映射，缺乏通用性。

领域内另一条路线是轨迹拼接（Trajectory Stitching），允许不同去噪器在采样不同阶段接管，但通常假设所有模型共享同一潜空间。这暴露了当前研究的盲区：如何在异构潜空间之间实现无缝的轨迹迁移？本文观察到，尽管原生潜空间不兼容，但不同模型的中间状态在空间组织上具有相似性，且直接交接虽引入伪影但仍保留粗粒度语义。这一发现表明，异构生成器编码了部分共享的视觉结构，其去噪过程并非完全脱节。InstantFusion 正是基于此观察，旨在构建一个轻量级共享接口，连接异构生成器的去噪轨迹。

## 核心方法

### 方法参照系：异构潜空间对齐与动态同步

InstantFusion 属于架构创新与混合范式中的跨模型接口设计。其参照系为传统的跨模型潜空间对齐，但关键差异在于：传统方法仅对齐静态潜状态，且需成对映射；InstantFusion 则构建一个共享潜空间，通过模型专属的轻量级潜自编码器（LAE）实现多模型间的通用接口，并显式对齐去噪动态。

### 潜空间对齐与重建（Latent Alignment and Reconstruction）

为实现跨模型状态迁移，InstantFusion 为每个冻结生成器 $m$ 配备一个时间条件 LAE，包含编码器 $E_m$ 和解码器 $D_m$。编码器将模型原生潜状态 $x_t$ 映射至共享表示 $z_t^m$，解码器则将其重构回原生空间。设计动机在于，仅对齐状态会导致信息丢失，因此需同时优化对齐损失与重建损失。对齐损失 $\mathcal{L}_{align}$ 强制不同模型在相同噪声水平下的共享表示一致：

$$ \mathcal{L}_{align} = \frac{2}{M(M-1)} \sum_{1 \le A < B \le M} \| z_t^A - z_t^B \|_2^2 $$

该公式确保来自同一图像、相同噪声水平的中间状态在共享空间中聚类。同时，重建损失 $\mathcal{L}_{rec}$ 保证共享表示保留足够的原生信息以支持后续去噪：

$$ \mathcal{L}_{rec} = \frac{1}{M} \sum_{m=1}^M \| \tilde{x}_t^m - x_t \|_2^2 $$

其中 $\tilde{x}_t^m$ 为重构潜状态。这一设计解决了传统对齐方法中“对齐即遗忘”的失效模式，确保共享空间既具跨模型一致性，又保留模型特异性信息。

### 去噪动态对齐（Denoising Dynamics Alignment）

静态状态对齐不足以保证轨迹连续性，因为不同模型的去噪速度（向量场）可能差异巨大。InstantFusion 引入动态对齐损失 $\mathcal{L}_{dyn}$，同步共享空间中的局部去噪位移。对于采样步 $k$，模型 $m$ 的位移在共享空间中定义为 $\Delta z_k^m = E_m(x_{t_{k+1}}^m, t_{k+1}) - z_{t_k}^m$。动态对齐损失强制不同模型的位移一致：

$$ \mathcal{L}_{dyn} = \frac{2}{M(M-1)} \sum_{1 \le A < B \le M} \text{MSE}(\Delta z_k^A, \Delta z_k^B) $$

该公式确保模型切换时，接收方模型能沿发送方模型的轨迹方向继续去噪，避免轨迹断裂。总损失函数为 $\mathcal{L} = \mathcal{L}_{rec} + \mathcal{L}_{align} + \lambda_{reg}\mathcal{L}_{reg} + \lambda_{dyn}\mathcal{L}_{dyn}$，其中 $\mathcal{L}_{reg}$ 为范数一致性正则项。这一创新解决了仅对齐状态导致的去噪速度不匹配问题，使跨模型交接后的生成过程平滑稳定。

## 实验评估

实验在 SD3、Z-Image、FLUX.1 和 Qwen-Image 四个文生图模型上进行，使用 VisPrompt 数据集训练 LAE，评估指标包括 GenEval-v2、HPSv2、CVTG-2K 等。基线覆盖包括单模型生成、T-Stitch 加速方法及跨模型对齐方法。

| 方法 | 延迟 (s) | GenEval-v2 | HPSv2 | OneIG-Bench Avg. |
| :--- | :--- | :--- | :--- | :--- |
| Qwen-Image (Baseline) | 18.84 | 41.73 | 25.46 | 0.4849 |
| Qwen-Few-Step | 0.893 | 32.94 | 27.48 | 0.5148 |
| T-Stitch | 20.76 | 7.762 | 21.24 | 0.2659 |
| InstantFusion (Qwen+Z-Image) | 4.373 | 33.34 | - | 0.5386 |
| InstantFusion (Qwen+FLUX.2) | 2.545 | 27.19 | - | 0.5467 |

InstantFusion 在加速任务中显著优于 T-Stitch，Qwen-Image 与 Z-Image-Turbo 组合将延迟从 18.84s 降至 4.373s，同时保持较高的 GenEval-v2 分数。在跨模型组合任务中，Qwen-Image 指导 SD3 使 GenEval-v2 提升 12.92，验证了共享接口的能力迁移效果。

消融实验表明，$\mathcal{L}_{align}$、$\mathcal{L}_{rec}$ 和 $\mathcal{L}_{dyn}$ 三者缺一不可。移除 $\mathcal{L}_{dyn}$ 导致跨架构蒸馏训练发散，移除 $\mathcal{L}_{rec}$ 则严重损害重建质量。LAE 架构中时间条件残差块的设计至关重要，替换为标准卷积层导致 GenEval-v2 下降 7.20-19.17。评估边界方面，实验未报告置信区间，且未对比跨 VAE 架构的接口扩展性，可复现性依赖于特定 VAE 共享假设。

## 关联研究分析

从问题动机看，InstantFusion 与 T-Stitch 均旨在通过模型切换加速生成，但 T-Stitch 假设同潜空间，无法处理异构模型；InstantFusion 通过共享接口突破此限制。然而，T-Stitch 在单模型加速上可能更高效，InstantFusion 的加速收益部分源于组合了高效模型（如 Z-Image-Turbo），而非接口本身带来的纯加速。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

从方法设计看，InstantFusion 与 Cross-Model Latent Alignment 均涉及潜空间对齐，但后者仅关注静态状态，且需成对映射。InstantFusion 引入动态对齐与共享空间，实现了多模型通用接口。然而，动态对齐是否足以消除异构模型间的分布偏移，还是仅掩盖了局部伪影，论文未深入分析。此外，InstantFusion 依赖共享 VAE，这与领域内潜空间独立性的传统认知相悖，其通用性受限于 VAE 架构兼容性。

## 总结

InstantFusion 针对异构生成模型间潜空间不兼容与去噪动态脱节的核心矛盾，提出了一种轻量级共享潜空间接口。通过模型专属 LAE 对齐中间状态与去噪速度，实现了无需成对映射的跨模型状态迁移。实验表明，该接口在生成加速（延迟降低至 4.373s）与能力组合（GenEval-v2 提升 12.92）上有效。然而，其依赖共享 VAE 及多模型同时加载的局限性，限制了其在资源受限场景下的应用。当 VAE 架构异构时，该共享接口的有效性是否依然成立，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.13944)