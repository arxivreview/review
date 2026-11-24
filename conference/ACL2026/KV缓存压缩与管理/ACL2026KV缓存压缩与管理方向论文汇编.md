# ACL2026 · KV缓存压缩与管理方向论文汇编

> 本方向共 5 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【HeteroCache: A Dynamic Retrieval Approach to Heterogeneous KV Cache Compression for Long-Context LLM Inference ｜异构头动态检索的KV缓存压缩

研究机构：浙江大学

作者：Zhiyuan Shi、Qibo Qiu、Feng Xue 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.13684)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.13684)

> 长上下文推理中，静态驱逐策略因不可逆丢弃导致注意力漂移下的精度损失，而现有动态方法又受困于粗粒度检索带来的高I/O开销。HeteroCache基于注意力头的时间异质性与层内冗余性，通过离线校准将头分为四类角色，并设计由Pivot头监控漂移触发的异步CPU-GPU检索机制，在保持细粒度压缩的同时隐藏I/O延迟。该方法在50%内存预算下接近全注意力精度，但离线校准的泛化边界与量化正交性未获充分验证。

】

---

【HybridKV: Hybrid KV Cache Compression for Efficient Multimodal Large Language Model Inference ｜混合键值缓存压缩

研究机构：浙江大学

作者：Bowen Zeng、Feiyang Ren、Jun Zhang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.05887)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05887)

> 多模态大语言模型（MLLM）推理中，视觉Token引发的键值缓存（KV Cache）线性增长导致显存溢出与解码延迟。现有压缩方法仅优化预算分配粒度，却忽视了注意力头部在静态与动态行为上的本质差异，导致激进驱逐或过度保留。HYBRIDKV通过文本中心稀疏度将头部分类为静态与动态，并分别采用剪枝与检索策略，在10%缓存预算下实现了7.9倍的显存节省与1.52倍的解码加速。该框架在极端压缩率下保持了生成质量，但其头部分类机制对任务依赖性的鲁棒性仍存疑。

】

---

【MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning ｜查询感知混合精度量化

研究机构：华南理工大学、北京航空航天大学

作者：Tao Zhang、Ziqian Zeng、Hao Peng 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.19206)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.19206)

> 长链思维推理模型在生成数万Token时，键值缓存（KV Cache）的线性增长导致显存溢出与带宽瓶颈，而现有低比特量化方法在2-bit极端压缩下因无法区分通道重要性，导致推理精度崩溃。本文指出，仅基于Key矩阵尺度分配比特位是低效的，因为高幅度Key若对应低幅度Query，对注意力输出影响甚微。MixKVQ通过引入查询感知显著性分数，动态分配BF16/INT4/INT2三级精度，在2.7-bit平均位宽下实现了接近全精度的推理性能。该方法在数学推理任务上显著优于固定精度基线，但其对多模态及非自回归架构的适用性尚未验证。

】

---

【The Pitfalls of KV Cache Compression ｜公平驱逐策略下的多指令遵循与系统提示泄露

研究机构：美国加州大学洛杉矶分校

作者：Alex Chen、Renato Geh、Aditya Grover 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.00231)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.00231)

> 导读 KV缓存压缩旨在通过牺牲少量精度换取推理效率，但现有方法在多指令场景下表现出不可预测的“选择性遗忘”，导致部分指令被完全忽略。本文指出标准驱逐策略存在指令级偏差，将压缩问题从全局精度优化转向指令公平性约束。通过引入按指令边界均衡保留率的公平压缩机制，该方法在70%驱逐率下显著降低了系统提示泄露率。这一视角揭示了效率-安全权衡中的隐藏成本，但其对量化压缩路线的适用性及长上下文下的精度边界仍存疑。

】

---

【ZoomR: Memory Efficient Reasoning through Multi-Granularity Key Value Retrieval ｜多粒度键值检索实现内存高效推理

研究机构：美国伦斯勒理工学院、IBM研究院

作者：David H. Yang、Yuxuan Zhu、Mohammad Mohammadi Amiri 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.10898)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10898)

> 长输出推理中，键值缓存（KV Cache）随生成序列线性增长，导致显存溢出与解码延迟激增。现有驱逐策略多针对预填充阶段的静态输入压缩，难以应对解码阶段动态生成内容的长程依赖丢失问题。ZoomR 通过微调模型生成段落级摘要，利用摘要键作为粗粒度索引，动态检索并加载关键细节段至 GPU，实现了显存与精度的平衡。该方法在 AIME2025 上接近全缓存性能，但牺牲了吞吐量，且依赖额外的微调步骤。

】
