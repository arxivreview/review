# HuggingFace最新推荐论文 ｜Edit-Compass & EditReward-Compass: A Unified Benchmark for Image Editing and Reward Modeling ｜指令式图像编辑统一评测基准

作者：Xuehai Bai、Yang Shi、Yi-Fan Zhang 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.13062)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.13062)

> 指令式图像编辑（IBIE）领域面临评估标准与模型能力脱节的困境，现有基准难以区分前沿模型的细微差异，且奖励模型评测脱离强化学习（RL）实际分布。本文通过构建包含深层推理任务的多维度评测体系，并模拟RL采样策略构建偏好对，旨在解决评估失真问题。其价值在于揭示了开源模型在复杂推理上的短板，但评估协议对闭源模型黑盒特性的依赖仍存疑。

## 研究背景

当编辑模型面对“让左边的人把杯子递给右边的人”这类指令时，传统基于CLIP-I的自动指标无法捕捉空间交互的逻辑错误，导致评估分数与人类感知出现系统性偏差。这种偏差源于评估维度的单一性，即仅关注语义相似度而忽略视觉一致性（Visual Consistency）与指令感知（Instruction Awareness）。为量化这种偏差，需引入多模态大语言模型（MLLM）作为裁判，通过思维链（CoT）推理结合结构化评分细则（Scoring Rubrics），将评估从单一标量扩展为多维度的细粒度分析。

IBIE领域的核心矛盾已从“能否编辑”转向“编辑是否精准”，但评估体系滞后于模型能力的演进。主流基准如GEdit-Bench和ImgEdit-Bench依赖简单的MLLM提示，任务难度局限于浅层感知，导致强模型分数饱和，无法区分细微能力差异。同时，RL优化中的奖励模型（Reward Model）评测存在分布不匹配问题，现有基准多采用跨模型对比，而实际RL训练中奖励模型需比较同一模型在不同去噪步长下的输出。Edit-Compass通过引入世界知识推理（WKR）和算法视觉推理（AVR）等高难度任务，并模拟FlowGRPO采样策略构建偏好对，填补了深层推理评估与RL场景模拟的空白。

## 核心方法

### 方法参照系

本文问题属于评测体系构建，而非生成方法。与GEdit-Bench等通用基准的关键差异在于：前者采用单一指标与简单提示，本文采用多维度CoT评估与模拟RL分布的偏好对构建，旨在解决强模型评估失真与奖励模型评测脱离实际的问题。

### 多维度CoT评估框架

传统评估通常输出单一标量分数，缺乏对错误类型的解释。本文在评估流程中引入结构化推理，将评估分解为指令感知、视觉一致性和视觉质量三个维度。每个维度的评分由MLLM基于预定义的评分细则生成，公式如下：

$$ S_{total} = \frac{1}{3} \sum_{d \in \{IA, VC, VQ\}} \left( \frac{1}{|C_d|} \sum_{c \in C_d} s_{c} \right) $$

其中 $S_{total}$ 为总分，$C_d$ 为维度 $d$ 下的子组件集合，$s_c$ 为子组件 $c$ 的评分。该设计动机在于解决传统指标无法区分“语义正确但视觉失真”与“语义错误”的问题，通过细粒度子组件评分提升评估的可解释性与人类对齐度。

### 模拟RL分布的偏好对构建

现有奖励模型基准多采用跨模型对比，导致评估分布与RL训练分布不匹配。本文在采样阶段引入FlowGRPO-inspired策略，通过随机微分方程（SDE）控制去噪步长，从同一编辑模型生成候选输出。偏好对构建公式为：

$$ P = \{ (I_{src}, T, I_{pos}, I_{neg}) \mid I_{pos}, I_{neg} \sim \mathcal{M}(I_{src}, T, \sigma) \} $$

其中 $\mathcal{M}$ 为编辑模型，$\sigma$ 为去噪步长参数。该设计动机在于解决奖励模型在RL训练中需比较同一模型不同输出而非不同模型输出的问题，通过模拟真实RL采样过程，确保偏好对反映模型在优化过程中的实际决策场景。

## 实验评估

实验在Edit-Compass（2,388实例）和EditReward-Compass（2,251偏好对）上进行，覆盖29个图像编辑模型和21个奖励模型。基线审计显示，对比方法涵盖扩散模型（FLUX.1 Kontext）、统一多模态模型（Qwen-Image-Edit, BAGEL）及闭源SOTA（Nano-Banana Pro），但缺失早期GAN基线（如InstructPix2Pix仅作为低分参照）。

| 模型 | 类型 | General | World Knowledge | Visual Reasoning | Overall |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Nano-Banana Pro | 闭源 | 4.76 | 4.33 | 3.61 | 3.99 |
| Qwen-Image-Edit | 开源 | 4.61 | 2.33 | 1.26 | 2.69 |
| FLUX.1 Kontext Dev | 开源 | 3.53 | 1.65 | 1.27 | 1.93 |
| InstructPix2Pix | 开源 | 1.98 | 1.51 | 1.09 | 1.19 |

Nano-Banana Pro在Overall得分上以3.99领先，Qwen-Image-Edit以2.69次之，两者差距达1.30分。在World Knowledge任务上，Nano-Banana Pro得分4.33，而Qwen-Image-Edit仅2.33，差距扩大至2.00分，表明闭源模型在深层推理任务上具有显著优势。

| 奖励模型 | 类型 | Instruction Awareness | Visual Consistency | Visual Quality | AVG |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Gemini 3.1 Pro | 闭源 | 0.8324 | 0.6002 | 0.4459 | 0.7433 |
| Qwen3.6-27B_‡ | 开源 | 0.7961 | 0.5656 | 0.5743 | 0.7183 |
| EditScore_† | 专用 | 0.5092 | 0.4160 | 0.5890 | 0.4912 |
| EditReward_† | 专用 | 0.5524 | - | 0.6369 | 0.5601 |

Gemini 3.1 Pro在AVG得分上以0.7433领先，Qwen3.6-27B_‡以0.7183次之，两者差距0.0254分。专用奖励模型EditScore_†得分仅0.4912，显著低于原生MLLM，表明专用模型在复杂场景下的泛化能力受限。

评估边界方面，Edit-Compass依赖MLLM-as-judge，可能引入裁判模型自身的偏见；EditReward-Compass的偏好对构建依赖去噪步长控制，未覆盖所有RL优化场景。可复现性上，论文提供GitHub链接，但未报告评估所需的GPU资源与推理延迟。

## 关联研究分析

从问题动机看，Edit-Compass与GEdit-Bench均旨在解决IBIE评估失真，但GEdit-Bench依赖简单MLLM提示，任务难度局限于浅层感知，导致强模型分数饱和。Edit-Compass引入WKR和AVR任务，将评估从语义相似度转向逻辑推理，揭示了开源模型在深层推理上的短板。这一差异源于任务特性决定：浅层任务无法区分模型的推理能力，而深层任务需模型具备世界知识与符号推理能力，现有开源模型在此方面存在盲区。

从方法设计看，EditReward-Compass与EditReward均针对奖励模型评测，但EditReward采用跨模型对比，而EditReward-Compass模拟FlowGRPO采样策略，构建同一模型不同输出的偏好对。这一差异源于RL训练场景决定：实际RL优化中，奖励模型需比较同一模型在不同去噪步长下的输出，而非不同模型的输出。EditReward的跨模型对比导致评估分布与训练分布不匹配，限制了奖励模型质量的忠实评估。

## 总结

IBIE领域面临评估标准与模型能力脱节的核心矛盾，现有基准无法区分前沿模型的细微差异，且奖励模型评测脱离RL实际分布。Edit-Compass通过引入深层推理任务与模拟RL采样策略，构建了多维度CoT评估框架，揭示了闭源模型在复杂推理上的优势（Nano-Banana Pro 3.99 vs Qwen-Image-Edit 2.69）及原生MLLM作为奖励模型的潜力（Gemini 3.1 Pro 0.7433 vs EditScore 0.4912）。其边界在于评估协议依赖MLLM裁判，可能引入偏见，且未覆盖所有RL优化场景。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.13062)