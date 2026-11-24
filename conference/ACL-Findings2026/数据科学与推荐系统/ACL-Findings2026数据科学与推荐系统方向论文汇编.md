# ACL-Findings2026 · 数据科学与推荐系统方向论文汇编

> 本方向共 9 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Adaptive and Representative Multi-Interest Modeling for Recommendation with Large Language Model ｜LLM驱动的多兴趣自适应建模

研究机构：新加坡南洋理工大学

作者：Ziyan Wang、Yingpeng Du、Tianjun Wei 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_060eaf6b0d96)

> 多兴趣推荐旨在突破单一向量对用户多元偏好的表达局限，但现有方法依赖共现统计等启发式规则，难以捕捉语义层面的兴趣边界。本文指出直接调用大语言模型（LLM）进行兴趣分析存在粒度不可控与个体视角缺失两大瓶颈，提出LARMI框架。该框架通过自适应对齐模块校准LLM生成的语义簇，并利用最大覆盖问题合成代表性用户以扩展全局视角。该方法在多个基准上超越了传统多兴趣基线，但其性能增益是否完全源于LLM的语义推理能力，还是受限于特定数据集的规模，仍需进一步审视。

】

---

【AutoPKG: An Automated Framework for Dynamic E-commerce Product-Attribute Knowledge Graph Construction ｜动态电商属性知识图谱自动构建

研究机构：新加坡南洋理工大学、新加坡国立大学

作者：Pollawat Hongwimol、Haoning Shang、Chutong Wang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.16950)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16950)

> 电商属性抽取长期受限于静态本体无法适应长尾库存与多语言噪声，导致覆盖率不足且维护成本高昂。现有方法多假设固定标签空间，缺乏对Schema动态演化与全局一致性的联合优化。AutoPKG通过多智能体协作与集中式决策代理，实现了从空图谱到规范知识图谱的增量构建。该框架在工业界验证了商业价值，但其依赖大模型共识的评估机制与集中式写入瓶颈仍存疑。

】

---

【Beyond Topology: Generative Node Importance Estimation via Structure-Guided Semantic Reasoning ｜超越拓扑：基于结构引导语义推理的节点重要性估计

研究机构：北京邮电大学

作者：Kuofei Fang、Siyan Wu、Yu Guo 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ed6425111283)

> 节点重要性估计（NIE）旨在量化知识图谱（KG）中实体的显著性，但现有方法受限于监督范式与局部拓扑聚合，导致跨域泛化能力薄弱。GenNIE 将 NIE 重构为生成式推理任务，通过混合参数高效微调（Hybrid PEFT）联合优化生成损失与结构对比损失，使大语言模型（LLM）在冻结骨干下直接输出重要性分数。该方法在 FB15K 上 NDCG@100 达 0.9755，显著优于 GNN 基线，但其对大规模稀疏图的感知瓶颈及端到端架构的误差累积风险仍存疑。

】

---

【CogNet-KG: Empowering Tutoring Dialogues with a Cognitively-Structured Knowledge Graph for STEM Learning ｜认知结构化教育知识图谱驱动的教学对话生成

研究机构：北京师范大学

作者：Ding Yu、Yu Lu、Tengju Li 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_df64b9f4a5b8)

> 智能辅导系统（Intelligent Tutoring System, ITS）面临的核心困境是，大语言模型（Large Language Model, LLM）虽具备流畅的对话能力，却缺乏基于认知逻辑的引导式推理能力，导致无法有效诊断学生误区或促进概念迁移。现有教育知识图谱（Educational Knowledge Graph, EKG）多局限于单一学科或简单的语义/顺序关系，且未与具体学习目标绑定，致使图谱结构无法直接转化为教学决策。本文通过构建跨学科、认知结构化的 CogNet-KG，并以此生成自适应教学对话数据集，训练出内化图谱逻辑的专用模型 CogTutor-LM。该方案在自建基准上显著提升了教学连贯性与指导合理性，但其有效性依赖于特定 STEM 领域的结构化数据，且缺乏对图谱结构因果贡献的独立验证。

】

---

【EULoInf: Efficient Hessian-Free Entropy Based Uncertainty-Aware Data Influence Approximation ｜基于预测熵与单层梯度的无Hessian数据影响近似

研究机构：新加坡国立大学

作者：Runxin Cai、Jingtan Wang、Bryan Kian Hsiang Low

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_457afefd083e)

> 大语言模型微调中的数据估值面临逆Hessian-向量积（iHVP）计算带来的二次复杂度瓶颈，导致现有影响函数近似方法在大规模模型上内存与时间开销不可接受。EULoInf 抓住高影响数据与高预测熵之间的统计相关性，利用前向传播获取的Rényi熵替代昂贵的梯度范数计算，并引入仅针对最后一层的梯度点积符号以区分有益与有害样本。该方法将计算复杂度从二次降至线性，在GSM8K等任务上以41.13%的计算时间超越了最佳基线2.93%的精度，但其单层梯度近似在深层网络中的方向判别保真度仍存疑。

】

---

【HORIZON: A Benchmark for In-the-wild User Behaviour Modeling ｜HORIZON：跨域长时序用户行为建模基准

研究机构：美国卡内基梅隆大学、微软研究院

作者：Arnav Goel、Pranjal A Chitale、Bhawna Paliwal 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17259)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17259)

> 序列推荐领域长期依赖单域、短窗口的下一项预测任务，导致模型在真实多平台、长周期场景下的泛化能力被高估。现有基准如Amazon Reviews按类别隔离交互，无法捕捉跨域转移，且Leave-One-Out评估存在时间泄漏，掩盖了分布偏移下的性能衰减。HORIZON通过合并Amazon Reviews全类别构建54.51M用户的统一历史，并引入全局时间截断与用户可见性解耦的四象限评估协议，系统量化了模型在时间外推与未见用户场景下的鲁棒性边界。该基准揭示了Transformer骨干在分布偏移下的显著退化及LLM零样本建模的局限，但其评估协议对计算效率的忽视及基线覆盖的缺失，限制了其对工业部署可行性的全面判断。

】

---

【MaskTab: Scalable Masked Tabular Pretraining with Scaling Laws and Distillation for Industrial Classification ｜MaskTab：面向工业级高缺失表格数据的自监督预训练与蒸馏框架

研究机构：浙江大学

作者：Bo Zheng、Yudong Chen、Zihua Xiong 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.11408)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.11408)

> 导读 工业级表格数据面临高维稀疏、缺失值蕴含信号且标签稀缺的三重困境，传统梯度提升树（GBDT）虽鲁棒但缺乏自监督预训练机制，而现有表格基础模型受限于中小规模数据假设，难以处理大规模真实分布。MaskTab 将缺失值编码为可学习令牌，通过双路径混合预训练联合优化掩码重建与任务监督，并利用混合专家（MoE）路由处理高维特征交互。该框架在工业基准上实现了超越 GBDT 的性能，并验证了数据、特征与模型规模的扩展规律，但其对私有数据的依赖与合成数据范式的偏离使其泛化边界尚存疑。

】

---

【Self-Reinforcing Controllable Synthesis of Rare Relational Data via Bayesian Calibration ｜关系数据生成器与动态引导

研究机构：德国慕尼黑大学

作者：Chongsheng Zhang、Hao Wang、Zelong Yu 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.16817)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16817)

> 导读 不平衡分类任务中，少数类样本的稀缺导致模型泛化能力受限，而大语言模型（LLM）在结构化表格数据合成中的应用尚处于早期阶段，缺乏有效的质量迭代机制。现有基于提示词的方法（如EPIC）采用静态生成策略，无法在合成过程中动态修正分布偏差，导致生成数据与真实数据的统计一致性不足。本文提出RDDG框架，通过核心集选择、关系挖掘与自强化反馈闭环，将LLM的上下文学习转化为贝叶斯校准过程，实现约束驱动的可控合成。该方法在不平衡分类任务上取得了显著的性能提升，但其数值保真度是否足以替代专用生成模型仍存疑。

】

---

【SocraticKG: Knowledge Graph Construction via QA-Driven Fact Extraction ｜问答驱动的知识图谱构建

研究机构：韩国首尔大学

作者：Sanghyeok Choi、Woosang Jeon、Kyuseok Yang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5480c8804628)

> 大语言模型（LLM）直接抽取三元组常因缺乏全局语义视角导致图谱碎片化，而预定义实体结构又易造成事实遗漏。SocraticKG 将问答对（QA）形式化为结构化中间表示，通过 5W1H 引导的语义展开平衡事实覆盖与结构连贯。该方法在 MINE 基准上以 96.3% 的事实保留率领先，但其对 LLM 推理能力的依赖及计算成本尚未充分量化，限制了其在资源受限场景下的适用性。

】
