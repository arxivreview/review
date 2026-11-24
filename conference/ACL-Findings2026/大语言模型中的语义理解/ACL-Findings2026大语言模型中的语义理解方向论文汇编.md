# ACL-Findings2026 · 大语言模型中的语义理解方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Comparing Human and Large Language Model Interpretation of Implicit Information ｜隐含信息提取中的人机认知对齐差异

研究机构：意大利米兰理工大学

作者：Antonio De Santis、Tommaso Bonetti、Andrea Tocchetti 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17085)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17085)

> 导读 大语言模型（LLM）在生成流畅文本时，常将字面意义与隐含意义混淆，导致其在需要推断言外之意的场景中表现保守或过度发散。现有评估多聚焦于显式事实抽取或单一维度的语义一致性，缺乏对“可推断内容”这一开放集合的结构化对比，无法量化模型与人类在推理边界上的具体分歧。本文提出隐含信息提取（Implicit Information Extraction, IIE）框架，通过构建双层知识图谱并引入众包人类判断作为基准，系统解析了模型在推断严格性、时间关系解析及共识形成上的行为特征。该研究揭示了LLM在社会语境下比人类更保守、在事实语境下人类更保守的反直觉现象，但受限于小样本规模与黑盒评估，其结论对模型内部机制的解释力仍存疑。

】

---

【Emergence and Localisation of Semantic Role Circuits in LLMs ｜语义角色电路的因果定位与时间涌现

研究机构：英国曼彻斯特大学

作者：Nura Aljaafari、Danilo Carvalho、Andre Freitas

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1d11346a4cab)

> 大语言模型（LLMs）在事实回忆和算术任务中已被证实存在局部化电路，但抽象语义结构（如谓词-论元绑定）是否由因果功能性的内部机制实现，仍缺乏直接证据。现有机制可解释性研究多聚焦于静态检查点或特定算法行为，忽略了语义电路在训练过程中的形成时序与跨规模迁移性。本文提出 COMPASS 方法，结合对比最小对、边归因电路发现与训练时间追踪，揭示语义角色电路的局部化、渐进涌现及跨架构保守性。该工作为浅层语义结构的机制解释提供了因果证据，但受限于浅层角色定义与单一任务范式，其结论向深层语义泛化的边界尚不明确。

】

---

【Mechanistic Insights into Deferred Semantic Drift in LLMs ｜延迟语义漂移机制

研究机构：大连理工大学

作者：Jingjie Zeng、Huayang Li、Liang Yang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1fae9d195424)

> 因果Transformer在处理歧义词时，其初始表征因单向信息流限制而无法即时更新，导致语义消解存在延迟。现有机制可解释性研究多聚焦静态特征定位，缺乏对动态语义更新过程的追踪。本文提出“延迟语义漂移”机制，通过非因果Oracle诊断与注意力值向量分析，揭示后续token如何主动检索并整合歧义信息。该工作提供了因果验证的新视角，但受限于单一模型架构与自建数据集，其泛化性存疑。

】
