# ICLR2026 · ASR鲁棒性与自适应方向论文汇编

> 本方向共 2 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CONFIDENT AND ADAPTIVE GENERATIVE SPEECH RECOGNITION VIA RISK CONTROL ｜基于风险控制自适应假设集选择的生成式语音识别纠错

作者：Amit Damri、Bracha Laufer-Goldshtein

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_15128053)

> 生成式语音识别纠错（GER）旨在利用大语言模型（LLM）修复自动语音识别（ASR）输出的错误，但现有方法普遍采用固定大小的N-best假设集，导致在简单音频上浪费计算资源，在复杂音频上引入噪声假设。本文指出固定N值缺乏对输入难度的感知，且无法提供性能退化的统计保证，切入点在于将假设集大小视为动态变量。通过引入Learn then test (LTT) 框架，基于ASR置信度分数动态调整假设集大小，并在高概率下控制相对词错误率（WER）退化。该方法在保持或提升纠错精度的同时显著降低了计算开销，但其理论保证依赖于校准集分布与测试集分布的交换性假设，在极端分布偏移场景下的鲁棒性尚需验证。

】

---

【Pay Attention to CTC: Fast and Robust Pseudo-Labelling for Unified Speech Recognition ｜统一语音识别中的CTC驱动伪标签生成

研究机构：英国帝国理工学院

作者：Alexandros Haliassos、Rodrigo Mira、Stavros Petridis

论文原文见 [arXiv](https://arxiv.org/abs/2602.19316)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.19316)

> 统一语音识别（USR）旨在通过单一模型同时处理音频、视觉及视听语音识别，但现有半监督框架依赖自回归（AR）解码生成伪标签，导致训练耗时且易在分布外（OOD）数据上累积错误。本文指出AR解码的串行依赖与解耦监督是鲁棒性瓶颈，提出CTC驱动教师强制策略，利用CTC贪心解码结果并行生成注意力伪标签。该方法将训练时间缩短近2倍，并在长序列与噪声场景下显著降低词错误率（WER），但其对全局语义连贯性的依赖在推理阶段仍存在潜在风险。

】
