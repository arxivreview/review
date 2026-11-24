# Others2026 · 大语言模型中的偏见与公平性方向论文汇编

> 本方向共 2 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【LLM BiasScope: A Real-Time Bias Analysis Platform for Comparative LLM Evaluation ｜LLM BiasScope：实时多模型偏见对比分析平台

研究机构：德国慕尼黑工业大学、意大利罗马第一大学

作者：Himel Ghosh、Nick Elias Werner

论文原文见 [arXiv](https://arxiv.org/abs/2603.12522)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.12522)

> 导读 大语言模型（LLM）部署中，偏见检测工具长期局限于静态基准或单模型分析，无法在用户自定义提示下实时对比多个模型的偏见模式。现有平台如 Chatbot Arena 侧重质量偏好，缺乏细粒度偏见类型分析；Perspective API 仅检测毒性，忽略社会偏见维度。本文构建 LLM BiasScope，通过两级流水线（句子级偏见检测 + 偏见类型分类）实现多模型并行对比与实时可视化。该工具填补了交互式偏见评估的空白，但其检测器选型依赖静态基准，未验证实时场景下的鲁棒性，且样本量极小，统计效力存疑。

】

---

【记忆增强智能体中的偏见编码与放大机制

作者：Himanshu Gharat、Himanshi Agrawal、Gourab K. Patro

论文原文见 [arXiv](https://arxiv.org/abs/2512.16532)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.16532)

> 大语言模型（Large Language Models, LLMs）在招聘等高利害场景中部署时，其记忆模块可能将历史偏好转化为系统性歧视。现有研究多关注静态输出公平，忽视了智能体（Agent）工作流中记忆对偏见的动态编码与跨阶段放大效应。本文通过构建基于 GPT-4.1 的记忆增强招聘智能体，量化了个性化检索与重排过程中性别偏见的累积路径。该工作揭示了记忆机制作为偏见载体的风险，但缺乏对去偏干预有效性的验证，其结论的普适性仍受限于单一属性与模拟环境。

】
