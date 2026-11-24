# ACL-Findings2026 · 多模态幻觉缓解方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CCD: Mitigating Hallucinations in Radiology MLLMs via Clinical Contrastive Decoding ｜临床对比解码

研究机构：英国格拉斯哥大学

作者：Xi Zhang、Zaiqiao Meng、Jake Lever 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.23379)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.23379)

> 放射学多模态大语言模型在生成报告时，常因过度依赖提示中的临床文本而忽略图像证据，导致“临床幻觉”。现有通用对比解码方法在灰度医学影像上失效，且训练时干预面临隐私与算力瓶颈。CCD通过引入外部专家模型，在推理阶段以结构化标签和置信度分数双路校准Logits，实现免训练的幻觉抑制。该方法在MIMIC-CXR上显著提升了临床指标，但其对特定专家模型的依赖限制了跨模态泛化能力。

】

---

【DICA: Dual-Indicator Guided Contrastive Alignment in Multimodal Large Language Models ｜双指标引导对比对齐

作者：Hao Yang、Jin Wang、Xuejie Zhang

论文原文见 [arXiv](https://arxiv.org/abs/2607.23944)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.23944)

> 多模态大语言模型在视觉问答中常因注意力漂移或视觉证据利用不足产生幻觉，现有免训练方法往往采用统一的概率抑制策略，缺乏对具体失效模式的诊断能力。DICA通过引入视觉注意力熵与输出-图像相关性两个动态指标，在推理过程中实时监测并触发针对性的隐藏状态校正。该方法无需重训练即可在多个基准上提升准确率并降低幻觉率。其核心贡献在于将幻觉缓解从“统一修正”细化为“分型干预”，但阈值设定的跨架构泛化性及长序列下的指标稳定性仍存疑。

】

---

【Spotlight and Shadow: Attention-Guided Dual-Anchor Introspective Decoding for MLLM Hallucination Mitigation ｜双锚点内省解码

研究机构：澳门大学、香港科技大学

作者：Yebo Wu、Han Jin、Zhijiang Guo 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.10071)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10071)

> 多模态大语言模型（MLLMs）在生成过程中常因语言先验压倒视觉证据而产生幻觉，现有免训练对比解码方法依赖外部扰动构建负样本，既引入随机噪声导致语义偏移，又因额外前向传播增加1.83倍推理延迟。本文切入点在于发现模型内部层间存在“浅层幻觉高发”与“中层视觉感知峰值”的结构性差异，提出双锚点内省解码（Dual-Anchor Introspective Decoding, DAID），通过视觉注意力动态定位并对比内部层状态，在单次前向传播中同时放大视觉信号并抑制语言惯性。该方法在POPE基准上实现85.08%准确率，但相较于2026年SOTA方法存在显著性能差距，且未验证长序列场景下的有效性。

】
