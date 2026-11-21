# ACL2026最新论文 ｜Reasoning Fails Where Step Flow Breaks ｜基于步骤级显著性诊断的推理信息流修复

研究机构：上海交通大学、吉林大学

作者：Xiaoyu Xu、Yulan Pan、Xiaosong Yuan 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.06695)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.06695)

> 大型推理模型（Large Reasoning Models, LRMs）在多步任务中表现优异，但其内部计算过程常因信息流断裂导致错误，且现有诊断工具难以在长文本中定位失效步骤。传统注意力分析噪声大且缺乏步骤级对齐，无法揭示深层推理的因果依赖。本文提出 Step-Saliency 诊断方法，将 token 级显著性聚合为步骤级映射，识别出“浅层锁定”与“深层衰减”两种失效模式，并设计 StepFlow 测试时干预机制，通过 Odds-Equal Bridge 和 Step Momentum Injection 修复信息流。该方法在不重训练的前提下显著提升了多个基准上的准确率，验证了内部机制修复的有效性，但其对潜在推理模型的适用性及安全性影响尚待验证。

## 研究背景

当大型推理模型生成思维链（Chain-of-Thought, CoT）时，其内部计算并非均匀分布，而是存在显著的信息流瓶颈。模型在浅层往往过度关注当前生成的 token，忽略问题背景与早期推理步骤，这种现象称为“浅层锁定”（Shallow Lock-in）；而在深层，随着推理链延长，早期步骤的显著性迅速衰减，导致最终答案与完整推理过程脱节，即“深层衰减”（Deep Decay）。这两种模式导致模型在复杂任务中频繁出错，且错误难以归因。

现有研究多聚焦于外部文本的忠实度评估，如 FaithCoT-Bench 通过反事实干预量化 CoT 与内部计算的一致性，或 Circuit-based Reasoning Verification 利用电路追踪分析推理结构。然而，这些方法侧重于“审计”而非“修复”，且 token 级显著性分析在长序列中噪声极大，难以直接指导干预。本文切入点在于将机制可解释性从诊断延伸至干预，通过步骤级显著性映射定位信息流断裂点，并设计轻量级测试时干预策略，直接修复内部计算路径，从而在不改变模型权重的前提下提升推理性能。

## 核心方法

### 步骤级显著性诊断框架

本文方法建立在机制可解释性框架之上，区别于传统的 token 级注意力分析，其核心创新在于将显著性评分聚合至语义步骤级别。通常的显著性分析直接计算 token 间的梯度加权影响，但在长推理链中，这种细粒度信号难以解释步骤间的依赖关系。Step-Saliency 首先计算 token 级影响矩阵，随后根据思维链的自然分段（问题、思考步骤、总结）进行池化，生成步骤到步骤的显著性映射。

$$ M^{(\ell)}_{i \leftarrow j} = \frac{1}{|\Gamma_i| |\Gamma_j|} \sum_{t \in \Gamma_i} \sum_{k \in \Gamma_j} I^{(\ell)}_{t,k} $$

该公式表示在第 $\ell$ 层，步骤 $j$ 对步骤 $i$ 的平均显著性影响，其中 $\Gamma$ 代表 token 序列片段。通过这种聚合，模型内部的“浅层锁定”表现为对角线附近的高显著性，而“深层衰减”表现为深层中思考步骤显著性的快速下降。这一诊断框架为后续干预提供了精确的定位依据，解决了传统方法无法识别步骤级信息丢失的局限。

### 浅层信息流桥接（Odds-Equal Bridge）

针对浅层锁定问题，StepFlow 在模型前向传播的浅层引入 Odds-Equal Bridge (OEB) 机制。通常的注意力机制允许模型将绝大部分注意力权重分配给当前生成的 token，导致早期上下文被抑制。OEB 通过约束注意力分布，强制保留一定比例的注意力权重在“桥接区域”（即问题或早期步骤），防止信息流坍缩。

$$ \tau_B = \min\left( \sqrt{\frac{|B|}{|S|}} \cdot \tau_{\max}, \tau_{\max} \right) $$

该公式定义了桥接区域 $B$ 的最小注意力质量阈值 $\tau_B$，其中 $S$ 为当前步骤，$\tau_{\max}$ 为最大干预强度。当实际桥接注意力 $p_t(B)$ 低于 $\tau_B$ 时，通过 KL 散度投影调整注意力 logits，确保早期上下文保持非零影响力。这一设计直接对抗了浅层模型对局部信息的过度依赖，确保问题背景在推理初期不被遗忘。

### 深层步骤动量注入（Step Momentum Injection）

针对深层衰减问题，StepFlow 在深层引入 Step Momentum Injection (SMI) 机制。随着深度增加，早期步骤的显著性自然衰减，导致总结阶段缺乏完整推理链的支持。SMI 在步骤边界处，将前一步骤的隐藏状态均值作为“动量”注入到下一步骤的初始隐藏状态中。

$$ \mathbf{h}^{(\ell)}_{t} \leftarrow \mathbf{h}^{(\ell)}_{t} + \alpha \cdot \mathbf{m}_{\text{prev}} $$

该公式表示在深层 $\ell$，将前一步骤的动量向量 $\mathbf{m}_{\text{prev}}$ 以系数 $\alpha$ 注入当前 token $t$ 的隐藏状态 $\mathbf{h}$。这一操作相当于在深层残差流中维持一个低通滤波器，确保早期推理内容在深层计算中保持可见性，从而缓解深层衰减导致的信息丢失。OEB 与 SMI 协同工作，分别修复浅层和深层的信息流断裂，形成完整的测试时干预闭环。

## 实验评估

实验在 DeepSeek-R1-Distill (7B/14B/32B)、GPT-OSS-20B 和 QwQ-32B-Preview 等主流大型推理模型上进行，涵盖 AIME24/25、MATH-500、GPQA-Diamond 和 LiveCodeBench 等高难度基准。基线对比包括 Budget Forcing、Hint-Infer、Plan-and-Solve 以及 Self-Consistency (SC) 等测试时扩展方法。StepFlow 在所有模型和基准上均取得一致提升，尤其在需要长推理链的竞赛级数学问题上增益显著。

| 模型 | 基准 | 基线准确率 (%) | StepFlow 准确率 (%) | 增益 (百分点) |
| :--- | :--- | :--- | :--- | :--- |
| DeepSeek-R1-Distill-32B | AIME25 | 54.9 | 66.7 | +11.8 |
| GPT-OSS-20B (medium) | LiveCodeBench | 70.0 | 79.5 | +9.5 |
| DeepSeek-R1-Distill-7B | AIME24 | 54.0 | 62.5 | +8.5 |
| QwQ-32B-Preview | GPQA-D | 58.1 | 63.3 | +5.2 |

消融实验显示，OEB 和 SMI 单独使用均能带来提升，但组合使用时效果最佳，验证了两种失效模式的互补性。在 GPT-OSS-20B medium 上，仅使用 OEB 在 AIME25 上提升 2.5 个百分点，仅使用 SMI 提升 2.0 个百分点，而组合使用提升 7.2 个百分点。此外，干预层数的选择至关重要，仅在底部和顶部各 1/4 层应用干预效果最佳，过度干预反而导致性能下降，表明信息流修复需精准定位而非全局覆盖。

评估边界方面，本文主要关注准确率提升，未深入讨论干预对模型安全性或对抗鲁棒性的影响。虽然代码已开源，但超参数 $\tau_{\max}$ 和 $\alpha$ 需针对每个模型单独调整，缺乏统一的自适应策略。此外，实验未覆盖潜在推理（Latent CoT）模型，其连续空间中的信息流修复机制尚不明确。

## 关联研究分析

从问题动机看，本文与 FaithCoT-Bench 和 Circuit-based Reasoning Verification 形成鲜明对比。FaithCoT-Bench 侧重于通过外部行为评估量化 CoT 的忠实度，属于“审计”范式；Circuit-based Reasoning Verification 利用内部电路追踪验证推理逻辑，属于“验证”范式。本文则进一步延伸至“干预”范式，不仅识别信息流断裂，还通过 OEB 和 SMI 直接修复。这种从诊断到干预的跨越，填补了机制可解释性在提升模型性能方面的应用空白。然而，本文未讨论修复后的 CoT 是否更易于被对抗攻击利用，这与 Stress-Testing CoT Monitorability 中揭示的监控规避风险形成潜在张力。

从方法设计看，StepFlow 与 Self-Consistency (SC) 和 Longer Generation 等测试时扩展方法存在本质差异。SC 通过多路径采样投票提升鲁棒性，计算成本随采样数线性增加；Longer Generation 通过延长生成长度增加推理深度，但易引入噪声。StepFlow 在单次前向传播中通过修改内部计算路径提升性能，计算开销仅为基线的 1.35 倍，却取得了优于 SC (k=2) 的效果。这种效率优势源于其直接针对信息流瓶颈的机制性修复，而非外部统计聚合。然而，StepFlow 对模型架构的依赖性较强，其在非 Transformer 架构或潜在推理模型上的泛化能力尚未验证。

## 总结

本文针对大型推理模型内部信息流断裂导致的推理失效问题，提出 Step-Saliency 诊断框架与 StepFlow 干预机制。通过识别“浅层锁定”与“深层衰减”两种模式，并设计 OEB 和 SMI 两种干预算子，本文在 DeepSeek-R1-Distill-32B 的 AIME25 基准上将准确率从 54.9% 提升至 66.7%，验证了内部机制修复的有效性。该方法在不重训练的前提下显著提升了推理性能，且计算效率优于传统采样策略。然而，本文未探讨干预对模型安全性的潜在影响，且超参数需针对特定模型调整，限制了其通用性。当模型架构从离散 token 转向连续潜在空间时，基于步骤边界的动量注入机制是否依然有效，是一个亟待验证的问题。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.06695)