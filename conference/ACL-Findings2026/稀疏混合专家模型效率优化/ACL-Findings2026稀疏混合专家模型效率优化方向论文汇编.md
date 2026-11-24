# ACL-Findings2026 · 稀疏混合专家模型效率优化方向论文汇编

> 本方向共 7 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【COMPEL: Compensated Mixture-of-Experts Pruning with Expert-Layer distribution ｜补偿式混合专家剪枝与专家-层分布对齐

研究机构：韩国汉阳大学

作者：Seohee Yoon、Yong Suk Choi

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_53551d3bb491)

> 混合专家模型（Mixture-of-Experts, MoE）在推理时需将全部专家权重驻留内存，导致显存占用远超激活参数量，成为部署的核心瓶颈。现有专家剪枝方法多采用跨层统一剪枝率，忽视了不同层间专家冗余度的结构性差异，导致低冗余层中独特专家被误删，引发性能显著退化。COMPEL 将剪枝指标转化为连续优化问题，通过 Fisher 信息估计专家敏感度、层级离群分布量化层重要性，并引入 Fisher 引导的权重补偿机制。该方法在 25% 剪枝率下实现了近乎无损的性能保持，但在 50% 高压缩率下的精度边界及与 Shapley 值类方法的对比缺失，使其泛化能力存疑。

】

---

【Do Domain-specific Experts exist in MoE-based LLMs? ｜领域特定专家的存在性验证与无训练路由干预

作者：Giang Do、Hung Le、Truyen Tran

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9560f1be8794)

> 稀疏混合专家（Sparse Mixture-of-Experts, SMoE）架构在提升模型容量的同时，其内部专家是否真正形成了可解释的领域分工，长期缺乏实证依据。现有研究多聚焦于通过修改架构或损失函数来“促进”专业化，却未验证专业化是否真实存在，更未探索如何利用这种潜在的分工结构进行零成本推理优化。本文通过梯度归因量化专家对特定领域的贡献度，证实了领域特定专家的存在，并据此提出 Domain Steering Mixture of Experts (DSMoE)，在推理阶段对路由权重进行线性缩放以激活特定专家。该方法在 MMLU-Pro 和 GPQA Diamond 上实现了显著的性能增益，但其效果高度依赖领域数据的分布特性，且未验证在混合领域任务中的鲁棒性。

】

---

【LightMoE: Task-Aware Expert Availability Management for Memory-Efficient MoE-LLM Inference ｜任务感知的专家可用性管理

作者：Puhan Luo、Yunhao Yao、Junyang Wang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4da6f9f64034)

> 边缘设备部署混合专家模型时，巨大的专家池内存占用与严格的硬件限制构成核心矛盾。静态剪枝损失精度，动态换入换出引入高延迟，现有方案难以兼顾。LightMoE 利用边缘请求的时空局部性，通过频率初始化、相似度重定向与任务级异步替换，解耦逻辑选择与物理驻留。该方法在精度-延迟权衡上优于剪枝与交换基线，但其对任务语义漂移的响应粒度及跨层依赖建模仍存疑。

】

---

【ModularMoE: Fast LLM Customization with Parameter-Sharing Mixture-of-Experts for Low-Resource Settings ｜模块化混合专家模型

作者：Jiaxing Liu、Qi Qi、Haifeng Sun 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c19f9aef8c68)

> 导读 低资源场景下的大语言模型部署面临算力与存储的双重瓶颈，传统“剪枝-微调”范式因计算开销大或任务间干扰而难以落地。现有方法要么牺牲通用能力换取特定任务性能，要么因灾难性遗忘导致知识退化。本文切入点在于利用预训练模型中神经元共激活形成的涌现模块化特性，将前馈层拆分为可共享的模块，通过组合模块构建任务特定专家，实现参数高效的多任务定制。该方法在同等稀疏度下显著优于传统剪枝基线，但其静态路由机制对动态输入复杂度的适应性存疑。

】

---

【SARA: Unlocking Multilingual Knowledge in Mixture-of-Experts via Semantically Anchored Routing Alignment ｜语义锚定路由对齐

研究机构：天津大学、阿里巴巴集团

作者：Tianyu Dong、Yangyang Liu、Jiang Zhou 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.25821)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.25821)

> 稀疏混合专家模型在低资源语言上常因路由分歧导致性能衰减，现有微调方法多聚焦输出层或隐藏状态，未能直接修正专家激活路径。SARA 将高资源语言的路由分布作为语义锚点，通过 Jensen-Shannon 散度约束对齐中间层路由概率。该方法在 Qwen3-30B-A3B 上实现了跨语言推理能力的提升，但其效果高度依赖锚点语言的质量与层选择策略，泛化性仍存疑。

】

---

【Specialization without Sparsity: Efficient and Expressive Split-Path Experts for LLM Fine-Tuning ｜稀疏激活与参数效率的冲突：SparMoE 的软路由解法

作者：Ganghao Liu、Qin Zhou、Zhe Wang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9081507bc433)

> 参数高效微调（PEFT）旨在以极小参数代价适配大模型，但现有 MoE-PEFT 方法将 LoRA 复制为专家并采用离散硬路由，导致参数量随专家数线性膨胀，且在数据稀缺下因路由高方差引发专家欠训练。本文指出离散选择与受限参数空间存在根本错配，提出 SparMoE，以全激活软路由替代硬路由，并用缩放-偏置双路径向量专家替代低秩矩阵专家，在 GLUE 上以 0.29M 参数超越全量微调。该设计在低资源微调场景下有效，但其全激活机制在长序列下的计算开销未经验证，且缺乏与大规模 LLM 推理任务 SOTA 的直接可比性。

】

---

【TENP: Trapezoidal Expert Neuron Pruning For Mixture-of-Experts ｜梯形专家神经元剪枝

研究机构：天津大学

作者：Jiangyang He、Shaolin Zhu、Deyi Xiong

论文原文见 [arXiv](https://arxiv.org/abs/2606.09885)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.09885)

> 混合专家（Mixture-of-Experts, MoE）模型在扩展参数容量时面临静态显存占用过高的部署瓶颈。现有压缩方法要么移除整个专家从而破坏预训练路由拓扑，要么采用无结构权重剪枝导致硬件加速困难。本文切入点在于保留专家实体与路由路径，仅对专家内部冗余神经元进行结构化剪枝，并引入深度感知的梯形稀疏度分配策略。该方法在保持路由稳定性的同时显著降低了激活参数量，但在跨域泛化与极端稀疏度下的理论边界仍存疑。

】
