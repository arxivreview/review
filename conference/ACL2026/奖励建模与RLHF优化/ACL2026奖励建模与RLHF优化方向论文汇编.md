# ACL2026 · 奖励建模与RLHF优化方向论文汇编

> 本方向共 14 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Comprehensive Survey of Process Reward Models: Data Generation, Model Construction, and Usage ｜过程奖励模型综述：从结果信号到过程监督的闭环构建

作者：Congmin Zheng、Jiachen Zhu、Zhuoying Ou 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e07e657bb9ed)

> 长链推理中仅依赖最终答案的奖励信号过于稀疏，导致策略模型无法定位中间步骤错误，现有方案或依赖高成本人工标注，或受限于静态评估无法动态引导搜索。本文切入点在于将过程奖励模型（Process Reward Model, PRM）视为一个“数据生成-模型构建-应用迭代”的闭环系统，而非单向评估器。通过系统梳理判别式、生成式与隐式PRM的构建范式及其在测试时扩展与强化学习中的应用，本文揭示了PRM作为推理动态控制器的潜力。其价值在于提供了全景式的方法论地图，但缺乏对闭环迭代中误差累积机制的定量分析。

】

---

【AdaJudge: Adaptive Multi-Perspective Judging for Reward Modeling ｜自适应多视角评判框架

研究机构：美国埃默里大学、香港中文大学

作者：Yongliang Miao、Yangyang Liang、Mengnan Du

论文原文见 [arXiv](https://arxiv.org/abs/2601.08097)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.08097)

> 奖励模型（Reward Model, RM）旨在将人类偏好转化为标量信号以指导大语言模型对齐，但主流架构依赖固定池化策略压缩序列表示，导致数学推理等局部信号任务与安全对齐等全局信号任务间产生结构性冲突。现有方案通过数据清洗或骨干扩容提升性能，却忽视了评分头部的归纳偏置与任务证据分布的错配。本文提出 AdaJudge，通过深度门控精炼表示与域感知混合池化动态适配不同任务粒度。该框架在 JudgeBench 上超越强基线，但在 RM-Bench 上仍受限于训练数据规模，其架构改进能否完全弥补数据差距尚存疑。

】

---

【Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward Modeling ｜工具增强智能体轨迹级奖励建模基准

研究机构：南京大学、阿里巴巴集团

作者：Jiaxuan Wang、Yulan Hu、Wenjin Yang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.08178)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.08178)

> 随着大语言模型从单轮对话演进为具备工具调用能力的智能体，其输出从单一响应变为包含推理、执行与环境反馈的长程轨迹，传统基于短文本响应的奖励模型（Reward Model, RM）评估体系无法覆盖这种动态复杂性。现有基准多聚焦于原子动作正确性或静态文本偏好，缺乏对多轮规划逻辑与错误恢复能力的系统性测试。本文构建了Plan-RewardBench，通过多源扰动生成硬负例，在统一成对协议下评估判别式、生成式RM及LLM-as-Judge在轨迹级偏好判断上的表现。该基准揭示了现有评估器在长程轨迹上的严重性能退化，为智能体强化学习提供了必要的诊断工具，但其标签主观性与非均匀分布限制了结论的普适性。

】

---

【C2: Scalable Rubric-Augmented Reward Modeling from Binary Preferences ｜合作与批判的奖励建模

研究机构：日本国立情报学研究所、日本东京大学

作者：Akira Kawabata、Saku Sugawara

论文原文见 [arXiv](https://arxiv.org/abs/2604.13618)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.13618)

> 奖励模型在评估标准隐式的开放域任务中，常因依赖单一标量分数而陷入对表面特征的过拟合，导致判断鲁棒性不足。现有基于评分量表（Rubric）的验证方法虽能提升细粒度评估能力，但严重依赖昂贵的人工或大模型标注，且自生成量表质量参差不齐，低质量量表甚至会主动误导验证器。本文切入点在于揭示量表生成与验证之间的“合作失败”现象，并提出C2框架，通过从二元偏好中自举合成对比量表对，联合训练合作型生成器与批判型验证器。该框架在8B参数规模下实现了超越4倍参数量外部量表方法的性能，但其训练阶段依赖大规模候选采样，计算开销与推理效率的平衡仍是存疑点。

】

---

【ConsistRM: Improving Generative Reward Models via Consistency-Aware Self-Training ｜一致性感知自训练生成式奖励模型

作者：Yu Liang、Liangxin Liu、Longzheng Wang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.07484)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07484)

> 生成式奖励模型（Generative Reward Model, GRM）旨在通过自然语言批评替代标量分数以提升对齐可解释性，但其训练高度依赖昂贵的人工标注，而现有无监督自训练方法因伪标签噪声极易引发奖励黑客。本文切入点在于利用模型内部的时间序列一致性与语义一致性作为监督信号，构建无需人工反馈的稳定自训练框架。ConsistRM通过结合答案偏好一致性与批评语义一致性奖励，在五个基准上平均提升1.5%。该方法在无人工标注约束下实现了性能与鲁棒性的平衡，但其对早期噪声标签的累积效应及跨骨干泛化边界仍需进一步验证。

】

---

【DARM: Distribution-Aware Reward Modeling by Alleviating Biases from Low Preference-Context Dependency Data ｜分布感知奖励建模

研究机构：复旦大学、清华大学

作者：Shaofan Liu、Guoqiang Zhang、Shihan Dou 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9d4b7de736bc)

> 奖励模型在训练数据中存在大量“响应质量与上下文无关”的样本，导致模型学会忽略提示词、仅依赖响应表面特征进行打分，进而在分布外场景下失效。现有去偏方法如信息瓶颈或注意力正则化均采取全局约束，无法区分“需要上下文”与“无需上下文”的样本，导致在低依赖样本上引入虚假梯度或在高依赖样本上约束不足。本文提出分布感知奖励建模（Distribution-Aware Reward Modeling, DARM），通过引入条件互信息正则化项，利用对比学习强制模型在给定响应下保留对上下文的敏感性。该方法在分布外基准上平均准确率提升1.56%，优于现有去偏基线，但其效果依赖于负样本构造的质量，且在单轮短文本场景下的增益幅度未充分验证。

】

---

【Debiasing Reward Models via Causally Motivated Inference-Time Intervention ｜基于因果中介分析的奖励模型推理时去偏

作者：Kazutoshi Shinoda、Kosuke Nishida、Kyosuke Nishida

论文原文见 [arXiv](https://arxiv.org/abs/2604.27495)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.27495)

> 奖励模型（RM）在基于人类反馈的强化学习（RLHF）中常因长度、格式等虚假特征产生偏差，导致策略模型通过“奖励黑客”获取高分而非提升真实质量。现有去偏方法多依赖训练时正则化或仅针对单一长度偏差的推理时惩罚，难以兼顾多类型偏差消除与性能保持。本文提出CIRM，通过定位并替换与偏差强相关的神经元激活值，在推理时实现多偏差联合抑制。该方法以极低的计算成本使小模型RM的对齐效果逼近70B SOTA模型，但其对未知偏差类型的泛化能力及因果图假设的适用边界尚存疑。

】

---

【DUAL RM: Beyond Rule-based Preference Reward Modeling via Meta-Reward ｜双模奖励模型：基于元奖励的递归验证解耦

作者：Xiaobo Liang、Wanfu Wang、Qipeng Huang 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_df87d008a2e1)

> 奖励模型（Reward Model, RM）在强化学习对齐中面临“验证器需要验证器”的递归依赖困境，即Matryoshka Doll Problem，导致对人工标注的持续高成本依赖。现有生成式奖励模型（Generative Reward Model, GenRM）虽提供可解释性，但缺乏对推理轨迹有效性的客观度量，而判别式奖励模型（Discriminative Reward Model, DisRM）虽评分精准却缺乏推理深度。本文提出DUAL RM，通过耦合GenRM的推理预测与DisRM的观测评分构建非参数化元奖励，实现无外部监督的自校准。该方法在8B参数规模下显著提升了偏好判断准确率，但其性能上限受制于固定DisRM的偏差传递，且跨模态迁移的鲁棒性边界尚待明确。

】

---

【Efficient Hyperparameter Optimization for LLM Reinforcement Learning ｜联合保真度超参数优化

研究机构：香港科技大学

作者：Minping Chen、Bowen Xiao、Du Liang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.03073)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.03073)

> 大语言模型强化学习训练对超参数极度敏感，微小变动即可导致性能剧烈波动，但现有超参数优化方法因单次训练成本过高而在该场景下效率低下。本文切入点在于将模型规模与训练预算联合作为保真度维度，通过小代理模型加速搜索。具体做法是构建一个基于高斯过程贝叶斯优化的框架，结合检查点复用与动态早停策略。该方法在48小时预算内实现了最高14.9倍的单次试验加速，但其在复杂推理任务上的泛化边界及代理模型相关性假设的普适性仍需进一步验证。

】

---

【OpenRubrics: Towards Scalable Synthetic Rubric Generation for Reward Modeling and LLM Alignment ｜基于对比生成与一致性过滤的评分量表奖励建模

作者：Tianci Liu、Ran Xu、Tony Yu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2273f7068f53)

> 导读 在长文本问答与通用帮助性等主观领域，二元可验证奖励无法捕捉人类偏好的多维性，而传统标量奖励模型又缺乏对具体质量维度的显式解释，导致策略优化易陷入长度偏差等虚假相关。现有评分量表（Rubric）方法多依赖前沿大模型直接提示生成，成本高且质量不可控，难以规模化。本文提出OpenRubrics框架，通过对比式量表生成（CRG）与偏好-标签一致性过滤，训练小模型自动生成判别性量表，并构建基于量表的奖励模型（RUBRIC-RM）。该方法在多个基准上较同规模基线平均提升8.4%，但在绝对性能上仍落后于大规模SOTA奖励模型，其增益是否主要源于数据规模而非CRG机制本身尚存疑。

】

---

【PaTaRM: Bridging Pairwise and Pointwise Signals via Preference-Aware Task-Adaptive Reward Modeling ｜偏好感知任务自适应奖励模型

研究机构：北京邮电大学、美团

作者：Ai Jian、Jingqing Ruan、Xing Ma 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.24235)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.24235)

> 生成式奖励模型（GRM）旨在通过自然语言理由替代标量分数，以解决传统模型在开放式任务中缺乏可解释性及易过拟合的问题。然而，现有GRM范式存在根本性矛盾：成对方法无法处理单实例评估，而点式方法依赖昂贵的绝对评分标签。PaTaRM通过偏好感知奖励机制，利用成对数据直接训练点式GRM，并引入动态评分量表实现实例特异性评估。该框架在匹配数据条件下显著提升了下游强化学习策略的泛化能力，但其对静态基准准确率的牺牲是否值得，仍需更多跨域验证。

】

---

【ReflectRM: Boosting Generative Reward Models via Self-Reflection within a Unified Judgment Framework ｜统一判断框架下的生成式奖励模型自我反思

研究机构：清华大学

作者：Kai Qin、Liangxin Liu、Yu Liang 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.07506)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07506)

> 生成式奖励模型（Generative Reward Model, GRM）旨在通过输出文本分析与偏好标签来替代传统标量奖励，以解决开放式任务中单一分数无法捕捉多维质量权衡的问题。然而，现有GRM主要依赖结果级监督，忽略了分析推理过程的质量，导致模型在复杂判断中缺乏自我纠错能力，且易受位置偏差影响。本文提出ReflectRM，将响应偏好与分析偏好统一为单一生成任务，通过构建“反思数据”实现过程级监督，并在推理阶段利用自我反思筛选可靠输出。该方法在小模型上显著提升了基准测试准确率并大幅缓解了位置偏差，但其对初始模型生成质量的依赖及反思数据构建的潜在偏差风险仍存疑。

】

---

【Triviality Corrected Endogenous Reward ｜平凡性修正内生奖励

作者：Xinda Wang、Zhengxu Hou、Yangshijie Zhang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0228d35fcfab)

> 开放式文本生成缺乏客观验证标准，导致强化微调（RFT）长期依赖昂贵的外部裁判模型或人工标注偏好数据。现有基于置信度的内生奖励方法在数学推理中有效，但直接迁移至写作任务时，策略会坍缩至高概率、低多样性的模板化输出。本文通过引入通用策略与专家策略的信息增益分解，并施加概率依赖的门控修正，构建了无需外部监督的奖励信号。该方案在多个写作基准上实现了无外部依赖的性能提升，但其对长文本累积误差及跨域泛化边界的验证仍显不足。

】

---

【WildReward: Learning Reward Models from In-the-Wild Human Interactions ｜野外交互奖励建模

研究机构：清华大学、智谱AI

作者：Hao Peng、Yunjia Qi、Xiaozhi Wang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.08829)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.08829)

> 奖励模型（Reward Model, RM）训练长期依赖大规模人工标注偏好对，成本高且难以扩展。现有去偏方法聚焦于算法层面的因果解耦，却忽视了真实用户交互中已存在的天然质量信号。本文切入点在于直接从野外交互（in-the-wild interactions）中提取隐含反馈，构建无需偏好对的高质量训练集。通过有序回归训练标量RM，在通用基准上超越70B参数基线，但其在开放式任务中的泛化边界及噪声鲁棒性仍存疑。

】
