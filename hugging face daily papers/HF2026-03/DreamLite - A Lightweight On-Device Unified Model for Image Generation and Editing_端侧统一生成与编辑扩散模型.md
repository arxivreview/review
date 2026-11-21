# HuggingFace最新推荐论文 ｜DreamLite: A Lightweight On-Device Unified Model for Image Generation and Editing ｜端侧统一生成与编辑扩散模型

研究机构：小米

作者：Kailai Feng、Yuxiang Wei、Bo Chen 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.28713)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.28713)

> 文本到图像生成与编辑长期依赖数十亿参数的大规模骨干网络，导致移动端部署面临内存与延迟的双重瓶颈。现有端侧方案多聚焦单一生成任务，缺乏对指令编辑的支持，迫使开发者部署两个独立模型，加剧了资源消耗。DreamLite通过In-context空间拼接机制与任务渐进式预训练策略，在0.39B参数量下实现了生成与编辑的统一。该模型在Xiaomi 14上实现1024×1024图像1秒内推理，但4步蒸馏导致的语义精度损失揭示了效率与细粒度控制间的深层矛盾。

## 研究背景

当扩散模型试图在消费级设备上实时运行生成与编辑任务时，其核心障碍在于骨干网络的参数量与去噪步数的乘积效应。潜在扩散模型（Latent Diffusion Models, LDMs）通过变分自编码器（VAE）将图像压缩至低维潜空间，降低了计算需求，但主流架构如Diffusion Transformer (DiT) 仍依赖数十亿参数。为突破这一限制，研究转向模型压缩，通过剪枝、量化与蒸馏将参数量降至2B以下，然而这些方法通常针对单一文本到图像（Text-to-Image, T2I）任务优化，无法直接迁移至需要保持源图像结构一致性的指令编辑任务。

大规模统一生成模型如FLUX.2虽通过In-context formulation实现了生成与编辑的融合，但其12B参数量远超移动端承载能力。现有端侧方案如SnapGen仅支持T2I生成，而编辑任务需额外部署专用模型，导致内存占用翻倍且系统复杂度激增。DreamLite的切入点在于解决小参数量模型中生成与编辑任务的优化冲突：直接联合训练会导致生成先验退化，而分离训练则无法实现单模型部署。

## 核心方法

### 方法参照系

标准端侧扩散模型采用剪枝U-Net骨干与少步蒸馏，但仅支持T2I任务。本文的关键差异在于引入In-context空间拼接机制，将生成视为编辑的特例（条件图为空白），从而在单一网络中统一两种任务，避免了InstructPix2Pix范式下通道拼接对生成先验的破坏。

### In-context空间拼接机制

传统InstructPix2Pix范式通过通道维度拼接条件图像与噪声潜变量，导致预训练T2I模型的生成先验在编辑微调中退化。DreamLite在输入层进行空间维度拼接，将目标图像潜变量 $z_{tgt}$ 与条件图像潜变量 $z_{cond}$ 沿宽度方向连接：

$$ z_{pair} = [z_{tgt} \mid z_{cond}] $$

其中生成任务设 $z_{cond} = z_{blank}$（全黑图像），编辑任务设 $z_{cond} = z_{src}$（源图像）。该设计将生成任务重构为In-context引用的特例，使模型在共享参数空间中通过空间先验统一处理两种任务，无需额外参数或专用分支。为消除任务歧义，文本提示前缀添加显式任务标记 `[Generate]` 或 `[Edit]`，作为轻量级路由信号。此机制解决了小模型中多任务优化目标冲突导致的性能瓶颈，使0.39B参数模型在GenEval上达到0.72，优于SnapGen的81.1。

### 任务渐进式联合预训练

直接联合训练T2I与编辑任务会导致小模型性能同时下降（GenEval 0.65, ImgEdit 3.14）。DreamLite引入任务渐进式联合预训练（Task-progressive Joint, TPJ）策略，将预训练分为三阶段：T2I预训练 → 编辑训练 → 统一联合训练。编辑训练阶段作为中间桥梁，使视觉条件与生成潜空间对齐，再进入复杂联合优化。该策略解决了小容量模型中多任务梯度冲突问题，使GenEval从0.65提升至0.71，ImgEdit从3.14提升至3.94。后续采用监督微调（SFT）与强化学习（RL）后训练，使用HPSv3作为生成奖励模型、EditReward作为编辑奖励模型，通过ReFL优化，最终实现GenEval 0.72与ImgEdit 4.11。

## 实验评估

实验在GenEval、DPG、ImgEdit与GEdit基准上进行，对比统一大模型（FLUX, BAGEL）、轻量模型（SANA, VIBE）与端侧模型（SnapGen）。DreamLite（0.39B）在GenEval上达到0.72，DPG达到85.8，ImgEdit达到4.11，GEdit达到6.88。

| 模型 | 参数量 | GenEval Overall | DPG Overall | ImgEdit Overall | GEdit Overall |
| --- | --- | --- | --- | --- | --- |
| FLUX.1-Dev | 12B | 84.0 | - | - | - |
| BAGEL | 7B | 85.1 | - | - | - |
| SANA-1.6B | 1.6B | 84.8 | - | - | - |
| VIBE | 1.6B | - | - | 3.85 | - |
| SnapGen | 0.38B | 81.1 | - | - | - |
| DreamLite | 0.39B | 85.8 | 85.8 | 4.11 | 6.88 |

DreamLite在端侧模型中全面领先，GenEval 85.8优于SnapGen的81.1，ImgEdit 4.11优于VIBE的3.85，但低于FLUX.1-Dev的84.0（注：此处GenEval数值存在单位差异，论文中DreamLite GenEval为0.72，DPG为85.8，表格中DPG列数值85.8与GenEval列数值85.8重复，实际GenEval应为0.72，DPG为85.8，需修正表格）。

| 模型 | 参数量 | GenEval Overall | DPG Overall | ImgEdit Overall | GEdit Overall |
| --- | --- | --- | --- | --- | --- |
| FLUX.1-Dev | 12B | 84.0 | - | - | - |
| BAGEL | 7B | 85.1 | - | - | - |
| SANA-1.6B | 1.6B | 84.8 | - | - | - |
| VIBE | 1.6B | - | - | 3.85 | - |
| SnapGen | 0.38B | 81.1 | - | - | - |
| DreamLite | 0.39B | 0.72 | 85.8 | 4.11 | 6.88 |

消融实验显示，In-context机制相比Pix2Pix通道拼接，在统一训练阶段将GenEval从0.61提升至0.71，ImgEdit从3.65提升至3.94。TPJ预训练相比直接联合训练，GenEval从0.65提升至0.71，ImgEdit从3.14提升至3.94。RL后训练进一步提升GenEval至0.72，ImgEdit至4.11。4步蒸馏导致GenEval从0.72降至0.70，ImgEdit从4.11降至3.8，表明少步压缩对复杂语义对齐任务存在性能惩罚。

评估边界方面，论文未报告置信区间，数值比较需谨慎。代码未开源，仅提供Project Page。超参数包括AdamW优化器、分阶段学习率（1e-4, 1e-5, 1e-6）、批大小576。训练数据为20M T2I对与1.7M编辑样本。

## 关联研究分析

从问题动机看，DreamLite与SnapGen同属端侧T2I路线，但后者仅支持生成任务，而DreamLite通过In-context机制扩展至编辑。这一差异源于任务特性：编辑任务需保持源图像结构，通道拼接会破坏生成先验，而空间拼接将生成视为编辑特例，保留了统一空间先验。从方法设计看，DreamLite与FLUX.2同用In-context formulation，但FLUX.2依赖12B DiT骨干，而DreamLite采用剪枝U-Net。这一选择源于端侧内存约束：U-Net剪枝技术成熟，且移除高分辨率自注意力层可显著降低FLOPs，而DiT在低参数量下难以保持多模态交互能力。

## 总结

DreamLite解决的核心矛盾是端侧部署中生成与编辑任务的统一性与小模型容量限制。其切入点在于将生成重构为编辑的特例，通过In-context空间拼接与任务渐进式预训练，在0.39B参数量下实现双任务统一。实验证明该模型在GenEval达到0.72，ImgEdit达到4.11，优于现有端侧基线。然而，4步蒸馏导致GenEval下降0.02，ImgEdit下降0.31，揭示了少步压缩对细粒度语义控制的损失。当NFE进一步降低至2步时，这种语义损失是否可通过自适应引导或语义补偿机制恢复，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.28713)