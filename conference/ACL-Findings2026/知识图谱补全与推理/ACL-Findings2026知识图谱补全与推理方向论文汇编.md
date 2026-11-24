# ACL-Findings2026 · 知识图谱补全与推理方向论文汇编

> 本方向共 4 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【MAKI: Multi-layer Aligned Knowledge Injection for Structure-aware Knowledge Graph Completion with Large Language Models ｜多层对齐知识注入

研究机构：澳门大学、华为

作者：Zhiwen Xie、Xin Wang、Guangyou Zhou 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9f0810d7f6b7)

> 知识图谱补全（KGC）旨在预测图谱中缺失的实体或关系，其核心价值在于缓解结构化数据稀疏性与开放世界推理需求之间的张力。现有基于大语言模型（LLM）的方法常因结构嵌入与语义空间的根本错位，导致对长尾及未见实体的泛化能力受限。MAKI 通过构建与 LLM 隐层逐层对齐的图神经网络（GNN）模块，将结构信息以门控方式注入 LLM 内部，实现了语义与拓扑的深层协同。该框架在归纳式基准上展现了显著的推理优势，但其性能增益在多大程度上归因于 LLM 骨干本身而非结构注入机制，仍存疑。

】

---

【Not All Modalities at Once: Dynamic Dropout and Bidirectional Fusion for Robust Multi-modal Knowledge Graph Completion ｜模态丢弃与双向门控融合

研究机构：美国东北大学

作者：Jiashun Peng、Fu Zhang、Hongzhi Chen 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b6df3569bffd)

> 多模态知识图谱补全（Multi-modal Knowledge Graph Completion, MKGC）旨在利用文本、图像与结构化三元组推断缺失链接，但现有方法在训练时默认所有模态始终可用且互补，导致模型在异构噪声下产生模态依赖与竞争。本文指出，这种“全模态无差别训练”忽视了单模态对训练动态的独立影响，进而提出MDBGF框架，通过概率驱动的模态丢弃（Modality Dropout, MD）与双向门控融合（Bidirectional Gated Fusion, BGF）动态调控模态使用。该框架在轻量级嵌入骨干上实现了多模态基准的SOTA，但其未验证在大型语言模型（Large Language Models, LLMs）骨干下的有效性，且缺乏对推理时模态缺失鲁棒性的直接评估。

】

---

【Risk-Controlled Event-Driven Cascading Updates for Knowledge Graph Consistency Restoration ｜事件驱动级联知识图谱一致性修复

研究机构：美国范德堡大学、Adobe研究院

作者：Bo Ni、Qinwen Ge、Haowei Fu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a2fb024a048d)

> 动态知识图谱（Dynamic Knowledge Graph, DKG）在引入新事实时，常因局部更新引发依赖关系的连锁失效，导致图谱整体不一致。传统补全模型假设数据内部一致，无法处理这种由外部事件触发的多跳级联修正需求。本文提出 CASCADEKG 框架，通过 Learn-Then-Test (LTT) 校准控制级联错误累积，并结合大语言模型（Large Language Model, LLM）增强事件语义评分。该方法在自建基准上实现了风险可控的一致性恢复，但其统计保证依赖于校准集规模，且未验证在超大规模图谱上的计算效率。

】

---

【Structure-Aware Zero-Shot Relational Learning for Knowledge Graphs without External Knowledge ｜结构感知零样本关系学习

研究机构：北京交通大学

作者：Kuan Xu、Baoxin Zhang、Shuyue Fan 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8c19695e2cdd)

> 知识图谱补全（Knowledge Graph Completion, KGC）在处理新涌现关系时面临零样本关系学习（Zero-Shot Relational Learning, ZRL）难题，现有方法依赖文本描述或本体等外部知识，导致标注成本高且适用性受限。本文切入点在于利用KG内部结构模式替代外部知识，通过共享实体构建条件查询图并自适应聚合邻居关系嵌入。该方法在NELL-ZS和Wiki-ZS上分别取得10.66%和4.33%的MRR提升，证明了纯结构信号的可行性，但其对关系语义抽象程度的依赖及在大规模稀疏图上的泛化能力存疑。

】
