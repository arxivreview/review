# ACL-Findings2026 · 可信AI与安全隐私方向论文汇编

> 本方向共 26 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Counterfactual Explanation Framework for Retrieval Models ｜检索模型反事实解释框架

研究机构：英国利物浦大学

作者：Bhavik Chandna、Procheta Sen

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1f74cf54d14d)

> 信息检索（IR）系统的可解释性长期聚焦于“为何文档被检索”，却忽视了“为何相关文档未被检索”这一关键盲区。现有解释方法无法回答哪些缺失词汇导致文档排名跌出Top-K，阻碍了模型偏差的诊断与修正。本文提出CFIR框架，通过构建局部二分类器并优化词频向量，生成仅包含新增词汇的反事实解释。该框架在多种检索模型上验证了有效性，但其解释的语义连贯性与因果有效性仍存疑。

】

---

【Adaptive Data Collection for Latin-American Community-sourced Evaluation of Stereotypes (LACES) ｜自适应社区源刻板印象数据集构建

作者：Guido Ivetta、Pietro Palombini、Sofía Martinelli 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0ef6c7d1c837)

> 拉丁美洲地区缺乏本土化的刻板印象评估资源，导致现有模型偏见检测无法覆盖该区域的文化特异性。主流静态收集方法因缺乏动态覆盖评估机制，导致数据冗余且长尾知识缺失。本文提出一种将新条目生成与验证整合于同一工作流的自适应采样方法，通过加权概率算法平衡群体内代表性与验证覆盖。该方法构建了包含4,789条关联的LACES数据集，其独特概念率显著高于现有基准，但去偏实验显示现有缓解策略在该数据集上效果有限，且标注者群体内偏差可能影响数据客观性。

】

---

【AdaptiveK Sparse Autoencoders: Dynamic Sparsity Allocation for Interpretable LLM Representations ｜自适应TopK稀疏自编码器

研究机构：浙江大学

论文原文见 [arXiv](https://arxiv.org/abs/2508.17320)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2508.17320)

> 导读 稀疏自编码器（Sparse Autoencoder, SAE）旨在将大语言模型（LLM）中叠加的密集激活分解为稀疏、单义的特征，但现有架构普遍采用固定稀疏度约束，导致简单输入过度激活而复杂输入特征不足。本文指出这种“一刀切”的稀疏策略忽视了文本语义复杂度的差异，提出基于线性探针预测复杂度并动态调整激活特征数量的AdaptiveK SAE。该方法通过复杂度驱动的动态稀疏分配，在多个模型规模上实现了优于固定基线的重构保真度与解释方差。尽管在Pareto前沿上表现优异，但缺乏与门控SAE等强基线的直接标量对比，其是否真正超越现有架构上限仍存疑。

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

【Do Generalisation Results Generalise? ｜分布外泛化结果的跨测试集相关性分析

研究机构：加拿大麦吉尔大学

作者：Matteo Boglioni、Andrea Sgobbi、Gabriel Tavernini 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.07832)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.07832)

> 大语言模型在单一分布外（Out-of-Distribution, OOD）测试集上的高分常被误读为模型已掌握任务本质，但不同分布偏移下的泛化能力未必同步。现有评估体系缺乏对“泛化结果本身是否具备泛化性”的量化手段，导致模型鲁棒性结论存在严重偏差。本文通过回归控制域内性能，计算多个OOD测试集间的偏相关系数，揭示了泛化表现的高度不稳定性。这一发现挑战了单一基准测试的有效性，但受限于自然语言推理（Natural Language Inference, NLI）任务及模型规模，其结论向其他任务迁移的边界尚不明确。

】

---

【Fair RAG: End-to-End Fairness Across Retrieval and Generation ｜检索增强生成中的端到端公平性校准

作者：Farsheed Haque、Zhe Fu、Ramit Aditya 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f8a357928903)

> 检索增强生成（Retrieval-Augmented Generation, RAG）旨在通过外部知识检索缓解大语言模型（Large Language Models, LLMs）的幻觉问题，但这一机制同时引入了检索侧与生成侧的双重偏见来源，导致人口统计学偏差在“数据库→检索→上下文→生成”链路中级联放大。现有公平性研究通常孤立处理检索去偏或生成对齐，忽略了两者间的耦合效应，且缺乏无需重训练的联合干预手段。本文提出一个后处理三阶段流水线，通过公平贪心重排器（Fair Greedy Reranker, FGR）平衡检索列表，利用残差列表偏见估计器（Residual Slate Bias Estimator, RSBE）量化剩余偏差，并以此信号驱动置信门控对数校准（Confidence-Gated Logit Calibration, CGLC）修正生成器输出。该框架在职业分类任务上实现了检索与生成双侧偏差的同步降低，但仅验证了单一分类场景，其向开放式生成任务的泛化能力存疑。

】

---

【From "Thinking" to "Justifying": Aligning High-Stakes Explainability with Professional Communication Standards ｜结构化可解释性框架

作者：Chen Qian、Yimeng Wang、Yu Chen 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.07233)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.07233)

> 高利害领域的大语言模型（LLM）解释常因推理与结论脱节而误导用户，现有事后归因方法无法捕捉论证结构。本文切入点在于将法律与军事沟通规范转化为输出约束，通过“结论先行”的结构化提示提升可验证性。SEF 框架定义了六项启发式指标，同时作为生成约束与评估标准。其价值在于证明了结构约束能同时提升准确性与可解释性，但指标仅衡量形式合规，未解决语义事实错误。

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

【LIBERTy: A Causal Framework for Benchmarking Concept-Based Explanations of LLMs with Structural Counterfactuals ｜基于结构因果模型的LLM概念解释基准

研究机构：以色列理工学院

作者：Gilat Toker、Nitay Calderon、Ohad Amosy 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.10700)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.10700)

> 概念解释的忠实度评估长期受困于缺乏真实因果机制作为参照，导致现有方法无法区分统计关联与因果效应。Abraham et al. (2022) 提出的 CEBaB 虽引入干预数据集，但受限于人工标注成本、短文本场景及简单因果图，无法适配 LLM 的复杂生成过程。LIBERTy 通过显式定义文本生成的结构因果模型（SCM），利用 LLM 作为 SCM 组件自动生成结构反事实，从而构建具有因果对齐的评估基准。该框架解决了评估参考值与数据生成过程（DGP）脱节的问题，但受限于合成数据的分布偏差，其结论在真实世界文本上的泛化性存疑。

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

【OSCR-Attack: One-Shot Character Level Attacks through Self-Optimizing Continuous Relaxation ｜字符级对抗攻击的连续松弛优化

研究机构：西北工业大学

作者：Lingyi Kong、Zhuo Liu、Zhanghao Hu 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e9fd3cecc8ee)

> 字符级文本对抗攻击旨在通过插入少量字符诱导大语言模型（LLM）产生错误预测，同时保持语义不变。传统方法依赖逐步贪心搜索，在离散空间中存在效率低下且易陷入局部最优的瓶颈。OSCR-Attack 提出将离散的插入位置与字符选择松弛为连续分布，通过端到端梯度优化实现一次性多位置扰动。该方法在攻击成功率与语义保持的平衡上优于现有基线，但其连续松弛到离散映射的冲突解决机制在复杂分词边界下的鲁棒性尚待检验。

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

【SEA-SafeguardBench: Culturally Grounded Safety Benchmark for Southeast Asian Languages ｜东南亚文化接地安全基准

作者：Panuthep Tasawong、Jian Gang Ngui、Alham Fikri Aji 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cd0b1cfc2597)

> 多语言大语言模型的安全评估长期受困于英语中心主义，导致低资源语言中的文化禁忌与隐性危害被系统性忽视。现有翻译基准无法捕捉本地特有的社会规范，而本文通过构建首个全人工验证的东南亚（SEA）原生安全基准，填补了这一区域空白。该基准涵盖7国8种语言，通过对比通用、野外及内容生成场景，揭示了当前SOTA模型在文化敏感内容上的显著性能退化。尽管基准有效暴露了现有护栏模型的盲区，但其依赖高昂的人工标注成本，且对模型内部机制的解释仍停留在行为层。

】

---

【Talent or Luck? Evaluating Attribution Bias in Large Language Models ｜归因理论视角下的大语言模型偏见评估

研究机构：美国乔治梅森大学、美国华盛顿大学

作者：Chahat Raj、Mahika Banerjee、Jinhao Pan 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_58e36c6a5474)

> 大语言模型（Large Language Models, LLMs）在解释社会事件成败时，往往将成功归因于主导群体的能力，而将失败归咎于边缘群体的努力不足，这种认知层面的归因不对称性比表层刻板印象更具隐蔽性。现有基准如 BBQ 和 StereoSet 仅测量模型对特定词汇或句式的偏好概率，无法捕捉模型在解释“原因”时的逻辑偏差。本文引入心理学归因理论，构建包含 14 万条提示的评估框架，通过单主体、双主体及观察者三种情境量化模型对内部与外部原因的分配差异。该框架揭示了模型在比较情境下对少数群体成功的系统性低估，但缺乏与主流去偏见方法的直接性能对比，其评估结论的泛化性仍存疑。

】

---

【TinyAttack: Exploring Stylistic Vulnerabilities in Large Language Models ｜基于Unicode样式变换的大语言模型对抗攻击

作者：Mamta Mamta、Bogdan Grecu、Oana Cocarascu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2eadcea15a32)

> 大语言模型（LLM）在自然语言处理任务中表现优异，但其对输入扰动的脆弱性在安全敏感场景（如仇恨言论检测、事实核查）中构成严重威胁。现有对抗攻击多聚焦于词级同义词替换或字符级增删，忽略了真实用户生成内容中日益普遍的Unicode样式变形（如上标、下标、特殊字体）这一隐蔽攻击向量。TinyAttack提出了一种利用五种Unicode样式变换的黑盒攻击框架，通过LLM自归因机制以极低查询成本定位关键词并实施扰动。该框架揭示了LLM分词器对非标准字符的处理缺陷，但其在不同模型间的鲁棒性差异及防御有效性仍存疑。

】

---

【Towards Provably Secure Generative AI: Reliable Consensus Sampling ｜可靠共识采样（RCS）：消除弃权的生成式AI形式化安全框架

研究机构：北京理工大学、清华大学

作者：Yu Cui、Hang Fu、Sicheng Pan 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0bdadeaf9ebc)

> 导读 生成式AI的安全防御长期依赖经验性过滤，但密码学证明表明高效提示过滤器不存在，且部分风险不可检测，导致模型推理风险无法根除。现有共识采样（Consensus Sampling, CS）虽提供理论风险上界，却依赖频繁弃权牺牲可用性，且在拜占庭模型恶意操纵下鲁棒性崩溃。本文提出可靠共识采样（Reliable Consensus Sampling, RCS），通过实时追踪接受概率并在采样失败后进入重加权追踪阶段，彻底消除弃权并保证最终交付。该工作将安全从经验性防护转向可证明的数学保证，但其有效性严格依赖于模型组中安全模型数量占优的假设，在极端对抗强度下安全率仍显著衰减。

】

---

【Towards Understanding the Robustness of Sparse Autoencoders ｜稀疏自编码器作为推理时对抗鲁棒性瓶颈

研究机构：美国弗吉尼亚大学

作者：Ahson Saiyed、Sabrina Sadiekh、Chirag Agarwal

论文原文见 [arXiv](https://arxiv.org/abs/2604.18756)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18756)

> 大语言模型（LLM）易受基于梯度优化的越狱攻击，现有防御多聚焦于输入扰动或解码约束，忽视了内部表示几何结构对攻击优化的影响。本文切入点在于将稀疏自编码器（Sparse Autoencoder, SAE）作为推理时插入的不可微分瓶颈，通过重构残差流改变对抗优化的景观。具体做法是在Transformer中间层插入预训练SAE，保持梯度穿透以隔离表示效应。该研究证实了SAE能显著降低攻击成功率，但其防御效果依赖于稀疏度与层深的精细权衡，且缺乏与随机投影基线的对比，其防御上限存疑。

】

---

【Trustworthy and Explainable Causal Representation Learning in Transformers ｜因果可识别解释模型

作者：Yang Liu、Yinghao Zhang、Lin Liu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2b3b97093598)

> 可解释人工智能（XAI）旨在通过量化输入特征重要性来揭示模型决策逻辑，但传统掩码方法缺乏理论保证，导致解释结果可能源于数据噪声而非真实因果机制。现有方法多聚焦于保真度（Faithfulness），即解释是否反映模型行为，却忽视了可识别性（Identifiability），即解释是否由真实数据分布唯一确定。CIEM 通过构建结构因果模型（SCM），将注意力机制分解为权重与值两个潜变量，利用可识别变分自编码器（iVAE）理论确保解释的唯一性。该方法在理论上填补了掩码解释的歧义性漏洞，但其依赖生成模型拟合而非因果干预，在机制可解释性（MI）坐标系中缺乏因果必要性的直接验证。

】

---

【UbuntuGuard: A Culturally-Grounded Policy Benchmark for Equitable AI Safety in African Languages. ｜动态策略下的非洲语言安全评估基准

研究机构：美国布朗大学、美国俄亥俄州立大学

作者：Tassallah Abdullahi、Macton Mgonzo、Mardiyyah Oduwole 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_95fd48235ab2)

> 现有守护者模型依赖静态、预定义的安全类别，无法适应不同文化语境下动态变化的安全规范，导致低资源语言中的安全评估失效。UbuntuGuard 通过引入推理时策略注入机制，构建了首个覆盖10种非洲语言的动态政策合规评估基准。该基准利用155名领域专家生成的对抗性查询，派生出多轮用户-代理对话及本地化行为规则，以量化模型在跨语言环境下的策略遵循能力。其核心贡献在于揭示了大规模模型安全对齐带来的“对齐税”现象，但依赖机器翻译的构建流程限制了文化语义的绝对保真度。

】

---

【Where meaning lives: Layer-wise accessibility of psycholinguistic features in encoder and decoder language models ｜心理语言学特征的层间可解码性：嵌入提取方法与架构约束的交互作用

研究机构：德国柏林工业大学、瑞士巴塞尔大学

作者：Taisiia Tikhomirova、Dirk U. Wulff

论文原文见 [arXiv](https://arxiv.org/abs/2601.03798)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03798)

> 本文旨在厘清Transformer内部各层对情感、具体性等心理语言学维度的编码分布，以解决现有探测研究中因固定单一嵌入提取策略导致的层间定位结论不稳定问题。既往工作多依赖最终层表征或孤立词嵌入，忽视了上下文提取方式对可解码性的系统性影响，本文通过交叉对比三种提取方法与十种架构模型，揭示了提取方法本身是层间定位的第一序变量。具体做法是构建统一线性探测框架，量化不同提取策略下58个人工验证特征在各层的Selectivity与中心质量（Center of Mass, COM）。该研究为表征几何分析提供了方法论修正，但其结论限于线性可解码性，未触及因果必要性，且未验证提取方法差异是否掩盖了架构本身的层间分布规律。

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
