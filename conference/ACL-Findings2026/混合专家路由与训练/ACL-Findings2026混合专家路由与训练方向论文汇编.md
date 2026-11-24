# ACL-Findings2026 · 混合专家路由与训练方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【From Outcome to Process: Optimizing MoE Load Balancing with MCTS ｜基于蒙特卡洛树搜索的LoRA-MoE层级负载均衡

研究机构：东南大学、澳门大学

作者：Wenjun Ke、Hengyuan Xu、Ziyu Shang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4f1df957d029)

> 混合专家模型在参数高效微调中面临专家激活坍缩，即少数专家主导计算而多数闲置，导致容量浪费。现有方法仅在最终损失层面施加平衡约束，忽略了路由决策在层间累积的偏差。本文提出LayerMoE，将专家选择重构为序列决策问题，利用蒙特卡洛树搜索（MCTS）生成层级奖励信号，在训练阶段引导门控机制实现过程级负载均衡。该方法在多个基准上提升了LoRA-MoE基线的平均准确率，但实验规模局限于单卡小模型，且未验证MCTS在大规模预训练场景下的可扩展性。

】

---

【From Pseudo-Balancing to True Specialization: Memory-Aware Routing for Mixture-of-Experts ｜记忆感知路由

研究机构：北京大学、阿里巴巴集团

作者：Peixuan Hou、Yunbo Hou、Bin Chen 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_397698e75146)

> 混合专家（Mixture-of-Experts, MoE）模型在引入负载均衡损失后，常陷入“伪平衡”陷阱：为追求专家利用率均匀，同一输入在不同训练步被随机分配至不同专家，导致语义对齐失效与参数冗余。现有方法仅从参数或分布层面干预，未能解决路由决策的时序不稳定问题。本文通过为每个专家引入记忆缓冲区，将历史Token表示转化为偏好向量，并以此修正路由分数，实现训练阶段的语义一致性引导。该方法在保持全局负载均衡的同时显著提升了专家专业化程度，但其效果依赖于训练阶段的记忆维护，推理阶段需依赖基础路由器已内化的策略，其长期泛化能力尚存疑。

】

---

【Improved Policy Optimization for Mixture-of-Experts Models: Importance Sampling and Rewarding from an Expert-Centric Perspective ｜专家相对策略优化

研究机构：东南大学、华为

作者：Yining Qian、Jinpeng Li、Fei Mi 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_536380857cc6)

> 混合专家模型在强化学习后训练中因新旧策略专家分配分歧导致重要性采样比率剧烈波动，引发训练崩溃。现有序列级采样方法虽稳定但丢失了Token功能差异，而路由重放方法虽对齐但抑制了探索。本文提出专家级重要性采样与熵奖励机制，在保持采样稳定性的同时保留功能粒度并显式优化路由策略。该方法在数学推理基准上显著优于基线，但其对路由一致性的依赖及熵奖励的泛化性仍存疑。

】
