# ACL-Findings2026 · 基于大语言模型的角色模拟方向论文汇编

> 本方向共 6 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Distribution Shift Alignment Helps LLMs Simulate Survey Response Distributions ｜分布偏移对齐

研究机构：中国科学技术大学、复旦大学

作者：Ji Huang、Mengfei Li、Shuai Shao

论文原文见 [arXiv](https://arxiv.org/abs/2510.21977)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.21977)

> 大规模社会调查面临高昂成本与隐私瓶颈，利用大语言模型（LLM）模拟人类响应成为替代方案，但现有方法受限于训练数据分布，无法超越数据本身的上限。本文指出LLM虽无法精准预测绝对分布，但能有效捕捉不同背景间的相对偏好差异。通过两阶段微调对齐分布偏移，DSA实现了比训练集更准确的分布估计。该方法在数据效率上表现突出，但其对背景独立性的强假设限制了在复杂交互场景下的适用性。

】

---

【ExpertIVS: Sociological Expert Driven Individual Value Simulation in Large Language Models ｜社会学专家驱动的个体价值观模拟

研究机构：天津大学

作者：Zhen Wang、Yuqi Ren、Yuehan Cui 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_87bdb809a704)

> 现有基于大语言模型（LLM）的社会模拟常将调查数据机械拼接为提示，导致个体价值观呈现语义碎片化，且静态评估无法捕捉动态交互中的价值漂移。ExpertIVS 通过构建 14 个社会学专家智能体对世界价值观调查（World Values Survey, WVS）数据进行结构化归纳推理，生成逻辑连贯的个体档案，并引入多智能体辩论机制评估动态一致性。该方法在 480 名受访者上实现了 90.78% 的价值观还原保真度，但其高准确率是否源于 WVS 问题的强语义锚点，以及专家推理是否引入新的系统性偏差，仍需进一步审视。

】

---

【HACHIMI: Scalable and Controllable Student Persona Generation via Orchestrated Agents ｜教育理论锚定下的分布可控学生画像生成

研究机构：华东师范大学、香港科技大学

作者：Yilin Jiang、Fei Tan、Xuanyu Yin 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.04855)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c619ed3be22c)

> 大规模教育模拟亟需兼具心理真实性与群体统计效度的合成学生画像，以替代高成本的人工访谈。现有基于大语言模型（LLM）的生成方法虽能产出叙事性文本，却普遍存在内部自相矛盾与群体分布坍缩问题，且缺乏教育学理论的显式约束。本文提出理论对齐与分布可控画像生成（Theory-Aligned and Distribution-Controllable Persona Generation, TAD-PG）任务，并构建多智能体框架 HACHIMI，通过神经符号验证与配额调度实现硬约束下的规模化生成。该框架在内部一致性上表现优异，但在深层心理构念的外部效度上存在明显梯度衰减，其作为通用模拟基础设施的边界尚待厘清。

】

---

【LifeSim: Long-Horizon User Life Simulator for Personalized Assistant Evaluation ｜长程用户生活模拟器与个性化助手评估基准

作者：Feiyu Duan、Xuanjing Huang、Zhongyu Wei

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9b036b43f343)

> 导读 个性化助手面临的核心挑战在于如何在动态物理环境与用户长期认知状态约束下，维持交互的连贯性与个性化。现有基准多依赖静态或短上下文数据，无法反映真实世界中用户意图随时间、地点及情绪演变的复杂性，导致模型在隐式意图推断与长期偏好保持上表现不佳。LifeSim 通过信念-欲望-意图（Belief-Desire-Intention, BDI）认知引擎与事件引擎生成符合物理规律的生活轨迹，并构建包含 1,200 个场景的 LifeSim-Eval 基准，以量化模型在长程交互中的表现。该框架揭示了当前大语言模型（Large Language Models, LLMs）在显式意图处理上的优势与在隐式意图及长程记忆上的显著短板，但其评估主要依赖 LLM-as-Judge，缺乏对因果机制有效性的直接验证。

】

---

【Query-Focused Individual Simulation with Progressive Persona Completion ｜查询聚焦个体模拟中的渐进式人格补全

研究机构：日本东京大学、日本名古屋大学

作者：Weiwen SU、Naoki Yoshinaga、Masashi Toyoda

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b024fa529e4c)

> 基于大语言模型的角色模拟旨在以合成数据替代高成本的人类社会调查，其核心价值在于解决大规模行为数据获取的效率与隐私瓶颈。现有方法通常预设完整且静态的人格画像，但在面对普通个体时，这种“全量前置”策略不仅成本高昂，且因不同查询依赖不同维度而导致信息冗余或覆盖不足。本文切入点在于将人格构建从静态输入转化为查询驱动的按需获取闭环，通过渐进式预测与自报告置信度停止机制，在冷启动场景下以极少的请求数实现高保真模拟。这一范式在效率与质量间取得了平衡，但其对代理推断真实性的依赖仍存疑。

】

---

【TwinVoice: A Multi-dimensional Benchmark Towards Digital Twins via LLM Persona Simulation ｜多维人格一致性基准

研究机构：清华大学、美国罗格斯大学

作者：Bangde Du、Minghao Guo、Songming He 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c65448fc3224)

> 大语言模型（LLM）在模拟个体人格时存在“角色坍缩”与长期一致性缺失问题，现有评估多依赖合成数据且仅关注整体准确率，无法诊断具体失效环节。本文切入点在于构建基于真实数字足迹与虚构叙事的多维基准，将人格模拟解耦为思维连贯性与语言表达六项细粒度能力。通过判别式与生成式双重评估协议，TwinVoice 揭示了当前 SOTA 模型在记忆召回与语气保持上的显著短板。该基准填补了细粒度评估空白，但其生成式评估对 LLM 裁判的依赖及虚构数据维度的生态效度仍存疑。

】
