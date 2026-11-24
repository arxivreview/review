# ACL-Findings2026 · 多语言推理方向论文汇编

> 本方向共 6 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Enhancing Multilingual Reasoning via Steerable Model Merging ｜可引导模型合并

研究机构：北京邮电大学、复旦大学

作者：Zhuoran Li、Rui Xu、Jian Yang 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7e05d33c8dc4)

> 多语言推理面临的核心困境是：固定权重的模型合并策略无法同时满足高资源语言的推理保真与低资源语言的语义理解，导致性能在两类语言间此消彼长。现有静态合并方法将多语言编码器与推理LLM的特征以恒定比例拼接，忽视了输入语言特性对最优融合比例的动态需求。本文提出ST-Merge，通过门控交叉注意力机制根据输入语言动态调节两个源模型的贡献权重，实现输入感知的自适应融合。该方法在21种语言的四个基准上验证了有效性，但其性能上限受限于7B参数骨干模型，且门控机制对离散选择类任务的增益有限。

】

---

【From Representation to Choice: Tracing Decision Emergence Across Languages in LLMs ｜从表示到选择：追踪大语言模型跨语言决策涌现

研究机构：印度理工学院坎普尔分校、三星研究院

作者：Divyanshu Bhatt、Abhinav Joshi、Ujjaval Patel 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7541fa42f785)

> 多语言大语言模型（LLMs）在回答不同语言问题时，内部推理路径如何演化尚不明确。现有研究多聚焦于静态表示相似度或最终准确率，忽略了决策形成的动态时序特征，导致无法解释为何相同语义在不同语言下表现差异巨大。本文通过构建层解析的决策轨迹，将推理过程建模为随机过程，量化了跨语言分歧的具体发生位置。这一视角揭示了英语中心主义在决策层的微观机制，但仅作为诊断工具，未直接提供性能优化方案。

】

---

【Language-Coupled Reinforcement Learning for Multilingual Retrieval-Augmented Generation ｜语言耦合强化学习用于多语言检索增强生成

研究机构：北京交通大学、清华大学

作者：Rui Qi、Fengran Mo、Yufeng Chen 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.14896)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2866bb327d19)

> 多语言检索增强生成（Multilingual Retrieval-Augmented Generation, MRAG）面临的核心矛盾是模型在跨语言查询中产生的知识偏差与检索结果间的事实冲突。现有单轮检索与独立优化策略无法同时解决这两类问题，导致模型在语言多样性增加时性能急剧下降。LCRL通过语言耦合的组相对策略优化（Group Relative Policy Optimization, GRPO）与分层多轮检索机制，将多语言决策与经验奖励统一在强化学习框架内。该方法在知识密集型问答任务上显著优于基线，但其对通用推理能力的泛化效果及内部表征干预的缺失仍是存疑点。

】

---

【Large Reasoning Models Are (Not Yet) Multilingual Latent Reasoners ｜多语言潜在推理的机制诊断

研究机构：德国慕尼黑大学

作者：Yihong Liu、Raoyuan Zhao、Hinrich Schuetze 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.02996)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b496606e361b)

> 大语言模型在多语言任务中常依赖显式思维链，但内部隐藏状态往往在文本生成前已形成答案，这种“潜在推理”机制此前仅在英语中被研究。现有干预方法如强化学习或表示工程侧重性能提升，却缺乏对内部计算动态的跨语言量化证据。本文通过截断推理轨迹与Logit Lens分析，系统测量了11种语言下潜在推理的强度与内部路径一致性。该工作提供了关键的机理诊断，但受限于仅覆盖数学任务且未提出干预策略，其结论向其他推理域迁移的有效性尚存疑。

】

---

【Why Do Multilingual Reasoning Gaps Emerge in Reasoning Language Models? ｜选择性翻译

作者：Deokhyung Kang、Seonjeong Hwang、Daehui Kim 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.27269)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.27269)

> 推理语言模型（Reasoning Language Models, RLMs）在多语言任务中普遍存在性能落差，现有方法多聚焦于训练阶段的权重调整或推理阶段的强制语言对齐，却忽视了差距产生的具体环节。本文指出，该落差主要源于模型在将非英语输入转化为内部英语推理轨迹时的“理解失败”，而非推理逻辑本身的缺陷。通过构建基于隐藏状态的行为检测器，仅在检测到理解失败时触发外部翻译，该方法以极低的计算开销实现了接近全量翻译的准确率。这一发现将多语言推理优化从“全局对齐”转向“局部纠错”，但其检测器在极低资源语言上的泛化能力仍存疑。

】

---

【x1: Learning to Think Adaptively Across Languages and Cultures ｜自适应多语言推理

研究机构：哈尔滨工业大学、华为

作者：Yangfan Ye、Xiaocheng Feng、Xiachong Feng 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bc2799709cf4)

> 大语言模型在多语言任务中默认使用英语进行内部推理，导致低资源语言性能受损且文化语境丢失。现有方法或依赖外部翻译引入噪声，或通过强化学习优化全局奖励，但难以在单实例层面动态选择最优推理语言。本文提出x1模型，通过两阶段自监督训练使模型学会在特定实例上自适应切换至优势语言进行推理。该工作证明了语言选择是推理的功能性组件，但在高难度数学任务上的增益有限，且其效果高度依赖骨干模型原有的语言合规能力。

】
