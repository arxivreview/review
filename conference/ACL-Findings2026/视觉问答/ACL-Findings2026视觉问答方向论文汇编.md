# ACL-Findings2026 · 视觉问答方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Chain-of-Procedure: Hierarchical Visual-Language Reasoning for Procedural QA ｜视觉程序问答中的粒度对齐与层级推理

研究机构：澳门大学

作者：Guanhua Chen、Yutong Yao、Shenghe Sun 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4517046165a8)

> 视觉程序问答（VP-QA）要求模型根据中间状态图像预测复杂任务的下一步操作，但现有视觉语言模型（VLMs）在处理静态快照时，常因文本步骤的粗粒度与视觉证据的细粒度不匹配而失效。本文指出，直接对齐导致模型无法识别隐含的原子动作，从而在跨程序检索与状态定位上表现不佳。为此，论文构建了ProcedureVQA基准，并提出链式程序（Chain-of-Procedure, CoP）框架，通过检索、分解与预测三阶段解耦推理过程。该工作揭示了VLMs在因果推理上的短板，但其在非结构化任务上的泛化能力仍存疑。

】

---

【CoGR-MoE: Concept-Guided Expert Routing with Consistent Selection and Flexible Reasoning for Visual Question Answering ｜概念引导专家路由与选项感知重加权

研究机构：香港科技大学

作者：Xiyin Zeng、Yi Lu、Hao Wang

论文原文见 [arXiv](https://arxiv.org/abs/2604.16930)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16930)

> 视觉问答（VQA）中混合专家（MoE）架构面临路由稳定性与选项区分灵活性的内在矛盾：稳定路由导致专家固化，削弱细粒度判别；不稳定路由则引发同类问题专家选择漂移。现有方法多从嵌入空间或交互特征入手，未能解耦“选谁”与“怎么用”两个环节。CoGR-MoE 通过 LLM 生成正负语义线索，将正确答案的语义方向注入路由层以稳定 Top-K 专家选择，再利用各选项自身线索对共享专家输出进行动态重加权，生成选项特定表示。该方法在 MRAG-Bench 上取得 63.25% 准确率，较最强基线 MoME 提升 0.49%，但在 Others 子集上仍落后于交互驱动路由方法，其语义引导策略对复杂跨模态交互的覆盖能力存疑。

】

---

【SimpleOCR: Rendering Visual Questions to Teach MLLMs to Read ｜视觉化问题训练策略

研究机构：美国卡内基梅隆大学、美国密歇根大学

作者：Yibo Peng、Peng Xia、Ding Zhong 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b2d4504c1c1b)

> 多模态大语言模型（MLLMs）在具备强大光学字符识别（OCR）能力的同时，存在严重的“模态懒惰”现象，即推理时过度依赖文本通道捷径而忽视图像中的视觉文本证据。现有强化学习方法聚焦于逻辑推导或图像扰动鲁棒性，缺乏强制模型激活视觉文本提取路径的结构化约束。本文提出SimpleOCR，通过将所有训练样本转化为视觉化问题（VQ）格式，在输入层面消除文本捷径，迫使模型通过视觉通道解码问题内容。该策略以极低的数据成本实现了分布外泛化的显著提升，但其对纯几何推理任务的轻微负迁移表明，视觉接地与抽象逻辑推理之间存在尚未解耦的张力。

】
