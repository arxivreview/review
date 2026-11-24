# ACL-Findings2026 · 奖励建模与RLHF优化方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Beyond Length Scaling: Synergizing Breadth and Depth for Generative Reward Models ｜混合推理机制的生成式奖励模型

研究机构：香港城市大学

作者：Qiyuan Zhang、Yufei Wang、Tianhe Wu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.01571)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.01571)

> 生成式奖励模型（GRM）旨在通过自然语言理由替代标量分数以指导策略优化，但现有方法普遍陷入“长度即质量”的误区，导致推理机制与任务需求错配。本文指出，主观偏好与客观正确性需要正交的推理路径，提出Mix-GRM框架，通过模块化重组原始理由为广度（B-COT）与深度（D-COT）两种结构，并采用SFT与RLVR实现机制自适应。该框架在五个基准上刷新SOTA，但其在分布外数据上的泛化边界及模块化重组的幻觉风险尚未得到充分验证。

】

---

【Beyond Monolithic Rewards: Hybrid Multi-Aspect Reward Optimization ｜混合多面奖励优化

作者：Radha Gulhane、Sathish Reddy Indurthi

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4a7915cc79f3)

> 多模态强化学习长期受困于单一奖励模型在视觉-语言任务中的校准失效，导致策略优化陷入长度偏差或格式错误的局部最优。现有方案要么依赖高成本的全量奖励模型训练，要么在可验证任务中缺乏对主观质量的捕捉。本文切入点在于构建一个融合规则验证、模型评分与行为约束的混合奖励信号，以低成本实现多源信号的互补。该框架在3B模型上实现了9.48%的平均基准提升，但其对规则验证器准确性的强依赖及缺乏动态权重机制，限制了其在模糊边界任务上的泛化能力。

】

---

【Joint Optimization of Training Data and Policy in RLHF ｜联合优化训练数据与策略的强化学习

作者：Zhuohao Yu、Jiali Zeng、Weizheng Gu 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2152130824bb)

> 强化学习从人类反馈（RLHF）旨在弥合大语言模型输出与人类期望的偏差，但传统范式将训练问题视为固定输入，导致策略在缺乏显式规范的问题上探索空间受限，难以发现多样化的解题策略。现有方法通过增加同一固定问题的采样数量来提升多样性，但当问题本身缺乏行为标准或推理指引时，这种冗余采样提供的学习信号极为有限。本文提出联合优化数据与策略（Joint Optimization of Data and Policy, JODP）框架，利用策略模型自身生成多样化的问题规范（Specifications），并通过多臂老虎机算法动态选择有效规范以引导Rollout生成，同时保持奖励计算基于原始问题以防止目标漂移。该方法以极低的计算开销实现了4B模型接近8B模型的性能，但其有效性依赖于规范生成质量与任务复杂度的匹配，且在开放式非验证任务中的泛化能力尚未得到充分验证。

】

---

【OpenGenAlign: A Preference Dataset and Benchmark for Trustworthy Reward Modeling in Open-Ended, Long-Context Generation ｜长上下文开放生成的偏好数据基准

作者：Hanning Zhang、Juntong Song、Juno Zhu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5ad0865e86f1)

> 长上下文开放生成缺乏专用偏好数据与评估基准，导致通用奖励模型在幻觉与全面性维度上失效。现有方法依赖通用对话数据训练，无法捕捉长文本特有的质量权衡，本文通过o3多维评估构建领域特定数据集填补空白。其核心贡献是提供33K高质量偏好对及1.5K测试集，验证了领域数据对策略优化的增益。该工作确立了长上下文奖励建模的数据基线，但o3标注噪声对模型鲁棒性的影响尚未量化。

】

---

【Reward Yourself: Efficient Self Rewards for Trustworthy Sampling ｜自奖励可信采样

作者：Mingjie Li、Wai Man Si、Michael Backes 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_657a157c0c03)

> 现有奖励模型在隐私与偏见等可信任务上表现不佳，甚至劣于贪心解码，而重新训练奖励模型成本高昂。本文切入点在于不训练新模型，而是通过剪枝现有大语言模型（LLM）构建“可信”与“不可信”双变体，利用其对数似然比作为辅助奖励信号。具体做法是集成到Best-of-N采样流程中，先过滤低分候选，再由外部奖励模型选择最终答案。该方法在隐私任务上提升10-20%拒绝率，但仅在特定可信域验证，通用基准有效性未证实。

】
