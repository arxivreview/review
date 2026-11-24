# ICASSP2026 · 注意力机制变体与效率方向论文汇编

> 本方向共 1 篇（ICASSP2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Do we really need Self-Attention for Streaming Automatic Speech Recognition? ｜流式语音识别中自注意力的局部算子本质与卷积替代方案

作者：Youness Dkhissi、Valentin Vielzeuf、Elys Allesiardo 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.19960)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.19960)

> 流式自动语音识别（Streaming ASR）要求模型在固定时间块内完成转录，无法访问未来或过远的过去上下文。传统 Conformer 架构中的自注意力模块旨在捕获长程依赖，但在严格流式约束下，其全局视野被物理截断，导致计算成本与功能收益严重失衡。本文通过可视化诊断发现，流式场景下自注意力权重自发坍缩至对角线附近，实质退化为昂贵的局部算子。作者提出用可变形卷积替换或直接移除自注意力，在保持词错误率（WER）持平的前提下大幅降低参数量与实时因子（RTF）。这一发现挑战了“流式 ASR 必须依赖注意力机制”的默认假设，但结论局限于特定块大小与数据集，对跨块长程依赖的捕获能力未做深入验证。

】
