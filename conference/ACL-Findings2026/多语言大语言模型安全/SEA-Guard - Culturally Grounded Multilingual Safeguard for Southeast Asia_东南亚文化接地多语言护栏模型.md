# ACL-Findings2026最新论文 ｜SEA-Guard: Culturally Grounded Multilingual Safeguard for Southeast Asia ｜东南亚文化接地多语言护栏模型

作者：Panuthep Tasawong、Jian Gang Ngui、Alham Fikri Aji 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0d007443ef3f)

> 现有安全护栏在东南亚低资源语言上因依赖机器翻译而丢失文化语境，导致对地区性敏感内容的检测失效。本文切入点在于构建首个基于多智能体合成框架生成的、覆盖8种东南亚语言的文化安全数据集，并训练专用护栏模型。通过蒙特卡洛推理集成（MCRE）解决标注不确定性，SEA-Guard在文化基准上显著优于通用SOTA，但在通用安全任务上仅具竞争力，其离线标注的高计算成本限制了实时部署潜力。

## 研究背景

安全护栏模型部署于大语言模型（LLM）前后，用于分类提示与响应为安全或有害。当模型处理低资源语言时，若仅依赖英语训练数据或机器翻译，会因语义漂移与文化缺失导致安全机制失效。这种失效不仅表现为语言层面的翻译错误，更深层地源于文化特异性危害的识别困难，即通用安全分类法无法覆盖特定文化语境下的独特禁忌。

多语言安全对齐的主流路线分为行为对齐与机制干预。行为对齐（如DPO）依赖大量多语言偏好数据，成本高且易受翻译伪影影响；机制干预（如稀疏权重编辑）虽轻量但可能破坏通用能力。现有护栏模型（如LlamaGuard, ShieldGemma）多基于通用数据训练，在东南亚（SEA）等文化复杂区域表现不佳。本文针对“文化接地”这一被忽略的维度，提出通过专用数据合成框架弥补原生标注数据的稀缺，而非直接修改主模型权重。

## 核心方法

### 方法参照系

标准护栏模型训练流程依赖高质量标注数据，通常通过人工标注或简单翻译获取。本文的关键差异在于：数据源从“翻译/通用数据”转变为“文化感知的多智能体合成”，且标注环节引入概率化不确定性建模以处理文化边界模糊性。

### 多智能体文化数据合成

传统合成数据缺乏文化深度，导致模型无法区分如“泼水节”在不同国家的具体禁忌差异。本文设计输入构建、提示/响应生成、标注与质量保证四个阶段。在提示生成阶段，使用Gemma-SEA-LION-v4-27B结合指南、人设与目标语言生成提示，并通过改写缓解关键词偏差。响应生成使用四个LLM（Llama3.1-70B-IT, Gemma3-27B-IT, Gemma-SEA-LION-v4-27B-IT, GPT-OSS-20B-IT）以产生多样性。该设计解决了通用合成数据在文化细微差别上的缺失，确保数据覆盖53个SEA文化类别。

### 蒙特卡洛推理集成（MCRE）

单一推理轨迹的LLM标注往往过度自信，无法准确捕捉文化敏感内容的边界不确定性。本文提出MCRE，对每个输入执行$N$次独立随机推理，形成轨迹集合$R = \{r_1, \dots, r_N\}$。最终类别概率由经验频率估计：

$$ P(\hat{y}_{final} = c | R, x) = \frac{1}{N} \sum_{i=1}^{N} I(\hat{y}_i = c) $$

为处理Safe/Sensitive/Harmful之间的模糊性，模型在5级序数空间$C_{safety} = \{Safe, Safe\text{-}Sensitive, Sensitive, Sensitive\text{-}Harmful, Harmful\}$上分类，并计算有害性得分$h(x)$：

$$ h(x) = \sum_{c \in C_{safety}} s_c \cdot P(\hat{y}_{final} = c | R, x) $$

其中$s_c \in [0, 1]$为归一化严重度（Safe=0.0, Harmful=1.0）。最后通过阈值（0.33, 0.66）映射回三级标签。该机制通过多次采样聚合降低单次推理的过置信偏差，提升了文化边界样本的标注可靠性，尽管其计算开销比单次推理高两个数量级。

## 实验评估

实验在SEA-SafeguardBench（文化基准）、SEALS/PKU-SafeRLHF（通用基准）及视觉-文本基准上进行。基线覆盖LlamaGuard, ShieldGemma, Qwen3Guard, PolyGuard等主流护栏，但缺失机制干预类基线（如Sparse Weight Editing）。

| 模型 | Prompt AUPRC (ITW) | Response AUPRC (ITW) | Prompt AUPRC (CG) | Response AUPRC (CG) |
| :--- | :--- | :--- | :--- | :--- |
| ShieldGemma | 75.1 | 55.2 | - | - |
| Qwen3Guard-Gen 8B | 98.7 | 74.6 | 74.4 | 71.1 |
| SEA-Guard-12B | 99.5 | 80.0 | 75.4 | 73.2 |

SEA-Guard-12B在SEA-SafeguardBench的Prompt分类上达到99.5 AUPRC，Response分类达到80.0，显著优于ShieldGemma（Response 55.2）。在通用基准上，SEA-Guard-12B的Prompt AUPRC为79.5，Response为75.2，与Qwen3Guard-Gen 8B（Prompt 74.6, Response 74.4）相比具有竞争力，但未全面超越。

消融实验显示，数据规模从200k增加到1M时，性能呈边际收益递减趋势，但去重后的数据集在较少样本下达到可比性能，表明数据多样性比单纯规模更重要。MCRE的$N=10$设置平衡了标注质量与计算成本，但论文未提供不同$N$值的详细消融数据。

评估边界方面，视觉-文本基准均为英语，限制了跨语言零样本泛化的全面验证。代码与模型权重已开源（MIT License），但MCRE的离线标注流程未提供实时部署优化方案。

## 关联研究分析

从问题动机看，SEA-Guard与MrGuard同属多语言护栏，但MrGuard侧重通用推理能力的课程学习，而本文聚焦文化数据的专用合成。差异根源在于任务特性：文化安全需要细粒度的地区知识，通用推理无法替代。MrGuard在通用基准上表现稳定，但在文化特异性任务上缺乏针对性，这解释了为何本文在SEA基准上显著优于通用SOTA。

从方法设计看，本文与PolyGuard等通用多语言护栏的核心差异在于数据源。PolyGuard依赖翻译数据，导致文化语境丢失；本文通过多智能体合成生成原生文化数据。然而，本文未探索机制干预路线（如SS-Neuron），后者通过稀疏权重编辑实现跨语言安全迁移，无需大量数据。SEA-Guard的高数据合成成本与MCRE的离线限制，使其在数据效率上不及机制干预方法，但在文化准确性上更具优势。

## 总结

SEA-Guard针对东南亚低资源语言文化安全识别困难的问题，通过多智能体合成框架与MCRE标注机制，构建了首个文化接地的多语言护栏。实验证明其在SEA-SafeguardBench上Prompt AUPRC达99.5，Response AUPRC达80.0，显著优于通用SOTA。然而，其依赖离线MCRE标注的高计算成本，以及在通用安全任务上仅具竞争力的表现，暴露了文化专用性与通用泛化性之间的权衡。当数据规模进一步增大时，MCRE的标注成本是否成为主要瓶颈，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_0d007443ef3f)