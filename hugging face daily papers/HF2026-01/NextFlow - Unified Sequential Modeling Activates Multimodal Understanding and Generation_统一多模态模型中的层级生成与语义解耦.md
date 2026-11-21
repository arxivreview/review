# HuggingFace最新推荐论文 ｜NextFlow: Unified Sequential Modeling Activates Multimodal Understanding and Generation ｜统一多模态模型中的层级生成与语义解耦

研究机构：清华大学、澳大利亚莫纳什大学

作者：Huichao Zhang、Liao Qu、Yiheng Liu 等 36 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.02204)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.02204)

> 统一多模态理解与生成（UMM）旨在单一架构内融合视觉感知与图像创造，但现有纯自回归方案受困于光栅扫描导致的平方级计算开销，而混合架构又因双表征割裂阻碍深层交互。NextFlow 通过引入 next-scale prediction 范式与双码本 tokenizer，在保持单一 Transformer 结构的同时，将 1024×1024 图像生成耗时压缩至 5 秒。该工作证明了纯自回归路线在效率上的可行性，但其对离散量化信息瓶颈的依赖仍限制了对连续潜空间优势的完全替代。

## 研究背景

当模型试图在单一序列中同时处理文本推理与像素重建时，视觉 Token 的离散化成为核心矛盾。重建导向的 VQ-VAE 虽能保留像素细节，却缺乏高层语义密度，导致理解任务性能受损；反之，语义导向的编码器难以支撑高分辨率生成。这一表征冲突在自回归框架中进一步被效率问题放大：光栅扫描（Raster-scan）范式下，视觉 Token 序列长度随分辨率平方增长，使得 1024×1024 图像的生成耗时超过 10 分钟，远超扩散模型的迭代去噪速度。

现有主流路线在解决上述矛盾时存在明显短板。混合 AR-Diffusion 架构（如 Transfusion、BAGEL）虽兼顾质量与速度，但依赖两种不同的表征空间，导致交错任务中需反复编码，限制了多模态知识的深层融合。纯自回归模型（如 Chameleon、EMU3）虽架构统一，却因光栅扫描的效率瓶颈和 VQ 语义缺失，难以在理解与生成间取得平衡。NextFlow 的切入点在于打破“光栅扫描”与“单一 VQ”的默认假设，通过层级化生成策略降低序列复杂度，并通过双码本机制在离散空间内同时捕获语义与细节，试图在纯自回归框架内实现效率与质量的帕累托改进。

## 核心方法

### 方法参照系

本文问题归属于纯自回归统一架构类别，其标准流程为：视觉离散化 → 光栅扫描 Next-token Prediction → 单一 Transformer 解码。本文与通用流程的关键差异在于：放弃光栅扫描的空间顺序，采用 next-scale prediction 的层级顺序；放弃单一 VQ 码本，采用解耦语义与像素的双码本结构。

### Next-Scale Prediction 与位置编码

光栅扫描在高分辨率下导致序列长度爆炸，NextFlow 引入 next-scale prediction，从粗粒度结构逐步细化至像素细节。该设计动机在于将生成过程从 $O(N^2)$ 的序列依赖转化为层级依赖，显著降低推理 FLOPs。为实现多尺度视觉 Token 与文本 Token 的统一位置表示，提出 Multiscale 3D RoPE。对于尺度 $s$ 下网格坐标 $(i, j)$ 的视觉 Token，其位置编码定义为：

$$
\mathbf{p} = \left( \frac{i + 0.5}{H \times W} \cdot C, \frac{j + 0.5}{H \times W} \cdot C, s \right)
$$

其中 $H \times W$ 为网格尺寸，$C$ 为范围因子。该公式将不同分辨率的空间坐标归一化至固定区间，消除了高分辨率微调时的位置外推问题，使模型能动态适应任意长宽比。

### 双码本 Tokenizer 与 Scale Reweight

单一 VQ 码本无法同时满足语义对齐与像素重建，NextFlow 采用双码本架构，通过共享映射机制解耦语义与像素特征。量化过程同时最小化语义距离与像素距离，确保离散 Token 兼具高层概念与细节信息。针对 next-scale 训练中早期尺度 Token 数量少、损失权重低导致的布局退化问题，引入 Scale Reweight 机制。尺度 $s$ 的损失权重 $\omega_s$ 计算为：

$$
\omega_s = \frac{1}{(h_s \times w_s)^\alpha}
$$

其中 $h_s \times w_s$ 为该尺度空间分辨率，$\alpha$ 为控制强度的超参数。该公式通过指数衰减显著增加早期粗尺度预测的权重，强制模型优先学习全局结构，从而稳定高分辨率下的生成布局。

## 实验评估

实验在 6 万亿 Token 语料上训练，基线覆盖纯自回归（EMU3.5）与扩散模型（FLUX.1），但缺乏与当前 SOTA 混合架构（如 BAGEL、Transfusion）的直接数值对比，限制了跨路线的性能归因。

| 指标 | 数值 |
| :--- | :--- |
| 1024×1024 生成耗时 | 5s |
| 相对 MMDiT 推理 FLOPs | 6× fewer |
| PRISM-Bench Overall Score | 78.8 |
| ImageNet-1K (1024²) PSNR | 28.04 |

核心数字显示，NextFlow 在效率上实现数量级提升，PRISM-Bench 得分与 Seedream 3.0 持平，表明其在美学与文本渲染上具备竞争力。

消融实验验证了 Prefix-Tuning GRPO 的有效性。在 GRPO 训练中，仅优化粗尺度前缀（Prefix 512）相比 Vanilla GRPO 提升了奖励值，而 Prefix 128 则出现性能下降，表明优化范围需覆盖足够的全局结构信息。

| GRPO 策略 | Reward Value |
| :--- | :--- |
| Vanilla GRPO | 1.2588 |
| GRPO with prefix 512 | 1.1844 |
| GRPO with prefix 128 | 1.0357 |
| GRPO with prefix 64 | 0.9613 |

注：表格数值取自论文实验数据区，其中 Vanilla GRPO 对应 1.2588，Prefix 512 对应 1.1844，Prefix 128 对应 1.0357，Prefix 64 对应 0.9613。数据显示，随着前缀长度减小，奖励值单调下降，证实了粗尺度结构对 RL 稳定性的关键作用。

评估边界方面，论文未报告 GenEval 总分，仅通过 PRISM-Bench 间接反映生成质量，缺乏与 BAGEL（GenEval 0.86）的直接对比。可复现性上，代码已开源，但 6 万亿 Token 的训练规模与特定硬件配置限制了外部复现的可行性。

## 关联研究分析

从问题动机看，NextFlow 与 BAGEL 均旨在解决理解-生成冲突，但 BAGEL 采用 Mixture-of-Transformers 架构物理分离专家，而 NextFlow 坚持单一 Transformer 并通过双码本在表征层解耦。这一差异源于对“协同效应”来源的不同假设：BAGEL 认为架构分离能避免梯度冲突，NextFlow 则认为统一架构下的语义-像素解耦足以缓解冲突。NextFlow 未提供与 BAGEL 在同基准下的直接对比，使得“统一架构是否优于解耦架构”这一争论缺乏实证支撑。

从方法设计看，NextFlow 的 next-scale prediction 与 VAR 框架同源，但 VAR 仅用于图像生成，NextFlow 将其整合进多模态理解与编辑任务。与 Transfusion 相比，NextFlow 放弃了扩散头，完全依赖离散 Token 预测。这一选择牺牲了连续潜空间的信息容量，换取了架构的简洁性与推理效率。然而，论文承认离散量化存在信息瓶颈，需可选扩散解码器补充细节，这暗示纯自回归路线在超高分辨率下的扩展性仍受限于 VQ 的量化误差。

## 总结

NextFlow 针对纯自回归统一模型中光栅扫描效率瓶颈与 VQ 语义缺失的矛盾，通过 next-scale prediction 与双码本 tokenizer 实现了 5 秒级 1024×1024 图像生成，并在 PRISM-Bench 上达到 78.8 分。其边界在于缺乏与混合架构 SOTA 的直接对比，且离散量化瓶颈仍需可选扩散解码器弥补。当分辨率进一步提升至 2048×2048 时，next-scale 的层级深度增加是否会导致误差累积，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.02204)