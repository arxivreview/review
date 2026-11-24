# ACL2026 · 用于分子与材料发现的LLM方向论文汇编

> 本方向共 2 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CAML: A Conflict-Aware Molecular Language Model Merging Framework for Multi-Constraint Molecular Generation ｜冲突感知分子语言模型合并框架

作者：Xuanbai Ren、Luoda Tan、Pei Liu 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_143b558d6ff2)

> 多属性分子生成面临数据稀疏与属性内在冲突的双重瓶颈，传统迁移学习难以同时满足多个竞争性约束。现有模型合并方法依赖静态启发式阈值，无法动态处理专家模型间复杂的非线性属性冲突。本文提出CAML，将模型合并重构为合作博弈，通过无梯度进化算法求解纳什均衡以最小化属性冲突。该方法在四组多约束任务上优于静态合并基线，但其性能提升是否源于博弈论假设对分子属性耦合关系的过度简化，仍需更广泛的化学有效性验证。

】

---

【MolMem: Memory-Augmented Agentic Reinforcement Learning for Sample-Efficient Molecular Optimization ｜记忆增强型代理强化学习用于样本高效分子优化

研究机构：美国西北大学

作者：Ziqing Wang、Yibo Wen、Abhishek Pandy 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12237)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12237)

> 分子优化旨在有限实验预算下迭代改进先导化合物性质，但现有试错法与模板模仿法均难以在低样本效率下平衡性质提升与结构相似性。本文切入点在于将多轮交互中的成功经验蒸馏为可检索的长期记忆，以弥补单次生成或静态检索的知识复用缺陷。通过构建静态示例库与动态技能库的双记忆系统，结合密集步级奖励的代理强化学习，该方法在500次Oracle调用下实现了单属性任务90%的成功率。其价值在于验证了记忆机制对样本效率的关键作用，但技能库的泛化边界与动态更新机制仍存疑。

】
