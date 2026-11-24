# Others2026 · 视频问答与推理方向论文汇编

> 本方向共 2 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Video Evidence to Reasoning Efficient Video Understanding via Explicit Evidence Grounding ｜证据链推理

研究机构：香港理工大学

作者：Yanxiang Huang、Guohua Gao、Zhaoyang Wei 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.07761)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.07761)

> 视频大语言模型（LVLMs）在处理长视频时面临感知精度与推理效率的结构性矛盾：冗长的思维链（Chain-of-Thought, CoT）消耗大量计算资源，而高效采样又导致视觉证据丢失引发幻觉。现有方法要么依赖外部多阶段流水线增加延迟，要么在提示层隐式接地，无法在架构层面同时保证证据的显式定位与推理的紧凑性。本文提出CoE框架，通过内嵌的证据接地模块（Evidence Grounding Module, EGM）在编码器与解码器之间进行查询引导的特征过滤，并结合强化学习优化证据-逻辑对齐，实现了精度与效率的协同提升。该框架在多个基准上刷新了开源模型SOTA，但其性能增益中骨干网络贡献与架构创新贡献的边界尚不清晰。

】

---

【VIGiA: Instructional Video Guidance via Dialogue Reasoning and Retrieval ｜指令性视频计划引导

作者：Diogo Glória-Silva、David Semedo、João Maglhães

论文原文见 [arXiv](https://arxiv.org/abs/2602.19146)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.19146)

> 指令性视频计划引导旨在让模型在对话中实时跟踪用户执行进度，并基于视觉输入与文本计划进行接地推理。现有方法多局限于纯文本引导或单帧检索，无法处理多模态交互中的状态漂移与证据缺失。VIGiA 通过多目标架构与专门设计的检索投影层，实现了计划推理与视频片段检索的统一。该模型在自建数据集上展现了极高的任务准确率，但其依赖私有数据且未采用强化学习后训练，泛化能力存疑。

】
