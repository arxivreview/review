# ICLR2026最新论文 ｜DUET: Distilled LLM Unlearning from an Efficiently Contextualized Teacher ｜蒸馏式大语言模型遗忘

研究机构：美国乔治梅森大学

作者：Yisheng Zhong、Zhengbang Yang、Zhuangdi Zhu

论文原文见 [arXiv](https://arxiv.org/abs/2601.21283)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.21283)

> 大语言模型（LLM）遗忘旨在移除敏感知识同时保持通用效用，但现有训练法计算昂贵且易致效用崩溃，上下文法虽高效却易被反向工程。本文切入点在于利用上下文提示生成的教师模型Logit分布作为监督信号，通过Top-K Logit蒸馏将拒绝行为固化至学生模型参数。该方案在数据效率与鲁棒性间取得平衡，但其对长尾知识及非Top-K候选的覆盖能力存疑。

## 研究背景

当LLM面对隐私或版权查询时，直接微调往往导致模型在无关领域性能急剧下降，这一现象称为灾难性遗忘。为缓解此问题，研究者引入保留集正则化，但固定权重难以平衡遗忘与保留的梯度冲突。与此同时，上下文学习（In-Context Learning, ICL）能通过提示词引导模型拒绝特定知识，无需参数更新，但其效果依赖于推理时的提示存在，一旦提示被移除或对抗性修改，被抑制的知识极易恢复，即“反遗忘”（Un-unlearning）现象。

LLM遗忘的主流路线分为训练法与上下文法。训练法如梯度上升（GA）和负偏好优化（NPO）通过参数更新实现持久遗忘，但需大量数据且易破坏通用能力；上下文法如ICU轻量高效，但缺乏鲁棒性。现有方法未能同时解决数据效率、效用保持与对抗鲁棒性三大难题。DUET的切入点在于发现上下文提示虽易被逆转，但其诱导的Logit分布偏移包含精细的监督信息，可通过蒸馏将这些瞬时的行为模式转化为持久的参数更新，从而结合两派优势。

## 核心方法

### 方法参照系

训练法遗忘通常优化目标 $\min_{\theta} \mathcal{L}_{forget}(\theta; \mathcal{D}_f) + \lambda \mathcal{L}_{retain}(\theta; \mathcal{D}_r)$，其中 $\lambda$ 需手动调节。DUET的关键差异在于摒弃显式的遗忘损失与保留损失加权，转而使用教师模型在上下文提示下的Logit分布作为统一监督信号，将遗忘与保留整合为单一蒸馏目标。

### Top-K Logit蒸馏机制

传统蒸馏使用全词表KL散度，计算昂贵且噪声主导。DUET仅关注教师模型中Logit值最高的Top-K候选词，忽略长尾噪声。设计动机在于：上下文提示主要改变高概率词的分布，而非全词表，聚焦Top-K能捕捉核心拒绝信号并降低计算成本。

$$ \min_{\theta} \mathbb{E}_{x_f \in \mathcal{D}_f} \sum_{k \in \mathcal{C}_K} l(g_{\pi_\theta}[k|x_f], g_{\pi_{ref}}[k|x_{ic} \oplus x_f]) $$

其中 $l(\cdot)$ 为Huber L-1损失，$\mathcal{C}_K$ 为教师模型Logit最高的K个词索引。该公式通过最小化学生与教师在Top-K词上的Logit差值，将教师的拒绝行为（如“抱歉”、“不知道”）嵌入学生参数。

### 统一遗忘-保留目标

传统方法需分别优化遗忘与保留，导致梯度冲突。DUET将保留集 $\mathcal{D}_r$ 样本混入训练批次，对保留集应用相同的Top-K蒸馏目标。设计动机在于：上下文提示对无关查询的影响极小，教师模型在保留集上的Logit分布接近原始模型，因此蒸馏保留集Logit等价于保持通用效用，无需额外正则化项。

$$ \mathcal{L}_{DUET} = \mathbb{E}_{x_f \in \mathcal{D}_f \cup \mathcal{D}_r} \sum_{k \in \mathcal{C}_K} l(g_{\pi_\theta}[k|x], g_{\pi_{ref}}[k|x_{ic} \oplus x]) $$

该统一目标消除了超参数 $\lambda$ 的调节需求，通过单一优化过程同时实现知识移除与效用保持，避免了加权求和导致的效用退化。

## 实验评估

实验在MUSE-Books（Harry Potter）和WMDP（Bio/Cyber）基准上进行，基线覆盖GA、NPO、SimNPO、FLAT、RMU及Refusal Training，但未对比SISA或Exact Unlearning（因成本不可行）。DUET在MUSE-Books上R-Forget为4.27，MMLU为61.45，显著优于GA（R-Forget 0.00，MMLU 24.87）和NPO（R-Forget 24.18，MMLU 54.79）。

| 方法 | R-Forget ↓ | R-Forget-500 ↓ | R-Retain ↑ | MMLU ↑ | Performance Shift ↑ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Base Model | 32.13 | 39.99 | 84.29 | 61.46 | 0 |
| GA | 0.00 | 0.00 | 0.00 | 24.87 | -48.76 |
| NPO | 24.18 | 26.83 | 69.69 | 54.79 | -0.16 |
| FLAT | 0.47 | 0.64 | 58.33 | 58.92 | 42.51 |
| DUET | 4.27 | 5.98 | 78.33 | 61.45 | 55.90 |

消融实验显示，Top-K=1000时R-Forget-500为6.12%，MMLU为61.45%；Top-K=1时R-Forget-500为5.66%，MMLU降至58.83%。这表明Top-K=1虽遗忘略优，但效用损失显著，Top-K=1000在遗忘与效用间取得最佳平衡。教师提示质量对效果影响巨大：使用“refuse-all”提示时R-Forget升至15.65，MMLU降至60.87，而优化提示下R-Forget为4.27，MMLU为61.45。

评估边界方面，DUET仅使用100个查询样本训练，数据效率极高，但未报告置信区间。评估协议包含QA和内容补全两种格式，但未涵盖多跳推理或对抗性越狱攻击的完整测试。代码未公开，超参数（如Top-K值、Huber损失参数）需从附录获取，可复现性依赖作者提供的详细设置。

## 关联研究分析

从问题动机看，DUET与NPO均旨在解决遗忘-保留权衡，但NPO依赖参考模型对比，需额外计算参考模型Logit，而DUET利用上下文提示生成的教师Logit，无需参考模型，降低了计算开销。这一差异源于DUET将上下文学习视为监督信号源，而非NPO的偏好优化框架。NPO在WMDP-Bio上Acc-Forget为62.69，MMLU为56.88，DUET为29.40，MMLU为60.63，表明DUET在效用保持上更优，但遗忘深度因指标不同（Acc vs ROUGE）难以直接比较。

从方法设计看，DUET与RMU同属参数更新法，但RMU通过随机扰动表示空间实现遗忘，缺乏针对性，而DUET通过Top-K Logit蒸馏精准定位拒绝行为。RMU在WMDP-Bio上Acc-Forget为25.84，MMLU为25.50，DUET为29.40，MMLU为60.63，显示DUET在效用保持上显著优于RMU。这一差异源于DUET的监督信号来自教师模型的精细Logit分布，而非RMU的随机方向，使得遗忘更具针对性且副作用更小。

## 总结

DUET旨在解决LLM遗忘中数据效率、效用保持与对抗鲁棒性的矛盾。现有训练法计算昂贵且易致效用崩溃，上下文法虽高效但易被反向工程。DUET通过Top-K Logit蒸馏将上下文提示生成的教师拒绝行为固化至学生参数，实现了单一目标下的遗忘-保留平衡。实验显示，DUET在MUSE-Books上R-Forget为4.27，MMLU为61.45，显著优于GA和NPO，且在反向提示攻击下R-Forget仅从5.98升至7.27，鲁棒性优于上下文法。其边界在于Top-K截断可能遗漏长尾知识，且评估未涵盖多跳推理。当Top-K值增大时，遗忘深度是否进一步下降而效用损失增加，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.21283)