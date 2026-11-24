# ICLR2026 · 奖励建模与RLHF优化方向论文汇编

> 本方向共 18 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【BaseReward: A Strong Baseline for Multimodal Reward Model ｜多模态奖励模型构建的系统性实证研究

研究机构：小米

作者：Yi-Fan Zhang、Haihua Yang、Huanyu Zhang 等 15 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.16127)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.16127)

> 多模态大语言模型（MLLMs）的对齐依赖奖励模型（RM）提供可优化的标量信号，但现有工业界方案各自为政，缺乏统一架构与数据策略的对照基准。本文通过解耦范式、头部结构、数据源与骨干网络等组件，系统验证了简单标量架构在多模态场景下的有效性。其价值在于提供了可复现的构建指南，但缺乏对视觉特征偏差的显式去偏机制，且在纯文本任务上表现弱于同规模纯语言模型。

】

---

【Chasing the Tail: Effective Rubric-based Reward Modeling for Large Language Model Post-Training ｜追逐高奖励尾部：基于量表的LLM后训练奖励建模

研究机构：美国加州大学洛杉矶分校、美国芝加哥大学

作者：Junkai Zhang、Zihao Wang、Lin Gui 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.21500)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.21500)

> 强化微调（Reinforcement Fine-Tuning, RFT）中，策略模型常通过利用奖励模型的缺陷获取高分，导致真实质量下降，即奖励过优化。现有标量奖励模型难以区分“极好”与“优秀”响应，且离策略数据易引入表面特征偏差。本文指出高奖励区域的误指定是过优化的主因，并提出通过差异化精炼量表（Refinement-through-Differentiation, RTD）来聚焦该区域。该方法在医疗与金融领域显著提升了胜率并延缓了性能衰减，但其对离策略数据分布偏移的鲁棒性仍存疑。

】

---

【Critique-RL: Training Language Models for Critiquing through Two-Stage Reinforcement Learning ｜两阶段强化学习训练批评模型

研究机构：复旦大学

作者：Zhiheng Xi、Jixuan Huang、Xin Guo 等 18 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.24320)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.24320)

> 可规模监督（Scalable Oversight）旨在解决复杂推理任务中人类难以直接提供可靠标注的问题，核心在于训练能评估并反馈模型输出的批评模型。现有方法依赖强监督标注或测试时外部验证器，导致成本高昂或无法独立判别响应质量。本文提出 Critique-RL，通过两阶段强化学习解耦批评模型的判别性与有用性，无需强监督即可在线优化。该方法在数学推理任务上显著提升了 Actor 的修正准确率，但依赖训练时的 Oracle 验证器，限制了其在无验证器开放域任务中的直接适用性。

】

---

【Dun Yuan ｜策略收缩感知近端策略优化

研究机构：加拿大麦吉尔大学、加拿大康考迪亚大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_72198057)

> 强化学习从人类反馈（RLHF）中的近端策略优化（PPO）常导致模型输出多样性下降，即策略支持集在训练过程中逐渐收窄。现有方法将熵和KL散度作为固定权重的辅助惩罚项，无法在奖励提升的同时维持分布广度。本文提出CaPPO，将奖励、熵和KL散度视为平等目标，通过最小范数多梯度下降求解帕累托改进方向，并引入熵调度控制器动态调节探索压力。该方法在保持或提升对齐性能的同时恢复支持集保留率，但仅在对话与摘要任务上验证，未覆盖长链推理场景。

】

---

【Efficient Adversarial Attacks on High-dimensional Offline Bandits ｜离线多臂老虎机评估的对抗鲁棒性

研究机构：伊朗谢里夫理工大学

作者：Seyed Mohammad Hadi Hosseini、Amir Najafi、Mahdieh Soleymani Baghshah

论文原文见 [arXiv](https://arxiv.org/abs/2602.01658)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.01658)

> 离线多臂老虎机（MAB）评估旨在通过复用固定日志数据高效筛选最优生成模型，但公开共享的奖励模型权重使其面临被恶意篡改的风险。现有鲁棒MAB算法仅防御训练过程中的实时奖励污染，无法应对训练前对模型权重的静态扰动。本文通过构建高维凸优化攻击框架，证明微小权重扰动即可劫持算法行为。该研究揭示了评估基础设施的安全盲区，但防御机制仍不彻底，且理论保证依赖高维假设。

】

---

【Eliminating Inductive Bias in Reward Models with Information-Theoretic Guidance ｜基于信息论的奖励模型去偏

研究机构：香港中文大学

作者：Zhuo Li、Pengyu Cheng、Zhechao Yu 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.23461)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.23461)

> 奖励模型（RM）在强化学习从人类反馈（RLHF）中常因训练数据中的长度、格式等归纳偏置而失效，导致策略模型进行奖励黑客。现有去偏方法多依赖线性相关或单一偏差假设，难以处理非线性及多偏差并发场景。本文提出DIR框架，通过最大化RM与真实偏好的互信息并最小化其与偏差属性的互信息，实现通用去偏。该方法在鲁棒性上表现优异，但在通用基准绝对精度上未超越最新SOTA，且对连续型偏差的处理能力存疑。

】

---

【From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism ｜从好奇到谨慎：基于悲观估计的Best-of-N奖励黑客缓解

研究机构：美国卡内基梅隆大学、美国哥伦比亚大学

作者：Zhuohao Yu、Zhiwei Steven Wu、Adam Block

论文原文见 [arXiv](https://arxiv.org/abs/2604.04648)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.04648)

> 推理时扩展（Inference-time Scaling）旨在通过增加采样数量提升大语言模型（LLM）性能，但Best-of-N（BoN）采样常因奖励模型（RM）对分布外（OOD）响应的虚假高分导致性能随N增加而下降。现有方案或依赖更复杂的RM训练，或采用过于保守的分布正则化，无法兼顾鲁棒性与计算收益。本文提出Caution机制，将强化学习中的悲观原则迁移至推理时，通过预测误差惩罚OOD响应。该方法在GSM8K上将N=512时的准确率从71.5%提升至81.1%，但仅在标量RM场景下验证，未探索生成式RM的内在鲁棒性。

】

---

【How Reinforcement Learning After Next-Token Prediction Facilitates Learning ｜强化学习后训练对自回归模型泛化与推理长度的理论解释

研究机构：美国纽约大学、美国哈佛大学

作者：Nikolaos Tsilivis、Eran Malach、Karen Ullrich 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.11495)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.11495)

> 导读 大语言模型在数学与逻辑推理任务中展现出显著的能力跃升，这一现象通常归因于“预训练+强化学习（Reinforcement Learning, RL）”的两阶段训练范式。然而，现有研究多聚焦于奖励模型构建与偏好对齐，缺乏对RL如何从含噪或稀疏数据中提取有效梯度、并驱动模型生成更长推理链的底层优化机制的理论解释。本文通过构建长短序列混合的奇偶校验合成任务，证明当长链推理数据稀缺时，纯自回归预训练受限于样本复杂度壁垒，而RL通过放大稀有长序列的梯度信号，以极低的样本开销实现泛化，并伴随生成长度的必然增加。该工作为理解RL在推理任务中的增益机制提供了严格的理论边界，但其结论在真实噪声奖励与复杂语义任务中的普适性仍需进一步验证。

】

---

【LEARNING ORDINAL PROBABILISTIC REWARD FROM PREFERENCES ｜序数概率奖励模型

研究机构：中国科学院、中国科学院大学

作者：Longze Chen、Lu Wang、Renke Shan 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_60522592)

> 奖励模型在强化学习从人类反馈（RLHF）中充当策略优化的代理信号，但传统判别式模型输出的标量分数仅反映相对偏好，缺乏绝对质量锚定，导致无法建立可信的接受阈值。生成式模型虽提供解释性，却依赖高成本的点式监督且输入格式僵化。本文提出序数概率奖励模型（OPRM），将奖励建模重构为学习质量分数的完整概率分布，并通过区域淹没调优（RgFT）将分布校准至绝对质量区间。该方法在多个基准上超越现有标量模型，但其对标注质量的依赖及在复杂推理任务中的泛化能力仍存疑。

】

---

【mR3: Multilingual Rubric-Agnostic Reward Reasoning Models ｜多语言评分标准无关奖励推理模型

研究机构：美国斯坦福大学、加拿大多伦多大学

作者：David Anugraha、Shou-Yi Hung、Zilu Tang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.01146)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.01146)

> 多语言大语言模型评估长期受限于英语中心主义，现有奖励模型在非英语场景下性能显著退化，且缺乏对低资源语言推理能力的系统性研究。本文切入点在于构建覆盖72种语言的评分标准无关（Rubric-Agnostic）奖励推理模型，通过多语言蒸馏与课程学习策略解决跨语言泛化难题。MR3采用监督微调（SFT）训练，在保持小参数量（4B-14B）的同时，性能超越9倍规模的GPT-OSS-120B。其价值在于验证了目标语言推理在低资源场景下的有效性，但SFT优于强化学习验证奖励（RLVR）的结论在更大规模模型上是否成立仍存疑。

】

---

【OPPO: Accelerating PPO-based RLHF via Pipeline Overlap ｜重叠执行加速近端策略优化

研究机构：美国卡内基梅隆大学

作者：Kaizhuo Yan、Yingjie Yu、Yifan Yu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.25762)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.25762)

> 基于人类反馈的强化学习（RLHF）训练管线因多模型串行依赖与长尾响应延迟导致GPU利用率低下，现有算法级简化或系统级并行方案未能消除阶段间的空闲时间。本文切入点在于重构PPO执行时序，通过流式令牌传输与跨步超额承诺实现计算重叠。具体做法是引入步内重叠与步间重叠机制，在不改变PPO收敛性的前提下最大化硬件吞吐。该框架在保持最终模型质量的同时实现了显著加速，但其对动态超参数收敛性的理论保证仍显薄弱。

】

---

【P-GENRM: PERSONALIZED GENERATIVE REWARD - - MODEL WITH TEST TIME USER BASED SCALING ｜个性化生成式奖励模型与测试时用户缩放

研究机构：华东师范大学、阿里巴巴集团

作者：Pinyi Zhang、Ting-En Lin、Yuchuan Wu 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_97051753)

> 个性化对齐旨在让大语言模型适应个体用户偏好，但现有方法常将动态偏好固化为静态规则，且难以泛化至反馈稀疏的新用户。P-GenRM 通过生成包含用户画像与评分标准的结构化评估链，并引入基于用户原型的测试时双粒度缩放机制，解决了偏好推断噪声与冷启动问题。该方法在个性化基准上刷新了最佳成绩，但其计算开销与原型聚类的稳定性仍需进一步审视。

】

---

【REPRESENTATION-BASED EXPLORATION FOR LANGUAGE MODELS: FROM TEST-TIME TO POST-TRAINING ｜基于表示的探索机制

研究机构：美国普林斯顿大学、微软研究院

作者：Jens Tuyls、Dylan Foster、Akshay Krishnamurthy 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_98244695)

> 当前大语言模型（LLM）的强化学习后训练往往陷入“锐化”陷阱，即仅放大基础模型已有的低概率行为，而非发现新能力。现有数据策展与算法干预在开放域任务中面临数据规模瓶颈，难以有效激发新颖行为。本文提出基于预训练模型隐藏状态的椭圆奖励机制，在推理时选择与后训练两个阶段引导模型探索多样化行为。该机制显著提升了验证器效率与测试时样本效率，但其在无验证器场景下的泛化能力仍存疑。

】

---

【Representation-Based Exploration for Language Models: From Test-Time to Post-Training ｜基于表示的探索：突破语言模型强化学习的锐化瓶颈

研究机构：美国普林斯顿大学、微软研究院

作者：Jens Tuyls、Dylan J. Foster、Akshay Krishnamurthy 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.11686)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.11686)

> 强化学习后训练旨在提升大语言模型在数学与代码等可验证任务上的推理能力，但现有方法往往仅放大基座模型已有的低概率行为，而非发现新能力。这种“锐化”效应源于标准算法缺乏对行为多样性的显式激励，导致模型在复杂开放域中陷入局部最优。本文提出RepExp，利用预训练模型隐状态构建椭圆奖励，在推理时选择与后训练阶段同时注入多样性信号。该方法在AIME 2024上将样本效率提升3.2至13.4倍，但仅适用于有验证器的任务，其在无验证器场景下的泛化能力存疑。

】

---

【Reward Model Routing in Alignment ｜奖励模型路由中的贝叶斯自适应选择

研究机构：新加坡国立大学

作者：Xinle Wu、Yao Lu

论文原文见 [arXiv](https://arxiv.org/abs/2510.02850)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.02850)

> 在基于人类反馈的强化学习（RLHF）中，单一奖励模型（RM）难以兼顾不同任务域的偏好差异，且易因过拟合特定偏差导致策略模型“奖励黑客”。现有集成方法计算成本过高，而早期路由方法LASER存在冷启动慢与探索不足的问题。本文提出BayesianRouter，通过离线多任务学习构建RM能力先验，并结合在线贝叶斯汤普森采样实现查询级动态路由。该方法在指令遵循与推理基准上显著优于单RM及集成基线，但其收益是否完全源于算法本身而非RM池的多样性，仍需进一步剥离验证。

】

---

【REWARDBENCH 2: ADVANCING REWARD MODEL EVALUATION ｜奖励模型评估基准的区分度与下游相关性

研究机构：美国华盛顿大学、Cohere

作者：Saumya Malik、Valentina Pyatkin、Sander Land 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_82054036)

> 现有奖励模型（RM）评估基准在高分区间趋于饱和，且分数与下游强化学习（RLHF）或推理时采样（Best-of-N, BoN）性能缺乏稳定映射，导致开发者难以依据基准分数选择适配的RM。本文通过引入未见过的真实人类提示、将评估协议从1对1扩展为1对3（Best-of-4），并新增“平局”（Ties）域，构建了更具区分度的REWARDBENCH 2。该基准显著降低了头部模型的得分，并验证了其与BoN性能的强相关性，但揭示了RLHF中RM选择受模型谱系制约的复杂边界。

】

---

【Semantic-aware Wasserstein Policy Regularization for Large Language Model Alignment ｜语义感知Wasserstein策略正则化

研究机构：韩国科学技术院

作者：Byeonghu Na、Hyungho Na、Yeongmin Kim 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.01685)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.01685)

> 大语言模型对齐中的策略优化长期依赖KL散度约束，但该度量仅比较相同索引处的Token概率，忽略了Token间的语义关联，导致策略在支持集不匹配时数值不稳定且输出多样性受限。本文切入点在于引入熵正则化Wasserstein距离，通过最优传输对偶变量将语义几何信息转化为Token级奖励惩罚。该方法在摘要与对话生成任务上显著优于KL及多种f-散度基线，但其计算开销随词表规模增长，且在缺乏显式奖励模型去偏机制的情况下，其鲁棒性边界尚待验证。

】

---

【Unifying Stable Optimization and Reference Regularization in RLHF ｜双KL正则化统一稳定优化与参考约束

研究机构：澳大利亚悉尼大学、澳大利亚新南威尔士大学

作者：Li He、Qiang Qu、He Zhao 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.11523)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.11523)

> 强化学习从人类反馈（Reinforcement Learning from Human Feedback, RLHF）旨在通过奖励信号对齐大语言模型（Large Language Models, LLMs）与人类偏好，但策略优化常陷入奖励黑客与训练不稳定的双重困境。现有方法将防止奖励黑客的参考正则化与保证稳定更新的策略裁剪独立施加，导致优化空间被过度压缩，无法探索高奖励区域。本文提出双KL对齐目标，将两种正则化统一为对动态插值参考策略的约束，并推导为加权监督微调（Weighted Supervised Fine-Tuning, SFT）损失。该算法在多个基准上显著优于主流在线强化学习基线，但其对在线数据收集的依赖限制了离线场景的适用性。

】
