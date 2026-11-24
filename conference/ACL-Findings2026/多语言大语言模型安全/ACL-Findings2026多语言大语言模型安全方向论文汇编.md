# ACL-Findings2026 · 多语言大语言模型安全方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Multilingual Refusal Alignment for Safer Large Language Models ｜多语言拒绝对齐：RefusEU 数据集与 DPO 跨语言迁移实验

研究机构：英国伦敦大学学院

作者：Aleksandra Krasnodębska、Wojciech Kusa、Aldo Lipani

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d35ff25464c6)

> 导读 多语言大语言模型在全球部署中面临安全行为不一致的困境，根源在于安全对齐数据对英语的过度依赖，导致模型在低资源语言中拒绝机制失效。现有方法多依赖翻译或单语对齐，但缺乏系统性的跨语言受控实验来验证单语对齐的迁移边界。本文构建了覆盖 12 种欧洲语言的 RefusEU 数据集，并采用消融安全机制后的模型作为基线，通过 DPO 训练量化不同数据配置下的安全恢复效果。该工作提供了首个欧洲多语言拒绝对齐基准，但其结论受限于特定语言家族，且未深入探讨安全与语言身份在表征空间中的纠缠机制。

】

---

【SEA-Guard: Culturally Grounded Multilingual Safeguard for Southeast Asia ｜东南亚文化接地多语言护栏模型

作者：Panuthep Tasawong、Jian Gang Ngui、Alham Fikri Aji 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0d007443ef3f)

> 现有安全护栏在东南亚低资源语言上因依赖机器翻译而丢失文化语境，导致对地区性敏感内容的检测失效。本文切入点在于构建首个基于多智能体合成框架生成的、覆盖8种东南亚语言的文化安全数据集，并训练专用护栏模型。通过蒙特卡洛推理集成（MCRE）解决标注不确定性，SEA-Guard在文化基准上显著优于通用SOTA，但在通用安全任务上仅具竞争力，其离线标注的高计算成本限制了实时部署潜力。

】
