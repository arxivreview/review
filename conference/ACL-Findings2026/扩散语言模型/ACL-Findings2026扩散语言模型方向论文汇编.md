# ACL-Findings2026 · 扩散语言模型方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Leveraging Pretrained Language Models as Energy Functions for Glauber Dynamics Text Diffusion ｜基于Glauber动力学的离散扩散语言模型

研究机构：美国俄亥俄州立大学

作者：Tarun Kathuria、Sachin Kumar

论文原文见 [arXiv](https://arxiv.org/abs/2605.04291)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.04291)

> 离散扩散语言模型（DLMs）旨在通过并行去噪突破自回归（AR）模型的串行延迟瓶颈，但现有掩码扩散范式因前向过程缺陷难以超越AR模型的质量上限。本文指出，将预训练语言模型作为能量函数嵌入Glauber动力学，能显著拉近噪声分布与数据分布的距离，从而解决离散扩散训练样本效率低下的核心痛点。该方法通过UL2架构实现因果生成与掩码填充的统一，在GPT-2规模下实现了与AR模型相当的生成困惑度。尽管其推理速度较慢，但在同等计算预算下，其单位算力产生的文本质量优于AR模型，为离散扩散提供了理论更严谨的替代路径。

】

---

【One Token Is Enough: Improving Diffusion Language Models with a Sink Token ｜固定注意力汇聚点：扩散语言模型的稳定性修正

作者：Zihou Zhang、Zheyong Xie、Li Zhong 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.19657)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.19657)

> 扩散语言模型（DLMs）在并行解码中面临注意力汇聚点位置随去噪步长漂移的“移动汇聚点”问题，导致推理过程缺乏稳定锚点，进而限制模型性能上限。现有加速或优化方法多聚焦于采样步数或KV缓存，忽视了注意力机制内部的信息混合失控这一底层动力学缺陷。本文通过引入一个仅自注意且全局可见的额外Sink Token，将不稳定的移动汇聚点转化为位置固定的结构锚点。该方案以极低的计算开销实现了跨规模、跨初始化策略的性能提升，但其有效性是否依赖于特定模型规模或长序列场景，仍存疑。

】

---

【SDAR: A Synergistic Diffusion-AutoRegression Paradigm for Scalable Sequence Generation ｜协同扩散-自回归范式

研究机构：浙江大学、美国马里兰大学帕克分校

作者：Shuang Cheng、Yihan Bian、Dawei Liu 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.06303)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.06303)

> 扩散语言模型（DLMs）旨在通过并行解码突破自回归（AR）模型的串行延迟瓶颈，但受限于证据下界（ELBO）训练目标收敛缓慢及缺乏键值（KV）缓存导致的 $O(N^3)$ 推理复杂度，难以在大规模场景落地。现有混合架构虽尝试结合两者优势，却因端到端联合训练带来的算力开销激增而缺乏实用性。本文提出 SDAR，通过解耦训练与推理阶段，利用轻量级适配将预训练 AR 模型转换为块扩散模型，在保留 AR 训练效率的同时实现块内并行生成。该范式在 30B 规模下展现出与 AR 模型相当的推理能力，并因局部双向注意力在科学推理任务上取得优势，但其性能增益是否完全源于架构转换而非数据适配，仍需更严格的隔离实验验证。

】
