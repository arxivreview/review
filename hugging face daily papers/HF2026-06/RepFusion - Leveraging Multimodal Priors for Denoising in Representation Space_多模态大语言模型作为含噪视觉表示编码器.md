# HuggingFace最新推荐论文 ｜RepFusion: Leveraging Multimodal Priors for Denoising in Representation Space ｜多模态大语言模型作为含噪视觉表示编码器

研究机构：Meta AI、美国纽约大学

作者：Xichen Pan、Aashu Singh、Satya Narayan Shukla 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.14700)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.14700)

> 现代文本到图像生成系统通常将大语言模型（LLM）限制为静态文本编码器，导致其强大的多模态先验无法参与去噪过程。现有方案在变分自编码器（VAE）潜空间中，因潜变量缺乏语义结构，LLM无法有效感知视觉状态；而统一架构虽尝试整合，但参数分配效率低下。RepFusion 将表示自编码器（RAE）的语义潜变量直接输入冻结的多模态大语言模型（MLLM），使其成为动态条件编码器，从而在相同推理算力下以更小的去噪器参数实现更优生成质量。该设计验证了预训练多模态先验可直接迁移至生成任务，但其在高频细节保真度上的表现及与个性化微调方法的兼容性尚存疑。

## 研究背景

理解本文需厘清两个关键概念：潜空间表示的语义属性与条件编码器的动态性。传统扩散模型在 VAE 潜空间去噪，该空间为重建优化，维度低且局部性强，不具备预训练语言模型可理解的语义结构。这导致 LLM 即使接入去噪循环，也缺乏可消费的视觉信号。表示自编码器（RAE）通过冻结 CLIP 或 DINO 等视觉基础模型作为编码器，构建了语义丰富的潜空间，使得视觉表示与 MLLM 的特征空间天然对齐。然而，现有 T2I 流水线中，LLM 仍仅处理文本，其多模态感知能力被闲置。

主流 T2I 架构面临参数分配效率瓶颈。Stable Diffusion 3 和 FLUX.1 等系统投入数十亿参数于文本编码器，但仅用于生成静态嵌入，去噪任务完全依赖新初始化的扩散 Transformer（DiT）。Transfusion 等统一架构尝试让 LLM 同时处理文本与视觉，但需联合训练大量参数，且未充分利用预训练 MLLM 的现成先验。RepFusion 的切入点在于：既然 MLLM 已通过 MLP 投影器对齐了干净视觉表示，那么将其扩展至含噪表示，即可让冻结的 LLM 直接为去噪过程提供动态条件，无需训练新的去噪器。

## 核心方法

### 方法参照系

标准 T2I 流程中，条件信号 $c$ 仅由文本嵌入 $E_\phi(y)$ 构成，去噪器独立处理含噪潜变量 $z_t$。本文的关键差异在于将含噪视觉表示 $z_t$ 纳入条件编码器输入，使条件信号 $c_t$ 随去噪步数动态变化，而非保持静态。

### 含噪表示编码机制

RepFusion 将含噪 RAE 潜变量 $z_t$ 与时间步嵌入 $e_t$ 相加后，通过 MLP 投影器 $P_\psi$ 映射至 LLM 输入空间，并与文本 token 序列拼接。条件信号定义为：

$$ c_t = \text{Last}_N(E_{\text{LLM}}([E_{\text{LLM}}(y), P_\psi(z_t + e_t)])) $$

其中 $\text{Last}_N$ 选取对应含噪视觉 token 的最后 $N$ 个隐藏状态。这一设计使 LLM 能感知当前去噪状态，其输出 $c_t$ 随 $z_t$ 演化而更新，解决了静态文本嵌入无法反映视觉生成进程的问题。

### 动态条件注入与参数分配

DiT 通过自适应层归一化（AdaLN-Single）接收 $c_t$，每个块计算调制参数：

$$ m_t = W_{\text{mod}}(\text{SiLU}(e_t + c_t)) $$

其中 $W_{\text{mod}}$ 为共享线性层，$m_t$ 被分解为移位 $\beta$、缩放 $\gamma$ 和残差门控 $\alpha$，逐 token 应用于 DiT 块。该机制避免了交叉注意力模块，且 $c_t$ 与 DiT 中间状态 $h_{t\ell}$ 在 token 维度对齐（$N=576$），确保条件信号精确匹配视觉结构。在参数分配上，RepFusion 冻结 7B MLLM，仅微调 1.3B DiT 和 MLP 投影器，而 TextEmbed 基线需训练 8B DiT，Transfusion 需训练 8B 联合 Transformer，体现了“复用预训练先验优于扩大新去噪器”的策略。

## 实验评估

实验在 GenEval 基准上进行，对比 TextEmbed、Transfusion 和 MetaQuery 基线。RepFusion 在 RAE 潜空间下达到 0.70 的 GenEval 分数，显著优于 TextEmbed-RAE（0.64）和 Transfusion-RAE（0.66）。在相同推理 FLOPs（约 550 TFLOPs）下，RepFusion 仅训练 1.3B 参数，而 TextEmbed 和 Transfusion 分别训练 8B 参数，表明预训练 MLLM 先验的高效性。

| 方法 | 潜空间 | GenEval 分数 | 可训练参数 (B) | 推理 FLOPs (TFLOPs) |
| :--- | :--- | :--- | :--- | :--- |
| RepFusion | RAE | 0.70 | 1.3 | 547 |
| TextEmbed-RAE | RAE | 0.64 | 8.0 | 552 |
| Transfusion-RAE | RAE | 0.66 | 8.0 | 559 |
| MetaQuery | RAE | 0.55 | 1.3 | 113 |

消融实验揭示，从 VAE 切换到 RAE 为 RepFusion 带来 30% 相对提升（+0.16 绝对值），而 TextEmbed 仅提升 21%（+0.10），Transfusion 提升 11%（+0.06），证明 RAE 的语义结构是 MLLM 先验生效的前提。冻结 MLLM 优于联合微调：在 RAE 空间下，微调 LLM 骨干导致性能从 0.70 降至 0.65，表明预训练多模态先验比任务特定优化更鲁棒。MetaQuery 基线即使增加推理 FLOPs 至 552 TFLOPs，GenEval 仍为 0.54，证实增益源于含噪表示输入而非单纯计算量增加。

评估边界受限于 GenEval 的组合生成指标，未覆盖高频细节保真度（如 LPIPS）或个性化概念保留（如 CLIP-I）。代码未公开，但训练细节完整：128 H200 GPU，batch size 2048，10 epochs，AdamW 优化器，余弦衰减学习率。

## 关联研究分析

从问题动机看，RepFusion 与 Transfusion 均旨在整合语言模型与去噪器，但 Transfusion 通过联合训练单一 Transformer 处理文本与视觉，而 RepFusion 复用冻结 MLLM 作为专用编码器。Transfusion 的瓶颈在于新初始化的去噪模块缺乏多模态先验，导致参数效率低；RepFusion 则利用 MLLM 已有的视觉感知能力，将参数预算集中于轻量去噪器。这一差异源于任务特性：生成任务更依赖预训练视觉先验，而非从零学习视觉-语言对齐。

从方法设计看，RepFusion 与 MetaQuery/BLIP-3o 同属 RAE 路线，但 MetaQuery 使用可学习查询替代含噪表示输入，导致条件信号静态化。RepFusion 的含噪表示输入使条件随去噪步数演化，解锁了测试时计算扩展：重复 MLLM 编码携带输入依赖信息，而 MetaQuery 的重复推理无新视觉信号。这暗示，静态条件机制无法充分利用 MLLM 的动态感知能力，含噪表示输入是激活该能力的关键。

## 总结

RepFusion 解决了 T2I 系统中 LLM 多模态先验闲置与去噪器参数低效的矛盾。其切入点在于 RAE 潜空间的语义结构使冻结 MLLM 能直接编码含噪视觉表示，从而以 1.3B 可训练参数超越 8B 参数的 TextEmbed 和 Transfusion 基线，GenEval 分数达 0.70。该设计证明了预训练多模态先验可直接迁移至生成任务，且冻结优于联合微调。然而，实验未评估高频细节保真度，且 0.70 的分数是否受限于 1.3B DiT 的容量上限，论文未给出回答。当支持集增大或引入个性化微调时，冻结 MLLM 的通用先验是否会与特定概念冲突，仍需验证。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.14700)