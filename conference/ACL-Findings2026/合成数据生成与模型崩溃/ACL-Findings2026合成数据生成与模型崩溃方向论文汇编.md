# ACL-Findings2026 · 合成数据生成与模型崩溃方向论文汇编

> 本方向共 6 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CircuitSynth: Reliable Synthetic Data Generation ｜电路合成：基于概率句法决策图的可靠数据生成

研究机构：英国牛津大学、奥地利维也纳技术大学

作者：Zehua Cheng、Wei Dai、Jiahao Sun 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.10114)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10114)

> 合成数据生成旨在突破真实数据稀缺与隐私限制，但大语言模型（LLM）在结构化生成中常因随机采样导致幻觉、逻辑不一致及模式坍缩，即长尾分布覆盖不足。现有提示工程或检索增强生成（RAG）方法缺乏对逻辑一致性与分布覆盖的形式化保证，无法同时满足硬逻辑约束与软分布目标。CircuitSynth 提出一种神经符号框架，通过将教师 LLM 的推理能力蒸馏至概率句法决策图（PSDD），构建可处理语义先验，并引入凸优化机制强制满足分布约束。该框架在复杂逻辑谜题中实现了 100% 模式有效性，显著优于基线，但其适用性受限于约束图的树宽，高维密集约束下的可扩展性存疑。

】

---

【Data Swarms: Optimizable Generation of Synthetic Evaluation Data ｜数据群优化：合成评测数据生成的连续搜索范式

研究机构：美国华盛顿大学

作者：Shangbin Feng、Yike Wang、Weijia Shi 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_63c7c325dbc3)

> 现有合成评测数据生成方法依赖启发式提示工程，缺乏对数据质量的量化优化机制，导致生成结果难以稳定提升模型区分度或难度。本文提出 DATA SWARMS，将数据生成器视为权重空间中的粒子，通过粒子群优化（Particle Swarm Optimization, PSO）在连续参数空间中搜索最优生成策略，并引入对抗性共进化机制。该方法在四个领域上优于八种基线，但仅验证了文本任务，未解决多模态或长尾分布下的泛化问题。

】

---

【DualAlign: Generating Clinically Grounded Synthetic Data ｜双重对齐临床合成数据生成

作者：Rumeng Li、Xun Wang、Hong Yu

论文原文见 [arXiv](https://arxiv.org/abs/2509.10538)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.10538)

> 临床电子健康记录（EHR）受隐私法规严格限制，导致阿尔茨海默病（AD）等慢性病的纵向轨迹数据稀缺，而通用大语言模型（LLM）生成的文本缺乏疾病特异性与时间连贯性。现有方法多聚焦于结构化数据或无约束的通用文本生成，无法捕捉AD跨认知、功能及生理领域的复杂交互。DualAlign通过引入人口统计学统计对齐与症状轨迹语义对齐，构建了具备临床合理性的合成叙事框架。该框架在低资源场景下提升了症状分类性能，但其对长期时序动态的压缩处理仍存疑。

】

---

【HSS-Synth: Humanities and Social Sciences Data Synthesis for LLMs ｜人文社科数据合成流水线

研究机构：浙江大学、北京大学

作者：Ru Peng、Tianyu Zhao、Xijun Gu 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b5997bd83437)

> 大语言模型在人文社科（HSS）领域的表现受限于高质量、多样化指令数据的稀缺，且该领域任务缺乏可验证答案，导致现有合成方法难以直接迁移。本文提出 HSS-Synth，通过“种子文档构建-多属性指令回译-教师强制回答”三阶段流水线，系统性解决 HSS 数据合成的质量与多样性瓶颈。该方法在 16 个基准上超越 14 个基线，验证了领域特定合成策略的有效性，但其对递归训练稳定性的影响尚未被评估。

】

---

【Model in Distress: Sentiment Analysis on French Synthetic Social Media ｜基于回译与合成推理的隐私敏感合成数据流水线

作者：Pierre-Carl Langlais、Pavel Chizhov、Yannick Detrois 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_372c49b13e11)

> 隐私敏感场景下的情感分析面临标注数据稀缺、评估集匮乏及数据合规三重约束，传统直接翻译或通用合成方法难以兼顾领域语用特征与隐私保护。本文切入点在于构建“专家蒸馏”范式，利用少量真实种子数据微调辅助模型，通过回译与合成推理生成大规模高保真合成数据，而非直接依赖通用大模型生成。具体做法是训练专用生成器与推理器，产出170万条带推理轨迹的法语公交推文，用于训练600M参数的小模型。该方案在隐私合规前提下实现了小模型超越大模型的性能，但依赖专有模型生成种子数据，其可复现性与通用性边界尚存疑。

】

---

【Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning ｜合成数据源多样性对大语言模型微调的影响

研究机构：荷兰乌得勒支大学

作者：Max Schaffelder、Albert Gatt

论文原文见 [arXiv](https://arxiv.org/abs/2511.01490)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b598de7dafee)

> 大语言模型在数据受限场景下依赖合成数据微调，但单一来源的合成数据会导致输出分布收窄与长尾token增加，即分布坍缩。现有缓解策略多聚焦于递归训练中的真实数据混合或外部验证器注入，缺乏对单次微调中数据源多样性效应的系统量化。本文通过对比单一源与多源合成数据微调，发现多源数据能显著缓解分布坍缩并降低自偏好偏差，但会改变模型对抗鲁棒性的风险分布。该研究填补了微调阶段数据源多样性与模型安全、评估偏差关联性的空白，但其结论局限于特定模型规模与任务类型，长期递归场景下的有效性存疑。

】
