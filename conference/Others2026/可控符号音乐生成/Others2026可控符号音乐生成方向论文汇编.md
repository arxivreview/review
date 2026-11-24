# Others2026 · 可控符号音乐生成方向论文汇编

> 本方向共 1 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【融合记忆与注意力：LSTM、Transformer 及混合架构在符号音乐生成中的对比研究

作者：Soudeep Ghoshal、Sandipan Chakraborty、Pradipto Chowdhury 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.21282)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.21282)

> 符号音乐生成需同时捕捉局部旋律细节与全局结构连贯性，但现有单一架构往往顾此失彼：LSTM 擅长局部连贯却丢失长程依赖，Transformer 能建模全局结构却缺乏低层节奏细腻度。本文切入点在于系统量化这两种架构在 17 项局部与全局音乐指标上的互补性，并验证混合架构能否同时优化两端。具体做法是构建 Transformer 编码器与 LSTM 解码器的混合模型，在 Deutschl 数据集上生成 1,000 首旋律进行对比评估。该研究验证了混合架构在感知质量上的优势，但其基于固定短序列（64 步）的实验设置限制了结论向长序列场景的泛化，且缺乏与当前主流高效 Transformer 基线的直接对比。

】
