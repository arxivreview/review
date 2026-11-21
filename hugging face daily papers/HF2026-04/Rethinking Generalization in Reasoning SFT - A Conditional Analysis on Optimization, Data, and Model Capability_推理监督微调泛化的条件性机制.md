# HuggingFace最新推荐论文 ｜Rethinking Generalization in Reasoning SFT: A Conditional Analysis on Optimization, Data, and Model Capability ｜推理监督微调泛化的条件性机制

研究机构：上海交通大学、中国科学技术大学

作者：Qihan Ren、Peng Wang、Ruikun Cai 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.06628)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.06628)

> 大语言模型后训练中，监督微调（Supervised Fine-Tuning, SFT）常被诟病为仅提升域内性能而缺乏跨域泛化能力，这一“SFT记忆化，强化学习泛化”的叙事主导了当前研究。然而，既有结论多建立在短训练周期、低质量数据或弱基座模型等特定实验条件下，混淆了优化不足与算法固有缺陷。本文通过系统解耦优化动态、数据质量与模型能力三个变量，揭示了推理SFT泛化的条件性本质。其价值在于修正了领域内对SFT泛化能力的绝对化认知，但缺乏与强化学习范式的直接公平对比，且未量化泛化收益与安全退化之间的精确权衡边界。

## 研究背景

当模型在数学推理任务上进行SFT时，其跨域能力（如代码、科学推理）往往在训练初期出现显著下降，随后缓慢恢复。这一现象被称为“dip-and-recovery”动态，其根源在于长思维链（Long Chain-of-Thought, Long-CoT）数据的拟合难度：模型首先模仿长文本的表面形式（冗长思考），而非内化其中的程序性推理模式（如回溯、验证）。这种表面模仿导致早期检查点在域外任务上表现不佳，而充分优化后，模型才能提取出可迁移的推理结构。

后训练领域长期存在SFT与强化学习（Reinforcement Learning, RL）的对比争议。Chu et al. (2025) 在合成任务上确立了“SFT记忆化，RL泛化”的框架，后续研究在数学推理中复现了类似结论。然而，这些研究的实验条件存在系统性偏差：Chu et al. (2025) 未使用Long-CoT监督，Huan et al. (2025) 训练周期过短，Wu et al. (2026) 数据质量不均，且多数研究使用弱基座模型而未将模型能力作为独立变量。这种混淆使得“SFT不泛化”的结论可能仅是特定实验条件下的伪影，而非SFT目标的固有局限。

本文切入点在于将SFT泛化视为一个条件性现象，而非固定属性。通过控制优化步数、数据质量与基座模型规模，本文旨在回答：在何种条件下推理SFT能够泛化，以及这种泛化的代价是什么。这一视角将问题从“SFT是否泛化”转变为“SFT在什么条件下泛化”，为理解后训练机制提供了更精细的分析框架。

## 核心方法

### 方法参照系

本文问题属于后训练泛化机制分析，与标准SFT流程的关键差异在于：标准流程关注最终检查点的性能，而本文关注训练动态轨迹（dip-and-recovery）及多变量解耦。参照系为基于Long-CoT数据的SFT，目标函数为响应token的负对数似然：

$$ \mathcal{L}_{SFT} = -\sum_{t=1}^{T} \log P(y_t | x, y_{<t}) $$

其中 $x$ 为输入，$y_t$ 为第 $t$ 个响应token。本文创新在于系统变化优化动态、数据质量与模型能力，而非仅优化单一变量。

### 优化动态与Dip-Recovery机制

设计动机：短训练周期导致跨域性能被系统性低估，需揭示优化不足与过优化的边界。本文发现Long-CoT SFT中，跨域性能呈现dip-and-recovery模式：初期下降，随后恢复并超越基座模型。这一动态源于模型首先学习长文本的表面形式（响应长度激增），随后内化程序性推理模式（响应长度收缩）。公式上，响应长度 $L(t)$ 与性能 $P(t)$ 呈负相关：

$$ \frac{dL(t)}{dt} < 0 \implies \frac{dP(t)}{dt} > 0 \quad \text{(在恢复阶段)} $$

这表明响应长度可作为优化阶段的诊断指标：长度收缩伴随性能提升，标志着从表面模仿到模式内化的转变。

### 数据质量与程序性模式迁移

设计动机：低质量数据导致泛化失败，需区分数据质量与数据结构的影响。本文对比验证过的Long-CoT数据（Math-CoT-20k）与低质量数据（NuminaMath-20k），发现前者在域外任务上持续增益，后者导致广泛退化。关键发现是：来自玩具算术游戏（Countdown）的Long-CoT数据，在强基座模型上可提升数学、代码、科学推理性能，甚至优于无CoT的多样化数学数据。这表明泛化的核心是程序性模式（如回溯、验证），而非数学内容本身。数据质量的影响可形式化为：

$$ \Delta P_{OOD} = f(\text{Quality}, \text{Structure}) \quad \text{where} \quad \text{Quality} \in \{\text{Verified}, \text{Low-Quality}\} $$

验证数据通过提供正确的推理轨迹，使模型能够提取可迁移的程序性模式，而低质量数据则强化了错误模式。

### 模型能力与表面模仿阈值

设计动机：弱模型无法内化程序性模式，需量化模型能力对泛化的门槛效应。本文在相同数据与协议下训练Qwen3系列（1.7B, 4B, 8B, 14B），发现14B模型呈现明显的dip-and-recovery并实现广泛泛化，而1.7B模型在所有基准上增益微弱或为负，且响应长度持续偏长。这表明弱模型仅模仿表面冗长，未能内化推理模式。模型能力的影响可表示为：

$$ \text{Generalization} = g(\text{Capability}) \quad \text{where} \quad \text{Capability} \propto \text{Model Size} $$

当模型能力低于阈值时，SFT仅导致表面模仿，泛化失败；高于阈值时，模型能够提取程序性模式，实现跨域迁移。

## 实验评估

实验采用Qwen3-14B-Base与Qwen3-8B-Base为主模型，辅以InternLM2.5-20B-Base与Qwen2.5系列验证跨家族鲁棒性。训练数据为Math-CoT-20k（20,480条验证过的Long-CoT数学推理样本），默认协议为AdamW优化器、学习率5e-5、批量大小256、余弦衰减、8个epoch。评估覆盖域内（MATH500, AIME24）、域外（LCB v2, GPQA-D, MMLU-Pro）、通用能力（IFEval, AlpacaEval 2.0, HaluEval, TruthfulQA）及安全（HEx-PHI）。基线包括基座模型、无CoT数据、低质量数据及不同优化动态设置。

| 模型 | 数据 | MATH500 | AIME24 | LCB v2 | GPQA-D | IFEval |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Qwen3-14B-Base | Base | 77.8% | 14.7% | 37.5% | 41.8% | 64.2% |
| Qwen3-14B-Base | Math-CoT-20k (640 steps) | 95.1% | 66.0% | 72.2% | 63.3% | 74.4% |
| Qwen3-14B-Base | NuminaMath-20k (640 steps) | 74.8% | 14.0% | 62.7% | 38.4% | 69.1% |
| Qwen3-1.7B-Base | Math-CoT-20k (640 steps) | 56.2% | 5.0% | 59.4% | 9.4% | 59.8% |

Qwen3-14B-Base在Math-CoT-20k上MATH500达95.1%，AIME24达66.0%，LCB v2达72.2%，显著超越基座模型（77.8%, 14.7%, 37.5%）。NuminaMath-20k导致MATH500降至74.8%，LCB v2降至62.7%，验证了低质量数据的负面影响。Qwen3-1.7B-Base在Math-CoT-20k上MATH500仅56.2%，低于基座模型58.9%，LCB v2为59.4%，高于基座模型9.1%但远低于14B模型，证实了模型能力门槛。

消融实验显示，优化动态对泛化影响显著：16个epoch余弦衰减下，Qwen3-14B-Base MATH500达95.5%，AIME24达68.7%；而16个epoch恒定学习率1e-4下，MATH500降至90.7%，AIME24降至37.0%，LCB v2降至30.9%，表明激进优化导致过拟合。数据结构方面，Countdown-CoT-20k在Qwen3-14B-Base上MATH500达91.5%，AIME24达41.7%，LCB v2达72.4%，接近Math-CoT-20k性能，验证了程序性模式的迁移性。

评估边界方面，本文未提供与RLVR（如GRPO、DeepSeek-R1）的直接公平对比，仅使用DeepSeek-R1生成数据作为高质量Long-CoT来源。安全评估显示，Long-CoT SFT导致HEx-PHI攻击成功率上升，模型在思考中自我合理化（如“为教育目的”）并生成有害内容，但论文未量化安全退化与泛化收益的精确权衡。代码开源（github.com/Nebularaid2000/rethink-sft-generalization），超参数完整，但GPU配置未明确说明。

## 关联研究分析

从问题动机看，本文与Huan et al. (2025) 的SFT泛化研究形成直接对比。Huan et al. (2025) 在短训练周期下发现SFT跨域增益有限，本文复现了该结果，但指出这是优化不足的伪影：延长训练后，SFT泛化性能显著超越基座模型。差异根源在于实验条件：Huan et al. (2025) 未控制优化步数，而本文系统变化epoch数，揭示了dip-and-recovery动态。这一发现挑战了“SFT不泛化”的绝对化结论，表明泛化是条件性的，而非算法固有缺陷。

从方法设计看，本文与ZPD-Guided Synthesis（基于最近发展区的数据合成）共享课程学习思想，但焦点不同。ZPD-Guided Synthesis关注数据难度动态调整以提升训练效率，本文关注数据质量与结构对泛化的影响。本文使用Countdown游戏数据验证程序性模式迁移，类似ZPD-Guided Synthesis的难度匹配，但本文更强调数据质量（验证 vs 低质量）而非难度梯度。差异根源在于任务特性：ZPD-Guided Synthesis针对数据稀缺场景，本文针对泛化机制分析，两者互补而非竞争。

## 总结

本文核心矛盾在于SFT泛化能力的认知偏差：既有研究将优化不足误判为算法局限。切入点在于系统解耦优化动态、数据质量与模型能力，通过控制变量揭示泛化的条件性。方法上，本文采用多变量SFT实验，结合dip-and-recovery动态分析与程序性模式迁移验证。证明了Qwen3-14B-Base在Math-CoT-20k上MATH500达95.1%，AIME24达66.0%，显著超越基座模型，且低质量数据导致广泛退化。边界在于缺乏与RLVR的直接公平对比，且未量化安全退化与泛化收益的权衡。当模型能力低于阈值时，SFT仅导致表面模仿，泛化失败；这一阈值是否可通过数据增强或架构修改降低，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.06628)