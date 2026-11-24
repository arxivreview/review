# ACL-Findings2026 · 基于人工智能的教育题目难度与心理测量建模方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Can LLMs Estimate Student Struggles? Human-AI Difficulty Alignment with Proficiency Simulation for Item Difficulty Prediction ｜人机难度对齐诊断：LLM解题能力与认知感知的解耦分析

研究机构：美国卡内基梅隆大学、美国纽约州立大学布法罗分校

作者：Ming Li、Han Chen、Yunze Xiao 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.18880)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.18880)

> 教育评估中的冷启动问题要求在新题缺乏真实作答数据时估计其难度参数。现有直接回归方法受限于表面语言特征与深层认知负荷的解耦，而基于大语言模型（LLM）的模拟作答虽符合项目反应理论（Item Response Theory, IRT）假设，却面临模型自身高解题能力与人类低能力学生认知局限之间的系统性偏差。本文切入点在于解构“解题能力”与“难度感知”的内在关联，通过双视角实证检验零样本LLM能否忠实模拟人类认知挣扎。其价值在于揭示了通用LLM在难度预测上的系统性失效机制，但零样本诊断结论是否适用于微调后的专用模型仍存疑。

】

---

【Take Out Your Calculators: Estimating the Real Difficulty of Question Items with LLM Student Simulations ｜基于LLM学生模拟的数学题难度估计

研究机构：美国马里兰大学帕克分校

作者：Christabel Acquaye、Yi Ting Huang、Marine Carpuat 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_86445c9bd9ce)

> 教育评估中题目难度校准依赖高昂的现场测试，而直接文本回归方法无法捕捉认知负荷与作答者能力的交互效应。本文切入点在于利用开源大语言模型（LLM）扮演不同能力水平的学生，通过生成个体化响应数据来重构项目反应理论（IRT）参数。具体做法是提示LLM模拟“课堂”作答，拟合IRT模型以估计难度，并验证其与真实NAEP数据的对齐度。该工作证明了零样本模拟在纯文本数学题上可达到0.82的相关性，但其对低能力学生错误模式的模拟保真度及身份标识的作用机制仍存疑。

】
