# Others2026 · 面向大语言模型的智能体强化学习方向论文汇编

> 本方向共 1 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs ｜回合级优势估计的PPO变体

研究机构：美国德克萨斯大学奥斯汀分校

作者：Junbo Li、Peng Zhou、Rui Meng 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.17008)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.17008)

> 多轮智能体强化学习（Agentic RL）面临的核心困境是：在长程交互中，稀疏且延迟的奖励信号难以准确归因到具体的决策步骤，导致策略优化陷入不稳定甚至崩溃。当前主流算法组相对策略优化（Group Relative Policy Optimization, GRPO）因依赖采样均值估计优势，在高方差的多轮环境中表现脆弱，而传统近端策略优化（Proximal Policy Optimization, PPO）若沿用Token级建模，则因状态转移不连续导致Critic学习失效。本文通过重构马尔可夫决策过程（Markov Decision Process, MDP）的粒度，将状态-动作对从Token级提升至Turn级，提出Turn-PPO，利用可学习Critic在回合边界进行价值估计，从而获得更稳定的优势信号。该方案在防止训练崩溃方面表现出显著优势，但其绝对性能仍远低于多智能体协作方法，且对模型推理长度的敏感性揭示了其泛化边界的模糊性。

】
