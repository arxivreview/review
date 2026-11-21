# HuggingFace最新推荐论文 ｜Lexical Reference Frames: Interpreting LM Residual Streams in Native Semantics ｜词汇参考系：在原生语义下解释语言模型残差流

研究机构：澳大利亚莫纳什大学

作者：Jian Gu、Hongyu Zhang、Chunyang Chen 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.22169)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.22169)

> 导读 语言模型中间层隐藏状态缺乏原生语义定义，导致现有解释工具在中间层失效。传统Lens方法使用固定线性映射，忽略了上下文对状态读取的影响；点云统计仅描述分布而非模型使用方式。本文提出Lexical Reference Frames，通过模型自身剩余层和有限轮次注意力近似原生参考系，实现自适应非线性读取。该方法在SmolLM3-3B和OLMo3-7B上显著优于Logit Lens和Jacobian Lens，为中间层解释提供了新范式。其闭式计算特性提升了效率，但在长上下文依赖捕捉上仍存疑。

## 研究背景

当研究者试图理解语言模型中间层隐藏状态时，面临一个根本困境：模型仅在输入嵌入和输出解嵌入处定义了词汇语义，中间状态本身不具备明确的语义标签。为了读取这些状态，Logit Lens直接应用输出帧，Tuned Lens学习每层一个仿射映射，Jacobian Lens平均剩余层的雅可比矩阵。这些方法共同假设每层存在一个固定的线性读取方向，忽略了剩余层通过注意力机制对前文上下文的依赖。这种固定映射导致在中间层，读取方向与模型实际使用的方向偏差高达75度以上，无法忠实反映模型决策。

另一类方法将每层状态视为点云，分析其秩、内在维度或各向异性。这类统计描述状态分布，而非模型如何使用状态。两个在点云中接近的状态可能导致完全不同的预测，反之亦然。因此，现有方法要么忽略上下文导致读取偏差，要么忽略模型使用方式导致解释无关。本文指出，每个隐藏状态都有一个由剩余层诱导的“原生参考系”，该参考系随上下文自适应变化。任何每层仅有一个映射的Lens都无法跨越不同上下文跟随这一参考系。

## 核心方法

### 方法参照系：从固定Lens到自适应参考系

本文问题属于机制可解释性中的中间层状态解释。通用流程是寻找一个映射将隐藏状态投影到词汇空间。Logit Lens使用输出解嵌入矩阵，Jacobian Lens使用剩余层雅可比矩阵的平均值。本文的关键差异在于：原生参考系是状态特定的（state-specific）且上下文敏感的（context-sensitive），而非每层固定的。

### 原生参考系与词汇读出

原生参考系由剩余层对状态的读取方式定义。对于层 $\ell$ 位置 $t$ 的状态 $x_\ell(t)$，其词汇读出方向 $b_\ell(v)$ 是标签 $v$ 的居中logit对状态的梯度：

$$ b_\ell(v) = \frac{\partial c_v}{\partial x_\ell(t)} = J_\ell^\top (w_v - \bar{w}) $$

其中 $J_\ell$ 是从 $x_\ell(t)$ 到最终归一化状态的雅可比矩阵，$w_v$ 是解嵌入行，$\bar{w}$ 是平均解嵌入行。该公式表明，读取方向取决于剩余层的具体计算路径，包括注意力机制对前文的依赖。因此，不同上下文下同一层的读取方向不同。词汇基 $s_\ell(v) = J_\ell^+ s_v$ 则是使输出沿 $s_v$ 移动所需的状态移动方向。设计动机在于：固定Lens无法捕捉这种上下文依赖性，导致中间层解释失效。

## 实验评估

实验在SmolLM3-3B和OLMo3-7B上进行，对比Logit Lens、Jacobian Lens、监督探针及点云统计。基线覆盖全面，但缺失Integrated Gradients等归因方法，不过通过Activation Patching进行了因果验证。

| 方法 | SmolLM3-3B KL (nats) | SmolLM3-3B Top-1 | OLMo3-7B KL (nats) | OLMo3-7B Top-1 |
| :--- | :--- | :--- | :--- | :--- |
| Logit lens | 29.06 | 0.04 | 5.66 | 0.15 |
| Jacobian lens | 7.51 | 0.14 | 6.19 | 0.13 |
| LEXFRAME[0] | 0.87 | 0.64 | 0.93 | 0.64 |
| LEXFRAME[1] | 0.16 | 0.86 | 0.15 | 0.86 |
| LEXFRAME[2] | 0.06 | 0.92 | 0.05 | 0.93 |

LEXFRAME[1] 在中间层将KL散度从Jacobian Lens的7.51降至0.16，Top-1一致率从0.14提升至0.86。消融显示，从LEXFRAME[0]到LEXFRAME[1]的一轮注意力闭合了大部分差距，而LEXFRAME[2] 进一步降低KL至0.06。点云统计与状态替换效应的相关性极低， lexical readouts 几乎完全位于状态变化方向之外。

评估边界方面，实验仅覆盖两个模型家族，未测试更大规模模型或长上下文场景。代码未开源，但方法基于闭式计算，复现性较高。

## 关联研究分析

从问题动机看，本文与Jacobian Lens（Gurnee et al., 2026）直接相关。Jacobian Lens通过平均雅可比矩阵提供每层一个固定方向，本文指出这种平均化忽略了上下文特异性，导致在中间层偏差巨大。LEXFRAME通过保留注意力机制，实现了状态特定的自适应读取。

从方法设计看，本文与Activation Patching（Conmy et al., 2023）形成互补。Activation Patching通过因果干预测量组件贡献，计算成本高；LEXFRAME通过系数差异近似归因，相关性达0.88，接近Patching的0.90，但无需迭代干预。LEXFRAME的归因更忠实于线性归因（0.62），但计算效率更高。

## 总结

本文针对语言模型中间层状态缺乏原生语义定义的问题，提出Lexical Reference Frames，通过模型自身剩余层和有限轮次注意力近似原生参考系。该方法在SmolLM3-3B和OLMo3-7B上，LEXFRAME[1]将KL散度降至0.16 nats，Top-1一致率达0.86，显著优于固定Lens。其边界在于仅测试了中等规模模型，且LEXFRAME[1]仅保留一轮注意力，当上下文依赖超过一轮注意力传播时，其忠实性是否衰减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.22169)