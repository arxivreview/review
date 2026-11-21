# ICLR2026最新论文 ｜LET S EXPLORE STEP BY STEP: GENERATING PROV - ABLE FORMAL STATEMENTS WITH DEDUCTIVE EX PLORATION ｜演绎探索：生成可证明的形式化数学陈述

研究机构：上海交通大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_34523096)

> 数学问题合成旨在解决大语言模型训练数据枯竭与评测污染问题，但现有方法陷入表达力、有效性与复杂性的三难困境。一次性生成或依赖外部证明器导致逻辑错误频发或难度受限，本文提出DExploration框架，通过逐步演绎探索替代一次性生成，在Lean 4环境中保证陈述的可证明性。该方法通过探索轨迹蒸馏解决数据稀缺问题，实现了难度与有效性的平衡，但其探索深度仍受限于现有定理库的复杂度边界。

## 研究背景

理解本文需厘清形式化验证与问题合成的关系。Lean 4基于Curry-Howard同构，将数学陈述视为类型，证明视为类型检查过程。传统问题合成依赖自然语言生成，缺乏机器可验证的逻辑闭环，导致生成问题常存在矛盾或无法证明。为突破此局限，研究者引入形式化环境，但面临“表达力-有效性-复杂性”三难：纯LLM方法表达力强但有效性低；领域特定方法有效但表达力受限；形式化方法兼顾前两者，却受限于外部证明器的能力上限，难以生成真正高难度问题。

数学问题合成是缓解AI数据瓶颈的关键路径。早期LLM-based方法如WizardMath和MetaMath通过提示工程扩展种子数据，但生成质量受限于LLM自身的逻辑能力，且无法保证有效性。Domain-specific方法如DyVal利用符号算法保证有效性，但局限于特定领域。Formal-based方法分为Autoformalizer-based和Conjecture-Prover两类：前者先生成非形式化问题再自动形式化，后者直接生成形式化陈述并调用证明器。然而，Autoformalizer的错误会破坏有效性，而Prover的能力上限直接限制了生成问题的复杂度。DExploration的切入点在于摒弃“一次性生成+外部验证”的范式，将问题合成重构为逐步探索过程，使证明生成内化为探索的一部分，从而突破复杂度上限。

## 核心方法

### 方法参照系

本文问题属于形式化数学问题合成，最接近的通用流程是Conjecture-Prover范式：LLM直接生成形式化陈述，外部Prover尝试证明。关键差异在于，DExploration将“生成陈述”与“生成证明”解耦为“探索过程”与“轨迹重构”，不再依赖外部Prover的采样成功率，而是通过探索过程中的每一步验证来保证最终陈述的可证明性。

### 演绎探索框架

DExploration将数学探索建模为确定性马尔可夫决策过程，状态 $S_t = (\Gamma_t, \Lambda_t)$ 包含引入上下文 $\Gamma_t$ 和推导上下文 $\Lambda_t$。动作空间包含三个原子操作：

$$
\text{Introduce}(v:T)(\Gamma, \Lambda) = (\Gamma \circ [(v:T)], \Lambda)
$$

该公式表示引入新变量或假设，不改变推导上下文。

$$
\text{Deduce}(h:H)(\Gamma, \Lambda) = (\Gamma, \Lambda \circ [(h:H)])
$$

该公式表示基于当前上下文推导新事实，需证明 $\Gamma \circ \Lambda \vdash H$。

$$
\text{Submit}(h:H)(\Gamma, \Lambda) = \Gamma \vdash H
$$

该公式表示提交事实作为结论，重构陈述并结束探索。设计动机在于解决Conjecture-Prover中“陈述生成与证明生成分离”导致的无效性：通过逐步验证，确保每一步推导都成立，最终提交的陈述必然可证明，无需外部Prover重试。

### 探索轨迹蒸馏

为训练DExplorer智能体，本文提出Exploratory Transformation，将现有定理-证明对转化为探索轨迹。首先，将证明重写为演绎风格，将非演绎战术包裹为 $s_{-2} := \text{have } h_U : U := \text{by } [s_i]_{k<i\le m}$ 和 $s_{-1} = \text{exact } h_U$。其次，构建依赖图，节点为变量和演绎步骤，边表示依赖关系。最后，按拓扑序遍历，优先选择推理深度 $d(s)$ 高且非引入步骤的节点，重组为探索轨迹。设计动机在于解决DExploration训练数据稀缺问题：通过从现有证明中蒸馏“探索直觉”，使智能体学习如何逐步推导而非一次性生成，从而在探索中自然发现高复杂度结论。

## 实验评估

实验在Lean 4环境中进行，对比基线包括MUSTARD（Autoformalizer-based）、PromptCoT/ScaleQuest（LLM-based）、Conjecture-Prover（消融基线）。DExplorer在5000次探索中生成3209个有效陈述，成功率54.52%，显著高于Conjecture-Prover的40.70%。Token成本从52.9K降至8.8K，降幅83%。Top-500复杂度从1231提升至1374，Top-500难度从0.16降至0.05（越低越难）。

| 方法 | 有效陈述数 | 成功率 (%) | Token Cost | Cplx.500 | Diff.500 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| MUSTARD | 3791 | - | >172,927 | 1231 | 0.16 |
| Conjecture-Prover | 1164 | 40.70 | 187,128 | 1193 | 0.09 |
| DExplorer (Staged) | 2340 | 52.10 | 8,841 | 1374 | 0.05 |
| DExplorer | 2726 | 54.52 | 8,800 | 1374 | 0.05 |

消融实验显示，移除Exploratory Transformation（即DExplorer Staged）导致成功率从54.52%降至52.10%，复杂度从1374降至1193，表明探索轨迹蒸馏对提升复杂度和成功率至关重要。移除DExploration框架（即Conjecture-Prover）导致成功率大幅下降，且Token成本激增，验证了逐步探索在效率上的优势。

评估边界方面，本文主要关注形式化陈述的有效性、复杂度和难度，缺乏与纯自然语言合成方法在“解题能力提升”上的直接对比。可复现性方面，论文提供GitHub链接，但Lean 4环境配置和超参数细节需查阅附录。

## 关联研究分析

从问题动机看，DExploration与AlphaGeometry同属“符号+神经”结合路线，但AlphaGeometry侧重解题，DExploration侧重出题。AlphaGeometry通过符号推导引擎保证几何问题的有效性，但局限于几何领域；DExploration通过Lean 4覆盖通用数学，但依赖现有定理库。差异根源在于任务特性：解题需快速收敛，出题需探索多样性。DExploration的逐步探索机制更适合出题，但可能牺牲解题效率。

从方法设计看，DExploration与CogAtom同属结构化生成路线，但CogAtom通过认知原子图生成自然语言问题，DExploration通过依赖图生成形式化陈述。CogAtom的优势在于自然语言多样性，DExploration的优势在于逻辑严谨性。差异根源在于验证机制：CogAtom依赖LLM自我验证，DExploration依赖Lean 4形式化验证。DExploration的验证更可靠，但自然语言表达力受限。

## 总结

DExploration旨在解决数学问题合成中表达力、有效性与复杂性的三难困境，其切入点在于将问题合成重构为逐步演绎探索，通过Lean 4环境保证每一步推导的有效性，从而突破外部证明器的复杂度上限。该方法通过探索轨迹蒸馏解决数据稀缺问题，实现了成功率54.52%和Top-500难度0.05的提升。然而，其探索深度仍受限于现有定理库的复杂度边界，生成的难题在开源LLM上解题率极低，暗示其可能触及当前LLM的能力边界。当探索深度超过现有定理库的复杂度上限时，DExploration是否仍能生成有效的高难度陈述，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_34523096)