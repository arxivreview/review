# ACL-Findings2026 · 序列建模的状态空间模型方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Rectified Sparse Attention for Efficient Long-Sequence Generation ｜修正稀疏注意力

作者：Yutao Sun、Tianzhu Ye、Li Dong 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8e716de139dd)

> 长序列生成中，标准自注意力机制因需访问完整键值缓存（KV Cache）导致内存带宽成为推理瓶颈，而现有稀疏解码方法虽降低计算量，却因近似误差在缓存中累积导致生成质量随长度增加而显著退化。本文切入点在于识别出“误差累积”是稀疏解码失效的根本原因，而非单纯的检索精度不足。通过引入周期性稠密修正机制，在保持稀疏检索效率的同时将误差约束在常数窗口内。该方法在256K上下文长度下实现3.77倍端到端加速，且数学推理性能接近稠密基线，但其“近无损”结论仅验证于特定模型规模与任务类型，对复杂状态跟踪任务的泛化能力存疑。

】

---

【SepSeq: A Training-Free Framework for Long Numerical Sequence Processing in LLMs ｜分离序列（SepSeq）：基于注意力汇聚的长数值序列处理框架

研究机构：中国科学技术大学、南京大学

作者：Jie Sun、Yu Liu、Lu Han 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cb947e2438ef)

> 导读 Transformer大语言模型在处理长数值序列时，因Softmax机制导致注意力权重在大量相似Token间稀释，无法精确访问局部值，造成计数、过滤等精度敏感任务性能崩塌。现有扩展上下文窗口或引入外部工具的方法未能解决模型对原始序列的忠实保持瓶颈，本文切入点在于识别“注意力分散”为根本原因。SepSeq通过无训练地在序列中定期插入分隔符Token，将其作为注意力汇聚点，将长序列切分为短片段以重构注意力分布。该框架在9个主流LLM上平均提升35.6%准确率并减少16.4%推理Token消耗，但其效果依赖于模型对分隔符的内在注意力偏好，且未验证其在非Transformer架构中的普适性。

】

---

【StateX: Enhancing RNN Recall via Post-training State Expansion ｜状态扩展后训练

研究机构：清华大学

作者：Xingyu Shen、Yingfa Chen、Zhen Leng Thai 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.22630)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.22630)

> 递归神经网络（RNN）在处理长上下文时，因将全部历史信息压缩至固定大小的隐状态，导致精确召回能力显著弱于Transformer。现有扩大状态维度的方案要么从头训练成本高昂，要么引入复杂新架构难以集成，而本文切入点在于利用预训练模型，通过低成本的后训练阶段直接扩展状态尺寸。StateX针对线性注意力与状态空间模型设计了两种无参数或低参数增加的状态扩展机制，并在1.3B规模模型上验证了其有效性。该方法以极低的额外训练成本显著提升了长上下文召回性能，但其效果是否能在更大规模或混合架构中保持，仍存疑。

】
