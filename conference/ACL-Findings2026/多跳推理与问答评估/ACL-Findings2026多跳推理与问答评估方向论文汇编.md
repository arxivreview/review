# ACL-Findings2026 · 多跳推理与问答评估方向论文汇编

> 本方向共 15 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AgenticRAGTracer: A Hop-Aware Benchmark for Diagnosing Multi-Step Retrieval Reasoning in Agentic RAG ｜AgenticRAGTracer：面向智能体检索增强的多跳推理诊断基准

研究机构：北京科技大学、北京大学

作者：Qijie You、Wenkai Yu、Hao Liang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_01ea47c59e57)

> 多跳推理评估旨在检验大语言模型整合跨文档证据以推导复杂答案的能力，其核心价值在于突破单跳事实检索的饱和瓶颈。现有基准多基于静态“检索-阅读”范式，仅提供最终问答对与支持文档，无法捕捉智能体（Agent）在动态多步交互中的决策过程，导致“答案正确但推理错误”的捷径学习问题难以被诊断。本文提出 AgenticRAGTracer，一个通过自动流水线构建、支持逐跳（Hop-aware）验证的智能体检索增强生成（Retrieval-Augmented Generation, RAG）基准，旨在暴露模型在长链推理中的步骤分配缺陷。该基准填补了动态智能体评估的空白，但其对检索策略与推理链因果关系的量化仍停留在相关性层面，缺乏机制层面的解释。

】

---

【AlgBench: To What Extent Do Large Reasoning Models Understand Algorithms? ｜算法中心范式下的推理能力评估

研究机构：香港科技大学、北京理工大学

作者：Henan Sun、Kaichi Yu、Yuyao Wang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.04996)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.04996)

> 现有代码推理基准因题目混杂多算法且源自公开题库，导致无法区分模型是掌握了特定算法原理还是仅记忆了表面解题模式。AlgBench 通过专家原创构建 3000 道单算法隔离题目，从“问题中心”转向“算法中心”范式，以诊断大推理模型在复杂优化算法上的真实能力断层。该基准揭示了模型在全局优化任务上的显著性能衰减及“策略过度转移”现象，为算法推理评估提供了抗污染的新视角，但其单算法隔离设计是否过度简化了真实工程场景中的多算法协同需求，仍存疑。

】

---

【BloomEval: A Bloom’s Cognitive Taxonomy-Based Benchmark for Evaluating LRMs via Cognitive Hierarchy Trace ｜基于布卢姆认知分类学的推理轨迹评估

作者：Zhiyi Duan、Lei Gao、Jiangshan Guan 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_49851fc007ae)

> 多跳推理与数学解题评估长期依赖最终答案的精确匹配，导致模型通过捷径或结构断裂的推理得出正确答案时无法被识别。现有过程评估多聚焦于逻辑一致性或因果验证，缺乏对推理步骤认知层级结构的系统性诊断。本文提出认知层级轨迹（Cognitive Hierarchy Trace, CHT），将布卢姆认知分类学（Bloom's Cognitive Taxonomy, BCT）映射至推理步骤，构建大规模基准BloomEval以量化层级跳跃与断裂。该方法揭示了答案正确性与认知结构完整性之间的解耦，但受限于数学领域单一性及线性层级假设的普适性存疑。

】

---

【Breaking the Evaluation Paradox: Evaluating High-Entropy Search with Computationally Irreducible Constraints ｜高熵搜索评估悖论与计算不可约约束

作者：Juntao Wu、Wei Wen、Xianting Huang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a63e276d803a)

> 高熵搜索（High-Entropy Queries, HEQs）要求模型在开放网络空间中枚举大量候选项，但验证完整性所需的真值集在任务定义上不可获得，导致现有基准系统性惩罚超额正确项。现有基于人工标注答案池的评估范式无法解决这一悖论，本文切入点是通过引入计算不可约的哈希约束，将枚举任务转化为稀疏答案搜索。具体做法是利用密码学哈希函数构建可自动验证且语义不可优化的约束，使模型必须执行真实的遍历搜索。该范式在理论上证明了与全量枚举的计算等价性，但在实证中暴露出对前沿模型区分度不足及缺乏语义歧义性模拟的局限。

】

---

【CogBench: Benchmarking Cognitive Alignment of Large Language Models in Educational Question Answering ｜教育问答中的认知对齐基准

作者：Tong Lu、Zhichun Wang、Yuanhao Sun 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f0469b223ded)

> 教育场景下的大语言模型（LLM）常因解释抽象度固定，导致高阶解法对低龄学生不可理解，或低阶解法对高阶学生缺乏严谨性，这一现象称为认知失配。现有基准如 C-EVAL 和 CMMath 通过不同年级的题目区分难度，混淆了问题本身难度与解释适切性，无法隔离评估模型调整推理深度的能力。本文提出 CogBench，将 K-12 数学题重构为“一题多解”形式，利用课程知识图谱对齐解法与认知层级，并引入认知准确率、知识一致性与知识发散度指标。该基准揭示了模型在事实正确性与认知对齐间的权衡，但知识注入反而降低对齐度的反直觉结果暗示了预训练偏置的深层影响。

】

---

【Eval-RAR: Evaluation-Driven Retrieval-Augmented Reasoning via Reinforcement Learning ｜评估驱动检索增强推理

研究机构：中国科学技术大学

作者：Heng Yu、Rui Li、Qi Liu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_550f6f059639)

> 检索增强推理（Retrieval-Augmented Reasoning, RAR）旨在通过迭代检索解决复杂问答，但现有强化学习（RL）范式常陷入“盲搜”循环，即模型无法诊断信息缺口导致检索偏离。本文指出失效根源并非检索能力不足，而是缺乏对“信息不充分”的显式诊断。Eval-RAR 引入“搜索-评估”范式，通过显式自我评估步骤及对应的评估奖励，引导模型在检索后主动识别证据缺口。该方法在七个基准上优于基线，但评估奖励的泛化性及对长链推理的稳定性仍存疑。

】

---

【KnowledgeBerg: Evaluating Systematic Knowledge Coverage and Compositional Reasoning in Large Language Models ｜冰山缺口：有界全集覆盖与组合推理评估

研究机构：荷兰格罗宁根大学、荷兰莱顿大学

作者：Xiao Zhang、Qianru Meng、Yongjian Chen 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17621)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17621)

> 现有大语言模型基准多聚焦于孤立事实检索或线性单链推理，缺乏对“隐式有界全集系统性覆盖”能力的检验。主流多跳问答范式依赖离散文档链接，无法诊断模型在完整知识域上的组合运算缺陷。本文通过构建基于权威本体的有界全集基准，量化表面简单性与潜在复杂度差距，并诊断出完整性、意识与应用三阶段失效。该工作揭示了当前模型在结构化知识组织上的系统性盲区，但其对动态知识更新及检索策略的局限性仍存疑。

】

---

【MorphoBench: A Benchmark with Difficulty Adaptive to Model Reasoning ｜自适应难度推理基准

研究机构：北京大学、北京航空航天大学

作者：Xukai Wang、Xuanbo Liu、Mingrui Chen 等 19 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.14265)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.14265)

> 现有静态推理基准无法随模型能力进化而动态调整难度，导致评估失效。MORPHOBENCH 通过证明图形式化推理难度，并利用模型反馈动态修改题目条件或提示，实现了难度与模型能力的匹配。其价值在于提供了跨学科动态评估框架，但依赖 o3-mini 自动判分且未验证难度调节对逻辑完整性的影响，存疑。

】

---

【OMHBench: Benchmarking Balanced and Grounded Omni-Modal Multi-Hop Reasoning ｜全模态多跳推理基准：OMHBench

研究机构：韩国汉阳大学、索尼AI

作者：Seunghee Kim、Ingyu Bang、Seokgyu Jang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2508.16198)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f60af72fee23)

> 全模态大语言模型（MLLMs）在处理文本、视觉与语音联合输入时，常因评估基准存在模态捷径或推理路径偏斜而表现虚高。现有全模态理解（OMU）基准允许模型忽略部分模态作答，跨模态多跳推理（CMR）基准则排除语音且路径分布严重失衡，导致无法真实反映模型的跨模态整合能力。OMHBench 通过强制三模态联合接地与模态排列组合，构建了 6,144 道平衡多跳推理题，并引入路径平衡分数（PBS）量化模型对模态顺序的鲁棒性。该基准揭示了模型在语音模态接地上的系统性不对称，但受限于静态表格数据源，其结论在动态视频或实时音频场景下的普适性尚存疑。

】

---

【OpenExempt: A Diagnostic Benchmark for Legal Reasoning and a Framework for Creating Custom Benchmarks on Demand ｜法律破产豁免推理诊断基准

作者：Sergio Servantez、Sarah B. Lawsky、Rajiv Jain 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8de1f4ce7e26)

> 静态法律基准将复杂推理压缩为单一准确率指标，无法隔离模型在规则应用、时序判断或干扰抵抗上的具体失效点。现有方案依赖人工标注，成本高且难以动态调整难度，导致评估信号模糊。OpenExempt 利用符号化法律逻辑与分支定界求解器，按需生成可机器验证的动态任务，实现了对推理链条中阶段错误与传播错误的因果分解。该框架在 13 个模型上揭示了长链推理下的性能悬崖，但其符号化逻辑对真实法律模糊性的覆盖度仍存疑。

】

---

【PBEBench: A Multi-Step Programming by Examples Reasoning Benchmark inspired by Historical Linguistics ｜基于历史语言学的多步程序示例推理基准

作者：Atharva Naik、Darsh Agrawal、Prakam 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_366acb5deb19)

> 多步归纳推理评估长期受困于领域知识混杂与数据污染，导致模型性能无法真实反映其顺序逻辑整合能力。现有基准如 HotpotQA 依赖静态文本，难以隔离纯粹的推理机制，且易被预训练数据覆盖。本文切入点在于利用历史语言学中的音变顺序约束，构建一个无领域知识、可自动生成的字符串重写任务。通过符号系统生成受控难度的程序级联，量化模型在顺序依赖推理上的瓶颈。该基准揭示了当前前沿模型在长级联任务上的严重失效，但其在真实语言歧义处理上的泛化能力仍存疑。

】

---

【Progressive Planning and Reinforced Reasoning: Large Language Model-Guided Multi-hop Question Answering over Knowledge Graph ｜渐进式规划与强化推理：知识图谱多跳问答的LLM引导框架

研究机构：北京邮电大学

作者：Xiang Li、Runhai Jiao、Ruifan Li 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f4371fb70e97)

> 多跳问答要求模型在结构化知识中跨越多个实体链接推导答案，传统强化学习（RL）方法因缺乏中间步骤监督而陷入盲目探索，且策略网络仅关注局部邻域，无法预判决策的长期后果。本文切入点在于将大语言模型（LLM）从间接信号提供者升级为显式规划器，通过子问题分解引导逐步决策，并引入结构感知前瞻网络评估动作长期价值。具体做法是结合LLM宏观规划与RL微观推理，构建渐进式规划与强化推理（Progressive Planning and Reinforced Reasoning, PPRR）框架。该框架在四个公开基准上超越现有方法，但其依赖静态知识图谱且LLM规划仅用于训练，推理时的泛化能力与规划错误率仍是存疑点。

】

---

【SciVQR: A Multidisciplinary Multimodal Benchmark for Advanced Scientific Reasoning Evaluation ｜多学科多模态科学推理基准

研究机构：中国科学院、中国科学院大学

作者：Longteng Guo、Xuanxu Lin、Dongze Hao 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.10187)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.10187)

> 现有多模态大语言模型（MLLMs）在科学推理评估中面临学科覆盖窄、难度单一且缺乏过程可追溯性的困境，导致无法区分模型是依赖视觉感知还是真正的多步逻辑推导。本文通过构建覆盖6大领域54个子学科、包含专家解题轨迹的多模态基准SciVQR，填补了从基础事实到研究生级多跳推理的评估空白。该基准不仅评估最终答案，更通过五维指标诊断思维链（Chain-of-Thought, CoT）的忠实性。其价值在于提供了过程级评估的多模态参照系，但静态考试题源的数据污染风险及缺乏检索增强基线，限制了其对模型真实知识整合能力的全面诊断。

】

---

【SEARCH-R: Structured Entity-Aware Retrieval with Chain-of-Reasoning Navigator for Multi-hop Question Answering ｜结构化实体感知检索与推理导航的多跳问答框架

研究机构：香港城市大学、浙江大学

作者：FU Yuqing、Yimin Deng、Wanyu Wang 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_946baeb79164)

> 多跳问答（MHQA）的核心困境在于模型常因推理路径随机或检索信息同质化而得出错误答案。现有提示工程方法无法精确控制子问题分解质量，传统稠密检索则难以区分高相似度但低实用性的文档。本文通过训练端到端推理导航器与依赖树实体量化检索双模块，将分解过程从提示驱动转为策略优化。该框架在长链推理基准上表现优异，但其对短链标准基准的增益有限，且依赖特定句法工具，泛化边界尚待验证。

】

---

【SR-RAG: Verifiable Multi-Hop Reasoning via On-the-fly Symbolic Graph Construction ｜符号验证检索增强生成

作者：Zehua Wang、Zhaojin Zhang、Boyu Qiu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2d4deba1f41c)

> 多跳推理中，动态检索范式因缺乏中间步骤验证，导致错误在推理链中逐级累积，最终答案失效。现有聚合优先方法构建成本高且适应性差，动态优先方法则依赖大语言模型内部推理，易受幻觉与逻辑断裂影响。SR-RAG 通过即时构建查询特定知识图谱并引入外部符号验证器，将中间推理步骤转化为形式化逻辑蕴含检查，阻断错误传播。该方法在多个基准上提升了准确率与鲁棒性，但其高计算延迟与对结构化实体关系的强依赖，限制了其在纯文本无实体场景及长链复杂逻辑中的适用边界。

】
