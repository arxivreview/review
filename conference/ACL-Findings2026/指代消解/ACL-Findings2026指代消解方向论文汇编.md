# ACL-Findings2026 · 指代消解方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【MEIC-DT: Memory-Efficient Incremental Clustering for Long-Text Coreference Resolution with Dual-Threshold Constraints ｜双阈值约束下的内存高效增量聚类

研究机构：清华大学

作者：Kangyang Luo、Shuzheng Si、Yuzhuo Bai 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8255170f17b0)

> 长文本共指消解面临Transformer自注意力机制的内存溢出瓶颈，传统增量聚类方法虽通过缓存驱逐缓解内存压力，但牺牲了全局语义建模能力。MEIC-DT针对这一矛盾，提出双阈值约束机制，在严格内存预算下同时限制集群数量与每集群提及数。该方法通过统计感知驱逐策略与内部正则化策略，在LitBank基准上以81.27%的CoNLL F1超越基线，验证了其在资源受限环境下的有效性，但其性能优势是否完全源于底层Maverick模型而非约束机制本身，仍需进一步隔离验证。

】
