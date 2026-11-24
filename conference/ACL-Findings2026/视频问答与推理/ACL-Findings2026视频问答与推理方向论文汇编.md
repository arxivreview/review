# ACL-Findings2026 · 视频问答与推理方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【MT-Video-Bench: A Holistic Video Understanding Benchmark for Evaluating Multimodal LLMs in Multi-Turn Dialogues ｜多轮视频对话基准

研究机构：复旦大学、南京大学

作者：Yaning Pan、Qianqian Xie、Guohui Zhang 等 16 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.17722)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.17722)

> 视频理解领域长期聚焦于单轮问答，忽略了真实交互中用户迭代提问、话题切换与上下文依赖的复杂性。现有基准如Video-MME和LongVideoBench仅评估模型对视频内容的静态感知，无法衡量其在多轮对话中维持连贯性、拒绝幻觉及主动交互的能力。本文构建MT-Video-Bench，通过1,000个多轮对话实例系统评估多模态大语言模型（MLLMs）的感知性与交互性。该基准填补了多轮视频对话评估的空白，但仅作为评测工具，未提出新的模型架构或训练策略，其有效性依赖于Checklist评估协议的完备性。

】

---

【VChain: Chain-of-Visual-Thought for Reasoning in Video Generation ｜视觉思维链驱动的推理增强视频生成

研究机构：新加坡南洋理工大学

作者：Ziqi Huang、Ning Yu、Gordon Chen 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.05094)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.05094)

> 导读 视频生成模型在合成复杂动态场景时，常因缺乏对物理规律和因果逻辑的显式建模，导致生成的视频在状态转换上出现逻辑断裂或物理违和。现有方法多依赖大规模数据驱动的黑盒学习，难以在推理阶段灵活注入高层语义约束，且全量微调成本高昂。VChain 提出了一种推理时微调框架，利用多模态大模型生成稀疏的“视觉思维”关键帧，并通过低秩适配（LoRA）对预训练视频生成器进行轻量级对齐。该工作验证了将语言模型的因果推理能力转化为视觉监督信号的有效性，为视频生成的可控性提供了新路径，但其对多模态模型生成质量的依赖及评估基准的局限性仍需进一步审视。

】
