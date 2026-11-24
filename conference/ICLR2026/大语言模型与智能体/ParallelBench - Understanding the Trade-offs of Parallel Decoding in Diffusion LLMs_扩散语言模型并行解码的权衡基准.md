# ICLR2026最新论文 ｜ParallelBench: Understanding the Trade-offs of Parallel Decoding in Diffusion LLMs ｜扩散语言模型并行解码的权衡基准

研究机构：微软研究院、韩国首尔大学

作者：Wonjun Kang、Kevin Galim、Seunghyuk Oh 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.04767)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.04767)

> 扩散语言模型（dLLMs）旨在通过并行解码打破自回归生成的顺序依赖，但其条件独立性假设导致在强令牌依赖任务中质量严重退化。现有研究多聚焦于标准基准上的加速比，忽视了并行解码在真实场景下的质量-速度权衡失效。本文通过信息论分析量化这一退化下界，并构建首个专门评估该权衡的基准 ParallelBench。该工作揭示了现有自适应解码策略的局限性，但未提供能动态感知依赖结构的新型解码算法。

## 研究背景

自回归大语言模型（LLMs）推理时受限于左到右顺序依赖，每个令牌生成需完整前向传播，导致延迟随生成长度线性增加。扩散语言模型（dLLMs）通过迭代去噪和双向注意力支持任意顺序的并行令牌更新，理论上可大幅加速推理。然而，dLLMs 在并行解码时假设同一时间步内的令牌相互独立，即 $P_\theta(y_i | X, S_{<t}) \cdot P_\theta(y_{i+1} | X, S_{<t})$，忽略了令牌间的联合约束。这种条件独立性假设使得模型可能生成如“New City”而非“New York”的无效组合，因为每个令牌是独立采样而非基于联合分布 $P_\theta(y_i, y_{i+1} | X)$ 采样。

dLLM 并行解码的核心矛盾在于速度-质量权衡。Fast-dLLM 等早期工作通过阈值解掩码和 KV 缓存复用实现了 2.5x-17x 的加速，但主要评估 GSM8K 和 HumanEval 等标准基准。这些基准中的任务（如数学推理、代码生成）通常具有局部依赖或可通过上下文充分约束，未能暴露并行解码在强全局依赖任务上的脆弱性。Wu et al. (2025) 虽指出条件独立性导致质量退化，但缺乏量化其严重程度的理论框架和针对性基准。本文切入点在于：现有评估体系无法区分“并行解码本身的质量损失”与“模型容量不足”，且缺乏能系统性评估不同解掩码策略在依赖结构变化下表现的基准。

## 核心方法

### 方法参照系

dLLM 并行解码的标准流程是将目标序列 $Y$ 划分为 $T$ 个不相交集合 $S_1 \cup \dots \cup S_T$，每步并行生成 $S_t$ 中的令牌。解掩码策略决定划分方式：静态 Top-k 策略每步固定解掩 $k$ 个令牌，自适应阈值策略解掩置信度超过 $\gamma$ 的令牌。本文问题与该通用流程的关键差异在于：不优化特定策略的加速比，而是量化不同依赖结构下所有策略的质量下界，并构建能暴露这些下界的基准。

### 信息论下界与合成任务量化

设计动机：现有工作缺乏量化并行解码质量退化的理论指标，导致无法区分模型缺陷与算法固有局限。本文引入条件总相关 $C(Y|X)$ 作为并行解码难度的度量，定义为 $C(Y|X) = -H_{data}(Y|X) + \sum_{y_i \in Y} H_{data}(y_i|X)$。该公式衡量令牌间的依赖强度：$C(Y|X)=0$ 表示令牌独立，可无损并行；$C(Y|X)>0$ 表示存在依赖，并行解码必然引入分布误差。

对于 $T$ 步并行解码，最小可达 KL 散度下界为：

$$
\min_\theta D_{KL}(P_{data}(Y|X) \| P_\theta(Y|X)) \ge L_T = \sum_{i=1}^T \mathbb{E}_{S_{<i} \sim P_{data}} [C(S_i | X, S_{<i})]
$$

该公式表明，即使使用理想模型，$T$ 步并行解码的误差下界 $L_T$ 也随 $T$ 减小而单调增加。当 $T=1$（全并行）时，$L_1 = C(Y|X)$；当 $T=|Y|$（逐令牌）时，$L_{|Y|}=0$。

为验证该理论，本文设计四个合成列表操作任务，其 $C(Y|X)$ 可解析计算：

- **Copy & Replace Index**：$C(Y|X)=0$，令牌由输入唯一确定，可无损并行。

- **Replace Random**：$C(Y|X) = (n-1)[\log_2(n) - \log_2(n-1)]$，$\lim_{n\to\infty} C(Y|X) = \log_2(e) \approx 1.44$，依赖强度有界。

- **Shuffle**：$C(Y|X) = n\log_2(n) - \log_2(n!)$，$\lim_{n\to\infty} C(Y|X) = \infty$，依赖强度无界增长。

实验显示，Shuffle 任务在 $k=2$ 时准确率已降至 0%，而 Replace Random 在 $k=2$ 时保持 50% 准确率，与理论预测一致。

### ParallelBench 基准构建

设计动机：合成任务虽可解析，但无法代表真实文本的依赖结构。本文构建 ParallelBench，包含 17 个真实任务，覆盖三个类别：Waiting Line（10 个，如 Reverse、Shuffle）、Text Writing（5 个，如 Paraphrasing、W2S）、Puzzles（2 个，如 Sudoku、Latin Square）。

基准设计原则：任务对人和自回归 LLM 简单，但对 dLLM 并行解码极具挑战。例如，Waiting Line 中的 Shuffle 任务要求打乱列表项，自回归 LLM 准确率接近 100%，但 dLLM 在 $k=4$ 时准确率降至 0%。Text Writing 中的 W2S（Word-to-Sentence）任务从稀疏单词约束生成完整句子，依赖强度高于 Paraphrasing，导致并行解码退化更陡峭。

ParallelBench 的评估指标包括准确率、语法分数和联合指标，覆盖从易并行（$C(Y|X)=0$）到难并行（$C(Y|X)>0$）的完整难度谱系。该基准使研究者能系统性评估解掩码策略在不同依赖结构下的表现，而非仅关注单一基准上的加速比。

## 实验评估

实验设置：使用 LLaDA 1.5 8B、Dream 7B、Mercury 等 dLLM 及 Llama 3.1 8B、Qwen2.5 7B 等自回归 LLM。解掩码策略包括 Top-k（Random、Confidence、Left-to-Right、Margin、Entropy）和 Threshold（Confidence，$\gamma \in \{0.5, 0.6, \dots, 1.0\}$）。评估协议为 5-shot 或 0-shot，未报告置信区间。

| 任务 | 模型 | 解掩码策略 | 准确率 (%) |
| --- | --- | --- | --- |
| Shuffle | LLaDA 1.5 | Random Top-k, k=2 | 0 |
| Replace Random | LLaDA 1.5 | Random Top-k, k=2 | 50 |
| Copy | LLaDA 1.5 | Random Top-k, k=32 | 100 |
| Reverse | Mercury | Random Top-k, k=20 | 100 |
| Shuffle | Mercury | Random Top-k, k=20 | 0 |

核心发现：dLLM 在强依赖任务上质量退化严重。Shuffle 任务中，LLaDA 1.5 在 $k=2$ 时准确率降至 0%，而自回归 LLM 保持 100%。Mercury 在 Reverse 任务上保持 100% 准确率，但在 Shuffle 任务上 $k=20$ 时准确率降至 0%，表明其无法自适应调整并行度。

消融分析显示，解掩码策略的选择对结果影响显著。在 $C(Y|X)=0$ 的任务（如 Copy、Replace Index）上，Confidence Top-k 优于 Random Top-k，因为模型不完美性限制准确率，优先解掩高置信度令牌有益。在 $C(Y|X)>0$ 的任务（如 Replace Random、Shuffle）上，Random Top-k 反而优于 Confidence Top-k，因为依赖结构使得高置信度令牌可能相互冲突。Threshold 策略在保守阈值（$\gamma \ge 0.8$）下优于 Top-k，但在激进阈值（$\gamma < 0.6$）下因不可预测的解掩峰值而快速退化。

评估边界：ParallelBench 任务虽覆盖多种依赖结构，但均为结构化任务（列表操作、句子生成、谜题），未涵盖开放式对话或长文本摘要等更复杂的依赖模式。代码开源，但超参数（如 $\gamma$ 范围）需手动调整，缺乏自动调参机制。

## 关联研究分析

从问题动机看，本文与 Fast-dLLM 等加速导向工作形成互补。Fast-dLLM 通过阈值解掩码和 KV 缓存复用实现 2.5x 加速，但假设标准基准上的质量损失可接受。本文揭示，在强依赖任务上，即使使用 Fast-dLLM 的阈值策略，质量退化仍不可忽略。根源在于任务特性：GSM8K 等基准中的数学推理具有局部依赖，而 Shuffle 等任务具有全局依赖，导致条件独立性假设失效。Fast-dLLM 未探索依赖结构对加速效果的影响，本文则通过 $C(Y|X)$ 量化了这一影响。

从方法设计看，本文与 Speculative Decoding 形成对比。Speculative Decoding 通过草稿-验证机制保证无损加速，但依赖独立草稿模型，增加系统复杂度。本文指出，dLLM 并行解码的有损性源于条件独立性假设，而非模型容量不足。Speculative Decoding 的验证机制可视为一种“事后纠错”，而 dLLM 并行解码缺乏此类机制。本文未探索将验证机制引入 dLLM 的可能性，但 ParallelBench 为评估此类混合策略提供了基准。

## 总结

本文要解决的核心矛盾是 dLLM 并行解码的速度-质量权衡，现有方法在强依赖任务上质量退化严重但缺乏量化指标。本文抓住的切入点是条件总相关 $C(Y|X)$ 作为并行解码难度的理论下界，通过合成任务验证其有效性，并构建 ParallelBench 暴露现有策略的局限。本文证明了 Shuffle 任务在 $k=2$ 时准确率降至 0%，而自回归 LLM 保持 100%，揭示了 dLLM 并行解码的固有局限。本文的边界在于：ParallelBench 任务均为结构化任务，未涵盖开放式生成；解掩码策略需手动调参，缺乏自适应机制。当依赖结构从全局依赖（如 Shuffle）过渡到局部依赖（如 Paraphrasing）时，现有阈值策略的失效边界在哪里，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.04767)