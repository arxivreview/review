# ICLR2026最新论文 ｜CRITIQUE-CODER: ENHANCING CODER MODELS BY CRITIQUE REINFORCEMENT LEARNING ｜批判强化学习

研究机构：加拿大滑铁卢大学、加拿大向量研究所

作者：Chi Ruan、Dongfu Jiang、Yubo Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_10167755)

> 代码生成模型在标准强化学习（RL）训练中缺乏对错误解的反思机制，导致推理深度受限。现有RLVR范式仅奖励最终解的正确性，无法激励模型识别中间步骤的逻辑缺陷。本文提出CRL，通过奖励模型对“问题-解”对的二元判断准确性，显式引入批判机制。该范式在4B/8B小模型上显著提升了LiveCodeBench等基准的性能，但二元奖励的粒度是否足以捕捉复杂逻辑错误仍存疑。

## 研究背景

当模型面对复杂编程任务时，标准RLVR（Reinforcement Learning with Verifiable Reward）通过执行测试用例生成奖励信号，驱动策略优化。然而，这种基于最终结果的反馈机制存在盲区：模型可能通过模式匹配生成看似正确实则逻辑脆弱的代码，且无法从错误解中汲取教训。为弥补这一缺陷，研究界尝试引入批判机制，如CFT（Critique-Fine-Tuning）通过监督学习让模型学习教师提供的批判轨迹，但其依赖外部标注且未与RL优化闭环结合。

代码生成领域的评估正从静态基准向动态、仓库级任务转移，LiveCodeBench等基准要求模型具备深层逻辑推理与自我修正能力。主流RL方法如DeepCoder虽通过长上下文训练提升了推理链长度，但仍未解决“如何激励模型主动反思”的问题。本文切入点在于将批判行为本身作为RL的奖励目标，而非仅作为辅助监督信号，旨在通过内在激励机制提升模型的批判性思维与代码生成质量。

## 核心方法

### 标准RLVR参照系

标准RLVR流程中，策略模型$\pi_\theta$针对问题$q$采样$n$个解$\{s_i\}$，每个解在测试集$T$上执行，通过通过率计算奖励$R_{rl,i}$。该流程的关键差异在于：奖励仅反映解的最终正确性，未涉及对解本身质量的评估或反思，导致模型缺乏对错误模式的识别能力。

### 批判强化学习（CRL）机制

CRL在标准RLVR基础上引入二元判断奖励。给定问题-解对$[q; s]$，模型生成$n$个判断$c_i \in \{True, False\}$，奖励$R_{crl,i}$定义为$c_i$与真实标签$c^*$的匹配度：

$$
R_{crl,i} = \mathbb{1}[c_i = c^*]
$$

该公式的物理含义是：模型仅当正确判断解的可行性时获得奖励，迫使模型在生成解的同时发展批判性评估能力。设计动机在于解决标准RLVR中“模型无法从错误解中学习”的失效问题，通过显式奖励批判准确性，引导模型关注逻辑缺陷而非仅结果正确性。

### 混合训练与GRPO优化

CRL与标准RLVR通过混合数据训练整合：20%数据用于CRL（问题-解对+判断标签），80%用于RLVR（问题+测试用例）。两种奖励信号在GRPO（Group Relative Policy Optimization）中联合优化，优势估计$A_{\hat{i},t}$同时受任务结果与批判指导影响：

$$
A_{\hat{i},t} = \frac{R_i - \text{mean}(R_{\text{group}})}{\text{std}(R_{\text{group}})}
$$

其中$R_i$为CRL或RLVR奖励。该设计确保模型在生成解（RLVR）与评估解（CRL）间平衡，避免纯CRL导致的“判断偏好”偏差。迭代上下文扩展（16k→32k tokens）进一步支持长推理链，使批判机制在复杂任务中有效运作。

## 实验评估

实验基于Qwen3-4B/8B模型，在EvalPlus、BigCodeBench-I、Aider-Polyglot、LiveCodeBench v5上评估。基线覆盖Qwen3基线、RL-only模型、DeepCoder-14B、GPT-o1，但缺失其他CRL变体或纯监督批判模型对比。主结果显示CRITIQUE-CODER-4B在LiveCodeBench v5达59.0（+4.8 vs 基线），8B达60.8（+3.3 vs 基线），超越DeepCoder-14B（60.6）但低于GPT-o1（59.5，注：GPT-o1在LiveCodeBench v5为59.5，本文8B 60.8略超）。

| 模型 | EvalPlus | BigCodeBench-I Full | Aider-Polyglot | LiveCodeBench v5 | AVG |
|---|---|---|---|---|---|
| Qwen3-4B (Baseline) | 85.2 | 42.0 | 21.8 | 54.2 | 44.8 |
| Qwen3-4B-RL | 84.9 | 40.6 | 23.6 | 56.6 | 45.7 |
| CRITIQUE-CODER-4B | 86.5 | 43.1 | 24.4 | 59.0 | 47.2 |
| Qwen3-8B (Baseline) | 85.8 | 44.6 | 28.4 | 57.5 | 48.0 |
| Qwen3-8B-RL | 86.2 | 44.5 | 34.5 | 59.6 | 49.8 |
| CRITIQUE-CODER-8B | 87.7 | 46.6 | 35.6 | 60.8 | 51.5 |

消融实验验证CRL比例影响：20% CRL数据最优（AVG 47.2），50%时BigCodeBench-I Hard下降（22.3 vs 23.0），100% CRL导致性能显著退化（AVG 44.5）。这表明CRL作为补充而非替代RLVR，过度依赖批判数据会削弱解生成能力。

评估边界：未报告置信区间，LiveCodeBench v5时间窗口（2024.10–2025.02）可能引入数据污染风险；代码开源但超参数细节（如GRPO学习率）未完整披露，可复现性受限。

## 关联研究分析

从问题动机看，CRL与CFT均针对模型缺乏批判能力，但CFT依赖教师标注的批判轨迹，而CRL通过RL奖励自我生成判断，避免了外部标注成本。差异根源在于任务特性：CFT适用于有高质量批判数据场景，CRL更适合数据稀缺但可执行验证的代码任务。CRL的二元奖励是否足以捕捉细粒度逻辑错误（如边界条件缺陷），论文未提供细粒度错误分析。

从方法设计看，CRL与DeepCoder同属RL驱动的代码推理增强，但DeepCoder侧重长上下文训练，CRL引入批判机制。DeepCoder未解决“模型为何生成错误解”的问题，CRL通过奖励判断准确性间接提升推理深度。CRL在低资源语言或安全代码领域的泛化性未验证，批判机制是否加剧模型对特定代码风格的偏好，需进一步实验。

## 总结

本文核心矛盾是标准RLVR缺乏对错误解的反思激励，导致模型推理深度受限。切入点在于将批判行为作为RL奖励目标，通过二元判断准确性显式激励模型发展批判性思维。方法上，CRL与RLVR混合训练，GRPO联合优化，迭代扩展上下文。实验证明CRITIQUE-CODER-4B在LiveCodeBench v5达59.0（+4.8 vs 基线），8B达60.8，超越DeepCoder-14B。边界在于二元奖励粒度有限，未验证细粒度逻辑错误捕捉能力，且小模型提升能否外推至大模型未明确。当CRL比例超过20%时性能退化，批判机制与解生成能力的平衡点是否随模型规模变化，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_10167755)