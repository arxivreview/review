# ICLR2026 · 高效Transformer架构与训练方向论文汇编

> 本方向共 9 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CAN TRANSFORMERS REALLY DO IT ALL? ON THE COMPATIBILITY OF INDUCTIVE BIASES ACROSS TASKS ｜任务特异性归纳偏置优化

研究机构：瑞士洛桑联邦理工学院

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_60883527)

> 现有大语言模型架构在自然语言处理上表现优异，但在算术等算法任务上存在系统性失效，这引发了对Transformer通用归纳偏置有效性的质疑。主流改进方案多聚焦于注意力机制替换或位置编码调整，但缺乏对底层非线性函数与任务匹配度的系统性评估。本文提出一种两阶段架构优化方法，通过替换GeLU和Softmax为可学习样条函数，量化不同任务间归纳偏置的兼容性。该方法揭示了标准Transformer在算法任务上的显著次优性，但在语言建模中仅带来微幅提升，其价值在于挑战了“单一架构通吃”的假设，但任务特异性限制了其通用部署潜力。

】

---

【Completed Hyperparameter Transfer across Modules, Width, Depth, Batch and Duration ｜完成超参数迁移：跨模块、宽度、深度、批次与时长

研究机构：英国剑桥大学

作者：Bruno Mlodozeniec、Pierre Ablin、Louis Béthune 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.22382)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.22382)

> 大规模模型训练面临超参数（HPs）调优成本随规模指数级上升的困境，现有µP等参数化方法仅能迁移全局HPs，无法处理细粒度模块差异及批次/时长维度的缩放。本文提出Complete[(d)]P参数化，统一了宽度、深度、批次大小与训练时长的HPs迁移规则，并验证了Per-module HPs在约600倍FLOP预算下的直接迁移能力。该方法将50M模型上优化的Per-module HPs直接应用于7.2B模型，实现了1.32倍的训练加速，但其优势是否足以覆盖高维搜索的额外计算成本，以及在非Transformer架构中的泛化性仍存疑。

】

---

【Cutting the Skip: Training Residual-Free Transformers ｜无残差Transformer训练：基于Jacobian条件数的初始化策略

研究机构：新西兰奥克兰大学

作者：Yiping Ji、James Martens、Jianqiao Zheng 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.00345)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.00345)

> 深层Transformer依赖残差连接（Skip Connections）维持梯度流动，但残差连接破坏了表示的层级抽象，导致网络实际有效深度远低于名义深度。现有去除残差的方法要么修改架构导致硬件不兼容，要么收敛速度极慢。本文通过Jacobian分析发现残差连接本质上是正则化项，提出一种无需修改架构的初始化策略，使无残差Vision Transformer（ViT）在监督与自监督任务中达到甚至超越有残差基线。该方法证明了残差连接并非深度学习的必要组件，但其在超深层扩展中的稳定性仍存疑。

】

---

【Efficient Resource-Constrained Training of Transformers via Subspace Optimization ｜权重-激活子空间迭代

作者：Le-Trung Nguyen、Enzo Tartaglione、Van-Tam Nguyen

论文原文见 [arXiv](https://arxiv.org/abs/2510.09160)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.09160)

> 边缘设备上的Transformer微调受限于内存容量而非算力，传统方法仅压缩权重或忽略激活存储，导致反向传播时内存溢出。本文切入点在于发现微调过程中模型参数与激活特征均驻留在稳定的低维子空间内，据此提出权重-激活子空间迭代（Weight-Activation Subspace Iteration, WASI），通过联合低秩分解同时压缩权重与激活以控制信息损失。该方法在Raspberry Pi 5上将训练内存降低至多62倍，但其在长序列大语言模型上的泛化能力尚未验证。

】

---

【MeSH: Memory-as-State-Highways for Recursive Transformers ｜记忆作为状态高速公路

研究机构：阿里巴巴集团、浙江大学

作者：Chengting Yu、Xiaobo Shu、Yadao Wang 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.07739)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.07739)

> 递归Transformer通过权重共享解耦计算深度与参数深度，但在计算匹配下常因表征停滞与坍缩而落后于非递归模型。现有启发式状态传递机制仅缓解信息过载，无法解决核心块缺乏迭代位置感知导致的未分化计算问题。MeSH将隐式状态管理外化为显式记忆缓冲，通过动态读写路由器实现功能特化。该架构在1.4B规模下以33%更少的非嵌入参数实现了优于非递归基线的性能，但其路由机制在超大规模下的训练稳定性与计算开销边界尚待验证。

】

---

【TAMING CURVATURE: ARCHITECTURE WARM-UP FOR STABLE TRANSFORMER TRAINING ｜曲率驯服：基于架构预热的Transformer稳定训练

作者：Sameera Ramasinghe、Thalaiyasingam Ajanthan、Hadi Mohaghegh Dolatabadi 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_38777733)

> 大模型训练常因损失尖峰或发散浪费算力，现有稳定化手段多依赖经验性归一化，缺乏对优化器-架构协同动态的精确监控。本文切入点在于证明Hessian最大特征值（曲率）在训练中是慢变的，从而实现了十亿参数模型下的在线曲率追踪。通过冻结部分层权重为恒等映射来渐进增加有效深度，该方法在1B-3B参数规模下避免了基线模型的发散，并显著降低了损失尖峰频率。其价值在于将稳定性理论工程化，但受限于模型规模，未验证其在更大参数下的精度优势。

】

---

【Taming Curvature: Architecture Warm-Up for Stable Transformer Training ｜驯服曲率：通过架构预热实现稳定Transformer训练

作者：Sameera Ramasinghe、Ajanthan Thalaiyasingam、Hadi Mohaghegh Dolatabadi 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.16768)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.16768)

> 大模型训练常因损失尖峰或发散浪费算力，现有稳定化手段如QK-Norm仅针对注意力局部问题，缺乏对全局优化动态的监控。本文切入点在于将Edge of Stability (EoS) 理论中的曲率控制从离线分析转化为在线工程实践，通过Warm-started Power Iteration实时追踪预条件Hessian最大特征值，并据此动态调整网络有效深度。该方法在1B参数规模下显著降低了训练不稳定性，但其优势能否外推至更大规模及非递归架构仍存疑。

】

---

【The Effect of Attention Head Count on Transformer Approximation ｜注意力头数对Transformer近似效率的理论下界分析

研究机构：新加坡国立大学、北京大学

作者：Penghao Yu、Haotian Jiang、Zeyu Bao 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.06662)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.06662)

> 高效Transformer架构研究长期聚焦于降低计算复杂度或优化训练稳定性，但缺乏对结构超参数如何制约模型表达力的严格理论解释。现有近似理论多提供上界，无法量化“头数不足”带来的参数代价，导致实践中头数选择依赖启发式。本文通过构造稠密的广义D-检索任务族，首次证明当注意力头数小于目标内在维度时，参数量随序列长度呈指数增长。这一结果揭示了多头机制在信息解耦中的必要性，但分析局限于单层、无LayerNorm设置，其在深层实际网络中的普适性尚存疑。

】

---

【TNT: Improving Chunkwise Training for Test-Time Memorization ｜深度记忆模块的分层训练范式

研究机构：美国南加州大学、谷歌研究院

作者：Zeman Li、Ali Behrouz、Yuan Deng 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.07343)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.07343)

> 深度记忆模块（Deep Memory Modules）虽具备超越线性注意力的表达潜力，但受限于非线性递归导致的硬件利用率低下，训练效率远低于Transformer。现有方法被迫在“大分块保速度”与“小分块保精度”间做静态妥协，无法兼顾。TNT通过引入全局-局部分层记忆与周期性状态重置，将训练吞吐量与推理分辨率解耦，实现了17.37倍的训练加速并同步提升模型精度。该范式在150M参数规模下验证了可行性，但其优势能否迁移至更大规模模型仍存疑。

】
