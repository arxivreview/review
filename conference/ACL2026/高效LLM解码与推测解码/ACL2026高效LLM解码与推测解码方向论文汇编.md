# ACL2026 · 高效LLM解码与推测解码方向论文汇编

> 本方向共 3 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AdaFuse: Adaptive Ensemble Decoding for Large Language Models ｜自适应词级集成解码

研究机构：美国伊利诺伊大学厄巴纳-香槟分校、OpenAI

作者：Chengming Cui、Tianxin Wei、Ziyi Chen 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dac701a16cea)

> 推理时集成旨在通过组合多个大语言模型（LLM）的互补优势提升生成质量，但现有方法受限于固定融合粒度，无法在生成过程中动态适应语义上下文与不确定性变化。ADAFUSE 提出以词为基本单元，利用首 Token 置信度阈值动态决定融合边界，并在不确定状态下触发多样性搜索以增强候选池。该方法在开放域问答、算术推理及机器翻译任务上，相比最强集成基线实现了 6.88% 的平均相对提升。尽管在 GSM8K 等推理任务上未超越最强单模型，但其自适应机制在异构模型融合中展现了显著的纠错潜力，其效率-质量权衡仍需进一步验证。

】

---

【CreditDecoding: Accelerating Parallel Decoding in Diffusion Large Language Models with Trace Credit ｜轨迹信用解码

研究机构：上海交通大学、西湖大学

作者：Kangyu Wang、Zhiyun Jiang、Haibo Feng 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.06133)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.06133)

> 扩散语言模型（dLLMs）在并行解码中面临“计算冗余”与“历史无关”的双重瓶颈，导致正确令牌因瞬时置信度不足被反复重掩码。现有阈值解码策略仅依赖当前步Logits，忽略了去噪过程中置信度的时间一致性，造成大量无效迭代。本文提出CreditDecoding，通过累积历史Logits构建轨迹信用（Trace Credit）作为先验，融合至当前Logits以提升置信度。该方法免训练，在LLaDA-8B-Instruct上实现5.48倍加速并提升0.48分准确率，但其在长上下文下的稳定性及与KV缓存优化的协同效应仍需进一步验证。

】

---

【Diving into the Decoding Space of Non-Autoregressive Models via Lexically Constrained Search ｜非自回归模型解码空间分析：基于词汇约束搜索的 LexMAP 算法

研究机构：加拿大阿尔伯塔大学

作者：Chenyang Huang、Osmar Zaiane

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_eb8bfdd0f6a4)

> 导读 自回归模型在受限生成任务中虽能精确控制输出，但其顺序依赖导致搜索空间呈网格状，难以高效处理大规模约束。现有非自回归方法多采用贪心迭代编辑，缺乏对搜索空间结构的系统性洞察，无法与自回归模型在同等约束下进行公平对比。本文提出基于动态规划的 LexMAP 算法，利用有向无环 Transformer 的独立预测特性，在词汇约束机器翻译中实现了全约束覆盖与竞争性 BLEU 分数。该工作揭示了非自回归解码在概率质量累积与位置偏差上的独特优势，但其在神经指标上的劣势表明，效率与质量的权衡仍未完全解决。

】
