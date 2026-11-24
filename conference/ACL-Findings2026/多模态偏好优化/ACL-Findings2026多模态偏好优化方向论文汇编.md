# ACL-Findings2026 · 多模态偏好优化方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Trident: Self-Supervised Preference Alignment via Triplet Regularization ｜三元组正则化自监督偏好对齐

研究机构：浙江大学、上海交通大学

作者：Yingnan Guo、Kejia Chen、Xiaofeng Zhang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2c896ca5aa0e)

> 多模态大语言模型在自监督场景下难以获取高质量偏好数据，标准直接偏好优化（Direct Preference Optimization, DPO）因自动生成的“优选”响应未必优于“劣选”响应而陷入监督噪声。Trident 通过引入中性锚点将二元偏好扩展为三元组结构，并设计自适应边际正则化目标，在无外部反馈条件下实现了对幻觉的有效抑制。该方法以极少的自生成数据达到了与依赖大规模人工标注或强模型反馈的方法相当的性能，但其对复杂视觉语义理解的提升能力仍存疑。

】
