# ICLR2026 · KV缓存压缩与管理方向论文汇编

> 本方向共 12 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Beyond Speedup -- Utilizing KV Cache for Sampling and Reasoning ｜键值缓存语义复用

研究机构：香港中文大学、华为

作者：Zeyu Xing、Xing Li、Hui-Ling Zhen 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.20326)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.20326)

> 大语言模型推理中，键值缓存（KV Cache）长期仅作为加速自回归解码的中间状态，其蕴含的上下文语义信息未被利用。现有自评估与自适应推理方法依赖存储完整隐藏状态，导致显存与计算开销激增，无法在生产环境中实时部署。本文切入点在于证明KV缓存本身已包含足够的局部轨迹几何与难度信号，通过零成本池化即可替代隐藏状态。具体做法是构建基于KV缓存的嵌入轨迹（KV-CoE）与难度分类器（KVClassifier），实现自评估与快慢思维切换。该工作验证了KV缓存作为“免费表示”的可行性，但其通用嵌入能力有限，且未探讨与压缩策略的协同效应。

】

---

【Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs ｜基于内在重要性的Token保留机制

研究机构：美国耶鲁大学、韩国光州科学技术院

作者：Ngoc Bui、Shubham Sharma、Simran Lamba 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.03324)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.03324)

> 长上下文推理中，键值缓存（KV Cache）随序列长度线性增长，导致显存溢出与延迟瓶颈。现有驱逐策略依赖瞬时注意力分数作为重要性的代理指标，在长思维链生成中因注意力滞后与偏差导致关键Token被过早丢弃。本文提出TRIM-KV，通过轻量级保留门在Token创建时预测其内在重要性，并随时间指数衰减以驱动驱逐。该方法在低内存预算下显著优于启发式基线，但高预算下的性能增益及跨任务泛化能力仍存疑。

】

---

【CHANNEL-AWARE MIXED-PRECISION QUANTIZATION FOR EFFICIENT LONG-CONTEXT INFERENCE ｜通道感知混合精度量化

研究机构：香港科技大学

作者：Chengxi Liao、Zeyi Wen

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_91255932)

> 长上下文推理中，键值缓存（KV Cache）的线性增长导致显存溢出，而现有低比特量化方法在2-bit配置下因忽略通道敏感度差异，导致检索性能严重退化。本文切入点在于发现Key缓存中存在对检索任务极度敏感的特定通道，提出通道感知的混合精度量化框架。通过K-means聚类与检索掩码识别敏感通道，动态分配4/3/1比特精度，在RULER基准上实现至少5个点的绝对提升。该方法在长上下文检索场景下显著优于均匀量化基线，但其检索通道检测依赖离线构造的特定提示，在线动态适应性存疑。

】

---

【FASA: FREQUENCY-AWARE SPARSE ATTENTION ｜频率感知稀疏注意力

研究机构：阿里巴巴集团、美国加州大学圣迭戈分校

作者：Yifei Wang、Yueqi Wang、Zhenrui Yue 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.03152)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_35581973)

> 长上下文推理中，键值缓存（KV Cache）的线性增长导致解码阶段受限于内存带宽而非算力，成为吞吐量瓶颈。现有Token驱逐策略要么采用静态规则导致信息不可逆丢失，要么依赖历史注意力分数存在滞后性，无法实现真正的查询感知。本文切入点在于发现旋转位置编码（RoPE）中频率块（Frequency Chunk, FC）的功能稀疏性，即仅少数主导FC承载语义信息，其余仅构建位置模式。FASA利用这一特性，通过离线校准主导FC集合，在解码时仅聚合这些FC的分数来动态预测Token重要性，实现无训练、查询感知的驱逐。该方法在LongBench上以256 Token预算达到接近全缓存的性能，但在极端分布外数据上的鲁棒性尚待验证。

】

---

【IceCache: Memory-efficient KV-cache Management for Long-Sequence LLMs ｜IceCache：基于语义聚类的动态KV缓存卸载管理

研究机构：加拿大西蒙弗雷泽大学、美国哈佛大学

作者：Yuzhen Mao、Qitong Wang、Martin Ester 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.10539)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10539)

> 长上下文推理中，键值缓存（KV Cache）随序列线性增长导致GPU显存溢出，现有卸载方法因静态分页与缺乏动态更新机制，在长生成任务中检索命中率低且性能退化。本文切入点在于将语义聚类引入分页存储，通过层级索引结构实现动态维护与高效检索。具体做法是构建DCI-tree将语义相似Token映射至同一物理页，结合CPU-GPU流水线重叠隐藏延迟。该方法在256 Token预算下保持99%精度，但依赖CPU内存充足假设，且未验证低带宽硬件下的延迟收益。

】

---

【KV Cache Transform Coding for Compact Storage in LLM Inference ｜KV缓存变换编码

研究机构：波兰华沙大学

作者：Konrad Staniszewski、Adrian Łańcucki

论文原文见 [arXiv](https://arxiv.org/abs/2511.01815)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.01815)

> 导读 大语言模型（LLM）多轮对话中，键值缓存（KV Cache）的复用面临存储与传输瓶颈，现有运行时压缩方法因实时性约束难以兼顾高压缩率与精度。本文切入点在于将经典图像压缩中的变换编码框架迁移至KV缓存存储场景，通过一次性校准的PCA去相关、动态比特分配与熵编码，实现离线/异步压缩。该方法在保持推理精度的同时，将16位KV缓存平均压缩20倍，为缓存分层存储与跨节点传输提供了低延迟代价的解决方案，但其对在线推理延迟的影响及与驱逐策略的组合效果仍需进一步验证。

】

---

【LouisKV: Efficient KV Cache Retrieval for Long Input-Output Sequences ｜基于时间局部性的解耦式KV缓存检索框架

研究机构：北京大学、华为

作者：Wenbo Wu、Qingyi Si、Xiurui Pan 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.11292)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.11292)

> 长序列推理中，键值缓存（KV Cache）的线性增长导致GPU显存溢出，现有检索方法因逐Token触发和粗粒度分页管理，在长输出场景下面临高昂的传输开销与精度损失。LouisKV利用关键KV访问的时间局部性，将检索触发从每Token粒度降至语义片段边界，并通过输入聚类与输出分段的解耦管理提升检索精度。该框架在保持近无损精度的同时实现了最高4.7倍的端到端延迟加速，但其对Query相似度阈值的依赖及未覆盖量化基线的评估边界仍存疑。

】

---

【Mixing Importance with Diversity: Joint Optimization for KV Cache Compression in Large Vision-Language Models ｜混合重要性与多样性：大型视觉语言模型KV缓存压缩的联合优化

研究机构：上海交通大学、四川大学

作者：Xuyang Liu、Xiyan Gui、Yuchao Zhang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.20707)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.20707)

> 大型视觉语言模型（LVLM）处理高分辨率图像或长视频时，键值缓存（KV Cache）的线性增长导致显存溢出，成为部署瓶颈。现有驱逐策略仅依据注意力分数保留“重要”Token，忽略了多模态输入中视觉Token的高语义冗余，导致压缩后的缓存覆盖不全。本文提出MixKV，通过量化每个注意力头内的语义冗余度，自适应地平衡重要性评分与多样性评分，在保留关键信息的同时最大化语义覆盖。该方法在极端压缩预算下平均提升基线5.1%，但在纯文本任务中收益有限，且未对比量化类方法，其相对于低比特量化的绝对优势尚存疑。

】

---

【PM-KVQ: PROGRESSIVE MIXED PRECISION KV CACHE QUANTIZATION FOR LONG-COT LLMS ｜渐进混合精度键值缓存量化

研究机构：清华大学、美国哥伦比亚大学

作者：Tengxuan Liu、Shiyao Li、Jiayi Yang 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_56899977)

> 长思维链（Long-CoT）推理模型在生成数万Token时，键值缓存（KV Cache）的显存占用远超模型权重，成为部署瓶颈。现有短上下文量化方法直接应用于长序列时，因量化误差随解码步数累积及校准数据分布偏差导致性能严重退化。PM-KVQ通过渐进式比特位宽缩减、基于敏感度的块级内存分配及位置插值校准，在同等显存预算下显著提升了低比特量化下的推理精度。该方法在7B至70B模型上实现了最高8%的精度提升，但其有效性依赖于对Transformer标准架构的假设，未覆盖低秩注意力等新型架构。

】

---

【PROTOKV: LONG CONTEXT KNOWLEDGES ARE AL READY WELL-ORGANIZED BEFORE YOUR QUERY ｜语义锚点驱动的KV缓存原型压缩

研究机构：南京大学、复旦大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_93298219)

> 长上下文推理中，键值缓存（KV Cache）的线性增长导致显存溢出，现有驱逐策略因孤立评估Token重要性而破坏语义完整性。本文发现Key嵌入空间中少数“语义锚点Token”（SAT）具有局部偏差属性并自发聚类，提出ProtoKV算法，通过混合语义原型构建与观察窗口选择机制，在保持语义连贯性的同时实现高效压缩。该方法在LongBench上平均提升2.11%，但在长思维链任务中的累积误差控制能力尚待验证。

】

---

【REST-KV: ROBUST KV CACHE EVICTION WITH - LAYER WISE OUTPUT RECONSTRUCTION AND SPATIAL-TEMPORAL SMOOTHING ｜层级输出重构与时空平滑的KV缓存驱逐

研究机构：中国科学院、中国科学院大学

作者：Yongqi An、Chang Lu、Kuan Zhu 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_63271124)

> 长上下文推理中，键值缓存（KV Cache）驱逐策略面临的核心困境是：基于静态注意力权重的Token重要性评估无法捕捉移除Token后引发的注意力重分配效应，导致在低缓存预算下关键信息被误删。现有方法如SnapKV和H2O仅依赖Query-Key相似度或累积注意力分数，忽略了Value向量对输出的实际贡献及空间-时间动态变化。ReST-KV将驱逐问题重构为层级输出最小化重构损失，并引入指数移动平均（EMA）与自适应窗口（AWS）平滑机制，以隐式建模注意力重分配。该方法在RULER基准上较基线提升15.2%，但在纯驱逐路线内验证，未与量化方法同协议对比，其相对于数值压缩路线的绝对优势仍存疑。

】

---

【ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models ｜思维自适应KV缓存压缩

研究机构：美国佐治亚理工学院、英伟达研究院

作者：Akshat Ramachandran、Marina Neseem、Charbel Sakr 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.01290)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.01290)

> 大推理模型（LRM）在生成数千Token的思维链时，键值缓存（KV Cache）的线性增长导致显存溢出，成为长输出推理的核心瓶颈。现有压缩方法多聚焦于预填充阶段或采用Token级贪心驱逐，忽略了推理过程中的语义结构差异，导致高精度压缩下准确率显著下降。本文提出ThinKV，通过注意力稀疏度分解思维类型，实施思维自适应量化与驱逐，并设计连续思考内核消除内存碎片。该框架在低于5%的原始KV缓存预算下实现了近乎无损的推理精度，但其思维类型定义的泛化性在跨模型场景下仍存疑。

】
