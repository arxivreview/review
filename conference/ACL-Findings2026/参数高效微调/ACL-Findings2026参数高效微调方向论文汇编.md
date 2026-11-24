# ACL-Findings2026 · 参数高效微调方向论文汇编

> 本方向共 4 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Accelerating LLM Fine-Tuning via Embedding Knowledge Transfer ｜嵌入层知识迁移加速大模型微调

研究机构：香港科技大学、澳门大学

作者：Meishu Peng、Ziyue Zhang、Yi Zhang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_96dc596b9a16)

> 参数高效微调（Parameter-Efficient Fine-Tuning, PEFT）旨在以极小参数预算适应下游任务，但现有方法如 LoRA 仅更新 Transformer 块权重，忽略了嵌入层对领域特定语义的编码作用，导致收敛缓慢且无法利用已有小模型专家知识。本文切入点在于通过异构模型间的嵌入层维度扩展与加权融合，将小专家模型的知识直接注入大目标模型，规避了伪标签生成的显存与时间开销。具体做法是构建词汇对齐后的嵌入矩阵，通过隐藏层维度扩展和加权融合实现参数迁移，再结合双阶段微调加速收敛。该方法在代码和数学任务上显著加速了收敛并提升了最终性能，但其通用性受限于同模型族内的架构一致性，跨架构迁移能力存疑。

】

---

【Astra: Activation-Space Tail-Eigenvector Low-Rank Adaptation of Large Language Models ｜激活空间尾部特征向量低秩适配

作者：Kainan Liu、Yong Zhang、Ning Cheng 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6990a57c3efc)

> 参数高效微调（PEFT）旨在以极小的可训练参数预算适应下游任务，但标准低秩适配（LoRA）的随机初始化导致早期梯度极小，阻碍收敛并限制表达力。现有初始化策略多依赖静态权重结构或瞬时梯度信号，忽略了预训练模型输出激活维度利用不均这一动态特性。Astra 通过校准集估计输出激活协方差矩阵，将低秩更新约束在尾部特征子空间内，实现了更快的收敛与更优的下游性能。该方法在 16 个基准上超越现有 PEFT 基线，但在复杂推理任务上是否具备普适性仍需验证。

】

---

【GRASS: Gradient-based Adaptive Layer-wise Importance Sampling for Memory-efficient Large Language Model Fine-tuning ｜基于梯度范数的自适应层采样微调

研究机构：国防科技大学

作者：Kaiyuan Tian、Yu Tang、Gongqingjian Jiang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.07808)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07808)

> 大语言模型全参数微调受限于GPU显存瓶颈，而低秩适配方法虽节省内存却牺牲了模型表达力。现有层选择式微调方法依赖静态、任务无关的层重要性假设，无法适应不同任务和训练阶段下层重要性的动态变化。GRASS通过引入平均梯度范数（Mean Gradient Norm, MGN）作为动态重要性指标，并配合层级优化器状态卸载机制，实现了内存高效且性能接近全参数微调的自适应层采样。该方法在算术与常识推理基准上取得了显著的性能提升，但其对梯度统计量的依赖是否在所有优化景观下均具鲁棒性，仍需进一步验证。

】

---

【Small Data, Big Noise: Adversarial Training for Robust ParameterEfficient Fine-Tuning ｜小数据大噪声：面向参数高效微调的对抗训练框架

研究机构：以色列巴伊兰大学

作者：Eitan Cohen、Idan Simai、Uri Shaham

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a53a88fdd7b5)

> 参数高效微调（PEFT）在低资源场景下常因训练数据缺乏多样性而难以抵抗真实文本中的噪声与域偏移，导致模型性能急剧下降。现有PEFT方法虽能降低计算成本，但极少将鲁棒性作为核心优化目标，且随机噪声注入无法精准定位模型脆弱点。本文提出SDBN框架，将对抗训练引入PEFT流程，通过构造连续嵌入空间与离散字符/语义不确定性集，在训练阶段主动寻找最坏情况样本以增强模型稳定性。该方法在不增加可训练参数的前提下显著提升了小数据噪声场景下的鲁棒性，但其对生成式任务的离散扰动依赖外部大模型，且未验证在极端数据稀缺下的收敛稳定性。

】
