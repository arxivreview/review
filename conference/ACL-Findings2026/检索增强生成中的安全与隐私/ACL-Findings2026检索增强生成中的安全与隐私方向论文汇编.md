# ACL-Findings2026 · 检索增强生成中的安全与隐私方向论文汇编

> 本方向共 14 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Systemic Evaluation of Multimodal RAG Privacy ｜多模态检索增强生成隐私泄露评估

作者：Ali Al-Lawati、Suhang Wang

论文原文见 [arXiv](https://arxiv.org/abs/2601.17644)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.17644)

> 多模态检索增强生成（mRAG）通过引入外部图像-文本库提升视觉语言模型（VLM）的准确性，但这一机制将私有数据暴露于推理接口，导致元数据泄露风险。现有文本RAG的隐私防御机制无法直接迁移至视觉嵌入空间，且缺乏针对图像变换鲁棒性的系统评估。本文通过黑盒提示词工程，量化了成员推断攻击（MIA）与图像字幕检索（ICR）在真实视觉扰动下的成功率。该研究填补了多模态RAG隐私评估的空白，但仅验证了攻击可行性，未提供形式化防御保证。

】

---

【Context-attended Adversarial Reinforcement Learning for Robust Multi-step Retrieval Augmented Generation ｜多步检索增强生成的对抗鲁棒性

作者：Yingtao Ren、Xiao Luo、Yu-Cheng Chang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_86675022a01b)

> 多步检索增强生成（Retrieval-Augmented Generation, RAG）在迭代获取证据时，长上下文中的噪声与对抗性伪造文档会累积并导致生成器失效。现有防御方法多基于单步检索假设，缺乏对动态演化攻击的适应能力。本文提出上下文感知对抗强化学习（Context-attended Adversarial Reinforcement Learning, CARE），通过文本梯度优化与强化学习交替迭代，构建动态对抗训练闭环。该方法在多步基准上显著提升了生成准确性与抗攻击能力，但其鲁棒性是否泛化至未见过的攻击类型，仍需进一步验证。

】

---

【ConvX: A Lightweight Converter to Bridge Indexed Dense Representations and Large Language Models for Retrieval-Augmented Generation ｜检索向量直接转换的轻量级RAG压缩框架

作者：Bonggeun Choi、Keunha Kim、Junho Han 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4424a967744c)

> 长上下文导致Transformer推理延迟呈二次方增长，现有压缩方法要么依赖重型压缩器引入额外开销，要么将文档坍缩为单向量丢失细粒度信息。本文切入点在于直接复用检索器已计算的密集向量，通过轻量级转换器将其扩展为多个记忆槽，避免二次编码。该方法在保持检索器独立性的同时，实现了接近无压缩RAG的问答性能与显著的效率提升。其价值在于解耦了词汇信息保留与任务适配，但记忆槽是否构成新的隐私泄露面尚存疑。

】

---

【Differentially Private Synthetic Text Generation for Retrieval-Augmented Generation (RAG) ｜差分隐私合成文本生成用于检索增强生成

研究机构：日本东京科学大学、日本理化学研究所

作者：Junki Mori、Kazuya Kakizaki、Taiki Miyagawa 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.06719)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.06719)

> 检索增强生成（Retrieval-Augmented Generation, RAG）在敏感数据场景下面临隐私泄露风险，现有基于查询时差分隐私（Differential Privacy, DP）的方法因隐私预算随查询次数线性消耗，导致多轮交互下效用急剧下降。本文提出 DP-SynRAG，通过离线生成具备 DP 保证的合成知识库，将隐私成本从“每次查询”转移至“一次性生成”，从而在固定预算下支持无限次查询。该方法结合 DP 软聚类与私有预测机制，在医疗等垂直领域显著优于查询时 DP 基线，但其对动态知识库的适应性及长尾知识保留能力尚存疑。

】

---

【Knowledge-Infused Multi-Bit Watermarking for RAG Knowledge Bases ｜知识注入多比特水印

作者：Ke Yang、Shuguang Yuan、Jing Yu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bdaf97edbb86)

> RAG系统依赖外部知识库提升生成准确性，但这些知识库蕴含高价值知识产权，面临被窃取风险。现有水印方法要么改写原文导致质量下降，要么注入低质文本损害检索效用，且仅能编码1比特信息，无法承载版权元数据。KMW将水印嵌入重构为良性知识补全任务，通过无偏生成算法注入多比特水印文本，并设计索引器优化检测查询。该方案在恢复率与隐蔽性上优于基线，但其高查询成本与对LLM生成质量的依赖限制了实际部署的灵活性。

】

---

【LeakDojo: Decoding the Leakage Threats of RAG Systems ｜检索增强生成泄露风险解耦评估

研究机构：清华大学、新加坡南洋理工大学

作者：Maosen Zhang、Jianshuo Dong、Boting Lu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.05818)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.05818)

> 检索增强生成（RAG）在提升大语言模型（LLM）知识时效性的同时，将外部知识库暴露为数据提取攻击面，现有研究缺乏对泄露机制的系统性量化。传统攻击评估将查询生成与指令注入视为整体，无法区分架构组件对风险的独立贡献，导致防御策略缺乏针对性。本文提出模块化评估框架 LeakDojo，将 RAG 系统、攻击策略与防御机制解耦为可独立配置的组件，通过控制变量实验揭示泄露风险的内在机制。该框架提供了可复现的评估基准，但仅针对文本模态，且未解决高指令遵循模型泄露风险的根本抑制问题。

】

---

【Learning to Extract Rational Evidence via Reinforcement Learning for Retrieval-Augmented Generation ｜理性证据提取

作者：Xinping Zhao、Shouzheng Huang、Yan Zhong 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2507.15586)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_76bb57466d0c)

> 检索增强生成（RAG）面临的核心矛盾是检索噪声与生成准确性的冲突，现有证据提取方法因缺乏深层上下文理解而丢失关键线索。本文切入点在于将“先推理后提取”的理性证据范式与基于可验证奖励的强化学习结合，解决监督微调（SFT）依赖启发式标注导致的泛化不足问题。EviOmni 通过 Group Relative Policy Optimization (GRPO) 优化证据提取策略，在五个基准上实现了高压缩率与高准确率的平衡。其价值在于证明了推理机制对检索鲁棒性的提升，但仅针对随机噪声，未验证对对抗性投毒的有效性。

】

---

【Masking or Mitigating? Deconstructing the Impact of Query Rewriting on Retriever Biases in RAG ｜查询改写对密集检索器偏差的解耦与缓解机制

作者：Agam Goyal、Koyel Mukherjee、Apoorv Saxena 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e61f2510417d)

> 密集检索器在RAG系统中存在系统性偏差，导致检索结果偏离事实依据。现有查询增强技术虽能提升检索效率，但其对偏差的影响机制不明，可能掩盖而非消除问题。本文通过控制变量实验，量化五种查询改写策略对四种偏差类型的差异化影响，揭示简单改写与伪文档生成在机制上的根本差异。该研究提供了偏差感知的部署指南，但未能解决编码型偏差的根源问题。

】

---

【PRA-RAG: Provably Robust Aggregation in Retrieval-Augmented Generation against Retrieval Corruption ｜可证明鲁棒检索聚合

研究机构：复旦大学、美国伍斯特理工学院

作者：Xue Tan、Yi Zheng、Chang Huo 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.00012)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.00012)

> 检索增强生成（Retrieval-Augmented Generation, RAG）系统面临外部知识库投毒攻击，导致生成结果被恶意操纵。现有防御机制依赖大语言模型（LLM）内部知识进行启发式检测，缺乏理论保证且在模型知识不足时失效。本文提出PRA-RAG，通过在嵌入空间构建最小半径球进行组合聚合，提供语义偏差的理论上界。该方法在保持高准确率的同时将攻击成功率降至1%，但组合爆炸限制了检索规模的扩展性。

】

---

【Privacy-Preserving Reasoning with Knowledge-Distilled Parametric Retrieval Augmented Generation ｜知识蒸馏对齐的参数化检索增强生成

研究机构：北京航空航天大学、中国科学院

作者：Jinwen Chen、Hainan Zhang、Liang Pang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_32d51663ab1b)

> 参数化RAG（PRAG）旨在通过将文档编码为LoRA参数替代明文传输，解决云端推理时的隐私泄露风险，但现有方案因依赖逐文档微调或单文档映射，导致推理延迟高且跨文档推理能力缺失。本文指出PRAG与标准RAG在文档结构和参数激活上的内部不对齐是泛化失效的根源，提出DistilledPRAG，通过跨文档QA合成与知识蒸馏对齐师生模型隐状态。该方法在OOD数据集上实现了优于基线的F1分数，但其隐私保护缺乏形式化保证，且未量化参数生成器本身可能引入的新泄露风险。

】

---

【Reflective RAG: Self-Evaluation Driven Strategy Optimization in Agentic Retrieval-Augmented Generation ｜反思式检索增强生成

作者：Haiyan Wu、Chenchen Wang、Chaoqun Sun 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b04a885b061f)

> 代理式检索增强生成（Agentic RAG）旨在解决多跳推理中静态检索无法动态整合外部知识的困境，但现有强化学习（RL）方法仅依赖最终答案正确性作为奖励，导致模型在中间检索步骤缺乏对信息效用的显式评估，易陷入盲目检索或过早终止。本文切入点在于将自评估信号从被动监督转化为主动策略约束，通过基于困惑度（Perplexity, PPL）变化的标签自校正与评估引导的KL正则化，实现检索策略与评估语义的协同优化。该方法在五个基准上超越了Search-R1等强基线，但其性能增益是否源于评估信号的内在可靠性，还是仅依赖于特定语料库的分布特性，仍需进一步验证。

】

---

【Relevance to Utility: Process-Supervised Rewrite for RAG ｜从相关性到效用：RAG桥接模块的联合推理轨迹蒸馏

研究机构：韩国首尔大学

作者：Jaeyoung Kim、Jongho Kim、Seung-won Hwang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.15577)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.15577)

> 检索增强生成（RAG）系统长期面临检索相关性与生成效用脱节的问题，现有桥接模块因依赖独立重写与二元结果监督，在复杂推理任务中失效。本文提出R2U框架，通过联合观察重写与答案生成的推理轨迹，并基于下游生成器的效用改进量构造软标签，解决监督信号与文档实际贡献脱钩的困境。该方法将平均F1提升6.8%pt，但在对抗性安全威胁下的鲁棒性及多模态场景的适用性尚未验证。

】

---

【Rethinking Retrieval-Augmented Generation as a Cooperative Decision-Making Problem ｜协同检索增强生成

研究机构：吉林大学

作者：Lichang Song、Ting Long、Yi Chang

论文原文见 [arXiv](https://arxiv.org/abs/2602.18734)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.18734)

> 检索增强生成（Retrieval-Augmented Generation, RAG）旨在通过外部知识缓解大语言模型（LLM）的幻觉，但现有架构中重排序器与生成器存在非对称依赖，导致生成质量对排序结果过度敏感。主流方法独立优化两个组件，忽视了二者在任务目标上的耦合性，使得系统在排序噪声下稳定性不足。本文提出CoRAG，将二者重构为共享任务奖励的协同决策智能体，通过联合优化降低生成器对细粒度排序的依赖。该框架在仅使用1万条训练数据的情况下实现了跨数据集的泛化，但其重排序器独立性能受限，揭示了协同优化中组件解耦的潜在代价。

】

---

【RIPRAG: Hack a Black-box Retrieval-Augmented Generation Question-Answering System with Reinforcement Learning ｜基于黑盒反馈强化学习的检索增强生成投毒攻击

研究机构：浙江大学

作者：Meng Xi、Sihan Lv、Yechen Jin 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.10008)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.10008)

> 检索增强生成（Retrieval-Augmented Generation, RAG）系统因引入外部知识库而面临投毒威胁，但现有黑盒攻击方法依赖静态启发式或失配的代理模型，在低投毒率与复杂检索架构下失效。RIPRAG 将目标系统视为不透明环境，通过强化学习从黑盒交互反馈中动态优化投毒文档生成策略。该方法在复杂检索设置下将攻击成功率（ASR）提升至 0.49-1.00，显著优于基线，但仅验证了文本模态与特定防御机制，未覆盖多模态或动态更新场景。

】
