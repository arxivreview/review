# ACL-Findings2026 · 高效LLM解码与推测解码方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Breaking the Autoregressive Chain: Hyper-Parallel Decoding for Efficient LLM-Based Attribute Value Extraction ｜超并行解码

研究机构：加拿大麦吉尔大学、加拿大魁北克人工智能研究所

作者：Theodore Glavas、Nikhita Vedula、Dushyanta Dhyani 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.26209)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.26209)

> 属性值提取（Attribute Value Extraction, AVE）任务中，多个属性值的生成在给定文档上下文时具有条件独立性，但标准自回归解码强制将其串行化，导致离线批量推理吞吐量受限。现有投机解码受限于草稿质量与验证开销，无法充分利用这种结构独立性。本文通过操纵位置ID与注意力掩码，实现非连续令牌的并行生成，在保持输出质量的前提下将推理成本降低至13.8倍。该方案在特定结构化任务上有效，但其对属性长度分布的依赖性及位置编码外推误差的影响尚存疑。

】

---

【LLM-Codec: Neural Audio Codec Meets Language Model Objectives ｜语音编码器的目标错位：从重建保真到语言模型可预测性

研究机构：国立台湾大学、新加坡南洋理工大学

作者：Ho-Lam Chung、Yiming Chen、Hung-yi Lee

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_81b8293f3d1d)

> 语音语言模型（SLM）依赖离散音频令牌进行自回归生成，但现有神经音频编码器为波形重建优化，导致令牌空间充满声学噪声，使语言模型困惑度居高不下。本文指出重建目标与预测目标的根本错位是SLM性能瓶颈，而非模型容量不足。通过引入未来令牌预测与语义对齐正则项，在保持编码器架构不变的前提下重塑令牌分布。该方法在语音连贯性基准上取得61.6%准确率，困惑度降低35倍，但仅验证了语音域，非语音音频的泛化能力存疑。

】
