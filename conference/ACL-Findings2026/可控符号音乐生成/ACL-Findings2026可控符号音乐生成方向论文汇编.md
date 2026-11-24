# ACL-Findings2026 · 可控符号音乐生成方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Anchored Cyclic Generation: A Novel Paradigm for Long-Sequence Symbolic Music Generation ｜锚定循环生成：长序列符号音乐生成的误差抑制范式

研究机构：华南理工大学

作者：Boyu Cao、Lekai Qian、Dehan Li 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.05343)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05343)

> 长序列符号音乐生成面临自回归模型固有的误差累积问题，导致结构断裂与质量退化。现有层级架构虽能捕捉全局依赖，但缺乏对生成过程中偏差的实时校准机制，而扩散模型则受限于多步采样的高计算开销。本文提出锚定循环生成（Anchored Cyclic Generation, ACG）范式，通过引入已确定内容作为锚点特征重新校准后续生成，并构建分层框架Hi-ACG实现从全局结构到局部细节的逐级细化。该方法在缓解误差累积方面展现出显著优势，但其对非周期性音乐结构的适应性及与最新SOTA的差距仍需进一步验证。

】

---

【Muse: Towards Reproducible Long-Form Song Generation with Fine-Grained Style Control ｜可复现的长曲生成与分段风格控制

研究机构：复旦大学

作者：Changhao Jiang、Jiahao Chen、Zhenghao Xiang 等 17 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3acc99339203)

> 长曲生成旨在产出包含人声、歌词与完整结构的分钟级音频，核心难点在于维持长程时序一致性并实现细粒度风格操控。现有学术系统因版权限制缺乏公开训练数据，导致性能不可验证且对比不公平，商业系统则封闭于专有API。本文通过构建11.6万首全授权合成歌曲数据集，并采用单阶段监督微调训练基于Qwen的音频语言模型，实现了开源条件下的分段级风格控制。该工作解决了领域可复现性瓶颈，但其性能上限受限于合成数据的分布偏差，且未探索推理时干预机制。

】
