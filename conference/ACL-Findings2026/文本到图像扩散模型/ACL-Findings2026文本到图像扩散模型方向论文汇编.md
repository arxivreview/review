# ACL-Findings2026 · 文本到图像扩散模型方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Universal Avoidance Method for Diverse Multi-branch Generation ｜通用避免生成

研究机构：韩国首尔大学

作者：Kyeongman Park、Minha Jhang、Kyomin Jung

论文原文见 [arXiv](https://arxiv.org/abs/2604.17323)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17323)

> 多分支生成任务要求同一提示词产生显著差异的输出，但现有方法要么依赖逐token或逐像素的高开销操作，要么绑定特定架构导致通用性缺失。UAG通过惩罚最终输出与历史输出的相似度梯度，在推理阶段实现跨架构的多样性增强。该方法将局部与全局相似度损失按生成阶段调度，以极低的计算成本同时适用于自回归与扩散模型。其核心价值在于以1/64的FLOPs实现了比SOTA方法更高的多样性，但图像生成中CLIP分数的下降暗示了多样性与语义保真度之间的潜在冲突。

】
