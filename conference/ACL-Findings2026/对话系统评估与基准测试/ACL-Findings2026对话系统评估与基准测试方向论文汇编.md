# ACL-Findings2026 · 对话系统评估与基准测试方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Real or Robotic? Assessing Whether LLMs Accurately Simulate Qualities of Human Responses in Human-LLM Dialogue ｜真实还是机械？评估LLM模拟人类对话的保真度

研究机构：美国约翰斯·霍普金斯大学、美国密歇根大学

作者：Jonathan Ivey、Shivani Kumar、Jiayu Liu 等 15 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7809bd2ed654)

> 对话系统评估正面临工具可靠性危机，核心矛盾在于用户模拟器无法高保真复现人类行为，导致下游评估失效。现有LLM模拟器虽能生成流畅文本，但其风格与句法特征与真实人类存在系统性偏差，且缺乏量化其“拟人性”边界的实证标准。本文基于WildChat真实数据，通过对比LLM输出与人类标注基线在21项语言学指标上的相关性，量化了模拟器的失效语境。该研究揭示了LLM仅能模拟人类分布的窄子集，为评估工具的质量审计提供了实证基础，但其零样本设定是否足以代表高保真模拟器的极限仍存疑。

】

---

【VCB Bench: An Evaluation Benchmark for Audio-Grounded Large Language Model Conversational Agents ｜语音对话大模型基准

研究机构：武汉大学、腾讯AI实验室

作者：Jiliang Hu、Wenfu Wang、Zuchao Li 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2ee384a1bf31)

> 语音对话大模型（Large Audio Language Models, LALMs）的评估长期受限于合成数据的声学单一性与英语语料的霸权，导致模型在真实中文交互场景下的鲁棒性被高估。现有基准多依赖文本转语音（TTS）或从文本问答集迁移，无法捕捉口语中的停顿、方言及环境噪声等物理扰动。本文构建了首个完全基于真实人类录音的中文语音对话基准，通过指令遵循、知识理解与鲁棒性三维框架量化模型表现。该基准揭示了开源模型在跨语言声学对齐上的显著短板，但其评估协议对长程多轮对话的依赖度较低，且缺乏对高风险场景的动态审计能力。

】

---

【Who's Asking? Simulating Role-Based Questions for Conversational AI Evaluation ｜角色感知对话评估框架

研究机构：美国华盛顿大学、美国普林斯顿大学

作者：Navreet Kaur、Hoda Ayad、Hayoung Jung 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.16829)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.16829)

> 对话系统评估长期面临“谁在问”这一变量缺失的问题，导致模型对同一问题的响应无法区分用户的社会角色与需求差异。现有评估多剥离个人语境，忽视了角色对响应质量（如知识量、支持度）的系统性影响。本文提出CORUS框架，通过社会学角色理论构建患者、照护者及从业者三类角色的分类法，并模拟嵌入角色语境的提问，以量化角色对大语言模型（LLM）响应的影响。该工作揭示了脆弱角色（如患者）虽获得更高情感支持，却伴随知识内容显著下降的权衡现象，为高风险领域的评估提供了新视角，但其单轮静态设定限制了动态交互场景的适用性。

】
