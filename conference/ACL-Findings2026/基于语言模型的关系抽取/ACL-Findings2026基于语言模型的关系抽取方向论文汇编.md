# ACL-Findings2026 · 基于语言模型的关系抽取方向论文汇编

> 本方向共 8 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Multilingual Dataset and Empirical Validation for the Mutual Reinforcement Effect in Information Extraction ｜多语言互强效应数据集与实证验证

研究机构：深圳大学、浙江大学

作者：Chengguang Gan、Sunbowen Lee、Qingyu Yin 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2407.10953)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1f6382a3ec64)

> 信息抽取（IE）长期将词级任务（如命名实体识别）与文本级任务（如情感分类）视为独立目标，忽略了二者在同一输入中的双向语义依赖。现有互强效应（Mutual Reinforcement Effect, MRE）研究仅局限于日语，无法验证其跨语言普适性，且缺乏多语言混合数据集支撑系统性消融。本文通过LLM辅助翻译框架构建覆盖英、中、日三语的21个子数据集MMM，并训练统一生成模型OIELLM进行全参数微调，实证了76%的子集存在显著正向互强。该工作填补了MRE多语言验证的空白，但其对开放域任务性能衰减的解释仍显薄弱，且未探讨互强效应在低资源语言中的边界。

】

---

【Bayesian Active Learning with Gaussian Processes Guided by LLM Relevance Scoring for Dense Passage Retrieval ｜贝叶斯主动学习引导的LLM密集段落检索

研究机构：韩国成均馆大学、加拿大多伦多大学

作者：Junyoung Kim、Anton Korikov、Jiazhou Liang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17906)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17906)

> 密集段落检索（Dense Passage Retrieval, DPR）面临LLM重排成本高且无法覆盖语义分散簇的困境。现有LLM重排范式被动依赖第一阶段候选集，导致召回率受限且信号无法传播。本文提出BAGEL框架，利用高斯过程（Gaussian Process, GP）在嵌入空间中主动探索以平衡探索与利用。该方法在固定预算下显著提升了检索性能，但其对GP平滑性假设与LLM离散打分兼容性的验证尚显不足。

】

---

【DiffER: Diffusion Entity-Relation Modeling for Reversal Curse in Diffusion Large Language Models ｜扩散大语言模型中的反转诅咒与实体关系建模

研究机构：重庆大学、清华大学

作者：Shaokai He、Kaiwen Wei、Xinyi Zeng 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_61fecc743636)

> 扩散大语言模型（DLLM）虽具备双向注意力架构，理论上应能克服自回归模型的方向性偏差，但在处理逻辑双向关系时仍表现出严重的“反转诅咒”，即从 A→B 推理到 B→A 时性能骤降。现有研究多将此归因于自回归训练机制，忽视了扩散模型特有的去噪过程对实体完整性的破坏以及数据分布的固有偏斜。本文通过系统实验定位了实体碎片化、数据不对称与关系稀疏三大根因，并设计了全实体掩码、对称对齐与逆关系建模三位一体的后训练框架 DiffER。该框架在 PORE 基准上显著提升了双向推理准确率，但其有效性依赖于结构化三元组数据的可构造性，在大规模非结构化语料中的泛化能力尚存疑。

】

---

【From Local Perspective to Global Reasoning: A Neuro-Symbolic Framework for Zero-Shot Relation Extraction ｜全局神经符号推理框架

研究机构：美国东北大学

作者：Kailun Lyu、Fu Zhang、Zehan Li 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_93e3835b0357)

> 零样本关系抽取（ZSRE）的核心困境在于模型往往孤立地评估每个实体对，导致在语义相似但逻辑不同的关系间产生混淆。现有基于嵌入匹配或提示学习的方法均局限于局部视角，缺乏跨事实的逻辑一致性约束。G-NSR 通过构建双重类型约束命题集，利用神经符号推理器执行全局逻辑蕴含与证据聚合，将独立预测转化为相互印证的逻辑系统。该方法在 FewRel 上取得平均 +4.14 F1 的提升，但其依赖 BERT 编码器而非前沿大语言模型（LLM），且全局推理的计算复杂度随候选关系数增长，限制了其在大规模开放场景下的直接适用性。

】

---

【HCRE: LLM-based Hierarchical Classification for Cross-Document Relation Extraction with a Prediction-then-Verification Strategy ｜层级分类与预测验证策略

研究机构：厦门大学

作者：Guoqi Ma、Liang Zhang、Hongyao Tu 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5f000b33468d)

> 跨文档关系抽取（Cross-Document RE）旨在从分散在不同文档的实体间识别语义关联，但现有“小语言模型+分类器”范式受限于语义理解能力，难以处理大规模预定义关系集。直接引入大语言模型（LLM）虽具备更强推理能力，却因选项过多导致区分度下降与注意力分散，性能甚至低于强SLM。本文通过构建层级关系树将分类任务拆解为自顶向下的多步决策，并引入预测-验证策略抑制层级间错误传播，从而在CodRED基准上显著超越SLM基线。该方案验证了结构化选项缩减对LLM性能的关键作用，但其对树结构构建质量的依赖及推理延迟增加问题尚存疑。

】

---

【LoRE: Enhancing Search Relevance with Progressive Chain-of-Thought and Preference Alignment ｜电商搜索相关性评估：渐进式思维链合成与偏好对齐

作者：Chenji Lu、Zhuo Chen、Hui Zhao 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b9565e0cd407)

> 电商搜索相关性评估旨在判定查询与商品间的匹配程度，但通用大语言模型（LLM）缺乏垂直领域知识与刚性业务规则遵循能力，导致长尾查询与多模态商品匹配出现系统性偏差。现有基于直接分类或单模态思维链（CoT）的方法难以同时覆盖知识推理、视觉理解与规则约束，且监督微调（SFT）易陷入表面模式模仿。本文提出LoRE框架，通过渐进式多模态CoT合成注入综合能力，并引入基于课程学习的强化学习（RL）阶段修剪冗余逻辑。该框架在工业级部署中验证了显著增益，但其对教师模型依赖与奖励稀疏性缓解机制的普适性仍需审视。

】

---

【Prompt Optimization for Relation Extraction using Reinforcement Learning ｜基于深度强化学习的领域关系抽取提示优化

研究机构：美国东北大学

作者：Ying Liu、Dong Shuai、Cui Zibo 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f29d6466a30b)

> 导读 关系抽取（Relation Extraction, RE）在低资源领域场景中面临标注数据稀缺与提示工程依赖人工的双重瓶颈。现有自动提示优化方法多采用无结构搜索或启发式重写，难以高效探索组合式的提示空间且易产生语义漂移。本文提出REPO框架，将提示优化建模为马尔可夫决策过程，利用深度强化学习在受限动作空间内迭代精炼提示。该框架在医疗、金融等四个领域数据集上验证了跨域泛化能力，但其动作空间的离散性是否限制了提示结构的创造性探索，仍存疑。

】

---

【Tracing Relational Knowledge Recall in Large Language Models ｜追踪大语言模型中的关系知识回忆机制

作者：Nicholas Popovič、Michael Färber

论文原文见 [arXiv](https://arxiv.org/abs/2604.19934)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f57f2547d1eb)

> 大语言模型（LLMs）在生成文本时如何内部存储并检索关系知识，是解释性研究的核心难题。现有机制分析多聚焦于实体表征或全层状态，缺乏对关系类型特征在注意力头与源词元层面可归因性的系统验证，导致无法解释为何某些关系类型易于线性解码而另一些则失败。本文通过构建基于单头注意力贡献的线性探针，并引入HeadScore与TokenScore归因方法，系统评估了不同内部表征在少样本关系分类中的有效性及其预测因子。该工作揭示了注意力头贡献是关系分类的强特征，且探针性能受谓词输出范围与信号集中度影响，为理解LLM关系绑定机制提供了可操作的诊断工具，但其线性假设在复杂关系场景下的泛化能力仍存疑。

】
