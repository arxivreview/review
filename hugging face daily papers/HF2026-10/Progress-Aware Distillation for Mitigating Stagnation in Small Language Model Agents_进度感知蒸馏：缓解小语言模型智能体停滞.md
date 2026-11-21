# HuggingFace最新推荐论文 ｜Progress-Aware Distillation for Mitigating Stagnation in Small Language Model Agents ｜进度感知蒸馏：缓解小语言模型智能体停滞

作者：Yuanpu Cao、Saket Sathe、Hanyu Wang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.19439)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.19439)

> 导读 小语言模型（Small Language Models, SLMs）在智能体蒸馏中面临长程交互下的“进度停滞”问题，即模型陷入重复无效动作的循环，无法从环境反馈中学习并推进任务。现有基于监督微调（Supervised Fine-Tuning, SFT）的蒸馏方法仅模仿教师轨迹，缺乏对学生生成轨迹中停滞行为的显式惩罚，导致SLM在复杂任务中性能显著低于教师模型。本文提出进度感知蒸馏（Progress-Aware Distillation, ProD）框架，通过量化学生与教师轨迹间的停滞差距，构建自适应边际（Adaptive Margin），在优化过程中动态惩罚停滞行为。该框架在多个SLM骨干上显著提升了任务成功率与完成效率，逼近教师模型性能。然而，停滞评分依赖启发式规则或LLM-as-judge，其鲁棒性在极端噪声环境下存疑。

## 研究背景

当智能体在长程任务中运行时，上下文窗口迅速被推理链与环境反馈（如噪声搜索结果、代码日志）填满。SLM受限于容量，难以从冗长且含噪的上下文中提取有效信号，导致其倾向于重复前几轮失败的策略，形成“进度停滞”。这一现象在SFT蒸馏中尤为突出，因为SFT仅最大化教师轨迹的似然，未对学生在推理时生成的停滞轨迹施加约束。

智能体蒸馏旨在将大模型（如GPT-4.1）的推理与工具调用能力迁移至SLM，以降低部署成本。主流路线依赖SFT进行行为克隆，但分析表明，随着轨迹长度增加和模型规模减小，停滞现象加剧，成为SLM智能体性能瓶颈。现有去重方法（如重复惩罚）仅在解码层抑制表面重复，无法解决轨迹级的策略停滞。本文切入点在于：在蒸馏优化阶段显式检测并惩罚学生轨迹中的停滞，通过自适应边际动态调整优化强度，使SLM习得教师打破停滞循环的能力。

## 核心方法

### 方法参照系：SFT智能体蒸馏

标准智能体蒸馏流程包括：收集教师成功轨迹，过滤后构建数据集，通过SFT训练学生模型。在CodeAct框架下，轨迹由Thought-Action-Observation三元组构成。SFT损失函数仅计算教师生成Token的对数似然，掩码环境观测。该流程使SLM掌握工具调用格式，但无法保证在长轨迹中维持有效探索，导致停滞。

### 停滞量化与自适应边际构建

为量化停滞，本文定义轮次级停滞评分 $S(h_i \oplus a_i) \in [0,1]$，基于词汇重叠（ROUGE-L）、语义相似度（余弦相似度）或LLM-as-judge。停滞评分越高，表示当前轮次与历史轮次越相似。设计动机在于：SFT无法区分“有效重复”与“无效停滞”，需显式度量停滞程度以指导优化。

本文定义轨迹级停滞差距 $\Delta S(\tilde{\tau}, \tau)$ 为学生与教师平均轮次停滞评分之差：

$$ \Delta S(\tilde{\tau}, \tau) := \frac{1}{L_{\tilde{\tau}}} \sum_{i=1}^{L_{\tilde{\tau}}} S(\tilde{h}_i \oplus \tilde{a}_i) - \frac{1}{L_{\tau}} \sum_{i=1}^{L_{\tau}} S(h_i \oplus a_i) $$

该公式衡量学生相对于教师的停滞严重程度。若 $\Delta S > 0$，表示学生比教师更停滞。

为动态调整惩罚强度，构建自适应边际 $f(\tilde{\tau}, \tau)$，结合停滞差距与答案正确性：

$$ f(\tilde{\tau}, \tau) = c_0 \left( \alpha \max\{0, \Delta S(\tilde{\tau}, \tau)\} + (1 - \alpha) \mathbb{I}[\text{Ans}(\tilde{\tau}) \neq \text{Ans}(\tau)] \right) $$

其中 $\alpha$ 平衡停滞与正确性贡献，$\mathbb{I}$ 为指示函数。该设计确保停滞严重且答案错误的轨迹获得最大边际，从而在优化中受到最强惩罚。

### 进度感知优化目标

ProD采用SimPO式偏好优化目标，利用学生自生成轨迹 $\tilde{\tau}$ 与教师轨迹 $\tau$ 构建对比损失：

$$ L_{\text{PRO}}(\theta) = -\mathbb{E}_{(x,\tau) \sim D, \tilde{\tau} \sim p_{\theta_0}^S(\cdot|x)} \left[ \log \sigma \left( \frac{\beta}{|\tau|} \log p_\theta^S(\tau|x) - \frac{\beta}{|\tilde{\tau}|} \log p_\theta^S(\tilde{\tau}|x) - f(\tilde{\tau}, \tau) \right) \right] $$

该公式通过自适应边际 $f(\tilde{\tau}, \tau)$ 动态缩放梯度信号：停滞严重的学生轨迹产生较大边际，迫使模型大幅降低其概率；接近教师行为的轨迹边际较小，避免过度修正。最终损失联合SFT损失 $L(\theta) = L_{\text{PRO}}(\theta) + \lambda L_{\text{SFT}}(\theta)$，防止似然位移，保留教师轨迹的高概率。

## 实验评估

实验在MATH和HotpotQA（域内）及Omni-MATH（域外）上进行，评估8个SLM（0.6B-8B）。基线包括基础SLM、SFT蒸馏、重复惩罚（RP）和简洁SFT。ProD在域内和域外任务上均显著优于SFT，接近GPT-4.1教师性能。

| 模型 | 方法 | MATH | HotpotQA | Avg. | Omni-MATH (L1-3) | Omni-MATH (L4-5) | Avg. |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| GPT-4.1 | Teacher | 90.4 | 71.0 | 80.7 | 82.0 | 60.0 | 67.1 |
| Qwen3-4B | SFT Distill | 81.9 | 66.6 | 74.2 | 73.6 | 39.4 | 54.1 |
| Qwen3-4B | ProD | 85.2 | 70.8 | 78.0 | 76.8 | 46.0 | 58.4 |
| Qwen3-1.7B | SFT Distill | 65.7 | 58.6 | 62.2 | 59.2 | 23.0 | 41.7 |
| Qwen3-1.7B | ProD | 70.8 | 65.0 | 67.9 | 64.8 | 28.2 | 48.1 |
| Llama-3.2-3B | SFT Distill | 55.5 | 61.6 | 58.6 | 49.0 | 11.0 | 35.1 |
| Llama-3.2-3B | ProD | 58.6 | 67.0 | 62.8 | 53.6 | 14.8 | 39.9 |

ProD在Qwen3-4B上使HotpotQA准确率从66.6%提升至70.8%，几乎追平教师（71.0%）。在域外Omni-MATH上，ProD同样带来显著提升，验证了停滞缓解的泛化性。

消融实验表明，ProD优于解码级重复惩罚（RP）和数据级简洁SFT。RP在HotpotQA上甚至导致性能下降（Qwen3-4B: 66.6% -> 61.6% @ RP 1.3），证明解码层去重无法解决轨迹级停滞。简洁SFT仅带来微小增益，因未约束学生行为。迭代ProD进一步优化停滞评分，提升准确率。

评估边界方面，停滞评分依赖LLM-as-judge或启发式规则，在极端噪声下可能失效。实验未覆盖BFCL等工具调用基准，无法验证ProD在复杂API交互中的表现。代码未开源，复现依赖论文描述。

## 关联研究分析

从问题动机看，ProD与Tool-R0（Acikgoz et al., 2026）均关注长程任务中的策略优化，但路线不同。Tool-R0通过强化学习（RL）在合成环境中从零训练，依赖可验证奖励；ProD则改进SFT蒸馏，通过停滞惩罚优化学生轨迹。ProD无需RL训练成本，但依赖高质量教师轨迹；Tool-R0无需教师，但训练不稳定。ProD在SLM蒸馏场景下更高效，但RL在长程信用分配上可能更具优势。

从方法设计看，ProD与Repetition Penalty（Keskar et al., 2019）均旨在抑制重复，但作用层级不同。RP在解码层调整Logits，仅抑制表面重复；ProD在训练层通过轨迹级停滞评分惩罚无效策略。实验显示RP在复杂任务中效果有限甚至负面，证明轨迹级停滞需训练层干预。ProD的自适应边际设计优于固定边际的SimPO，能更精准地反映行为差异。

## 总结

本文针对SLM智能体蒸馏中的进度停滞问题，提出ProD框架，通过量化停滞差距并构建自适应边际，在优化中动态惩罚停滞轨迹。实验表明，ProD在MATH和HotpotQA上显著提升SLM性能，Qwen3-4B在HotpotQA上达到70.8%，接近教师模型。ProD证明了通过改进蒸馏损失函数即可有效缓解停滞，挑战了“必须依赖RL”的隐含假设。然而，停滞评分的鲁棒性在极端噪声环境下未经验证，且实验未覆盖复杂工具调用基准。当停滞评分依赖LLM-as-judge时，其计算开销与评分一致性在大规模蒸馏中是否可接受，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.19439)