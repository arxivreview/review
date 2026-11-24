# ACL2026 · 文本到SQL生成方向论文汇编

> 本方向共 12 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Adaptive Text2GQL: Integrating Structural Twig Linking and Evolutionary In-Context Learning ｜自适应图查询生成

研究机构：清华大学

作者：Fang Niu、Chaokun Wang、Hang Zhang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ff774942a04d)

> 图数据库查询语言（GQL）的语法异构性与拓扑复杂性使得自然语言到查询的转换面临比关系型数据库更严峻的冷启动与结构幻觉挑战。现有方法依赖静态示例或单一语言微调，无法在缺乏平行标注数据的情况下实现跨语言泛化，且难以修复逻辑正确但拓扑无效的查询。本文提出一种无训练框架，通过结构树链接提供拓扑先验，利用演化式上下文学习动态构建验证示例库，并引入对抗性执行引导修正闭环。该框架在跨语言生成上优于现有基线，但其性能上限受限于自建小数据集的规模，且未验证在大规模工业图数据库上的可扩展性。

】

---

【DPC: Training-Free Text-to-SQL Candidate Selection via Dual-Paradigm Consistency ｜双范式一致性

研究机构：香港科技大学

作者：Boyan Li、Ou Ocean Kun Hei、Yue Yu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.15163)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8432e7ca4ec5)

> 文本到SQL（Text-to-SQL）任务中，大语言模型（LLM）生成的候选查询池往往包含正确逻辑，但缺乏可靠的无训练选择机制将正确项从噪声中剥离，导致高潜在准确率无法转化为实际执行准确率。现有基于多数投票或LLM自评估的方法受限于系统性偏差与符号盲性，无法在隐藏数据分布上做出确定性判断。本文提出DPC框架，通过合成最小可区分数据库并引入Python代码作为代理真值，将概率猜测转化为确定性验证。该方法在BIRD和Spider基准上稳定优于基线，但其性能增益依赖于候选池质量，且对Python生成错误的鲁棒性未充分验证。

】

---

【GBV-SQL: Guided Generation and SQL2Text Back-Translation Validation for Multi-Agent Text2SQL ｜语义反向验证与基准清洗：GBV-SQL 的深度剖析

研究机构：英国谢菲尔德大学、北京交通大学

作者：Daojun Chen、Xi Wang、Shenyuan Ren 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.12612)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.12612)

> 导读

】

---

【GQLBench: A Large-Scale Cross-Domain, Cross-Dialect Benchmark for NL2GQL ｜图查询语言生成基准

作者：Yanning Su、Yuhang Zhou、Yang Fang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_45593ae6b20a)

> 自然语言到图查询语言（NL2GQL）任务旨在将用户意图转化为可执行的图数据库查询，但现有资源缺乏同时具备大规模、跨领域及跨方言支持的能力，导致模型泛化能力评估碎片化。本文通过自动化框架整合NL2SQL资源转换与图原生数据合成，构建了支持Cypher与ISO GQL执行验证的基准。该框架利用规则与LLM混合迁移关系数据，并基于几何分布生成复杂拓扑结构。GQLBench揭示了当前LLM在图结构推理上的显著短板，但缺乏与专用NL2GQL模型的直接横向对比，其作为通用基准的排他性边界尚待厘清。

】

---

【MTSQL-R1: Towards Long-Horizon Multi-Turn Text-to-SQL via Agentic Training ｜长程多轮文本到SQL代理训练

研究机构：美国圣母大学

作者：Taicheng Guo、Hai Wang、ChaoChun Liu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.12831)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.12831)

> 多轮文本到SQL旨在将连续对话中的每句用户话语映射为可执行SQL，同时维持跨轮次语义一致性与模式接地。现有方法多采用短程推理范式，仅基于当前话语与少量历史生成查询，缺乏对数据库的显式交互验证与自我修正机制，导致输出常出现语义无效或前后矛盾。本文提出MTSQL-R1，将任务重构为马尔可夫决策过程（MDP），通过自教式预热监督微调与端到端强化学习，使模型在“提议-执行-验证-修正”闭环中自主迭代。该方法在开源小模型上实现了多轮任务的性能突破，但其依赖金标准SQL筛选轨迹的预热机制，可能限制了模型探索非标准正确解的空间。

】

---

【PExA: Parallel Exploration Agent for Complex Text-to-SQL ｜并行探索代理：软件测试视角下的复杂文本到SQL生成

研究机构：美国加州大学洛杉矶分校

作者：Tanmay Parekh、Ella Hofmann-Coyle、Shuyi Wang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.22934)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.22934)

> 复杂企业数据库中的自然语言查询往往涉及嵌套数据类型与超长SQL，现有串行推理代理虽能提升准确率，但延迟随推理步骤线性增长，难以满足交互式分析需求。PEXA将文本到SQL重构为软件测试覆盖问题，通过并行生成并执行一组简化的“测试用例”SQL，在获取充分语义证据后合成最终查询。该框架在Spider 2.0基准上取得了70.2%的执行准确率，同时保持了与串行基线相当的低延迟。其价值在于打破了性能与延迟的帕累托约束，但测试用例的“过度生成”策略是否会在极端复杂场景下导致计算成本失控，仍需进一步验证。

】

---

【QBridge: Bridging Natural Language and SQL via Gold Query Rewriting with Agentic Refinement ｜QBridge：基于金标准查询范式的代理式NL2SQL框架

研究机构：浙江大学、香港科技大学

作者：Zhensheng Luo、Sai Wu、Yuan Qiu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9e06f6ffe13e)

> 自然语言到SQL（NL2SQL）旨在将口语化问题映射为可执行查询，但真实用户提问常存在噪声、歧义及与数据库语义的弱对齐，导致单步解码脆弱。现有方法多依赖解码器同时处理意图解析与模式链接，缺乏对语言层面失配的显式干预。QBridge通过引入“金标准查询”（Gold Query）作为结构化中间表示，结合蒸馏回译与双反馈修正机制，在零样本骨干下提升生成鲁棒性。该框架在Spider基准上取得86.2%的执行准确率，但绝对性能仍低于最新强化学习基线，其轻量级适配策略的泛化边界尚待验证。

】

---

【REaR : Retrieve, Expand and Refine for Effective Multitable Retrieval ｜多表检索中的结构连接性缺失与无LLM解耦框架

作者：Rishita Agarwal、Himanshu Singhal、Peter Baile Chen 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5c485344cd65)

> 文本到SQL任务中，多表查询的准确性高度依赖于候选表集是否包含所有必要的连接路径，但现有检索器仅优化查询与单表的语义相关性，忽略了表与表之间的结构兼容性，导致下游生成器因缺乏连接线索而幻觉或丢弃约束。本文指出这一“相关性-连接性”错位是性能瓶颈，提出REAR框架，通过离线预计算列嵌入实现无LLM调用的三阶段检索。该框架在保持与LLM检索方法相当性能的同时，将延迟降低约4倍，但其端到端执行准确率仍受限于生成模型能力，且固定阈值在不同领域数据库中的鲁棒性存疑。

】

---

【ReEx-SQL: Reasoning with Execution-Aware Reinforcement Learning for Text-to-SQL ｜执行感知强化学习文本到SQL生成

研究机构：复旦大学、中国科学院大学

作者：Yaxun Dai、Wenxuan Xie、Xialie Zhuang 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ef7ba813e7b8)

> 文本到SQL的核心矛盾在于自然语言的模糊性与SQL执行的确定性之间的鸿沟，传统思维链推理缺乏外部验证导致错误累积。现有强化学习方法虽能优化推理路径，但将执行反馈隔离在解码之外，无法实时修正语义偏差。ReEx-SQL将SQL执行器嵌入强化学习的Rollout过程，通过生成-验证-修正闭环实现端到端交互。该方法在7B规模下实现了鲁棒性基准的领先，但其性能上限受限于骨干模型能力，且执行反馈的延迟开销在复杂查询中是否可接受仍存疑。

】

---

【Rose-SQL: Role-State Evolution Guided Structured Reasoning for Multi-Turn Text-to-SQL ｜角色状态演化引导的结构化推理

研究机构：国防科技大学、中国科学院

作者：Le Zhou、Feng Yao、Fengcai Qiao 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6f069643ee92)

> 多轮文本到SQL任务要求模型在连续对话中追踪指代并生成上下文一致的查询，现有微调方法成本高且难以适应新场景，而直接提示小模型常因缺乏结构约束导致语义与语法脱节。Rose-SQL通过引入角色状态（Role-State）作为结构蓝图，利用同构检查验证历史轨迹，在无微调条件下引导小模型进行分层推理。该框架在SParC和CoSQL验证集上显著超越了微调基线，但其对复杂嵌套查询的表示能力及跨方言泛化性仍存疑。

】

---

【ROSE: An Intent-Centered Evaluation Metric for NL2SQL ｜意图中心评估指标 ROSE

研究机构：香港科技大学、新加坡国立大学

作者：Wenqi Pei、Shizheng Hou、Boyan Li 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12988)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12988)

> NL2SQL 领域长期依赖执行准确率（EX）作为核心指标，但该指标在语义等价但形式不同、问题存在歧义或金标准错误时失效，导致模型性能被系统性低估或误判。现有 LLM 评估器虽引入语义判断，但仍锚定单一金标准 SQL，无法区分“逻辑正确但形式偏离”与“逻辑错误”。本文提出 ROSE，通过 Prover-Refuter 对抗级联实现意图中心评估，在金标准独立判断与对抗验证之间取得平衡。其在专家共识验证集上 Cohen’s κ 达 80.43%，较最强基线 FLEX 提升 24%，但依赖推理模型成本且验证集规模有限，长期稳定性存疑。

】

---

【SQL-Trail: Multi-Turn Reinforcement Learning with Interleaved Feedback for Text-to-SQL ｜多轮强化学习文本到SQL代理

研究机构：美国斯坦福大学

作者：Harper Hua、Zhen Han、Zhengyuan Shen 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.17699)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.17699)

> 文本到SQL任务的核心矛盾在于自然语言的模糊性与SQL语法的严格性，现有单轮生成范式无法利用数据库执行反馈进行自我修正，导致在复杂模式链接和嵌套查询上性能受限。SQL-TRAIL 将任务重构为多轮交互代理，通过自适应轮次预算和复合奖励机制，让模型在训练阶段即学会“探测-执行-修正”的闭环行为。该方法以极少的训练数据（1.8k样本）实现了显著的数据效率提升和跨域泛化能力，但其绝对精度仍受限于小模型基座，且对执行环境的依赖引入了新的计算开销。

】
