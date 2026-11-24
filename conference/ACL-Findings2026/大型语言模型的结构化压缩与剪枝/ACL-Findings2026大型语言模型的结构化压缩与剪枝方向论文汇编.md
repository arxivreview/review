# ACL-Findings2026 · 大型语言模型的结构化压缩与剪枝方向论文汇编

> 本方向共 7 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Beyond Uniform SVD: Dual-Level Optimization across Columns and Modules for LLM Compression ｜双层级优化奇异值分解

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9bbfb78c9638)

> 大语言模型（LLM）低秩分解压缩长期受困于权重矩阵内部误差分布不均与模块间重要性差异，导致统一截断策略在有限秩预算下近似次优。现有方法如 SVD-LLM 和 SoLA 仅依赖激活范数或局部截断误差作为代理指标，缺乏对模型全局性能影响的直接评估。Duo-SVD 通过列级混合分解与模块级全局约束优化，在免训练条件下实现了更精细的压缩预算分配。该方法在 20% 压缩率下显著优于现有 SVD 基线，但其列保留策略对硬件执行效率的影响及高压缩率下的鲁棒性仍存疑。

】

---

【Break Through the Compression Bottleneck: From Theory to Practice ｜量化与低秩分解的非正交性证明及对角粘合法

研究机构：中国科学院、中国科学院大学

作者：Xiusheng Huang、Lu Wang、Yequan Wang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_08ae6203b98c)

> 大语言模型（LLM）压缩常假设量化与低秩分解相互独立，但本文指出二者组合会引入复合误差。现有方法忽略激活值离群点导致的非正交效应，且未明确最优压缩顺序。本文通过理论证明量化与低秩分解非正交，推导先低秩后量化的最优顺序，并提出对角粘合法（Diagonal Adhesive Method, DAM）以平衡量化方差。该工作为组合压缩提供了理论依据，但其效果高度依赖特定比特宽度和压缩率，泛化性存疑。

】

---

【Decomposed Trust: Privacy, Adversarial Robustness, Ethics, and Fairness in Low-Rank LLMs ｜低秩分解对大语言模型可信度的解耦分析

研究机构：美国爱荷华州立大学

作者：Daniel Agyei Asante、Md Mokarram Chowdhury、Yang Li

论文原文见 [arXiv](https://arxiv.org/abs/2511.22099)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.22099)

> 大语言模型（LLM）在资源受限场景下的部署依赖低秩分解等压缩技术，但现有研究仅关注压缩后的性能保持，忽视了压缩对模型安全属性的潜在破坏。本文切入点在于首次系统量化低秩分解在隐私、对抗鲁棒性、伦理和公平四个维度的副作用，通过多模型、多压缩算法的对比实验揭示压缩与可信度的非正交关系。其价值在于填补了压缩评估中“可信度”维度的空白，但实验局限于特定骨干网络与压缩率区间，未提供可信度感知的压缩优化策略。

】

---

【Do We Need Distinct Representations for Every Speech Token? Unveiling and Exploiting Redundancy in Large Speech Language Models ｜语音大语言模型中的Token冗余解剖与免训练压缩

作者：Bajian Xiang、Tingwei Guo、Xuan Chen 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.06871)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.06871)

> 语音大语言模型（LSLMs）因高帧率编码导致序列长度远超语义内容，引发高昂推理成本。现有压缩方法多借鉴视觉语言模型（VLMs）技术，缺乏对语音内部冗余层级结构的系统性解析，导致压缩位置与力度选择缺乏理论依据。本文通过层间干预实验揭示深层表示的极端冗余性，并提出基于余弦相似度的免训练Token合并机制Affinity Pooling。该方法在削减27.48%预填充FLOPs的同时保持或提升任务精度，但其在长上下文推理及非英语语音上的泛化能力尚存疑。

】

---

【Lightweight Haar Wavelet Subband Pruning for LLMs ｜Haar 小波子带剪枝

研究机构：中国科学院

作者：Jiang Li、Pengfei Cao、Chenxi Zhou 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_04dd35dc9ce7)

> 大语言模型（LLM）压缩面临校准数据依赖与权重更新开销的双重瓶颈，现有免重训练方法如 SparseGPT 和 Wanda 仍需消耗大量算力进行二阶优化或激活统计。本文切入点在于利用 Haar 小波变换的正交性，将剪枝问题转化为频域系数幅值排序，从而彻底消除对校准集和梯度计算的依赖。通过强制四个频率子带均匀稀疏，HWSP 在保持精度接近 SOTA 的同时将剪枝时间降低至秒级。该方案在免校准场景下具有显著效率优势，但其非结构化稀疏模式在硬件推理加速上的实际收益仍存疑。

】

---

【POP: Prefill-Only Pruning for Efficient Large Model Inference ｜阶段感知剪枝：解耦预填充与解码的冗余性

研究机构：武汉大学

作者：Junhui He、Zhihui Fu、Jun Wang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.03295)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.03295)

> 大语言模型推理加速面临结构化剪枝精度崩溃与非结构化剪枝硬件低效的双重困境。现有方法将预填充（Prefill）与解码（Decode）视为同质过程，忽略了二者在功能上的根本不对称：预填充仅需编码上下文，而解码需同时编码并预测下一词。本文提出 Prefill-Only Pruning (POP)，通过虚拟门机制识别深层在预填充阶段的冗余性，仅在该阶段移除深层，保留全模型用于解码，辅以独立 KV 投影与边界处理。该方法在 Llama-3.1 等模型上实现了 1.37 倍预填充加速且精度损失极小，但其加速收益高度依赖输入长度，短序列场景下优势微弱。

】

---

【TELL-TALE: Task Efficient LLMs with Task Aware Layer Elimination ｜任务感知层消除

作者：Omar Naim、Krish Sharma、Niyar R Barman 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.22767)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.22767)

> 导读 大语言模型（Large Language Models, LLMs）的固定架构假设所有层对任意下游任务同等重要，导致在特定任务上存在计算冗余甚至性能干扰。现有剪枝方法多聚焦于通过移除权重或层来降低计算开销，往往以牺牲下游任务精度为代价，且依赖困惑度或表示相似度等通用指标，无法捕捉任务特异性。TALE 提出一种推理时贪心算法，以任务验证集准确率为唯一优化目标，迭代移除对当前任务无益甚至有害的层。该方法在无需重训练的前提下，不仅降低了推理成本，更在多个基准上实现了超越原始模型的性能提升，挑战了“剪枝必然导致性能下降”的领域共识。

】
