# ACL-Findings2026 · LLM游戏推理与决策方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Can Large Language Models Infer Human Actions and Motives? Evaluation in Social Prediction and Inspection Games ｜社会预测与检查博弈中的大语言模型动机推断

研究机构：美国南加州大学

作者：Kaleen Shrestha、Abhinav Gupta、Harish Dukkipati 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c6d196101900)

> 该方向旨在评估大语言模型（LLM）能否从历史交互中推断对手的潜在动机，并将其泛化至新情境。现有方法多依赖静态基准或实时对抗，缺乏对“动机-行为”因果链的细粒度诊断，导致无法区分LLM是真正理解了对手意图，还是仅匹配了表面统计规律。本文引入认知科学验证的社会预测博弈（SPG）与检查博弈（IG），通过对比人类与LLM在预测动作及跨情境泛化上的表现，揭示了LLM在动机推断上的结构性缺陷。这一发现挑战了LLM具备通用社会推理能力的假设，但其结论受限于特定博弈结构与温度设置，泛化性存疑。

】

---

【Do You Get the Hint? Benchmarking LLMs on the Board Game Concept ｜溯因推理基准：Concept 游戏

研究机构：比利时安特卫普大学

作者：Ine Gevers、Walter Daelemans

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ce81ab23342c)

> 大语言模型（LLM）在静态知识问答中表现优异，但在需要整合不完整线索、推断对手意图并动态修正假设的溯因推理任务中，其能力边界尚不明确。现有评测多聚焦于单轮语义匹配或完美信息博弈，缺乏对“线索-概念”映射中抽象推理与心智理论（Theory of Mind, ToM）交互的细粒度诊断。本文引入经典桌游 Concept 作为多语言基准，通过让 LLM 仅扮演猜测者并接收人类生成的分层线索，量化了模型在静态与动态设置下的推理失败模式。该基准揭示了 LLM 在低资源语言及序列信息更新中的显著劣势，但单侧评估设定可能掩盖了模型作为线索提供者时的策略缺陷。

】
