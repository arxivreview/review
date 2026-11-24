# ACL-Findings2026 · 语言模型的可解释性与可解释性方向论文汇编

> 本方向共 7 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Aligning What LLMs Do and Say: Towards Self-Consistent Explanations ｜归因自一致性优化

研究机构：以色列理工学院、英伟达研究院

作者：Sahar Admoni、Ofra Amir、Assaf Hallak 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2506.07523)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2d4420d24e74)

> 大语言模型生成的解释常与其实际决策所依赖的输入特征脱节，导致用户信任被误导。现有忠实度评估方法计算成本高昂，且缺乏将评估指标转化为训练信号以直接改善对齐的机制。本文通过构建大规模归因-解释配对基准，并利用直接偏好优化微调模型，使解释的归因向量与决策的归因向量在秩相关上显著对齐。该方法在保持任务准确率的前提下提升了自一致性，但其改进是否真正反映因果机制的忠实性，还是仅优化了归因分布的统计匹配，仍存疑。

】

---

【From Scoring to Explanations: Evaluating SHAP and LLM Rationales for Rubric-based Teaching Quality Assessment ｜基于SHAP与LLM推理的评分忠实度评估框架

研究机构：德国慕尼黑工业大学、瑞典隆德大学

作者：Ivo Bueno、Babette Bühler、Philipp Stark 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.05180)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.05180)

> 该方向旨在解决高利害教育场景中，不透明模型生成的评分缺乏可审计依据的问题。现有方法或依赖注意力权重（因果性弱），或依赖LLM自由文本解释（忠实性低），导致教师无法有效质疑自动化判断。本文切入点在于将句子级SHAP归因与LLM生成的句子排名进行系统性对比，并通过删除测试量化其因果影响。其价值在于提供了跨架构的解释迁移评估协议，但结论局限于特定教育数据集，且未探讨句子级归因对Token级细节的掩盖效应。

】

---

【GeoLAN: Geometric Learning of Latent Explanatory Directions in Large Language Models ｜几何潜空间正则化框架

研究机构：美国佛罗里达大学

作者：Tianyu Bell Pan、Damon L. Woodard

论文原文见 [arXiv](https://arxiv.org/abs/2603.19460)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.19460)

> 大语言模型（LLM）在高风险场景部署面临黑盒决策的审计危机，现有后验归因方法难以保证解释的因果忠实性。本文切入点在于将可解释性从推理时的特征发现前移至训练时的几何结构约束，通过强制潜空间各向同性来消除表示坍缩。具体做法是引入基于Kakeya猜想衍生的Wolff公理，设计两个可微分损失函数在训练阶段重塑Token轨迹的几何形态。该框架在中等规模模型上验证了几何约束对解释指标的提升，但在小模型上引发性能退化，且缺乏与主流机制可解释性方法的直接因果对比。

】

---

【LLM-Guided Semantic Bootstrapping for Interpretable Text Classification with Tsetlin Machines ｜基于大语言模型引导的Tsetlin Machine语义引导框架

研究机构：美国斯坦福大学、美国加州大学尔湾分校

作者：Jiechao Gao、Rohan Kumar Yadav、Yuangang Li 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12223)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12223)

> 该方向旨在解决符号模型在高风险领域部署时，因缺乏语义泛化能力而导致的性能瓶颈。现有方案要么依赖不透明的预训练语言模型（PLM），要么使用静态词向量增强符号模型，均无法兼顾透明性与语义深度。本文切入点在于利用大语言模型（LLM）离线生成结构化合成数据，引导非否定Tsetlin Machine（NTM）提取可解释的字面量特征，再注入真实数据微调。该方法在保持完全符号透明性的同时，将Tsetlin Machine（TM）的性能提升至接近BERT的水平，但其对LLM生成数据质量的依赖及缺乏因果验证的评估体系仍存疑。

】

---

【LLM-induced Rationales for More Compact Explainable Style Classification Models ｜基于LLM推理短语聚类的紧凑可解释特征工程

作者：Ahmad Aljanaideh、Saeb Ganideh

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_927aaeb63068)

> 该方向旨在解决线性分类器在风格识别任务中特征维度爆炸导致解释性丧失的问题。现有词级聚类方法虽能提升性能，但需为词汇表中每个词单独训练聚类模型，导致特征数量庞大且语义碎片化。本文切入点在于利用大语言模型（LLM）直接提取支持标签的语义短语（Rationale），并对其进行聚类以构建紧凑特征空间。通过GPT-4o mini提取短语并采用K-means聚类，该方法在保持与词级基线相当性能的同时，将特征数量减少了85-99%。这一策略验证了LLM辅助特征发现的可行性，但其对LLM幻觉的鲁棒性及因果忠实性缺乏严格验证。

】

---

【Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models ｜可操作机制可解释性：从定位到干预的工程化框架

研究机构：复旦大学、德国慕尼黑大学

作者：Hengyuan Zhang、Zhihao Zhang、Ercong Nie 等 28 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7986d401ebad)

> 机制可解释性（Mechanistic Interpretability, MI）长期被视为一种观察科学，旨在逆向工程大语言模型（LLMs）的内部计算逻辑，但现有综述多止步于“理解”层面，缺乏将洞察转化为模型改进动作的系统性协议。本文指出，随着外部扩展（Scaling）遭遇瓶颈，模型优化必须转向内部机制的“外科手术式”干预，然而当前领域缺乏统一的方法分类与实施指南。为此，本文构建了“定位-引导-改进”（Locate, Steer, and Improve）流水线，将MI重构为可操作的工程工具。该框架通过形式化定义可解释对象与干预方法，为对齐、能力与效率优化提供了具体路径，但其有效性依赖于尚未标准化的因果验证基准，实际收益的量化仍存疑。

】

---

【Tree-of-Evidence: Efficient "System 2" Search for Faithful Multimodal Grounding ｜证据树搜索：多模态临床预测的推理时忠实性验证

研究机构：美国佐治亚理工学院

作者：Micky C. Nnamdi、Benoit L. Marteau、Yishan Zhong 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.07692)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07692)

> 多模态大模型在医疗高风险场景中的部署面临“黑盒”决策不可审计的困境，现有注意力权重或后验归因方法无法提供可验证的硬证据轨迹。ToE 将解释问题重构为离散搜索问题，通过轻量级证据瓶颈与束搜索算法，在推理时动态定位支持预测的最小证据子集。该方法在严格证据预算下保留了全输入模型98%以上的预测性能，但仅验证了晚期融合架构，且其忠实性依赖于基础模型本身的逻辑正确性。

】
