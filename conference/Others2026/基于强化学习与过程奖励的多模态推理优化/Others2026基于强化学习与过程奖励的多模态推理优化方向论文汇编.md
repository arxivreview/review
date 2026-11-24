# Others2026 · 基于强化学习与过程奖励的多模态推理优化方向论文汇编

> 本方向共 1 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【PaLMR: Towards Faithful Visual Reasoning via Multimodal Process Alignment ｜多模态过程对齐推理

研究机构：南京大学

作者：Yantao Li、Qiang Hui、Chenyang Yan 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.06652)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.06652)

> 多模态大模型在强化学习后训练中常出现“答案正确但推理过程幻觉”的现象，即模型利用语言先验而非视觉证据解题。现有基于最终答案的奖励机制无法区分视觉忠实推理与文本捷径，导致长链推理中视觉漂移加剧。PaLMR通过构建感知对齐数据层与过程对齐优化层，将视觉一致性作为二元可验证指标融入组相对策略优化，实现过程级视觉锚定。该方法在7B规模下显著降低幻觉率，但其依赖外部LLM评分的机制在目标模型能力超越评估器时失效，限制了其向更强模型的泛化能力。

】
