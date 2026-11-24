# ACL-Findings2026 · 大语言模型后训练微调与对齐方向论文汇编

> 本方向共 6 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【GFT: From Imitation to Reward Fine-Tuning with Unbiased Group Advantages and Dynamic Coefficient Rectification ｜组微调：从模仿到奖励的无偏优化

研究机构：浙江大学

作者：Wangjie Gan、Miao Pan、Linbo Xi 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14258)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14258)

> 大语言模型后训练的核心矛盾在于，监督微调（SFT）虽能高效注入知识，却因单路径依赖导致策略熵坍缩，并引发灾难性遗忘，使得后续强化学习（RL）的探索空间被严重压缩。现有方案如标准SFT或纯RL均无法在保持通用能力与提升推理上限间取得平衡，本文切入点在于从训练动力学视角揭示SFT本质上是带有不稳定逆概率权重的稀疏奖励RL特例。通过引入组优势学习与动态系数校正，GFT在单一阶段内实现了无偏对比监督与优化稳定性的统一。该框架在数据效率上显著优于SFT基线，但其绝对性能仍低于当前SOTA混合策略，且对多任务场景下的组构成动态调整缺乏验证。

】

---

【Navigating the Alignment-Calibration Trade-off: A Pareto-Superior Frontier via Model Merging ｜导航对齐-校准权衡：基于模型合并的帕累托前沿

研究机构：英国剑桥大学

作者：Tiancheng Hu、Benjamin Minixhofer、Nigel Collier

论文原文见 [arXiv](https://arxiv.org/abs/2510.17426)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.17426)

> 后训练旨在提升大语言模型的指令遵循能力，但常伴随准确率下降与校准度恶化，即“对齐税”。现有缓解策略多聚焦于训练时的正则化或数据筛选，忽视了校准度这一隐性成本，且难以在保持对齐收益的同时恢复模型的不确定性表征。本文提出一种训练后（Post-hoc）的权重插值方法，通过混合预训练与指令微调模型的权重，在无需梯度更新的情况下探索对齐-校准帕累托前沿。该方法在多个基准上实现了准确率的帕累托改进并部分恢复了校准度，但其有效性依赖于白盒权重访问，且未量化对安全对齐的潜在稀释效应。

】

---

【ProFit: Leveraging High-Value Signals in SFT via Probability-Guided Token Selection ｜概率引导的Token掩码微调

研究机构：清华大学

作者：Tao Liu、Taiqiang Wu、Runming Yang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.09195)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.09195)

> 监督微调（SFT）在将大语言模型（LLM）对齐至人类意图时，常因强制拟合单一参考答案而陷入表面形式过拟合，导致模型记忆特定样本而非掌握核心逻辑。现有方案要么依赖高成本的多参考数据构建，要么采用软加权策略但无法彻底隔离噪声梯度。ProFit 通过识别高预测概率Token承载核心语义的特性，提出硬掩码机制屏蔽低概率Token，以单参考数据实现优于全量SFT的泛化性能。该方法在Qwen3系列模型上平均准确率提升3.0%至10.9%，但其效果是否源于骨干模型优势而非算法本身，仍缺乏跨架构的严格归因验证。

】

---

【Reinforcement Learning with Semantic Rewards Enables Low-Resource Language Expansion without Alignment Tax ｜语义空间对齐

研究机构：上海交通大学、澳门大学

作者：Zeli Su、Ziyin Zhang、Zhou Liu 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.14366)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.14366)

> 低资源语言扩展面临的核心矛盾是：在数据稀缺且分布偏斜的条件下，如何提升目标语言能力而不牺牲预训练模型的通用能力，即最小化“对齐税”。现有监督微调（SFT）方法通过token级似然最大化进行表面形式模仿，在窄分布上导致参数过度拟合与灾难性遗忘，无法兼顾适应性与保持性。本文切入点在于将对齐目标从token级匹配解耦为嵌入级语义一致性，利用组相对策略优化（GRPO）驱动模型在语义空间内探索多样表达。该方法在藏语-中文翻译任务上验证了RL比SFT更有效地保留通用能力，但其结论局限于单一语言对与特定骨干网络，泛化性存疑。

】

---

【RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning ｜奖励感知微调

作者：Zehua Liu、Shuqi Liu、Tao Zhong 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.09253)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.09253)

> 大语言模型后训练常面临高质量专家数据稀缺与自生成数据中负样本被浪费的双重困境。拒绝采样微调（RFT）虽通过自生成缓解数据依赖，但其硬阈值筛选机制丢弃了包含失败模式信息的负样本，导致模型无法区分正确与错误输出的细微差异。本文提出奖励感知微调（RIFT），通过有界线性代理损失稳定利用负样本梯度，在不引入参考模型的前提下实现数据高效对齐。该方法在数学推理基准上显著优于RFT与DPO，但其性能上限仍受限于奖励信号的判别力，且在非可验证任务上的泛化能力尚未得到验证。

】

---

【Training-Free Test-Time Contrastive Learning for Large Language Models ｜无梯度测试时对比学习

研究机构：华南理工大学

作者：Kaiwen Zheng、Kai Zhou、Jinwu Hu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.13552)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.13552)

> 冻结大语言模型在分布偏移下性能退化，现有测试时适应方法要么依赖梯度更新（需白盒访问），要么依赖外部知识（需预置数据库）。本文切入点在于：不更新参数、不依赖外部反馈，仅从模型自生成输出中提取对比信号。TF-TTCL通过多智能体角色扮演生成多样推理轨迹，蒸馏为显式文本规则并在线检索引导推理。该方法在黑盒场景下显著优于零样本基线，但其规则仓库的长期容量管理与跨域泛化边界尚存疑。

】
