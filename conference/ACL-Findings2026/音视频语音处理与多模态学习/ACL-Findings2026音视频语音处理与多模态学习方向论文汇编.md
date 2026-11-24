# ACL-Findings2026 · 音视频语音处理与多模态学习方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Bridging the Temporal Gap in Multimodal LLMs: Deeply Stacking Temporal Tokens for Audio-Visual Speech Recognition ｜弥合多模态大语言模型中的时序鸿沟：深层堆叠时序令牌用于视听语音识别

研究机构：北京科技大学、清华大学

作者：Liyong Wang、Junliang Xing、Tianyu Hu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9d8825c79ba5)

> 视听语音识别（AVSR）旨在利用唇部运动等视觉线索补偿噪声环境下的音频退化，但当前基于多模态大语言模型（MLLMs）的方法存在根本性的时序鸿沟：视觉编码器缺乏细粒度时序建模，且时序语义在LLM深层解码器中逐步退化。本文指出这一被忽视的缺陷，通过在视觉编码器引入时序感知注意力（TAA）与T-RoPE，并在LLM解码器早期层堆叠层级化时序令牌（HSTT），在LRS2和LRS3基准上实现了显著的性能提升。该方法在LLM-based AVSR中处于第一梯队，但其对深层语义推理的时序贡献及与稀疏对齐策略的优劣对比仍存疑。

】

---

【Two Heads Are Better Than One: Audio-Visual Speech Error Correction with Dual Hypotheses ｜双假设生成式纠错：在语言空间解耦视听模态

研究机构：韩国科学技术院

作者：Sungnyun Kim、Kangwook Jang、Sungwoo Cho 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.13281)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.13281)

> 导读 视听语音识别（AVSR）在噪声环境下依赖视觉线索补偿音频退化，但现有生成式错误纠正（GER）框架多采用特征级融合，导致单模态噪声污染统一表征，限制了纠错上限。本文切入点在于将模态融合延迟至语言空间，利用独立ASR与VSR模型生成双路假设，由大语言模型（LLM）进行组合推理。具体做法是提出DualHyp框架，并引入RelPrompt机制提供时间对齐的模态可靠性信号以引导LLM动态选择可信源。该范式在LRS2噪声基准上实现了显著的错误率降低，但其性能高度依赖VSR头的质量，且在真实世界复杂场景下的泛化能力尚待验证。

】
