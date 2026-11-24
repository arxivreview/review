# ACL-Findings2026 · 用于分子与材料发现的LLM方向论文汇编

> 本方向共 11 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CheMM-R1: Enhancing Chemical Structure Recognition and Elucidation with Reasoning Multimodal Large Language Models ｜化学多模态推理基准与强化学习模型

研究机构：澳大利亚悉尼科技大学、澳大利亚新南威尔士大学

作者：Liting Huang、Zhihao Zhang、Shoujin Wang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9a89518a2571)

> 化学结构解析需整合2D结构图与多种光谱数据，但现有模型要么仅处理单一模态，要么缺乏显式推理步骤，导致无法可靠地从光谱反推分子结构。本文切入点在于构建首个要求多步视觉推理与五类光谱联合解析的基准CheMM-Bench，并基于此训练专用模型。方法上，采用冷启动知识注入结合领域适配的Group Relative Policy Optimization (GRPO) 强化学习框架。该工作验证了领域专用多模态大语言模型在复杂化学推理上的有效性，但其对光谱图像直接处理的鲁棒性及与专用化学模型的公平对比仍存疑。

】

---

【EvoMD-LLM: Learning the Language of Species Evolution in Reactive Molecular Dynamics ｜演化分子动力学大语言模型

研究机构：上海交通大学

作者：Zhichen Tang、Zhengzheng Dang、Yulin Chen 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.29394)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.29394)

> 现有大语言模型擅长处理静态分子结构，却难以捕捉反应体系中随时间演化的动力学因果逻辑。主流方法依赖外部模拟器或数值回归，无法在离散符号空间内内化连续物理过程的“语法”。EvoMD-LLM 将分子动力学轨迹重构为包含时长信息的符号事件序列，通过自回归语言建模实现反应路径预测。该框架在单一反应体系上展示了有效的时序推理能力，但其泛化边界与物理机制的可解释性仍存疑。

】

---

【Feedback to Reasoning: LLM-Assisted Molecular Optimization with Domain Feedback and Historical Reasoning ｜反馈驱动推理与历史知识积累

作者：Wenhan Gao、Xiran Fan、Chin-Chia Michael Yeh 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_138783dcf576)

> 分子优化是一个依赖专家迭代反馈的经验驱动过程，但现有LLM辅助方法要么忽略历史经验，要么仅传递静态动作指令，导致模型无法从失败中反思并复用化学洞察。F2R通过引入领域反馈驱动的自我反思机制与动态结构-活性关系（SAR）知识库，将LLM从被动生成器转变为能积累推理经验的智能体。该方法在16个单目标小分子优化任务中，使用GPT-4.1时于15个任务取得最高成功率。其价值在于证明了反馈推理优于动作引导，但SAR提取的准确性与错误知识的累积风险仍是未解之题。

】

---

【GLA: Grounding Large Language Models in Molecular Hierarchy for Chemical Understanding ｜几何语言对齐

作者：Yingxu Li、Jingjie Zeng、Zekun Wang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e970a4c75939)

> 分子-文本对齐长期受困于线性序列丢失拓扑层级，导致模型无法区分药效团核心与侧链修饰。现有方法将分子压缩为单一欧氏嵌入，造成“几何同质化”，混淆了结构语义。GLA通过混合曲率编码器解耦骨架与侧链，利用双视图对比学习实现细粒度对齐。该方法在检索与描述任务上验证了几何解耦的有效性，但其对大规模属性预测的增益有限，且未解决3D构象缺失问题。

】

---

【LLMs as Lab Engineers: A Benchmark for Analytical Method Lifecycle Management ｜分析化学全生命周期评估基准

研究机构：美国印第安纳大学、美国伍斯特理工学院

作者：Xiaoyi Chen、Mahsa Monshizadeh、Chaoqi Zhang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_890015eda920)

> 现有LLM化学基准多聚焦于静态知识问答或分子性质预测，无法覆盖实验室仪器故障诊断等动态、开放式的实操场景。本文通过构建涵盖仪器就绪、系统适用性、方法开发与故障排除的分析化学全生命周期基准，并引入专家Rubric评估，发现通用大模型在复杂诊断任务中表现优于专用微调模型，且检索增强生成（RAG）与人类引导思维链（CoT）能显著提升性能。这一发现挑战了“领域专用预训练必然更优”的直觉，但受限于小样本规模与单一仪器类型，其结论的普适性仍需更大规模验证。

】

---

【MCLE-Mol: Empowering LLM with Molecular Comprehension and Low-Cost Continual Evolution for Interpretable Property Prediction ｜分子性质预测中的语义鸿沟与可解释性：MCLE-Mol 框架

作者：Zhili Pu、Lantian Zhang、Hao Duan 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f4f0ce91506f)

> 导读 分子性质预测（Molecular Property Prediction, MPP）旨在从分子结构推断生物活性或毒性，是AI辅助药物发现的核心环节。图神经网络（Graph Neural Networks, GNNs）虽精度高但缺乏可解释性，而大语言模型（Large Language Models, LLMs）虽能生成解释却常因语义鸿沟导致幻觉与性能下降。MCLE-Mol通过注入机器学习（Machine Learning, ML）模型产生的子结构归因值，并引入上下文校准子结构归因规则（Context-Calibrated Substructure Attribution Rules, CCSAR）动态修正统计偏差，实现了性能与可解释性的平衡。该框架在BACE和BBBP上超越了部分专用GNN模型，但在HIV等大规模数据集上仍落后于全量训练的专家模型，其规则库的长期演化稳定性尚待验证。

】

---

【MolSafeEval: A Benchmark for Uncovering Safety Risks in AI-Generated Molecules ｜分子生成安全基准

研究机构：浙江大学、英国牛津大学

作者：Tong Xu、Xinzhe Cao、Zhihui Zhu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.00464)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.00464)

> 现有分子生成基准聚焦于新颖性与性质优化，却系统性地忽视了生成物可能携带的毒性或化学危害。这一盲区源于安全数据分散于监管标准与毒理数据库，难以被单一预测器覆盖。MolSafeEval 通过构建整合 83,925 个危险化合物的知识图谱，结合大语言模型（Large Language Model, LLM）推理，首次实现了跨任务类型的系统性安全评估。该框架填补了安全维度的空白，但其依赖已知危险分子相似性的机制，对全新毒性机制的捕捉能力存疑。

】

---

【MotifAgent: Learning Molecular Assembly through Multi-Agent Collaboration for Chemical Language Understanding ｜基团组装多智能体强化学习框架

研究机构：中国人民大学

作者：Jinjia Feng、Wenda Wang、Zhewei Wei

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9408604be095)

> 现有LLM处理分子时，将SMILES视为字符序列进行静态模式匹配，无法理解基团间动态连接规则，导致生成结构缺乏化学有效性。本文切入点在于将分子组装重构为多智能体协商问题，通过共享LLM骨干的基团代理在集中式训练与分布式执行框架下显式学习连接规则。具体做法是结合Set-based行为克隆与拓扑感知奖励塑形，使模型在重建与生成模式下均能动态构建2D拓扑。该框架在通用LLM基线上超越了专用模型，但其性能上限受限于2D拓扑输入，未验证3D构象约束下的泛化能力。

】

---

【REAP: Towards Effective Training-Free Chemical Reasoning with Explicit Atomic Priors ｜显式原子先验驱动的无训练化学推理

研究机构：香港科技大学、南京大学

作者：Mingxu Zhang、Dazhong Shen、Qi Zhang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b7f337270ce0)

> 大语言模型（LLM）在分子科学中面临的核心困境是缺乏细粒度化学先验，导致推理依赖表面结构启发式而非物理化学约束。现有训练式方法将知识固化于参数中，存在更新僵化与通用能力丧失的风险，而传统检索增强生成（RAG）仅依赖粗粒度实例匹配，缺乏证据支撑。REAP通过构建首个原子级文本知识库，并设计任务感知的先验选择与证据获取机制，使冻结LLM能够基于显式物理化学属性进行推理。该框架在性质预测任务上超越了无训练基线并逼近训练式模型，但其推理忠实度与复杂生成任务的适用性仍存疑。

】

---

【Seeing Beyond Words: MatVQA for Challenging Visual-Scientific Reasoning in Materials Science ｜材料科学多模态视觉推理基准 MatVQA

研究机构：加拿大蒙特利尔大学、加拿大魁北克人工智能研究所

作者：Sifan Wu、Huan Zhang、Yizhan Li 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c7ffc0b3def7)

> 现有材料科学基准多依赖纯文本问答，无法评估模型对显微图像、衍射图谱等视觉证据的细粒度解析能力，导致模型可能通过阅读图注而非观察图像本身来回答科学问题。MatVQA 通过自动化流水线从 arXiv 论文中提取推理链，并迭代消除语言与图注捷径，强制模型依赖低层视觉感知。该基准揭示了当前多模态大语言模型在科研级视觉推理上的显著短板，但其自动化生成流程是否引入新的偏差，以及领域微调模型失效的根本原因，仍需进一步验证。

】

---

【ToxReason: A Benchmark for Mechanistic Chemical Toxicity Reasoning via Adverse Outcome Pathway ｜基于不良结局通路的毒性机理推理基准

研究机构：韩国高丽大学

作者：Jueon Park、Wonjune Jang、Chanhwi Kim 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.06264)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.06264)

> 现有分子毒性预测模型仅关注结构到标签的映射，忽略了毒性产生的生物因果链条，导致预测结果缺乏可解释性与可靠性。本文切入点在于引入不良结局通路（Adverse Outcome Pathway, AOP）框架，将毒性评估从结果预测转化为从分子启动事件到器官级不良结局的因果推理任务。通过整合AOP-Wiki、ChEMBL与CTD数据构建193个化合物的推理基准，并采用强化学习优化因果一致性，使4B参数模型在预测与推理上超越更大规模模型。该工作验证了机理推理对毒性预测的增益，但受限于AOP覆盖范围与LLM评估的主观性，其结论在复杂真实场景中的普适性仍存疑。

】
