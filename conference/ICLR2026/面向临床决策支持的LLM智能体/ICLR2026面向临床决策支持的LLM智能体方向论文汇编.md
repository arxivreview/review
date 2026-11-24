# ICLR2026 · 面向临床决策支持的LLM智能体方向论文汇编

> 本方向共 3 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Doctor-R1: Mastering Clinical Inquiry with Experiential Agentic Reinforcement Learning ｜经验驱动的智能体强化学习

研究机构：清华大学

作者：Yunghwei Lai、Kaiming Liu、Ziyue Wang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.04284)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.04284)

> 临床决策支持系统需解决在信息不完整环境下进行多步动态推理的问题，现有模型在静态基准上表现优异，但缺乏主动获取证据与情感沟通的能力。DOCTOR-R1 通过构建多智能体交互环境，结合双层奖励架构与经验库检索，训练模型掌握战略询问与共情沟通。该方法在 HealthBench 上以 8B 参数规模超越多个专有模型，验证了增强询问能力可提升决策准确性，但其依赖 LLM 评估器的可靠性仍存疑。

】

---

【From Conversation to Query Execution: Benchmarking User and Tool Interactions for EHR Database Agents ｜电子健康记录交互式查询基准

研究机构：韩国科学技术院

作者：Gyubok Lee、Woosog Chay、Heeyoung Kwak 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.23415)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.23415)

> 临床数据访问面临用户提问模糊与数据库术语不匹配的双重障碍，传统静态文本转SQL基准无法评估智能体在动态对话中消解歧义与调用工具的能力。EHR-ChatQA通过构建包含LLM模拟用户与验证器的交互式环境，首次量化了智能体在随机对话路径下的鲁棒性缺陷。该基准揭示了当前最优模型在“至少一次成功”与“五次全部成功”间存在高达60%的性能鸿沟，证明了现有智能体在安全关键场景中的不可靠性，但其评估局限于单智能体架构，未验证多智能体协作对一致性的增益。

】

---

【KNOWGUARD: KNOWLEDGE-DRIVEN ABSTENTION FOR MULTI-ROUND CLINICAL REASONING ｜知识驱动弃权

研究机构：香港中文大学

作者：Xilin Dang、Kexin Chen、Xiaorui Su 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_50424908)

> 临床决策中，模型在信息不足时往往给出过度自信的误诊，现有弃权方法依赖内部置信度评估，缺乏外部证据验证机制。本文提出“先调查后弃权”范式，通过系统探索医学知识图谱识别证据缺口，而非仅计算置信度。该方法在开放域多轮临床基准上，将诊断准确率提升至74.12%，平均交互轮次控制在5.40轮。其价值在于将弃权从概率校准转化为知识边界检测，但知识图谱的静态构建与单智能体架构限制了其在复杂共病场景下的泛化能力。

】
