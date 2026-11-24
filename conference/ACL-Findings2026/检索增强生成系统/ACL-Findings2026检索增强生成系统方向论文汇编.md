# ACL-Findings2026 · 检索增强生成系统方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Domain-Specific Data Generation Framework for RAG Adaptation ｜领域特定RAG适配的数据生成框架

研究机构：香港城市大学、北京大学

作者：Chris Xing Tian、Weihao Xie、Zhen Chen 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.11217)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.11217)

> 企业级RAG系统面临的核心矛盾是通用组件与领域术语分布的错位，导致检索精度与生成质量双降。现有适配方法多聚焦于单一组件（如仅微调嵌入模型或仅优化LLM），缺乏统一的数据监督源，且依赖人工标注或特定架构假设。RAGen通过自动化合成领域特定的问答上下文（QAC）三元组，为嵌入模型对比学习与LLM监督微调提供通用训练信号。该框架在三个垂直领域验证了数据质量对多组件适配的增益，但其效果高度依赖LLM生成质量，且未验证在大规模开放域语料上的泛化边界。

】

---

【Feedback Adaptation for Retrieval-Augmented Generation ｜反馈适应下的检索增强生成

研究机构：韩国成均馆大学

作者：Jihwan Bang、Seunghan Yang、Kyuhong Shim 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.06647)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8fc017c23852)

> 检索增强生成（RAG）系统在部署后常因知识过时或错误而需人工修正，但现有评估仅关注静态准确率，无法量化系统对反馈的响应速度与泛化能力。本文提出“反馈适应”新问题，定义修正延迟与反馈后性能双轴指标，揭示训练式方法在延迟与可靠性间的结构性权衡。通过推理时存储与检索反馈补丁的 PatchRAG 机制，实现无重训练下的即时行为更新。该框架填补了动态交互场景的评估空白，但其单路检索设计与静态快照协议限制了结论向复杂在线环境的推广。

】
