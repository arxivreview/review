# ACL-Findings2026 · 低秩适配变体方向论文汇编

> 本方向共 13 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CoMoL: Efficient Mixture of LoRA Experts via Dynamic Core Space Merging ｜核心空间混合LoRA专家

作者：Jie Cao、Zhenxuan Fan、Zhuonan Wang 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_10597fc9b9c1)

> 混合专家低秩适配（MoE-LoRA）旨在通过多个低秩矩阵捕捉互补特征以突破单一LoRA的表达瓶颈，但现有方法因专家参数冗余和实例级路由导致计算开销激增且适应粒度粗糙。本文切入点在于利用LoRA固有的低秩结构，将专家合并与路由操作从全维空间压缩至核心空间。具体做法是引入核心空间专家存储与核心空间路由机制，实现Token级细粒度适配。该框架在保持与标准LoRA相当参数量的同时提升了数学与代码任务性能，但其核心空间维度固定，未验证动态调整秩对复杂推理的增益。

】

---

【Context-Conditioned Masked LoRA: Dynamic Rank Routing for Compute-Efficient Parameter-Efficient Fine-Tuning ｜上下文条件掩码低秩适配

作者：Rifat Rafiuddin、Rafae Abdullah

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_adfec0cb95fc)

> 低秩适配（LoRA）通过冻结骨干并注入低秩矩阵实现参数高效微调，但固定秩导致每个 token 均执行全秩计算，参数效率未转化为计算效率。现有动态秩方法多在训练时分配或仅提供有限稀疏性，缺乏推理时逐样本的精确秩控制。本文提出 CCM-LoRA，通过轻量级路由器生成输入依赖的秩掩码，实现动态秩路由以削减适配器计算量。该方法在保持精度的同时显著降低推理 FLOPs，但路由器开销在短序列场景下仍构成瓶颈，且缺乏多任务干扰下的稳定性验证。

】

---

【DPLoRA: A Dual-Pruning Framework based on ILP Optimization and Progressive Pruning for Parameter-Efficient LoRA Fine-Tuning ｜双剪枝低秩适配

作者：Changjun Park、Sejong Yoon、Jaekwang Kim

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_270f9ca2232c)

> 导读

】

---

【FARSS: Fisher-Optimized Adaptive Low-Rank and Singular-Vector Selection for Knowledge-Preserving Fine-Tuning ｜基于Fisher信息的层感知低秩适配

作者：Renxing Chen、Ziwei Xiang、Peisong Wang 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6306e8c6c70c)

> 参数高效微调（PEFT）在提升目标任务性能时，常因更新幅度过大而破坏预训练模型的世界知识，现有方法多采用均匀秩分配或基于梯度的重要性剪枝，忽视了Transformer层间对知识存储的敏感度差异。本文指出浅层权重对世界知识保持具有决定性作用，提出FARSS框架，通过Fisher信息量化层敏感度并实施反向秩分配，结合任务感知的奇异向量初始化，在固定参数预算下实现知识保持与任务适应的帕累托最优。该方法在多项基准上验证了其在平衡指标上的优势，但其对Fisher估计样本量的依赖及深层非线性曲率近似的有效性仍存疑。

】

---

【G-LoRA: Global-Local Decoupled Low-Rank Adaptation ｜全局-局部解耦低秩适配

研究机构：华东师范大学

作者：Jiahao Xiong、Yihong Huang、Yihe Liu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5a2794b04c93)

> 低秩适配（LoRA）在固定秩约束下难以处理单一权重矩阵内部的参数重要性差异，导致关键子区域表达力不足。现有动态秩方法多聚焦层间分配或稀疏化，缺乏矩阵内部的细粒度容量调控。G-LoRA 通过一阶泰勒近似识别高重要性子块，并采用全局-局部解耦架构将高秩预算集中于此，在相同参数预算下提升有效秩。该方法在数学与代码任务上显著优于基线，但其区域收缩机制对早期全局信息捕获的影响尚存疑。

】

---

【Grouped Adaptive Weight Sharing (GAWS): An Inference-Efficient Adaptation Method for Large Language Models ｜分组自适应权重共享（GAWS）：未合并适配器的推理延迟优化

作者：Eman Alsuradi、Junhyun Lee、Kyenghun Lee 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ed41e93e9264)

> 导读 参数高效微调（PEFT）解决了大模型适配的计算与存储瓶颈，但主流方法如低秩适配（LoRA）在单请求、未合并场景下引入了显著的推理延迟，而现有系统级优化多依赖权重合并或批处理，无法直接应用于需保持适配器独立性的生产环境。本文切入点在于识别出LoRA延迟的根源并非参数数量，而是分段CUDA内核调用导致的启动开销。通过引入结构化Kronecker积分解，将双矩阵乘法压缩为单次分组矩阵乘法，在保持参数效率的同时大幅降低延迟。该方案在单请求场景下实现了帕累托最优，但其对非局部依赖的捕捉能力及在批量推理下的优势持续性存疑。

】

---

【Hebbian-Guided Bi-Directional Rank Adaptation for Parameter-Efficient Fine-Tuning ｜基于Hebbian协同的双向秩适应

研究机构：天津大学、电子科技大学

作者：Xing Zhao、Liu Yang、Xi-Le Zhao 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_83cc0601c2be)

> 低秩适配（Low-Rank Adaptation, LoRA）在微调大语言模型时，固定秩设计无法适配不同层对任务贡献的异构性，导致参数预算分配失衡。现有动态秩方法仅支持单向剪枝或扩展，难以同时解决冗余参数与容量不足问题。HeBiRA通过引入Hebbian启发的重要性评分，实现了秩的双向重分配，在GLUE基准上以89.80的平均准确率超越了仅剪枝的AdaLoRA（89.46）和仅扩展的IncreLoRA（88.90）。该方法验证了激活与梯度协同信号在秩选择中的有效性，但其理论推导基于线性假设，在复杂非线性任务中的泛化边界尚存疑。

】

---

【HyperAdaLoRA: Accelerating LoRA Rank Allocation During Training via Hypernetworks without Sacrificing Performance ｜超网络加速低秩适配收敛

研究机构：美国哈佛大学、中国科学院大学

作者：Hao Zhang、Zhenjia Li、Runfeng Bao 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.02630)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.02630)

> 动态秩分配旨在解决固定秩 LoRA 在异构层间参数预算分配不均的问题，但现有 SVD 基方法因直接优化分解矩阵导致收敛缓慢且计算开销高。HyperAdaLoRA 切入这一瓶颈，利用基于注意力机制的超网络动态生成 SVD 分量，替代传统的反向传播更新。该方法在保持最终精度的前提下显著缩短了训练时间，但其引入的超网络参数量是否违背 PEFT 的极简初衷，以及其在复杂推理任务上的泛化边界，仍需进一步审视。

】

---

【Polynomial Expansion Rank Adaptation: Enhancing Low-Rank Fine-Tuning with High-Order Interactions ｜多项式扩展秩适应

研究机构：安徽大学、中国科学技术大学

作者：Wenhao Zhang、Lin Mu、Li Ni 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.11841)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11841)

> 低秩适应（LoRA）通过冻结预训练权重并注入低秩矩阵实现高效微调，但其双线性更新形式仅捕捉一阶线性依赖，难以建模高阶参数交互。现有方法如 HiRA 依赖外部权重耦合，DoRA 侧重幅值方向解耦，均未在低秩因子内部引入显式非线性。PERA 通过在低秩因子空间执行结构化多项式展开，生成平方与交叉项，在不增加秩或推理开销的前提下提升表达力。该方法在常识推理与 NLU 任务上优于基线，但评估范围局限于语言理解，且高阶项的优化稳定性缺乏理论保证。

】

---

【RanLoRA: Residual-aware Nonlinear Low-Rank Adaptation ｜残差感知非线性低秩适配

研究机构：美国南加州大学

作者：Xu Luo、Yongbin Liu、Chunping Ouyang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_da3b5118e652)

> 低秩适配（LoRA）在复杂推理任务上受限于线性子空间的表达瓶颈，单纯增加秩或引入全局非线性模块往往导致参数冗余与预训练知识破坏。RanLoRA 通过奇异值分解（SVD）显式解耦预训练权重的主成分与残差，仅对残差路径施加轻量级非线性调制，在极低参数预算下实现了性能突破。该方法在常识推理与数学推理任务上显著优于同参数量基线，但其非线性结构对推理延迟的影响及在简单任务上的泛化边界仍需进一步审视。

】

---

【Rethinking Parameter Sharing for LLM Fine-Tuning with Multiple LoRAs ｜非对称低秩适配：共享B矩阵的多任务与联邦微调

研究机构：美国纽约州立大学布法罗分校

作者：Hao Ban、Kaiyi Ji

论文原文见 [arXiv](https://arxiv.org/abs/2509.25414)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.25414)

> 多LoRA微调中，共享内部矩阵$A$以降低参数开销是主流策略，但现有方法忽略了$A$与$B$在训练动力学中的功能差异。本文发现$A$的相似性源于初始化而非知识共享，且$A$存在“惰性学习”现象，阻碍特征子空间探索。通过反转共享对象，设计共享$B$、独立$A$的非对称架构，并扩展至异构联邦场景。该设计在保持精度的同时显著降低通信成本，但共享$B$是否成为单任务性能瓶颈尚存疑。

】

---

【SAMoRA: Semantic-Aware Mixture of LoRA Experts for Task-Adaptive Learning ｜语义感知混合LoRA专家

研究机构：北京交通大学、中国科学院

作者：Boyan Shi、Wei Chen、Shuyuan Zhao 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.19048)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.19048)

> 导读 多任务大语言模型微调面临专家同质化与更新强度僵化的双重瓶颈，现有混合专家低秩适配（Mixture-of-Experts Low-Rank Adaptation, MoE-LoRA）方法依赖隐式路由与全局固定缩放，导致不同任务间参数干扰严重。SAMoRA 通过引入显式语义匹配路由与任务自适应缩放机制，将输入语义与专家能力直接对齐，并动态调节各任务的更新幅度。该框架在常识推理与通用语言理解基准上以更低的可训练参数比例超越了主流基线，但其对大规模模型及多模态场景的适用性尚未得到验证。

】

---

【Why LoRA Fails to Forget: Regularized Low-Rank Adaptation Against Backdoors in Language Models ｜正则化低秩适配（RoRA）：基于谱强度与对齐的后门遗忘机制

作者：Hoang-Chau Luong、Lingwei Chen

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6a2e9f17c74a)

> 导读 大语言模型微调中的后门攻击防御长期面临一个核心矛盾：全参数微调虽能覆写中毒权重，但计算成本高昂，而低秩适配（LoRA）因参数冻结导致后门行为难以消除。现有防御多依赖外部检测或知识蒸馏，缺乏对LoRA内在遗忘机制的原理解释。本文从谱视角切入，指出LoRA脆弱性源于谱强度不足与谱对齐不良，而非单纯的低秩约束，并提出通过正则化增强谱分量、正交化触发器方向及后训练重缩放来主动遗忘后门。该工作为PEFT安全提供了新的理论框架，但其有效性高度依赖特定攻击类型与模型架构，在复杂推理任务上的泛化能力存疑。

】
