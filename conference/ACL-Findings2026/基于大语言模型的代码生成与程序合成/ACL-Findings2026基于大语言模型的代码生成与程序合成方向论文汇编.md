# ACL-Findings2026 · 基于大语言模型的代码生成与程序合成方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CodeRise: Bootstrapping LLMs for Ultra Low-Resource Programming Languages via Progressive Self-Refinement Curriculum ｜超低资源编程语言代码生成的渐进式自精炼框架

研究机构：中国科学院大学、中国科学院

作者：Tengfei Wen、Xuanang Chen、Ben He 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dd9054980de6)

> 超低资源编程语言（ULRPLs）因公开语料极度匮乏，导致大语言模型（LLMs）无法通过常规预训练习得其语法与库函数，陷入“冷启动”困境。现有合成数据方法在ULRPLs上失效，因为模型初始能力近乎为零，无法生成任何有效代码样本，且直接提供完整语法文档会导致推理缓慢与数据分布长尾化。CodeRise通过两阶段框架解决此问题：第一阶段利用语法引导与模块加权采样生成种子数据，第二阶段移除语法提示，通过自适应课程学习与多轮自调试生成复杂高质量数据。该方法在Tengo和Janet语言上显著优于基线，但其性能上限受限于骨干模型的通用推理能力，且对完整语法文档的依赖仍是潜在瓶颈。

】

---

【CollabCoder: Plan-Code Co-Evolution via Collaborative Decision-Making for Efficient Code Generation ｜协同进化代码生成

作者：Duy Tung Doan、Quang Huy Phung、Dzung Nguyen 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.13946)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a03012f7df10)

> 多智能体代码生成框架长期受困于静态规划与无状态调试，导致在复杂任务上产生大量冗余计算且难以定位根本错误。现有方案如MapCoder与CodeSIM虽引入迭代机制，但规划模块在调试过程中保持固定，无法根据代码反馈动态修正高层逻辑。本文提出CollabCoder，通过协同决策模块动态选择更新规划或代码，并结合推理轨迹累积历史经验，实现规划与代码的协同进化。该方法在保持高准确率的同时显著降低计算开销，但其固定权重机制在极端难度任务上的适应性仍存疑。

】

---

【HintPilot: LLM-based Compiler Hint Synthesis for Code Optimization ｜编译器提示合成

研究机构：浙江大学、美国普渡大学

作者：Hanyun Jiang、Peisen Yao、Kaiyue Li 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fd08108bd59a)

> 代码优化旨在提升程序执行效率，但传统编译器启发式规则难以适应复杂异构系统，而直接让大语言模型（LLM）重写源码又极易破坏语义正确性。现有方法要么全局选择优化Pass导致细粒度机会丢失，要么直接修改代码引入不可控风险。HINTPILOT 提出通过合成编译器提示（Compiler Hints）这一中间层，利用检索增强生成与执行反馈迭代，在保持语义不变的前提下实现细粒度性能调优。该方法在 HumanEval_CPP 上实现了相对 -Ofast 6.88× 的几何平均加速比，但其对特定硬件与编译器版本的依赖性及跨编译器泛化能力仍存疑。

】

---

【Parallel-SFT: Improving Zero-Shot Cross-Programming-Language Transfer for Code RL ｜平行监督微调（Parallel-SFT）：基于执行等价性的代码强化学习跨语言迁移

研究机构：美国麻省理工学院

作者：Zhaofeng Wu、Shiqi Wang、Boya Peng 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e95b94477403)

> 导读 代码强化学习（RL）在源编程语言上获得的策略增益，往往无法零样本迁移至目标语言，甚至导致性能退化。现有方法依赖自然语言中天然存在的平行文本对齐表示空间，但代码语料缺乏此类信号，导致模型陷入语法中心而非功能中心的表示陷阱。本文提出 Parallel-SFT，通过合成跨语言功能等价程序构建平行语料，在监督微调阶段对齐表示空间，从而提升后续 RL 阶段的跨语言迁移能力。该方法在 Llama-3.1-8B 上验证了有效性，但其对大规模模型及非执行等价语义迁移的适用性尚存疑。

】

---

【SolidCoder: Bridging the Mental-Reality Gap in LLM Code Generation through Concrete Execution ｜弥合心理-现实鸿沟：基于具体执行的代码生成框架

研究机构：韩国电子通信研究院

作者：Woojin Lee、Jin-Xia Huang

论文原文见 [arXiv](https://arxiv.org/abs/2604.19825)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.19825)

> 多智能体代码生成框架依赖大语言模型（LLM）内部的心理模拟来验证代码正确性，但模型常因幻觉而自信地通过有缺陷的代码。本文指出这一“心理-现实鸿沟”源于规划阶段的边界盲区与验证阶段的执行幻觉，并提出了 SolidCoder 框架。该框架通过前置边界识别与沙箱具体执行，将验证从“想象”转变为“运行”。这一转变在中等难度竞赛编程任务上带来了显著的性能提升，但其高昂的推理成本与对属性断言生成能力的依赖，限制了其在极端复杂或简单任务上的普适性。

】
