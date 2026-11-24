# ACL-Findings2026 · KV缓存压缩与管理方向论文汇编

> 本方向共 7 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【HqeKV: Towards Hybrid Quantization and Eviction for KV Cache in Long-Context LLM Inference ｜HqeKV：混合量化与驱逐的协同优化框架

研究机构：美国东北大学

作者：He Wang、Yu Gu、Fangfang Li 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_22fd1e0098b0)

> 长上下文大语言模型推理中，键值缓存（KV Cache）的线性增长导致显存溢出，现有单一量化或驱逐策略因压缩粒度粗糙及重要性评估偏差，难以在固定内存预算下最大化生成质量。HqeKV 提出一种混合压缩框架，通过联合 K-V 重要性指标与分比特宽度量化策略，将缓存对分配至 FP16、4-bit、2-bit、1-bit 及驱逐五种状态。该方法在相同内存约束下将 LongBench 平均准确率从 40.53 提升至 49.98，但其离线搜索依赖校准集，在线自适应能力存疑。

】

---

【LycheeCluster: Efficient Long-Context Inference with Structure-Aware Chunking and Hierarchical KV Indexing ｜结构感知分块与层级索引的长上下文推理加速

研究机构：哈尔滨工业大学、电子科技大学

作者：Dongfang Li、Zixuan Liu、Gang Lin 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.08453)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.08453)

> 长上下文解码受限于键值缓存（KV Cache）的内存带宽瓶颈，现有检索式方法因固定分页或Token聚类破坏语义完整性，导致检索预算浪费。LycheeCluster通过结构感知分块保留局部连贯性，并构建基于三角不等式的层级索引实现对数时间剪枝。该方法在保持精度接近全注意力的同时，将解码延迟降低至原速度的1/3.6。其核心假设——语义连贯块优于固定页或孤立Token——在结构化数据任务上得到验证，但在通用文本中的普适性及与驱逐式方法的内存效率对比尚存疑。

】

---

【MM-ShiftKV: Decode-Aware Prefill-Stage KV Selection for Multimodal Large Language Models ｜解码感知预填充键值选择

研究机构：浙江大学

作者：Jinsong Shu、Chenyang Wu、Zhongle Xie 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.22586)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.22586)

> 多模态大语言模型（MLLM）推理中，预填充阶段构建的键值缓存（KV Cache）因视觉Token数量庞大而成为显存瓶颈。现有预填充阶段KV选择方法隐含假设预填充统计量可代表解码阶段查询分布，但在多模态场景下该假设失效，导致紧预算下关键视觉Token被误删。MM-ShiftKV通过构建方差扩展的解码感知查询代理，在预填充阶段一次性校准重要性估计。该方法在严格预算下显著优于现有基线，但其固定超参对模态比例的敏感性尚未验证。

】

---

【OjaKV: Context-Aware Online Low-Rank KV Cache Compression ｜在线低秩键值缓存压缩

研究机构：美国伦斯勒理工学院、IBM研究院

作者：Yuxuan Zhu、David H. Yang、Mohammad Mohammadi Amiri 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.21623)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.21623)

> 长上下文推理中，键值缓存（KV Cache）随序列长度线性增长，导致显存溢出。现有低秩近似方法依赖静态离线学习的投影基，在推理时面对分布漂移会失效。OjaKV通过混合存储策略保留高误差Token的全秩表示，并利用Oja规则在线更新投影基，解决了静态基的适应性不足问题。该方法在生成任务上显著优于静态基线，但其绝对精度仍远低于量化与驱逐路线，且未与这些主流方法直接对比。

】

---

【StructKV: Preserving the Structural Skeleton for Scalable Long-Context Inference ｜结构感知键值缓存压缩

研究机构：中国科学院大学、北京大学

作者：Zhirui Chen、Peiyang Liu、Ling Shao

论文原文见 [arXiv](https://arxiv.org/abs/2604.06746)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ef0c1f5ffe4d)

> 长上下文推理中，预填充阶段的二次计算复杂度与解码阶段的线性内存增长构成双重瓶颈，现有方法往往在加速预填充时牺牲解码精度，或在压缩内存时忽略计算开销。本文指出，基于单层局部显著性的剪枝策略会误删跨层信息枢纽，导致长距离依赖丢失。StructKV 通过累积全局入度中心性识别语义骨架，并动态检测注意力稳定层，实现了计算预算与存储预算的解耦。该方法在LongBench和RULER上优于FastKV，但在极低比特量化场景下的表现未经验证，其纯驱逐策略在内存效率上可能不及量化方法。

】

---

【Towards Efficient Large Language Model Serving: A Survey on System-Aware KV Cache Optimization ｜系统感知的大语言模型键值缓存基础设施

研究机构：澳大利亚墨尔本大学、华中科技大学

作者：Jiantong Jiang、Peiyu Yang、Rui Zhang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.08057)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.08057)

> 大语言模型（LLM）推理服务面临键值缓存（KV Cache）随序列长度线性增长导致的显存溢出与内存带宽瓶颈，现有算法级压缩方法（如驱逐、量化）往往孤立优化单一指标，忽视了系统层面的调度、放置与表示协同。本文提出系统感知的大语言模型键值缓存基础设施（sKis）框架，将KV优化重构为时间、空间、结构三维系统行为空间，通过行为-目标矩阵揭示不同优化策略对延迟、吞吐与内存的差异化影响。该框架提供了稳定的分析透镜，但缺乏统一基准下的端到端性能验证，其分类法是否掩盖了算法与系统实现的耦合效应仍存疑。

】

---

【Zipage: Maintain High Request Concurrency for LLM Reasoning through Compressed PagedAttention ｜压缩分页注意力

研究机构：北京交通大学

作者：Mengqi Liao、Lu Wang、Chaoyun Zhang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.08743)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.08743)

> 大语言模型推理服务在高并发长序列场景下，键值缓存（KV Cache）的线性增长导致显存溢出，成为限制吞吐量的核心瓶颈。现有算法级驱逐方法虽能降低内存占用，但无法与现代推理引擎的连续批处理及前缀缓存机制兼容，导致实际吞吐量低于全量缓存引擎。本文提出压缩分页注意力，将Token级KV驱逐与分页内存管理深度集成，通过混合调度与异步压缩实现高并发下的内存恒定。该方案在数学推理任务上实现了2.1倍提速并保留95%精度，但其对非RoPE架构及多模态场景的适用性尚未验证。

】
