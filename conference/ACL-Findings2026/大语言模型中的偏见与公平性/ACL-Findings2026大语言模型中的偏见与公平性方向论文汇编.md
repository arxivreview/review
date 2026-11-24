# ACL-Findings2026 · 大语言模型中的偏见与公平性方向论文汇编

> 本方向共 13 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Adaptive Data Collection for Latin-American Community-sourced Evaluation of Stereotypes (LACES) ｜自适应社区源刻板印象数据集构建

作者：Guido Ivetta、Pietro Palombini、Sofía Martinelli 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0ef6c7d1c837)

> 拉丁美洲地区缺乏本土化的刻板印象评估资源，导致现有模型偏见检测无法覆盖该区域的文化特异性。主流静态收集方法因缺乏动态覆盖评估机制，导致数据冗余且长尾知识缺失。本文提出一种将新条目生成与验证整合于同一工作流的自适应采样方法，通过加权概率算法平衡群体内代表性与验证覆盖。该方法构建了包含4,789条关联的LACES数据集，其独特概念率显著高于现有基准，但去偏实验显示现有缓解策略在该数据集上效果有限，且标注者群体内偏差可能影响数据客观性。

】

---

【Analysing Differences in Persuasive Language in LLM-Generated Text: Uncovering Stereotypical Gender Patterns ｜指令属性对LLM说服语言风格影响的成对评估框架

研究机构：丹麦奥胡斯大学、日本东京大学

作者：Amalie Brogaard Pauli、Maria Barrett、Max Müller-Eberstein 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.05751)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05751)

> 大语言模型在生成说服性文本时，是否会根据接收者性别等属性调整修辞策略，进而固化社会刻板印象？现有偏见评估多聚焦于事实性内容或单一维度的刻板印象，缺乏对“说服风格”这一动态生成过程的系统性量化。本文构建了一个基于成对提示与LLM裁判的评估框架，从19个社会心理学维度解析指令属性对语言风格的重塑。该框架揭示了所有测试模型均存在显著的性别修辞偏见，但仅停留在行为层观测，未触及内部表征的因果机制。

】

---

【BIASEDTALES-ML: A Multilingual Dataset for Analyzing Narrative Attribute Distributions in LLM-Generated Stories ｜多语言叙事属性分布分析

研究机构：美国东北大学

作者：Yuxuan Ouyang、Yingfeng Luo、JingBo Zhu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17008)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_340a1d437137)

> 现有社会偏见评估多依赖英文短文本基准，难以捕捉长叙事生成中隐含的社会属性分布及其跨语言变异。本文通过构建包含35万条平行儿童故事的八语言数据集，利用“生成-提取”管道量化叙事结构中的偏差。该方法揭示了语言类型学特征对偏见分布形态的调节作用，但受限于提取器精度与缺乏去偏基线，其结论的因果归因能力存疑。

】

---

【DeFrame: Debiasing Large Language Models Against Framing Effects ｜框架效应下的LLM公平性评估与去偏

研究机构：韩国科学技术院

作者：Kahee Lim、Soyeon Kim、Steven Euijong Whang

论文原文见 [arXiv](https://arxiv.org/abs/2602.04306)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.04306)

> 大语言模型在标准公平性基准上表现良好，但语义等价、极性相反的提示会导致偏见水平剧烈波动，这种“框架效应”构成了隐式偏见的重要来源。现有去偏方法仅降低平均偏见，无法消除框架间的方差，导致模型在真实部署中仍可能因措辞差异产生歧视性决策。本文提出“框架差异”指标量化该现象，并设计DeFrame框架，通过极性反转提示、公平指南生成与自我修正三阶段流程，强制模型在跨框架下保持一致性。该方法在BBQ基准上平均降低92%的框架差异，但在绝对偏见分数上未超越多角色思维等SOTA方法，其有效性依赖于推理时多次调用带来的计算开销。

】

---

【Fair RAG: End-to-End Fairness Across Retrieval and Generation ｜检索增强生成中的端到端公平性校准

作者：Farsheed Haque、Zhe Fu、Ramit Aditya 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f8a357928903)

> 检索增强生成（Retrieval-Augmented Generation, RAG）旨在通过外部知识检索缓解大语言模型（Large Language Models, LLMs）的幻觉问题，但这一机制同时引入了检索侧与生成侧的双重偏见来源，导致人口统计学偏差在“数据库→检索→上下文→生成”链路中级联放大。现有公平性研究通常孤立处理检索去偏或生成对齐，忽略了两者间的耦合效应，且缺乏无需重训练的联合干预手段。本文提出一个后处理三阶段流水线，通过公平贪心重排器（Fair Greedy Reranker, FGR）平衡检索列表，利用残差列表偏见估计器（Residual Slate Bias Estimator, RSBE）量化剩余偏差，并以此信号驱动置信门控对数校准（Confidence-Gated Logit Calibration, CGLC）修正生成器输出。该框架在职业分类任务上实现了检索与生成双侧偏差的同步降低，但仅验证了单一分类场景，其向开放式生成任务的泛化能力存疑。

】

---

【Justice in Judgment: Unveiling (Hidden) Bias in LLM-assisted Peer Reviews ｜同行评审中的隐性偏见：硬评分与软评分的背离

研究机构：德国萨尔大学

作者：Sai Suresh Macharla Vasu、Ivaxi Sheth、Hui-Po Wang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.13400)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.13400)

> 学术同行评审正引入大语言模型（LLMs）以提升效率，但模型训练数据中的社会偏见可能扭曲评审公正性。现有评估多依赖最终整数评分，忽略了模型内部概率分布中潜藏的偏好，导致“表面中立”掩盖了“内部偏袒”。本文通过反事实干预作者元数据，并引入基于Token概率的软评分机制，揭示了硬评分与软评分间的巨大偏差。该研究证实了机构声望偏见在LLM评审中的系统性存在，但其合成数据设定限制了向真实盲审场景的泛化能力。

】

---

【Multi-Persona Thinking for Bias Mitigation in Large Language Models ｜多视角辩证推理去偏

研究机构：加拿大阿尔伯塔大学

作者：Yuxing Chen、Guoqing Luo、Zijun Wu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.15488)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.15488)

> 大语言模型在歧义语境下易依赖刻板印象进行推断，现有单一人格提示法虽能介入推理过程，却因视角单一而可能强化特定偏见。本文提出多视角辩证推理框架，通过模拟对立社会身份与中立视角的迭代交互，将人格分配从偏见来源转化为去偏机制。该方法在推理阶段实现偏见抑制与准确率保持的平衡，但其效果是否完全独立于骨干模型的对齐质量，仍需更严格的控制实验验证。

】

---

【Probing Social Identity Bias in Chinese LLMs with Gendered Pronouns and Social Groups ｜中文大语言模型社会身份偏见探测

研究机构：意大利米兰理工大学、中国科学技术大学

作者：Geng Liu、Li Feng、Junjie Mu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e196a7e12061)

> 现有偏见评估多依赖英语语境下的刻板印象基准，难以捕捉中文特有的形态性别标记对模型输出的影响。本文利用中文默认复数“他们”与女性复数“她们”的形态差异，构建内群体与外群体提示框架，量化十款中文大语言模型的情感与毒性不对称。通过控制变量提示设计与双层测量框架，揭示了指令微调对情感偏见的缓解作用有限，且毒性差距在微调后依然显著。该研究提供了语言感知的评估视角，但缺乏跨语言可比性基准，且未深入解析形态标记与内部表征的因果机制。

】

---

【Ready to Translate, Not to Represent? Bias and Performance Gaps in Multilingual LLMs Across Language Families and Domains ｜翻译纠缠：多语言大模型翻译质量与偏见评估框架

研究机构：美国弗吉尼亚大学

作者：Md. Faiyaz Abdullah Sayeedi、Subhey Sadi Rahman、Md. Mahbub Alam 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a4c8274bde9e)

> 多语言大语言模型在翻译任务中普遍存在质量与公平性解耦现象，传统自动指标无法捕捉文化语境偏移。现有评估基准多聚焦高资源语言，缺乏针对低资源语言及垂直领域的偏见量化标准。本文提出混合检测管道，结合规则启发式、语义相似度过滤与大模型验证，并构建人工标注数据集以校准自动系统。该框架填补了翻译领域偏见评估空白，但自动检测器与大模型判断的一致率偏低，限制了其作为独立筛选工具的可靠性。

】

---

【Rethinking Research on Stereotypes: An Analysis through Social Psychological and Computational Perspectives ｜社会心理学视角下的刻板印象计算化重构

研究机构：印度理工学院孟买分校

作者：Kaustubh Shivshankar Shejole、Pushpak Bhattacharyya

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3351a29507f4)

> 大语言模型（LLMs）在继承训练数据中的社会偏见时，往往将“偏见”与“刻板印象”混为一谈，导致现有评估基准存在概念混淆与资源浪费。本文指出，刻板印象作为群体间关系的主要基础，需独立于偏见进行系统性研究，并主张通过整合社会心理学理论（如Stereotype Content Model, SCM）来指导计算化建模。文章系统梳理了SCM、ABC模型等理论框架的计算化现状，分析了其在叙事、媒体及多模态场景下的应用缺口。该工作为刻板印象研究提供了理论坐标系，但缺乏具体的算法实现与量化验证，其理论指导价值需后续实证工作检验。

】

---

【Talent or Luck? Evaluating Attribution Bias in Large Language Models ｜归因理论视角下的大语言模型偏见评估

研究机构：美国乔治梅森大学、美国华盛顿大学

作者：Chahat Raj、Mahika Banerjee、Jinhao Pan 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_58e36c6a5474)

> 大语言模型（Large Language Models, LLMs）在解释社会事件成败时，往往将成功归因于主导群体的能力，而将失败归咎于边缘群体的努力不足，这种认知层面的归因不对称性比表层刻板印象更具隐蔽性。现有基准如 BBQ 和 StereoSet 仅测量模型对特定词汇或句式的偏好概率，无法捕捉模型在解释“原因”时的逻辑偏差。本文引入心理学归因理论，构建包含 14 万条提示的评估框架，通过单主体、双主体及观察者三种情境量化模型对内部与外部原因的分配差异。该框架揭示了模型在比较情境下对少数群体成功的系统性低估，但缺乏与主流去偏见方法的直接性能对比，其评估结论的泛化性仍存疑。

】

---

【Who Gets Which Message? Auditing Demographic Bias in LLM-Generated Targeted Text ｜人口统计学条件化生成中的说服性偏见审计

研究机构：美国普渡大学

作者：Tunazzina Islam

论文原文见 [arXiv](https://arxiv.org/abs/2601.17172)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.17172)

> 大语言模型在定向传播场景中，若将性别或年龄作为条件信号，会系统性地调整语言的说服力强度，而非仅改变内容。现有偏见评估多依赖情感或毒性指标，无法捕捉“如何说服”这一维度，导致对微观定向（Microtargeting）中隐性刻板印象放大的盲区。本文通过独立生成与语境丰富生成双范式解耦内在偏见与语境放大效应，并引入说服偏见指数（Persuasion Bias Index, PBI）量化代理框架、模态确定性与指令性差异。该框架揭示了个性化生成可能放大人口统计学刻板印象，但缺乏去偏见基线对照，其诊断效力尚待缓解策略验证。

】

---

【Whose Voice, Whose Avatar? Gender Matching Bias in Multimodal AI Teammates ｜多模态大语言模型中的语音-视觉身份冲突偏见审计

作者：Kyusik Kim、Jaehoon Choi、Hyunwoo Yoo 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_472d7c561c80)

> 多模态大语言模型（MLLMs）在协作场景中需整合语音与视觉身份线索，但现有评估多聚焦单模态刻板印象，忽视了跨模态冲突下的决策机制。本文通过反事实配对设计，将语音性别与化身外观独立操纵，以隔离“语音匹配”与“语境刻板印象”两种独立偏见模式。实验揭示闭源模型存在近确定性的二元对齐偏好，而开源模型则表现出与语音无关的语境性别刻板印象。该工作填补了跨模态社会身份冲突评估的空白，但其二元性别操作化与合成刺激限制了结论向真实复杂社交场景的泛化。

】
