# HuggingFace最新推荐论文 ｜PixRestore: Unified Image Restoration via Pixel Diffusion Transformer ｜像素空间扩散统一图像恢复

研究机构：香港理工大学

作者：Lingchen Sun、Rongyuan Wu、Xiangtao Kong 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2608.16793)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.16793)

> 统一图像恢复（UIR）旨在用单一模型处理多种图像退化，但现有生成式方法依赖文本到图像（T2I）预训练，其变分自编码器（VAE）压缩会丢失恢复所需的细节，且开放合成先验易引入内容不一致伪影。PixRestore 提出无 VAE 的像素空间扩散 Transformer（DiT），通过直接在 RGB 像素上进行流匹配，并利用自适应层级 DINO 特征引导退化感知，在保持高保真与感知质量的同时，将推理延迟降至 44 ms。该设计挑战了“大模型 T2I 先验更强”的共识，但在高分辨率下的计算扩展性与零样本泛化能力仍存疑。

## 研究背景

图像恢复任务中，低质量（LQ）图像往往包含丰富的视觉线索，而高质量（HQ）图像需忠实重建这些线索。传统回归模型使用 $L_1/L_2$ 损失优化，虽高效但易产生过平滑结果，丢失高频细节。扩散模型通过生成式先验提升感知质量，但主流方法如 FoundIR-v2 和 Flux-IR 依赖 T2I 预训练，其 VAE 编码过程可能丢弃纹理细节，且 T2I 的开放合成特性可能导致恢复结果与输入内容不一致。

UIR 的核心矛盾在于平衡保真度、感知质量与计算效率。现有生成式 UIR 方法虽提升了视觉真实感，但引入了三个成本：VAE 的有损瓶颈、T2I 先验的目标不匹配、以及十亿级骨干与迭代采样带来的冗余计算。PixRestore 的切入点在于重新审视 T2I 模型对 UIR 的适用性：UIR 从 LQ 图像出发，无需 T2I 的开放生成能力，而是需要鲁棒的退化适应与像素对齐的细节重建。

## 核心方法

### 像素空间流匹配

UIR 通常将图像编码至潜在空间以降低计算复杂度，但 VAE 压缩会牺牲小结构与细纹理。PixRestore 直接在 RGB 像素空间操作，通过 patchification 保持空间结构，避免 VAE 的信息损失。设计动机是解决 VAE 导致的细节丢失问题，使输出更忠实于输入。给定 HQ 图像 $y_{hq}$ 和 LQ 图像 $y_{lq}$，采用线性插值路径 $x_t = (1-t)y_{hq} + t\epsilon$，其中 $\epsilon \sim \mathcal{N}(0, I)$ 且 $t \sim U(0, 1)$。恢复 DiT $f_\theta$ 预测干净图像：

$$ \hat{y}_{hq} = f_\theta([y_{lq}; x_t], t, F(y_{lq})) $$

其中 $[\cdot; \cdot]$ 表示通道拼接，$F(y_{lq})$ 为 LQ 输入的多层 DINO 特征。流匹配损失定义为速度场误差：

$$ \mathcal{L}_{flow} = \|\hat{v}_t - v_t\|_2^2 $$

其中 $v_t = (x_t - y_{hq})/t$，$\hat{v}_t = (x_t - \hat{y}_{hq})/t$。该设计在相同训练设置下，像素 DiT 的 PSNR 达 26.62 dB，LPIPS 为 0.1593，优于所有潜在空间基线。

### 自适应层级视觉引导

静态全局退化表示不足以处理多样化复合退化，需动态适应不同退化类型。PixRestore 利用 DINOv2 自监督视觉基础模型提取多层密集特征，浅层保留局部结构，深层编码全局语义，且各层对不同退化的可靠性不同。设计动机是解决固定层或均匀平均导致的次优引导问题。对于每层 $l$，计算 LQ-HQ 特征相似度 $s_l$，并归一化为权重 $q_l$：

$$ q_l = \frac{\exp(s_l)}{\sum_{k \in \mathcal{L}} \exp(s_k)} $$

由于推理时无 HQ 图像，训练轻量预测器 $\rho_\psi$ 从 LQ 图像与特征估计权重 $p_l$：

$$ p_l = \text{softmax}(\rho_\psi([y_{lq}, U_l])) $$

交叉熵损失 $\mathcal{L}_{wpred} = -\sum_{l \in \mathcal{L}} q_l \log p_l$ 监督预测器。融合特征 $U_{fuse} = \sum_{l \in \mathcal{L}} p_l U_l$ 通过交叉注意力注入 DiT 块。此外，引入层级特征监督损失 $\mathcal{L}_{feat}$，对可靠性低的层施加更强的 HQ 特征监督，促进退化去除。

## 实验评估

实验在 GoPro、RESIDE 等 8 个公开基准及真实世界测试集上进行，对比 PromptIR、FoundIR-v2、Flux-IR 等回归与生成式方法。PixRestore 在大多数指标上表现领先，尤其在退化去除（DR-Score）与感知质量（LPIPS）上显著优于 T2I 基线。

| 方法 | PSNR (dB) | LPIPS | MUSIQ | DR-Score | 参数量 (M) | 延迟 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| PixRestore | 28.49 | 0.1120 | 55.52 | 65.20 | 53.70 | 44 |
| PixRestore-B | 28.49 | 0.1120 | 55.52 | 67.88 | 210.89 | 79 |
| FoundIR-v2* | 27.85 | 0.1773 | 54.32 | 51.80 | 16910.09 | 18293 |
| Flux-IR* | 21.01 | 0.4511 | 59.45 | 39.45 | 17698.23 | 795290 |

消融实验显示，添加单层 DINO 特征（层 5）将 PSNR 从 26.62 提升至 27.36，LPIPS 从 0.1593 降至 0.1489。自适应层级引导（A7）相比均匀平均（A6）进一步提升 PSNR 至 27.66，LPIPS 降至 0.1209，验证了退化依赖的层可靠性假设。单步微调（A10）相比多步模型（A9）将 PSNR 从 28.07 提升至 28.49，LPIPS 从 0.1202 降至 0.1120，表明单步生成在保持效率的同时提升了质量。

评估边界方面，DR-Score 使用 VLM 判断退化去除，虽与人类感知对齐，但存在随机性（测试 5 次取平均）。真实世界测试集无 GT，仅依赖无参考指标，可能低估保真度。代码已开源，但超参数与 GPU 配置细节需查阅附录，复现成本中等。

## 关联研究分析

从问题动机看，PixRestore 与 FoundIR-v2 均旨在提升 UIR 的感知质量，但 FoundIR-v2 依赖 SDXL 的 T2I 先验，通过 MoE 路由与 MLLM 描述符适应退化，而 PixRestore 摒弃 T2I 预训练，主张从头训练像素空间 DiT。这一差异源于对 VAE 瓶颈的批判：FoundIR-v2 的潜在空间压缩导致细节丢失，而 PixRestore 的像素空间建模直接保留空间证据。根源在于任务特性：UIR 需忠实重建输入细节，而非开放合成，因此 T2I 的生成先验并非必需，反而可能引入不一致伪影。

从方法设计看，PixRestore 与 MiM-DiT 同属 DiT 架构，但 MiM-DiT 采用层级化 MoE in MoE 架构进行专家路由，而 PixRestore 使用自适应层级 DINO 特征引导。MiM-DiT 在 FoundIR 上 PSNR 达 30.50 dB，略高于 PixRestore 的 30.20 dB，但 PixRestore 的延迟仅为 44 ms，远快于 MiM-DiT 的迭代采样。这一差异源于设计取舍：MiM-DiT 通过 MoE 解耦参数冲突，提升保真度，但计算成本高；PixRestore 通过轻量 DiT 与单步微调，牺牲部分保真度换取效率。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

PixRestore 解决的核心矛盾是生成式 UIR 中 T2I 先验导致的细节丢失与计算冗余。其切入点在于识别 UIR 与 T2I 的目标差异：UIR 需像素对齐的细节重建，而非开放合成，因此无需 T2I 的生成能力，而是需要鲁棒的退化适应与高效推理。PixRestore 通过像素空间流匹配与自适应 DINO 引导，在 53.7M 参数与 44 ms 延迟下实现了 PSNR 28.49 dB 与 LPIPS 0.1120 的性能，证明了无 VAE 设计的可行性。其边界在于，单步微调虽提升效率，但可能限制模型对复杂复合退化的建模能力，且真实世界测试集缺乏 GT，无法全面评估保真度。当输入图像包含空间变化大的未知混合退化时，自适应层级引导的可靠性是否仍能保持，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.16793)