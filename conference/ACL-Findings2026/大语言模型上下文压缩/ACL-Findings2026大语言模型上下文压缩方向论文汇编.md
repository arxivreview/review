# ACL-Findings2026 · 大语言模型上下文压缩方向论文汇编

> 本方向共 6 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Adaptive Zooming via Relevance-Informed Positional Resource Allocation for Training-free LLM Context Extension ｜基于语义相关性的位置资源分配

研究机构：华东师范大学、复旦大学

作者：Hongbo Zhao、Huibin Wang、Bin Tang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_76a2cef09da3)

> 长上下文推理中，模型在超出预训练窗口时因位置编码分布外（Out-of-Distribution, OOD）效应导致性能骤降。现有免训练外推方法仅依据Token相对距离进行均匀或固定比例的位置映射，无法区分语义关键信息与噪声，导致关键证据在长序列中被模糊。本文提出RiPRA，将位置编码重构为基于查询语义相关性的约束资源分配问题，动态调整位置分辨率。该方法在免训练外推类别中表现最优，但其性能上限仍低于专用上下文压缩方法，且缺乏对压缩率与推理延迟的联合评估。

】

---

【BRIEF-Pro: Universal Context Compression with Short-to-Long Synthesis for Fast and Accurate Multi-Hop Reasoning ｜短长合成与指令控制的通用上下文压缩

研究机构：美国加州大学洛杉矶分校

作者：Jia-Chen Gu、Junyi Zhang、Di Wu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.13799)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9c4e840c17e8)

> 检索增强生成（RAG）在处理复杂多跳推理时，因检索文档过长导致推理延迟激增且模型认知负载过重。现有压缩方法要么依赖专有模型蒸馏，要么局限于短上下文且缺乏用户可控性。BRIEF-PRO 通过短上下文种子数据合成长上下文训练集，并引入指令条件化机制，实现了对 10k+ 词上下文的轻量级摘要压缩。该方法在保持高压缩比的同时提升了多跳问答准确率，但其对多跳依赖结构的线性化处理在复杂推理任务上存在性能瓶颈。

】

---

【CODEPROMPTZIP: Code-specific Prompt Compression for Retrieval-Augmented Generation in Coding Tasks with LMs ｜代码提示压缩

作者：Pengfei He、Shaowei Wang、Tse-Hsun Chen

论文原文见 [arXiv](https://arxiv.org/abs/2502.14925)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c07d2f7d9ca8)

> 检索增强生成（RAG）在代码任务中常因引入大量示例导致提示词长度激增，超出模型上下文窗口或产生高额API成本。现有通用压缩方法缺乏对代码语法结构的感知，盲目剔除Token易破坏代码逻辑。本文提出CodePromptZip，一种基于程序分析类型优先级与复制机制的硬压缩框架，旨在保留关键代码语义的同时实现可控比率压缩。该方法在三个代码任务上显著优于熵基与蒸馏基线，但其依赖静态分析工具的特性限制了在不可解析代码上的泛化能力。

】

---

【Concept rather than Document: Context Compression via AMR-based Conceptual Entropy ｜基于抽象意义表示的概念熵上下文压缩

研究机构：澳大利亚悉尼科技大学、香港理工大学

作者：Kaize Shi、Xueyao Sun、Xiaohui Tao 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2509f5d14fe6)

> 导读 检索增强生成（RAG）场景下，长文档中的冗余信息常干扰大语言模型（LLM）对关键事实的提取，导致推理性能下降。现有压缩方法多依赖词法或Token级特征，易割裂语义单元，难以保留核心概念。本文提出基于抽象意义表示（Abstract Meaning Representation, AMR）的概念熵筛选框架，通过量化AMR节点的信息熵识别语义关键概念，重构紧凑上下文。该方法在PopQA和EntityQuestions上优于基线，但实验设置排除了检索噪声，且未对比最新软压缩方法，其泛化能力存疑。

】

---

【Decoupled Reasoning with Implicit Fact Tokens (DRIFT): A Dual-Model Framework for Efficient Long-Context Inference ｜解耦推理与隐式事实Token

研究机构：复旦大学、同济大学

作者：Wenxuan Xie、Yujia Wang、Xin Tan 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.10021)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.10021)

> 长上下文推理面临计算复杂度与有效信息利用率的双重瓶颈，现有静态压缩方法在极端压缩比下易丢失任务关键信息，而参数化知识编辑又面临灾难性遗忘风险。DRIFT 通过双模型架构将知识提取与核心推理解耦，利用轻量级知识模型将文档压缩为查询感知的隐式事实Token，再投影至推理模型嵌入空间。该设计在保持推理模型参数冻结的前提下实现了32倍压缩比下的性能提升，但其对大规模模型扩展性及隐式表示的可解释性边界尚存疑。

】

---

【RepoDistill: Distilling Repository Knowledge through Compression-Aware Budget Allocation and Policy Optimization ｜代码仓库级上下文蒸馏：基于预算分配与策略优化的压缩框架

研究机构：浙江大学、上海交通大学

作者：Xin Yin、Zixiang Ding、Yiang Zhang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2f34605a547f)

> 大语言模型在处理仓库级代码任务时，常因长上下文中的冗余信息导致注意力稀释与关键逻辑丢失。现有检索方法虽能定位相关片段，但无法在函数内部进一步剔除噪声，且静态压缩策略难以适应动态查询需求。RepoDistill 通过图结构检索结合强化学习驱动的细粒度预算分配，实现了从“片段级筛选”到“行级蒸馏”的跨越。该方法在代码问答与生成任务上显著优于基线，但其效果高度依赖预训练小模型的蒸馏质量，跨仓库泛化能力尚存疑。

】
