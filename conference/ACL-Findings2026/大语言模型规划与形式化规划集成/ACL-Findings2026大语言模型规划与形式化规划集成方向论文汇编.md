# ACL-Findings2026 · 大语言模型规划与形式化规划集成方向论文汇编

> 本方向共 9 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Bridging Reasoning and Action: Hybrid LLM–RL Framework for Efficient Cross-Domain Task-Oriented Dialogue ｜验证式LLM知识赋能强化学习

作者：Yangyang Zhao、Linfan Dai、Li Cai 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e73fb8b2ecea)

> 跨域任务导向对话（Task-Oriented Dialogue, TOD）的核心难点在于单一领域决策对其他领域施加的可行性约束，这些约束常隐含于常识或时间逻辑中，导致长程规划失效。现有方法要么依赖纯强化学习（RL）在状态缺失下盲目探索，要么直接使用大语言模型（LLM）生成动作却因幻觉和跨轮次漂移而不可靠。本文切入点是将约束建模重构为状态构建问题，通过双角色LLM交叉质询验证隐式约束，并将其接地为结构化槽值对以增强RL策略输入。该框架在MultiWOZ 2.1和Frames上显著提升了跨域泛化能力，但验证机制依赖LLM自身逻辑，存在循环论证风险。

】

---

【CARL: Constraint-Aware Reinforcement Learning for Planning with LLMs ｜约束感知强化学习

研究机构：浙江大学、香港城市大学

作者：Qiuyi Qi、Jinjian Zhang、Mutian Bao 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.04854)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.04854)

> 大语言模型在规划任务中常因忽略输入中的硬性限制而生成无效方案，现有方法多依赖外部符号求解器或任务分解来规避此缺陷，但未能提升模型内在的约束遵循能力。本文切入点在于将约束合规性转化为强化学习中的连续奖励信号，通过对比有约束与无约束输入下模型输出的分布差异来引导策略优化。具体做法是构建基于KL散度的约束感知奖励函数，兼容多种RL算法。该方法在TravelPlanner上取得56.1%的最终通过率，显著优于基线，但其效果是否源于对约束形式的过拟合而非语义理解，仍需更严格的跨域验证。

】

---

【From Coarse to Fine: Self-Adaptive Hierarchical Planning for LLM Agents ｜自适应层级规划

研究机构：中国人民大学

作者：Haoran Tan、Zeyu Zhang、Chen Ma 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.23194)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.23194)

> 现有 LLM 智能体规划器通常在固定粒度下生成计划，导致简单任务过度规划、复杂任务细节不足。本文切入点在于引入认知科学中的“渐进细化”理论，通过蒙特卡洛奖励评估动态选择最优层级，并采用两阶段训练优化层级选择与计划质量。该方法在 ALFWorld 和 ScienceWorld 上验证了自适应粒度对任务效率与成功率的提升，但其依赖单一骨干模型构建监督信号，跨模型泛化能力存在显著偏差。

】

---

【NITI: Neural Plan Concretization for Incremental Execution, Bridging and Trigger Inference from Underspecified Human Policies ｜神经计划具体化框架

作者：Ayan Banerjee、Shomrik Barua Banerjee、Sandeep Gupta

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_01214c2289d3)

> 安全关键领域的执行困境在于，人类策略往往故意省略前置条件与异常处理，而现有大语言模型（LLM）或强化学习（RL）范式无法在缺乏完整状态枚举和显式奖励的情况下可靠执行此类未指定策略。NITI 提出了一种神经符号框架，将 LLM 定位为执行时的“具体化器”而非自主规划器，通过验证器接地的增量执行、触发推断与神经桥接机制，在无需训练或微调的前提下实现长程任务的安全执行。该框架在魔方解法与胰岛素给药任务中显著优于基线，但其对符号提示结构的依赖及连续状态空间的泛化能力仍存疑。

】

---

【ParaCook: On Time-Efficient Planning for Multi-Agent Systems ｜具身多智能体时间高效规划基准

研究机构：上海交通大学、美国加州大学默塞德分校

作者：Shiqi Zhang、Xinbei Ma、Yunqing Xu 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.11608)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.11608)

> 长程具身任务中，任务完成不等于规划高效，现有基准仅评估正确性而忽略并行调度下的时间成本。ParaCook 通过简化烹饪场景的动作空间，将“最小化总完成时间”确立为核心指标，隔离了底层路径规划对高层调度能力的干扰。该基准揭示了当前大语言模型（LLM）在抽象调度推理上接近最优，但在具身执行映射上存在显著效率鸿沟。其价值在于填补了时间效率评估的空白，但缺乏符号验证机制使其在复杂逻辑约束下的鲁棒性存疑。

】

---

【Policy-Guided Stepwise Action Planning for Controllable LLM Reasoning ｜策略引导的高层动作规划

研究机构：中山大学、新加坡南洋理工大学

作者：Jianpeng Zhou、Qisheng Hu、Jiahai Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b7d8080eed5c)

> 现有基于高层动作的LLM推理方法常陷入结构冗余或动作序列坍缩，导致性能不及简单思维链。PG-HAP通过解耦轻量级规划器与冻结执行器，利用强化学习动态选择推理动作，解决了静态模板无法适应复杂推理路径的问题。该方法在数学与常识推理基准上实现了超越基线的准确率，并提供了可解释的推理轨迹。尽管在连续推导任务上略逊于思维链，但其可控性与效率优势为LLM推理提供了新的工程范式，其在更复杂多步逻辑任务中的泛化边界仍需进一步验证。

】

---

【SGA-MCTS: Decoupling Planning from Execution via Training-Free Atomic Experience Retrieval ｜状态-目标-动作原子检索框架

作者：Xin Xie、Dongyun Xue、Wuguannan Yao 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14712)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14712)

> 长程工具调用任务中，推理时搜索的高延迟与监督微调的泛化僵化构成核心矛盾。现有记忆代理依赖完整轨迹检索，在实体值或Schema微变时失效，无法复用底层因果逻辑。本文提出SGA-MCTS，通过离线蒙特卡洛树搜索挖掘并去词化为状态-目标-动作原子，在线以混合符号-语义检索作为软提示指导生成。该范式在工具调用基准上显著缩小了小模型与前沿模型的差距，但其缺乏形式化验证机制，在逻辑一致性保障上存在结构性缺口。

】

---

【TripTide: A Benchmark for Adaptive Travel Planning under Disruptions ｜扰动感知旅行规划基准

研究机构：印度理工学院

作者：Priyanshu Karmakar、Soumyabrata Chaudhuri、Shubhojit Mallick 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.21329)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.21329)

> 导读 大语言模型（Large Language Model, LLM）在旅行规划中常假设理想无扰动环境，导致生成的计划缺乏现实鲁棒性。现有基准如 TravelPlanner 和 TripCraft 仅评估静态约束满足，忽略了航班取消、天气突变等动态扰动对计划执行的影响。TripTide 通过引入扰动严重性等级与旅行者容忍度画像，构建首个动态扰动响应基准，并设计意图保留、响应性与适应性三维评估指标。该工作填补了 LLM 在动态环境规划评估上的空白，但缺乏符号验证机制，其逻辑可行性在长程任务中面临挑战。

】

---

【Unifying Inference-Time Planning Language Generation ｜统一推理时规划语言生成流水线

研究机构：美国宾夕法尼亚大学、美国西北大学

作者：Prabhu Prakash Kagitha、Bo Sun、Ishan Desai 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c72fc314f24f)

> 经典规划任务要求从自然语言描述生成可被符号求解器执行的 PDDL 模型，但 LLM 直接生成 PDDL 时极易出现语法或语义错误，导致计划失效。现有方法多采用单次生成加简单重试，缺乏对中间表示（IR）选择的系统性评估，且依赖闭源大模型，开源中小模型性能骤降。本文提出基于 IR 层级的统一框架，引入高资源、语法对齐的 PyPDDL 作为中间语言，通过多阶段推理时计算换取生成可靠性。该框架在开源 32B 模型上验证了 IR 与求解器反馈的关键作用，但未探索训练时优化与推理时优化的协同效应。

】
