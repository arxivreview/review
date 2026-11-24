# ACL-Findings2026 · 大语言模型智能体安全与运行时治理方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Safety Sidecar: Reflection-Driven Runtime Control for Safer Agents ｜安全侧车：基于反思驱动的运行时控制

研究机构：北京大学、厦门大学

作者：Wang Bin、Quan Jiazheng、Xingrui Yu 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ac4bf9f7ef33)

> 大语言模型智能体在自主执行多步任务时，微小的推理或检索偏差会被工作流放大为具有实际副作用的危险动作，而现有静态提示或事后过滤机制无法在动作执行前进行干预。本文提出 Safety Sidecar，一个即插即用的运行时控制模块，通过将反思过程转化为闭环控制器，在动作执行前检索证据并生成修复，同时利用外部验证器门控记忆更新。该方法在安全代码生成场景中验证了可行性，但其在通用工具调用场景下的泛化能力与验证器覆盖范围仍存疑。

】
