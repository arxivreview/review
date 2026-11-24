# ACL-Findings2026 · 面向LLM智能体的长期记忆架构方向论文汇编

> 本方向共 16 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AMA: Adaptive Memory via Multi-Agent Collaboration ｜多智能体协作的自适应记忆框架

研究机构：香港科技大学、山东大学

作者：Weiquan Huang、Zixuan Wang、Hehai Lin 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.20352)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.20352)

> 长时程智能体交互面临的核心矛盾是存储粒度与检索需求之间的静态错配，以及缺乏显式一致性维护导致的逻辑矛盾累积。现有Agentic Memory系统虽引入LLM抽象，但普遍依赖固定分块或单一控制器，无法在推理时动态对齐任务复杂度，且更新机制粗糙导致冗余信息 unchecked 累积。本文提出AMA框架，通过解耦Constructor、Retriever、Judge、Refresher四个角色，实现多粒度存储、意图路由与逻辑审计的闭环。该设计在Token效率与知识更新准确率上表现优异，但其绝对性能仍低于最新结构化图谱基线，且多智能体协作带来的额外推理开销是否抵消了粒度适配收益，尚需更严格的效率-精度权衡验证。

】

---

【Beyond Dialogue Time: Temporal Semantic Memory for Personalized LLM Agents ｜语义时间锚定与持续记忆构建

研究机构：中国科学院、中国科学院大学

作者：Miao Su、Yucan Guo、Zhongni Hou 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.07468)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.07468)

> 长期对话智能体面临的核心困境是记忆的时间维度建模失效：现有系统普遍将“对话发生时间”等同于“事件发生时间”，且将连续经历切割为孤立点状记录，导致跨会话推理与时间敏感查询的召回严重失准。Temporal Semantic Memory (TSM) 通过构建语义时间线（Semantic Timeline）与持续记忆（Durative Memory）双轨架构，解耦了对话时间与事件时间，并将离散事实聚合为具有时间跨度的状态摘要。该方法在 LongMemEval 上实现了 74.80% 的整体准确率，但在 LoCoMo 基准上落后于结构化语义图方案，表明其优势局限于时间维度而非通用检索能力。

】

---

【BMAM: Brain-inspired Multi-Agent Memory Framework ｜脑启发式多智能体记忆框架

研究机构：日本东京科学大学、香港理工大学

作者：Yang Li、Jiaxiang Liu、Yusong Wang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_528dd5a5b1be)

> 长时程智能体在跨会话交互中面临记忆碎片化导致的时序错乱、事实矛盾与身份丢失，即“灵魂侵蚀”。现有检索增强生成（RAG）将记忆视为静态外部文本，缺乏内部演化机制，无法解决动态状态下的认知一致性。BMAM借鉴认知神经科学，将记忆解耦为海马体、颞叶等六个功能子系统，通过时间线索引与混合检索实现多尺度协同。该架构在LoCoMo上取得78.45%准确率，验证了模块化分工对缓解记忆退化的有效性，但其性能仍低于当前结构化图谱SOTA，且身份一致性评估依赖特定基准，泛化性存疑。

】

---

【From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents ｜从检索到遗忘：个性化智能体长期记忆基准

研究机构：美国亚利桑那州立大学、美国亚利桑那大学

作者：Md Nayem Uddin、Kumar Shubham、Eduardo Blanco 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.20006)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f499e22c429f)

> 长期记忆评估长期被简化为跨会话事实检索，掩盖了智能体在信息更新与废弃时的状态一致性缺陷。现有基准如LoCoMo和LongMemEval对记忆整合与突变施加的压力极低，导致模型在真实非平稳交互中的失效模式被隐藏。Memora通过构建周、月、季度尺度的高突变对话流，并引入遗忘感知记忆准确率（FAMA）指标，将记忆评估从“是否召回”转向“是否维持当前有效状态”。该基准揭示了现有记忆智能体在长时程下的脆弱性，但其评估协议对生成数据质量的依赖及基线覆盖的局限性，限制了结论的普适性。

】

---

【From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms ｜从存储到经验：LLM智能体记忆机制的演化框架

研究机构：香港浸会大学、香港科技大学

作者：Jinghao Luo、Yuchen Tian、Chuxue Cao 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.06716)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.06716)

> 大语言模型（LLM）智能体在长时程任务中因固有状态lessness导致逻辑断裂与重复错误，现有研究在操作系统工程与认知科学两条范式间割裂，缺乏统一的技术演化视角。本文提出“存储-反思-经验”（Storage-Reflection-Experience, SRE）三阶段演化框架，将记忆机制从被动记录重构为主动抽象的认知过程。该框架通过形式化定义各阶段的信息抽象层级，揭示了记忆从轨迹保真向策略先验转化的内在驱动逻辑。其价值在于提供了跨范式的理论整合视角，但作为定性综述，缺乏定量验证以证明经验阶段在特定任务上的实际增益。

】

---

【Grounding Agent Memory in Contextual Intent ｜基于上下文意图的智能体记忆系统

研究机构：美国伊利诺伊大学厄巴纳-香槟分校、美国斯坦福大学

作者：Ruozhen Yang、Yucheng Jiang、Yueqi Jiang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.10702)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.10702)

> 长时程智能体交互中，语义相似但上下文不同的信息极易导致检索混淆，现有记忆系统缺乏对潜在目标状态的显式建模。STITCH 通过在线诱导“上下文意图”三元组作为结构化检索线索，解决了这一干扰问题。其核心在于将记忆检索从语义相似度匹配升级为意图兼容性过滤。该方法在高干扰场景下显著优于基线，但其对强 LLM 骨干的依赖限制了轻量化部署，且未验证在通用事实召回任务上的泛化优势。

】

---

【Learning How to Remember: A Meta-Cognitive Management Method for Structured and Transferable Agent Memory ｜元认知记忆抽象

研究机构：中科院自动化所、中国科学院大学

作者：Sirui Liang、Pengfei Cao、Jian Zhao 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.07470)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.07470)

> 长时程具身智能体在分布偏移下复用历史经验时，常因记忆抽象层级固定而遭遇负迁移。现有检索或总结方法将记忆视为静态内容，无法自适应选择抽象粒度。MCMA将记忆抽象建模为可学习的元认知策略，通过独立训练的Memory Copilot决定记忆结构与层级。该方法在ALFWorld和ScienceWorld上显著提升了跨任务泛化能力，但其对DPO训练信号的依赖及单一文本模态的局限尚待检验。

】

---

【LiCoMemory: Lightweight and Cognitive Agentic Memory for Efficient Long-Term Reasoning ｜轻量级认知图记忆架构

作者：Zhengjun Huang、Zhoujin Tian、Qintian Guo 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2e2e1cb339ac)

> 长时程对话智能体受限于固定上下文窗口，导致跨会话状态丢失与推理断裂。现有图结构记忆方案虽能捕捉关系，但普遍存在语义与拓扑耦合导致的冗余存储、检索碎片化及更新延迟高企的问题，难以满足实时交互需求。LiCoMemory 提出 CogniGraph，将知识图谱重构为仅存储标识符的轻量级语义索引层，结合层级化检索与 Weibull 时序衰减重排序，实现了低延迟的实时记忆更新与高精度检索。该方案在效率-精度权衡上显著优于传统图记忆系统，但其绝对精度仍低于最新 SOTA，且未探索端到端策略优化路径。

】

---

【MemoBrain: Executive Memory as an Agentic Brain for Reasoning ｜执行记忆：作为推理智能体的协同大脑

研究机构：中国人民大学

作者：Hongjin Qian、Zhao Cao、Zheng Liu

论文原文见 [arXiv](https://arxiv.org/abs/2601.08079)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.08079)

> 工具增强智能体在长时程推理中因上下文窗口受限导致认知过载与任务对齐失效，现有跨任务持久记忆无法适应单任务内动态演化的推理结构。MemoBrain 提出“执行记忆”范式，将记忆从被动存储重构为主动控制机制，通过独立协同模型异步构建依赖感知记忆图并执行折叠与冲刷操作，在有界预算下维持推理连贯性。该方法在 BrowseComp-Plus 等基准上显著提升了基线智能体性能，但其仅限单任务生命周期且依赖独立模型部署，是否适用于跨会话经验复用尚存疑。

】

---

【Memory as Action: Autonomous Context Curation for Long-Horizon Agentic Tasks ｜记忆即动作：长时程智能体任务的自主上下文策展

研究机构：北京交通大学

作者：Yuxiang Zhang、Jiangming Shu、Ye Ma 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.12635)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.12635)

> 长时程智能体任务中，固定上下文窗口随交互累积导致注意力稀释与关键信号丢失，现有外部记忆管理模块因与推理策略解耦而无法联合优化信息保留与任务性能。MemAct 将工作记忆管理重构为策略空间内的可学习动作，通过端到端强化学习实现上下文编辑与任务执行的统一优化。该框架引入动态上下文策略优化算法解决非连续轨迹的训练不匹配问题，使14B模型在保持高准确率的同时将平均上下文长度压缩51%。其价值在于证明了记忆管理作为内生策略的可行性，但实验局限于单任务长时程场景，跨会话泛化能力未经验证。

】

---

【Memory Matters More: Event-Centric Memory as a Logic Map for Agent Searching and Reasoning ｜事件中心记忆作为逻辑地图

研究机构：中国人民大学

作者：Yuyang Hu、Jiongnan Liu、Jiejun Tan 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.04726)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.04726)

> 长时程智能体交互中，扁平化文本存储导致多跳推理与时间逻辑断裂，现有结构化方法虽引入图结构却仍依赖被动相似度检索。本文切入点在于将记忆从静态容器转化为引导推理的“逻辑地图”，通过事件分割与显式关系提取构建事件图，并设计主动多路径导航机制。该方法在LoCoMo和NarrativeQA上显著优于基线，但其绝对性能仍低于最新工业级系统，且高计算开销限制了实时部署。

】

---

【MemPO: Self-Memory Policy Optimization for Long-Horizon Agents ｜自记忆策略优化

研究机构：清华大学、阿里巴巴集团

作者：Ruoran Li、Xinghua Zhang、Haiyang Yu 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.00680)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.00680)

> 长时程智能体在ReAct范式下因上下文线性膨胀面临窗口截断、成本激增与“中间迷失”三重瓶颈，现有外部记忆模块因离线压缩与任务目标脱节，导致检索被动且无法联合优化。本文切入点在于将记忆管理内化为策略模型的内生动作，通过自记忆策略优化算法（Self-Memory Policy Optimization, MemPO）实现记忆、推理与工具调用的端到端协同。其核心机制是引入基于条件概率的记忆级奖励，解决长时程交互中的信用分配难题。该方案在单任务多跳推理中显著降低了Token消耗并提升了精度，但其缺乏跨会话持久化存储，在需要长期状态一致性的场景中有效性存疑。

】

---

【MemWeaver: Weaving Hybrid Memories for Traceable Long-Horizon Agentic Reasoning ｜记忆固化驱动的三层混合架构

作者：Juexiang Ye、Xue Li、Yang Xinyu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b52e4a4dda81)

> 长时程智能体交互面临的核心挑战是跨会话状态丢失与认知矛盾，现有基于向量检索或单一知识图谱的方法在时序一致性与证据可追溯性上存在结构性缺陷。MemWeaver 将记忆管理从被动存储重构为主动固化过程，通过整合时序知识图谱、经验抽象与原始段落证据的三层架构，解决多跳推理中的时间冲突与幻觉问题。该方法在 LoCoMo 基准上显著提升了时序与多跳任务的性能，同时大幅压缩了推理上下文长度，但其离线构建依赖高算力 LLM 的瓶颈限制了实时部署的可行性。

】

---

【Preference-Aware Memory Update for Long-Term LLM Agents ｜偏好感知记忆更新机制

作者：Haoran Sun、Zekun Zhang、Shaoning Zeng

论文原文见 [arXiv](https://arxiv.org/abs/2510.09720)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.09720)

> 长期对话智能体面临用户偏好随时间漂移导致的响应失配问题，现有记忆系统多聚焦于静态存储与检索，缺乏对动态偏好演化的实时追踪能力。PAMU通过滑动窗口与指数移动平均融合构建双视角偏好向量，以统计信号触发记忆更新，实现无微调的模块化适配。该方法在LoCoMo基准上提升了生成质量，但仅验证了风格一致性，未触及多跳推理或事实准确性SOTA，其统计建模对语义细粒度的捕捉能力存疑。

】

---

【RecMem: Recurrence-based Memory Consolidation for Efficient and Effective Long-Running LLM Agents ｜基于复现的记忆固化

研究机构：香港中文大学、北京邮电大学

作者：Zijie Dai、Shiyuan Deng、Sheng Guan 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.16045)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.16045)

> 长时程智能体面临固定上下文窗口导致的跨会话状态丢失，现有记忆系统通过每轮交互调用大语言模型进行事实提取，虽保真度高但构建成本极高。本文指出这种“急切固化”策略在低信息密度交互中是过度设计，提出基于复现的记忆固化机制，仅在检测到语义复现时触发高成本处理。该方法在保持准确率的同时大幅降低Token消耗，但其扁平化存储结构在复杂多跳推理任务上的表现仍存疑。

】

---

【TiMem: Temporal-Hierarchical Memory Consolidation for Long-Horizon Conversational Agents ｜时序层级记忆固化框架

研究机构：中科院自动化所

作者：Kai Li、Xuanqing Yu、Ziyi Ni 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.02845)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.02845)

> 长时程对话智能体面临的核心矛盾是交互历史无限增长与LLM有限上下文窗口的冲突，导致用户状态演化中的时间连贯性丢失与个性化表征不稳定。现有外部记忆系统多依赖语义相似度聚类，将时间结构降格为辅助元数据，致使不同时期的记忆在无明确边界下聚合，检索时缺乏时序排序，无法构建因果证据链。TiMem的切入点是将时间结构提升为一等组织原则，通过显式时间包含约束的层级树结构，将细粒度情景交互逐步固化为抽象人格画像。该框架在LoCoMo和LongMemEval-S上取得了优于对比基线的准确率，同时大幅降低了检索上下文长度，但其性能上限受限于指令提示的固化策略，且未与最新结构化SOTA方法直接对比。

】
