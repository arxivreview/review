# CVPR2026最新论文 ｜RADAR: VQ-VAE Decoder of VAR is a Good Student for Restoring Against Degradation by Acceleration ｜语义成本感知掩码与解码器适配

作者：Ziyang Wang、Yue Zhang、Mingdao Wang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_de23d4a2420b)

> VAR 模型在推理加速中面临注意力模式复杂导致的掩码设计难题，现有启发式方法缺乏量化准则以平衡效率与质量。RADAR 将掩码设计转化为预算约束优化问题，并首次引入解码器侧的内部知识蒸馏以补偿潜变量退化。该方法实现了约 1.9 倍加速且保持生成质量，但其“数据-free”特性在开放域任务中的泛化能力存疑。

## 研究背景

VAR 模型通过 Next-Scale 预测范式，将图像生成从光栅扫描的 Token 序列转化为从粗到细的尺度层级序列。这一结构使得早期粗尺度 Token 在自注意力中呈现显著的“注意力汇聚”现象，即全局结构由少数粗粒度特征主导，而细尺度 Token 则表现出强烈的空间局部性。这种非均匀的注意力分布意味着，对注意力矩阵不同区域的剪枝对最终图像质量的影响截然不同，传统的均匀或启发式掩码策略难以精准保留关键语义信息。

现有加速方法如 LiteVAR 和 HACK 依赖人工观察到的对角线集中模式或手动划分注意力头，缺乏量化指标来衡量 Token 剪枝与上下文压缩对语义内容的具体代价。这种定性设计导致加速比与质量退化之间的权衡无法显式优化，且在激进加速下，Transformer 输出的潜变量序列发生退化，直接导致 VQ-VAE 解码器重建图像出现结构性失真。RADAR 的切入点在于，将掩码设计从经验主义转向基于语义成本的约束优化，并指出被忽视的解码器适配环节是恢复质量的关键低成本路径。

## 核心方法

### 方法参照系

VAR 加速通常通过修改 Transformer 注意力掩码来减少 FLOPs 和 KV 缓存内存。标准流程是设计固定形状的掩码以跳过低重要性计算，但 VAR 的层级生成特性使得掩码设计需同时考虑步骤、尺度和空间维度，现有方法多采用手工规则，缺乏对语义损失的系统性量化。

### 语义成本感知掩码（SCA-Mask）

针对手工掩码缺乏量化准则的问题，RADAR 将注意力矩阵划分为与 GPU 计算粒度匹配的 Tile（如 64×64），并定义 Tile 的语义重要性为其与其他 Tile 的信息交换频率。具体地，计算每个 Tile 作为 Query 和 Key/Value 的有效注意力次数，将其转化为预算约束下的优化问题。

$$
\max_{x,y} \alpha \sum_{i,j} \text{Score}_Q(\text{tile}_{i,j}) x_{ij} + \beta \sum_{i,j} \text{Score}_{KV}(\text{tile}_{i,j}) y_{ij}
$$

$$
\text{s.t. } \sum_{i,j} c_{ij} x_{ij} \le C_{\text{budget}}, \quad \sum_{i,j} m_{ij} y_{ij} \le M_{\text{budget}}
$$

该公式在给定计算和内存预算下，最大化保留的语义内容。由于 GPU 上每个 Tile 的计算成本近似恒定，约束简化为线性规划，可高效求解。此设计自动识别高语义成本 Tile 并保留其计算，避免了启发式掩码在复杂空间结构下的误剪枝。

### 解码器后加速适配（PAA）

SCA-Mask 导致的潜变量退化无法仅靠 Transformer 侧优化完全消除。RADAR 引入 PAA 模块，利用内部知识蒸馏（Internal Knowledge Distillation）微调 VQ-VAE 解码器。具体做法是并行运行正常前向分支（教师）和加速前向分支（学生），通过 LoRA 适配器最小化两者解码图像的 MSE 和 LPIPS 损失。

$$
\mathcal{L}_{KD} = \lambda_m \text{MSE}(\hat{im}_n, \hat{im}_{ac}) + \lambda_p \text{LPIPS}(\hat{im}_n, \hat{im}_{ac})
$$

其中 $\hat{im}_n$ 为正常解码图像，$\hat{im}_{ac}$ 为加速解码图像。PAA 仅训练 LoRA 参数，冻结 VAR 主干和解码器权重，无需外部数据。这一设计利用了解码器参数量小（约 100M）且推理占比低的特性，以极低的 GPU 开销补偿 Transformer 侧激进剪枝带来的质量损失，实现了加速与保真的解耦优化。

## 实验评估

实验基于 ImageNet-1K 256x256 类别条件生成、GenEval 文本到图像及 VQA 基准，对比 Infinity、ScaleKV、FastVAR 等加速方法。RADAR 在 VAR-d20 骨干上实现了 1.92 倍加速，FID 从退化状态的 5.02 恢复至 2.68，接近原始 VAR 的 2.61。

| 方法 | FID↓ | GFLOPs↓ | Latency(ms)↓ |
| :--- | :--- | :--- | :--- |
| Vanilla VAR | 2.61 | 81.25 | 5458±57 |
| +SCA-Mask | 5.02 | 64.47 | 2895±88 |
| +PAA | 2.88 | 81.44 | 5403±48 |
| +full RADAR | 2.68 | 64.47 | 2964±84 |

消融显示，SCA-Mask 单独使用导致 FID 显著恶化，而 PAA 单独使用对未退化模型有轻微负迁移，两者结合才实现质量恢复。在 VARGPT-v1.1 上，RADAR 实现 1.6 倍吞吐提升，GQA 准确率从 66.2 降至 63.8，仍优于 Qwen-VL-Chat 等基线。

评估边界方面，实验仅在单卡 RTX 5090 上进行，未覆盖多卡或动态分辨率场景。PAA 的“数据-free”特性依赖于内部蒸馏，其在开放域文本生成任务中是否依然有效，论文未提供充分证据。代码未公开，超参数如 LoRA 秩和损失权重 $\lambda_m, \lambda_p$ 的具体值未在正文中详细列出，影响复现性。

## 关联研究分析

从问题动机看，RADAR 与 StepVAR 和 SSD 同属推理加速路线，但 StepVAR 依赖结构-纹理引导的启发式剪枝，SSD 利用空间先验进行推测解码，两者均未解决掩码设计的量化问题。RADAR 的核心差异在于将掩码设计形式化为优化问题，提供了可解释的语义成本指标。然而，StepVAR 在保持 1.92 FID 的同时实现了效率提升，而 RADAR 的 FID 2.68 高于 StepVAR，这暗示优化求解的掩码可能在特定骨干上不如启发式规则鲁棒，或 PAA 的补偿能力存在上限。

从方法设计看，RADAR 与 MVAR 形成鲜明对比。MVAR 通过重训练 Transformer 块来适应激进加速，消耗大量 GPU 小时；RADAR 则通过轻量级解码器适配避免重训练。这种差异源于对“退化来源”的不同判断：MVAR 认为 Transformer 输出需重新学习，RADAR 认为解码器可灵活映射退化潜变量。RADAR 的 PAA 模块在 VQA 任务中表现良好，但在高频细节恢复上可能不如 MVAR 的重训练方案，因为 LoRA 的低秩约束限制了解码器的表达能力。

## 总结

RADAR 旨在解决 VAR 加速中掩码设计缺乏量化准则及潜变量退化导致的质量损失矛盾。其切入点在于将掩码设计转化为预算约束优化问题，并首次引入解码器侧的内部知识蒸馏以低成本补偿退化。方法通过 SCA-Mask 自动求解高语义成本 Tile，结合 PAA 微调解码器，实现了 1.92 倍加速且 FID 恢复至 2.68。实验证明该框架在类别条件生成和 VQA 任务中有效，但边界在于 PAA 的“数据-free”特性在开放域任务中的泛化能力未经验证，且 LoRA 的低秩约束可能限制其对极端退化的补偿能力。当支持集增大到开放域文本生成时，内部蒸馏是否足以替代外部数据驱动的重训练，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_de23d4a2420b)