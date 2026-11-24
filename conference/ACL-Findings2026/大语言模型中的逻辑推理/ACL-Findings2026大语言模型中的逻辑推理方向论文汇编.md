# ACL-Findings2026 · 大语言模型中的逻辑推理方向论文汇编

> 本方向共 12 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Beyond Memorization: Testing LLM Reasoning on Unseen Theory of Computation Tasks ｜确定性有限自动机构建中的记忆与推理解耦评估

作者：Shlok Shelat、Jay Raval、Souvik Roy 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.13392)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.13392)

> 大语言模型在形式语言任务上的高分表现长期引发“符号推理”与“模式匹配”的本体论争论，现有基准因缺乏对训练数据记忆的严格隔离，无法区分模型是执行了组合泛化还是检索了相似样例。本文通过构建包含已见（Seen）与未见（Unseen）分割的确定性有限自动机（DFA）构建基准，利用阿登定理逆向生成结构新颖的正则表达式，量化了模型在组合泛化上的性能断层。实验表明，模型在知识问答与已见任务上表现优异，但在未见任务上准确率骤降30-64%，且思维链提示未能缓解该缺陷，揭示了LLM在符号状态跟踪上的根本局限。

】

---

【Code over Words: Overcoming Semantic Inertia via Code-Grounded Reasoning ｜代码接地推理：克服语义惯性

研究机构：北京大学、美国加州大学伯克利分校

作者：Manjie Xu、Isabella Yin、Xinyi Tu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.18352)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.18352)

> 动态本体环境要求模型抑制预训练先验以执行非单调推理，但现有自然语言推理方法因分布语义纠缠导致大模型出现逆缩放现象。本文切入点在于将规则表示从描述性文本转换为可执行代码，通过反事实对比对齐训练实现摊销理论归纳。该方法在Baba Is You环境中显著优于推理时搜索基线，但局限于特定游戏环境且未验证通用逻辑任务迁移性。

】

---

【Evaluating Implicit Biases in LLM Reasoning through Logic Grid Puzzles ｜逻辑谜题推理中的隐性偏见评估

研究机构：美国罗格斯大学、美国约翰斯·霍普金斯大学

作者：Fatima Jahara、Mark Dredze、Sharon Levy

论文原文见 [arXiv](https://arxiv.org/abs/2511.06160)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.06160)

> 大语言模型（LLM）在安全对齐后仍可能在复杂推理中受社会刻板印象驱动，导致决策偏差。现有偏见检测多依赖开放式生成，难以客观量化推理过程中的隐性偏差，且逻辑推理评测常忽略偏见对演绎过程的干扰。本文提出PRIME框架，通过生成中性、刻板与反刻板三种逻辑网格谜题变体，利用编辑距离量化模型在演绎推理中对人口统计学线索的依赖。该框架填补了“推理公平性”评估空白，但其结论局限于性别偏见与特定谜题规模，未验证神经符号方法能否同时消除逻辑错误与偏见。

】

---

【Evaluating Reasoning Models for Queries with Presuppositions ｜预设谬误下的推理模型事实可靠性评估

作者：Rose Sathyanathan、Kinshuk Vasisht、Danish Pruthi

论文原文见 [arXiv](https://arxiv.org/abs/2605.03050)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b0cfbb8803a1)

> 用户查询常包含未经证实的隐含假设，若模型盲目接受，将强化错误认知。现有研究多聚焦于传统大语言模型（LLM）在预设谬误下的表现，却忽略了近期兴起的大推理模型（LRM）是否因具备中间推理能力而能更有效地识别并反驳这些错误前提。本文构建了涵盖健康、科学与通用知识的预设强度梯度查询集，系统评估了多种主流模型在事实准确性与决策坚定性上的表现。研究发现，推理能力仅带来2–11%的准确率提升，且未能扭转模型随预设强度增加而倾向于附和错误前提的根本趋势，其价值在于揭示了当前推理机制在事实核查场景下的局限性，但缺乏对错误根源的机制级解释。

】

---

【How Language Models Conflate Logical Validity with Plausibility: A Representational Analysis of Content Effects ｜逻辑有效性与事实可信度的表征解耦

作者：Leonardo Bertolazzi、Sandro Pezzelle、Raffaella Bernardi

论文原文见 [arXiv](https://arxiv.org/abs/2510.06700)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d22dacd24127)

> 大语言模型在逻辑推理中常受语义内容干扰，将“事实为真”误判为“逻辑有效”，这一现象称为内容效应。现有研究多关注长链推理的准确率衰减，却忽视了短链推理中语义与逻辑的表征纠缠机制。本文通过提取并干预潜空间中的线性方向，揭示了这种混淆的几何根源。该工作为理解模型内部逻辑偏差提供了微观证据，但其干预手段是否真正改变了推理路径仍存疑。

】

---

【Logical Structure as Knowledge: Enhancing LLM Reasoning via Structured Logical Knowledge Density Estimation ｜结构化逻辑知识密度（SLKD）驱动的大语言模型推理增强

研究机构：英国爱丁堡大学、浙江大学

作者：Zhen Bi、Zhenlin Hu、Xueshu Chen 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.24836)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24836)

> 大语言模型（LLM）的推理能力长期被归因于参数规模扩张，但数据质量对推理涌现的潜在作用被低估。现有数据中心范式多将“质量”等同于事实性覆盖或多样性，忽视了文本内部蕴含的逻辑拓扑复杂度，导致训练数据中高密度逻辑样本被低密度事实性样本稀释。本文提出结构化逻辑知识密度（Structured Logical Knowledge Density, SLKD）度量，将自然语言分解为谓词逻辑原语并计算其组合拓扑复杂度，进而设计两阶段重认知优化策略，通过密度加权采样重塑模型认知框架并强化推理路径。该策略在不增加数据总量的前提下显著提升了小模型在逻辑基准上的表现，但其依赖LLM进行逻辑蒸馏的循环性，以及仅验证于微调阶段的有效性，使其在预训练及复杂OOD泛化场景下的普适性存疑。

】

---

【MAC-Reasoner: A Multi-Agent Collaborative Framework for Enhancing Logical Reasoning in Large Language Models ｜逻辑增强上下文

作者：Yehua Lin、Liping Zheng、Yin Chen

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_df0cb4b987cb)

> 大语言模型在严格演绎推理中常因幻觉或忽略约束而失效，纯神经方法缺乏逻辑严谨性，而传统神经符号方法将模型降格为翻译器，无法利用其内部推理能力。MAC-Reasoner 通过构建逻辑增强上下文，将外部求解器的符号证据转化为自然语言参考，引导模型自主完成最终推理。该方法在多个基准上显著提升了不同规模模型的准确率，并验证了推理轨迹可用于监督微调。其价值在于平衡了求解器的可靠性与模型的自主性，但效果高度依赖翻译准确性，且未解决长程推理中的状态一致性问题。

】

---

【ReasonIF: Large Reasoning Models Fail to Follow Instructions During Reasoning ｜推理轨迹指令遵循基准与微调策略

研究机构：美国斯坦福大学

作者：Yongchan Kwon、Shang Zhu、Federico Bianchi 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.15211)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.15211)

> 大推理模型（Large Reasoning Models, LRMs）在生成最终答案时往往能遵循用户指令，但在生成中间推理轨迹时却频繁违背格式、语言或长度约束，导致过程不可控且难以审计。现有指令遵循评估仅关注主响应，忽视了推理过程本身的合规性，而强化学习训练侧重答案正确性，未对推理轨迹施加约束。本文提出ReasonIF基准，通过可验证指令自动评估推理轨迹的指令遵循得分（Instruction Following Score, IFS），并设计推理指令微调（Reasoning Instruction Finetuning, RIF）策略。该工作揭示了推理过程可控性的严重缺失，但RIF仅验证了单一模型上的初步效果，未证明其对逻辑严谨性的增益。

】

---

【Self-Awareness before Action: Mitigating Logical Inertia via Proactive Cognitive Awareness ｜行动前自我意识：通过主动认知感知缓解逻辑惯性

研究机构：吉林大学

作者：Fulong Fan、Peilin Liu、Fengzhe Liu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.20413)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.20413)

> 大语言模型在非交互式长叙事推理中面临“信息不对称”困境，即模型需在固定文本中重构隐藏真相，却常因早期假设固化导致错误传播。现有思维链（Chain-of-Thought, CoT）与后置修正方法缺乏对前提完整性的前置审计，无法阻断初始错误向后续推理的扩散。SABA框架通过“信息融合”构建结构化基线状态，并采用“查询驱动结构化推理”递归解决缺失前提，实现了从直接预测到状态评估的范式转移。该框架在自建侦探谜题基准上显著优于基线，但其依赖骨干模型自评估能力的局限及较高的推理成本，限制了其在实时场景与小型模型中的泛化潜力。

】

---

【Training Language Models to Use Prolog as a Tool ｜强化学习驱动的大语言模型Prolog工具调用

作者：Niklas Mellgren、Peter Schneider-Kamp、Lukas Galke Poech

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_556f75183209)

> 导读 大语言模型（LLM）在逻辑推理中常产生看似合理实则错误的思维链，这种“忠实性差距”使得纯文本推理难以满足安全关键领域的审计需求。现有神经符号方法多依赖监督微调或提示工程，导致小模型难以掌握Prolog等小众符号语言，且缺乏对推理过程的结构化约束。本文切入点在于利用可验证奖励强化学习（RLVR）训练3B参数模型将Prolog作为外部工具，通过执行反馈闭环实现可审计推理。该方案在GSM8K验证集上超越7B基线，但揭示了准确率与可审计性之间的根本权衡，其泛化能力在测试集上显著衰减。

】

---

【Unlocking Human-Like Visible Logic: How Logic Diagrams Boost Logic Reasoning in Large Language Models? ｜视觉逻辑图辅助大语言模型推理

研究机构：华南理工大学

作者：Xin Wu、Yuqi Bu、Mengchen Zhao 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ffb749ddc497)

> 大语言模型（LLMs）在处理形式逻辑时，常因文本表征的边界模糊而推导失效。现有神经符号融合路线依赖外部求解器，成本高且缺乏直观性；纯文本提示工程则难以显式呈现集合间的空间关系。本文切入点在于利用视觉逻辑图（Venn、Euler、Linear）作为中间表征，直接输入视觉语言模型（VLMs）以辅助推理。通过程序化生成图表并对比不同对齐策略，本文发现视觉辅助在有效案例上提升显著，但在无效案例上引发“过度依赖”导致准确率下降。该研究提供了受控实证框架，但缺乏强文本基线对比，其增益是否源于视觉本质仍存疑。

】

---

【Where Reasoning Breaks: Logic-Aware Path Selection by Controlling Logical Connectives in LLMs Reasoning Chains ｜逻辑连接词干预下的推理路径选择

研究机构：美国佛罗里达大学

作者：Seunghyun Park、Yuanyuan Lei

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_047d76711f65)

> 导读 大语言模型在多步逻辑推理中常因单点错误导致全链失效，现有全局搜索或神经符号验证方案计算开销大且依赖外部形式化。本文切入点在于识别出逻辑连接词是推理链中熵值最高、因果杠杆最大的脆弱节点，通过激活引导、局部分支和针对性偏好优化三层机制精准干预这些节点。该方法在保持贪心解码效率的同时提升了推理稳定性，但其有效性受限于连接词定义的边界及缺乏强基线对比。

】
