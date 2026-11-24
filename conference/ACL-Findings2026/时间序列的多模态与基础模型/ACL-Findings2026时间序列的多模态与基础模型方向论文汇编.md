# ACL-Findings2026 · 时间序列的多模态与基础模型方向论文汇编

> 本方向共 4 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CaTS-Bench: Can Language Models Describe Time Series? ｜时序描述基准

研究机构：意大利罗马第一大学

作者：Luca Zhou、Pratham Yashwante、Marshall Fisher 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.20823)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.20823)

> 时序描述生成（Time Series Captioning, TSC）旨在将原始数值序列转化为人类可读的自然语言摘要，以辅助金融、医疗等领域的快速决策。现有基准多依赖模板化合成数据，缺乏真实语境与视觉模态，导致模型评估无法反映实际场景下的数值幻觉与语义偏差。本文构建了包含1746个人工重写金标准样本的多模态基准，并验证了基于合成数据微调开源视觉语言模型（VLM）的有效性。该工作填补了生成式时序评估的空白，但暴露了当前VLM在视觉结构理解上的系统性失效。

】

---

【CTRL: Control-Based Time Series Forecasting with LLM-Guided Residual Learning ｜基于LLM控制信号的时序预测框架

研究机构：韩国延世大学

作者：Minkyoung Kim、Daeun Ji、Yohan Lee 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b09bf6da9a7a)

> 导读 多模态时序预测旨在融合外部语义信息以提升非平稳场景下的鲁棒性，但现有方法常将大语言模型（LLM）降级为数值预测器，导致精度受损或预测不稳定。CTRL框架的核心切入点在于解耦语义推理与数值计算，将冻结的LLM定位为战略控制器而非直接预测器。该框架通过LLM分析骨干网络误差并生成紧凑控制信号，驱动轻量级残差解码器进行修正，同时引入无标签测试时适应机制以应对分布偏移。这一设计在显著降低LLM调用开销的同时提升了非平稳序列的预测精度，但其对平稳数据集的增益有限，且依赖特定骨干网络的误差特征。

】

---

【Enhancing Zero-Shot Time Series Forecasting in Off-the-Shelf LLMs via Noise Injection Prompting ｜噪声注入增强的大语言模型零样本时序预测

作者：Xingyou Yin、Ceyao Zhang、Min Hu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4115ac1063ff)

> 现有基于大语言模型（LLM）的时序预测方法多依赖微调或复杂适配器以弥合数值与文本的模态鸿沟，但完全冻结的“开箱即用”LLM在面对分布偏移时表现出严重的输入脆弱性。NLTS通过一种非侵入式的推理时策略，在原始时序数据分词前注入受控随机噪声，迫使模型依赖底层时间结构而非表面数值特征进行预测。该方法无需任何参数更新或额外训练，理论上证明了噪声注入能降低泛化误差，并在多个基准上显著优于传统基线。尽管其提升了零样本预测的鲁棒性，但噪声强度的选择依赖验证集调参，且未解决LLM对复杂因果关系的深层理解缺失。

】

---

【LLaTiSA: Towards Difficulty-Stratified Time Series Reasoning from Visual Perception to Semantics ｜分层时序推理模型

研究机构：阿里巴巴集团

作者：Yueyang Ding、HaoPeng Zhang、Rui Dai 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17295)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17295)

> 时序推理（Time Series Reasoning, TSR）旨在让模型从数值证据、模式感知到语义判断中构建对时间序列的综合理解，但现有基准缺乏统一的任务分层定义且标签存在模糊性，导致高级推理建立在不可靠的基础接地之上。本文切入点在于指出当前模型在基础数值读取（L1）上的失败是高层推理失效的根源，而非单纯缺乏语义能力。通过构建四级认知分类法与配套数据集HITSR，并采用双视图输入与三阶段课程微调训练VLM，LLATISA实现了从定性视觉直觉到定量数值精度的桥接。该工作确立了时序推理的评估基线，但其对长序列处理效率及真实世界复杂因果场景的泛化能力仍存疑。

】
