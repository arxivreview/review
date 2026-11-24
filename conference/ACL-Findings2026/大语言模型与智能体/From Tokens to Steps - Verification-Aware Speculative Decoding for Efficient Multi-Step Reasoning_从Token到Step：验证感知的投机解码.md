# ACL-Findings2026最新论文 ｜From Tokens to Steps: Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning ｜从Token到Step：验证感知的投机解码

作者：Kiran Purohit、Ramasuri Narayanam、Soumyabrata Pal

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_93a681b62387)

> 多步推理任务中，标准投机解码（Speculative Decoding, SD）的Token级验证常因拒绝语义正确但概率低的草稿Token而引发错误级联，导致加速失效。现有方案依赖外部奖励模型（Process Reward Model, PRM）进行步骤级验证，但引入了高延迟与任务泛化性差的问题。SPECGUARD通过集成模型内部的注意力接地与对数概率信号，在步骤级执行自适应验证，无需外部验证器。该方法在推理基准上提升了准确率并降低了延迟，但其对标准SD无损性假设的偏离及在通用文本生成中的适用性仍存疑。

## 研究背景

自回归解码的串行特性受限于内存带宽，SD通过草稿模型并行生成候选Token、目标模型单次验证来打破这一瓶颈。然而，SD的严格无偏性要求目标模型必须拒绝所有概率不匹配的草稿Token，这在多步推理中表现为“语义正确但概率低”的Token被频繁拒绝，导致计算浪费与错误传播。为缓解此问题，奖励引导投机解码（Reward-Guided Speculative Decoding, RSD）引入外部PRM在步骤级评估草稿质量，但PRM的引入增加了推理延迟，且其训练数据通常局限于特定任务，难以泛化至多样化的推理场景。

SPECGUARD针对RSD的外部依赖瓶颈，提出利用模型内部信号替代外部验证器。其核心假设是：正确生成的推理步骤应表现出对输入上下文的高注意力接地（Grounding）以及较高的条件对数概率。通过结合这两个轻量级信号，SPECGUARD在保持草稿-验证范式的基础上，实现了步骤级的自适应计算分配，旨在解决多步推理中错误级联与验证成本过高的矛盾。

## 核心方法

### 方法参照系

标准SD流程中，草稿模型生成Token序列，目标模型通过拒绝采样验证。SPECGUARD将验证粒度从Token扩展至推理步骤（Step），并引入自一致性选择器（Self-Consistency Selector）从多个草稿候选中筛选最优步骤，随后通过集成验证器决定接受或调用目标模型重算。

### 注意力接地验证（ABGV）

ABGV利用模型内部注意力矩阵评估生成步骤是否忠实于输入上下文。设计动机在于解决标准SD中语义正确但概率低的Token被误拒的问题，通过检查Token与输入的对齐程度来识别“无接地”的幻觉步骤。ABGV采用注意力滚动（Attention Rollout）机制计算累积归因，并取步骤内最小Token接地分数作为严格判据：

$$ G_{min-step} = \min_{t} G(y_{i,t}) $$

其中 $G(y_{i,t})$ 为Token $y_{i,t}$ 对输入Token集合 $I$ 的注意力权重和。该公式确保步骤中每个Token均充分接地，防止个别无接地Token被平均效应掩盖。

### 集成验证与自一致性选择

集成验证器结合ABGV与对数概率验证（LPBV），通过加权聚合决定接受与否。LPBV取步骤内最小对数概率 $L_{min-step} = \min_{t} L(y_{i,t})$ 以捕捉Token级置信度。两个信号经Min-Max归一化后，计算集成分数 $r_i = \beta \tilde{\ell}_i + (1-\beta) \tilde{g}_i$。若 $r_i \ge \tau$，则接受草稿步骤；否则调用目标模型。自一致性选择器通过Sentence Transformer编码候选步骤，计算相似度矩阵的行Softmax，选取对角线分数最小（即与其他候选最一致）的步骤作为代表，降低采样方差。

## 实验评估

实验在MATH500、GSM8K、Gaokao 2023 En和OlympiadBench上进行，采用精确匹配（EM）指标。基线包括Target-only、Draft-only（含Majority Voting/Best-of-N）、标准SD及RSD。SPECGUARD在Qwen2.5-Math-Instruct（7B Target, 1.5B Draft）上表现最佳，GSM8K准确率达95.8%，高于SD（94.2%）和RSD（94.4%）。在Llama-3.1-Instruct（8B Target, 1B Draft）上，SPECGUARD在MATH500上达51.6%，显著优于SD（47.0%）和RSD（50.0%）。

| 模型配置 | 方法 | MATH500 | GSM8K | Gaokao 2023 En | Olympiad Bench Math |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Qwen2.5-Math (7B/1.5B) | SD | 82.4 | 94.2 | 66.3 | 39.4 |
| Qwen2.5-Math (7B/1.5B) | RSD | 82.4 | 94.4 | 68.5 | 39.6 |
| Qwen2.5-Math (7B/1.5B) | SPECGUARD | 85.4 | 95.8 | 69.4 | 41.2 |
| Llama-3.1 (8B/1B) | SD | 47.0 | 83.4 | 40.1 | 16.1 |
| Llama-3.1 (8B/1B) | RSD | 50.0 | 83.9 | 41.8 | 15.7 |
| Llama-3.1 (8B/1B) | SPECGUARD | 51.6 | 85.1 | 43.9 | 17.2 |

消融实验显示，SPECGUARD GREEDY（无自一致性选择器）在Qwen2.5-Math上GSM8K达95.6%，略低于完整版本的95.8%，表明自一致性选择器贡献有限但稳定。在Llama-3.1上，SPECGUARD GREEDY的MATH500为50.0%，完整版本为51.6%，显示自一致性在较弱草稿模型上收益更明显。

评估边界方面，论文未报告加速比（Speedup Ratio），仅声称延迟降低约11%，缺乏与主流SD方法（如EAGLE）在吞吐量上的直接对比。代码未公开，超参数（如 $\beta$, $\tau$）未详细列出，可复现性受限。此外，实验仅覆盖数学推理任务，未验证在通用文本生成或代码生成中的效果。

## 关联研究分析

从问题动机看，SPECGUARD与RSD均针对多步推理中的错误级联，但RSD依赖外部PRM，而SPECGUARD利用内部信号。这一差异源于SPECGUARD假设模型内部注意力与概率信号足以捕捉步骤正确性，而RSD认为外部监督更可靠。SPECGUARD在Llama-3.1上优于RSD，表明内部信号在特定模型架构下可能更鲁棒，但其泛化性未得到充分验证。

从方法设计看，SPECGUARD的Step级验证偏离了标准SD的Token级无损性保证。标准SD通过拒绝采样确保输出分布与目标模型一致，而SPECGUARD通过集成分数阈值接受草稿步骤，可能引入分布偏差。这与EAGLE等特征对齐方法不同，后者通过训练草稿模型对齐目标模型特征以保持无损性。SPECGUARD的“松弛验证”策略在推理任务中提升了准确率，但在通用场景中是否破坏无损性，论文未提供证据。

## 总结

SPECGUARD旨在解决多步推理中SD因Token级验证导致的错误级联与效率低下问题。其切入点在于利用模型内部的注意力接地与对数概率信号替代外部PRM，实现步骤级自适应验证。实验表明，该方法在Qwen2.5-Math上GSM8K准确率达95.8%，延迟降低约11%，优于SD和RSD。然而，论文未报告加速比，且实验局限于数学推理任务，未验证其在通用文本生成中的无损性。当草稿模型与目标模型分布差异较大时，内部信号是否仍能可靠区分正确与错误步骤，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_93a681b62387)