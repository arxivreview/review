# ACL-Findings2026 · 大语言模型个性化方向论文汇编

> 本方向共 9 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Attention to Non-Adopters ｜关注非采用者：LLM 开发中的群体盲区与需求重构

研究机构：美国斯坦福大学、美国约翰斯·霍普金斯大学

作者：Kaitlyn Zhou、Kristina Gligorić、Myra Cheng 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.15951)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.15951)

> 大语言模型（LLM）的个性化研究长期聚焦于如何适配现有用户的风格与偏好，却系统性忽视了占美国人口 66% 的“非采用者”群体。现有基于交互日志和偏好数据的开发范式，将技术能力锁定在数字素养较高的采用者需求上，导致基础数字服务导航、护理协调等高频痛点被边缘化。本文通过定性访谈与定量调查，论证了将非采用者需求纳入设计、评估与部署闭环的必要性，并提出了“能力增强”评估范式。该立场论文揭示了 LLM 普及中的结构性不平等，但其定性结论向量化训练目标的转化路径尚不明确。

】

---

【Beyond Static Profiles: Capturing the Fluidity of User Preferences in Diverse Scenarios ｜情境依赖性偏好评估基准

作者：Chunyang Gao、Yi Huang、Jingyu Yao 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_00b094756eb0)

> 大语言模型个性化长期受困于“千人一面”的静态画像假设，无法捕捉用户偏好随语境动态切换甚至冲突的特性。现有基准多将偏好视为固定属性，导致模型在复杂社交场景中产生意图幻觉或给出通用化建议。本文切入点在于构建一个区分“稳定偏好”与“情境偏好”的细粒度分类体系，并设计配套的多轮对话数据集与评估任务。通过量化模型在动态语境下的对齐能力、歧义消解效率及样本识别效率，S2Pref 为动态个性化提供了新的测试床，但其评估协议中信息不对称的设置可能高估通用推理能力对个性化效果的贡献。

】

---

【ChildEval:WHEN LARGE LANGUAGE MODELS MEET CHILDREN’S PERSONALITIES ｜儿童偏好个性化评估基准

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a241f802c54e)

> 通用大语言模型（LLM）的个性化研究长期聚焦于成人场景，缺乏针对3-6岁儿童特定发展需求与语言特征的评估体系。现有基准如LaMP和PersonaMem虽提供了多轮对话与画像框架，但无法捕捉儿童互动中情感适应、发展适宜性等细粒度维度，导致模型在儿童陪伴场景下的表现无法被系统量化。本文构建ChildEval基准，通过合成29K儿童画像与隐式偏好对话，并提出儿童导向评估协议（COE），以验证不同适配策略在长上下文下的偏好一致性。该工作填补了儿童个性化评估的空白，但其依赖全合成数据且未建模动态安全约束，评估结果向真实儿童场景的迁移性存疑。

】

---

【From Personal to Collective: On the Role of Local and Global Knowledge in LLM Personalization ｜局部-全局知识协同框架

研究机构：美国圣母大学、南开大学

作者：Zehong Wang、Junlin Wu、Zhaoxuan Tan 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_339cb5de52ad)

> 大语言模型个性化长期受困于“孤立用户建模”的结构性缺陷：数据稀疏的新用户无法获得有效适配，而历史丰富的老用户则易陷入行为偏斜的过拟合。现有参数高效微调（PEFT）与检索增强生成（RAG）路线均将用户视为独立实体，忽略了跨用户共享的集体行为模式。LoGo 通过构建时间演化且社区感知的全局知识模块，并将其作为局部适配器的初始化先验，在层级化参数空间中平衡群体规律与个体偏好。该框架在 LaMP 基准上显著提升了冷启动用户的泛化能力并降低了高活跃用户的预测偏差，但其离线聚类假设与动态偏好演化之间存在潜在张力。

】

---

【Learning to Retrieve User History and Generate User Profiles for Personalized Persuasiveness Prediction ｜面向个性化说服预测的上下文感知用户画像构建

研究机构：韩国首尔大学

作者：Sejun Park、Yoonah Park、Jongwon Lim 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.05654)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05654)

> 个性化说服预测旨在判断特定消息能否改变目标用户的既有观点，其核心难点在于同一论证对不同用户的有效性差异巨大，而现有方法依赖静态人口统计属性或语义相似度检索，无法捕捉说服语境下的动态用户特征。本文切入点在于将用户画像构建视为一个可学习的、任务导向的过程，通过联合优化查询生成器与画像生成器，使检索与摘要环节直接服务于观点改变预测这一下游目标。该方法在ChangeMyView数据集上将Llama-3.3-70B-Instruct的F1分数从0.3284提升至0.4661，证明了上下文依赖画像的必要性，但其效用评分机制对预测器性能的强依赖性及跨域泛化的有限验证，仍构成应用边界。

】

---

【PerDucer: Keyphrase-Driven Personalization Inducer for Summarization from User Histories ｜基于关键短语诱导的冻结模型个性化摘要

作者：Parthiv Chatterjee、Asish Joel Batha、Sourish Dasgupta 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e20fcf3d4091)

> 个性化摘要旨在使生成内容同时满足文档重要性与用户动态兴趣，但直接将长交互历史注入大语言模型（LLM）提示词会导致性能不稳定甚至下降。现有方法多依赖静态画像或粗粒度主题，无法捕捉细粒度的时序偏好演化。PerDucer 将历史注入重构为关键短语引导，通过编码器预测潜在偏好信号并解码为紧凑的关键短语集，作为控制线索引导冻结的摘要模型。该方法在保持模型参数不变的前提下实现了显著的个性化增益，但其对稀疏历史信号的鲁棒性边界及跨域迁移的泛化能力仍需进一步审视。

】

---

【Personalized Benchmarking: Evaluating LLMs by Individual Preferences ｜个性化基准测试：基于个体偏好的大语言模型评估

研究机构：美国芝加哥大学

作者：Cristina Garbacea、Heran Wang、Chenhao Tan

论文原文见 [arXiv](https://arxiv.org/abs/2604.18943)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18943)

> 大语言模型（LLM）评估长期依赖聚合指标，掩盖了用户偏好的个体异质性。现有基准如 Chatbot Arena 通过平均所有用户投票计算全局排名，导致多数用户的实际偏好与推荐结果严重偏离。本文切入点在于量化这种偏离，并探索预测个体排名的特征空间。通过计算 115 名活跃用户的 ELO 与 Bradley-Terry (BT) 个体排名，结合主题与风格分析，证明了聚合排名的失效。其价值在于提供了个性化评估的量化证据，但样本量有限且未涉及动态偏好演化，结论的普适性存疑。

】

---

【Towards Proactive Personalization through Profile Customization for Individual Users in Dialogues ｜基于多轮马尔可夫决策过程的主动个性化智能体

研究机构：浙江大学

作者：Xiaotian Zhang、Yuan Wang、Ruizhe Chen 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8908109bd2be)

> 大语言模型在长程对话中难以捕捉用户隐式偏好的动态演化，且面临冷启动时无历史数据可用的困境。现有方法多依赖静态画像或一次性检索，缺乏跨轮次、跨会话的持续对齐机制。本文提出 PersonalAgent，将多轮对话分解为逐轮偏好推理任务，构建为多轮马尔可夫决策过程（Multi-turn Markov Decision Process, MDP），通过强化学习优化策略以动态维护用户画像。该方法在冷启动场景下显著优于记忆基线，但其长程一致性未经验证，且主动查询机制对用户打扰度的影响尚不明确。

】

---

【When Personalization Misleads: Understanding and Mitigating Hallucinations in Personalized LLMs ｜个性化诱导幻觉的推理时缓解

研究机构：中国人民大学

作者：Zhongxiang Sun、Yi Zhan、Chenglei Shen 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.11000)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.11000)

> 大语言模型（LLM）个性化旨在适配用户偏好，但现有提示增强与检索方法在提升主观满意度的同时，往往导致事实推理被用户历史干扰，产生“个性化诱导幻觉”。本文指出该现象源于隐层表示空间中个性化方向与事实方向的非正交纠缠，并提出事实保持个性化转向（Factuality-Preserving Personalized Steering, FPPS）框架，通过推理时探测纠缠程度并自适应调整隐层激活来恢复事实性。FPPS在自建基准上显著提升了事实准确率，但其评估依赖LLM-as-a-Judge且未覆盖参数化基线，跨基准泛化性存疑。

】
