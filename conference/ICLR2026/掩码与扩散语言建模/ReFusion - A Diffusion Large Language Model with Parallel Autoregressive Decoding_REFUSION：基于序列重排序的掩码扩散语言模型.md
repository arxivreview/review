# ICLR2026最新论文 ｜ReFusion: A Diffusion Large Language Model with Parallel Autoregressive Decoding ｜REFUSION：基于序列重排序的掩码扩散语言模型

研究机构：中国人民大学

作者：Jia-Nan Li、Jian Guan、Wei Wu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.13586)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.13586)

> 掩码扩散语言模型（Masked Diffusion Language Model, MDLM）试图通过并行去噪突破自回归模型串行解码的效率瓶颈，但双向注意力导致的关键值（Key-Value, KV）缓存失效与并行采样中的条件独立性失效，使其在效率与连贯性上均落后于自回归模型（Autoregressive Model, ARM）。REFUSION 通过引入槽位（Slot）级序列重排序，将并行解码粒度从 token 提升至 slot，在保持全局生成灵活性的同时实现了全量 KV 缓存复用，并将学习复杂度从指数级 token 组合空间降至可管理的 slot 排列空间。该方法在七个基准上确立了 MDLM 的新状态-of-the-art，但其在长文本一致性上的表现仍存疑。

## 研究背景

自回归模型依赖严格的从左到右因果注意力，使得已生成的 token 可以缓存其 KV 状态，从而将推理延迟与序列长度解耦。然而，这种串行机制限制了吞吐量。MDLM 通过迭代去噪允许并行生成多个 token，理论上能发现比固定左到右更优的生成顺序。但 MDLM 通常采用双向注意力以利用全局上下文，这破坏了 KV 缓存的因果结构，导致每步解码需重新计算全序列的 KV 状态，抵消了并行带来的效率增益。

现有高效 MDLM 方案主要分为三类：近似复用 KV 状态、混合双向与因果注意力、以及纯因果注意力重排序。其中，纯因果注意力方案（如 Eso-LMs）虽能实现精确 KV 缓存，但在 token 级重排序引入了不可解的训练目标，导致性能显著下降。同时，MDLM 并行解码多个高边际概率 token 时，邻近 token 间的条件独立性假设频繁失效，产生如“right once”这类语义不连贯的输出。REFUSION 的切入点在于将重排序与并行解码的粒度从 token 提升至 slot，通过槽内自回归捕捉局部强依赖，槽间扩散选择保留全局灵活性，从而同时解决缓存失效与学习复杂度两大瓶颈。

## 核心方法

### 方法参照系

标准 MDLM 在推理时通过置信度阈值并行解码多个 token，训练时仅对掩码位置计算去噪损失。其关键差异在于：REFUSION 将序列划分为固定长度的连续子序列（slot），并采用“槽间并行选择、槽内自回归填充”的混合解码策略，而非 token 级并行。

### 序列重排序与全量 KV 缓存复用

REFUSION 采用标准因果注意力框架，但在每步解码后将新解码的 slot 移至剩余掩码 slot 之前，保持其内部相对顺序。这种布局使得所有已解码 token 在序列前端连续排列，从而支持全量 KV 缓存复用。为解决重排序导致的位置 ID 偏移问题，注意力计算使用 token 的原始索引作为位置 ID。以旋转位置嵌入（Rotary Position Embedding, RoPE）为例，查询 $\mathbf{q}_m$ 与键 $\mathbf{k}_n$ 的注意力计算中，相对距离项 $\mathbf{R}_{n-m}$ 保持不变，确保注意力分数对 token 重排序不变。这一设计解决了纯因果注意力方案中 token 级重排序导致的训练目标不可解问题，同时保留了 MDLM 的全局生成灵活性。

### 槽位划分与混合训练目标

为降低学习复杂度，REFUSION 将序列划分为长度为 $k$ 的连续 slot。槽间采用扩散式选择，槽内采用自回归填充，以捕捉邻近 token 间的强依赖。训练时，响应序列被随机掩码若干 slot，未掩码 slot 被随机排列，最终输入为排列后的干净 slot 拼接掩码 slot。混合训练目标包括干净 slot 上的自回归损失 $\mathcal{L}_{ARM}$ 和掩码 slot 上的去噪损失 $\mathcal{L}_{MDM}$：

$$ \mathcal{L} = \mathcal{L}_{ARM} + \lambda \mathcal{L}_{MDM} $$

其中 $\mathcal{L}_{ARM}$ 监督干净 slot 的下一个 token 预测，$\mathcal{L}_{MDM}$ 监督掩码 slot 的原始 token 重建。该目标使模型从每个 token 中学习，提升了数据效率，解决了传统 MDLM 中干净 token 仅提供上下文而无直接监督的问题。

## 实验评估

REFUSION 基于 Qwen3-8B 初始化，在 3.7M 样本（约 1.22B token）上微调 4 个 epoch。基线覆盖 LLaDA、Dream 及其加速变体（Fast-dLLM, D2F），以及 ARM 基线 Qwen3-8B 和 Llama-3-8B-Instruct。未对比最新 RL 对齐方法（如 SPG, TraceRL），限制了与顶级推理模型的直接比较。

| 模型 | MMLU-Pro | GSM8K | HumanEval | MBPP | Avg. TPS |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Qwen3-8B | 67.25 | 81.96 | 87.80 | 63.80 | 32.42 |
| LLaDA-8B-Instruct | 35.80 | 76.35 | 45.12 | 25.60 | 12.41 |
| Dream-7B-Instruct | 40.05 | 76.42 | 56.71 | 50.40 | 8.84 |
| REFUSION | 45.94 | 84.91 | 78.66 | 68.20 | 72.62 |

REFUSION 在 GSM8K 和 MBPP 上分别以 84.91 和 68.20 超越 Qwen3-8B 的 81.96 和 63.80，平均吞吐量 72.62 TPS 是 Qwen3-8B 的 2.33 倍。在 HumanEval 上，REFUSION 的 78.66 比次优 MDLM（Dream-7B-Instruct）高 21.95 个点。

消融实验显示，强制 REFUSION 采用左到右串行解码（ReFusion left-to-right）后，性能下降但吞吐量提升，验证了并行解码对性能的贡献。槽大小 $k$ 和阈值 $\tau_{slot}$、$\tau_{token}$ 的敏感性分析表明，$k=4$ 和 $\tau_{slot}=0.6$ 在性能与效率间取得最佳平衡。

评估边界方面，论文未报告长文本生成的一致性指标，且所有实验基于 8B 规模模型，未验证更大规模下的可扩展性。代码与模型权重已开源，但训练细节（如 $\lambda$ 的具体值）仅在附录中提供，复现需仔细核对超参数。

## 关联研究分析

从方法设计看，REFUSION 与 Block Diffusion 的核心差异在于并行/串行逻辑的逆转。Block Diffusion 采用块间串行、块内并行，牺牲全局灵活性以换取 KV 缓存；REFUSION 采用槽间并行、槽内串行，保留全局灵活性并实现全量 KV 缓存。这一差异源于 REFUSION 将 slot 视为“可重排序的单元”，而 Block Diffusion 将 block 视为“固定顺序的单元”。REFUSION 的槽内自回归是否完全消除了槽间并行带来的全局依赖缺失，论文未提供长文本一致性实验来验证。

从问题动机看，REFUSION 与 Eso-LMs 同属纯因果注意力路线，但 Eso-LMs 在 token 级重排序导致训练目标不可解，性能显著下降。REFUSION 通过将重排序粒度提升至 slot 级，并将槽内解码改为自回归，降低了学习复杂度。这一改进是否源于 slot 级排列空间比 token 级排列空间更易优化，还是源于槽内自回归本身缓解了条件独立性失效，论文未通过消融实验解耦这两者的贡献。

## 总结

REFUSION 解决了 MDLM 中 KV 缓存失效与并行解码不连贯的核心矛盾，通过槽位级序列重排序与混合训练目标，实现了全量 KV 缓存复用与可管理的学习复杂度。在七个基准上，REFUSION 以 84.91 的 GSM8K 准确率和 72.62 TPS 的平均吞吐量，同时超越了 MDLM 基线与 ARM 基线。其边界在于未验证长文本生成的一致性，且所有实验基于 8B 规模模型。当序列长度增加至数千 token 时，槽间并行生成的累积误差是否会显著影响最终输出的连贯性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.13586)