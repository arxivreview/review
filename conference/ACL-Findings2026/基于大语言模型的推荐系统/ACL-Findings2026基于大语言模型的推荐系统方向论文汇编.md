# ACL-Findings2026 · 基于大语言模型的推荐系统方向论文汇编

> 本方向共 9 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Data-Efficient Adaptation to Contextual Shifts in LLM-based Conversational Recommendation ｜上下文漂移下的数据高效适配

作者：Hyeongjun Yang、Donghyun Kim、Seokju Hwang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_40f301419265)

> 对话推荐系统（CRS）在语言与社会趋势演变后，其冻结模型生成的推荐往往偏离当前用户偏好，而全量微调成本高昂且包含大量冗余样本。现有数据选择方法无法区分“模型已掌握”的熟悉样本与“真正需要学习”的有价值样本，导致在分布偏移场景下筛选失效。本文提出CAPT框架，通过训练损失与代理损失的比值量化样本可学习性，并结合损失加权训练策略，以10–50%的数据实现超越全量微调的性能。该框架在时序分割基准上验证了有效性，但其对非时序漂移（如用户个体偏好突变）的泛化能力尚未被检验。

】

---

【Distilling LLM Reasoning into Dense Encoders: Bridging the Accuracy-Efficiency Gap in Recommendation ｜推理至编码器蒸馏

作者：Donghee Han、Daeyoung Roh、A Young Kim 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_38c751571e07)

> 大语言模型（LLM）在推荐系统中具备强大的语义推理能力，但其自回归生成机制导致推理延迟高企，难以满足工业级实时性要求。现有蒸馏路线要么将推理压缩至小语言模型（SLM）保留生成能力但牺牲速度，要么压缩至传统推荐模型（CRM）提升速度但丢失推理深度。本文提出推理至编码器蒸馏（Reasoning-to-Encoder Distillation, R2END），通过将LLM对齐后的推理语义压缩至轻量级文本编码器的稠密向量空间，在消除推理阶段LLM依赖的同时保留推理本质。该架构在精度与延迟间实现了显著折中，但其对“向量压缩等效于显式推理”的假设在复杂多跳场景下的有效性尚存疑。

】

---

【GraphLoRA: Structure-Aware Low-Rank Adaptation for Large Language Model Recommendation ｜结构感知低秩适配

研究机构：安徽大学、中国科学技术大学

作者：Lin Mu、Guoji Wang、Li Ni 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.07526)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.07526)

> 推荐系统面临的核心矛盾在于大语言模型（LLM）擅长处理文本语义，却难以内化用户-物品交互中隐含的高阶拓扑结构。现有方法或将协同信号线性化为提示词，或注入静态嵌入，均无法在参数空间内动态捕捉结构依赖。本文提出 GraphLoRA，将图神经网络（GNN）嵌入低秩适配（LoRA）瓶颈层，实现结构感知的参数对齐。该方法在参数效率与结构推理间取得了平衡，但其对生成式推荐范式的适用性尚存疑。

】

---

【HSUGA: LLM-Enhanced Recommendation with Hierarchical Semantic Understanding and Group-Aware Alignment ｜分层语义理解与分组感知对齐

作者：Guorui Li、Dugang Liu、Lei Li 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.11662)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b01b6e01dc69)

> 序列推荐中，长交互历史直接输入大语言模型（LLM）易引发推理困难与语义漂移，且统一对齐策略忽视了用户活跃度差异。HSUGA通过分层编辑操作实现可控偏好演化，并依据用户分组动态调整语义利用强度，解决了上述两个核心瓶颈。该方法作为即插即用插件，显著提升了多种骨干模型的推荐性能，但其对计算效率的忽略及缺乏生成式基线对比，限制了其工业落地的评估完整性。

】

---

【Internalizing Multi-Agent Reasoning for Accurate and Efficient LLM-based Recommendation ｜单智能体轨迹对齐推荐器

作者：Yang Wu、Haoze Wang、Qian Li 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7c4789bdbeb0)

> 推荐系统面临的核心矛盾是LLM的语义泛化能力与协同过滤信号的结构性缺失，以及多智能体推理带来的实时性瓶颈。现有方案要么将协同信号压缩为不可解释的向量，要么依赖高延迟的多轮工具调用。本文切入点在于将多智能体的推理过程离线转化为文本轨迹，并通过蒸馏内化至单模型。具体做法是构建多智能体教师系统生成含工具调用的轨迹，经SFT与GRPO两阶段训练得到单智能体学生模型。该方法在效率与精度间取得了平衡，但其对静态协同信号的依赖及跨域泛化能力的边界仍需审慎评估。

】

---

【Multimodal Item Scoring for Natural Language Recommendation via Gaussian Process Regression with LLM Relevance Judgments ｜高斯过程回归增强的大语言模型自然语言推荐

作者：Yifan Simon Liu、Qianfeng Wen、Jiazhou Liang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d2d70c92690a)

> 自然语言推荐（NLRec）旨在根据用户自由文本请求生成物品建议，但现有密集检索（DR）方法将请求嵌入视为唯一相关性信号，导致评分函数呈单峰分布，无法捕捉复杂请求中分散在不同语义区域的多模态相关性。本文提出GPR-LLM，利用少量大语言模型（LLM）标注的锚点段落，通过高斯过程回归（GPR）估计底层相关性函数，以突破DR的单峰假设。该方法在四个NLRec数据集上较基线提升最高65%，但其性能增益是否完全源于GPR的外推能力而非LLM骨干本身，尚需更严格的消融验证。

】

---

【ReasonRec: A Reasoning-Augmented Multimodal Agent for Unified Recommendation ｜推理增强的多模态智能体推荐

研究机构：Meta AI、美国密歇根州立大学

作者：Yihua Zhang、Mingfu Liang、Jiyan Yang 等 14 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.28357)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.28357)

> 多模态推荐系统长期依赖黑盒前向推理，将意图推断、语义评估与效用权衡压缩为不透明的打分机制，导致在冷启动与跨域场景下缺乏透明度与鲁棒性。现有视觉语言模型（VLM）虽能融合多模态特征，但无法显式量化自身不确定性，也无法动态调用外部轻量模型以平衡计算成本。ReasonRec 通过构建“观察-深思-行动”三阶段智能体管道，结合证据地平线课程学习与不确定性引导的工具委托，将推荐重构为可解释的自适应决策过程。该框架在多项基准上显著提升了排序指标并降低了推理延迟，但其对预训练 VLM 骨干及手工指令模板的强依赖，限制了其在资源受限环境下的泛化潜力。

】

---

【UCGRec: User-Centric Graph Learning for LLM-based Sequential Recommendation ｜用户中心图学习驱动的LLM序列推荐

作者：HanBeul Kim、CheolWon Na、Suyoung Bae 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c3516609da12)

> 序列推荐的核心矛盾在于LLM缺乏实时交互数据，导致无法精准捕捉用户动态偏好。现有方法或依赖随机采样引入噪声，或仅利用单一偏好维度，忽视了不同偏好信号间的结构关联。UCGRec通过构建用户中心图，将长期、短期及协同偏好统一为结构化知识，并联合训练图神经网络与LLM适配器以注入该知识。该方法在四个基准数据集上显著优于现有LLM基线，但其对图构建计算开销的敏感性以及在稀疏图场景下的性能波动，限制了其在超大规模工业场景中的直接适用性。

】

---

【Unleashing the Native Recommendation Potential: LLM-Based Generative Recommendation via Structured Term Identifiers ｜基于结构化术语标识符的生成式推荐

作者：Zhiyang Zhang、Junda She、Kuo Cai 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7e2b163165fe)

> 生成式推荐旨在利用大语言模型（LLM）的语义理解能力替代传统判别式打分，但现有方案在物品标识符构建上陷入两难：文本标识符易致幻觉，语义标识符（SID）则需高昂的词表扩展与对齐成本。本文提出术语标识符（Term ID, TID），利用LLM原生词汇构建结构化关键词序列，通过上下文感知生成与弹性标识符接地机制，在保持语义丰富性的同时抑制幻觉。该框架在多个基准上超越了基于SID的SOTA方法，但其跨域优势是否源于TID的通用语义而非模型规模，仍需更严格的对照实验验证。

】
