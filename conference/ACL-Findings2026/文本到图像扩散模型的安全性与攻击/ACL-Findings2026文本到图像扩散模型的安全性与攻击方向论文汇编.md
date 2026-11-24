# ACL-Findings2026 · 文本到图像扩散模型的安全性与攻击方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【When Backdoors Go Beyond Triggers: Semantic Drift in Diffusion Models Under Encoder Attacks ｜编码器后门引发的无触发语义漂移诊断

作者：Shenyang Chen、Liuwan Zhu

论文原文见 [arXiv](https://arxiv.org/abs/2602.20193)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.20193)

> 文本到图像（T2I）扩散模型的后门攻击研究长期聚焦于触发器激活成功率（ASR），却忽视了编码器侧污染对良性生成质量的隐性损害。现有基于ASR的评估范式存在“盲区”，无法捕捉无触发状态下嵌入空间的几何扭曲，导致防御机制在抑制显式攻击的同时遗留结构性缺陷。本文提出SEMAD框架，通过Jacobian局部变形分析与语义漂移评分，量化这种无触发的语义坍缩。该工作揭示了后门攻击的几何本质，但缺乏对修复效果的验证，其诊断价值是否足以指导防御设计仍存疑。

】
