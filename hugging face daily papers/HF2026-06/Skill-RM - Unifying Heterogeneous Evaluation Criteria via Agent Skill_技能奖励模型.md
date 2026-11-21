# HuggingFace最新推荐论文 ｜Skill-RM: Unifying Heterogeneous Evaluation Criteria via Agent Skill ｜技能奖励模型

研究机构：中山大学、香港中文大学

作者：Tao Chen、Gangwei Jiang、Pengyu Cheng 等 13 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.03980)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.03980)

> 奖励模型在处理数学、代码及代理任务时，需整合验证器、参考证据与检查清单等异构资源，但现有标量或扁平提示范式无法统一调度这些资源，导致评估过程不透明且缺乏灵活性。本文提出Skill-RM，将奖励计算重构为可复用的“奖励评估技能”执行过程，通过动态资源编排实现证据驱动的判断。该方法在多个基准上超越了同骨干的LLM-as-a-Judge基线，但其优势是否源于技能编排本身而非资源可用性，仍需更严格的消融验证。

## 研究背景

当LLM生成代码或数学解答时，奖励模型（Reward Model, RM）需判断其正确性。传统标量RM仅输出单一分数，无法区分“格式错误”与“逻辑错误”，也无法调用外部验证器执行代码。这种黑盒评分在复杂任务中失效，促使研究者引入LLM-as-a-Judge，通过自然语言推理生成判断。然而，LLM-as-a-Judge通常采用扁平提示，将评分标准、参考答案和工具说明堆砌在单一Prompt中，导致上下文噪声大，且无法根据输入动态选择所需资源。

现有生成式奖励模型（Generative Reward Model, GRM）和基于评分量表的系统虽提升了可解释性，但多聚焦于单一资源模态，如仅使用评分量表或仅调用工具，缺乏统一框架整合异构证据。本文切入点在于引入“Agent Skill”概念，将奖励评估视为一个可执行的技能包，包含程序化规范和资源库，使奖励计算从被动吸收上下文转为主动编排资源。

## 核心方法

### 方法参照系

本文问题属于生成式/Rubric RM路线，但关键差异在于：传统Rubric RM将标准硬编码在Prompt中，而Skill-RM将标准外化为可加载的资源包，通过技能规范动态选择资源，而非全量注入。

### 奖励评估技能定义

Skill-RM将奖励评估实例化为可复用的技能 $\mathcal{S}_{RM} = (\mathcal{M}_{RM}, \mathcal{U}_{RM})$，其中 $\mathcal{M}_{RM}$ 是程序化技能规范，$\mathcal{U}_{RM}$ 是资源库。$\mathcal{M}_{RM}$ 定义评估标准、资源调用协议、证据收集模式及输出契约。这一设计动机在于解决扁平提示中资源选择与证据追踪隐式化的问题，通过显式协议确保仅任务相关资源被激活，减少上下文噪声。

### 技能中介判断与奖励读出

给定提示 $\mathbf{x}$ 和候选响应 $\mathbf{Y}$，LLM Judge $\pi_\phi$ 执行技能，生成动作-观察轨迹 $\tau = \{(a_t, o_t)\}_{t=1}^T$。对每个标准 $c_m$，Judge生成局部证据项 $e_m = (q_m, s_m)$，其中 $q_m$ 是来自资源的观察，$s_m$ 是局部评估。最终结构化判断 $z = (d, \mathcal{E})$ 包含决策字段 $d$ 和证据集 $\mathcal{E}$。奖励输出通过确定性读出函数 $\mathcal{A}(\cdot)$ 从 $z$ 映射：

$$
r = \mathcal{A}(z)
$$

该公式将结构化判断投影到任务所需的奖励空间，确保奖励可追溯至具体证据。这一创新解决了传统RM中奖励与证据脱节的问题，使评估过程可审计且实例自适应。

## 实验评估

实验在RewardBench2、RM-Bench和JudgeBench上评估，基线覆盖标量RM、生成式RM、Rubric系统及Agentic Judge，但缺失因果去偏RM（如InfoRM）对比。

| 方法 | RewardBench2 | RM-Bench | JudgeBench | Avg. |
| :--- | :--- | :--- | :--- | :--- |
| Qwen3.5-27B Baseline | 81.1 | 89.8 | 80.8 | 83.9 |
| Skill-RM (Qwen3.5-27B) | 85.0 | 91.5 | 82.1 | 86.2 |
| Skill-RM + sample-spec. | 86.0 | 91.5 | 89.7 | 89.1 |

Skill-RM在平均准确率上较基线提升2.3个百分点，挂载样本特定资源后进一步提升至89.1%。

| 方法 | RewardBench2 | RM-Bench | JudgeBench | Avg. | Δ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Baseline | 81.1 | 89.8 | 80.8 | 83.9 | 0.0 |
| + appended resources | 77.7 | 86.3 | 78.9 | 81.0 | -2.9 |
| + Python tool | 82.7 | 88.7 | 79.5 | 83.6 | -0.3 |
| Skill-RM | 85.0 | 91.5 | 82.1 | 86.2 | +2.3 |
| Skill-RM + sample-spec. | 86.0 | 91.5 | 89.7 | 89.1 | +5.2 |

消融显示，直接附加资源导致平均准确率下降2.9个百分点，而Skill-RM提升2.3个百分点，表明增益源于技能编排而非资源可用性。

评估边界方面，论文未报告计算延迟，且JudgeBench上Skill-RM（82.1%）低于OpenRS（93.1%），暗示其在纯正确性任务上可能过度复杂化。代码已开源，但资源库构建细节仅在附录中简要说明，可复现性依赖外部资源的一致性。

## 关联研究分析

从方法设计看，Skill-RM与CAMEL（2026）代表两条路径：CAMEL侧重内部置信度门控，Skill-RM侧重外部资源编排。CAMEL在RewardBench2上达82.9%，Skill-RM达85.0%，但CAMEL未处理异构资源整合，而Skill-RM通过技能规范统一调度。这一差异源于任务特性：CAMEL针对通用对话，Skill-RM针对资源依赖任务。

从问题动机看，Skill-RM与InfoRM（2025）形成互补：InfoRM通过信息瓶颈过滤虚假特征，Skill-RM通过证据链隐式去偏。InfoRM未处理资源依赖判断，而Skill-RM未提供针对长度偏差的专项消融。证据链机制是否足以替代显式因果去偏，特别是在长文本场景下，论文未给出回答。

## 总结

Skill-RM旨在解决奖励模型整合异构评估资源的碎片化问题，通过引入Agent Skill范式，将奖励计算重构为可执行的技能过程，实现动态资源编排与证据驱动判断。实验显示，Skill-RM在平均准确率上较基线提升2.3个百分点，挂载样本特定资源后达89.1%。其边界在于JudgeBench上低于OpenRS，且未报告计算延迟，暗示其在纯正确性任务上可能过度复杂化。当支持集增大时，技能编排的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.03980)