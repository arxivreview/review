# WACV2026最新论文 ｜SCAdapter: Content-Style Disentanglement for Diffusion Style Transfer ｜SCAdapter：基于CLIP空间显式解耦的扩散风格迁移

作者：Luan Thanh Trinh、Kenji Doi、Atsuki Osanai

论文原文见 [arXiv](https://arxiv.org/abs/2512.12963)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.12963)

> 扩散模型在艺术风格迁移中表现优异，但在照片写实场景下常产生绘画化伪影或丢失细节，根源在于内容-风格特征在潜空间中的纠缠。现有方法要么依赖推理时优化导致速度瓶颈，要么缺乏对原图风格残留的显式控制。SCAdapter 通过 CLIP 图像空间的代数运算（均值与减法）显式分离纯内容与纯风格特征，并结合 KVS 注入与 CSAdaIN 实现可控混合。该方法在写实迁移上取得 SOTA 性能且推理速度提升 2 倍以上，但其解耦机制对复杂语义场景的鲁棒性仍存疑。

## 研究背景

当扩散模型处理“晴天转雪景”这类写实风格迁移时，往往无法彻底移除原图的天气特征，导致输出图像出现不自然的混合状态。这一现象源于内容-风格纠缠（Content-Style Entanglement），即自然图像中语义结构与视觉属性在像素及特征层面高度耦合。为了解耦，早期方法依赖 VGG 特征匹配或 GAN 循环一致性，但受限于计算成本与表达能力。随着 Stable Diffusion 成为主流骨干，研究重心转向如何在去噪过程中实现可控的风格注入。

当前主流路线分为注意力调制与文本反转两类。注意力调制方法如 StyleID 利用自注意力层的 Key/Value 特征编码风格，Query 特征编码内容，在艺术迁移中表现强劲，但面对缺乏鲜明笔触的写实风格时，往往产生绘画化结果。文本反转方法如 InST 和 InstantStyle 将风格编码至提示嵌入空间，虽在写实场景有一定优势，但难以精确控制原图风格的保留比例。此外，DiffuseIT 等推理优化方法虽无需训练，但每个风格-内容对需耗时数百秒，难以满足实时需求。SCAdapter 的切入点在于利用 CLIP 图像空间的线性可分性，通过显式代数运算替代隐式学习或推理优化，实现高效且干净的内容-风格分离。

## 核心方法

### 方法参照系

本文问题属于扩散模型下的条件生成任务，标准流程为：编码内容/风格特征 → 注入去噪网络 → 生成图像。与 IP-Adapter 等通用适配器不同，SCAdapter 的关键差异在于引入了显式的“减法”解耦机制，而非依赖交叉注意力的隐式过滤，旨在从源头消除特征交叉污染。

### CLIP 空间显式解耦

传统方法直接提取 CLIP 特征作为风格条件，导致参考图中的内容语义（如物体形状）泄漏至输出。SCAdapter 设计了一个内容提取器（Content Extractor），其核心假设是：相同内容在不同风格下的 CLIP 特征均值即为纯内容特征。通过微调 CLIP 的视觉投影层，利用 LoRA 生成的多风格变体图像进行训练，得到内容特征 $\mathbf{C}(I)$。随后，风格特征 $\mathbf{S}(I)$ 通过整体 CLIP 特征减去内容特征获得：

$$ \mathbf{S}(I) = \mathbf{CLIP}(I) - \mathbf{C}(I) $$

这一代数减法在特征空间中实现了正交分离，确保风格向量不包含内容语义，从而解决了参考图内容泄漏导致的构图扭曲问题。

### KVS 注入与 CSAdaIN 控制

解耦后的特征需有效注入去噪 UNet。SCAdapter 借鉴 StyleID 的发现，将风格特征与提示嵌入的 Key/Value 拼接，形成 KVS 注入（Key-Value Style Injection），专门注入上采样块以捕捉局部风格细节，而内容特征注入下采样块以维持结构。为解决写实迁移中需保留部分原风格的需求，引入可控风格自适应实例归一化（CSAdaIN）。给定原风格 $\mathbf{S}_1$ 与新风格 $\mathbf{S}_2$，通过权重 $\omega \in [0,1]$ 插值统计量：

$$ \mu_\omega = \omega \mu_1 + (1-\omega) \mu_2, \quad \sigma_\omega = \omega \sigma_1 + (1-\omega) \sigma_2 $$

该机制允许用户在“完全替换”与“部分保留”间平滑过渡，并通过风格迁移一致性损失（Style Transfer Consistency Loss）在训练中强化多风格混合的连贯性，避免了静态权重合并导致的风格冲突。

## 实验评估

实验基于 SD 1.5 与 SDXL 骨干，在 MSCOCO 与 WikiArt 数据集上评估。基线覆盖 StyleID、InST、InstantStyle、DiffuseIT 等扩散方法及 AesPA-Net 等传统方法，但缺乏对最新 LoRA 子空间混合方法（如 Balanced Subspace Blending）的对比。

| 任务 | 指标 | Ours (SDXL) | StyleID | InstantStyle | DiffuseIT |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Photo-realistic | FID_style ↓ | **21.151** | 24.349 | 23.051 | 33.119 |
| Photo-realistic | LPIPS_content ↓ | **0.3015** | 0.3774 | 0.4202 | 0.5226 |
| Artistic | ArtFID ↓ | **28.541** | 28.801 | 39.415 | 40.721 |

在写实迁移任务中，SCAdapter 的 FID_style 为 21.151，显著优于 StyleID 的 24.349 和 InstantStyle 的 23.051，表明显式解耦有效抑制了风格残留。艺术迁移的 ArtFID 为 28.541，略优于 StyleID 的 28.801，优势幅度较小，可能受限于艺术风格本身的多样性。

消融实验显示，移除 KVS 注入后，写实任务的 FID_style 从 22.417 上升至 22.988，艺术任务的 ArtFID 从 28.707 上升至 28.887，证实 KVS 对局部细节捕捉的关键作用。移除风格一致性损失后，写实任务的 Aesthetic Score 从 5.2198 降至 5.1979，LPIPS_content 从 0.3055 升至 0.3085，表明该损失对多风格混合时的内容保持有正向贡献，但边际收益有限。

评估协议采用 ArtFID 综合衡量内容与风格保真度，避免了单一 Style Loss 的过拟合风险。然而，论文未报告置信区间，且仅使用 20 张内容图像与 40 张风格图像进行定量对比，样本量较小，统计显著性存疑。代码未公开，超参数（如 $\lambda=0.1$）的敏感性未充分探讨，可复现性受限。

## 关联研究分析

从解耦机制看，SCAdapter 与 CleanStyle 均针对内容泄漏问题，但路线截然不同。CleanStyle 采用 SVD 截断尾部奇异值以过滤内容伪影，属于后处理信号过滤；SCAdapter 则通过训练内容提取器进行显式代数减法，属于前置特征分离。SCAdapter 的优势在于解耦更彻底，能同时处理原图风格残留与参考图内容泄漏，但依赖 LoRA 生成的伪数据训练，引入了数据分布偏差风险。CleanStyle 无需训练，部署更灵活，但可能损失高频风格细节。两者在“解耦精度”与“部署效率”间做出了不同取舍。

从风格控制看，SCAdapter 的 CSAdaIN 与 Balanced Subspace Blending 均致力于风格强度可控性，但作用空间不同。Balanced Subspace Blending 在 LoRA 子空间层面通过可学习混合矩阵调整权重，属于参数空间控制；SCAdapter 在特征统计量层面通过 AdaIN 插值，属于特征空间控制。SCAdapter 的方法更直观，支持任意数量风格的线性混合，但缺乏对风格间语义冲突的非线性处理机制。Balanced Subspace Blending 能捕捉子空间间的正交性，但训练复杂度高。SCAdapter 在写实场景下的优势表明，特征统计量的插值可能比子空间混合更适用于低对比度风格迁移。

## 总结

SCAdapter 针对扩散模型在写实风格迁移中风格残留与内容泄漏的矛盾，利用 CLIP 空间显式代数解耦替代隐式学习，实现了高效且干净的特征分离。该方法通过 KVS 注入与 CSAdaIN 结合，在写实迁移任务中取得 FID_style 21.151 的 SOTA 性能，推理速度较 DiffuseIT 提升 2 倍以上。其边界在于解耦机制依赖 LoRA 生成的伪数据，且对艺术风格的优势幅度有限，暗示显式减法在复杂语义场景下可能不如子空间混合鲁棒。当支持集增大到 5-shot 时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.12963)