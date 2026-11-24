# ACL-Findings2026 · 模型合并与权重集成方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【On the Representation Geometry of LoRA Model Merging ｜LoRA 模型合并中的 SVD-CUR 几何互补性分析

研究机构：加拿大多伦多大学、美国西北大学

作者：Chenyang Lu、Jiaru Li、Jinman Zhao 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a22ac2d9d557)

> 导读 多任务 LoRA 合并面临的核心困境在于，现有方法普遍假设单一全局子空间足以对齐所有任务更新，但低秩约束导致不同任务的更新方向在参数空间中系统性错位。本文切入点在于揭示奇异值分解（SVD）与列选择分解（CUR）在捕获共享结构与任务特异结构上的几何互补性，而非直接提出新算子。通过构建双分支并行对齐框架并基于残差能量加权融合，该方法在视觉与语言基准上实现了无训练合并性能的稳定提升。其价值在于从表示几何层面解构了合并失效的根源，但实验未覆盖异构秩或跨架构场景，其理论边界仍受限于同源初始化假设。

】

---

【PRIME: Ultra-Low-Rank Principal–Residual Model Merging ｜超低位秩主-残差模型合并

作者：Seung-Ho Lee、Kyungsu Lee、Bazarvaani Zuchi 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f438846722d1)

> 模型合并旨在通过参数空间操作整合多个专家模型，以规避联合训练的高昂成本，但任务向量间的参数干扰常导致合并性能低于单任务专家。现有基于稀疏化或子空间投影的方法在激进截断以消除干扰时，往往丢失关键的任务特异性信息，陷入干扰消解与能力保留的权衡困境。PRIME 提出超低位秩主-残差分解框架，将任务向量分离为主成分与正交残差，分别进行白化合并与正交投影恢复。该方法在 T5 和 LLaMA-3.2 上均显著优于现有代数基线，但其固定 1% 秩的设定在任务数量剧烈变化时的鲁棒性尚存疑。

】

---

【Will it Merge? On The Causes of Model Mergeability ｜模型更新的可合并性归因分析

研究机构：以色列理工学院、IBM研究院

作者：Adir Rahamim、Asaf Yehudai、Boaz Carmeli 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_56a884c3193b)

> 模型合并旨在通过参数空间操作整合多个专家模型，以缓解海量微调模型部署时的存储与推理成本瓶颈。现有算法如 TIES-Merging 和 KNOTS 聚焦于消解参数干扰，但未能解释为何在相同训练条件下，部分模型更新能无缝融合而另部分则导致性能退化。本文切入点在于定义“可合并性”（Mergeability），将其量化为模型更新在合并后保留知识的程度，并归因于基座模型对特定任务的先验知识。通过构建基于基座准确率的加权合并策略，本文证明了先验知识是决定合并成败的主导因素，但该方法在极端异构任务下的鲁棒性尚未得到充分验证。

】
