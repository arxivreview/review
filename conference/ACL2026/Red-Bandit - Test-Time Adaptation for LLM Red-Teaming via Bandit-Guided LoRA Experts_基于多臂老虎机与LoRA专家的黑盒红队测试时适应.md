# ACL2026最新论文 ｜Red-Bandit: Test-Time Adaptation for LLM Red-Teaming via Bandit-Guided LoRA Experts ｜基于多臂老虎机与LoRA专家的黑盒红队测试时适应

研究机构：英国帝国理工学院

作者：Christos Ziakas、Nicholas Loo、Nishita Jain 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.07239)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cc33e1f6ce17)

> 自动化红队测试旨在以规模化手段替代高成本人工审计，以探测大语言模型（LLM）的安全边界。现有强化学习（RL）攻击方法虽能生成高毒性提示，但受限于单一策略优化导致的模式坍塌，且缺乏在测试时针对特定目标模型漏洞进行动态适应的能力。Red-Bandit 通过训练多个风格特化的 LoRA 专家，并在推理阶段利用多臂老虎机（Multi-Armed Bandit, MAB）动态路由，实现了黑盒环境下的测试时适应。该方法在保持极低提示困惑度的同时提升了攻击成功率，但其收益高度依赖查询预算，且未验证在强对齐前沿模型上的泛化性。

## 研究背景

理解 Red-Bandit 需厘清黑盒红队测试中的两个核心约束：查询效率与策略多样性。在黑盒场景下，攻击者无法获取目标模型的梯度或对数概率，只能依赖模型响应进行反馈。传统迭代搜索方法（如 PAIR）虽具备测试时适应性，但查询成本极高；而基于 RL 的静态生成方法（如 AdvPrompter）虽查询效率高，却因奖励信号稀疏易陷入模式坍塌，即仅生成少量高奖励但重复的提示风格，无法覆盖目标模型多样化的失效模式。

自动化红队测试的演进路径反映了从“静态映射”到“动态博弈”的重构。早期工作如 GCG 依赖白盒梯度优化对抗后缀，虽高效但难以迁移至闭源模型。随着前沿模型对单轮静态攻击鲁棒性的提升，研究重心转向黑盒环境下的自适应策略。Rainbow Teaming 将红队测试建模为质量多样性（Quality-Diversity, QD）搜索，通过维护提示词档案优化攻击质量与多样性，解决了单一目标优化导致的分布收窄问题。然而，QD 搜索仍需大量离线计算，且未解决测试时针对特定模型漏洞的动态选择问题。Red-Bandit 的切入点在于：将攻击风格视为离散动作空间，利用 MAB 在推理阶段实时平衡探索（风格多样性）与利用（攻击成功），从而在无需重新训练的前提下实现模型特异性漏洞挖掘。

## 核心方法

### 方法参照系

Red-Bandit 属于强化学习攻击生成路线，其标准流程为：定义奖励函数 → RL 优化单一攻击策略 → 生成对抗提示。本文的关键差异在于将“单一策略优化”解耦为“多专家并行训练 + 测试时离散选择”，并将奖励信号从响应级降级为提示级规则奖励，以适配黑盒约束。

### 风格特化 LoRA 专家训练

传统 RL 攻击方法在单一策略下优化毒性奖励，易导致生成提示的风格单一化。Red-Bandit 采用 Group Relative Policy Optimization (GRPO) 变体，针对 Rainbow Teaming 定义的 10 种攻击风格（如角色扮演、俚语、历史场景等）分别训练独立的 LoRA 专家。每个专家通过上下文条件化生成特定风格的对抗指令，其损失函数为：

$$
L_\theta = -\mathbb{E}_{\pi_\theta} \left[ \min \left( r_\theta \hat{A}, \text{clip}(r_\theta, 1-\epsilon, 1+\epsilon) \hat{A} \right) \right]
$$

其中 $\hat{A} = R(x, y) - \frac{1}{G}\sum_{j=1}^{G} R(x, y_j)$ 为组内相对优势估计，$R(x, y)$ 为基于 Llama Guard 的提示级安全奖励。该设计动机在于：通过架构解耦强制保留风格多样性，避免单一策略优化导致的模式坍塌，同时提示级奖励无需查询目标模型，显著降低了训练成本。

### 多臂老虎机引导的测试时适应

在推理阶段，Red-Bandit 将每个 LoRA 专家视为 MAB 中的一个臂（Arm）。目标模型对生成提示的响应安全性由规则模型评估，作为选择该臂的奖励信号。采用 Upper Confidence Bound (UCB) 算法选择动作，其选择准则为：

$$
a_t = \arg\max_{a \in \mathcal{A}} \left( \hat{\mu}_a + c \sqrt{\frac{\ln t}{N_a(t)}} \right)
$$

其中 $\hat{\mu}_a$ 为臂 $a$ 的经验平均奖励，$N_a(t)$ 为截至时刻 $t$ 臂 $a$ 被选择的次数，$c$ 为探索系数。该公式通过置信区间宽度动态平衡探索与利用：对采样较少的臂给予更宽的置信区间以鼓励探索，对高奖励臂则倾向于利用。这一机制解决了静态迁移方法（如 Atoxia）无法识别目标模型特异性漏洞的问题，实现了测试时自适应。

## 实验评估

实验在 AdvBench（520 条有害指令）和 HarmBench 上进行，基线包括 GCG、AutoDAN、AdvPrompter 和 Atoxia。基线覆盖白盒、灰盒及黑盒迁移路线，但缺失 Rainbow Teaming 等 QD 类基线及多轮对话基线。

| 目标模型 | 方法 | ASR@1 (%) | ASR@10 (%) | PPL |
| :--- | :--- | :--- | :--- | :--- |
| Mistral-7B | Atoxia | 73.1 | 99.2 | 54.42 |
| Mistral-7B | Red-Bandit (UCB) | 70.2 | 100.0 | 2.31 |
| Vicuna-7B | Atoxia | 82.7 | 92.3 | 4.53 |
| Vicuna-7B | Red-Bandit (UCB) | 63.5 | 100.0 | 2.37 |
| Llama2-7B | Atoxia | 18.3 | 41.4 | 5.80 |
| Llama2-7B | Red-Bandit (UCB) | 33.7 | 99.0 | 2.40 |

Red-Bandit 在 ASR@10 上全面超越基线，且在 Mistral-7B 和 Vicuna-7B 上达到 100.0%。其困惑度（PPL）显著低于 Atoxia（2.31 vs 54.42），验证了低困惑度攻击在规避统计特征防御上的有效性。然而，在 ASR@1 上，Red-Bandit 在 Mistral-7B 和 Vicuna-7B 上低于 Atoxia，反映了 MAB 在单次尝试中探索不足导致的利用效率损失。

| 变体 | ASR@1 (KM) | H_norm | PPL |
| :--- | :--- | :--- | :--- |
| Baseline (No RL, No Bandit) | 38.5 | 0.98 | 2.45 |
| Red-Bandit (No RL) | 50.9 | 0.65 | 2.22 |
| Red-Bandit (No Bandit) | 55.8 | 0.98 | 2.65 |
| Red-Bandit (RL + Bandit) | 58.7 | 0.67 | 2.62 |

消融实验显示，RL 后训练与 MAB 组件均对性能有正向贡献。去除 RL 后 ASR 下降 7.8%，去除 MAB 后下降 2.9%，表明 RL 对基础攻击能力的提升大于 MAB 的边际收益。风格熵（H_norm）在引入 MAB 后从 0.98 降至 0.67，证实了 MAB 在收敛过程中牺牲部分多样性以换取攻击成功率。

评估协议采用关键词匹配（AdvBench）和 HarmBench-cls 分类器（HarmBench），与训练奖励模型（Llama Guard）独立，避免了结果膨胀。但论文未报告置信区间，且未提供代码 URL，可复现性受限。HarmBench 实验仅对比了 Llama-3.1-8B 和 Qwen3-8B，未覆盖 GPT-4 等强对齐前沿模型，限制了结论的泛化性。

## 关联研究分析

从问题动机看，Red-Bandit 与 Rainbow Teaming 均关注攻击多样性，但解决路径截然不同。Rainbow Teaming 通过 QD 搜索在离线阶段维护提示词档案，优化质量与多样性的帕累托前沿；Red-Bandit 则通过架构解耦将多样性内化于 LoRA 专家库，并在测试时通过 MAB 动态选择。这一差异源于任务约束：Rainbow Teaming 假设可获取大量离线计算资源，而 Red-Bandit 聚焦黑盒查询效率，将多样性维护从搜索过程转移至模型参数空间。Red-Bandit 的 MAB 路由机制本质上是一种后验硬路由混合专家（Mixture-of-Experts）架构，其优势在于推理时的低延迟与低查询成本，但劣势在于风格空间固定，无法自动发现新风格。

从方法设计看，Red-Bandit 与 Atoxia 均属于黑盒攻击方法，但适应机制存在本质差异。Atoxia 依赖提示迁移性，即在源模型上优化后直接应用于目标模型，缺乏测试时反馈；Red-Bandit 通过 MAB 实时接收目标模型响应反馈，动态调整风格选择。这一差异导致 Red-Bandit 在 ASR@10 上显著优于 Atoxia（如 Llama2-7B 上 99.0% vs 41.4%），但在 ASR@1 上可能因探索开销而落后。这种权衡反映了测试时适应的固有成本：动态选择需要多次查询以收敛策略，而静态迁移则依赖预训练阶段的泛化能力。Red-Bandit 未探索如何进一步压缩 MAB 的收敛查询数，这在查询预算严格受限的场景下可能成为瓶颈。

## 总结

Red-Bandit 旨在解决黑盒红队测试中静态生成方法缺乏模型特异性适应性的矛盾。其切入点在于将攻击风格解耦为独立 LoRA 专家，并利用 MAB 在测试时动态路由，从而在无需重新训练的前提下实现漏洞挖掘。该方法在 AdvBench 上实现了 100.0% 的 ASR@10 和 2.31 的极低困惑度，证明了风格特化与动态选择的有效性。然而，其 ASR@1 性能低于静态迁移基线，且风格空间固定于 10 类预定义类别，无法适应未知攻击模式。当目标模型对特定风格具有强鲁棒性时，MAB 的探索效率是否会因奖励稀疏而显著下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_cc33e1f6ce17)