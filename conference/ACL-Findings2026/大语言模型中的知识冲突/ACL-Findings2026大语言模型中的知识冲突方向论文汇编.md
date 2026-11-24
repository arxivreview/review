# ACL-Findings2026 · 大语言模型中的知识冲突方向论文汇编

> 本方向共 12 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AED-RAG: Continuous Multi-Granular Context Fusion for Retrieval-Augmented Generation via Adaptive Ensemble Decoding ｜自适应集成解码

作者：Junzhe Zhou、Fulin Lin、Tairan Cheng 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_23efdcdbec71)

> 检索增强生成（RAG）面临检索粒度与生成效用错位的问题，粗粒度段落引入噪声，细粒度三元组缺乏语境，且传统离散重排截断了置信度信号。现有方法在平衡外部证据与内部记忆时，往往陷入“非此即彼”的硬选择，无法实现连续的概率融合。本文提出 AED-RAG，通过训练效用预测器并实施自适应集成解码，将段落、三元组与参数记忆映射至统一概率空间进行 Token 级软融合。该方法在通用问答基准上优于传统 RAG 基线，但其对冲突场景的鲁棒性及效用预测器的泛化能力存疑。

】

---

【AWARE: Agentic Knowledge Warehousing for Contextual Intelligence ｜代理知识仓库

研究机构：香港科技大学、中国人民大学

作者：Hongjin Qian、Siqi Bao、Zhao Cao 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d9c104e9df1a)

> 复杂信息检索任务中，答案相关证据稀疏地嵌入在海量异构文本中，导致大语言模型（LLM）在有限上下文预算内无法组装出足够解决任务的证据链。传统检索增强生成（RAG）单次注入缺乏深度，工具集成推理受限于上下文膨胀，均无法应对这种低知识密度下的“数据混乱”。AWARE 将检索重构为代理知识构建过程，通过离线文档结构化与在线多线程探索，将原始文本转化为紧凑的任务条件化知识表示。该框架在 GAIA 等基准上显著优于基线，但其性能增益究竟源于检索策略优化还是底层 LLM 推理能力的差异，尚存疑。

】

---

【Beyond Black-Box Interventions: Latent Probing for Faithful Retrieval-Augmented Generation ｜潜在空间探针驱动的忠实检索增强生成

研究机构：厦门大学、阿里巴巴集团

作者：Linfeng Gao、Qinggang Zhang、Baolong Bi 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.12460)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b7975816c614)

> 检索增强生成（RAG）系统在处理上下文与参数化知识冲突时，常因模型过度依赖内部记忆而丧失上下文忠实度。现有解码干预或偏好优化方法将大语言模型视为黑盒，无法诊断冲突发生的内部机制，导致在噪声环境下表现脆弱。本文切入点在于发现冲突知识在模型潜在空间中线性可分，并据此构建探针进行因果干预。ProbeRAG 通过知识剪枝、潜在冲突探针与冲突感知注意力三阶段框架，实现了从外部纠偏向内部引导的范式转移。该方法在多个基准上超越了最强基线，但其探针依赖特定模型训练，跨架构通用性仍存疑。

】

---

【CoDA: Restoring Contextual Dominance via Copy-Encouraged Attention Intervention for Mitigating RAG Hallucinations ｜基于复制鼓励注意力调度的RAG幻觉缓解

作者：JinWei Shi、Qizhuo Xie、Qianzi Hou 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3668ec879d08)

> 检索增强生成（RAG）在证据准确时仍产生幻觉，根源在于Transformer内部参数化知识对上下文证据的压制。现有解码干预方法仅调整输出分布，未修正内部信息路由；FFN抑制方法虽触及内部机制，但全局抑制导致参数知识丧失。CoDA将幻觉归因于注意力路由失败，通过推理时动态增强证据对齐的值状态，恢复上下文在残差流中的主导地位。该方法在忠实度上优于FFN抑制基线，但其对非复制头的强制复制是否引入语义扭曲，论文未提供直接证据。

】

---

【How Large Language Models Balance Internal Knowledge with User and Document Assertions ｜三元来源交互下的 LLM 决策平衡与区分能力评估

研究机构：新加坡南洋理工大学、美国加州理工学院

作者：Shuowei Li、Haoxin Li、Wenda Chu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.22193)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_52003acd71b6)

> 检索增强生成（RAG）与对话系统要求大语言模型（LLM）在参数化知识、用户断言与文档断言三者间进行动态权衡，但现有研究多局限于“参数-上下文”二元冲突，忽略了用户与文档作为独立来源时的差异化权重及交互效应。本文提出三元交互评估框架，通过13种探针变体量化27个模型对三源的依赖模式，发现模型普遍偏好文档断言且易受外部信息误导（“易感”型），并验证了混合监督微调（SFT）能显著提升模型区分有益与有害信息的能力。该工作填补了多源交互评估的空白，但其结论是否泛化至开放域长文本场景仍存疑。

】

---

【How Retrieved Context Shapes Internal Representations in RAG ｜检索增强生成中检索上下文对内部表征的塑造机制

作者：Samuel Yeh、Sharon Li

论文原文见 [arXiv](https://arxiv.org/abs/2602.20091)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2abd8adf8981)

> 检索增强生成（Retrieval-Augmented Generation, RAG）旨在通过外部文档弥补大语言模型（LLM）参数化知识的滞后与缺失，但实际检索结果常混杂相关、干扰及随机噪声，导致模型行为不可预测。现有研究多聚焦于输出层面的准确率或幻觉率，无法区分模型是有效整合了证据、抑制了内部记忆，还是触发了拒绝机制。本文通过受控实验分析不同相关性文档对LLM隐藏状态的层间动态影响，揭示了相关文档主要起确认作用而随机文档触发拒绝的表征模式。该工作为理解RAG失效提供了机制解释，但其仅停留在诊断层面，未提出具体的干预算法。

】

---

【NeuRAG: End-to-End Neural Knowledge Augmentation via Hyper-Neurons ｜神经化检索增强生成

研究机构：南开大学

作者：Liwei Zheng、Xuemin Liu、Jie Liu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6d0b007ecdb9)

> 检索增强生成（RAG）范式下，外部知识与模型内部推理长期处于解耦状态，导致复杂推理任务中知识集成碎片化。现有动态RAG方法虽能迭代注入文本，但受限于上下文窗口瓶颈及阶段式优化目标错位，无法实现参数级深度整合。NeuRAG将文档编码为LoRA模块构成的“超神经元”，通过隐藏状态驱动的路由机制在解码过程中动态重配置模型参数空间，实现检索与生成的端到端可微分耦合。该框架在通用多跳问答基准上优于现有参数化RAG基线，但其对知识冲突场景下的忠实度表现及参数融合后的可解释性尚未得到验证。

】

---

【No-Worse Context-Aware Decoding: Preventing Neutral Regression in Context-Conditioned Generation ｜无劣化上下文感知解码

作者：Yufei Tao、Ameeta Agrawal

论文原文见 [arXiv](https://arxiv.org/abs/2604.16686)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16686)

> 检索增强生成（RAG）中，模型常因非信息性上下文干扰而覆盖原本正确的答案，这一现象被称为中性回归。现有对比解码方法虽能提升冲突场景下的准确率，但缺乏“不伤害”保证，导致在上下文无用时仍改变输出。本文提出无劣化上下文感知解码（No-Worse Context-Aware Decoding, NWCAD），通过两阶段门控机制实现显式回退与动态路由。该方法在保持上下文利用能力的同时，从机制上杜绝了中性回归，但其在黑盒API模型中的适用性受限于logits访问权限。

】

---

【Not All Citations Are Equal:Entropy-Guided Citation Selection for Noise-Resistant Medical LLM ｜熵引导引用选择

作者：Minyu Gao、Hanlin Xiao、Ruoyu Wang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_183d809c4e9b)

> 医疗检索增强生成（RAG）中，模型在内部知识与外部检索冲突时往往盲目采信外部证据，导致检索噪声污染推理。现有解码干预方法仅调整输出分布，无法从根源修正模型对噪声引用的依赖偏好。本文切入点在于发现有效引用具有显著更低的Token级熵，将其作为奖励信号引入强化学习。通过无训练反思框架蒸馏数据，结合基于引用熵的GRPO训练，使模型内化选择性引用能力。该方法在医疗基准上稳定提升了噪声鲁棒性，但其熵信号在通用领域的泛化性及细粒度定位能力仍存疑。

】

---

【Rational Synthesizers or Heuristic Followers? Analyzing LLMs in RAG-based Question-Answering ｜群体证据动力学与启发式聚合

研究机构：美国卡内基梅隆大学

作者：Atharv Naphade

论文原文见 [arXiv](https://arxiv.org/abs/2601.06189)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.06189)

> 检索增强生成（RAG）系统面临的核心挑战在于，当模型面对多源、冗余且相互矛盾的检索文档时，其决策机制是否具备理性聚合能力。现有基准多聚焦于单文档或双文档的冲突仲裁，忽略了真实检索场景中“证据群体”对模型信念的扰动效应。本文通过构建 GroupQA 数据集，量化了模型在群体证据下的信念可塑性、翻转阈值及归因忠实度，揭示了大模型作为“启发式跟随者”而非“理性聚合器”的行为本质。这一发现挑战了 RAG 范式中关于模型能理性权衡证据的隐含假设，但缺乏针对该偏差的算法级干预方案。

】

---

【Resonant Context Anchoring: Decoupling Attention Routing and Signal Gain at Inference Time ｜共振上下文锚定

研究机构：中国科学技术大学、同济大学

作者：Mingkuan Zhao、Yide Gao、Wentao Hu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.01923)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.01923)

> 大语言模型在检索增强生成中常因参数化记忆干扰而忽略外部证据，导致事实幻觉。现有对比解码方法虽能缓解冲突，但需多次前向传播，显著增加推理延迟；激活工程方法则因粗粒度抑制破坏语言流畅性。本文提出共振上下文锚定（Resonant Context Anchoring, RCA），通过解耦注意力路由与信号增益，在单次前向传播中动态放大上下文Value向量范数，以提升残差流中的信噪比。该方法在Llama-3系列上实现了忠实度与流畅性的帕累托改进，但其仅针对单轮、单源冲突场景，且缺乏与主流对比解码方法的同骨干公平对比，通用性存疑。

】

---

【When Facts Change: Temporal Knowledge Conflict Resolution in LLMs ｜时间性知识冲突中的事实可变性诊断

作者：Jonas Wallat、Wolfgang Nejdl、Sandipan Sikdar

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_90f893989a76)

> 检索增强生成（RAG）系统面临参数化记忆与外部上下文的时间错位，导致模型在事实更新时产生冲突。现有解码干预方法假设冲突源于静态权重偏差，却忽略了事实本身的“可变性”这一动态仲裁信号。本文通过构建基于 Wikidata 真实时间戳的基准，诊断模型是否自发利用可变性进行推理，发现模型虽能识别可变事实，但推理与最终预测存在脱节。该工作揭示了当前 LLM 在时间性冲突中“知而不行”的机制缺陷，为后续基于内部状态的动态仲裁提供了关键诊断依据，但其结论局限于推理模型的文本轨迹，未验证非推理模型的内部表征。

】
