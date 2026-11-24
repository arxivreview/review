# CVPR2026最新论文 ｜MMTIT-Bench: A Multilingual and Multi-Scenario Benchmark with Cognition-Perception-Reasoning Guided Text-Image Machine Translation ｜多模态图像内机器翻译的认知-感知-推理范式

研究机构：中国科学院、南开大学

作者：Gengluo Li、Chengquan Zhang、Yupu Liang 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.23896)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.23896)

> 图像内机器翻译（Text-Image Machine Translation, TIMT）旨在直接转换图像中的文本内容，其核心难点在于低资源语言下视觉布局与语义的联合重构。现有端到端模型常陷入纯语言推理或级联解析的陷阱，忽视了视觉认知在翻译决策中的锚定作用。本文提出CPR-Trans数据范式，通过结构化思维链将场景认知、文本感知与翻译推理统一，并构建覆盖14种非英中语言的MMTIT-Bench基准。该范式显著提升了小模型性能，但其对视觉依赖度的量化验证仍显不足，且合成数据分布偏差可能掩盖真实场景下的泛化极限。

## 研究背景

当视觉语言大模型（Vision-Language Large Models, VLLMs）处理图像内文本时，常面临视觉特征与文本语义对齐失效的困境。这种失效源于模型倾向于依赖语言先验而非视觉证据，导致在歧义消解或复杂布局中产生幻觉。为缓解此问题，研究者引入思维链（Chain-of-Thought, CoT）推理，但现有设计多为级联式（先OCR后翻译）或纯语言推理，未能将视觉感知深度嵌入推理过程，致使模型在低资源语言场景下鲁棒性不足。

TIMT领域的评估长期受限于基准的语言覆盖与场景单一性。早期数据集如DITrans和DoTA聚焦英中文档翻译，MTIT6虽扩展至真实场景但仅涵盖4种语言，无法全面评估多语言泛化能力。同时，级联系统因OCR错误传播导致翻译失败，而端到端模型虽统一了架构，却缺乏针对TIMT的原生推理范式设计。本文切入点在于：现有VLLMs在TIMT中缺乏有效的“思考范式”，既未充分利用视觉认知，也未提供可解释的推理监督。

## 核心方法

### 方法参照系

本文问题置于端到端多模态翻译框架下，与通用VLLM微调流程的关键差异在于：传统微调仅优化最终翻译标签，而本文引入结构化推理监督，将视觉感知过程显式编码为训练信号，以解决模型“视觉依赖度不足”导致的语义漂移问题。

### CPR-Trans 数据范式

CPR-Trans的核心创新在于将翻译过程解耦为三个认知阶段，形成统一推理序列。设计动机在于：直接翻译或简单CoT设计无法区分视觉理解与语言转换，导致模型在复杂布局中丢失空间结构信息。本文通过VLLM驱动的多阶段生成流水线，构建结构化监督信号：

$$
\text{CPR-Trans} = \langle \text{Cognition} \rangle \langle \text{Perception} \rangle \langle \text{Trans} \rangle \rightarrow \text{Answer}
$$

其中，$\text{Cognition}$ 阶段生成全局视觉上下文描述（排除文本识别），$\text{Perception}$ 阶段基于OCR标注推理空间布局与阅读顺序，$\text{Trans}$ 阶段整合视觉与文本理解生成翻译决策。该公式的物理含义是：将隐式的视觉-文本对齐过程显式化为可监督的推理链，使模型在生成翻译前必须完成视觉认知与空间感知，从而强化视觉依赖。

### 多阶段生成流水线

数据生成采用VLLM辅助的多阶段策略，确保推理链的语义一致性。设计动机在于：人工标注成本高且难以规模化，而纯模型生成易产生幻觉。本文通过Gemini 2.5 Flash进行初始解析，结合多模型投票机制（Gemini、Seed 1.6 Thinking、Qwen3-VL Thinking）筛选高质量翻译，最终形成165,200个对齐样本。该流程的关键在于：每个阶段的输出作为下一阶段的输入约束，例如$\text{Perception}$阶段必须与人工OCR结果一致，从而确保推理链的可靠性。

## 实验评估

实验在MMTIT-Bench上进行，覆盖14种非英中语言，评估协议包括VLLM-based Judging（Gemini 2.5 Flash、Qwen3-VL-235B）和COMET指标。基线涵盖级联系统（MinerU2.5+Qwen3）、通用VLLMs（Gemini 2.5-Flash、Qwen3-VL、Seed1.6）及本文微调模型。

| 模型 | 参数 | Gemini-Flash (other2en) | Gemini-Flash (other2zh) | COMET (other2en) | COMET (other2zh) |
|---|---|---|---|---|---|
| Qwen2.5-VL-Origin | 7B | 53.98 | 46.89 | 70.27 | 71.67 |
| Qwen2.5-VL-sft(Direct) | 7B | 68.40 | 62.42 | 75.42 | 76.81 |
| Qwen2.5-VL-sft(CPR-Trans) | 7B | 83.98 | 82.84 | 81.07 | 81.04 |
| Gemini 2.5-Flash | - | 82.94 | 85.00 | 76.21 | 78.81 |

CPR-Trans微调的7B模型在Gemini-Flash评估下other2en方向得分83.98，接近Gemini 2.5-Flash的82.94，显著优于直接翻译基线（68.40）。在COMET指标下，CPR-Trans（81.07/81.04）也超越直接翻译（75.42/76.81），验证了结构化推理对翻译质量的提升。

| 组件 | 3B (Gemini o2e) | 7B (Gemini o2e) | 3B (Qwen3VL o2e) | 7B (Qwen3VL o2e) |
|---|---|---|---|---|
| Baseline | 72.31 | 74.65 | 74.06 | 76.30 |
| +Cognition | 75.23 | 76.91 | 76.82 | 79.08 |
| +Perception | 72.40 | 74.43 | 73.53 | 75.69 |
| +Trans | 79.47 | 80.73 | 78.49 | 80.51 |
| Full CPR-Trans | 82.00 | 83.98 | 81.39 | 82.99 |

消融实验显示，移除Cognition导致性能下降（7B从83.98降至76.91），而Perception单独贡献有限（7B从74.43至75.69），但与其他组件结合后产生协同效应。Trans阶段贡献最大（7B从80.73至83.98），表明显式翻译推理对忠实度与流畅度的提升最为显著。

评估边界方面，MMTIT-Bench仅覆盖静态图像，未涉及视频或动态场景；合成数据（SynthDog）可能引入分布偏差，论文未提供真实场景下的泛化验证。可复现性上，论文未公开代码，但提供了详细超参数（3 epochs, lr=3e-5, 32 H20 GPUs），便于复现。

## 关联研究分析

从问题动机看，本文与UniTranslator同属端到端TIMT路线，但UniTranslator侧重架构统一建模，而本文聚焦数据范式。差异根源在于：UniTranslator假设视觉-文本对齐可通过联合训练自动学习，而本文认为显式推理监督对小模型更关键。MT3采用多任务强化学习优化MLLM，本文则通过结构化CoT微调，二者均旨在解决VLLM在TIMT中的专业化不足，但MT3侧重训练策略，本文侧重数据构造。

从方法设计看，VQA-Augmented MT通过视觉问答对增强对齐，本文的Cognition阶段与之逻辑相似，但本文更强调空间感知与阅读顺序。VQA方法依赖外部QA数据，而CPR-Trans的推理链内生于翻译过程，无需额外数据源。这一差异暗示：当视觉布局复杂时，显式空间推理可能比语义增强更有效，但论文未对比VQA方法在复杂布局下的表现。

## 总结

本文核心矛盾在于低资源语言下VLLMs的视觉依赖度不足与推理范式缺失。切入点在于：现有方法未将视觉认知结构化嵌入翻译过程，而本文通过CPR-Trans范式显式编码认知-感知-推理链，使小模型获得可解释的推理监督。实验证明，CPR-Trans微调的7B模型在Gemini-Flash评估下other2en方向得分83.98，接近Gemini 2.5-Flash的82.94，验证了范式有效性。边界在于：MMTIT-Bench仅覆盖静态图像，合成数据分布偏差未量化，且缺乏对视觉依赖度的直接度量。当支持集增大到真实场景时，CPR-Trans的推理链是否仍能保持视觉锚定，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.23896)