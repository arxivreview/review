# ACL2026最新论文 ｜When Benchmarks Leak: Inference-Time Decontamination for LLMs ｜推理时嵌入扰动去污

研究机构：日本东京科学大学、日本理化学研究所

作者：Jianzhe Chai、Yu Zhe、Jun Sakuma

论文原文见 [arXiv](https://arxiv.org/abs/2601.19334)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.19334)

> 基准测试集污染导致大语言模型（LLM）评估分数虚高，现有“检测-过滤”策略因检测器误报率无法消除残留污染，且过滤会破坏基准可比性。本文切入点在于不修改基准与模型权重，而是在推理阶段通过输入嵌入空间的有界扰动抑制记忆捷径。DeconIEP 训练一个轻量生成器，利用参考模型引导扰动方向，在恢复干净性能的同时最小化良性效用下降。该方法在白盒场景下实现了去污效率与性能保持的平衡，但其对参考模型依赖及闭源模型适用性仍存疑。

## 研究背景

当 LLM 在预训练或微调阶段接触到基准测试样本时，模型可能通过记忆而非泛化获得高分，这种现象称为数据污染（Data Contamination）。污染不仅包括精确匹配，还涵盖语义改写（Semantic-level Contamination）和领域级分布重叠（Domain-level Contamination），使得传统的 n-gram 匹配失效。为应对这一问题，研究范式从静态检测转向动态评估与推理时干预，其中推理时去污（Inference-time Decontamination）旨在不改变基准集的前提下，通过干预模型内部状态恢复真实能力评估。

主流去污路线分为黑盒与白盒两类。黑盒方法如 TED 和 ITD 通过分布校准或提示重写干预，但计算开销大且可能改变任务语义；白盒方法如 Shortcut Neuron 和 Short-circuiting 直接修补激活或注意力，虽去污效率高，但往往导致未污染样本的性能显著下降（Benign Utility Drop, BUD）。现有方法面临的核心矛盾是：强干预能消除记忆，却损害正常推理；弱干预保真，却残留污染。DeconIEP 针对这一权衡，提出在输入嵌入层施加有界扰动，利用参考模型作为行为锚点，实现精细化的去污控制。

## 核心方法

### 方法参照系

推理时去污的标准流程是在模型推理阶段引入干预算子 $\mathcal{M}$，将污染模型 $f_{con}$ 映射为缓解后的预测器 $\mathcal{M}(f_{con})$，目标是使 $\text{Perf}(\mathcal{M}(f_{con}), D_{test}) \approx \text{Perf}(f_{clean}, D_{test})$。与直接修改权重或过滤样本不同，本文保持提示词不变，仅在输入嵌入空间添加扰动 $\delta(x)$，确保基准项的语义与难度不变。

### KL 散度代理目标

直接最小化性能差距 $\Delta_{perf}$ 不可行，因为准确率等指标离散且不可微。本文采用分布级代理目标，利用 KL 散度上界性能差距。对于输入 $x$，设 $p_{con}(\cdot|x)$ 和 $p_{clean}(\cdot|x)$ 分别为污染与干净模型的输出分布，目标是最小化两者的 KL 散度：

$$ \mathcal{L}_{KL} = D_{KL}(p_{con}(\cdot|x) \| p_{clean}(\cdot|x)) $$

该公式的物理含义是：通过调整污染模型的输出分布，使其逼近干净模型的行为分布，从而间接消除记忆导致的概率质量偏移。由于 $f_{clean}$ 通常不可用，本文使用相对低污染的参考模型 $f_{ref}$ 作为代理，训练生成器 $G_\theta$ 以摊销逐样本优化。

### 嵌入空间有界扰动

生成器 $G_\theta$ 将输入嵌入 $e(x)$ 映射为原始扰动，并通过缩放 tanh 函数保证扰动范数有界：

$$ \delta(x) = \zeta \cdot \tanh(G_\theta(e(x))) $$

其中 $\zeta$ 为扰动预算，确保 $\|\delta(x)\|_\infty \le \zeta$。这一设计动机在于：$\ell_\infty$ 球约束使扰动嵌入保持在原始嵌入的局部邻域内，旨在破坏记忆的表面模式，同时保留底层语义。生成器通过复合 KL+CE 目标训练，KL 项优化分布对齐，CE 项稳定训练并防止退化。相比深层激活修补，嵌入层扰动更温和，避免了通用计算通路的干扰，从而降低 BUD。

## 实验评估

实验在 MMLU 和 TruthfulQA 上进行，模拟精确、语义、领域三级污染，对比 TED、ITD、Shortcut Neuron 和 Short-circuiting。基线覆盖了黑盒与白盒主要路线，但缺失 Min-K% Prob 等纯检测基线，因任务侧重去污而非检测。

| 模型 | 方法 | TruthfulQA Exact RC↓ | MMLU Exact RC↓ | BUD (TruthfulQA)↓ |
|---|---|---|---|---|
| Mistral | DeconIEP | 0.011 | 0.007 | 0.019 |
| Mistral | Shortcut Neuron | 0.167 | 0.071 | 0.129 |
| Qwen2.5 | DeconIEP | 0.027 | 0.007 | 0.009 |
| Qwen2.5 | Short Circuit | 0.033 | 0.028 | 0.172 |

DeconIEP 在多数设置下取得最低或接近最低的 RC，且 BUD 显著低于白盒基线。例如，在 Mistral 上，DeconIEP 的 BUD 为 0.019，而 Shortcut Neuron 为 0.129，表明嵌入扰动在保持良性效用方面具有优势。

| $\zeta$ | TruthfulQA RC↓ | TruthfulQA BUD↓ | MMLU RC↓ | MMLU BUD↓ |
|---|---|---|---|---|
| 1e-5 | 0.512 | 0.000 | 0.344 | 0.000 |
| 1e-3 | 0.062 | 0.038 | 0.165 | 0.041 |
| 1e-2 | 0.022 | 0.062 | 0.032 | 0.102 |

消融实验显示，$\zeta$ 作为控制旋钮，RC 与 BUD 呈单调权衡关系。随着 $\zeta$ 从 $10^{-5}$ 增至 $10^{-2}$，RC 显著下降，但 BUD 上升。这表明去污强度与性能保持之间存在明确的 trade-off，实际应用中需根据容忍度选择 $\zeta$。

评估边界方面，论文未报告置信区间，且仅在 Qwen2.5 系列上验证了规模泛化性。代码未公开，超参数（如 $\lambda_{KL}$）未在正文详细列出，可复现性受限。

## 关联研究分析

从方法设计看，DeconIEP 与 Shortcut Neuron 同属白盒干预，但干预点从深层激活前移至输入嵌入。Shortcut Neuron 通过修补特定神经元消除记忆，但易误伤通用计算通路，导致高 BUD；DeconIEP 通过有界扰动在嵌入层“软化”记忆信号，保留了更多通用特征，从而降低 BUD。这一差异源于对记忆机制的不同假设：前者认为记忆集中于特定神经元，后者认为记忆表现为输入-输出映射的局部偏移。

从问题动机看，DeconIEP 与 LNE-Blocking 均关注推理时去污，但 LNE-Blocking 基于长度归一化熵动态调整解码策略，属于黑盒方法；DeconIEP 依赖参考模型引导，属于白盒方法。LNE-Blocking 无需参考模型，适用于闭源 API，但去污效率受限于解码参数调整；DeconIEP 去污效率更高，但依赖参考模型，限制了其在无锚点场景的应用。参考模型的存在是否必要，以及无参考模型时的自适应去污机制，是两者路线分歧的核心。

## 总结

DeconIEP 解决了推理时去污中“去污效率”与“良性效用保持”的矛盾，通过嵌入空间有界扰动和参考模型引导，实现了低 RC 与低 BUD 的平衡。实验表明，在 Mistral 和 Qwen2.5 上，DeconIEP 的 BUD 低于 0.03，显著优于 Shortcut Neuron 等基线。然而，该方法依赖参考模型，且仅在白盒场景下有效，对闭源模型不适用。当参考模型本身存在中度污染时，去污效果是否仍稳健，论文虽提供了初步证据，但未给出严格的理论保证。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.19334)