# ACL-Findings2026 · 人类与LLM标注质量方向论文汇编

> 本方向共 4 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Herd of Language Models Makes a Better Zero-shot Annotator for Clinical Named Entity Recognition ｜多LLM临床命名实体识别中的上下文感知标签聚合

作者：Seiji Shimizu、Shoko Wakamiya、Eiji Aramaki

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2acd2916a503)

> 临床命名实体识别（NER）的规模化瓶颈在于高质量标注语料的获取成本与数据共享限制。现有零样本大语言模型（LLM）标注方案在临床文本中表现受限，且单一模型输出存在系统性偏差，简单集成策略难以平衡精确率与召回率。本文提出 MARY 框架，通过域自适应预训练与加权对比学习，在表示空间中锚定类别中心，从而选择性整合少数派模型提取的实体。该方法在 i2b2 2010 等基准上显著优于单模型及传统标签模型，但其性能增益高度依赖冲突消解等预处理步骤，且未验证在缺乏高置信度锚点时的鲁棒性。

】

---

【BNLP: A Text Annotation Platform for Quality Control of LLM-Generated Annotations ｜BNLP：面向 LLM 辅助标注的质量控制平台

研究机构：中国科学院、美国普林斯顿高等研究院

作者：Xinhao Zhuang、Qiongyu Tian、Yalin Chen 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9f8d9e2efa06)

> 导读

】

---

【Decomposing Unitization and Typing for Efficient and Consistent Span-Bound Concept Annotation ｜概念标注任务分解

研究机构：美国卡内基梅隆大学、美国芝加哥大学

作者：Nupoor Gandhi、Michael Bada、Emma Strubell

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9d8a911f4251)

> 领域专家标注面临高昂的时间成本与标注者间一致性瓶颈，传统全跨度标注将语义判断与语言学边界选择耦合，导致低资源场景下数据量受限。现有LLM辅助标注方案多直接生成完整实体，但在专业领域少样本性能不足，且未解决边界决策的主观性噪声。本文提出将标注解耦为“类型位置标注”与“跨度边界检测”，由人工仅标记位置，模型推断边界。该策略在低预算下显著提升了数据效用与一致性，但其收益高度依赖跨度检测模型的准确率，高预算场景下优势消失。

】

---

【From Fallback to Frontline: When Can LLMs be Superior Annotators of Human Perspectives? ｜视角采择的统计估计重构

研究机构：美国普渡大学、美国圣路易斯华盛顿大学

作者：Hasan Amin、Harry Yizhou Tian、Xiaoni Duan 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17968)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17968)

> 主观标注长期面临“无客观真值”与“群体视角难以直接观测”的双重困境，传统方法将LLM视为人类标注的廉价替代品，却忽视了二者在统计估计属性上的本质差异。本文切入点在于将视角采择（Perspective-Taking, PT）从“测量个体意见”重构为“估计潜在群体均值”，从而在缺乏金标准的主观任务中建立人类与LLM的可比性。通过引入偏差-方差-相关性分解框架与双镜头误差模型，论文量化了LLM在低预算下作为一线估计器的结构性优势。这一范式转换挑战了“LLM仅能作为后备”的领域共识，但其优势边界严格依赖于群体在训练数据中的覆盖度，对低 prevalence 群体的适用性仍存疑。

】
