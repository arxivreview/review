# ACL-Findings2026 · 音频-语言模型与推理方向论文汇编

> 本方向共 15 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Afrispeech Semantics: Evaluating Audio–Semantic Reasoning in Spoken Language Models Across Domains and Accents ｜音频语义推理的多任务评估框架

研究机构：美国佛罗里达大学

作者：Chibuzor Okocha、Christan Grant

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d5ebd8c4b1ae)

> 音频语言模型（ALM）在生成流畅文本的同时，常依赖语言先验而非声学证据进行推断，导致“过度蕴含”与口音敏感等系统性错误。现有基准如MMAU侧重表面正确性，无法区分合理幻觉与逻辑谬误，且缺乏对发音变体下语义稳定性的测试。本文构建了一个包含蕴含、一致性、可信度及口音漂移/克制五个子任务的统一评估框架，基于非洲口音语料库对13个ALM进行零样本审计。该工作揭示了当前模型在细粒度语义推理上的严重缺陷，但级联ASR+LLM系统优于端到端ALM的发现，挑战了“端到端架构必然更优”的领域共识。

】

---

【AHA: Aligning Large Audio-Language Models for Reasoning Hallucinations via Counterfactual Hard Negatives ｜基于反事实硬负样本的音频语言模型时序幻觉对齐

研究机构：美国亚利桑那州立大学、美国克莱姆森大学

作者：Yanxi Chen、Wenhui Zhu、Xiwen Chen 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.24052)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.24052)

> 导读 大型音频语言模型（LALM）在复杂声学场景中常因依赖语言先验而非声学证据，产生时序逻辑错误。现有监督微调（SFT）缺乏负约束，无法区分“语言流畅”与“声学真实”，导致模型编造细节以维持连贯性。本文提出 AHA 框架，通过挖掘反事实硬负样本构建偏好数据集，利用直接偏好优化（DPO）强制模型对齐声学事实。该策略在诊断基准上显著降低幻觉率，并在公开基准上实现零对齐税下的性能提升，但其对非时序类幻觉的泛化能力尚存疑。

】

---

【AUDITA: A New Dataset to Audit Humans vs. AI Skill at Audio QA ｜音频问答基准 AUDITA：基于 IRT 的人类-模型能力差距诊断

研究机构：美国哥伦比亚大学

作者：Tasnim Kabir、Dmytro Kurdydyk、Aadi Palnitkar 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_52412c480158)

> 音频问答（Audio QA）旨在评估模型从声学信号中提取语义与实体信息的能力，但现有基准多依赖封闭集分类或模板化问题，导致模型可通过文本先验或浅层声学线索“作弊”，无法真实反映听觉推理水平。本文切入点在于构建一个要求多线索整合与真实世界实体锚定的高难度基准，并引入人类基线作为参照系。具体做法是收集 9690 个人工撰写的音频问答对，利用项目反应理论（Item Response Theory, IRT）量化题目区分度与参与者能力，揭示人类与模型在听觉推理上的巨大鸿沟。该工作提供了诊断模型听觉盲区的有力工具，但其结论是否受限于特定文化实体类型，仍需进一步验证。

】

---

【Beyond Transcription: Unified Audio Schema for Perception-Aware AudioLLMs ｜统一音频模式（UAS）：重构音频大模型监督信号以弥合感知-推理鸿沟

研究机构：北京大学

作者：Linhao Zhang、Yuhan Song、Aiwei Liu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12506)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_334d18c689d9)

> 音频大语言模型（AudioLLM）在复杂推理任务上表现优异，却在基础声学感知上存在显著短板，这一矛盾源于以自动语音识别（ASR）为核心的训练范式系统性抑制了副语言与非语言信息的表达。现有方法通过扩大模型规模或引入对比学习未能解决该结构性偏差，本文切入点在于重构训练监督信号，将隐式感知需求转化为显式结构化目标。具体做法是提出统一音频模式（Unified Audio Schema, UAS），将音频分解为转录、副语言和非语言事件三个组件，并通过自动化管道生成大规模结构化标注数据。该方案在感知基准上取得显著提升，但其对推理能力的保留机制及跨域泛化边界仍需进一步验证。

】

---

【CliniCAST: Benchmarking Acoustic Grounding and Text Dominance in Medical Triage ｜临床声学接地基准

作者：Kyusik Kim、Hyunwoo Yoo、Jaehoon Choi 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2475ae91b56e)

> 大型音频语言模型（LALM）在医疗分诊中面临的核心矛盾是：模型能否在词汇内容固定时，仅凭副语言声学证据做出可靠的紧急度判断？现有通用基准无法隔离声学因果，导致模型对文本先验的依赖被掩盖。本文通过构建控制变量合成数据集，量化了LALM的“文本主导”偏差。该基准揭示了当前模型在高风险声学信号面前的脆弱性，但其合成语音的病理真实性仍存疑。

】

---

【CORD: Bridging the Audio-Text Reasoning Gap via Weighted On-policy Cross-modal Distillation ｜跨模态加权在线自蒸馏

研究机构：清华大学

作者：Jing Hu、Danxiang Zhu、Xianlong Luo 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.16547)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.16547)

> 大型音频语言模型（LALM）在音频条件任务上的表现持续落后于文本条件任务，这一“文本-音频理解差距”源于现有训练范式未能有效弥合声学特征与语义空间的对齐。传统监督微调依赖昂贵标注，外部教师蒸馏存在策略外分布不匹配，且均匀KL散度忽略了推理早期关键语义偏差的累积效应。CORD提出一种无需外部教师的在线跨模态自蒸馏框架，通过加权反向KL散度与基于奖励的组相对策略优化（GRPO）在token级和序列级同步对齐音频与文本推理轨迹。该方法以80k合成数据显著缩小模态差距，但绝对性能仍低于领域SOTA，且仅在数学域验证了泛化能力。

】

---

【DIFFA-2: A Practical Diffusion Large Language Model for General Audio Understanding ｜扩散大语言模型音频理解框架

作者：Jiaming Zhou、Xuxin Cheng、Shiwan Zhao 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4039d8fbe3e0)

> 音频语言模型（ALM）旨在通过自然语言接口统一音频理解、推理与生成任务，其核心价值在于突破单一模态音频处理的局限。现有主流自回归（AR）架构在数据效率与推理延迟上存在瓶颈，而早期扩散模型验证了非自回归范式的潜力但缺乏实用规模。本文提出 DIFFA-2，通过双适配器与四阶段训练将扩散骨干转化为实用音频模型。该工作证明了低参数更新下扩散架构的竞争力，但其对长序列时序依赖的建模能力仍存疑。

】

---

【Don’t Just Listen, Try Planning: Graph-based Retrieval-Generation Agent for Long-form Audio Meeting Understanding ｜长音频会议理解中的图检索生成代理

作者：Quanwei Tang、Dong Zhang、Shoushan Li 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d169fbf953db)

> 长音频会议理解（Long-form Audio Meeting Understanding, LAMU）面临的核心矛盾是：现有大型音频语言模型（Large Audio-Language Model, LALM）在处理超长会议时，因ASR转文本导致声学信息丢失（Acoustic Missing），且线性上下文窗口无法维持长程语义依赖（Context Fragmentation）。本文切入点在于将会议音频建模为多维异构图，并引入基于部分可观测马尔可夫决策过程（POMDP）的代理规划机制，替代传统的单次检索增强生成（RAG）。通过显式的查询分解、图遍历与自我反思，GRGA在长程多跳推理任务上显著优于端到端LALM与标准RAG基线。其价值在于证明了结构化图索引与代理规划对缓解长音频理解中“中间丢失”问题的有效性，但依赖外部LLM作为策略网络带来的推理延迟与评估者偏差仍是存疑点。

】

---

【Listen, Pause, and Reason: Toward Perception-Grounded Hybrid Reasoning for Audio Understanding ｜感知接地混合推理

研究机构：北京大学、香港中文大学

作者：Jieyi Wang、Yazhe Niu、Dexuan Xu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dc3d02b3b6a8)

> 大型音频语言模型（LALM）在复杂声学场景下常因感知错误导致推理失效，现有纯文本思维链（CoT）方法难以捕捉不可言说的声学线索。本文切入点在于将感知与推理解耦，通过显式声学分解与隐式潜空间计算建立可靠的推理基础。HyPeR 框架结合监督微调（SFT）与基于组相对策略优化（GRPO）的强化学习，引入 PAUSE 令牌处理声学模糊性。该方法在感知诊断任务上显著优于基线，但在通用推理基准上未超越现有 SOTA，其有效性局限于特定感知-推理解耦场景。

】

---

【MoE Adapter for Large Audio Language Models: Sparsity, Disentanglement, and Gradient-Conflict-Free ｜稀疏专家混合适配器

研究机构：清华大学

作者：Yishu Lei、Shuwei He、Jing Hu 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.02967)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.02967)

> 大型音频语言模型（LALM）在处理语音、音乐与环境音时，常因单一密集适配器导致参数更新方向相互抵消，引发梯度冲突。现有主流架构假设音频信号服从统一分布，无法解耦异构声学属性，致使模型在语义推理与副语言理解上受限。本文提出 MoE-Adapter，通过动态路由机制将音频特征分配至专门化专家，以稀疏激活实现特征解耦。该方法在固定参数预算下优于密集基线，但其绝对性能仍显著低于领域最先进模型，且未验证其在长音频或复杂推理链中的有效性。

】

---

【Pardon? Evaluating Conversational Repair in Large Audio-Language Models ｜可评估性感知与对话修复评估

作者：Shuanghong Huang、Jinlei Xu、Youchao Zhou 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_10cbb66276bd)

> 大型音频语言模型（Large Audio-Language Model, LALM）在语音问答中常因输入语义缺失而幻觉作答，现有评估仅测准确率或声学鲁棒性，隐含“输入始终可答”的假设。本文提出可评估性感知（Evaluability Awareness）概念，通过语义-声学掩码协议构造配对的可答/不可答输入，并定义非补偿性指标 EAR 分数，联合评估任务能力与修复行为。实验揭示主流 LALM 在不可答场景下系统性失效，EAR 分数显著低于其准确率，但掩码比例极小（2.5-6.7%）是否代表真实信息丢失程度存疑。

】

---

【PlanRAG-Audio: Planning and Retrieval Augmented Generation for Long-form Audio Understanding ｜规划式检索增强生成用于长音频理解

研究机构：美国卡内基梅隆大学

作者：Masao Someki、Chien-yu Huang、Siddhant Arora 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.20414)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.20414)

> 长音频理解面临的核心矛盾是输入序列长度与模型上下文窗口的指数级冲突，导致现有大型音频语言模型在处理小时级录音时性能急剧衰减。传统端到端生成范式无法在有限算力下保留跨模态的时序依赖，而纯文本转录又丢失了副语言信息。本文提出 PlanRAG-Audio，通过“规划-检索-生成”三阶段框架，将长音频理解转化为结构化数据库查询问题，从而解耦推理成本与音频时长。该方法在零样本条件下实现了跨模态组合推理，但在语义泛化能力与标准短音频基准上的表现尚未验证。

】

---

【PolyAudio: Advancing Multi-Audio Reasoning in Large Audio Language Models with Interleaved Multi-Audio Contexts ｜多音频交错推理

研究机构：美国马里兰大学帕克分校、美国杜克大学

作者：Sonal Kumar、Sreyan Ghosh、Yueqian Lin 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e7f378a730c0)

> 大型音频语言模型（LALM）在处理单片段音频时表现优异，但面对需要跨多个离散音频片段整合证据、解决指代冲突的复杂场景时，现有模型往往因缺乏原生多片段输入支持而失效。本文切入点在于证明无需大规模多音频预训练，仅通过显式交错格式与高质量指令微调即可解锁多音频组合式推理能力。具体做法是基于 Audio Flamingo 3 构建 PolyAudio，利用 1.3M 多音频指令数据训练模型识别片段边界与跨片段逻辑。该工作验证了后训练在多模态扩展中的高效性，但其依赖合成数据且仅支持至多 5 个片段，真实场景泛化能力存疑。

】

---

【RSA-Bench: Benchmarking Audio Large Models in Real-World Acoustic Scenarios ｜真实声学场景下的音频大模型鲁棒性基准

作者：Yibo Zhang、Kaiwen Luo、Liang Lin 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0feee803cac6)

> 音频大模型（Audio Large Model, ALLM）在干净音频上表现优异，但真实物理环境中的多源噪声导致其性能急剧下降，现有评估多依赖合成高斯噪声，无法反映真实声学生态的复杂性。本文提出 RSA-Bench，通过叠加 1-4 个真实环境噪声源构建压力测试集，量化模型在感知与认知任务上的鲁棒性边界。实验揭示“感知-认知差距”与“去噪悖论”，即高层推理任务对噪声更敏感，且标准去噪算法反而加剧性能退化。该基准填补了真实场景鲁棒性评估的空白，但固定信噪比设置可能掩盖不同噪声强度下的真实分布差异。

】

---

【Temporal Contrastive Decoding: A Training-Free Method for Large Audio-Language Models ｜时间对比解码

研究机构：阿联酋扎耶德大学、北京交通大学

作者：Yanda Li、Yuhan Liu、Zirui Song 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.15383)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.15383)

> 统一架构大型音频语言模型（LALM）在自回归解码时，常因语言先验压制瞬态声学线索，导致对短暂事件（如铃声次数）的感知失效。现有解码干预方法多采用全局模态消融，无法区分时间尺度差异，且易干扰语言主导步骤。本文提出时间对比解码（Temporal Contrastive Decoding, TCD），通过构建时间模糊的“慢路径”视图，在解码时对比原始与模糊音频的Logit差异，并引入门控机制仅在不确定且依赖音频时进行稀疏修正。该方法无需训练即可提升强基座模型性能，但其有效性严格依赖于解码器能否访问时序对齐的音频表示，对语义瓶颈架构无效。

】
