# ACL-Findings2026最新论文 ｜WikiSeeker: Rethinking the Role of Vision-Language Models in Knowledge-Based Visual Question Answering ｜WikiSeeker：重构视觉语言模型在知识增强多模态推理中的角色

研究机构：中国科学院大学、中国科学院

作者：Yingjian Zhu、Xinming Wang、Kun Ding 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.05818)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05818)

> 知识增强多模态推理（Knowledge-Augmented Multimodal Reasoning, KAMR）旨在解决多模态大语言模型在复杂视觉问答中因依赖内部参数化知识而导致的幻觉与知识滞后问题。现有方法普遍将视觉语言模型（Vision-Language Model, VLM）仅作为答案生成器，且检索键局限于图像，导致在视觉内容模糊时检索失效，且VLM在整合检索文本时表现弱于纯文本大语言模型（Large Language Model, LLM）。本文切入点在于重新定义VLM的角色，将其拆分为负责查询改写的Refiner与负责证据验证的Inspector，并引入强化学习优化查询生成。这一架构在静态检索框架内实现了性能跃升，但其单步检索机制与硬路由策略是否限制了其在长程推理任务中的潜力，仍存疑。

## 研究背景

KB-VQA任务要求模型回答图像中未直接呈现的事实性问题，这迫使模型超越视觉感知，依赖外部知识库。然而，多模态语义鸿沟导致基于单一模态的检索常返回视觉相关但事实无关的证据，而长尾实体的覆盖不足使得模型内部参数化知识在细粒度问答中频繁失效。

主流多模态检索增强生成（Retrieval-Augmented Generation, RAG）路线试图通过引入外部知识缓解上述问题，但存在两个结构性瓶颈。其一，检索策略的静态性：多数方法仅以查询图像为检索键，忽略了用户文本查询中的语义信息，当图像内容模糊时，检索噪声急剧增加。其二，VLM角色错位：现有系统通常将VLM仅用作最终答案生成器，但实证分析表明，VLM在从检索上下文中提取答案的能力弱于纯文本LLM，视觉token往往成为干扰噪声而非有效上下文。WikiSeeker针对这两个被忽略的痛点，提出将VLM重构为具备主动检索与验证能力的智能体，而非被动的生成组件。

## 核心方法

### 多模态密集检索参照系

标准多模态RAG流程通常包含索引构建、检索与生成三个阶段。本文问题与该通用流程的关键差异在于：传统流程中检索键仅包含图像嵌入，且VLM仅参与最终生成。WikiSeeker在检索阶段引入文本查询参与，并在生成阶段引入VLM作为验证者，打破了“图像检索-文本生成”的单向流水线。

### 基于强化学习的查询改写（Refiner）

设计动机在于解决静态检索键在视觉模糊场景下的失效问题。传统方法直接使用原始问题作为文本检索键，但用户查询往往简短且抽象，缺乏视觉实体细节。WikiSeeker引入Refiner，利用VLM的视觉感知能力重写查询。该模块采用Group Relative Policy Optimization (GRPO)进行优化，其目标函数定义为：

$$
\mathcal{J}(\theta) = \mathbb{E}_{q \sim \mathcal{D}, o_i \sim \pi_{\theta_{old}}} \left[ \frac{1}{G} \sum_{i=1}^{G} \left( \min\left( \rho_i A_i, \text{clip}(\rho_i, 1-\epsilon, 1+\epsilon) A_i \right) - \beta D_{KL}[\pi_\theta || \pi_{ref}] \right) \right]
$$

其中 $\rho_i$ 为概率比率，$A_i$ 为优势函数，基于组内奖励均值计算。奖励函数由检索奖励（基于命中排名）与格式奖励（基于JSON结构有效性）组成。这一设计使模型能自主发现最优的查询改写策略，将模糊的视觉线索转化为精确的文本检索键，显著提升了检索精度。

### 解耦生成与证据验证（Inspector）

设计动机在于解决VLM在整合检索文本时表现弱于LLM的问题。Refiner输出的精确查询用于多模态检索，但检索结果可能包含噪声。WikiSeeker引入Inspector，利用VLM评估检索上下文的充分性。其决策逻辑可形式化为：

$$
A = \begin{cases}
M_{gen}(Q, S_{rerank}) & \text{if } M_{ins}(I_q, Q, S_{rerank}) = \text{PASS} \\
M_{ins}(I_q, Q) & \text{if } M_{ins}(I_q, Q, S_{rerank}) = \text{FAIL}
\end{cases}
$$

其中 $M_{gen}$ 为纯文本LLM生成器，$M_{ins}$ 为VLM。若Inspector判定检索上下文充分，则路由至LLM进行答案提取；否则，VLM直接利用内部参数化知识作答。这种解耦策略利用了LLM在文本摘要上的优势与VLM在视觉推理上的优势，避免了视觉token对文本理解的干扰。

## 实验评估

实验在E-VQA、InfoSeek和M2KR基准上进行，对比了Wiki-LLaVA、EchoSight、OMGM等主流多模态RAG方法。基线覆盖了从纯视觉检索到多模态重排序的多种路线，但缺失2026年最新的智能体多步搜索方法（如DR-MMSearchAgent），这可能限制了性能对比的全面性。

| 方法 | E-VQA R@1 | E-VQA R@5 | InfoSeek R@1 | InfoSeek R@5 |
| :--- | :--- | :--- | :--- | :--- |
| OMGM | 13.2 | 48.8 | 53.8 | 77.9 |
| WikiSeeker (w/o Refiner) | 36.1 | 58.1 | 56.1 | 77.6 |
| WikiSeeker (w. Refiner) | 44.1 | 59.9 | 67.0 | 83.7 |

WikiSeeker在E-VQA上的R@1达到44.1，较OMGM提升30.9个百分点；在InfoSeek上的R@1达到67.0，较OMGM提升13.2个百分点。这表明Refiner引入的文本查询参与检索是性能提升的主要驱动力。

| 设置 | 生成器 | 策略 | E-VQA Accuracy (%) | InfoSeek Accuracy (%) |
| :--- | :--- | :--- | :--- | :--- |
| Zero-shot | VLM | VLM-only | 51.81 | 38.7 |
| Zero-shot | LLM | LLM-only | 52.97 | 37.69 |
| Zero-shot | VLM + LLM | Decoupled | 54.48 | 38.19 |
| Fine-tuned | VLM | VLM-only | 52.59 | 44.06 |
| Fine-tuned | LLM | LLM-only | 53.92 | 43.47 |
| Fine-tuned | VLM + LLM | Decoupled | 55.62 | 44.72 |

消融实验显示，解耦生成策略在零样本和微调设置下均优于单一模型生成。在E-VQA上，解耦策略较VLM-only提升3.81个百分点，较LLM-only提升2.65个百分点。这验证了Inspector路由机制的有效性，即通过验证检索质量，将可靠证据交由LLM处理，不可靠证据交由VLM内部知识处理，实现了两种模型能力的互补。

评估指标涵盖检索精度（Recall@K）与问答准确率（BEM/VQA Accuracy），但缺乏对推理过程可解释性的细粒度评估。代码已开源，实验在4块NVIDIA A800 GPU上完成，超参数设置详细，具备较高的可复现性。

## 关联研究分析

从问题动机看，WikiSeeker与EchoSight同属多模态RAG框架，但两者对VLM角色的定位存在根本差异。EchoSight将VLM视为端到端的生成器，依赖其多模态理解能力直接输出答案；而WikiSeeker认为VLM在文本整合上存在劣势，因此将其拆解为检索前的查询改写者与检索后的证据验证者。这一差异的根源在于对“多模态语义鸿沟”的不同理解：EchoSight假设VLM能弥合图文鸿沟，而WikiSeeker发现视觉token在文本检索上下文中常表现为噪声，因此选择将视觉感知与文本生成解耦。

从方法设计看，WikiSeeker与Search-R1等智能体多步搜索方法在检索策略上形成对比。Search-R1通过强化学习训练模型自主规划多步检索路径，以应对长程证据链断裂问题；而WikiSeeker仅支持单步检索，其Refiner仅优化单次查询的改写。这一差异源于任务复杂度的不同：WikiSeeker聚焦于静态百科知识中的细粒度实体定位，单步检索足以覆盖大部分事实性问答；而Search-R1面向动态开放域，需要迭代验证。WikiSeeker未探索多步检索机制，其硬路由策略在检索失败时直接回退至VLM内部知识，这种设计在长尾实体分布下是否会导致性能瓶颈，论文未给出回答。

## 总结

WikiSeeker旨在解决多模态RAG中检索键静态性与VLM角色错位导致的性能瓶颈。其切入点在于利用VLM的视觉感知能力优化检索查询，并通过解耦生成策略规避VLM在文本整合上的劣势。该方法通过GRPO训练的Refiner与验证检索充分性的Inspector，在E-VQA和InfoSeek基准上实现了SOTA性能，E-VQA R@1达到44.1，InfoSeek R@1达到67.0。然而，论文自身实验暴露了其边界：单步检索机制无法处理多跳推理任务，且硬路由策略在检索失败时缺乏迭代修正能力。当查询涉及需要多步逻辑关联的复杂事实时，这种单步检索与硬路由的组合是否足以维持推理链的连贯性，仍是待验证的问题。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05818)