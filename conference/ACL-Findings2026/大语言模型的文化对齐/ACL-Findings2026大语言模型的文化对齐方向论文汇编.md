# ACL-Findings2026 · 大语言模型的文化对齐方向论文汇编

> 本方向共 7 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Carefully Considering Culture: Analyzing LLM Alignment in Single- and Multi-Cultural Settings using Cultural Consensus Theory ｜文化共识理论下的LLM对齐诊断

研究机构：美国圣母大学

作者：Krishna Pothugunta、John P. Lalor

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1ab8719cb8a0)

> 大语言模型（LLMs）在跨文化部署中常出现“均值坍缩”，即模型输出趋向于稀释的中间态，无法反映特定文化群体的真实多样性。现有评估多依赖分布匹配或单一准确率指标，忽略了群体内部共识的结构差异，导致无法区分模型是真正理解文化还是仅仅制造了虚假的一致性。本文引入文化人类学中的文化共识理论（Cultural Consensus Theory, CCT），通过量化模型与人类群体在共识强度上的方差差异，揭示了模型在匹配共识方向时人为膨胀共识强度的现象。该研究提供了从“分布匹配”到“结构诊断”的新视角，但其诊断结果如何转化为具体的对齐干预策略仍待探索。

】

---

【CORAL: Adaptive Retrieval Loop for Culturally-Aligned Multilingual RAG ｜检索条件适配的多语言文化对齐框架

研究机构：三星研究院

作者：Nayeon Lee、Jiwoo Song、Byeongcheol Kang

论文原文见 [arXiv](https://arxiv.org/abs/2604.25676)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.25676)

> 多语言检索增强生成（mRAG）在处理文化特定查询时，常因固定检索空间导致语义相关但文化错位的证据被召回，进而生成形式正确但实质错误的回答。现有迭代检索方法仅优化查询本身，未触及语料库选择这一根本变量，使得低资源文化场景下的检索噪声无法消除。CORAL 通过 Planner-Critic 反馈循环，在测试时动态调整检索语料库范围并重写查询，将检索条件本身作为可修正的决策变量。该框架在低资源语言文化问答中实现了最高 3.58% 的准确率提升，但其效果高度依赖规划器模型的能力，且未验证在开放域生成场景中的泛化性。

】

---

【Deciphering Cultural Representations in Large Language Models via Sparse Autoencoders ｜稀疏自编码器解耦文化表征

研究机构：阿联酋扎耶德大学、加拿大多伦多大学

作者：Chenye Zou、Difan Jiao、Lijie Hu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2c0b13653ffe)

> 大语言模型内部的文化知识长期被多义神经元纠缠，导致无法区分深层价值观与表面词汇线索。现有神经元定位方法受限于叠加效应，难以实现精准干预。本文利用稀疏自编码器将激活分解为单义特征，通过因果消融验证其必要性，并证明定向引导可无重训练地调制文化行为。该工作提供了从机制解释到可控干预的闭环，但受限于特定模型架构与静态数据集，其结论在动态文化语境下的泛化性存疑。

】

---

【Exploring the Capability Boundaries of LLMs in Mastering of Chinese Chouxiang Language ｜中文抽象语言（Chouxiang Language）的大语言模型能力边界评估

作者：Dianqing Lin、Tian Lan、Jiali Zhu 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.15841)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4ab68bc9799a)

> 导读 现有大语言模型（LLMs）在处理非西方、非主流的网络亚文化语言时，往往因训练数据分布不均而陷入“表面正确、深层错位”的困境，导致对特定社群语义的解码失效。传统评估基准多聚焦于通用文化价值观或显性毒性检测，缺乏对动态演变的、非标准语义空间（如谐音替换、视觉隐喻）的细粒度量化手段。本文构建了Mouse基准，通过六个NLP任务系统评估LLM对中文抽象语言的掌握程度。该工作填补了亚文化语言评估的空白，但受限于静态数据集与单一语言模态，其结论在动态语境下的泛化能力存疑。

】

---

【FrameNet-Cultures: A Benchmark for Evaluating LLMs via Cross-Cultural Frame Semantics ｜基于框架语义的LLM文化结构评估基准

研究机构：丹麦哥本哈根大学

作者：Neda Jamshidi、Anders Søgaard、Monica Bianchini

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fd041deb5679)

> 该方向旨在解决大语言模型（LLMs）在生成文化描述时存在的系统性欧洲中心主义偏差，以及现有选择题基准无法区分“捷径学习”与“深层文化理解”的困境。现有方法多依赖封闭问答或预定义维度，难以量化模型内部潜在的文化结构同质化现象。本文切入点在于引入框架语义（Frame Semantics），通过开放生成任务将模型输出映射为二元特征向量，并与民族志数据进行结构对齐。其价值在于首次实现了从“事实正确性”到“结构相似性”的评估范式转变，但二元编码对文化梯度信息的丢失及单一标注者的主观性仍是主要存疑点。

】

---

【Mitigating Cultural Bias in LLMs via Multi-Agent Cultural Debate ｜多智能体文化辩论

研究机构：中国科学技术大学

作者：Qian Tan、Lei Jiang、Yuting Zeng 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.12091)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.12091)

> 大语言模型在跨文化部署中默认输出西方价值观，而现有评估基准强制将模型输出归类至特定文化，无法识别真正中立响应。本文指出，切换至中文提示仅将偏差转移至东亚视角，而非消除偏差，且功能型智能体框架无法保证文化视角的显式代表。为此，作者构建了包含“无偏见”选项的双语基准CEBiasBench，并提出赋予智能体显式文化身份的多智能体文化辩论框架MACD。该方法通过结构化辩论实现推理时去偏，但其在自建基准上的高分是否源于评估者从众效应，以及文化人设是否引入新刻板印象，仍存疑。

】

---

【MonCulture-Eval: A Hierarchical Benchmark for Evaluating Mongolian Cultural Capabilities of Large Language Models across Scripts and Regions ｜蒙古语双文字文化对齐基准

作者：Quulgan Minggad、Xiao Zinan、Yuan Sun

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dcac3d550b82)

> 大语言模型在低资源非西方语言中常出现“语言流利但文化错位”的断层，现有通用基准多依赖网络爬取数据，难以区分模型是真正理解文化逻辑还是仅靠翻译捷径作答。本文针对蒙古语双文字系统（传统竖排与西里尔字母）及三个区域亚文化，构建了基于原生非数字化档案的层级化评估基准。通过引入脚本对齐一致性（SAC）指标与三层认知框架，量化了模型在事实、情境与价值观层面的本体论对齐程度。该基准揭示了前沿模型普遍存在的“脚本鸿沟”与“游客视角”偏差，但受限于单一语言场景，其结论向其他低资源双文字系统的推广性尚待验证。

】
