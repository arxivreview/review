# ICLR2026 · 用于分子与材料发现的LLM方向论文汇编

> 本方向共 10 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CATALYSTBENCH: A COMPREHENSIVE MULTI-TASK BENCHMARK FOR ADVANCING LANGUAGE MODELS IN CATALYSIS SCIENCE ｜催化科学多任务基准与多头解耦微调

研究机构：中国科学院、中国科学院大学

作者：Xueqing Chen、Jian Xu、Ludi Wang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_91260175)

> 催化材料设计涉及数值回归、分类决策与机理推理的混合工作流，现有基准多聚焦单一模态或静态问答，无法反映真实研发闭环。通用大语言模型（LLM）在处理高精度数值预测时存在显著能力缺口，而传统单头微调易引发不同任务间的损失景观干扰。本文构建首个覆盖催化全生命周期的多任务基准CatalystBench，并提出多头全任务微调（Multi-head Full-task, MFT）策略，通过物理隔离输出头解决异构任务冲突。该工作验证了领域专用架构在混合科学推理中的有效性，但其纯文本输入限制了对催化剂表面几何结构的深层理解。

】

---

【DRUGTRAIL: INTERPRETABLE DRUG DISCOVERY VIA - STRUCTURED REASONING AND DRUGGABILITY TAILORED PREFERENCE OPTIMIZATION ｜可解释药物发现：结构化推理与成药性定制偏好优化

研究机构：中国人民大学、清华大学

作者：Yurou Liu、Mingyang Li、Xinyuan Zhu 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_98202259)

> 药物发现中的AI模型长期面临“黑盒”决策与单一结合能优化导致的成药性缺失问题。通用大语言模型（LLM）虽具备跨域知识，但直接应用时缺乏符合临床化学逻辑的推理轨迹，且现有强化学习（RL）奖励机制往往忽视合成可行性与脱靶风险。DRUGTRAIL通过构建临床化学信息推理（CCIR）轨迹与成药性定制偏好优化（DTPO）策略，将LLM的生成过程约束在可解释且符合药物化学规则的范围内。该框架在口袋配体设计任务中显著提升了结合亲和力与药物类属性，但其泛化能力受限于2D序列输入与单智能体架构，缺乏3D空间感知与多智能体协作验证。

】

---

【Entropy-Guided Dynamic Tokens for Graph-LLM Alignment in Molecular Understanding ｜熵引导动态令牌图-LLM对齐

作者：Zihao Jing、Qiuhao Zeng、Ruiyi Fang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.02742)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.02742)

> 分子图与语言模型的对齐长期受困于固定长度连接器的结构压缩与骨干微调的高昂成本。现有Q-Former类方法将变长分子强制映射为静态令牌，导致立体化学丢失，且联合训练易引发过拟合。EDT-Former通过熵值峰值分割生成动态令牌，并在冻结骨干下实现高效对齐。该方法在分子理解与性质预测上超越同规模基线，但其动态令牌机制在生成任务中的泛化能力尚存疑。

】

---

【From What to Why: A Multi-Agent System for Evidence-based Chemical Reaction Condition Reasoning ｜从预测到解释：基于多智能体辩论的反应条件证据推理系统

研究机构：清华大学、英国牛津大学

作者：Cheng Yang、Jiaxuan Lu、Haiyuan Wan 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.23768)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.23768)

> 反应条件推荐长期面临“黑盒预测”困境，模型能给出溶剂或催化剂，却无法解释其化学合理性，限制了在高风险合成工作流中的可信度。现有检索或单步推理方法缺乏对机理约束的显式验证，导致输出不可审计。本文提出ChemMAS，将条件选择重构为多智能体协作的证据推理任务，通过机理分析、多通道召回与锦标赛式辩论生成可证伪的决策依据。该方法在Top-1相似度上显著优于专用模型与通用大模型，但其性能高度依赖私有数据库的覆盖率，泛化边界尚待公开基准检验。

】

---

【Graph Diffusion Transformers are In-Context Molecular Designers ｜演示条件扩散分子设计

研究机构：美国圣母大学、美国麻省理工学院

作者：Gang Liu、Jie Chen、Yihan Zhu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.08744)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.08744)

> 分子设计面临属性空间巨大但单任务标注数据稀缺的矛盾，传统专用模型依赖大量Oracle调用或特定任务微调，而大语言模型（LLM）的上下文学习（In-Context Learning, ICL）在分子生成中效果有限。本文切入点在于将ICL范式从文本序列迁移至分子图结构，利用少量“分子-分数”演示对定义任务上下文，替代固定的属性向量。通过引入基团级分词器与图扩散Transformer，DemoDiff实现了零样本跨百万种属性的通用分子设计。其价值在于以0.7B参数模型匹配或超越百倍规模LLM的性能，但其在结构约束任务上的表现弱于属性驱动任务，且缺乏3D几何信息的融合。

】

---

【LLEMA: Evolutionary Search with LLMs for Multi-Objective Materials Discovery ｜LLEMA：基于LLM进化搜索的多目标材料发现框架

研究机构：美国弗吉尼亚理工大学、美国桑迪亚国家实验室

作者：Nikhil Abhyankar、Sanchit Kabra、Saaketh Desai 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.22503)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.22503)

> 材料发现需在高维化学空间中同时满足多个竞争性物理约束，传统生成模型因缺乏领域先验与热力学稳定性校验，常产出理论可行但无法合成的候选结构。现有LLM方法多聚焦单目标优化或无约束生成，忽略了真实工业场景中“多目标权衡”与“合成可行性”的耦合需求。LLEMA通过引入化学信息进化算子、代理模型评估及记忆池反馈机制，将材料设计重构为受约束的多目标进化搜索问题。该框架在14个工业任务上显著提升了候选结构的热力学稳定性，但其性能高度依赖代理模型的泛化能力，且在部分单一目标任务上的命中率未全面超越专用基线。

】

---

【MolecularIQ: Characterizing Chemical Reasoning Capabilities Through Symbolic Verification on Molecular Graphs ｜分子结构推理基准

作者：Christoph Bartmann、Johannes Schimunek、Mykyta Ielanskyi 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.15279)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.15279)

> 现有化学大语言模型（LLM）基准依赖公开数据集或代理验证器，导致模型可能通过记忆分子-性质对而非真实图推理获得高分，无法区分模式匹配与结构理解。本文提出MolecularIQ，一个完全基于符号验证的分子结构推理基准，通过RDKit动态生成Ground Truth消除数据泄漏，并引入多维复杂度轴以定位具体失效模式。实验表明，即便最强模型在结构解析上准确率仅47.5%，且化学微调反而系统性损害结构推理能力，揭示了当前LLM在分子图理解上的根本瓶颈。

】

---

【Reference-guided Policy Optimization for Molecular Optimization via LLM Reasoning ｜参考引导策略优化

研究机构：香港浸会大学、上海交通大学

作者：Xuan Li、Zhanke Zhou、Zongze Li 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.05900)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.05900)

> 指令式分子优化要求模型在提升分子性质的同时保持结构相似性，但现有数据集仅提供单一参考分子而无推理轨迹，导致监督信号严重失配。标准监督微调（SFT）会坍缩为短答案输出并抑制多步推理，而基于可验证奖励的强化学习（RLVR）因奖励稀疏陷入保守编辑。RePO通过引入答案级参考引导项，在保留RLVR探索能力的同时锚定参考分子，解决了这一矛盾。该方法在TOMG-Bench上取得最优成功率×相似度乘积，但其依赖参考分子的设定限制了完全自主探索的潜力。

】

---

【SPECTRALLM: UNCOVERING THE ABILITY OF LLMS - FOR MOLECULE STRUCTURE ELUCIDATION FROM MULTI SPECTRAL ｜光谱结构解析的大语言模型

研究机构：中国科学院、香港理工大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_95124861)

> 自动化分子结构解析长期受限于单一光谱模态的信息缺失与异构数据难以统一处理的瓶颈。现有深度学习模型虽能处理特定光谱，但缺乏跨模态联合推理能力，且架构僵化无法整合实验条件等上下文信息。SpectraLLM通过将多种光谱峰值转化为自然语言文本，利用冻结骨干的大语言模型进行自回归推理，实现了从单一到多光谱的端到端结构预测。该方法在四个基准数据集上超越了专用基线，证明了纯语言空间映射光谱-结构关系的可行性，但其对光谱固有歧义的区分能力仍受限于数据本身的物理特性。

】

---

【SPECTRALLM: UNCOVERING THE ABILITY OF LLMS FOR - MOLECULAR STRUCTURE ELUCIDATION FROM MULTI SPECTRAL DATA ｜光谱驱动的大语言模型结构解析

研究机构：中国科学院、香港理工大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_97751145)

> 自动化分子结构解析长期受限于单一光谱模态的信息缺失与异构数据难以统一处理的瓶颈。现有深度学习模型虽能处理特定光谱，但架构僵化，无法灵活整合红外、核磁共振等多种互补信号。SpectraLLM通过将光谱峰值序列化为自然语言文本，利用大语言模型的符号推理能力实现多模态联合解析。该方案验证了纯文本空间统一异构科学数据的可行性，但其对光谱物理歧义的解决能力仍受限于数据驱动的本质。

】
