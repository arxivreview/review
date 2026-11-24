# ACL2026 · 面向LLM智能体的长期记忆架构方向论文汇编

> 本方向共 12 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents ｜智能体记忆：统一长短期记忆管理的强化学习框架

研究机构：武汉大学、阿里巴巴集团

作者：Yi Yu、Liuyi Yao、Yuexiang Xie 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_25e74e011cdc)

> 长时程智能体任务中，固定上下文窗口导致关键信息丢失与认知矛盾，现有方法将长期记忆（LTM）与短期记忆（STM）作为独立模块处理，依赖启发式规则或外部控制器，难以端到端优化。AgeMem 将 LTM 与 STM 操作统一为智能体策略中的工具动作，通过三阶段渐进强化学习与步级 GRPO 实现联合优化。该框架在五个长时程基准上超越了 Mem0 等强基线，验证了统一策略的有效性，但其性能高度依赖骨干模型质量，且未解决多模态记忆融合问题。

】

---

【Chain-of-Memory: Lightweight Memory Construction with Dynamic Evolution for LLM Agents ｜记忆链：轻量构建与动态演化

研究机构：中科院计算所、中国科学院大学

作者：Xiucheng Xu、Bingbing Xu、Xueyun Tian 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.14287)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.14287)

> 长时程智能体记忆面临构建开销与推理效用的双重瓶颈。现有结构化记忆方案以高计算成本换取有限精度提升，而朴素检索拼接又无法将召回转化为准确答案。本文提出CoM框架，通过扁平索引降低构建成本，并在推理时动态组织记忆片段为连贯推理链。该范式在效率-精度权衡上取得突破，但其精度上限是否受限于非结构化存储，仍需在高复杂度多跳任务中验证。

】

---

【Cognitive Scaffold: From Fluid Context to Crystallized Memory for Long-Horizon DeepResearch Agents ｜认知脚手架：面向长时程深度研究智能体的流体-图谱解耦记忆架构

作者：Qiuyuan Ai、Zenghuang Fu、Zhaoyang Li 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2592b83fc558)

> 长时程深度研究智能体在数百步交互中面临线性上下文累积导致的“上下文-噪声权衡”，即关键证据被稀释且推理能力退化。现有摘要或折叠方法虽能压缩Token，但不可逆地丢失数值与实体细节，且检索依赖线性扫描。本文提出认知脚手架，将智能体状态解耦为流体工作上下文与持久化知识图谱，通过拒绝采样微调训练高保真压缩模型，实现结构化证据的结晶与思维驱动的双路检索。该架构在Xbench-DeepSearch等基准上超越了线性累积基线，但其性能高度依赖专用压缩模型的训练质量，且在通用事实召回任务上的泛化能力未经验证。

】

---

【Controllable Memory Usage: Balancing Anchoring and Innovation in Long-Term Human-Agent Interaction ｜可控制记忆使用：平衡锚定与创新

研究机构：复旦大学

作者：Muzhao Tian、Zisu Huang、Xiaohua Wang 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.05107)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05107)

> 长时程智能体交互中，用户常需动态调节模型对历史记忆的依赖程度，但现有架构将记忆检索视为静态注入，导致模型陷入“记忆锚定”——即无论用户意图如何，输出均过度依赖历史上下文。本文提出 SteeM 框架，通过偏好对齐的监督微调与强化学习，将记忆依赖度定义为用户可控的显式维度，实现从“全新视角”到“高保真继承”的连续调控。该方法在自建合成数据集上显著优于提示工程基线，但其有效性局限于特定任务类型，且缺乏在标准长时程基准上的泛化验证。

】

---

【EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning ｜EverMemOS：基于记忆生命周期的结构化长时程推理系统

作者：Chuanrui Hu、Xingze Gao、Zuyi Zhou 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.02163)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.02163)

> 导读 LLM智能体在长时程交互中面临的核心困境是固定上下文窗口导致的跨会话状态丢失与认知矛盾。现有记忆系统多将记忆视为孤立记录的扁平集合，缺乏将碎片化情景经验转化为连贯知识结构的显式机制，导致智能体虽能检索到相关事实，却无法检测冲突或维持稳定的用户模型。EverMemOS 提出了一种受生物记忆痕迹（Engram）启发的三阶段生命周期架构，通过情景轨迹形成、语义固化与重构性回忆，将离散交互转化为支持长时程推理的稳定语义结构。该系统在 LoCoMo 和 LongMemEval 基准上显著优于现有方法，但其性能增益对骨干模型的依赖以及前瞻性推断的独立贡献量化仍是存疑之处。

】

---

【Fine-Mem: Fine-Grained Feedback Alignment for Long-Horizon Memory Management ｜细粒度反馈对齐的长期记忆管理

作者：Weitao Ma、Xiaocheng Feng、Lei Huang 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c10ce71045ae)

> 长期记忆管理面临强化学习训练中的奖励稀疏与信用分配失效难题，导致策略优化停滞。现有训练式方法仅依赖全局任务奖励，无法指导局部记忆操作。本文通过引入块级步骤奖励与证据锚定奖励归因，将全局效用分解至具体操作步。该方法在Memalpha与MemoryAgentBench上取得领先性能，但其单层扁平记忆架构在多跳推理场景下的泛化能力存疑。

】

---

【GAM: Hierarchical Graph-based Agentic Memory for LLM Agents ｜分层图式智能体记忆

研究机构：浙江大学、美国罗格斯大学

作者：Zhaofen Wu、Hanrong Zhang、Fulin Lin 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12285)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12285)

> 长时程交互中，智能体需在实时捕获新信息与保持既有知识稳定之间取得平衡，但现有统一流式记忆系统因缺乏写隔离机制，易受瞬时噪声污染导致记忆丢失与语义漂移。GAM 通过解耦记忆编码与固化过程，将实时对话隔离在局部事件进展图中，仅在检测到语义边界时将其整合至全局主题关联网络，从而在结构上阻断噪声向长期记忆的传播。该框架结合图引导的多因子检索策略，在 LoCoMo 和 LongDialQA 基准上实现了推理准确率与计算效率的双重提升。其核心价值在于以生物启发式状态机替代启发式规则，但语义边界检测的 LLM 开销与开放域任务上的性能短板，限制了其在高延迟敏感场景中的普适性。

】

---

【HeLa-Mem: Hebbian Learning and Associative Memory for LLM Agents ｜基于赫布学习动态图的大语言模型记忆架构

作者：Jinchang Zhu、Jindong Li、Cheng Zhang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.16839)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cc2a35444f57)

> 大语言模型智能体在长时程交互中面临固定上下文窗口导致的跨会话状态丢失与认知矛盾，现有方法多将记忆视为静态向量库或固定图谱，忽视了记忆结构随交互动态演化的本质。HeLa-Mem 抓住“记忆关联需随共激活动态重组”这一被忽略的点，借鉴神经科学中的赫布学习机制，将对话历史建模为动态关联图，并通过在线编码、反思性固化与双路径检索实现记忆的持续演化。该架构在 LoCoMo 基准上以显著更少的上下文 Token 实现了优于基线的平均排名，但其绝对性能未超越最新工业级系统，且依赖固定超参数，在复杂长尾场景下的鲁棒性存疑。

】

---

【HyperMem: Hypergraph Memory for Long-Term Conversations ｜超图记忆架构

研究机构：中国科学院、中国科学院大学

作者：Juwei Yue、Chuanrui Hu、Jiawei Sheng 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.08256)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.08256)

> 长期对话智能体面临固定上下文窗口导致的跨会话状态丢失与高阶关联缺失问题。现有RAG与图谱方法依赖二元关系，无法捕捉三个及以上元素间的联合依赖，导致检索碎片化。HyperMem通过三层超图结构显式建模高阶关联，并设计粗到细检索策略。该架构在LoCoMo基准上取得92.73%的LLM-as-a-judge准确率，但评估协议单一且缺乏多基准验证，其泛化能力存疑。

】

---

【MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents ｜多图谱智能体记忆架构

研究机构：美国佛罗里达大学

作者：Dongming Jiang、Yi Li、Guanpeng Li 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.03236)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03236)

> 大语言模型在长时程交互中因固定上下文窗口导致状态丢失与推理断裂，现有记忆增强生成系统多依赖单一语义相似度检索，无法区分时间、因果与实体关系，导致多跳推理与对抗性任务表现受限。MAGMA 通过将记忆解耦为语义、时间、因果、实体四个正交图谱，并引入意图感知的策略引导遍历机制，实现了检索逻辑与存储结构的分离。该架构在长上下文基准上显著优于基线，但其性能优势高度依赖异步固化模块的离线计算，实时交互中的因果推理延迟仍是未解的权衡点。

】

---

【Mem2ActBench: A Benchmark for Evaluating Long-Term Memory Utilization in Task-Oriented Autonomous Agents ｜记忆驱动任务执行基准

研究机构：中国科学院、中国科学院大学

作者：Yiting Shen、Kun Li、Wei Zhou 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.19935)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.19935)

> 现有长期记忆评估基准多聚焦于显式查询下的事实召回，忽略了智能体在欠指定指令下主动重构工具参数的真实需求。MEM2ACTBENCH 通过反向生成范式，将评估目标从“问答”迁移至“工具调用”，强制模型依赖分散的历史记忆接地参数。该基准揭示了当前系统在中间上下文记忆利用与复杂参数接地上的显著短板，但受限于离线生成与固定骨干模型，其结论对交互式动态环境的普适性仍存疑。

】

---

【OCR-Memory: Optical Context Retrieval for Long-Horizon Agent Memory ｜光学上下文检索记忆

作者：Jinze Li、Yang Zhang、Xin Yang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.26622)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e7c695f0c9dc)

> 长时程智能体在有限上下文窗口内复用历史经验时，面临存储容量与信息保真度的根本冲突：文本摘要丢失细节，原始日志耗尽Token预算。现有检索增强生成（RAG）依赖相似度匹配，易混淆主题相关但逻辑无关的片段，且生成式检索存在幻觉风险。OCR-Memory将交互轨迹渲染为带视觉锚点的图像，通过“定位-转录”机制将检索转化为索引选择，从源头阻断幻觉。该框架在Mind2Web和AppWorld上取得SOTA，但视觉模态对复杂因果推理的支持能力仍存疑。

】
