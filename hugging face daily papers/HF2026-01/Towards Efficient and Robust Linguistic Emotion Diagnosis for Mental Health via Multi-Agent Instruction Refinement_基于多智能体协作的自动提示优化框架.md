# HuggingFace最新推荐论文 ｜Towards Efficient and Robust Linguistic Emotion Diagnosis for Mental Health via Multi-Agent Instruction Refinement ｜基于多智能体协作的自动提示优化框架

研究机构：新加坡国立大学

作者：Jian Zhang、Zhangqi Wang、Zhiyuan Wang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.13481)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.13481)

> 心理健康文本中的情绪共病现象导致单一标签分类失效，现有自动提示优化方法因缺乏全局规划与动态反馈，难以在复杂临床语义空间中高效搜索最优指令。本文提出 APOLO 框架，将提示优化建模为部分可观测马尔可夫决策过程，通过 Planner-Teacher-Critic-Student-Target 五智能体闭环协作实现指令的迭代精炼。该框架在六个基准数据集上取得了 SOTA 性能，但其仅优化提示词而不改变模型权重的策略，在应对深层临床知识缺失时的有效性仍存疑。

## 研究背景

临床文本中的情绪表达往往呈现共病特征，如焦虑与抑郁、创伤与内疚常交织出现。这种情绪共病（Emotional Comorbidity）使得固定模板或单标签提示词无法捕捉多态情感依赖，导致诊断遗漏。为解决此问题，自动提示优化（Automated Prompt Optimization, APO）被引入，旨在通过迭代搜索发现能覆盖复杂语义线索的最优指令。然而，通用 APO 方法多依赖生成-搜索或元提示策略，缺乏对高维提示空间的全局规划与不确定性建模，易陷入局部最优，且在医疗高风险场景下缺乏安全约束机制。

现有 APO 路线主要分为两类：生成-搜索范式通过局部搜索精炼候选提示，但探索范围有限；元提示范式依赖刚性模板，适应性不足。这两类方法均缺乏交互式反馈与风险感知能力，难以应对情绪诊断中的语义模糊与隐式表达。本文切入点在于将 APO 重构为决策控制问题，引入多智能体协作机制，通过 Planner 进行风险与成本约束下的轨迹规划，结合 Socratic 对话实现提示词的动态精炼，从而在保持模型权重冻结的前提下，提升情绪诊断的完整性与稳定性。

## 核心方法

### 方法参照系

传统 APO 流程通常由生成器产生候选提示，评估器打分，搜索器迭代更新。本文问题与该通用流程的关键差异在于：情绪诊断任务具有高上下文依赖性与多标签共病特性，要求优化过程不仅关注准确率，还需兼顾临床逻辑一致性与计算成本，且需在部分可观测状态下进行决策。

### 风险感知轨迹规划

Planner 智能体负责在 POMDP 框架下生成优化轨迹。设计动机在于解决通用 APO 缺乏全局规划导致的探索低效问题。Planner 根据初始提示 $p_0$ 与任务目标，生成包含 $n$ 个步骤的轨迹 $\mathbf{S_T} = \{st_1, \dots, st_n\}$，其中每个步骤 $st_i$ 对应一个子目标。该过程受风险阈值 $\gamma_{risk}$ 与成本阈值 $\gamma_{cost}$ 约束，确保优化路径不偏离临床安全边界且计算开销可控。

$$
\mathbf{S_T} = \arg\min_{\mathbf{S}} \left( \lambda \cdot L_{align}(\mathbf{S}, \mathbf{G}) + (1-\lambda) \cdot C_{cost}(\mathbf{S}) \right) \quad \text{s.t.} \quad R_{risk}(\mathbf{S}) \le \gamma_{risk}
$$

该公式表明 Planner 在最小化与子目标 $\mathbf{G}$ 的对齐损失及计算成本的同时，强制满足风险约束，从而生成结构化的优化路径。

### Socratic 联合策略精炼

Teacher-Critic-Student 三智能体沿 Planner 生成的轨迹执行提示精炼。设计动机在于解决静态提示无法动态适应复杂共病语义的问题。Teacher 提出苏格拉底式问题，Student 生成改进提示，Critic 评估逻辑正确性。若 Critic 判定为 [False]，则反馈修正建议，驱动 Teacher 重新提问。此过程形成伪梯度反馈，逐步细化提示中的角色设定、推理链与输出约束。

$$
p_{t+1} = \text{Student}(p_t, Q_t, F_t) \quad \text{where} \quad F_t = \begin{cases} \text{[True]} & \text{if } \text{Critic}(Q_t, p_t) = \text{Valid} \\ \text{[False]} + \text{Suggestion} & \text{otherwise} \end{cases}
$$

该机制通过多轮问答迭代，将模糊的初始指令转化为包含明确临床推理步骤的精细化提示，显著提升了模型对共病情绪的捕捉能力。

## 实验评估

实验在 DailyDialog、EmoryNLP、PELD、RECCON、EmotionX 及 DepressionEmo 六个数据集上进行，使用 GPT-5-mini、DeepSeek-V3 和 Qwen3-32B 作为骨干模型。基线包括原始提示、CoT（零样本/少样本）及 APE、ProTeGi、OPRO、PE2 等 SOTA APO 方法。

| 方法 | DailyDialog (M-F1/m-F1) | EmoryNLP (M-F1/m-F1) | DepressionEmo (M-F1/m-F1/EMR/PMA) | Avg. M-F1 | Avg. m-F1 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| OPRO (GPT-5-mini) | 43.95 / 60.95 | 45.25 / 62.55 | 44.83 / 62.03 / 24.28 / 86.75 | 45.25 | 62.55 |
| APOLO (GPT-5-mini) | 34.11 / 82.34 | 48.01 / 54.22 | 70.11 / 82.45 / 28.92 / 91.17 | 48.19 | 65.86 |
| APOLO (DeepSeek-V3) | 31.02 / 57.21 | 46.55 / 54.89 | 77.23 / 88.08 / 27.15 / 96.80 | 50.12 | 61.12 |

APOLO 在平均 Macro F1 上比最强基线 OPRO 提升 2.96%，在 Micro F1 上提升 3.40%。在 DepressionEmo 数据集上，APOLO 的 EMR 达到 28.92%，较 OPRO 的 24.28% 有显著提升，表明其在多标签共病识别上的优势。

消融实验显示，移除 Socratic 模块导致 Macro F1 平均下降 7.19%，Micro F1 下降 8.69%，是性能损失最大的组件。移除 Planner 导致 Macro F1 下降 3.75%，移除 Critic 导致下降 2.00%。这表明 Socratic 对话是提升诊断精度的核心机制，而 Planner 的结构化规划对优化效率至关重要。

评估边界方面，论文未报告置信区间，且不同骨干模型间的性能差异较大（如 DeepSeek-V3 的 Avg. m-F1 为 61.12%，低于 GPT-5-mini 的 65.86%），暗示模型能力对结果有显著影响。代码未公开，超参数（如温度 0.6、最大迭代 10 次）固定，限制了可复现性。

## 关联研究分析

从问题动机看，APOLO 与 MentalSeek-Dx 均旨在提升临床诊断的准确性，但路径截然不同。MentalSeek-Dx 通过微调模型权重并引入假设演绎推理链，直接增强模型内部的临床知识表示；而 APOLO 冻结模型权重，仅优化外部提示词。这种差异源于任务特性：MentalSeek-Dx 针对复杂共病诊断，需要深层语义理解，微调能更彻底地解决知识稀疏问题；APOLO 则侧重于在有限计算资源下快速适配新任务，提示优化提供了更轻量级的解决方案。然而，APOLO 未验证提示优化在极端知识缺失场景下是否优于微调，其性能上限可能受限于骨干模型的固有知识边界。

从方法设计看，APOLO 与 Empathy-R1 均涉及多智能体或迭代优化，但目标函数不同。Empathy-R1 使用强化学习优化共情生成，关注长文本中的情感一致性；APOLO 使用 Socratic 对话优化提示结构，关注单轮文本中的多标签准确性。Empathy-R1 的 RLHF 机制能捕捉动态情感变化，而 APOLO 的静态提示优化难以处理多轮对话中的状态追踪。这暗示 APOLO 更适用于静态筛查或单轮评估场景，而在需要动态交互的治疗联盟建立过程中，其提示优化策略可能无法替代基于强化学习的动态对齐方法。

## 总结

本文核心矛盾在于通用 APO 方法在情绪共病场景下的探索低效与诊断不稳定。APOLO 通过 POMDP 建模与多智能体协作，实现了风险感知下的提示动态精炼，在六个基准上取得了 SOTA 性能，其中 DepressionEmo 的 EMR 达 28.92%。其边界在于仅优化提示词而未改变模型权重，可能无法解决骨干模型临床知识稀疏的根本问题，且实验未包含与微调模型的直接对比。当骨干模型本身缺乏特定情绪类别的先验知识时，提示优化的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.13481)