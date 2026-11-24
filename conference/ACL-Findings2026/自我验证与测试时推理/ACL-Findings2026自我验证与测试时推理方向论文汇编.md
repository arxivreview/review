# ACL-Findings2026 · 自我验证与测试时推理方向论文汇编

> 本方向共 16 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【a1: Steep Test-time Scaling Law via Environment Augmented Generation ｜环境增强生成

研究机构：中国科学院、美国加州大学默塞德分校

作者：Lingrui Mei、Shenghua Liu、Yiwei Wang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f48bb6d7678d)

> 大语言模型在复杂推理中常因早期步骤错误导致后续推导级联失效，现有测试时扩展方法多依赖静态提示或内部状态验证，缺乏对中间步骤的实时外部校正机制。本文提出环境增强生成（Environment Augmented Generation, EAG）框架，通过实时环境反馈与动态分支探索解决错误传播问题。该方法将推理形式化为马尔可夫决策过程，利用执行环境验证每一步骤并引导路径选择。EAG在32B模型规模上实现了与更大模型相当的竞赛数学性能，但其依赖外部执行环境的设定限制了其在无代码接口任务中的直接适用性。

】

---

【Adversarial Yet Cooperative: Multi-Perspective Reasoning in Retrieved-Augmented Language Models ｜对抗协同：检索增强中的多视角推理

研究机构：华东师范大学、东南大学

作者：Can Xu、Lingyong Yan、Jiayi Wu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.04651)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.04651)

> 检索增强生成（RAG）系统在处理冲突或误导性外部文档时，单一智能体的自回归推理往往放大而非抑制错误，且基于最终结果的任务级奖励无法区分逻辑严谨的推导与侥幸猜对。现有自反思范式受限于“单一视角”架构，模型难以识别自身逻辑缺陷，导致验证过程陷入非收敛的镜像循环。本文提出对抗推理RAG（ARR），将推理与验证解耦为两个独立智能体，通过基于策略熵变化的过程感知优势函数实现内生过程监督。该方法在多个问答基准上显著优于单智能体基线，但其验证器本身仍依赖语言模型内部状态，是否构成真正的外部接地存疑。

】

---

【AgentV-RL: Scaling Reward Modeling with Agentic Verifier ｜代理式验证器

研究机构：复旦大学、华中科技大学

作者：Jiazheng Zhang、Ziche Fu、Zhiheng Xi 等 16 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.16004)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16004)

> 测试时扩展（Test-Time Scaling, TTS）旨在通过增加推理计算量提升大语言模型（LLM）的解题准确率，但其效能高度依赖验证器从候选解中筛选正确路径的能力。现有生成式奖励模型（GenRM）因单轮推理导致错误传播，且缺乏外部工具接地，在计算密集型任务中易产生幻觉。本文提出 Agentic Verifier，通过双向代理协同与工具调用实现多轮验证，并设计 AgentV-RL 训练配方将其能力蒸馏至单模型。该方法在数学基准上显著超越传统奖励模型，但高延迟与特定难度下的性能瓶颈限制了其通用性。

】

---

【Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction ｜打破上下文惯性：基于单轮锚点的强化学习

作者：Xingwu Chen、Zhanqiu Zhang、Yiwen Guo 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.04783)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.04783)

> 多轮交互中，大语言模型（LLM）常因固守前轮错误推理而忽略用户的新约束，导致性能较单轮场景显著下降。现有方法多通过弃权或澄清请求缓解信息不足，但无法处理需动态修正的“错误纠正”场景，且未触及模型内部对历史轨迹的刚性依赖这一根本原因。本文提出 RLSTA，利用模型自身在单轮全信息下的正确回答作为内部奖励锚点，通过强化学习校准多轮生成行为。该方法在数学与代码任务上显著优于标准微调，但其在缺乏明确单轮解的开放域任务中的泛化能力仍存疑。

】

---

【Confidence-Weighted Token Set Cover for Early Hypothesis Pruning in Self-Consistency ｜置信度加权集合覆盖

作者：Md Arafat Sultan、Ramón Fernandez Astudillo

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5f66374f4fb0)

> 自一致性（Self-Consistency, SC）通过并行采样多数投票提升大语言模型（LLM）推理准确率，但固定生成所有路径导致Token消耗随采样数线性增长，限制了其在高延迟敏感场景下的实用性。现有串行剪枝方法虽降低Token量，却牺牲了GPU并行计算优势，导致延迟显著增加。本文提出置信度加权集合覆盖（Confidence-Weighted Set Cover, CWSC），在保持完全并行的前提下，通过每步动态剪枝低效假设，实现10-35%的Token节省。该方法在5个LLM和3个数学基准上验证了效率增益，但未突破SC的准确率上限，且剪枝对高难任务的多样性损失影响尚不明确。

】

---

【Enhancing Long-Chain Reasoning Distillation through Error-Aware Self-Reflection ｜错误感知自反思蒸馏

作者：Zhuoyang Wu、Xinze Li、Zhenghao Liu 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3d8d959ff2e3)

> 长思维链（Long-CoT）蒸馏旨在将大模型的推理能力迁移至小模型，但教师生成的复杂轨迹常超出学生容量，导致训练不稳定或过拟合。现有直接蒸馏方法忽视了学生自身错误模式对监督信号的适配价值。本文提出 ORION，利用学生自生成的错误作为条件，反向精炼教师 CoT 以构建适配学生能力的训练数据。该方法在多个数学基准上稳定提升 2% 以上，但其收益依赖于学生初始错误分布的质量，且未验证在开放域任务中的泛化性。

】

---

【Format-Adapter: Improving Reasoning Capability of LLMs by Adapting Suitable Format ｜格式自适应测试时扩展

作者：Dingzirui Wang、Xuanliang Zhang、Rongyu Cao 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_77bd7ff5b23b)

> 测试时计算扩展（Test-Time Scaling, TTS）旨在通过增加推理时的计算资源来提升大语言模型（LLM）的推理性能，但现有并行扩展方法通常局限于固定推理格式，导致模型在特定格式下产生的系统性误差无法通过增加采样次数消除。本文指出，格式选择是塑造解空间分布的核心变量，固定格式下的TTS仅能降低方差，而多格式TTS能扩展推理模式以突破能力上限。FORMAT-ADAPTER通过生成候选格式并基于误差最小化原则进行贪心选择，实现了无需训练的格式自适应TTS。该方法在数学与常识推理基准上平均提升2.2%的相对性能，但其依赖LLM打分作为代理损失的可靠性仍存疑，且未验证格式多样性对极端复杂任务的覆盖能力。

】

---

【How Do Answer Tokens Read Reasoning Traces? Self-Reading Patterns in Thinking LLMs for Quantitative Reasoning ｜答案Token如何读取推理轨迹：思考型LLM中的自读模式

研究机构：南京大学、阿里巴巴集团

作者：Haoyang Chen、Yi Liu、Jianzhi Shao 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.19149)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.19149)

> 思考型大语言模型在生成最终答案前会先输出长推理轨迹，但答案Token究竟如何从这些轨迹中提取关键信息以生成可靠结果，此前缺乏机制层面的解释。现有激活引导方法主要优化推理轨迹本身的生成质量，却忽略了答案解码阶段对轨迹的“读取”行为，导致模型在内部状态不确定时仍可能输出错误答案。本文通过注意力分析发现正确解存在“良性自读”模式，并据此构建无训练引导向量以提升准确率。该方法在GSM8K上带来最高2.6%的提升，但其效果是否源于注意力模式本身还是样本筛选偏差，尚存疑。

】

---

【IREASONER: Trajectory-Aware Intrinsic Reasoning Supervision for Self-Evolving Large Multimodal Models ｜轨迹感知内在推理监督

作者：Meghana Sunil、Manikandarajan Venmathimaran、Muthu Subash Kavitha

论文原文见 [arXiv](https://arxiv.org/abs/2601.05877)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6aa90e10bcce)

> 多模态大模型（LMM）在无标注数据上的自进化长期受限于“结果级奖励”的盲区：模型仅根据最终答案的一致性获得梯度信号，导致中间推理步骤缺乏约束，即使答案正确，推理路径也可能充满幻觉或逻辑断裂。现有自进化框架（如EvoLMM、VisPlay）虽实现了无监督闭环，但无法区分“正确推理”与“碰巧正确的错误推理”。IREASONER 通过引入基于跨轨迹步骤一致性的内在奖励，将优化目标从答案层下沉至推理步骤层，在不依赖外部真值或标注的情况下，实现了对中间推理过程的直接监督。该方法在纯无监督后训练中带来了最高+2.1点的性能增益，但其有效性高度依赖于主导答案组的正确率，且仅验证了文本步骤的语义对齐，未触及视觉编码器内部的特征一致性。

】

---

【PuzzleClone: A DSL-Powered Framework for Synthesizing Verifiable Data ｜谜题克隆：基于领域特定语言的可验证数据合成框架

作者：Kai Xiong、Yanwei Huang、Rongjunchen Zhang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5f95ccefb08e)

> 大语言模型在复杂逻辑推理中常因训练数据稀缺且缺乏可靠真值而表现受限，现有基于大模型生成的数据合成方法存在可靠性低、多样性不足及验证成本高的瓶颈。PuzzleClone 提出了一种基于领域特定语言（DSL）的形式化数据合成框架，通过程序化验证确保生成谜题的逻辑正确性。该框架构建了包含 83,657 个可验证谜题的基准 PC-83K，并验证了其在强化学习训练中的有效性。尽管该方法在数据可靠性上实现了突破，但其依赖人工编码 DSL 规范的特性限制了其向非结构化任务自动扩展的能力。

】

---

【Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning ｜可靠性感知自适应自一致性

研究机构：韩国首尔大学

作者：Junseok Kim、Nakyeong Yang、Kyungmin Min 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.02970)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.02970)

> 大语言模型在复杂推理中常因解码随机性导致单次生成不可靠，自一致性（Self-Consistency, SC）通过多路径采样聚合提升准确率，但固定预算造成计算资源浪费。现有自适应方法依赖计数停止规则，忽略响应可靠性差异，导致证据累积低效。ReASC 引入响应级置信度信号，将采样决策从“计数”重构为“证据充分性”判断，通过两阶段门控机制动态调整采样量。该方法在保持精度的同时大幅降低推理成本，但其效率增益高度依赖置信度信号的质量与校准机制的稳定性。

】

---

【Self-Consistency from Only Two Samples: CoT-PoT Ensembling for Efficient LLM Reasoning ｜双模态一致性集成

研究机构：美国卡内基梅隆大学

作者：Raman Saparkhan、Majd Hawasly、Md Rizwan Parvez 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17433)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17433)

> 大语言模型在复杂推理中常因自回归生成的局部误差累积导致最终答案失效，而提升准确率的自一致性（Self-Consistency, SC）范式需消耗大量采样预算（如40次），造成高昂的计算延迟。现有早停方法依赖单一模态内的多数投票，难以捕捉语义层面的真实共识，导致效率与精度无法兼得。本文提出结合思维链（Chain-of-Thought, CoT）与程序思维（Program-of-Thought, PoT）的双模态集成框架，利用两种推理模式间低相关的错误分布，通过贝叶斯假设检验实现跨模态一致性早停。该方法在保持甚至提升精度的同时，将平均采样次数降低9.3倍，78.6%的任务仅需2次采样即可解决，但其性能高度依赖模型对PoT模态的内在能力，在弱推理模型上存在显著退化风险。

】

---

【Step Potential Advantage Estimation: Harnessing Intermediate Confidence and Correctness for Efficient Mathematical Reasoning ｜步骤潜力优势估计

作者：Fei Wu、Zhenrong Zhang、Qikai Chang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2fb631f15415)

> 长链思维模型在强化学习训练中常陷入“过度检查”陷阱，即在已得出正确答案后仍持续生成冗余验证步骤，甚至将正确结论篡改为错误答案。现有基于Token熵或序列长度的优化方法缺乏语义层面的进度感知，无法区分必要推导与无效验证。本文提出无需训练的探针机制提取步骤级置信度与正确性，构建“步骤潜力”信号以指导强化学习的信用分配。该方法在多个数学基准上同时提升了准确率并显著缩短了推理长度，但其依赖真值答案进行探针计算，限制了其在无标注开放域任务中的直接迁移。

】

---

【Tracing the Light of Thought: A Probabilistic Self- and Cross-Consistency Verification Mechanism Improving Mathematical Reasoning in LLMs ｜基于 Metropolis 采样的自洽性验证机制

研究机构：英国纽卡斯尔大学

作者：Xiaoyang Liu、Dawei Wang、Tian Li 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a91651ba1d72)

> 大语言模型在复杂数学推理中常因自回归生成的错误级联导致最终答案失效，而传统的自一致性（Self-Consistency, SC）策略在难题上因正确解概率极低而失效。本文切入点在于利用 Metropolis Light Transport (MLT) 思想，将随机采样转化为序列式迭代采样，通过接受-拒绝机制集中计算资源于高正确性区域。具体做法是构建基于 logprob 的轻量级正确性函数引导采样方向，并扩展为多模型交叉验证。该方法在弱模型上显著优于 SC，但在强模型上提升有限，且依赖 logprob 校准的稳定性。

】

---

【TT-SI: Self-Improving LLM Agents with Test-Time Training ｜测试时自我改进（TT-SI）：基于不确定性门控的代理模型即时适配

作者：Emre Can Acikgoz、Cheng Qian、Heng Ji 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6c5fb1416866)

> 导读 大语言模型（LLM）在代理任务中常因训练数据冗余或分布偏移导致泛化失效，传统归纳式微调需消耗海量标注数据且易引发灾难性遗忘。现有测试时扩展方法多聚焦于推理采样或外部验证，缺乏对模型参数层面的即时、轻量级适应机制。本文提出测试时自我改进（Test-Time Self-Improvement, TT-SI）框架，通过识别不确定样本、自合成相似实例并执行临时LoRA微调，实现无外部标注的在线能力适配。该范式在数据效率上显著优于全量微调，但其“临时更新后重置”机制是否阻碍了跨样本知识的长期累积，仍是核心存疑点。

】

---

【TTVS: Boosting Self-Exploring Reinforcement Learning via Test-time Variational Synthesis ｜测试时变分合成

研究机构：香港科技大学

作者：Sikai Bai、Haoxi Li、Jie Zhang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.08468)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.08468)

> 测试时训练（Test-Time Training, TTT）旨在让大语言模型在推理阶段利用无标注数据自我进化，但现有方法受限于静态测试集，易导致模型过拟合表层文本模式而非底层逻辑。本文切入点在于将静态查询动态转化为语义等价的变体流，通过在线变分合成与双模式探索机制，迫使模型学习不变的问题逻辑。该方法在仅使用无标注测试数据的前提下，显著超越了依赖大规模标注数据的强化学习后训练模型。其价值在于证明了动态数据增强对测试时适应的必要性，但变体生成的质量边界与潜在分布偏移风险仍存疑。

】
