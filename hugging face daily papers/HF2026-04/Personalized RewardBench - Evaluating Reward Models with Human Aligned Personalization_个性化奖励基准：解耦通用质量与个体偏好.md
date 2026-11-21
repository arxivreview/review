# HuggingFace最新推荐论文 ｜Personalized RewardBench: Evaluating Reward Models with Human Aligned Personalization ｜个性化奖励基准：解耦通用质量与个体偏好

研究机构：美国加州大学戴维斯分校

作者：Qiyao Ma、Dechen Gao、Rui Cai 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.07343)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07343)

> 现有奖励模型（Reward Model, RM）在通用对话中表现优异，却难以捕捉用户特定的风格与约束，导致对齐效果因人而异。传统基准通过降低回答质量来构造负样本，混淆了“通用质量”与“个性化偏好”，无法区分模型是真正理解了用户还是仅仅识别了错误。本文提出 Personalized RewardBench，通过构造通用质量等价但个性化偏好对立的回答对，并验证其与下游策略性能的强相关性。该基准揭示了当前前沿模型在个性化对齐上的显著瓶颈，但 Planner 模块引入的额外推理开销与潜在误差累积尚未被量化。

## 研究背景

当大语言模型（Large Language Models, LLMs）面对不同用户时，同一问题的“好回答”标准存在本质差异。这种差异源于用户的历史交互与特定约束，即个性化偏好。然而，传统强化学习从人类反馈（Reinforcement Learning from Human Feedback, RLHF）中的奖励模型通常基于通用质量指标（如事实性、相关性）进行训练，导致模型在捕捉个体特异性时失效。为评估这种失效，需要构建能够隔离“通用质量”与“个性化偏好”的基准。

主流奖励模型基准（如 RewardBench）通过选择低质量回答作为负样本，使得模型只需识别错误即可得分，无法验证其对用户特定需求的理解。PersonalRewardBench 虽引入个性化查询，但仅关注查询筛选，未将用户画像直接纳入奖励评估机制。此外，静态基准分数与下游策略（如 Best-of-N, BoN 或 Proximal Policy Optimization, PPO）性能之间缺乏可证明的相关性，导致高基准分数未必转化为实际效用。本文切入点在于构建一个通用质量恒定、仅个性化维度对立的基准，并系统验证其与下游策略效用的映射关系。

## 核心方法

### 方法参照系

标准奖励模型评估流程基于 Bradley-Terry (BT) 模型，假设偏好数据由通用质量决定。本文的关键差异在于：负样本（rejected response）并非来自低质量源，而是故意违反用户特定 Rubric 但保持通用高质量，从而将评估焦点从“质量判别”转向“偏好对齐”。

### 偏好对构造与质量解耦

传统基准中，负样本通常由较小模型生成或注入错误，导致通用质量与个性化偏好混淆。本文利用 LaMP-QA 数据集的用户历史，通过检索增强生成（Retrieval-Augmented Generation, RAG）提取用户画像 $u$，并基于用户特定 Rubric 集合 $R_u$ 构造偏好对。具体而言，Chosen 回答 $y_c$ 在生成时显式条件于 $R_u$，而 Rejected 回答 $y_r$ 则刻意规避 $R_u$，但均使用同一高质量 LLM（Gemini-3-Flash）生成。这一设计确保了 $y_c$ 与 $y_r$ 在事实性、相关性等通用维度上得分相近，仅在个性化维度上存在显著差异。

$$
y_c \sim P(y | q, u, R_u), \quad y_r \sim P(y | q, u, \neg R_u)
$$

该公式表明，两个回答的生成概率分布仅由是否满足 $R_u$ 区分，从而在数据层面实现了通用质量与个性化偏好的解耦。

### Planner 模块与训练-测试对齐

直接注入用户画像 $u$ 会导致训练-测试失配，因为奖励模型通常在标准提示-回答对上训练，缺乏处理辅助画像数据的能力。本文引入 Planner 模块 $P$，通过交叉熵损失训练其从查询 $q$ 和画像 $u$ 推断出结构化 Rubric $\tilde{R}_u$：

$$
\tilde{R}_u = P(q, u)
$$

随后，奖励模型基于 $\tilde{R}_u$ 计算分数 $s = \text{RM}(q, \tilde{R}_u, y)$。这一设计将非结构化的历史交互转化为结构化的评估标准，缓解了直接注入画像导致的性能退化，使模型能够专注于基于推断出的 Rubric 进行偏好判断。

## 实验评估

实验在自建 Personalized RewardBench 上进行，覆盖艺术、生活方式和社会文化三个领域。基线包括标量 RM（Skywork, Internlm2）、生成式 RM（RM-R1, R3, GPT-5.1, Gemini-3-Flash）及微调个性化 RM（BT, GPO, PAL）。缺失因果去偏类基线，但覆盖了当前主流架构。

| 模型类型 | 代表模型 | Art & Ent. (%) | Lifestyle (%) | Society (%) |
| :--- | :--- | :--- | :--- | :--- |
| Scalar RM | Skywork-Reward-V2-Llama-3.1-8B | 67.88 | 71.88 | 63.23 |
| Generative RM | Gemini-3-Flash | 72.36 | 75.94 | 75.51 |
| Finetuned RM | Bradley-Terry | 63.75 | 66.84 | 64.99 |

Gemini-3-Flash 在 Lifestyle 领域达到 75.94% 的最高准确率，但仍未突破 76% 阈值，表明即使前沿模型在个性化对齐上仍存在显著瓶颈。标量 RM 与生成式 RM 之间无显著性能差异，暗示架构规模并非个性化对齐的决定因素。

Planner 模块的消融实验显示，直接注入用户画像（w/ profile）导致性能低于无画像基线（w/o profile），而使用 Planner 推断 Rubric（w/ plan）则恢复并超越基线。这一反直觉结果证实了训练-测试失配的存在，并验证了结构化 Rubric 作为中介变量的有效性。

评估边界方面，本文未报告置信区间，且 Planner 模块的推理延迟与误差累积未量化。代码与数据已开源，但超参数细节（如检索 top-k 值）仅在附录中提及，复现时需仔细核对。

## 关联研究分析

从问题动机看，Personalized RewardBench 与 PersonalRewardBench 的核心差异在于评估粒度。后者仅筛选适合个性化的查询，未将用户画像纳入奖励计算；前者则通过 Rubric 约束直接评估模型对用户特定需求的响应能力。这一差异源于任务定义的不同：前者关注“哪些查询需要个性化”，后者关注“模型如何满足个性化”。

从方法设计看，本文的 Planner 模块与 LaMP-QA 的检索增强策略同源，但应用目标不同。LaMP-QA 旨在提升问答准确性，而本文旨在提升奖励模型的偏好判别能力。这种转化揭示了个性化对齐中“理解用户”与“评估回答”之间的鸿沟：即使模型能检索用户历史，若缺乏将历史转化为评估标准的机制，仍无法有效指导策略优化。

## 总结

本文针对现有奖励模型基准混淆通用质量与个性化偏好的问题，通过构造质量等价但偏好对立的回答对，建立了 Personalized RewardBench。该基准揭示了当前 SOTA 模型在个性化对齐上的显著瓶颈（最高 75.94%），并证明了基准分数与下游 BoN/PPO 性能的强相关性（NDCG 0.9180）。然而，Planner 模块引入的额外推理开销与潜在误差累积未被量化，且基准仅覆盖单一查询每用户场景。当用户历史长度增加或 Rubric 复杂度提升时，Planner 的推断准确率是否会显著下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07343)