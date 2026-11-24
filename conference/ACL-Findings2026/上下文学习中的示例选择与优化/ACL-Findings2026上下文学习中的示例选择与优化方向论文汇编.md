# ACL-Findings2026 · 上下文学习中的示例选择与优化方向论文汇编

> 本方向共 6 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Beyond Task-Level Context: Class-Conditional Context Vectors for Implicit In-Context Learning ｜类条件上下文向量（C3V）：隐式上下文学习中的细粒度语义解耦

作者：Jianxin Zhang、Yilu Hu、Teng Liu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_964d9478050d)

> 导读 隐式上下文学习旨在将演示样本压缩为潜在向量以消除推理时的长上下文开销，但现有任务级向量聚合掩盖了分类任务中不同类别的语义差异，导致细粒度判别能力受损。本文切入点在于将单一任务向量解耦为类条件向量组，通过线性干预机制在冻结骨干模型中注入类特异性信号。该方法以极小的可训练参数量实现了类感知适应，在多数基准上超越了任务级基线，但其性能增益依赖于类别数量的规模效应，且在二分类任务上未表现出一致优势。

】

---

【From Fake to Real: Mitigating Out-of-Distribution Bias in In-Context Learning via Feedback Supervision from Large Language Models ｜基于置信度与扰动困惑度的分布外伪标签迭代选择

研究机构：吉林大学

作者：Rui Song、Yingji Li、Jian Li 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e8772ba4cb74)

> 上下文学习（In-Context Learning, ICL）在源域与目标域分布差异显著时，基于相似度的演示检索往往失效甚至劣于随机选择。现有鲁棒性缓解方法多依赖显式分布对齐或代理域检索，难以在缺乏目标域标签的条件下直接利用测试样本。本文提出 LPL，通过轻量模型生成初始伪标签，结合置信度与扰动困惑度（CPP）筛选高质量样本，并由 LLM 迭代扩充演示池以规避分布外（Out-of-Distribution, OOD）偏差。该方法在多个 NLP 任务上验证了噪声容忍的有效性，但其性能增益高度依赖伪标签初始质量，在对抗性数据集上优势收窄。

】

---

【Label Words as Local Task Vectors in In-Context Learning ｜局部任务向量机制：ICL 信息聚合的双层解构

研究机构：香港中文大学、中国科学院

作者：Bowen Zheng、Ming Ma、Zhongqiao Lin 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_79ca5b43b0b0)

> 上下文学习（ICL）的核心机制在于模型如何从演示样本中提取并应用任务规则，但现有研究普遍假设存在一个统一的全局任务向量来承载所有任务信息。这一假设在依赖预训练知识的任务中成立，但在需要归纳复杂规则的分类任务中失效，导致基于全局向量的压缩或迁移策略性能崩溃。本文通过引入“局部任务向量”概念，揭示了每个演示的答案位置隐藏状态作为独立信息载体的作用，并证明全局向量仅是局部向量在特定任务下的收敛结果。这种双层机制解释为何全局向量在分类任务中无效，为理解 ICL 的边界条件提供了微观视角，但其结论局限于合成任务，向真实复杂场景的迁移性尚存疑。

】

---

【Many-Shot Scaling of In-Context Learning with Self-Generated Demonstrations ｜半监督上下文学习

研究机构：美国康奈尔大学、清华大学

作者：Zhengyao Gu、Henry Peng Zou、Yankai Chen 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f9e637235522)

> 上下文学习（In-Context Learning, ICL）的性能上限受限于高质量标注数据的获取成本，而现有自生成演示方法多局限于少样本场景，无法利用长上下文的规模效应。本文切入点在于将传统半监督学习的迭代精炼与课程学习范式迁移至 ICL 演示生成流程，通过置信度过滤与动态演示池更新实现千级伪演示的规模化扩展。具体做法是提出 Naive-SemiICL 基线与 IterPSD 迭代算法，利用 LLM 的口头置信度筛选低质标注，并通过课程采样缓解错误累积。该方法在零样本与少样本预算下均优于标准 ICL，但其在高资源场景下的增益边际递减，且未解决自生成演示在分布外数据上的鲁棒性问题。

】

---

【Task-Related In-Context Learning ｜任务相关上下文学习

研究机构：中山大学、兰州大学

作者：Wenqiang Wang、Peng Chen、Yan Xiao 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5d49badaa2b7)

> 上下文学习（In-Context Learning, ICL）通常假设检索集与测试集共享相同的输出空间，但在弱监督或跨任务场景中，这一假设常被打破，导致标准 ICL 性能崩溃。现有方法多聚焦于标签对齐下的演示筛选，对标签空间完全不相交（Fully Disjoint）的情形缺乏有效机制。本文提出 TRICL 框架，通过贝叶斯准则筛选任务相关子集，利用中间预测缩减目标输出空间，从而在不依赖标签对齐的前提下实现有效推理。该框架在多个数据集上显著优于基线，但其性能高度依赖中间任务预测的准确性，且未验证在大规模候选池下的检索效率。

】

---

【UCS: Estimating Unseen Coverage for Improved In-Context Learning ｜未见覆盖率选择

研究机构：美国宾夕法尼亚大学

作者：Jiayi Xin、Xiang Li、Evan Qiang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12015)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12015)

> 上下文学习（ICL）性能对演示样本的选择极度敏感，但现有方法多聚焦于实例级的相关性或多样性，缺乏对候选池潜在语义空间覆盖广度的量化机制。本文指出，仅优化局部相似度或子集体积无法捕捉长尾分布中未被揭示的潜在簇，导致模型在复杂任务上暴露不足。为此，提出未见覆盖率选择（Unseen Coverage Selection, UCS），一种基于平滑古德-图灵估计器的无训练子集级覆盖先验，通过正则化现有选择目标来偏向覆盖更多未见簇的子集。UCS在意图分类与推理任务上带来2-6%的准确率提升，但其效果高度依赖基线选择器的强度，且在强基线上增益微弱，其统计假设与LLM内部机制的对齐程度仍存疑。

】
