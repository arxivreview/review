# ACL-Findings2026 · CAD B-Rep 生成与理解方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【TOOLCAD: Exploring Tool-Using Large Language Models in Text-to-CAD Generation with Reinforcement Learning ｜工具调用型大语言模型在文本到CAD生成中的强化学习探索

作者：Yifei Gong、Xing Wu、Wenda Liu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.07960)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07960)

> 文本到CAD生成旨在将自然语言指令转化为可执行的参数化建模操作，但现有方法多依赖静态序列预测或一次性代码生成，难以处理多部件复杂模型中的长程推理与错误累积。本文切入点在于将大语言模型（LLM）重构为工具调用智能体，通过交互式CAD引擎反馈与在线强化学习（RL）实现迭代式建模。具体做法是构建包含规则奖励与结果监督的混合反馈环境，利用课程学习策略训练LLM自主规划并调用CAD原语工具。该框架在开源模型上实现了接近闭源模型的性能，但其对L3级精确指令的依赖及缺乏多模态输入支持，限制了其在模糊设计意图场景下的泛化能力。

】
