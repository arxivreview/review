# ACL-Findings2026 · 大语言模型对齐的偏好优化方向论文汇编

> 本方向共 9 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Dual-Phase Self-Evolution Framework for Large Language Models ｜双阶段自进化框架

研究机构：电子科技大学

作者：Haoran Sun、Zekun Zhang、Shaoning Zeng

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4626302df13f)

> 大语言模型（LLM）在部署后面临静态参数无法适应动态用户需求与领域知识更新的双重困境。现有偏好优化方法依赖离线静态数据，而记忆增强方法仅通过提示词检索历史交互，均未触及模型内部认知的系统性提升。本文提出双阶段自进化框架（Dual-Phase Self-Evolution, DPSE），通过实时交互信号驱动数据扩展与参数更新，实现用户偏好对齐与领域能力增强的协同。该框架在7B小模型上验证了在线进化的可行性，但其数据扩展策略对分布漂移的潜在影响尚存疑。

】

---

【Alignment Data Map for Efficient Preference Data Selection and Diagnosis ｜对齐数据地图

作者：Seohyeong Lee、Eunwon Kim、Hwaran Lee 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2505.23114)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_72ae40c93f58)

> 偏好数据选择长期依赖奖励边际（Reward Margin）作为唯一筛选信号，但边际相同的样本在绝对质量上差异巨大，导致低质数据混入训练集。本文指出边际信号的盲区，提出 Alignment Data Map，通过联合评估响应质量均值与方差，将数据划分为高质低变、低质低变及高变三个区域。实验表明，仅使用 33% 的高质低变数据即可超越全量数据训练效果。该工具在提升数据效率方面有效，但其依赖外部评分模型引入的偏差及标签诊断的泛化性仍存疑。

】

---

【Beyond Compromise: Pareto-Lenient Consensus for Efficient Multi-Preference LLM Alignment ｜帕累托宽容共识（PLC）：基于合作博弈的多目标LLM对齐

研究机构：浙江大学

作者：Renxuan Tan、Rongpeng Li、Zhifeng Zhao 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.05965)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05965)

> 多目标偏好对齐旨在同时优化有用性、无害性等异质人类价值观，但现有静态标量化或刚性梯度投影方法常陷入“风险规避均衡”，即模型为规避局部目标冲突而停滞于次优帕累托点。PLC将对齐重构为动态协商过程，通过联盟共识驱动的宽容梯度校正，允许少数目标暂时退化以换取整体帕累托改进。实验显示其在LLM-as-a-Judge评分上达到7.49，优于GAPO的7.03，但仅验证了3个目标维度，且未与正交分解类方法直接对比，其动态机制在高维目标空间下的稳定性存疑。

】

---

【CLewR: Curriculum Learning with Restarts for Machine Translation Preference Learning ｜基于重启机制的机器翻译课程学习偏好优化

研究机构：罗马尼亚布加勒斯特大学

作者：Alexandra Dragomir、Florin Brad、Radu Tudor Ionescu

论文原文见 [arXiv](https://arxiv.org/abs/2601.05858)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05858)

> 导读 大语言模型在机器翻译中的偏好优化面临训练数据顺序被忽视的问题，导致模型在训练后期遗忘早期易学样本，即灾难性遗忘。现有课程学习方法虽引入难度排序，但未解决多轮训练中的遗忘累积，且主要依赖参考模型导致优化信号弱。本文提出CLewR，通过每轮重启易到难的数据排序，结合机器翻译特定指标定义难度，并增强自适应拒绝偏好优化算法。该方法在多个模型家族上验证了有效性，但其在非翻译任务及复杂噪声场景下的泛化能力仍存疑。

】

---

【DynamicFocalPO: Adaptive Focusing Strategy for Preference Optimization ｜动态聚焦偏好优化

研究机构：南京大学

作者：Shu Zhou、Junan Chen、Rui Ling 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0fea5571ef4f)

> 直接偏好优化（DPO）在处理含噪偏好数据时，因固定加权策略导致梯度噪声累积，阻碍模型收敛。现有变体如FocalPO虽引入调制因子，但静态超参数无法适应模型能力演化。本文提出DynamicFocalPO，通过余弦退火动态调整聚焦参数，实现从易到难的课程学习。该方法在7B/8B模型上验证了性能增益，但缺乏大规模模型验证，其动态调度在复杂多目标场景下的泛化能力存疑。

】

---

【Intrinsic Mutual Information as a Modulator for Preference Optimization ｜基于内在互信息的自适应偏好优化

研究机构：中山大学、英国华威大学

作者：Peng Liao、Peijia Zheng、Lingbo Li 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.24804)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.24804)

> 离线偏好优化旨在将人类价值观内化至大语言模型，但主流方法如直接偏好优化（Direct Preference Optimization, DPO）对超参数极度敏感，导致训练成本高昂且性能不稳定。现有自适应机制或依赖额外的监控模块，或需保留参考模型，未能彻底消除调优开销。本文提出 RMiPO，利用响应级点互信息（Pointwise Mutual Information, PMI）差异动态调节奖励边际，实现无参考模型的实例级自适应优化。该方法在降低 15-20% 训练成本的同时提升了指令遵循性能，但其对长文本及复杂推理任务中的 PMI 信号有效性尚未验证。

】

---

【MEAV: Model Editing with Alignment Vectors for inference time LLM alignment in single and multidomain preference spectrum ｜对齐向量模型编辑

研究机构：亚马逊网络服务人工智能

作者：Sadat Shahriar、Zheng Qi、Nikolaos Pappas 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_57135049cbf4)

> 推理时偏好对齐旨在解决训练时方法（如DPO/RLHF）在偏好需求变化时需重新训练、成本高昂且缺乏细粒度控制的问题。现有推理时方法多依赖提示工程或固定混合，无法实现连续、动态的多域偏好强度调节。本文提出MEAV，通过提取域特定对齐向量并在推理时线性叠加，实现无需重训的连续偏好控制。该方法在自建医疗、金融、法律数据集上验证了可行性，但缺乏通用基准对比，其线性叠加假设在强冲突场景下的有效性存疑。

】

---

【PO-KGQA: Preference Optimization for Low-Resource Complex Knowledge Graph Question Answering ｜低资源复杂知识图谱问答的偏好优化

作者：Prerna Agarwal、Ayushman Kumar Singh、Srikanta Bedathur

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_70a181cc5ecb)

> 复杂知识图谱问答（KGQA）要求模型将自然语言问题转化为可执行的逻辑形式，但现有方法依赖大语言模型（LLM）的高昂算力或大量标注数据，导致小语言模型（SLM）在低资源场景下难以兼顾推理准确性与部署成本。本文切入点在于利用自反馈机制动态生成偏好数据，并修改迭代推理偏好优化（RPO）损失以聚焦中间推理步骤的正确性，从而摆脱对教师模型和最终答案的依赖。通过LoRA适配器微调7B级代码模型，PO-KGQA在KQA Pro基准上实现了超越主流对齐技术的性能。其价值在于证明了SLM在符号推理任务上的潜力，但自反馈循环的收敛稳定性与验证器错误累积效应仍存疑。

】

---

【Topology-Enhanced Alignment for Large Language Models: Trajectory Topology Loss and Topological Preference Optimization ｜拓扑增强对齐：轨迹拓扑损失与拓扑偏好优化

作者：Yurui Pan、Ke Xu、Bo Peng

论文原文见 [arXiv](https://arxiv.org/abs/2605.07172)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a67a56ea5945)

> 大语言模型对齐长期依赖局部信号，如词元似然或标量奖励，忽略了隐空间的全局几何结构，导致模型在复杂语义任务中轨迹漂移。现有直接偏好优化（DPO）等方法虽简化了流程，但未能约束隐藏状态从提示到答案的语义移动方向，造成对齐鲁棒性不足。本文提出拓扑增强对齐框架，通过0维持久同调提取隐空间“桥梁”方向，正则化生成轨迹。该方法在7B模型上提升了奖励模型分数与胜率，但其对数据清洗的依赖及高维拓扑特征的缺失仍存疑。

】
