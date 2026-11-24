# ACL-Findings2026 · 自动提示优化方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Adaptive Prompt Optimization for Open-Ended Tasks: Uncertainty Preference as a Secondary Signal ｜基于语义熵偏好形状的开放式任务提示优化

研究机构：中国科学技术大学、中国科学院大学

作者：Shuyang Zhang、Zhixuan Liu、Zhichen Dong 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_02d27d69fd01)

> 自动提示优化（Automatic Prompt Optimization, APO）旨在通过算法搜索最优指令以提升大语言模型（LLM）性能，但在开放式任务中，现有方法仅最大化单一标量分数，忽视了任务对生成不确定性的差异化需求。本文指出，安全类任务偏好低熵的保守输出，而创意类任务偏好高熵的多样输出，这种风格依赖性是提示优化不稳定的根源。通过引入语义熵作为辅助选择信号，本文在标准优化器上增加了偏好形状化机制，使提示进化方向与任务风格对齐。该方法在多个模型家族上提升了成对胜率，但其有效性依赖于预定义的风格模板，且未提供严格的理论收敛保证。

】

---

【HIPO: A Hierarchical Prompt Optimization Framework with Task Awareness and Fine-Grained Debugging ｜层级化提示优化框架

研究机构：北京航空航天大学、新加坡国立大学

作者：Lu Qi、Lei Chai、Hongrui Yu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0967ff7870f4)

> 自动提示优化（APO）旨在通过算法搜索最优指令以提升大语言模型（LLM）性能，但现有方法普遍采用数据集级优化范式，即寻找单一全局提示，忽略了样本间的难度差异。这种“一刀切”策略导致简单样本被过度优化而性能退化，复杂样本则因优化算法过早收敛而提升有限。HIPO 框架通过引入离线训练的难度路由器，将优化粒度从数据集级细化至样本级，动态匹配五级提示层级。该框架在27个任务上超越了所有基线方法，且成本降低1.2至80倍，但其对路由器泛化能力的验证仍显不足。

】

---

【Learning from Contrastive Prompts: An Automated Prompt Optimization Framework ｜基于对比提示的自动优化框架

作者：Mingqi Li、Karan Aggarwal、Yong Xie 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_89818f07c015)

> 自动提示优化（APO）旨在通过算法在离散指令空间中搜索最优提示，以解决闭源模型参数不可访问与人工试错效率低下的矛盾。现有反馈驱动方法如 ProTeGi 和 OPRO 主要依赖错误样本或历史排名列表，缺乏对“成功”与“失败”提示间结构性差异的显式建模，导致优化易陷入局部最优或过拟合特定错误模式。LCP 引入对比学习机制，通过直接分析高性能与低性能提示的语义差异来生成新候选，从而提取更具泛化性的提示设计原则。该方法在 Big-Bench Hard 基准上取得了显著的性能提升，但其高昂的计算成本与对特定模型家族的依赖限制了其通用性。

】

---

【LLM Prompt Duel Optimizer: Efficient Label-Free Prompt Optimization ｜无标签提示优化中的对偶赌博机框架

作者：Yuanchen Wu、Saurabh Verma、Justin Lee 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.13907)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dc94eecff4a1)

> 自动提示优化（APO）旨在通过算法搜索最优指令以提升大语言模型（LLM）性能，但主流方法严重依赖昂贵的真值标签进行候选评估。现有无标签方案如自监督提示优化（SPO）采用贪心爬山策略，缺乏探索-利用平衡机制，导致在噪声偏好信号下易陷入局部最优。本文提出提示决斗优化器（PDO），将无标签提示选择重构为对偶赌博机问题，结合双重汤普森采样（D-TS）与顶级表现者引导变异，在固定裁判预算下实现高效搜索。该框架在16个BBH任务中的13个上取得最高准确率，但其性能高度依赖裁判模型的推理能力，在复杂几何任务上仍显著落后于有标签SOTA。

】

---

【Revisiting Self-Play Preference Optimization: On the Role of Prompt Difficulty ｜自博弈偏好优化中的提示难度筛选

作者：Yao Xiao、Jung-jae Kim、Roy Ka-Wei Lee 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_412ace842d64)

> 自博弈偏好优化旨在通过模型自我生成响应并基于奖励模型筛选正负样本，利用直接偏好优化（DPO）提升大语言模型（LLM）的对齐性能，但现有方法通常假设所有提示对优化贡献均等，忽视了提示难度分布对训练效率的潜在干扰。本文切入点在于量化提示难度并揭示困难提示对DPO训练的负向影响，提出基于均值奖励的提示难度度量与筛选策略。具体做法是计算每个提示多次采样响应的平均奖励作为难度代理，剔除最困难的25%提示后仅保留最易的30%进行训练。该策略在AlpacaEval 2上显著提升了Tulu-8B和Mistral-7B的性能，但仅验证了静态筛选的有效性，未探讨动态难度适应机制。

】
