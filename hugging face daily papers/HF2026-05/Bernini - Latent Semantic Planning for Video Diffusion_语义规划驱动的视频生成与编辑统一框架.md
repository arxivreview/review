# HuggingFace最新推荐论文 ｜Bernini: Latent Semantic Planning for Video Diffusion ｜语义规划驱动的视频生成与编辑统一框架

作者：Bernini Team、Chenchen Liu、Junyi Chen 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.22344)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.22344)

> 视频生成领域长期面临语义理解与像素合成割裂的困境，现有方法难以在保持高保真度的同时实现复杂指令的精确遵循。Bernini 通过引入多模态大语言模型（MLLM）作为语义规划器，以 ViT 嵌入空间为接口连接扩散模型，解决了这一鸿沟。该框架采用 Planner-Renderer 解耦架构，实现了生成与编辑任务的统一。其核心价值在于验证了预训练理解能力向生成任务的直接迁移，但编辑任务的有效性评估仍依赖自设基准，外部可比性存疑。

## 研究背景

当扩散模型试图遵循“将视频中的花瓶替换为绿色植物”这类复杂指令时，其内部的时间/空间注意力机制往往无法精确解耦语义意图与像素细节，导致生成结果出现语义漂移或细节丢失。这一失效源于扩散模型的去噪过程本质上是像素级的，缺乏高层语义推理能力。多模态大语言模型（MLLM）擅长处理长指令和多参考图像，但其输出通常是离散文本或低维向量，无法直接驱动高分辨率视频合成。因此，如何在 MLLM 的语义空间与扩散模型的像素潜空间之间建立高效接口，成为统一理解与生成的关键。

视频生成领域的主流路线分为两类：一是联合骨干网络，如 Emu3 和 Janus，试图在单一 Transformer 中同时处理理解和生成，但往往牺牲了生成质量或理解深度；二是 MLLM 作为条件器，如 BAGEL，通过外部投影将 MLLM 特征注入扩散模型，但接口设计通常依赖离散 token 或额外适配器，导致语义信息损失。Bernini 的切入点在于利用 MLLM 自身的 ViT 嵌入空间作为连续语义接口，避免了离散化带来的信息损失，并允许两个组件独立训练后轻量级联合优化，从而保留 MLLM 的预训练理解能力。

## 核心方法

### 方法参照系

Bernini 属于“MLLM 作为视觉生成条件器”的技术路线。与 Janus 使用 VQ tokenizer 或 BAGEL 使用混合专家架构不同，Bernini 的关键差异在于将 MLLM 的连续 ViT 嵌入直接作为扩散模型的条件信号，而非通过离散 token 或额外投影层。这种设计使得语义规划与像素渲染在表示空间上解耦，但要求接口具备足够的语义容量以支撑复杂编辑任务。

### 基于掩码生成的语义规划

传统方法中，MLLM 输出通常作为文本特征直接拼接至扩散模型，缺乏对目标视觉内容的显式规划。Bernini 在 Planner 阶段引入掩码生成范式，将目标视觉 token 随机掩码，训练 MLLM 从上下文推断缺失内容。掩码比例 $r$ 从 Beta 分布 $\text{Beta}(\alpha, \beta)$ 中采样，训练目标为恢复被掩码的 ViT 嵌入：

$$ \mathcal{L}_{\text{visual}} = \mathbb{E}_{r \sim \text{Beta}(\alpha, \beta)} \left[ \| \hat{v}_{\text{tgt}} - v_{\text{tgt}} \|_2^2 \right] $$

该公式表明，Planner 学习的是在连续 ViT 空间中的语义重构，而非离散 token 预测。推理时，通过 $K$ 步迭代掩码细化，逐步从全掩码状态恢复完整目标表示。这一设计解决了传统文本条件无法精确指定目标视觉细节的问题，使 MLLM 能够“想象”出目标场景的语义结构，为 Renderer 提供高密度语义引导。

### 段感知三维旋转位置编码

在多源输入（如源视频、参考图像、目标输出）拼接为统一序列时，不同段的视觉 token 可能共享相同的时空坐标 $(t, h, w)$，导致注意力机制无法区分身份。Bernini 引入 SA-3D RoPE，将段索引 $i$ 编码为全局相位调制：

$$ \mathbf{r}_{\text{SA-3D}} = \mathbf{r}_{t,h,w} \odot e^{j \phi_i} $$

其中 $\phi_i$ 为段索引对应的相位。该公式在标准 3D RoPE 基础上叠加段级相位，使不同段的 token 在旋转空间中具有可区分的相位特征。这一设计解决了多主体一致性生成中常见的身份混淆问题，确保 Renderer 在去噪过程中能准确关联源内容与目标内容，提升编辑任务中的细节保持能力。

## 实验评估

Bernini 在 VBench、OpenS2V-Eval 及自设 Bernini-Bench 上进行评估。基线覆盖闭源系统（Sora, Veo3, Kling O3）和开源系统（Wan2.1-14B, CogVideoX-5B）。在 VBench 上，Bernini 未直接报告总分，但引用 Wan2.1-14B 为 83.69，据领域综述 SOTA AnyFlow 为 84.10，表明 Bernini 在生成任务上接近但未超越当前 SOTA。在 OpenS2V-Eval 上，Bernini 报告 SOTA，但该基准数据稀疏，缺乏可比数值。Bernini-Bench 采用 GSB（Good-Same-Bad）人工评估，Bernini 在视频一致性维度显著优于 Kling O3，与 Wan2.7 持平。

| 基准 | 方法 | 得分/胜率 | 备注 |
| :--- | :--- | :--- | :--- |
| VBench | Wan2.1-14B | 83.69 | 基线引用值 |
| Bernini-Bench | Bernini vs Kling O3 | 视频一致性显著优势 | GSB 人工评估 |
| Bernini-Bench | Bernini vs Wan2.7 | 整体持平 | GSB 人工评估 |

消融实验显示，引入 CoT 推理机制后，Bernini 在推理增强编辑任务上性能提升，但具体数值未在正文中详细列出。设计决策验证表明，使用 MLLM 的 ViT 嵌入而非离散 token 是提升编辑精度的关键，但论文未提供量化对比。评估边界方面，Bernini-Bench 缺乏公开数据集和自动评估指标，GSB 评估受主观偏差影响，可复现性受限。代码未开源，超参数（如 Beta 分布参数）未完全披露，限制了外部验证。

## 关联研究分析

从问题动机看，Bernini 与 Kaleido 均关注多主体一致性，但 Kaleido 依赖参考图像特征注入，而 Bernini 通过 SA-3D RoPE 在架构层面解决位置歧义。这一差异源于任务特性：Kaleido 聚焦静态主体保持，Bernini 需处理动态视频编辑中的时空关联。从方法设计看，Bernini 与 BAGEL 同属 MLLM 条件器路线，但 BAGEL 使用混合专家架构统一理解与生成，Bernini 采用串行 Planner-Renderer 架构。BAGEL 的架构更紧凑，但训练耦合度高；Bernini 的解耦设计允许独立优化，但引入了接口对齐成本。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

Bernini 旨在解决视频生成中语义理解与像素合成的割裂问题，通过 MLLM 的 ViT 嵌入空间作为连续语义接口，实现了理解能力向生成任务的直接迁移。该框架采用 Planner-Renderer 解耦架构，结合掩码生成语义规划和 SA-3D RoPE 位置编码，在编辑任务上展现出优势。实验表明，Bernini 在 Bernini-Bench 上视频一致性显著优于 Kling O3，与 Wan2.7 持平，但在 VBench 生成任务上未超越 SOTA。其边界在于编辑评估依赖自设基准，缺乏外部可比性，且代码未开源。当支持集增大到 5-shot 时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.22344)