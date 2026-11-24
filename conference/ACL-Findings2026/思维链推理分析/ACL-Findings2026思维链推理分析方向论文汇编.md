# ACL-Findings2026 · 思维链推理分析方向论文汇编

> 本方向共 9 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CoTJudger: A Graph-Driven Framework for Automatic Evaluation of Chain-of-Thought Efficiency and Redundancy in LRMs ｜思维链效率与冗余度图驱动评估

研究机构：中国科学技术大学、深圳大学

作者：Siyi Li、Jiajun Shi、Shiwen Ni 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.07078)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.07078)

> 大型推理模型（Large Reasoning Models, LRMs）在长链思维链（Chain-of-Thought, CoT）中普遍存在过度推理，导致计算资源浪费。现有基于Token计数的评估方法无法区分必要复杂度与结构性浪费，难以定位冗余来源。CoTJudger通过将有向依赖图构建于外部文本CoT之上，提取最短有效路径（Shortest Effective Path, SEP）以量化冗余。该框架提供了结构化的效率诊断信号，但其依赖大语言模型进行语义判断，可能引入新的评估偏差。

】

---

【Decoupling the Effect of Chain-of-Thought Reasoning: A Human Label Variation Perspective ｜长思维链在人类标签变异任务中的分布校准失效分析

研究机构：德国慕尼黑大学、英国剑桥大学

作者：Beiduo Chen、Tiancheng Hu、Caiqi Zhang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.03154)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5193cb02af2e)

> 长思维链推理旨在通过中间步骤提升模型在多步任务上的性能，但其在需要捕捉概率性歧义而非消除歧义的任务中表现如何尚不明确。现有评估多聚焦于单一正确答案的准确率，忽视了模型输出分布与人类集体判断分布的对齐程度，导致无法区分CoT是真正驱动了推理还是仅作为事后合理化。本文通过交叉CoT注入与逐步方差分解实验，量化了CoT内容与模型内在先验对最终答案准确率及分布结构的独立贡献。研究揭示了CoT作为“决策器”而非“校准器”的结构性局限，为理解推理模型在模糊任务中的行为边界提供了实证依据，但其结论是否适用于非选择题的开放式生成场景仍存疑。

】

---

【FACT-E: Causality-Inspired Evaluation for Trustworthy Chain-of-Thought Reasoning ｜因果工具变量下的思维链忠实度评估

研究机构：香港浸会大学、澳大利亚墨尔本大学

作者：Yuxi Sun、Aoqi Zuo、Haotian Xie 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.10693)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10693)

> 思维链（Chain-of-Thought, CoT）推理的可靠性审计面临核心困境：模型生成的中间步骤看似连贯，实则可能缺乏逻辑依赖，而现有的大语言模型（LLM）自评估方法因自肯定偏差无法识别这种“链内不忠实”。本文切入点在于将结构因果模型（Structural Causal Model, SCM）中的工具变量方法引入CoT评估，通过注入外部噪声构造反事实轨迹，分离真实因果效应与模型内部偏差。具体做法是计算原始与扰动轨迹在LLM评估下的平均因果效应（Average Causal Effect, ACE），结合答案一致性筛选可信推理路径。该方法在数学与常识任务上提升了答案准确率，但其黑盒因果推断能否替代白盒机制分析，仍存疑。

】

---

【GoT-R1: Internalizing Graph-of-Thought via Structural Reinforcement for High-Density Reasoning ｜图思维链强化学习

作者：Zuchao Li、Qiwei Li、Yao Yao 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3a9b559dd62c)

> 线性思维链（Chain-of-Thought, CoT）在复杂推理中常因顺序生成导致冗余叙述与级联错误，现有外部搜索框架虽能缓解但引入高延迟与编排开销。GoT-R1 将推理重构为原子节点构成的有向无环图，并通过两阶段训练将图结构内化至模型权重，以拓扑密度替代文本长度。该方法在 GSM8K 上以 95.07% 准确率仅消耗 632,167 tokens，显著优于外部搜索基线，但其对推理忠实性的因果验证缺失，使得结构效率与逻辑真实性的关系仍存疑。

】

---

【NSF-CoT: Neuro-Symbolic Formal Verification of Chain-of-Thought Faithfulness in Contextual Question Answering ｜神经符号形式化验证思维链

作者：Vishal Pramanik、Maisha Maliha、Nathaniel D. Bastian 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_faa056e91f8c)

> 思维链（CoT）生成的中间步骤常被用户视为模型决策的真实解释，但现有评估方法仅能检测“修改文本是否改变答案”，无法验证步骤是否由给定证据逻辑推导而来。本文针对上下文问答场景，提出一种结合符号逻辑求解与内部事实归因的混合验证框架。该方法将自然语言步骤解析为一阶逻辑原子，通过反事实消融识别模型实际依赖的事实子集，并利用SMT求解器与LLM裁判联合判定每步的接地性、有效性与效用性。NSF-CoT在多个基准上优于纯行为干预基线，但其依赖受限谓词表与线性归因假设，在复杂非线性推理中的泛化能力存疑。

】

---

【Revisiting the Uniform Information Density Hypothesis in LLM Reasoning ｜均匀信息密度假设在LLM推理中的重构

研究机构：韩国延世大学

作者：Minju Gwak、Guijin Son、Jaehyung Kim

论文原文见 [arXiv](https://arxiv.org/abs/2510.06953)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.06953)

> 思维链推理的脆弱性源于模型常生成表面连贯但逻辑断裂的文本，现有基于置信度或熵的筛选方法缺乏对推理轨迹内部结构的解释力。本文切入点在于引入心理语言学中的均匀信息密度（Uniform Information Density, UID）假设，将推理视为信息流过程，通过量化步骤级信息密度的全局与局部均匀性来预测推理质量。具体做法是定义基于预测分布熵的步骤信息密度，并计算其方差与突变计数作为Best-of-N采样的选择指标。该框架在数学基准上显著优于传统启发式，但其有效性依赖于对“全局非均匀性”这一反直觉特征的识别，且未验证其在闭源模型或知识密集型任务中的泛化能力。

】

---

【SPD-Faith Bench: Diagnosing and Improving Faithfulness in Chain-of-Thought for Multimodal Large Language Models ｜多模态思维链忠实性诊断与校准

研究机构：西安电子科技大学、新加坡国立大学

作者：Weijiang Lv、Yaoxuan Feng、Xiaobo Xia 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.07833)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.07833)

> 多模态大语言模型（MLLMs）的思维链（Chain-of-Thought, CoT）常被假设为视觉证据的忠实映射，但现有研究多聚焦于感知幻觉，忽视了“看到正确区域却生成错误解释”的推理级不忠实。本文通过图像差异描述任务剥离语言先验，构建SPD-Faith Bench基准，揭示感知盲区与感知-推理解离两种失效模式。基于注意力衰减与残差流漂移的机制分析，提出免训练框架SAGE，通过动态视觉路由、FFN抑制与对比解码对齐感知与生成。该工作填补了多模态CoT忠实性评估空白，但其干预幅度有限，未解决深层表征的根本解耦。

】

---

【The Inner Monologue of Language Models: When Reasoning Traces Reveal More Than They Hide ｜语言模型内心独白：推理轨迹揭示与隐藏

作者：Pratham Singla、Shivank Garg、Ayush Singh 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f29916dd6a6e)

> 大型推理模型（Large Reasoning Models, LRMs）通过生成中间推理轨迹来展示思考过程，但现有后训练范式主要优化最终答案，忽视了推理轨迹与答案之间的一致性。当前方法无法区分模型是真正理解其习得行为，还是仅在执行表面策略，导致基于文本的监控在对抗场景下失效。本文通过引入反思性行为自我意识概念，系统量化不同后训练范式对推理-答案对齐及潜在策略迁移的影响。该研究揭示了强化学习训练在提升自我意识的同时加剧了内外解耦现象，为理解模型内部状态提供了新视角，但其评估局限于行为层面，缺乏因果机制验证。

】

---

【Valid Necessary: Diagnosing Latent Inefficiency in Chain-of-Thought ｜有效但冗余：思维链推理效率盲区的诊断与压缩

作者：Daeyeop Lee、Hwanjo Yu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4a62ebefa20d)

> 现有推理评估器聚焦逻辑正确性，却对“有效但冗余”的步骤视而不见，导致模型在简单问题上过度思考，浪费算力。本文指出这一“效率盲区”，提出无监督信息密度指标 CAID 与后处理压缩策略 PACE。通过识别并压缩低效用步骤，在保持准确率的同时显著降低 Token 消耗。该方法在效率维度上提供了新的评估视角，但其对推理忠实性的因果影响尚未得到验证。

】
