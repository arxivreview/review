# ACL-Findings2026 · 大语言模型的多样性与可控解码方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【DeCoVec: Building Decoding Space based Task Vector for Large Language Models via In-Context Learning ｜解码空间任务向量

研究机构：深圳大学

作者：Feiyang Li、Yile Wang

论文原文见 [arXiv](https://arxiv.org/abs/2604.11129)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d49479e2329b)

> 大语言模型（LLMs）在特定任务上的表现往往受限于预训练阶段的通用分布，微调虽能提升性能但伴随高昂的计算成本与参数侵入性。现有任务向量方法多依赖权重差或激活状态干预，难以在冻结模型中实现轻量级引导。DECOVEC 提出在解码 logit 空间通过对比少样本与零样本上下文构建任务向量，直接注入生成过程以替代微调。该方法在 0.5B 至 9B 模型上验证了免训练引导的有效性，但其双前向传播机制带来的推理延迟与向量跨任务泛化能力仍存疑。

】
