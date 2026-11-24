# ICLR2026 · 高效长上下文Transformer架构方向论文汇编

> 本方向共 9 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【From Collapse to Control: Understanding and Extending Context Length in Emerging Hybrid Models via Universal Position Interpolation ｜通用位置插值

研究机构：美国伊利诺伊大学厄巴纳-香槟分校、IBM研究院

作者：Haochen Shen、Davis Wertheimer、Zheng Wang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_86224671)

> 混合Mamba-Transformer模型在超出训练窗口时性能崩溃，现有针对Transformer或纯Mamba的上下文长度扩展（CLE）方法无法直接迁移。本文发现崩溃根源并非位置编码失效，而是Mamba层中少数头部状态幅值失控增长。通过统一缩放Transformer旋转频率与Mamba时间步长，UPI以闭式解实现训练-free的外推。该方法填补了混合架构CLE的空白，但其对头部选择的依赖及在纯Mamba模型上的增益差异仍存疑。

】

---

【InfLLM-V2: Dense-Sparse Switchable Attention for Seamless Short-to-Long Adaptation ｜稠密-稀疏可切换注意力

研究机构：清华大学、哈尔滨工业大学

作者：Weilin Zhao、Zihan Zhou、Zhou Su 等 13 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.24663)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24663)

> 长序列处理中，标准Transformer的二次方计算复杂度与线性内存增长构成根本瓶颈，而现有可训练稀疏注意力方法在“短序列预训练、长序列微调”的标准工作流中暴露出架构不匹配与训练不稳定的缺陷。InfLLM-V2通过复用稠密注意力参数并统一稀疏模块，消除了从短到长序列转换时的分布偏移与额外参数开销。该框架在保持98.1%长上下文理解性能的同时，实现了4倍于稠密注意力的加速。其价值在于解决了稀疏架构与工业界主流预训练范式的兼容性问题，但固定稀疏率与纯稀疏路线在极长序列下的检索上限仍存疑。

】

---

【LEARNED META-TOKENS FOR LANGUAGE MODELING ｜学习元Token与元注意力机制

研究机构：美国宾夕法尼亚大学、IBM研究院

作者：Alok Shah、Khush Gupta、Keshav Ramji 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_95685666)

> 长上下文Transformer面临的核心矛盾是二次方计算复杂度与线性内存增长，导致模型无法在有限窗口内可靠检索远距离信息。现有稀疏注意力或递归架构往往牺牲精确检索能力，而位置编码的外推失效进一步加剧了长序列性能崩塌。本文切入点在于将上下文压缩内嵌于预训练过程，通过引入可学习的元Token（Meta-Tokens）及其专用的元注意力（Meta-Attention）层，使模型将历史上下文“缓存”在特定Token中，从而以内容驱动的方式替代纯位置依赖。该方法在152M参数模型上实现了2倍上下文窗口的泛化，但其在大规模真实语料上的检索精度及与动态稀疏机制的协同效应尚存疑。

】

---

【Long-Context Attention Benchmark: From Kernel Efficiency to Distributed Context Parallelism ｜长上下文注意力基准：从内核效率到分布式上下文并行

研究机构：南京大学、浙江大学

作者：Tao Bu、Qiangang Wang、Bowen Zeng 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.17896)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.17896)

> 长上下文训练面临计算与内存随序列长度二次方增长的瓶颈，现有研究分散于内核优化与分布式并行两条路线，但缺乏统一接口下的公平对比，导致研究者无法量化不同掩码模式与扩展规模下的真实性能权衡。LongCA-Bench 通过构建统一数据准备接口与模块化算子封装，系统评测了7种稠密内核、5种稀疏内核及5种分布式机制在14种掩码模式下的表现。该基准揭示了掩码类型对内核支持度的决定性影响及分布式通信在超大规模下的扩展瓶颈，为长上下文训练的系统选型提供了客观参考，但其仅关注吞吐量与内存指标，未关联模型精度，限制了其对端到端训练效果的直接指导意义。

】

---

【LycheeDecode: Accelerating Long-Context LLM Inference via Hybrid-Head Sparse Decoding ｜混合头稀疏解码

研究机构：哈尔滨工业大学

作者：Gang Lin、Dongfang Li、Zhuoen Chen 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.04541)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.04541)

> 长上下文大语言模型（LLM）推理面临键值缓存（KV Cache）内存线性膨胀与计算延迟激增的双重瓶颈，现有层级共享稀疏方法因忽略注意力头功能多样性导致精度损失。LycheeDecode 通过引入头级角色分工，将少量检索头用于动态识别关键 Token，多数稀疏头复用该集合进行高效计算，并利用 HardKuma 分布解决头类型识别的训练-推理差异。该方法在 128K 上下文下实现 2.7 倍端到端加速，但缺乏与最新动态稀疏 SOTA 的直接对比，其泛化性存疑。

】

---

【Scaling Attention via Feature Sparsity ｜稀疏特征注意力

研究机构：西安电子科技大学、美国石溪大学

作者：Yan Xie、Tiansheng Wen、Tangda Huang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.22300)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.22300)

> 长上下文Transformer受限于自注意力机制在序列长度增加时的二次方计算复杂度及键值缓存（KV Cache）内存线性膨胀。现有方案多聚焦于序列轴稀疏或线性递归，但前者牺牲检索精度，后者因固定状态导致信息遗忘。本文提出稀疏特征注意力（Sparse Feature Attention, SFA），通过沿特征轴稀疏化查询与键向量，在保留全Token覆盖的同时降低计算密度。该方法在GPT-2和Qwen3预训练中匹配稠密基线性能，但其在复杂语义任务上的泛化能力及与动态稀疏机制的兼容性仍存疑。

】

---

【SCALING LINEAR ATTENTION CAPACITY WITH SPARSE STATE EXPANSION ｜稀疏状态扩展（SSE）：线性注意力中的信息分类与容量解耦

研究机构：中国科学院、香港理工大学

作者：Yuqi Pan、Yongqi An、Zheng Li 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_25773893)

> 长上下文建模的核心矛盾在于，线性注意力通过固定尺寸状态实现恒定内存，却因信息过度压缩导致检索与推理能力崩塌。现有方案或依赖全注意力层保留精度，或简单扩大状态矩阵导致参数爆炸，均未能同时解决容量瓶颈与计算效率问题。本文提出将状态更新重构为信息分类过程，通过行稀疏选择与分区扩展机制，在参数不变的前提下提升状态容量。该设计在数学推理任务上超越了同规模Transformer，但在长上下文精确检索上仍落后于全注意力基线，其静态选择机制在动态语义场景下的鲁棒性存疑。

】

---

【Short window attention enables long-term memorization ｜短窗口注意力实现长程记忆

研究机构：奥地利林茨约翰·开普勒大学

作者：Loïc Cabannes、Maximilian Beck、Gergely Szilvasy 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.24552)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24552)

> 混合架构旨在结合滑动窗口注意力的局部精度与线性递归网络的恒定内存优势，以突破标准Transformer在长序列上的计算与内存瓶颈。然而，现有研究普遍认为增大滑动窗口能提升整体性能，却忽视了其对长程检索能力的潜在抑制。本文发现，在混合架构中，过长的滑动窗口会导致模型过度依赖局部注意力，从而削弱线性层的长程记忆训练。通过引入随机窗口大小训练策略，SWAX在保持短上下文推理能力的同时，显著提升了长序列的检索准确率。这一发现挑战了以验证困惑度为唯一优化目标的常规做法，但其结论主要基于1.4B至7B规模的小模型，在更大规模下的普适性尚存疑问。

】

---

【Understanding and Improving Length Generalization in Hierarchical Sparse Attention Models ｜层级稀疏注意力中的长度外推机制解析

研究机构：复旦大学、腾讯AI实验室

作者：Jiaqi Leng、Xiang Hu、Junxiong Wang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.17196)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.17196)

> 长上下文建模面临计算复杂度二次方增长与固定内存架构无法无损检索远端信息的矛盾。现有滑动窗口与状态空间模型虽能维持困惑度稳定，但牺牲了对任意历史片段的精确访问能力；而早期块稀疏方法在复杂检索任务上随长度增加性能急剧衰减。本文通过统一框架解构块稀疏注意力，指出非线性块编码器、CLS令牌解耦与旁路残差路径是实现极端长度外推的三个关键组件。该工作将4K训练长度的模型外推至32M tokens，但其在超大规模预训练数据分布下的泛化边界仍存疑。

】
