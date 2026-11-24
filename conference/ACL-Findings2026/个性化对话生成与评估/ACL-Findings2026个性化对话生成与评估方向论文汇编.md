# ACL-Findings2026 · 个性化对话生成与评估方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【D2PCM:A Multi-Turn Dialogue Dataset with Personalized Contextual Memory ｜基于自我参照效应的个性化上下文记忆对话数据集

研究机构：清华大学

作者：Zhe Yang、Yi Huang、Yaqin Chen 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_193c677ba567)

> 个性化对话生成旨在让机器在交互中展现特定的人格特征与用户偏好，其核心价值在于弥合通用语言模型的同质化输出与人类交流中高度情境化、个体化需求之间的鸿沟。现有检索增强生成（RAG）方法将记忆视为静态上下文，通过全局相似度搜索选取内容，忽视了个体认知机制对记忆激活的差异化影响，导致长程对话中画像漂移与语境脱节。本文基于认知心理学中的自我参照效应，构建了多轮对话数据集 D2PCM，通过模拟人格匹配的记忆检索偏好，为个性化记忆处理算法提供基准。该工作验证了显式人格对齐在记忆选择中的必要性，但评估依赖 LLM 裁判且缺乏跨数据集泛化证据，其结论的普适性仍存疑。

】

---

【LongMP-Bench: A Benchmark for Multimodal Persona Understanding in Long-Term Dialogues ｜长程多模态画像理解基准

研究机构：中国人民大学

作者：Zhuoqun Li、Zhaopei Huang、Wenxuan Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_568b6e919647)

> 个性化对话系统需追踪用户随时间演变的偏好与身份，但现有基准多局限于静态文本画像或视觉身份不一致的碎片化图像，无法评估模型在长程交互中融合图文线索并捕捉状态终止的能力。本文切入点在于构建首个兼具视觉一致性与动态演变属性的多模态长程对话基准。通过多阶段合成管线生成150个用户的演化画像，并定义问答与生成双任务，实证揭示了当前多模态大模型在跨会话状态追踪上的显著短板。该基准填补了动态多模态评估空白，但其合成数据分布偏差与单参考评估局限仍制约结论的泛化性。

】

---

【SEAD: Self-Evolving Agent for Multi-Turn Service Dialogue ｜自进化服务对话智能体

研究机构：美团

作者：Yuqin Dai、Ning Gao、Wei Zhang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4575a12bfca5)

> 目标导向服务对话面临数据稀缺与用户行为主观性双重瓶颈，传统静态微调受限于标注成本，而通用自博弈框架因用户模拟器可任意控制结果导致训练失效。SEAD 通过解耦用户建模，将难度调节权赋予独立的画像控制器，构建公平对抗环境。该框架无需大规模标注数据，仅凭标准作业程序与用户画像即可训练出超越商用大模型 API 的轻量级智能体。其核心价值在于验证了“难度自适应”在主观任务中的可行性，但模拟器公平性的量化评估仍存疑。

】
