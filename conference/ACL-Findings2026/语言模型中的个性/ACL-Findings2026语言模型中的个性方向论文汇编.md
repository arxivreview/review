# ACL-Findings2026 · 语言模型中的个性方向论文汇编

> 本方向共 11 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【At Your Own PACE: A Causal Framework for Evaluating EQ in LLMs ｜因果校准的大语言模型情商评估框架

作者：Lei Lyu、Shengling Wang、Ke Chao 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_12d3760083f9)

> 大语言模型（LLM）在情感交互中常陷入“诊断有余、恢复不足”的困境，且现有评估指标因维度割裂无法反映整体能力。传统量表侧重自我调节，直接迁移至LLM会导致目标错位，而分散测试忽略了维度间的协同效应。本文提出PACE分类法与因果推断框架，通过反事实干预解耦维度混杂，构建闭环评估体系。该框架在人类偏好对齐上达到89.31%，但评估结果高度依赖多智能体仲裁机制，其因果权重的跨模型泛化性存疑。

】

---

【Beyond Fixed Psychological Personas: State Beats Trait, but Language Models are State-Blind ｜基于潜在状态-特质理论的心理方差分解与AI系统盲区诊断

研究机构：美国佛蒙特大学

作者：Tamunotonye Harry、Ivoline Ngong、Chima Nweke 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.15395)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.15395)

> 大语言模型（LLMs）在个性化交互中面临的核心矛盾是：用户行为由稳定特质（Trait）与情境状态（State）共同决定，但现有AI系统仅能处理前者。传统人格数据集（如PersonaChat）假设人格为固定属性，忽略了情境对心理表达的动态塑造，导致模型生成与评估环节出现系统性偏差。本文通过构建首个支持状态-特质分解的Reddit数据集Chameleon，利用潜变量状态-特质（Latent State-Trait, LST）理论量化方差来源，并诊断LLM与奖励模型（Reward Model）在处理心理情境时的失效模式。该工作揭示了74%心理方差源于情境这一关键事实，但仅停留在诊断层面，未提供具体的控制算法，其结论在跨文化泛化性上仍存疑。

】

---

【Beyond Static Personas: Situational Personality Steering for Large Language Models ｜情境感知的人格神经元检索与调制

研究机构：中国科学技术大学、新加坡管理大学

作者：Zesheng Wei、Mengxiang Li、Zilei Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1a90fd517faa)

> 大语言模型（LLM）的人格控制长期受困于静态特质假设，导致模型在复杂交互中无法像人类一样根据情境动态调整行为。现有激活引导或稀疏编辑方法虽能实现免训练的人格注入，但缺乏对“情境-行为”一致性的显式建模，导致跨情境泛化能力不足。本文提出IRIS框架，通过构建情境人格神经元库并基于相似度检索进行加权调制，实现了免训练的情境自适应人格控制。该方法在新增基准SPBench上取得SOTA表现，但其依赖预构建的历史情境库，限制了其在完全未知情境下的即时适应能力。

】

---

【Chameleons and Guardians: Unveiling the Divergence in Personality Plasticity and Cognitive Resistance across LLMs ｜多智能体人格诱导框架

作者：Jiaxin Wu、Jie Zhao、Huangxinrong 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_265887caac73)

> 大语言模型（LLM）的人格可控性研究长期面临输入端提示诱导的稳定性缺陷，传统角色指令易受上下文漂移影响且无法跨模型泛化。本文切入点在于揭示不同LLM家族在人格诱导上的合规性分歧，即西方模型的高可塑性与东方模型的认知抵抗。通过构建生成器-裁判多智能体协作框架，将MBTI题目改写为语义等价但表达多样的诱导语境，实现免训练的人格重塑。该框架在输入端实现了细粒度控制，但未触及内部表示机制，其相对于白盒激活工程的优越性尚存疑。

】

---

【Do Personality Traits Interfere? Geometric Limitations of Steering in Large Language Models ｜人格特质干扰：大语言模型中转向的几何局限

研究机构：澳大利亚西澳大学、澳大利亚麦考瑞大学

作者：Pranav Bhandari、Usman Naseem、Mehwish Nasim

论文原文见 [arXiv](https://arxiv.org/abs/2602.15847)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.15847)

> 大语言模型（LLMs）的人格控制旨在通过内部表示干预实现特定特质的稳定表达，但现有激活工程方法隐含假设人格特质在激活空间中是线性独立的。这一假设导致在操纵单一特质时，其他特质发生不可预测的漂移，且强制正交化虽能消除几何重叠，却以牺牲生成流畅度为代价。本文通过系统分析 Big Five 人格转向向量的几何关系，并测试从软白化到硬正交化的多种约束策略，揭示了特质间存在持久的行为耦合，证明几何独立性并非行为独立性的充分条件。该研究挑战了“正交即解耦”的直觉，但受限于仅使用两个模型家族和 LLM 裁判评估，其结论的普适性仍需更多验证。

】

---

【DPN-LE: Dual Personality Neuron Localization and Editing for Large Language Models ｜稀疏神经元定位与编辑

研究机构：东南大学、上海交通大学

作者：Lifan Zheng、Xue Yang、Jiawei Chen 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.27929)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bd82969f02ee)

> 大语言模型（LLMs）在注入特定人格特质时，常因修改大量神经元而严重损害通用推理能力。现有神经元编辑方法（如NPTI）缺乏对神经元功能的细粒度区分，导致“对齐税”过高。本文切入点在于利用对立人格特质在激活空间中的互斥性，通过双准则过滤定位极少量特质专属神经元。具体做法是构建MLP激活引导向量，结合Cohen's d效应量与激活幅度进行稀疏干预。该方法在保留96%以上神经元未修改的前提下，将通用能力损失降低至全量编辑方法的三分之一，但其在多特质组合下的几何干扰机制尚未被验证。

】

---

【EmoRes: Toward Adaptive Psychological Support via User-Agnostic Benchmark and Topic-Mining Agent ｜情绪共鸣心理支持框架

作者：Zhengwei Zou、Xuanming Jiang、Baoyi An 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a9181e30ba41)

> 心理支持对话系统面临的核心矛盾是维持治疗连贯性与适应个体差异之间的平衡，现有递归上下文拼接方法导致对话停滞与情感碎片化。EmoRes 通过引入基于焦点解决短期治疗（Solution-Focused Brief Therapy, SFBT）的多智能体架构，将主题挖掘与自我反思解耦为两个协同代理，在推理时动态调节对话流向。该框架在自建基准 VeilEval 上实现了约 3 倍的性能提升，但其依赖合成数据与 LLM 评估的闭环验证，使得临床效度的外部泛化性存疑。

】

---

【How Value Induction Reshapes LLM Behavior ｜价值观诱导的间接效应分析

研究机构：丹麦哥本哈根大学、Anthropic

作者：Arnav Arora、Natalie Schluter、Katherine Metcalf 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0682d64cb862)

> 大语言模型（LLM）在生成文本时往往表现出特定的行为特质，但现有研究多关注单一特质的注入，忽略了特质间的系统性耦合。传统提示工程或单一维度的微调难以量化诱导某一价值观（如诚实）如何改变其他未诱导价值观（如创造力）的表达频率，且缺乏对安全性与拟人化语言影响的统一评估框架。本文通过构建基于偏好数据的价值观子集，利用直接偏好优化（Direct Preference Optimization, DPO）微调模型，系统性地测量了15种价值观诱导后的下游行为变化。该工作揭示了价值观诱导的“涟漪效应”，即正面价值观的注入不仅提升安全性，还显著增加了拟人化语言的使用，为理解模型对齐的副作用提供了实证基础，但其结论受限于特定模型家族与数据规模。

】

---

【PsyPath: Psychologically-guided Self-Exploration for Personality Detection ｜心理引导自探索人格检测

研究机构：北京大学

作者：Zheng Li、Hongxin Ding、Chenyu Zhang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_86dd14c75545)

> 文本人格检测长期受困于静态映射的局限，直接预测或固定问卷推理均无法捕捉临床心理学中动态诊断的逻辑。PsyPath 将人格推断重构为基于心理学的动态问答搜索过程，通过蒙特卡洛树搜索（MCTS）生成高置信度推理路径，并利用直接偏好优化（DPO）将这种诊断逻辑内化至模型。该方法在 MBTI 和 Essays 数据集上显著提升了预测准确率与可解释性，但其依赖外部 LLM 评分的机制是否真正解决了自报告与行为脱节的根本矛盾，仍存疑。

】

---

【Stable and Explainable Personality Trait Evaluation in Large Language Models with Internal Activations ｜基于内部激活的稳定性人格评估

研究机构：美国佐治亚理工学院、华南理工大学

作者：Xiaoxu Ma、Xiangbo Zhang、Zhenyu Weng

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_54dae42eb74d)

> 大语言模型（LLMs）的人格评估长期受困于提示词敏感性，导致同一模型在不同措辞下产生剧烈波动的人格分数。现有自报告与开放问答范式将表面行为混淆为稳定特质，无法区分提示诱导的临时表现与模型内在的行为偏差。本文提出 Persona-Vector Neutrality Interpolation (PVNI)，利用内部激活空间中的对比向量进行线性插值，以解耦提示干扰并量化中性人格强度。该方法在稳定性上显著优于传统量表，但其理论假设的线性边界及跨模型泛化能力仍存疑。

】

---

【ToMELP: A Theory-of-Mind Benchmark for Route-Controlled Persuasion under the Elaboration Likelihood Model ｜心智理论引导的精细加工可能性说服基准

作者：Ruirui Wang、Haoran Zhang、Tian Lan 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7e9e1302d33f)

> 说服对话中的心智理论（Theory of Mind, ToM）评估长期受困于“能答对问题”与“能据此行动”之间的鸿沟，现有基准缺乏对受众信息处理路径的显式控制，导致模型表现归因模糊。ToMELP 通过构建受众画像（Persona）与精细加工可能性模型（Elaboration Likelihood Model, ELM）双路径的 2×2 因子设计，将 ToM 推断与策略执行解耦为可审计的闭环。该基准揭示了 ToM 注入在外围路径下的稳定增益与中央路径下的证据组织瓶颈，但其依赖 LLM-as-a-judge 且未进行人类一致性验证，限制了结论的绝对效度。

】
