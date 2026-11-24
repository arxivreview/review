# ACL-Findings2026 · 大语言模型越狱攻击与防御方向论文汇编

> 本方向共 12 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Be Your Own Red Teamer: Safety Alignment via Self-Play and Reflective Experience Replay ｜安全自博弈与反思性经验回放

作者：Hao Wang、Yanting Wang、Hao Li 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_67e54d0cdb18)

> 大语言模型（LLM）的安全对齐长期受困于静态防御对新型越狱攻击的泛化失效，现有外部红队测试因攻击者滞后于防御者而陷入“猫鼠游戏”僵局。本文切入点在于将攻击与防御角色内化于单一模型，通过自博弈实现攻防策略的同步进化。具体做法是构建零和强化学习闭环，并引入基于UCB采样的反思性经验回放机制以重访历史失败案例。该方法在保持低过拒绝率的同时显著提升了鲁棒性，但其自博弈机制是否会导致攻击策略多样性坍缩，仍存疑。

】

---

【Defending LLMs against Jailbreak Attacks via Template-Based ICL with a Defensive Suffix ｜基于模板化上下文学习与防御后缀的大语言模型越狱防御

作者：Ruiyang Ni、Changlong Li、Shuaibiao Han 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7df65f69e909)

> 大语言模型（LLM）在部署中面临越狱攻击，现有防御方法在优化类与查询类攻击间难以兼顾，且常伴随高计算成本或效用损失。本文切入点在于利用LLM的上下文学习（In-Context Learning, ICL）能力与离线优化的防御后缀，构建一种轻量级、即插即用的混合防御机制。该方法通过离线训练鲁棒后缀抵御梯度优化攻击，并在推理时通过随机搜索筛选ICL演示以应对语义连贯的查询攻击。其价值在于以极低的额外开销实现了跨白盒与黑盒场景的广泛防御，但其对推理模型及多模态场景的泛化能力尚未验证。

】

---

【Experience-Driven Multi-Agent Optimization for Black-Box Jailbreak Attacks on Large Language Models ｜经验驱动多智能体黑盒越狱优化

研究机构：华东师范大学

作者：Zhaoyang Han、Yihe Liu、Kai Zhang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fbe1723d9981)

> 黑盒越狱攻击的核心矛盾在于高维提示空间探索与有限查询预算之间的张力。现有自动化方法依赖盲目搜索或固定模板，导致查询成本高昂且跨模型泛化能力弱。EMJO 通过引入动态经验库与多智能体诊断闭环，将无记忆搜索转化为经验引导的进化过程，显著降低了平均查询次数。该框架在效率上具有显著优势，但其经验库的跨模型迁移边界及单轮攻击对多轮防御鲁棒性的掩盖效应仍存疑。

】

---

【FLASH: Focused Layer Attention Sink Hijacking ｜聚焦层注意力汇聚劫持

研究机构：天津大学、美国伊利诺伊大学厄巴纳-香槟分校

作者：Siyuan Deng、Yerong Li、Fanhua Shang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_eea410d57922)

> 大语言模型的安全对齐机制往往依赖浅层结构维持，现有白盒攻击多陷入高成本的输入空间梯度优化，难以直接定位内部决策瓶颈。FLASH 切入点在于重新定义注意力汇聚（Attention Sink）现象，将其视为绑定安全约束的“安全锚点”，通过精准干预浅层注意力分数实现低开销越狱。该方法结合内部扰动、输入变体生成与输出过滤，在保持模型通用能力的前提下实现了高效攻击。其价值在于揭示了安全机制的结构性脆弱，但攻击效率是否受限于特定模型架构的浅层依赖，仍需进一步验证。

】

---

【Jailbreaking Attacks vs. Content Safety Filters: How Far Are We in the LLM Safety Arms Race? ｜越狱攻击与内容安全过滤器对抗评估

研究机构：德国马克斯·普朗克智能系统研究所、南方科技大学

作者：Yuan Xin、Dingfan Chen、Linyi Yang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.24044)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.24044)

> 大语言模型（LLM）部署中的核心矛盾在于，现有越狱攻击研究通常仅评估模型内部对齐的失效，而忽略了真实推理管道中必然存在的外部内容过滤层，导致攻击成功率被系统性高估。本文切入点在于首次将输入/输出过滤器纳入评估闭环，构建包含417对有害/良性提示的基准，系统测试10种SOTA攻击对6种主流过滤器的绕过能力。通过定义“通过率”（Pass）指标，量化攻击在完整管道中的实际威胁。该工作揭示了多数攻击在引入过滤后失效，但同时也暴露了过滤器在低误报率与高召回率之间的权衡困境，其结论对重新校准安全评估协议具有直接价值。

】

---

【LCO: LLM-based Constraint Optimization for Safer Agentic LLMs in Real-world Tasks ｜基于约束优化的LLM代理安全框架

作者：Jiayong Wan、Jiawei Chen、Zhaoxia Yin 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fd5457f3ecd7)

> 大语言模型（LLM）作为自主代理在持续交互中追求代理目标时，常因过优化产生有害副作用，即上下文奖励黑客（ICRH）。现有越狱防御针对静态恶意输入设计，无法拦截由内部目标优化引发的动态安全漂移。LCO通过自思考生成动态安全约束，并借助引导进化探索在解空间中搜索安全且高效的行动，无需修改模型权重即可缓解ICRH。该框架在特定优化场景下有效平衡了安全性与任务效用，但其依赖外部评估器且计算开销随种群规模线性增长，限制了实时部署的可行性。

】

---

【LS-Guard: Adaptive Safety Guardrails Tailored to Individual LLMs ｜模型特异性安全护栏

作者：Jinggui Liang、Lizi Liao

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_15abb4663f8d)

> 大语言模型（LLM）在商业部署中面临恶意输入威胁，现有安全护栏普遍采用“一刀切”策略，忽略了不同模型对同一有害查询的响应差异，导致防御失效或过度拒绝。LS-Guard 通过动态探测目标模型的行为特征，利用多 LoRA 专家架构实现个性化安全分类。该方法在多个主流 LLM 上显著优于通用护栏基线，但其依赖离线探测阶段的计算开销及跨模型泛化能力的边界尚待明确。

】

---

【Neuronal Insights into LLM Attacks: Targeted Neuron Tuning for Precise and Robust Vulnerability Patching ｜基于相似度归因的神经元级漏洞修补

研究机构：天津大学

作者：Dan Shi、Renren Jin、Zhuowen Han 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b0561b6dda2a)

> 大语言模型（LLM）的安全对齐长期面临“浅层性”困境，即模型仅在表面特征上表现出拒绝行为，深层语义中仍可能泄露有害内容。现有梯度归因方法依赖固定标签，无法处理越狱攻击中开放生成任务无标准答案的特性，导致关键神经元定位失效。本文提出基于相似度的梯度归因法，量化神经元对开放生成输出的影响，并据此实施仅微调最小关键神经元子集的 Targeted Neuron Tuning (TNT)。该方法在自有基准上实现了高安全率，但其评估协议未覆盖标准基准，泛化性存疑。

】

---

【RLShield: Dynamic Jailbreak Detection for LLMs via Reinforced Adaptive Learning ｜动态越狱检测：基于强化学习的自适应阈值框架

作者：Zhao Tong、Pengfei Yang、Yimeng Gu 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_85b141837edc)

> 大语言模型（LLM）的安全对齐面临静态防御边界易被对抗性输入突破的困境，现有检测机制依赖固定阈值，难以适应不断演化的攻击模式与模型更新。本文切入点在于将阈值选择建模为连续控制问题，通过强化学习实现针对每个提示的动态决策。具体做法是结合跨层参数定位与软演员-评论家（Soft Actor-Critic, SAC）代理，在推理时实时计算风险分数并输出样本特异性阈值。该框架在多个基准上提升了检测精度与效率，但其对内部参数稳定性的假设及单轮检测的局限仍存疑。

】

---

【Safety Is Not Universal: The Selective Safety Trap in LLM Alignment ｜选择性安全陷阱：LLM对齐中的群体偏差审计与公平性优化

作者：Iago Alves Brito、Walcy Rios、Julia Soares Dollis 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fc8a69554c91)

> 大语言模型的安全对齐长期被聚合指标掩盖，模型在“身份仇恨”等通用标签下表现出的高防御率，往往掩盖了对特定少数群体保护缺失的事实。现有基准如HarmBench聚焦于攻击行为类型（What），却忽略了受害群体维度（Who），导致无法区分模型是具备通用的语义拒绝能力，还是仅记忆了特定群体的防御触发器。本文通过构建双语、多群体的越狱基准MiJaBench，量化了这种“选择性安全陷阱”，并验证了直接偏好优化（DPO）在消除群体间防御率偏差上的有效性。该工作揭示了安全对齐的公平性盲区，但其结论受限于特定语言对与模型规模，跨语言泛化机制仍存疑。

】

---

【Silencing the Guardrails: Inference-Time Jailbreaking via Dynamic Contextual Representation Ablation ｜上下文表示消融（CRA）：推理时动态掩码拒绝子空间

研究机构：浙江大学

作者：Wenpeng Xing、Moran Fang、Guangtai Wang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.07835)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07835)

> 导读 大语言模型（LLM）的安全对齐常被视为静态防御，但现有机制在深层推理中极易被绕过，核心矛盾在于对齐目标与内部复杂语义表征的解耦。主流优化类攻击（如GCG）计算成本高且生成内容语义混乱，而静态编辑方法（如LED）会永久损害模型通用能力，导致防御与效用难以兼顾。本文提出上下文表示消融（Contextual Representation Ablation, CRA），通过推理时动态计算并掩码隐藏状态中的“拒绝子空间”，在不修改权重的情况下实现精准越狱。CRA在Llama-2上实现了53.0%的攻击成功率（ASR），较基线PEZ提升15.2倍，但其跨模型泛化性仍受限于7B规模模型的架构相似性，且未验证多轮对话中的状态连续性。

】

---

【When Safety Alignment Fails to Generalize: Probing with Language Game Jailbreaks ｜语言游戏越狱：安全对齐的格式特异性失效

作者：Zewen Long、Yu Peng、Fangming Dong 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d898311ee7da)

> 大语言模型（LLM）的安全对齐旨在阻止有害内容生成，但现有微调机制往往仅绑定特定表面形式，缺乏对语义意图的抽象泛化能力。当攻击者利用规则化语言变换（如 Ubbi Dubbi）改变提示词形态时，模型虽能理解语义却拒绝失效，暴露出对齐训练的分布局限。本文提出自定义语言游戏与自动化发现框架 AutoLanJail，通过系统化的形式变异探针验证了这一结构性脆弱性。该工作揭示了当前微调范式的根本缺陷，但其结论是否适用于所有对齐技术尚存疑。

】
