# Others2026 · 大型语言模型的机器遗忘方向论文汇编

> 本方向共 1 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Operationalising the Right to be Forgotten in LLMs: A Lightweight Sequential Unlearning Framework for Privacy-Aligned Deployment in Politically Sensitive Environments ｜串行两阶段层限制遗忘框架

作者：Esen Kurt、Haithem Afli

论文原文见 [arXiv](https://arxiv.org/abs/2604.12459)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12459)

> 大语言模型在政治敏感场景下的部署面临“被遗忘权”合规与通用能力保持的结构性冲突。现有联合优化方法因保留与遗忘梯度方向冲突导致训练不稳定或效用崩溃，而完全重训练在计算上不可行。本文提出一种串行两阶段优化策略，先通过正向微调锚定良性能力，再对高层参数执行受限负向微调以抑制敏感模式。该框架在GPT-2上实现了行为层面的有效抑制，但其机制深度与对抗鲁棒性未经验证，且实验局限于小模型规模。

】
