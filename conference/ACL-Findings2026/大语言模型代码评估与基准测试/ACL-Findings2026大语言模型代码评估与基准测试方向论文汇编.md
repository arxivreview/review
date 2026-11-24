# ACL-Findings2026 · 大语言模型代码评估与基准测试方向论文汇编

> 本方向共 11 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Can LLMs Compress (and Decompress)? Evaluating Code Understanding and Execution via Invertibility ｜往返代码一致性评估

研究机构：英国爱丁堡大学

作者：Nickil Maveli、Antonio Vergari、Shay B. Cohen

论文原文见 [arXiv](https://arxiv.org/abs/2601.13398)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.13398)

> 现有代码基准仅验证单向输入输出预测，无法区分模型是依靠模式匹配还是机制理解生成代码。RTCE通过强制模型执行无损压缩算法的正向编码与逆向解码，以精确匹配验证双向逻辑闭环。该框架揭示了当前大语言模型在双向推理一致性上的系统性缺陷，但受限于合成数据规模与算法类型，其结论向真实复杂代码库的泛化能力存疑。

】

---

【ContractEval: A Benchmark for Evaluating Contract-Satisfying Assertions in Code Generation ｜契约满足评估基准

研究机构：韩国延世大学

作者：Soohan Lim、Joonghyuk Hahn、Hyunwoo Park 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.12047)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.12047)

> 现有代码生成基准仅验证良构输入下的功能正确性，导致模型在拒绝非法输入这一关键防御机制上存在盲区。HumanEval+等基准虽标注了契约字段，却将其用于过滤违规测试而非评估拒绝行为，使得“契约满足”这一维度长期不可测。本文通过神经符号流水线生成精准违规测试，将契约满足率确立为独立评估轴。该工作揭示了当前大语言模型在边界防御上的系统性缺失，但其评估范围仍局限于函数级输入验证，未触及跨文件依赖或复杂类型系统的深层契约。

】

---

【CoRE: A Fine-Grained Code Reasoning Benchmark Beyond Output Prediction ｜代码推理基准 CoRE：从输出预测到过程忠实

作者：Jun Gao、Yun Peng、Qian Qiao 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1e462fbafd0f)

> 导读 代码生成模型在静态基准上接近满分，但“能写出正确代码”与“真正理解执行逻辑”之间存在断层。现有推理基准仅依赖单一标准实现和最终输出，无法区分深层语义推理与表面模式匹配。CoRE 通过构建功能等价但语法多样的多实现集合，并引入中间状态探针，联合评估实现不变性与过程透明度。该基准揭示了前沿模型的风格过拟合与表面执行现象，但其评估协议对探针难度的控制及跨语言泛化能力仍存疑。

】

---

【Duplicate-Aware Controlled Code Generation: Enhancing Copyright Protection with Targeted Reordering Beam Search in LLMs ｜重复感知受控代码生成

作者：Junbo Fu、Guoshuai Zhao、Linkang Yang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6274b366a671)

> 大语言模型在代码生成中倾向于逐字复现训练数据片段，直接触发版权侵权风险，而现有评估体系仅关注功能正确性，忽视了输出内容的法律合规性。传统的数据清洗或后处理去重方法要么破坏模型能力，要么无法实时控制重复长度，导致在保持代码功能完整性的同时消除逐字重复成为技术难点。本文提出重复感知受控代码生成（DACCG）任务，并设计目标重排束搜索（TRBS）算法，在解码阶段通过动态重排候选束来实时抑制重复序列。该方法在8B参数模型上实现了重复率与准确率的灵活权衡，但受限于单函数场景与小模型规模，其在真实仓库级工程环境中的有效性尚未得到验证。

】

---

【Exploring Coding Spot: Understanding Parametric Contributions to LLM Coding Performance ｜编码参数子集定位

作者：Dongjun Kim、Minhyuk Kim、Yongchan Chun 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c31722a1204c)

> 大语言模型（LLM）在代码生成任务上表现优异，但其内部如何组织编码知识仍属黑盒，现有评估体系仅关注外部行为正确性，无法解释能力来源。本文提出“编码点”（Coding Spot）概念，旨在定位承载编码能力的稀疏参数子集。通过跨语言泰勒近似评分与定向消融，验证了该子集的存在性及其语言无关性。这一发现为模型压缩与安全部署提供了新视角，但受限于单一模型家族与静态基准，其结论在复杂工程场景下的普适性尚存疑。

】

---

【Idea First, Code Later: Disentangling Problem Solving from Code Generation in Evaluating LLMs for Competitive Programming ｜先想后写：编辑式解耦竞赛编程中的推理与实现

作者：Sama Hadhoud、Alaa Elsetohy、Frederikus Hudi 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2164c4884be7)

> 竞赛编程（Competitive Programming, CP）评估长期将算法规划与代码实现混同为单一端到端任务，导致模型失败时无法区分是“想错了”还是“写错了”。现有基准如LiveCodeBench虽解决了数据污染，但仍无法定位推理瓶颈。本文切入点是将自然语言编辑式（Editorial）作为显式中间产物，通过对比模型自生成编辑式与专家金标编辑式下的代码通过率，量化“解题”与“实现”的独立贡献。其价值在于首次提供了可操作的解耦评估协议，但83题的小样本规模限制了统计稳健性，且仅覆盖C++/Python两种语言。

】

---

【IntentCoding: Amplifying User Intent in Code Generation ｜意图放大解码：多约束代码生成的信号增强机制

研究机构：北京大学、加拿大阿尔伯塔大学

作者：Zheng Fang、Yihong Dong、Lili Mou 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.00066)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.00066)

> 大语言模型在代码生成中常因用户意图对logits影响微弱而违背多约束指令，现有解码策略无法有效放大该信号。本文提出Intent[↑] Coding，通过对比原始与意图掩码logits提取意图信号，并采用多强度集成动态放大该信号以引导解码。该方法无需训练且模型无关，在约束遵循基准上取得最高71.0%的相对提升，但其收益是否随模型规模增大而递减尚存疑。

】

---

【LLMs are Brittle to Simple Code Transformations: Introducing CETBench – A Benchmark for Code-Equivalence Checking ｜代码等价性检查基准

作者：Neeva Oza、Ishaan Govil、Parul Gupta 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7fe2279b9011)

> 代码等价性检查旨在判定两段程序是否对所有输入产生相同输出，是程序验证与重构的基础。现有静态分析工具难以处理语义保持的语法变异，而基于测试用例的执行验证受限于输入域覆盖不全，导致LLM在此任务上表现脆弱。本文通过构建包含组合语义扰动的基准CETBench，量化模型区分语法变化与语义变化的能力。该基准揭示了SOTA模型在简单变换下的显著性能退化，但受限于二元标签简化与合成扰动结构，其结论向真实复杂重构场景的泛化性仍存疑。

】

---

【MdEval: Massively Multilingual Code Debugging ｜大规模多语言代码调试基准

作者：Shukai Liu、Linzheng Chai、Jian Yang 等 18 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0de3c21c27f1)

> 现有代码调试基准局限于Python等少数语言，无法反映LLM在Rust、Go等语言特定错误（如Missing mut）上的真实能力。本文通过人工标注与LLM生成混合构建覆盖20种语言、3.9K样本的MDEVAL基准，并设计xDebugGen注入策略生成指令语料。该工作填补了多语言调试评估的空白，但静态人工标注的规模限制与单文件任务粒度，使其难以捕捉仓库级上下文中的调试失效。

】

---

【SWE-QA-Pro: A Representative Benchmark and Scalable Training Recipe for Repository-Level Code Understanding ｜仓库级代码理解基准与代理训练

研究机构：加拿大滑铁卢大学、加拿大多伦多大学

作者：Songcheng Cai、Zhiheng Lyu、Yuansheng Ni 等 16 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.16124)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.16124)

> 仓库级代码理解要求模型在跨文件依赖中追踪控制流，但现有基准多依赖片段级问答或流行仓库，导致模型可通过预训练记忆“作弊”而非真正探索代码库。SWE-QA-Pro 通过长尾仓库采样与难度校准过滤掉可直接回答的题目，强制保留需多跳推理的任务，并配套 SFT→RLAIF 训练配方提升小模型代理能力。该工作验证了代理式探索对仓库级理解的必要性，但 LLM-as-Judge 评分的主观性与小模型泛化边界仍存疑。

】

---

【UCoder: Unsupervised Code Generation by Internal Probing of Large Language Models ｜无监督代码生成：内部探测与执行共识

作者：Jiajun Wu、Jian Yang、Wei Zhang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_19d4a1f0fa84)

> 导读 大语言模型（LLM）在代码生成上的能力依赖大量人工标注或外部代码语料，但高质量指令数据获取成本高且易受污染。现有无监督方法多依赖未标注代码片段，仍受限于外部数据分布偏差，无法完全脱离语料依赖。本文提出IPC框架，通过六阶段自举流程探测LLM内部潜在编程知识，利用执行反馈构建确定性监督信号，实现无外部语料的代码生成能力提升。该方法在开源模型上验证了可行性，但绝对性能仍落后于闭源SOTA，且自生成任务分布偏差风险未完全解决。

】
