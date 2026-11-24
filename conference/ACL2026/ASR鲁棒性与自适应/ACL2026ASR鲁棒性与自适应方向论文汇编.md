# ACL2026 · ASR鲁棒性与自适应方向论文汇编

> 本方向共 3 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Listening Like Humans: Semantics-Guided Noise-Robust Multimodal Speech Recognition ｜语义引导的多模态语音重建

研究机构：香港科技大学、中山大学

作者：Yan Fang、Jun Chen、Yian Yao 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1711a2b0bb75)

> 噪声环境下的语音识别面临声学线索丢失导致的语义崩塌，现有方法多聚焦于信号增强或参数微调，难以在极端退化下恢复深层语义。本文提出将ASR重构为语义引导的语音重建任务，通过融合频谱图视觉特征与文本改写先验，在共享语义空间中对齐多模态信息。该方法在多个噪声基准上显著降低了词错误率并提升了语义相似度，但其性能增益高度依赖外部LLM生成的文本先验，且未充分验证视觉频谱特征相对于纯音频编码的独立信息增益。

】

---

【Look before Transcription: End-to-End SlideASR with Visually-Anchored Policy Optimization ｜视觉锚定策略优化

研究机构：北京交通大学

作者：Rui Hu、Delai Qiu、Yining Wang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.08618)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.08618)

> 学术讲座等场景下，ASR系统常因缺乏领域术语上下文而转录错误，传统流水线方法复杂且延迟高，而新兴的全模态大语言模型（OLLMs）虽具端到端潜力，却常退化为单纯的OCR系统。本文切入点在于识别并解决OLLMs在多模态输入下的行为不可控问题，通过强制结构化推理来约束模型行为。具体做法是提出VAPO后训练方法，利用强化学习引导模型执行“先看图后转录”的显式推理过程。该方法在实体密集场景下显著提升了转录准确率，但其对合成数据的依赖及真实场景泛化能力仍存疑。

】

---

【Mixture-of-Experts with Intermediate CTC Supervision for Accented Speech Recognition ｜混合专家与中间CTC监督的口音鲁棒语音识别

作者：Wonjun Lee、Hyounghun Kim、Gary Geunbae Lee

论文原文见 [arXiv](https://arxiv.org/abs/2602.01967)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.01967)

> 口音语音识别面临的核心矛盾在于：追求口音不变性的通用模型在重口音或未见口音上性能崩塌，而依赖口音标签的特化方法无法泛化至无标签推理场景。现有混合专家（Mixture-of-Experts, MoE）方案要么在测试时仍需标签，要么路由机制与转录质量脱节。MOE-CTC通过为每个专家配备独立的CTC头，将路由决策直接对齐至转录准确率，并采用两阶段训练实现从口音感知到口音无关的平滑过渡。该方法在MCV-ACCENT基准上取得了显著的性能提升，但其对训练期口音标签的依赖及序列级路由对混合口音的假设，限制了其在更复杂真实场景中的直接适用性。

】
