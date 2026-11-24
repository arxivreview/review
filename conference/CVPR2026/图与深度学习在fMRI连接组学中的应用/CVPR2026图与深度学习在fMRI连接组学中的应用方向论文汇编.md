# CVPR2026 · 图与深度学习在fMRI连接组学中的应用方向论文汇编

> 本方向共 2 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Continual Learning for fMRI-Based Brain Disorder Diagnosis via Functional Connectivity Matrices Generative Replay ｜功能连接矩阵生成式回放的持续学习框架

研究机构：新加坡南洋理工大学

作者：Qianyu Chen、Shujian Yu

论文原文见 [arXiv](https://arxiv.org/abs/2604.14259)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14259)

> 临床fMRI数据通常来自不同机构，且受隐私法规限制无法集中存储，导致模型在顺序学习新站点数据时发生灾难性遗忘。现有离线训练或简单回放方法无法在保护隐私的同时维持跨站点泛化能力。本文提出FORGE框架，通过结构感知的变分自编码器合成功能连接矩阵，结合双层级知识蒸馏实现隐私友好的持续学习。该框架在三个神经影像数据集上显著降低了遗忘率，但其生成回放机制对站点特异性伪影的累积效应尚未被充分验证。

】

---

【IEBGL:An Interpretability-Enhanced Brain Graph Learning Framework with LLM-Instructed Topology and Literature-Augmented Semantics ｜基于大语言模型与文献语义的脑图可解释性增强框架

研究机构：南京大学

作者：Yihang Duan、Shuo Huang、Li Zhang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f1de245a93a2)

> 现有基于静息态功能磁共振成像（rs-fMRI）的脑图学习方法依赖统计相关性构建拓扑，导致节点特征缺乏生物学语义，模型预测难以映射至临床知识。IEBGL通过引入大语言模型（LLM）重构拓扑结构，并聚合生物医学文献语义增强节点表征，试图在提升分类精度的同时解决可解释性缺失问题。该框架在REST-meta-MDD和ABIDE数据集上取得了优于多数基线的性能，但其静态功能连接假设与当前动态建模趋势存在张力，且性能未超越领域内最新SOTA。

】
