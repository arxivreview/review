# ACL2026 · AI生成媒体取证方向论文汇编

> 本方向共 3 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【From Form to Logic: Masked Reconstruction and Reasoning Distillation for Short Video Fake News Detection ｜短视频假新闻检测：掩码重建与推理蒸馏

研究机构：西北工业大学、合肥工业大学

作者：Qingyan Wang、Lianwei Wu、Botao Wang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_380150fd702f)

> 短视频假新闻检测旨在区分真实报道与包含认知伪造的合成内容，核心难点在于现有方法要么忽略细粒度跨模态冲突，要么依赖大语言模型（LLM）导致幻觉与高延迟。PCDD通过感知-认知双驱动架构，利用掩码多模态建模（M3）放大局部不一致，并通过正则性-关系-结果（R3）蒸馏将LLM推理链压缩至轻量模型。该方法在数据稀缺场景下实现了优于现有基线的检测精度与实时性，但其对全模态骨干的依赖及跨平台泛化能力仍存疑。

】

---

【MedForge: Interpretable Medical Deepfake Detection via Forgery-aware Reasoning ｜医疗影像篡改检测中的事前定位推理

研究机构：新加坡国立大学、香港中文大学

作者：Zhihui Chen、Kai He、Qingyuan Lei 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.18577)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.18577)

> 医疗影像篡改检测需同时满足高准确率与临床可验证性，但现有黑盒分类器缺乏证据，而通用多模态大语言模型（MLLM）的事后解释常伴随视觉幻觉。本文切入点是将检测重构为“先定位篡改区域，再基于该区域生成医学逻辑推理”的事前推理任务，并通过伪造感知组序列策略优化（Forgery-aware GSPO）显式奖励定位精度。该框架在自建基准上实现了99.23%的准确率与90.2%的推理质量评分，但其泛化能力受限于单一静态图像模态及自建数据集的封闭性，临床部署的鲁棒性仍存疑。

】

---

【Process Over Outcome: Cultivating Forensic Reasoning for Generalizable Multimodal Manipulation Detection ｜过程优于结果：培养取证推理以实现可泛化的多模态操纵检测

研究机构：合肥工业大学、西北工业大学

作者：Yuchen Zhang、Yaxiong Wang、Kecheng Han 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.01993)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.01993)

> 多模态新闻操纵检测（DGM4）旨在从图文对中发现伪造痕迹，但现有方法依赖结果导向监督，导致模型过拟合特定统计伪影，在未见域泛化能力不足。本文指出，仅优化最终分类标签无法让模型习得内在的取证逻辑，因此提出从“结果拟合”转向“推理驱动优化”。通过构建包含70万+推理标注的ROM数据集，并设计基于GRPO强化学习的三阶段训练框架REFORM，使模型显式生成逻辑一致的取证解释。该范式在跨域和零样本任务上显著优于基线，但其小模型优势是否完全源于推理链优化，还是受限于特定骨干网络，仍需进一步验证。

】
