# ACL-Findings2026 · 视觉-语言模型的测试时自适应方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【DANCE: Diversity-attended Dynamic Caching with Asymmetric Quantization for Test-time Adaptation of Vision-Language Models ｜多样性感知动态缓存与非对称量化测试时适应

研究机构：北京大学

作者：Shunge Zou、Changhu Wang、Wei Ju 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4dee2167eda1)

> 视觉语言模型在分布偏移下的零样本性能退化，传统测试时适应方法依赖熵最小化筛选高置信样本，导致缓存覆盖度不足且检索不稳定。DANCE 通过引入“可靠性-新颖度”双门控机制维护动态缓存，并采用非对称量化（Asymmetric Quantization, AQ）作为统一检索原语，解决了流式数据下的原型漂移问题。该方法在跨域泛化任务上显著优于现有缓存基线，但其理论保证仅覆盖二元分类场景，且未与最新提示调优SOTA进行直接对比。

】

---

【Structured Confidence–Guided Online Adaptation for LLM-based Multi-Label Classification ｜结构化置信度引导的在线测试时适应

作者：Pengyu Xu、JingRen Hou、Liping Jing 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bfeac332b935)

> 大语言模型（LLMs）在零样本多标签文本分类中表现优异，但静态推理无法应对流式测试数据中的分布偏移与长尾标签退化。现有在线测试时适应（OTTA）方法依赖序列似然作为置信度信号，却因标签共享前缀导致“置信度幻觉”，使错误预测被反复复用。本文提出SCOTTA，通过标签集局部似然比（L3R）精准定位解码分支点的真实竞争，并结合子模记忆库（SMB）在固定预算下平衡标签覆盖与语义多样性，实现无参数更新的持续适应。该方法在四个基准上显著提升了长尾标签的Macro-F1，但其效果高度依赖子模优化的计算开销与标签空间结构，在极端动态分布下的稳定性仍存疑。

】
