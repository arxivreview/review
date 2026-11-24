# ACL-Findings2026 · 文本嵌入模型与表示方向论文汇编

> 本方向共 7 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【An LLM-Embedding Semantic Adaptation Network for Post-level Semantic Drift Evaluation ｜基于LLM嵌入与图卷积的帖子级语义漂移评估

研究机构：中国科学技术大学

作者：Ning Chen、Mingyu Kang、Jie Li 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5e041d9b3f56)

> 语义漂移评估旨在量化在线讨论中事件相关帖子随时间发生的动态语义变化，但事件关键词的稀疏与非均匀分布导致传统模型难以捕捉帖子级的细粒度漂移。现有方法多停留在时间或事件粒度，无法处理快速演变的单帖内容。本文提出LLM-SAN，通过冻结LLM提取嵌入，结合GRU时序建模与GCN话题增强，利用重构误差检测漂移点。该方法在中文新闻基准上实现了SOTA性能，但其依赖单一数据集且未验证跨语言泛化能力，评估边界受限。

】

---

【Embedding-based In-Context Prompt Training for Enhancing LLMs as Text Encoders ｜嵌入基上下文提示训练

研究机构：日本东京科学大学

作者：Ailiang Lin、Zhuoyun Li、Keyu Mao 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3d4c1ff535b3)

> 导读 文本嵌入模型在检索增强生成（RAG）等场景中需平衡语义精度与推理延迟，而基于大语言模型（LLM）的嵌入方法常因引入离散文本演示导致序列长度膨胀，显著增加计算开销。现有方案或牺牲精度换取速度，或依赖双向注意力改造破坏LLM原生指令跟随能力，难以兼顾效率与表示质量。本文提出EPIC，将离散文本演示压缩为连续向量嵌入，在保留因果注意力的同时实现高效上下文学习。该方法在公开检索数据上刷新MTEB基准，但其在低资源语言及非检索任务上的泛化能力尚待验证。

】

---

【FLARE: Task-agnostic embedding model evaluation through a normalization process ｜基于归一化流的无标签嵌入模型评估

研究机构：香港科技大学

作者：Jingzhou Jiang、Yixuan Tang、Yi Yang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17344)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17344)

> 在专有语料库缺乏标注数据时，如何可靠地预测文本嵌入模型的下游任务排名？现有基于核密度估计或几何指标的无标签评估方法在高维空间中失效，导致排名与真实性能脱节。FLARE 通过引入归一化流（Normalizing Flows）精确估计信息充分性，将评估误差依赖从原始维度转移至内在维度，解决了高维密度估计的稳定性问题。该方法在11个数据集上实现了与监督基准高达0.90的Spearman相关系数，但在低维场景及跨语言泛化性上仍缺乏充分验证。

】

---

【Information Representation Fairness in Long-Document Embeddings: The Peculiar Interaction of Positional and Language Bias ｜长文档嵌入中的信息表示公平性

研究机构：瑞士苏黎世大学

作者：Elias Schuhmacher、Andrianos Michail、Juri Opitz 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.16934)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.16934)

> 长文档嵌入模型在检索任务中面临的核心矛盾是：单向量表示需同时承载多段独立信息的语义，但现有编码器倾向于过度表征文档前部内容，导致后部信息在语义空间中“不可见”。主流的双向注意力机制虽解决了全局语义捕获问题，却未消除位置与语言维度的系统性偏差，使得公平性成为被忽视的评估盲区。本文通过置换实验量化首段偏差，并提出一种无需训练的推理时注意力校准方法，将注意力质量均匀分配至不同位置区间。该方法在降低位置偏差方面有效，但仅验证了编码器模型，且未评估校准对通用检索精度的影响，其泛化边界尚存疑。

】

---

【LLMs Meet Isolation Kernel: Lightweight, Learning-free Binary Embeddings for Fast Retrieval ｜隔离核嵌入

研究机构：南京大学

作者：Zhibo Zhang、Yang Xu、Kai Ming Ting 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_14defabed7f3)

> 高维大语言模型（LLM）嵌入在大规模检索中面临存储与延迟瓶颈，现有压缩方法如马特罗什卡表示学习（MRL）和对比稀疏表示（CSR）虽能降低维度，但需高昂训练成本且存在精度损失。本文提出隔离核嵌入（IKE），一种无需训练的随机分区映射方法，将LLM向量转化为二进制索引以加速检索。IKE通过引入分区多样性准则，在保持检索精度的同时实现了显著的存储与速度优势，但其对复杂语义空间的适应性仍存疑。

】

---

【MTEB-NL and E5-NL: Embedding Benchmark and Models for Dutch ｜荷兰语嵌入基准与模型构建

研究机构：比利时安特卫普大学

作者：Nikolay Banar、Ehsan Lotfi、Jens Van Nooten 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2f9a1cb6e7a3)

> 荷兰语在通用多语言嵌入资源中占比极低，导致现有模型在该语言上性能受限且缺乏可靠的评估标准。主流多语言模型依赖英语或中文数据训练，难以捕捉荷兰语特有的语义结构，而现有荷兰语基准数据量小且许可受限。本文通过构建包含40个数据集的MTEB-NL基准，结合LLM合成数据扩充训练集，并基于E5架构进行词表适配与微调，旨在填补这一资源空白。该工作提供了低资源语言嵌入开发的完整资源包，但其性能上限受限于E5骨干网络及合成数据的质量，未探索更先进的双向化架构。

】

---

【PL-MTEB: Polish Massive Text Embedding Benchmark ｜波兰语文本嵌入基准

作者：Rafał Poświata、Sławomir Dadas、Michał Wiktor Perełkiewicz

论文原文见 [arXiv](https://arxiv.org/abs/2405.10138)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_34a951901fd6)

> 文本嵌入模型在低资源语言上的性能评估长期缺乏统一标准，导致模型选择依赖单一任务或存在数据泄露风险。现有通用基准如 MTEB 主要覆盖英语，无法有效区分多语言模型在特定语言上的真实泛化能力。本文构建了包含 30 个任务的波兰语专用基准 PL-MTEB，通过引入零样本评估指标量化数据重叠度，系统评估了 30 个主流嵌入模型。该工作填补了波兰语评估空白，但受限于仅覆盖单一语言，其结论对更广泛低资源语言的普适性存疑。

】
