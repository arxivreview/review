# ACL2026 · 对话式AI代理与意图理解方向论文汇编

> 本方向共 2 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【ProActor: Timing-Aware Reinforcement Learning for Proactive Task Scheduling Agents ｜时序感知强化学习用于主动任务调度代理

研究机构：美国加州大学圣克鲁兹分校

作者：Lei Ding、Bin He、Chenguang Wang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.24900)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.24900)

> 导读 主动任务调度要求代理在对话中预判用户需求并选择最佳时机触发软件动作，但现有监督微调方法将时机视为单一正确答案，惩罚了同样有效的早期行动，导致策略僵化。ProActor 将主动行为优化形式化为对话轮级强化学习问题，通过自动化标注管道生成包含多个有效时机的参考动作范围，并利用阶段感知复合奖励在动作一致性与触发时机间取得平衡。该框架结合量化 LoRA 与自适应资源训练系统，在资源受限环境下实现了 4–8 倍训练加速。其价值在于证明了轮级 GRPO 能突破 SFT 的时序多解性瓶颈，但量化模型对策略探索空间的潜在限制尚未被充分验证。

】

---

【YIELD: A Large-Scale Dataset and Evaluation Framework for Information Elicitation Agents ｜信息提取代理（IEA）：基于离线强化学习的长程对话策略优化

研究机构：中国科学院、美国乔治城大学

作者：Victor De Lima、Grace Hui Yang

论文原文见 [arXiv](https://arxiv.org/abs/2604.10968)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3ff6235ecda7)

> 导读 传统对话智能体旨在满足用户即时需求，而司法审讯、新闻调查等机构场景要求系统主动从受访者中提取关键信息以达成外部目标，这一“信息提取”任务缺乏专用数据集与评估标准。现有任务导向对话方法依赖固定标签与单轮假设，无法处理长程交互中无单一最优解的开放提问策略，导致模型在复杂机构对话中表现僵化。本文提出信息提取代理（Information Elicitation Agents, IEAs）范式，构建首个大规模伦理合规数据集YIELD，并将信息提取形式化为有限时域部分可观测马尔可夫决策过程（POMDP），利用离线强化学习优化提问策略。该工作填补了机构级主动对话研究的空白，但其奖励信号依赖代理指标，且缺乏跨领域泛化验证，长期效用边界尚存疑。

】
