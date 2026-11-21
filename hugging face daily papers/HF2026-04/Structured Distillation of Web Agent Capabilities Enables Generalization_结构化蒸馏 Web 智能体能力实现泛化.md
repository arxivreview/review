# HuggingFace最新推荐论文 ｜Structured Distillation of Web Agent Capabilities Enables Generalization ｜结构化蒸馏 Web 智能体能力实现泛化

研究机构：加拿大麦吉尔大学

作者：Xing Han Lù、Siva Reddy

论文原文见 [arXiv](https://arxiv.org/abs/2604.07776)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07776)

> 前沿大模型在 Web 任务上表现优异，但高昂的 API 成本与数据隐私风险阻碍了本地部署，而小参数开源模型存在显著的能力缺口。现有合成数据管线缺乏统一框架，导致不同方法难以系统性比较，且往往陷入“规模扩张”而非“质量提升”的误区。本文提出 AGENT-AS-ANNOTATORS 框架，将人工标注角色映射为 LLM 模块，通过高质量轨迹蒸馏使 9B 模型超越部分前沿闭源模型。该框架验证了“质量优于数量”的假设，但其泛化边界与教师模型选择的普适性仍存疑。

## 研究背景

Web 智能体在开放网络环境中执行多步任务时，面临感知接地与规划鲁棒性的耦合挑战。感知接地要求将自然语言指令准确映射到 DOM 节点或像素坐标，而规划鲁棒性依赖对历史状态的准确记忆。当智能体无法精确定位元素或遗忘早期步骤时，后续动作必然失效，导致长程任务成功率随步骤数增加而急剧下降。解决这一问题的关键在于构建具备长期记忆与可解释规划的自主决策系统，但现有模型在动态噪声与对抗性环境下的脆弱性尚未得到根本解决。

当前领域正从单纯追求任务成功率转向鲁棒性、安全性与可解释性的系统平衡。主流路线包括基于规则脚本的早期方法、ReAct 框架确立的推理-行动交替范式，以及多模态大模型引入后的视觉接地优化。然而，这些方法多依赖封闭合成环境或半真实网络，长程任务中的上下文爆炸与“迷失在中间”现象暴露无遗。此外，提示注入等安全威胁使得智能体在真实网络中的自主性转化为安全风险。本文切入点在于通过结构化蒸馏，将前沿模型的能力迁移至小参数模型，以解决本地部署中的能力缺口问题。

## 核心方法

### 方法参照系

本文问题属于“数据合成”路线，标准流程为生成-过滤-训练。与 InSTA 等依赖规模扩张的方法不同，本文聚焦于通过角色映射提升轨迹质量，而非增加网站数量。关键差异在于引入 Persona Generator 与 Judge 模块，实现任务多样性与评估可靠性的双重优化。

### 角色映射与任务合成

传统合成数据管线中，任务设计、执行与验证由不同人工角色完成，但 LLM 管线缺乏统一框架。本文提出 AGENT-AS-ANNOTATORS，将 Task Designer、Annotator 与 Supervisor 映射为 Persona Generator、Agent 与 Judge。Persona Generator 生成多样化用户画像，诱导不同任务分布；Task Generator 基于画像探索环境，合成任务意图与评估提示。这一设计解决了此前方法中任务同质化与评估模糊的问题。

$$
\text{Task} = f_{\text{gen}}(\text{Persona}, \text{Env}) \quad \text{Hint} = g_{\text{eval}}(\text{Task}, \text{Env})
$$

该公式表示任务与提示由画像与环境共同决定，确保任务接地于真实实体而非幻觉。

### 轨迹过滤与质量验证

Agent 执行任务生成轨迹，Judge 基于交互记录与评估提示判断成功与否。Judge 采用“倒置”评估顺序，先检查循环、副作用与最优性，最后判断成功，以减少确认偏差。这一设计解决了此前 LLM-as-judge 方法中评估不可靠的问题，确保仅高质量轨迹用于训练。

$$
\text{Success} = h_{\text{judge}}(\text{Trajectory}, \text{Hint}) \quad \text{if } \text{Success} = \text{True} \rightarrow \text{Train}
$$

该公式表示仅当 Judge 判定成功时，轨迹才进入训练集，通过提示辅助提升评估准确性。

## 实验评估

实验在 WebArena、VisualWebArena、WorkArena L1/L2 与 MiniWoB 上进行，基线覆盖 GPT-4o、Claude 3.5 Sonnet 等前沿模型及 Qwen3.5 系列开源模型。本文方法在 WebArena 上取得 41.5% 成功率，超越 GPT-4o (31.5%) 与 Claude 3.5 Sonnet (36.0%)，并在 WorkArena L1 上实现 +18.2pp 提升，验证了跨环境泛化能力。

| 基准 | A3-Qwen3.5-9B | GPT-4o | Claude 3.5 Sonnet | Qwen3.5-9B (base) |
| :--- | :--- | :--- | :--- | :--- |
| WebArena | 41.5 | 31.5 | 36.0 | 31.0 |
| WorkArena L1 | 51.5 | 45.5 | 56.4 | 33.3 |
| MiniWoB | 69.0 | 63.8 | 69.8 | 63.2 |

消融实验显示，移除 Judge 过滤导致成功率下降 4.5pp，移除推理轨迹下降 7.9pp，验证了质量过滤与推理完整性的重要性。教师模型质量比数据量更关键：Gemini 3 Pro (reduced thinking) 产生 16,353 个高质量样本，成功率 69–85%，而 Gemini 3 Flash 产生 22,707 个低质量样本，成功率仅 17–53%。

评估边界在于：本文仅使用 SFT，未结合 RL，可能限制模型在复杂任务中的进一步优化；教师模型比较限于 Gemini 系列，未测试其他家族；Judge 的假阳性率未与人工标注对比，评估可靠性存疑。

## 关联研究分析

从问题动机看，本文与 InSTA 同属数据合成路线，但 InSTA 依赖 150K 网站规模扩张，本文聚焦 6 环境+Persona 质量提升。这一差异源于任务特性：InSTA 假设多样性来自环境广度，本文假设多样性来自用户画像深度。若环境覆盖不足，Persona 机制是否仍能维持泛化能力，论文未给出回答。

从方法设计看，本文与 Go-Browse 同属轨迹合成框架，但 Go-Browse 使用 VLM 可行性检查，本文使用 LLM Judge+Hint。这一差异源于评估可靠性：VLM 检查依赖视觉理解，LLM Judge+Hint 依赖语义理解与结构化提示。在视觉接地任务中，VLM 检查是否更优，论文未进行直接对比。

## 总结

本文要解决的核心矛盾是前沿模型能力与小模型本地部署需求之间的缺口。现有方法依赖规模扩张或单一评估，本文通过角色映射与质量过滤，实现高质量轨迹蒸馏。实验证明 9B 模型在 WebArena 上超越 GPT-4o 与 Claude 3.5 Sonnet，并在 WorkArena L1 上实现 +18.2pp 提升。本文边界在于仅使用 SFT、教师模型比较局限及 Judge 可靠性未验证。当环境覆盖扩展至 100K 网站时，Persona 机制的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07776)