# ACL-Findings2026 · 视觉语言模型的视觉提示调优方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Generalizable Prompt Tuning for Audio-Language Models via Semantic Expansion ｜语义扩展提示调优

研究机构：韩国科学技术院

作者：Jaehyuk Jang、Wonjun Lee、Kangwook Ko 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.20867)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.20867)

> 音频-语言模型（ALMs）提示调优面临基础类过拟合导致的新类泛化崩溃，即基础-新类权衡（BNT）。现有视觉提示调优方法直接迁移至音频域时，因音频基准语义稀疏性导致嵌入空间结构崩塌，单纯架构增强或静态正则化无法重建语义簇。SEPT 通过大语言模型生成语义邻居，引入带边际约束的语义扩展损失，在冻结骨干下显式重塑文本嵌入几何结构。该方法以零额外推理开销显著提升了跨数据集泛化性能，但其效果高度依赖外部 LLM 的邻居生成质量，且未验证在视觉域或动态提示架构下的普适性。

】
