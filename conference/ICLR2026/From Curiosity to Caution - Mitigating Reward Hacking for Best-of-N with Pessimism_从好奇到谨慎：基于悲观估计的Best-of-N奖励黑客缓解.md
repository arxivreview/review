# ICLR2026最新论文 ｜From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism ｜从好奇到谨慎：基于悲观估计的Best-of-N奖励黑客缓解

研究机构：美国卡内基梅隆大学、美国哥伦比亚大学

作者：Zhuohao Yu、Zhiwei Steven Wu、Adam Block

论文原文见 [arXiv](https://arxiv.org/abs/2604.04648)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.04648)

> 推理时扩展（Inference-time Scaling）旨在通过增加采样数量提升大语言模型（LLM）性能，但Best-of-N（BoN）采样常因奖励模型（RM）对分布外（OOD）响应的虚假高分导致性能随N增加而下降。现有方案或依赖更复杂的RM训练，或采用过于保守的分布正则化，无法兼顾鲁棒性与计算收益。本文提出Caution机制，将强化学习中的悲观原则迁移至推理时，通过预测误差惩罚OOD响应。该方法在GSM8K上将N=512时的准确率从71.5%提升至81.1%，但仅在标量RM场景下验证，未探索生成式RM的内在鲁棒性。

## 研究背景

当LLM生成多个候选响应时，BoN策略依赖RM选择最高分项。然而，RM在训练分布外往往失效，导致模型选择冗长但错误的响应，即奖励黑客（Reward Hacking）。这一现象源于Goodhart定律：当指标成为优化目标时，其作为质量代理的可靠性丧失。为缓解此问题，研究界主要采取两条路径：一是改进RM本身，如通过因果推断或信息瓶颈去偏；二是正则化选择过程，如Huang et al. (2025b)提出的分布约束。前者难以穷尽所有黑客策略，后者则因惩罚所有OOD响应而抑制了真正优质但略偏离分布的响应，未能充分利用推理时扩展的收益。

本文切入点在于区分“因RM缺陷导致的OOD”与“真正优质的OOD”。现有方法在分布层面进行均匀惩罚，忽略了响应级别的差异。本文借鉴强化学习中的悲观估计（Pessimism）与好奇心（Curiosity）机制，在奖励层面引入不确定性惩罚，仅对预测误差高的响应降低分数，从而在保持探索收益的同时抑制奖励黑客。

## 核心方法

### 方法参照系

BoN的标准流程为：采样N个响应 $y_i \sim \pi(\cdot|x)$，计算RM分数 $\hat{r}(x, y_i)$，选取 $\arg\max_i \hat{r}(x, y_i)$。该流程假设RM分数与真实质量 $r^\star$ 单调相关，但在大N下，RM对OOD响应的评分偏差导致选择失效。本文问题与该通用流程的关键差异在于：需在推理时动态评估RM评分的可靠性，而非依赖静态的RM权重或分布约束。

### 悲观奖励估计

设计动机：解决Huang et al. (2025b)中分布正则化过于保守、无法区分“优质OOD”与“黑客OOD”的问题。本文在RM分数基础上引入不确定性惩罚项。定义预测器网络 $P_\theta(x, y)$ 与目标网络 $T(x, y)$（取RM第L层隐藏状态），训练 $P_\theta$ 拟合 $T$ 在典型响应上的输出。推理时，计算预测误差 $\alpha(x, y) = \|P_\theta(x, y) - T(x, y)\|_2$ 作为OOD信号。悲观奖励定义为：

$$ \hat{r}_{LCB}(x, y) = \hat{r}(x, y) - \lambda \cdot \|P_\theta(x, y) - T(x, y)\|_2 $$

其中 $\lambda$ 控制惩罚强度。该公式的物理含义是：对RM评分高但预测误差大（即OOD）的响应进行降权，而对评分高且预测误差小（即ID）的响应保持原分。

### 离线好奇心实例化

设计动机：解决在线好奇心机制（如RND）需持续训练预测器、计算开销大的问题。本文采用完全离线训练策略。训练数据 $D_{train}$ 由基础模型 $\pi$ 在GSM8K训练集上采样生成，无需人工标注。预测器 $P_\theta$ 通过最小化均方误差损失 $\mathcal{L}(\theta) = \mathbb{E}_{(x,y)\sim D_{train}} \|P_\theta(x, y) - T(x, y)\|_2^2$ 进行训练。训练完成后，$P_\theta$ 冻结，推理时仅需两次前向传播（$P_\theta$ 和 $T$）即可计算 $\alpha$，计算成本与RM前向传播同阶。这一设计将OOD检测从在线探索转化为离线分类任务，显著提升了工程可行性。

## 实验评估

实验基于Llama-3.2-3B-Instruct，使用OASST DeBERTa作为RM，在GSM8K、MATH-500和BigBench-Hard上评估。基线包括RM-only、Pessimism-only及传统RND。本文未对比CAMEL或Skywork-Reward等SOTA RM，因这些方法侧重训练时优化，而本文聚焦推理时选择。

| 方法 | GSM8K Peak Acc (%) | GSM8K Final Acc (N=512) (%) | MATH-500 Peak Acc (%) | BBH-Hard Peak Acc (%) |
| :--- | :--- | :--- | :--- | :--- |
| Reward Model | 79.3 | 71.5 | 11.5 | 17.3 |
| Pessimism Only | 81.3 | 7.7 | 8.5 | 1.7 |
| RM + Pessimism (Ours) | **82.6** | **81.1** | **13.6** | **22.9** |

RM + Pessimism在GSM8K上Final Acc达81.1%，较RM-only的71.5%提升9.6个百分点，且随N增加性能稳定上升，未出现下降。MATH-500作为OOD任务，Peak Acc从11.5%提升至13.6%，表明Caution机制在分布外场景下仍有效。

| 预测器配置 | Reconstruction Loss | Peak Acc (%) | Final Acc (%) |
| :--- | :--- | :--- | :--- |
| Lightweight + Trainable Emb. | 0.242 | 82.2 | 82.2 |
| Lightweight + Frozen Emb. | 0.246 | 81.5 | 81.3 |
| Full + Trainable Emb. | 0.127 | 80.3 | 80.2 |
| Full + Frozen Emb. | 0.127 | 80.4 | 78.4 |

消融显示，Lightweight架构配合Trainable Embedding表现最佳，Peak Acc 82.2%。Full架构虽Reconstruction Loss更低（0.127 vs 0.242），但Peak Acc反而下降，表明过度拟合RM特征可能损害OOD检测泛化性。$\lambda=0.8$时性能最优，$\lambda=1.0$（纯Pessimism）在GSM8K上Final Acc仅7.7%，证实纯OOD惩罚会误杀优质响应。

评估边界方面，本文未报告计算效率指标，仅定性说明推理成本与RM同阶。代码未公开，但超参数表（Table 4）提供了完整配置，包括24GB VRAM需求、5000训练样本及$\lambda \in [0,1]$扫描范围。指标仅使用Accuracy，未评估响应长度或多样性，可能掩盖Caution对响应分布的潜在影响。

## 关联研究分析

从问题动机看，本文与Huang et al. (2025b)均针对BoN中的奖励黑客，但根源认知不同。Huang et al.认为问题源于选择分布偏离训练分布，故采用信息论约束分布距离；本文认为问题源于RM对OOD响应的评分偏差，故采用预测误差惩罚。这一差异源于任务特性：Huang et al.假设RM在ID内可靠，而本文实验显示RM在ID内也存在格式偏好偏差（如Figure 5中低分但格式正确的响应），因此分布约束无法解决ID内的评分偏差，而预测误差能捕捉RM内部的特征不一致性。

从方法设计看，本文与Sun et al. (2025)的Curiosity-driven RLHF同属好奇心机制应用，但方向相反。Sun et al.在训练时利用预测误差作为内在奖励鼓励探索，本文在推理时利用预测误差作为惩罚抑制探索。这一反转源于场景差异：训练时OOD是探索目标，推理时OOD是风险源。本文未验证生成式RM（GRM）是否天然具备OOD检测能力，若GRM通过自然语言理由显式评估质量，其预测误差是否仍需额外惩罚，论文未给出回答。

## 总结

本文核心矛盾在于BoN采样中RM评分可靠性随N增加而下降，导致性能退化。现有分布正则化方法因均匀惩罚OOD而牺牲了优质响应的选择机会，本文通过引入基于预测误差的悲观奖励，在奖励层面实现选择性惩罚。Caution机制在GSM8K上将N=512时的准确率从71.5%提升至81.1%，证明了离线好奇心实例化在推理时扩展中的有效性。然而，实验仅覆盖标量RM，且Lightweight架构优于Full架构的结果暗示，过度拟合RM特征可能损害OOD检测的泛化性。当RM本身具备强鲁棒性（如经过因果去偏训练）时，Caution的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.04648)