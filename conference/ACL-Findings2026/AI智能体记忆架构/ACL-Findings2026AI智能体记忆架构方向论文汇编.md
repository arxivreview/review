# ACL-Findings2026 · AI智能体记忆架构方向论文汇编

> 本方向共 7 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CLAG: Adaptive Memory Organization via Agent-Driven Clustering for Small Language Model Agents ｜基于代理驱动聚类的自适应记忆组织

研究机构：韩国高丽大学

作者：Taeyun Roh、Wonjune Jang、Junha Jung 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.15421)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.15421)

> 长程任务中，大语言模型（LLM）智能体依赖外部记忆维持连贯性，但传统全局检索池随记忆增长导致语义干扰与更新污染，小语言模型（SLM）对此尤为脆弱。现有代理记忆框架虽引入自进化机制，却仍在全局无结构存储中运行，无法隔离主题混杂带来的噪声。CLAG通过SLM代理在线路由将记忆划分为语义一致的簇，并在簇内执行局部演化与两阶段检索，以轻量级结构抑制跨主题干扰。该框架在SLM场景下显著提升了鲁棒性，但其对大模型骨干的增益边际递减，且未覆盖隐私合规与多模态对齐等生产级约束。

】

---

【Demystify the Role of Memory in Machine Learning Engineering Agents ｜机器学习工程智能体中的动态编码记忆：架构依赖性与探索-利用权衡

研究机构：美国北卡罗来纳大学教堂山分校

作者：Xinyu Zhao、Junpeng Wang、Yuzhong Chen 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_18671558eeed)

> 机器学习工程（Machine Learning Engineering, MLE）智能体在自动化数据科学工作流中常陷入重复错误循环，导致搜索效率低下。现有通用对话记忆系统无法适配代码调试的结构化特性，且未揭示记忆对不同搜索架构的差异化影响。本文提出任务-包粒度的动态编码记忆，将其集成至链式与树式两种智能体范式，实证了记忆对链式智能体可靠性的提升及对树式智能体探索多样性的抑制。该研究揭示了记忆作为“双刃剑”的架构依赖性，但缺乏对记忆强度动态调节的机制设计，其结论在更复杂的多任务迁移场景中是否普适仍存疑。

】

---

【ENPMR-Bench: Benchmarking Proactive Memory Retrieval for Emotional Support Agents ｜情感需求感知主动记忆检索基准

作者：Xing Fu、Yulin Hu、Mengtong Ji 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1e278c652254)

> 情感支持智能体面临的核心矛盾是用户情绪表达的间接性与记忆检索的语义表面性之间的错位。现有记忆基准假设用户能明确表达需求，导致检索目标与情感共鸣脱节，无法评估智能体推断潜在需求并匹配记忆类型的能力。本文通过构建基于马斯洛需求层级的结构化映射框架，将情感需求推断与记忆类型选择解耦为可评估的独立环节。该基准揭示了当前检索范式在情感场景下的系统性失效，但缺乏对动态记忆演化机制的验证，其结论的泛化性存疑。

】

---

【FlashMem: Distilling Intrinsic Latent Memory via Computation Reuse ｜计算复用蒸馏内在潜在记忆

研究机构：北京航空航天大学、中国科学院

作者：Yubo Hou、Zhisheng Chen、Tao Wan 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fe92e0585f8a)

> 大语言模型（Large Language Model, LLM）的无状态特性导致智能体在长程任务中必须冗余重处理历史上下文，而现有生成式潜在记忆（Generative Latent Memory）范式依赖独立辅助模块，造成架构分离与计算冗余。FlashMem 通过直接复用骨干网络的冻结键值（Key-Value, KV）缓存来合成记忆，并引入无参数注意力熵监控器实现自适应触发。该框架在推理任务上达到与重型基线相当的性能，同时将推理延迟降低 5 倍，但其长期记忆稳定性与跨会话一致性仍缺乏验证。

】

---

【MemORAI: Memory Organization and Retrieval via Adaptive Graph Intelligence for LLM Conversational Agents ｜记忆组织与自适应图智能检索

研究机构：澳大利亚莫纳什大学

作者：Hung Pham Van、Nguyen Manh Hieu、Khang Pham Tran Tuan 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c934793cded0)

> 长程对话智能体面临的核心矛盾是上下文窗口的有限性与个性化交互对持久化状态的需求。现有图谱记忆系统虽能建模实体关系，但普遍存在信息稀释、事实来源不透明以及检索传播机制忽略查询语义三大缺陷，导致高连接度节点主导结果而语义相关但稀疏连接的节点被抑制。MemORAI通过引入用户画像选择性过滤、轮次级溯源异质图谱及查询条件化动态加权PageRank，在存储、表示与检索三个环节同时介入，试图将记忆从被动存储转变为可审计、上下文敏感的认知组件。该框架在受控条件下显著提升了检索召回率与生成事实性，但其优势是否源于架构创新还是特定骨干模型的配合，以及静态过滤机制能否适应用户偏好的长期漂移，仍存疑。

】

---

【Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution ｜动态程序性记忆框架 ReMe

研究机构：上海交通大学、阿里巴巴集团

作者：Zouying Cao、Jiaji Deng、Li Yu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.10696)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.10696)

> 大语言模型智能体在长程任务中面临重复试错与经验无法有效复用的困境，现有记忆系统多采用被动累积范式，导致经验池随时间退化且检索结果缺乏任务适配性。ReMe 通过多面蒸馏、上下文自适应复用与效用驱动精炼，将程序性记忆从静态存储转变为反馈驱动的进化闭环。该框架验证了记忆质量可部分替代模型规模的效应，但其效用删除机制在单次失败场景下的鲁棒性仍存疑。

】

---

【Text2Mem: A Unified Memory Operation Language for Memory Operating System ｜统一记忆操作语言

作者：Leo Wang、Lihai Yang、Boyu Chen 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fa768cf74138)

> 大语言模型智能体在长程交互中面临记忆管理碎片化问题，现有系统仅暴露编码、检索等基础原语，缺乏对优先级调整、合并、锁定等高级治理操作的形式化定义，导致跨系统行为不一致且难以审计。本文切入点在于将自然语言指令映射为具有显式字段与语义不变量的模式化操作契约，通过验证-解析-适配流水线实现确定性执行。Text2Mem定义了12个覆盖记忆全生命周期的动词，并构建了分离规划与执行评估的双层基准。该工作确立了记忆操作接口的标准化范式，但其端到端任务性能优势及在复杂动态环境下的泛化能力尚未得到充分验证。

】
