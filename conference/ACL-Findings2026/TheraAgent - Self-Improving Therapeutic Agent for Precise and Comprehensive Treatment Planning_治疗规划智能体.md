# ACL-Findings2026最新论文 ｜TheraAgent: Self-Improving Therapeutic Agent for Precise and Comprehensive Treatment Planning ｜治疗规划智能体

研究机构：清华大学、新加坡国立大学

作者：Junkai Li、Yunghwei Lai、Tianyi Zhu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.05963)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.05963)

> 导读 临床治疗规划要求将诊断结论转化为具体、安全且完整的用药方案，但现有大语言模型（LLM）依赖单次生成，常导致剂量错误、覆盖不全或安全隐患。本文指出单次生成缺乏显式验证机制是核心瓶颈，提出 TheraAgent 框架，通过“生成-反思-精炼”的迭代闭环与临床对齐的 TheraJudge 评估模块实现自我纠错。该框架在 HealthBench 治疗子集上取得 48.94 分，并在专家盲评中以 86% 胜率超越人类医生，但其高计算成本与对骨干模型推理能力的依赖仍存疑。

## 研究背景

治疗规划不同于静态问答，其动作空间是开放且组合式的，必须同时满足精准用药、全面覆盖与风险控制等多维临床约束。单一 LLM 的直接输出往往缺乏对个体化指标（如炎症标志物、影像学特征）的细粒度整合，导致方案粗糙且存在潜在风险。这种“一次性预测”模式无法捕捉临床实践中常见的迭代修正过程，即医生需根据初步方案的缺陷进行反思与调整。

当前 LLM 医疗应用研究多聚焦于诊断任务，治疗规划领域存在显著空白。现有方法如 MedPlan 侧重工作流对齐，TxAgent 依赖特定疾病微调，均缺乏通用的迭代精炼机制。同时，评估体系多依赖 BLEU 或粗粒度 LLM 评分，无法捕捉治疗计划的多维临床质量。TheraAgent 的切入点在于将治疗规划重构为推理时扩展（Inference-time scaling）问题，通过内部批评者提供密集反馈信号，替代传统的训练时优化或外部多智能体协作。

## 核心方法

### 方法参照系

本文问题可置于自改进智能体（Self-improving Agent）框架下，其标准流程为“生成-评估-更新”。与通用反思框架（如 Reflexion）的关键差异在于，治疗规划需评估器具备临床维度对齐能力，且记忆机制需支持基于评分的检索以指导后续生成。

### 迭代生成与记忆检索

Planner 在迭代 $k$ 时，不仅依赖患者病例 $\mathbf{P}$，还从 Memorizer 中检索 Top-N 高分历史方案作为上下文。这一设计解决了单次生成中缺乏历史错误修正信号的问题，使模型能针对前序迭代的具体缺陷（如剂量不足）进行定向优化。

$$ \mathbf{T}_k, \mathbf{c}_k = f_\theta(\mathbf{P}, M_{[k-1]}) $$

其中 $M_{[k-1]}$ 为前 $k-1$ 次迭代的记忆状态，包含方案、理由与评分。通过条件化于历史反馈，Planner 将治疗规划转化为渐进优化过程，避免了从零开始生成的随机性。

### 临床对齐的多维评估

TheraJudge 作为内部批评者，对方案 $\mathbf{T}_k$ 进行多维评分，输出理由 $\mathbf{R}_k$ 与聚合分数 $\mathbf{s}_k$。其核心创新在于结合 RAG 检索权威指南与 Few-shot 临床范例，确保评分稳定性与事实准确性。

$$ \mathbf{R}_k, \mathbf{s}_k = g_\phi(\mathbf{P}, \mathbf{T}_k) $$

该公式表明评分是患者上下文与候选方案的联合函数。TheraJudge 的评分不仅用于选择最终方案，更作为 Memorizer 的更新信号，形成“生成-评估-记忆-再生成”的闭环。这种结构化反馈替代了模糊的整体评分，使 Planner 能明确识别需改进的具体维度（如 Harm Control）。

## 实验评估

TheraAgent 在 HealthBench 治疗子集（1,241 例）上评估，基线覆盖开源（DeepSeek-R1, Kimi-K2）与闭源（GPT-4o, Claude-4-Sonnet）模型，但缺失多智能体协作基线（如 MedCoAct）。

| 模型 | Overall | Hedging | Completeness | Context Seeking |
| :--- | :--- | :--- | :--- | :--- |
| Claude-4-Sonnet | 44.28 | 41.97 | 40.85 | 38.85 |
| DeepSeek-R1 | 42.94 | 41.89 | 48.16 | 41.56 |
| TheraAgent | **48.94** | **48.75** | **51.72** | **44.65** |

TheraAgent 整体得分 48.94，较次优模型高 4.66 分，在 Completeness 和 Context Seeking 维度优势显著。

| 组件配置 | HealthBench Score |
| :--- | :--- |
| Base Model w/o Judge | 41.15 |
| Fewshots Only | 50.62 |
| RAG Only | 45.98 |
| Fewshots + RAG | 45.96 |
| Fewshots + Dimensional Scoring | **52.36** |

消融实验显示，Few-shot 范例对评分稳定性贡献最大（50.62），而 RAG 单独使用效果有限（45.98），甚至与 Few-shot 结合时性能下降（45.96），表明指南异质性可能干扰评估。最佳配置为 Few-shot 与多维评分结合（52.36），验证了结构化反馈优于单一整体评分。

评估边界方面，HealthBench 评分与专家评分的相关性（Pearson 0.71）虽高，但样本量有限（35 例）。TheraAgent 计算成本显著，10 次迭代需 87,005 tokens 与 753.5 秒，相对成本达 64.1 倍。代码未公开，超参数（如 Top-N=3, τ=98）依赖特定骨干模型（DeepSeek-R1），可复现性受限于模型访问权限。

## 关联研究分析

从问题动机看，TheraAgent 与 MedCoAct 等多智能体协作框架形成鲜明对比。MedCoAct 通过角色分工与置信度感知解决“共识陷阱”，但计算开销大且依赖外部专家模拟；TheraAgent 采用单智能体自改进，通过内部记忆与反思实现类似效果，避免了多智能体通信开销。这一差异源于任务特性：治疗规划更依赖个体化数据的细粒度整合，而非多视角辩论，单智能体迭代可能更高效。

从方法设计看，TheraAgent 与 Process-Supervised MARL 均关注过程监督，但路径不同。后者通过强化学习优化训练策略，解决奖励稀疏问题；前者通过推理时扩展，利用 TheraJudge 提供密集反馈信号。TheraAgent 的优势在于无需大规模标注数据与训练成本，但劣势是推理延迟高。这种取舍暗示，在数据稀缺或部署资源受限场景下，推理时优化可能比训练时优化更具实用性，但论文未验证其在小模型上的泛化能力。

## 总结

TheraAgent 针对治疗规划中单次生成缺乏验证机制的核心矛盾，提出迭代生成-反思-精炼框架，通过 TheraJudge 提供临床对齐的多维反馈，实现了自我纠错。实验证明其在 HealthBench 上取得 48.94 分 SOTA，并在专家盲评中以 86% 胜率超越人类医生。然而，其高计算成本（64.1 倍相对成本）与对 DeepSeek-R1 强推理能力的依赖，限制了其在资源受限场景的部署。当骨干模型替换为较小规模模型时，TheraJudge 的反馈信号是否仍能驱动有效迭代，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.05963)