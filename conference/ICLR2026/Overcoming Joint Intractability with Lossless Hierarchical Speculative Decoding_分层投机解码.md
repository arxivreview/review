# ICLR2026最新论文 ｜Overcoming Joint Intractability with Lossless Hierarchical Speculative Decoding ｜分层投机解码

研究机构：美国华盛顿大学

作者：Yuxuan Zhou、Fei Huang、Heng Li 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.05724)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05724)

> 投机解码（Speculative Decoding, SD）旨在通过草稿-验证范式加速大语言模型（LLM）推理，但验证阶段的“联合不可行性”限制了接受率上限。现有无损验证方法如块级验证（Blockwise Verification）机制不透明且难以扩展至多草稿场景。本文提出分层投机解码（Hierarchical Speculative Decoding, HSD），通过分层分支重采样策略在保持严格无损性的同时最大化期望接受 token 数。该方法在 Qwen2.5 和 Llama-3.1 系列模型上实现了平均 6.7% 的解码速度提升，并与 EAGLE-3 集成后获得 12.4% 的加速，但其理论优势在极端分布偏移下的鲁棒性尚待验证。

## 研究背景

自回归解码中，目标模型 $p$ 与草稿模型 $q$ 的分布差异导致验证阶段需执行拒绝采样以维持无损性。标准 Token 级验证仅处理单 token 概率，当草稿序列长度增加时，联合概率 $p(\mathbf{X}_{1:\gamma})$ 的计算复杂度呈指数级增长，形成“联合不可行性”瓶颈。这一瓶颈使得序列级验证无法直接复用 Token 级重采样策略，因为后者依赖全路径联合概率来正确恢复目标分布，而自回归模型无法高效计算该值。

早期研究聚焦于草稿模型优化以提升接受率，但验证阶段的计算开销逐渐成为主要限制。块级验证（Sun et al., 2024）证明了序列级验证的无损性，但其机制缺乏解释性，且难以与多草稿（Multi-draft）框架兼容；其他方法如 MTAD（Qin et al., 2025）采用有损阈值，牺牲了分布保真度。本文切入点在于解决联合不可行性下的无损验证问题，通过局部分支重采样实现全局分布恢复，同时保持与现有 SD 框架的正交性。

## 核心方法

### 方法参照系

标准 Token 级 SD 通过独立验证每个 token 并执行重采样来恢复目标分布，其核心是散度对称性保证的局部无损性。本文问题与该通用流程的关键差异在于：序列级验证需处理分支间的概率质量转移，而 Token 级方法无法捕捉这种层级依赖关系，导致在长草稿序列中接受率次优。

### 分支散度与不对称性

Token 级验证失效于无法量化分支内局部概率缺失。本文定义分支散度 $D_{\text{Branch}}(p, q | \mathbf{X}_{1:t-1})$ 来度量草稿 $q$ 相对于目标 $p$ 在分支 $\text{Branch}(\mathbf{X}_{1:t-1})$ 内的缺失质量，并引入分支不对称性 $\Delta_{\text{Branch}}$ 来区分可补偿的缺失与不可补偿的过剩。该设计解决了块级验证中“部分信息受限”的问题，通过量化局部失衡为分层重采样提供理论依据。

$$
\Delta_{\text{Branch}}(\mathbf{X}_{1:t-1}) = D_{\text{Branch}}(q, p | \mathbf{X}_{1:t-1}) - D_{\text{Branch}}(p, q | \mathbf{X}_{1:t-1})
$$

该公式表明，当 $\Delta_{\text{Branch}} > 0$ 时，分支内存在无法局部补偿的缺失，需依赖更高层级的概率质量转移。

### 封顶分支重采样

Naive HSD 需对拒绝位置后的所有 token 执行重采样，导致额外目标模型调用。本文引入最大前缀比率索引 $m(\mathbf{X}_{1:t})$ 和封顶前缀比率 $r^*$，将重采样限制在可访问分支内，仅执行单次重采样。该设计消除了 Naive HSD 的计算开销，使剩余位置可直接由目标模型采样，与下一轮 SD 步骤对齐，从而在不增加额外前向传播的前提下实现无损性。

$$
r^*(\mathbf{X}_{1:t}) = \min\left(r(\mathbf{X}_{1:t}), \frac{1}{r(\mathbf{X}_{1:m(\mathbf{X}_{1:t})})}\right)
$$

该公式通过封顶机制将分支内过剩概率质量聚合至可访问层级，确保单次重采样即可恢复目标分布，避免了全路径联合概率的计算。

## 实验评估

实验采用 GPTQ-8bit 量化的 Qwen2.5 系列（0.5B 草稿，14B/32B/72B 目标）及 Llama-3.1 系列，在 GSM8K、HumanEval 和 CNN/DailyMail 上评估，基线为 Tokenwise 和 Blockwise 验证。主实验显示 HSD 在 Block Efficiency (BE) 和 Decoding Speed (DS) 上均优于基线，其中 HumanEval 32B 模型上 BE 提升 12.3%，DS 提升 11.4%。

| 数据集 | 模型规模 | 方法 | Block Efficiency (Token/Step) | Decoding Speed (Token/Second) |
| :--- | :--- | :--- | :--- | :--- |
| GSM8K | 72B | Tokenwise | 6.44 | 31.49 |
| GSM8K | 72B | HSD (Ours) | 6.65 (+3.3%) | 32.52 (+3.3%) |
| HumanEval | 32B | Tokenwise | 5.23 | 45.68 |
| HumanEval | 32B | HSD (Ours) | 5.49 (+12.3%) | 50.88 (+11.4%) |
| CNN/DailyMail | 14B | Tokenwise | 2.39 | 37.28 |
| CNN/DailyMail | 14B | HSD (Ours) | 2.59 (+8.4%) | 39.96 (+7.2%) |

消融实验表明，HSD 在温度 $t \in \{0.6, 0.8, 1.0\}$ 和草稿长度 $\gamma \in \{5, 10, 15\}$ 下均稳定优于基线，其中 $\gamma=15$ 时 BE 达 7.88 tokens/step，DS 达 52.95 steps/second，较 Tokenwise 提升 3.58% 和 3.88%。多草稿设置下，HSD 在 CNN/DailyMail 上 BE 提升 11.1%，DS 提升 8.9%，验证了其兼容性。

评估边界方面，本文未报告置信区间，且主要使用 Block Efficiency 和 Decoding Speed 而非统一的 Speedup Ratio，导致与领域 SOTA（如 HASS、GRIFFIN）的数值不可直接比较。代码已开源，但超参数细节（如温度、草稿长度）仅在消融实验中部分披露，可复现性依赖附录中的实现细节。

## 关联研究分析

从问题动机看，HSD 与块级验证（Sun et al., 2024）均聚焦序列级无损验证，但块级验证的机制不透明且难以扩展至多草稿场景，而 HSD 通过分层重采样提供了可解释的概率质量转移路径。这一差异源于块级验证依赖全路径联合概率的近似，而 HSD 利用分支不对称性实现局部补偿，避免了联合概率的计算。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

从方法设计看，HSD 与 EAGLE-3（Li et al., 2024）的集成展示了验证策略与草稿模型的解耦性，但 EAGLE-3 使用 top-K 采样导致草稿概率均为 1，使验证方法退化为相同行为，观察到的 BE 提升可能受采样随机性影响。这一冲突暗示，当草稿模型分布高度确定时，验证策略的边际收益可能递减，但论文未深入分析此条件依赖关系。

## 总结

本文核心矛盾在于序列级验证的联合不可行性与无损性要求的冲突。现有方法如块级验证依赖全路径联合概率的近似，而 HSD 通过分层分支重采样利用分支不对称性实现局部补偿，避免了联合概率的计算。该方法在 Qwen2.5 和 Llama-3.1 系列上实现了平均 6.7% 的解码速度提升，并与 EAGLE-3 集成后获得 12.4% 的加速。本文边界在于未与当前 SOTA 端到端加速比进行直接对比，且未分析草稿模型分布高度确定时验证策略的边际收益。当草稿模型使用 top-K 采样导致概率分布退化时，HSD 的 BE 提升是否仍具统计显著性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05724)