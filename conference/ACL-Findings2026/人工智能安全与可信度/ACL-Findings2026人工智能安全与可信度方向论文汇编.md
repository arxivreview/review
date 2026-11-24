# ACL-Findings2026 · 人工智能安全与可信度方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Towards Provably Secure Generative AI: Reliable Consensus Sampling ｜可靠共识采样（RCS）：消除弃权的生成式AI形式化安全框架

研究机构：北京理工大学、清华大学

作者：Yu Cui、Hang Fu、Sicheng Pan 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0bdadeaf9ebc)

> 导读 生成式AI的安全防御长期依赖经验性过滤，但密码学证明表明高效提示过滤器不存在，且部分风险不可检测，导致模型推理风险无法根除。现有共识采样（Consensus Sampling, CS）虽提供理论风险上界，却依赖频繁弃权牺牲可用性，且在拜占庭模型恶意操纵下鲁棒性崩溃。本文提出可靠共识采样（Reliable Consensus Sampling, RCS），通过实时追踪接受概率并在采样失败后进入重加权追踪阶段，彻底消除弃权并保证最终交付。该工作将安全从经验性防护转向可证明的数学保证，但其有效性严格依赖于模型组中安全模型数量占优的假设，在极端对抗强度下安全率仍显著衰减。

】
