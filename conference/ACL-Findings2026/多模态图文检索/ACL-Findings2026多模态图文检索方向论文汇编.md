# ACL-Findings2026 · 多模态图文检索方向论文汇编

> 本方向共 7 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AFMRL: Attribute-Enhanced Fine-Grained Multi-Modal Representation Learning in E-commerce ｜属性增强细粒度多模态表示学习

作者：Biao Zhang、Lixin Chen、Bin Zhang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.20135)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_83468a9d6fdb)

> 电商场景下的商品检索要求模型区分视觉高度相似但属性细微差异的单品，传统双编码器因全局嵌入模糊了局部属性绑定而失效。现有基于多模态大语言模型（MLLM）的嵌入方法虽提升了语义理解，但受限于因果注意力机制，难以直接利用区域级细粒度信号。本文提出AFMRL框架，通过解耦“表示模型”与“属性生成器”，利用生成式属性提取解决硬负样本歧义，并引入检索感知的强化学习闭环优化。该方法在电商基准上显著优于基线，但其依赖外部生成器的架构是否牺牲了实时检索效率，仍存疑。

】

---

【Benchmarking the Fine-Grained Discriminability in Image-Text Retrieval via Controlled Contrastive Differences ｜受控对比差异基准

研究机构：中国科学院、中国科学院大学

作者：Zhen Wang、Xi Zhou、Yating Yang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d19c809b4845)

> 多模态检索模型在常规基准上表现优异，却常检索到细节不一致的样本，暴露出全局嵌入对细微语义差异的钝感。现有评测仅关注整体相似度，无法量化模型对单一变量变化的判别力，导致细粒度能力被高估。本文通过构建仅存在一处受控差异的对比样本对，并定义细粒度对比判别准确率（FG-CDA），系统性地暴露了当前SOTA模型在实体情感、场景属性等细微特征上的判别短板。该基准为细粒度检索提供了必要的评估坐标，但其受控构造方式是否完全模拟真实长尾分布，仍存疑。

】

---

【Evaluating Perspectival Biases in Cross-Modal Retrieval ｜跨模态检索中的视角偏见评估

作者：Teerapol Saengsukhiran、Peerawat Chomphooyod、Narabodee Rodjananant 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e78203726d52)

> 多模态检索系统被期望在语言无关的语义空间中运作，但实际结果常受训练数据中语言流行度与文化关联的系统性偏差影响。现有评估体系聚焦于检索精度，缺乏量化这种“视角偏见”的专用指标与基准。本文构建了3XCM基准与DLBKL/SP指标，通过强制选择任务解耦语义忠实度与文化关联。该工作揭示了显式跨语言对齐在抑制偏见上的优势，但其评估协议基于封闭集选择，能否泛化至开放域大规模检索尚存疑。

】

---

【Generative Text-to-Image Retrieval via Hierarchical Identifiers and Semantic Internalization ｜生成式多模态对齐中的语义内化框架

研究机构：中国科学院、中国科学院大学

作者：Jie Huang、Junjie Wang、Xin Liao 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_24b8f3e99c5d)

> 文本到图像检索旨在从海量图库中定位与查询语义最匹配的视觉内容，但传统双塔模型因编码器独立导致细粒度交互缺失，单塔模型则因计算开销难以实时部署。生成式检索（Generative Retrieval, GR）将检索重构为标识符预测任务，试图兼顾效率与精度，却面临标识符语义判别性不足、硬对齐偏差及封闭集限制三大瓶颈。SIGMA 通过构建五级层级标识符并引入渐进式语义内化训练，实现了开放集下的动态索引。该框架在 Flickr30K 和 MS-COCO 上显著优于现有生成式基线，但其绝对性能是否超越对比学习 SOTA 仍存疑。

】

---

【MiMIC: Mitigating Visual Modality Collapse in Universal Multimodal Retrieval While Avoiding Semantic Misalignment ｜通用多模态检索中的模态坍塌与语义错位缓解

研究机构：南京大学

作者：Juan Li、Chuanghao Ding、Xujie Zhang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.21326)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.21326)

> 通用多模态检索（UMR）旨在将图像与文本映射至统一嵌入空间以支持跨模态匹配，但现有方法在融合策略上存在固有缺陷。早期融合模型易陷入视觉模态坍塌，晚期融合模型则面临语义错位，导致在缺失模态或复杂查询下检索性能骤降。MiMIC 通过解码器内融合架构与单模态混合训练策略，在保留模态独立性的同时实现动态聚合。该方法在 WebQA+ 与 EVQA+ 基准上超越了主流基线，但其对骨干网络规模的依赖及在完整模态场景下的相对优势仍需进一步审视。

】

---

【Region-R1: Reinforcing Query-Side Region Cropping for Multi-Modal Re-Ranking ｜区域裁剪强化学习

研究机构：美国德州农工大学

作者：Chan-Wei Hu、Zhengzhong Tu

论文原文见 [arXiv](https://arxiv.org/abs/2604.05268)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05268)

> 多模态检索增强生成（MM-RAG）的重排序阶段长期受困于查询图像中无关视觉干扰项对全局嵌入的污染，导致相似度计算失真。现有重排序方法如EchoSight和OMGM均假设查询表示固定，仅优化候选交互机制，忽略了查询侧视觉信息的动态可控性。本文提出Region-R1，将查询图像的区域选择形式化为强化学习决策问题，通过r-GRPO算法学习何时裁剪及裁剪何处。该方法在E-VQA和InfoSeek上将条件召回率@1分别提升20%和8%，但仅验证了单区域硬裁剪的有效性，未探讨软性注意力或多区域选择的潜力。

】

---

【Towards Visually Grounded Multimodal Summarization via Cross-Modal Transformer and Gated Attention ｜面向视觉接地多模态摘要的跨模态Transformer与门控注意力

研究机构：澳大利亚麦考瑞大学

作者：Abid Ali、Diego Molla-Aliod、Usman Naseem

论文原文见 [arXiv](https://arxiv.org/abs/2605.11753)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.11753)

> 多模态摘要生成旨在从图文混合文档中产出简洁摘要，但现有模型常将视觉特征浅层注入语言模型，导致跨模态语义对齐薄弱且图像选择冗余。本文切入点在于将图像子集选择视为摘要生成的内生组件而非后处理步骤，通过深度视觉处理器实现层对齐融合，并借助DPP教师蒸馏轻量级选择器。该框架在MSMO基准上实现了文本质量持平SOTA且视觉选择质量显著优于基线的效果，但其对“互补性”与“相关性”的区分能力仍存疑。

】
