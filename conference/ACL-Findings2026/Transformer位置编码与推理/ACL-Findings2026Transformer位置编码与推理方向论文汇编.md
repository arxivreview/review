# ACL-Findings2026 · Transformer位置编码与推理方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【LayerNorm Induces Recency Bias in Transformer Decoders ｜LayerNorm 诱导的近因偏差机制分析

研究机构：韩国科学技术院、微软研究院

作者：Junu Kim、Xiao Liu、Zhenghao Lin 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.21042)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.21042)

> 导读 Transformer 解码器中位置信息的来源长期被归因于显式位置编码（Positional Encoding, PE）或因果掩码，但实际模型中普遍存在的近因偏差（Recency Bias）与纯因果掩码理论预测的早期偏差相矛盾。现有理论未能解释这一矛盾，本文切入点在于剥离 PE，单独考察 LayerNorm 与因果自注意力的交互作用。通过理论推导与无参数模拟，证明 LayerNorm 是诱导近因偏差的关键架构组件。该发现修正了隐式位置信息的来源认知，但缺乏在真实预训练模型中的实证验证，其理论结论对实际性能的影响尚存疑。

】

---

【Mitigating Position Bias in Transformers via Layer-Specific Positional Embedding Scaling ｜层特定位置嵌入缩放

研究机构：复旦大学、西湖大学

作者：Zhenghua Wang、Yiran Ding、Changze Lv 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_df706e093bae)

> 长上下文大语言模型普遍存在“中间迷失”现象，即模型对序列首尾信息的注意力显著高于中间部分，导致关键信息被忽略。现有缓解方案如多基线集成或头级缩放虽能改善注意力分布，但需多次前向传播，带来高昂的推理延迟。本文提出层特定位置嵌入缩放（Layer-Specific Positional Embedding Scaling, LPES），通过为每层分配独立的RoPE缩放因子并引入贝塞尔曲线约束的遗传算法进行自动搜索，在单次前向传播中实现注意力均衡。该方法在关键值检索任务上取得最高11.2%的准确率提升，但其效果依赖于特定数据集的预搜索，且未验证其在复杂推理任务中的泛化边界。

】
