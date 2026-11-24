# ACL-Findings2026 · 文本到SQL生成方向论文汇编

> 本方向共 13 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Bidirectional Semantic Enhancement for Schema Routing Across Large-Scale Databases ｜双向语义路由

作者：Yuyang Wu、Xiaoliang Wang、Cam-Tu Nguyen

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0ebc0b5ce2d2)

> 大规模数据库场景下，用户查询与模糊表结构间的语义鸿沟导致传统检索失效，现有单向扩展或图遍历方法难以兼顾召回率与计算效率。Bi-SR 通过离线丰富表结构语义与在线推理查询意图的双向对齐策略，构建共享语义空间以解决这一瓶颈。该方法利用双增强对比训练目标优化稠密检索器，使其模仿大语言模型的语义扩展模式。尽管在噪声环境下展现出鲁棒性，但其对大模型推理能力的依赖及小模型适配性仍存疑。

】

---

【CORES: Code-Oriented Reasoning for Complex Text-to-SQL and Generalizable TableQA ｜代码导向推理的SQL生成与表格问答泛化

研究机构：国防科技大学、北京大学

作者：Meng Zhang、Ruochun Jin、Yuanxi Peng 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_de89c16574d8)

> 文本到SQL（Text-to-SQL）旨在将自然语言映射为可执行查询，但现有SQL微调模型在处理复杂逻辑时缺乏显式推理过程，且在表格问答（TableQA）任务上出现灾难性遗忘。本文指出SQL的声明式本质无法承载程序化逻辑，且单一任务微调导致通用代码能力丧失。CORES模型利用Python作为程序化推理枢纽，结合组相对策略优化（GRPO）与过程奖励函数进行训练，在提升复杂SQL生成准确率的同时，恢复了模型对TableQA的泛化能力。该框架在平衡领域特异性与通用推理能力上提供了新路径，但其性能上限仍受限于骨干模型规模与推理延迟。

】

---

【EXPO-SQL: Execution-based Clause-level Policy Optimization for Text-to-SQL ｜执行反馈的子句级信用分配：EXPO-SQL

研究机构：韩国成均馆大学

作者：Jaehoon Lee、CheolWon Na、Suyoung Bae 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_68ec44f7fa34)

> 文本到SQL任务中，强化学习（RL）方法长期依赖查询级二元奖励，导致模型无法区分SQL中正确与错误的子句，产生粗糙的信用分配。现有方案在复杂查询上因惩罚正确部分而收敛缓慢，本文切入点在于利用SQL逻辑执行顺序与差异类型分析，将奖励细化至子句粒度。通过增量执行定位错误子句并设计差异化奖励，EXPO-SQL在BIRD基准上超越最佳RL基线2.4个百分点。该方法验证了细粒度监督对复杂推理的有效性，但其依赖执行环境稳定性的假设在模糊问题场景下是否依然成立，尚存疑。

】

---

【LatentRefusal: Latent-Signal Refusal for Unanswerable Text-to-SQL Queries ｜基于隐状态探针的文本到SQL安全拒绝机制

研究机构：复旦大学

作者：Xuancheng Ren、Shijing Hu、Zhihui Lu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.10398)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.10398)

> 文本到SQL系统在面临不可回答或模糊查询时，极易生成看似合理但语义错误的可执行代码，导致数据泄露或业务事故。现有基于提示词或输出不确定性的拒绝策略要么在模型幻觉时失效，要么因需多次采样或执行SQL而违背安全低延迟约束。本文提出在SQL生成前，通过冻结大语言模型中间层隐状态进行确定性门控拦截。该机制以极低的计算开销实现了高可靠的安全拒绝，但其在复杂多跳推理场景下的信号捕捉能力仍存疑。

】

---

【Memo-SQL: Structured Decomposition and Experience-Driven Self-Correction for Training-Free NL2SQL ｜结构化分解与经验驱动自修正的无微调NL2SQL框架

研究机构：香港城市大学、华为

作者：Zerui Yang、Weichuan Wang、Yanwei Xu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.10011)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.10011)

> 自然语言到SQL（NL2SQL）的核心挑战在于将模糊的口语意图映射为精确的结构化查询，而现有测试时扩展（Test-Time Scaling, TTS）方法往往因分解随意导致候选SQL高度相关，且自修正机制依赖静态示例无法适应新错误类型。Memo-SQL通过预定义的多轴结构化分解和动态错误-修正记忆检索，解决了推理多样性不足与修正泛化能力弱的问题。该方法在无微调开源模型上实现了BIRD基准68.5%的执行准确率，同时大幅降低计算开销，但其跨域迁移能力和对复杂嵌套查询的覆盖度仍存疑。

】

---

【MTO: A Multi-turn Conversational Text-to-OverpassQL Dataset for Enhanced OpenStreetMap Query Generation ｜基于语法树剪枝的多轮地理空间查询数据集构建

作者：Haodi Zhang、Xinrui Zhu、Mingze Kong 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_38f3ab66aa65)

】

---

【PV-SQL: Synergizing Database Probing and Rule-based Verification for Text-to-SQL Agents ｜数据库探针与规则验证协同的文本到SQL智能体

研究机构：美国普渡大学

作者：Yuan Tian、Tianyi Zhang

论文原文见 [arXiv](https://arxiv.org/abs/2604.17653)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17653)

> 文本到SQL系统在处理复杂查询时，常因无法获取数据库实际值而误解语义，且生成的SQL缺乏有效的语义校验机制。现有提示工程方法依赖静态模式链接，无法动态探索数据内容，而基于大语言模型（LLM）的自我验证又存在不可靠与高成本问题。PV-SQL通过“数据库探针”动态获取数据证据，结合“规则约束验证”进行确定性修复，构建了输入增强与输出校验的闭环。该方法在免微调范式下显著提升了执行准确率与效率，但其规则覆盖范围有限，对长尾语义约束的泛化能力存疑。

】

---

【R$^3$-SQL: Ranking Reward and Resampling for Text-to-SQL ｜基于组级奖励与代理重采样的文本到SQL排序框架

研究机构：韩国电子通信研究院、韩国首尔大学

作者：Hojae Han、Yeonseok Jeong、Seung-won Hwang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.25325)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.25325)

> 文本到SQL系统普遍采用“生成-排序”范式，但现有排序器无法区分功能等价但表面形式不同的SQL，且当正确SQL未出现在候选池中时无法恢复。本文指出这两者分别对应“功能不一致性”与“有界召回”问题，提出R³-SQL框架，通过执行结果分组、组级双信号排序及条件触发的代理重采样统一解决。该方法在BIRD-dev上取得75.03%的执行准确率，但依赖监督训练的排序器限制了域外泛化能力。

】

---

【ReSQL: Self-Improving Framework for Reasoning-Aware Text-to-SQL Dataset Generation ｜检索增强错误推理框架

研究机构：LG AI研究院

作者：Minjun Park、Yongju Seong、Myoseop Sim 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c94eec99e1cb)

> 小模型在文本到SQL任务中面临高频执行错误且缺乏零样本自修正能力，现有提示工程方法因依赖大模型推理能力而失效。ReSQL将执行错误转化为结构化推理数据用于微调，并在推理时检索相似错误案例辅助修正。该框架在SPIDER和BIRD基准上使7B-9B模型超越GPT-4，但绝对性能仍低于大模型SOTA，且未验证跨域泛化能力。

】

---

【Rethinking Text-to-SQL: Dynamic Multi-turn SQL Interaction for Real-world Database Exploration ｜动态多轮SQL交互基准

研究机构：中国科学院大学、北京大学

作者：Linzhuang Sun、Tianyu Guo、Hao Liang 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f3178f68c7fe)

> 现有文本到SQL（Text-to-SQL）基准将任务简化为静态单轮翻译，忽略了真实场景中用户意图的动态演化与数据库状态的持续变更。本文指出，静态评估无法捕捉多轮对话中的状态维护与错误恢复能力，因此构建了首个支持完整CRUD操作的动态交互基准。通过两阶段自动合成管线与三元交互框架，DySQL-Bench揭示了前沿大语言模型在动态SQL推理上的显著脆弱性。该基准填补了动态评估空白，但模拟用户的保真度与评估协议的封闭性仍存疑。

】

---

【SQL-ASTRA: Alleviating Sparse Feedback in Agentic SQL via Column-Set Matching and Trajectory Aggregation ｜多轮代理强化学习中的轨迹级奖励聚合与列集匹配机制

研究机构：澳大利亚格里菲斯大学、复旦大学

作者：Long Li、Zhijian Zhou、Jiangxuan Long 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.16161)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.16161)

> 文本到SQL任务正从单轮静态生成向多轮动态交互演进，但现有强化学习方法受限于最终轮次的二值反馈，导致中间步骤的信用分配模糊且奖励信号稀疏。本文切入点在于构建一个双层奖励机制，通过列集匹配提供步级密集信号，并利用非对称转移矩阵聚合轨迹级奖励以激励单调改进。该方法将SQL生成建模为有限时域马尔可夫决策过程，结合Lyapunov稳定性理论证明策略的无环收敛性。尽管在7B小模型上验证了多轮代理范式的有效性并超越单轮基线，但其绝对性能仍低于当前SOTA，且多轮交互带来的推理延迟与部署成本问题未被充分量化。

】

---

【SQLAgent: Learning to Explore Before Generating as a Data Engineer ｜SQLAgent: 基于自主探索的双智能体文本到SQL框架

研究机构：西湖大学、美国加州大学默塞德分校

作者：Wenjia Jiang、Yiwei Wang、Boyan Han 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2688e00dcffb)

> 导读 企业级数据库的文本到SQL（Text-to-SQL）任务面临模式链接与跨域泛化的双重瓶颈，现有提示工程方法依赖静态示例或单次生成，难以应对未见过的复杂模式结构。SQLAgent 提出“探索-部署”两阶段框架，通过蒙特卡洛树搜索（MCTS）驱动的自主探索构建数据库特定知识库，再由双智能体协作完成查询生成。该设计将一次性生成转化为主动熟悉数据库的过程，显著提升了复杂查询的执行准确率。然而，探索阶段的高昂计算成本与对实时性场景的适用性限制，使其在通用基准上的表现未达领域最优，其价值边界需结合具体部署场景评估。

】

---

【VET: Verifiable Execution Tracing for Reliable Text-to-SQL Generation ｜可执行执行追踪

研究机构：中国科学技术大学

作者：Dongyu Wang、Jingyu Li、Lan Zhang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e8bed31a5c5c)

> 文本到SQL的核心困境在于自然语言意图与数据库结构间的语义鸿沟，导致模型生成语法正确但语义错误的查询。现有思维链方法依赖不可验证的文本推理，程序思维方法仅在最终阶段执行代码，均无法拦截中间步骤的逻辑错误。VET将推理过程重构为逐步执行的Python代码序列，每一步立即在真实数据库上运行并验证，确保中间状态与数据现实一致。该框架在免训练设置下显著提升了复杂查询的准确率，但其性能上限受限于骨干模型能力，且未解决推理延迟问题。

】
