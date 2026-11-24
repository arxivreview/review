# ACL-Findings2026 · 机器翻译评估与质量估计方向论文汇编

> 本方向共 8 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Just Use XML: Revisiting Joint Translation and Label Projection ｜标签感知翻译：XML标记下的联合翻译与投影

研究机构：美国麻省理工学院

作者：Thennal DK、Chris Biemann、Hans Ole Hatzel

论文原文见 [arXiv](https://arxiv.org/abs/2603.12021)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.12021)

> 跨语言迁移中，如何将高资源语言的跨度标注准确投射至低资源语言译文，同时不牺牲翻译质量，是制约NLP任务多语言扩展的核心瓶颈。现有方法要么将翻译与投影分步执行导致工程复杂度高，要么采用联合建模但被证实会损害译文质量。本文切入点在于挑战“标记必然降低翻译质量”的既有假设，提出基于XML标签的联合翻译与投影框架LabelPigeon。该方法通过微调预训练翻译模型，在单次前向传播中同时完成翻译与标签转移。其价值在于证明了联合建模不仅不损害质量，反而因额外训练提升了译文质量，但其在低资源语言及非QA任务上的泛化边界仍需进一步验证。

】

---

【LQM: Linguistically Motivated Multidimensional Quality Metrics for Machine Translation ｜语言学动机多维质量指标

研究机构：加拿大不列颠哥伦比亚大学

作者：Samar M. Magdy、Fakhraddin Alwajih、Abdellah El Mekki 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18490)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18490)

> 机器翻译评估在双言制语言中面临核心困境：通用指标无法区分社会语言学变体错配与语义错误。现有MQM协议将异质错误归入“Mistranslation”导致诊断失效，本文切入点在于构建基于语言学层级的分类法以定位错误根源。LQM通过六层语言学框架重新组织错误标注，实现方言敏感的诊断。其价值在于揭示了方向依赖的失败模式，但人工标注的高成本限制了自动部署的可行性。

】

---

【On Temperature-Constrained Non-Deterministic Machine Translation: Potential and Evaluation ｜温度约束下的非确定性机器翻译评估

研究机构：香港城市大学、OpenAI

作者：Weichuan Wang、Mingyang Liu、Chen Ma 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2209a87e8869)

> 机器翻译长期受困于多模态性，即同一源句存在多个有效译文，导致单一参考基准失效。传统确定性评估范式无法处理非确定性采样产生的候选分布，且现有指标在排名稳定性上表现不佳。本文通过引入组级词汇方差指标与期望采样策略，量化了非确定性系统在词汇多样性与语义等价间的平衡。该工作揭示了“桶底效应”对系统排名的主导作用，但其在低资源语言及长文本场景下的泛化能力仍存疑。

】

---

【PEGRL: Improving Machine Translation by Post-Editing Guided Reinforcement Learning ｜后编辑引导的强化学习

研究机构：南京大学

作者：Yunzhi Shen、Hao Zhou、Xin Huang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0629e962232a)

> 机器翻译中的强化学习（RL）长期受困于蒙特卡洛回报估计的高方差，导致策略梯度信号噪声大、训练不稳定。现有基于组相对策略优化（GRPO）的方法仅优化翻译轨迹，忽略了局部精修环节对全局探索的引导作用。PEGRL 将后编辑（Post-Editing, PE）建模为辅助任务，利用其低方差的回报估计稳定翻译策略更新，并通过方差感知加权平衡两任务贡献。该方法在低资源方向上显著优于纯RL基线，但奖励函数对特定质量估计指标的依赖可能引入过拟合风险。

】

---

【Remedy-R: Generative Reasoning for Machine Translation Evaluation without Error Annotations ｜生成式推理机器翻译评估

研究机构：荷兰阿姆斯特丹大学、新加坡管理大学

作者：Shaomu Tan、Ryosuke Mitani、Ritvik Choudhary 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_abcd582f3a7f)

> 机器翻译自动评估长期面临标量指标不可解释与闭源大模型高成本的双重困境。现有神经回归指标虽高效但缺乏诊断能力，而依赖提示工程的大语言模型评估器则受限于评分一致性与外部API依赖。本文切入点在于利用可验证奖励强化学习直接训练开源模型，使其在无错误标注条件下生成多维分析并输出校准分数。该方法在WMT22-25基准上达到了与顶级闭源模型相当的性能，但其对片段级细粒度检测的覆盖缺失及长文档场景下的稳定性仍存疑。

】

---

【Simul-COMET: A Quality Metric for Simultaneous Interpretation in Distant Language Pair Considering Word Order Difference ｜面向同声传译单调性的神经质量指标

作者：Kosuke Doi、Mana Makinae、Yusuke Sakai 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_743a36b147b4)

> 同声传译（SI）评估面临的核心矛盾是：实时性要求译文严格遵循源文语序（单调性），但通用神经指标COMET因训练于离线数据，反而给语序重排的译文更高分数。现有方案要么忽略单调性维度，要么依赖昂贵的人工SI标注数据。本文切入点在于利用大语言模型（LLM）将离线数据自动转换为SI风格，并在分数计算中引入单调性惩罚项。通过微调COMET骨干网络，该指标在专业译员评估中展现出比基线更强的相关性，但其绝对相关系数偏低且仅验证了英日这一极端语序差异的语言对，泛化能力存疑。

】

---

【Who Watches the Watchmen? Humans Disagree With Translation Metrics on Unseen Domains ｜域外鲁棒性与人标噪声解耦

作者：Finn Schmidt、Jan Philip Wahle、Terry Ruas 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1f04ef5b9750)

> 导读 机器翻译质量估计（QE）指标在WMT基准上表现优异，但其在未见领域（如医药、化工）的可靠性长期存疑，且现有研究常因标注者差异混淆了“指标失效”与“人标噪声”。本文通过构建受控的跨域错误跨度标注数据集（CD-ESA），在固定MT系统与标注者的前提下，量化了指标在域外场景下的真实表现。研究发现，指标在段级评估中看似鲁棒，但一旦通过平均标注或分组策略降低人标噪声，其在系统级评估中的失效便暴露无遗，尤其是微调指标在化工领域存在严重的系统性低估。这一发现挑战了“指标性能下降即域外失效”的简单共识，揭示了元评估中必须将人标一致性作为参照系的重要性，但其在低资源语言及更长文档上的泛化能力仍待验证。

】

---

【XQ-MEval: A Dataset with Cross-lingual Parallel Quality for Benchmarking Translation Metrics ｜跨语言平行质量基准与归一化校准

研究机构：复旦大学

作者：Jingxuan Liu、Zhi Qu、Jin Tei 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14934)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2c761f185c2e)

> 多语言机器翻译评估长期依赖跨语言分数平均，但这一做法隐含了“同等错误在不同语言中得分相同”的假设，该假设从未被系统性验证。现有基准缺乏跨语言平行质量实例，导致无法量化指标在语言间的评分偏差。本文通过半自动注入错误构建首个九语言平行质量数据集，并实证了跨语言评分偏差的存在。其提出的归一化策略虽能缓解偏差，但基于合成数据的校准在真实系统噪声下的泛化能力存疑。

】
