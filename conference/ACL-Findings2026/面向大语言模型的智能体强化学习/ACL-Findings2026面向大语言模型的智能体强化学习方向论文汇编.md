# ACL-Findings2026 · 面向大语言模型的智能体强化学习方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【ProCeedRL: Process Critic with Explorative Demonstration Reinforcement Learning for LLM Agentic Reasoning ｜过程级批评与探索性演示强化学习

研究机构：清华大学

作者：Jingyue Gao、Yanjiang Guo、Chen Xiaoshuai 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_655b3177927a)

> 多轮智能体任务中，次优动作引发的噪声反馈会累积并破坏后续推理，导致标准强化学习（RL）探索效率低下且受限于基座模型能力。现有方法依赖独立重复采样或事后惩罚，无法在错误扩散前进行干预。本文提出 ProCeedRL，通过实时过程级批评者（Critic）检测并回溯修正低质量步骤，将探索从被动选择转为主动干预。该方法在深度搜索与具身任务上突破了标准 RL 的性能上限，但其效果高度依赖 Critic 的准确性，且缺乏理论保证。

】

---

【Reason in Chains, Learn in Trees: Self-Rectification and Grafting for Multi-turn Agent Policy Optimization ｜树结构自校正智能体策略优化

研究机构：美国乔治·华盛顿大学

作者：Yu Li、Sizhe Tang、Tian Lan

论文原文见 [arXiv](https://arxiv.org/abs/2604.07165)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07165)

> 多轮智能体强化学习面临稀疏奖励下的信用分配难题，现有组相对策略优化方法将轨迹视为独立链，导致关键决策点与常规步骤获得相同梯度信号。T-STAR 通过合并功能相似节点构建认知树，实现方差缩减的优势估计，并在分歧点合成纠正推理以提供步骤级监督。该方法无需额外奖励模型或采样，可直接集成于 GRPO 等主流算法，在长程推理任务上带来稳定增益，但其性能上限仍受限于单智能体架构与树合并阈值的静态设定。

】
