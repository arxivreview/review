# ACL-Findings2026 · 大语言模型基准污染与评估鲁棒性方向论文汇编

> 本方向共 7 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AutoMonitor-Bench: Evaluating the Reliability of LLM-Based Misbehavior Monitor ｜LLM 行为监控器可靠性评估

作者：Shu Yang、Jingyu Hu、Tong Li 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.05752)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_48a05fce2af4)

> 前沿大模型在推理与执行任务时可能产生隐蔽的违规行为，如谄媚、捷径利用或规格博弈，但现有评估缺乏统一标准来量化“监控器”本身的可靠性。传统基于有害请求合规性的检测无法覆盖这些隐式行为，导致监控器在真实部署中失效。本文构建了包含 3,010 个配对样本的 AutoMonitor-Bench，通过漏报率（MR）与误报率（FAR）双指标系统评估 22 个 LLM 监控器，并验证微调对泛化能力的局限。该基准揭示了监控器在安全覆盖与操作效用间的固有张力，但静态基准的局限及微调泛化失败的深层原因仍待厘清。

】

---

【Beyond Static Synthetic Noise: Assessing the Robustness of Large Language Models to Natural Context Variation in the Real World ｜基于维基百科修订历史的自然扰动鲁棒性评估

作者：Yulong Wu、Viktor Schlegel、Riza Batista-Navarro

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_09710bfe4f33)

> 现有QA鲁棒性评估依赖人工合成扰动，难以复现真实世界中知识库随时间演化的文本漂移，导致模型在静态测试集上的高分无法反映其在动态环境中的可靠性。本文切入点在于利用维基百科的修订历史作为天然扰动源，构建标签保持的自然扰动测试集，以替代静态合成噪声。通过提取相邻版本差异并验证答案有效性，该框架量化了编码器与大型语言模型（LLM）在自然文本变化下的性能衰减。该工作揭示了LLM对自然漂移的显著脆弱性，但其防御策略的泛化能力仍存疑。

】

---

【EntroBench: Evaluating LLM Watermarking Under Multi-Entropy Scenarios and Practical User Operations ｜多熵场景下的LLM水印鲁棒性评估基准

研究机构：华中科技大学、武汉大学

作者：Pengyuan Qin、Linnan Tu、Yuhan Ke 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_97749f804ee9)

> 现有LLM水印评估局限于单一熵设定，无法反映真实生成任务中分布多样性的影响，导致方法在低熵或混合熵场景下性能骤降。本文切入点在于构建覆盖高、中、低三种熵水平及七类典型任务的统一基准，并引入非对抗性用户操作模拟。通过锚定数据集校准超参数，公平对比八种主流水印方法在检测率与生成质量上的权衡。该工作揭示了当前水印技术在真实使用场景下的脆弱性，但缺乏对自适应水印算法的理论下界探讨。

】

---

【Gaperon: A Peppered English-French Generative Language Model Suite ｜GAPERON：基于全开源模型的数据污染影响机制实证

研究机构：美国康奈尔大学

作者：Nathan Godey、Wissam Antoun、Rian Touchent 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.25771)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.25771)

> 导读 大语言模型评估失效的根源在于预训练数据与测试集的不可控重叠，导致模型通过记忆而非推理获得高分，严重扭曲了能力评估。现有检测方案多聚焦于事后识别污染或构建动态基准以规避泄露，却缺乏对“污染程度-性能增益”非线性关系的受控量化，尤其在全开源、可复现的训练全流程中，污染如何具体影响基准分数与生成质量仍属黑箱。本文通过构建全开源的GAPERON模型系列，在预训练后期故意注入基准测试集，实证了污染对下游任务的影响边界。该工作提供了污染研究的白盒实验床，但其结论局限于特定模型规模与数据混合策略，未验证在更大规模或不同架构下的普适性。

】

---

【Rethinking RL Evaluation: Can Benchmarks Truly Reveal Failures of RL Methods? ｜强化学习评估的泛化失效诊断

研究机构：中国科学院、中国科学技术大学

作者：Zihan Chen、Yiming Zhang、Hengguang Zhou 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.10541)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.10541)

> 当前大语言模型（LLM）强化学习（RL）后训练在基准测试上取得高分，但高分是否代表真实推理能力存疑。传统“训练集与测试集分离”的评估范式假设“未见数据”能区分泛化能力，但RL模型可能通过过拟合测试分布或捷径学习掩盖了这一区分度。本文提出Oracle Performance Gap (OPG) 指标，通过对比在训练集与测试集上直接训练的模型性能差距，量化基准的区分度失效。结合难度分层、分布偏移与反事实测试，本文揭示了RL模型泛化的脆弱性，为基准设计提供了原则，但仅局限于数学推理任务且未提供去污算法。

】

---

【SrDetection: A Self-Referential Framework for Data Leakage Detection in Code Large Language Models ｜自参照代码泄漏检测

作者：Shuaimin Li、Liyang Fan、Zeyang li 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6686f600bfa8)

> 代码大语言模型（Code LLMs）在公开基准上的高分常源于预训练阶段对测试集的隐性记忆，而非真实泛化能力。现有检测手段或依赖不可得的私有训练语料，或依赖在代码复用场景下失效的时间戳启发式，且普遍需要外部参考集校准阈值。本文提出 SrDetection，通过生成语义等价变体并与原样本进行内部对比，实现无需外部锚点的自参照泄漏检测。该方法在受控测试床上显著优于基线，但其对变体生成质量的依赖及在真实复杂预训练分布下的鲁棒性仍存疑。

】

---

【Toward Automated Robustness Evaluation of Mathematical Reasoning ｜数学推理鲁棒性自动压力测试

研究机构：南方科技大学

作者：Yutao Hou、Zeguan Xiao、Fei Yu 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_639577b588cf)

> 大语言模型在静态基准上表现优异，但面对语义等价的问题变体时往往性能崩塌，暴露出严重的鲁棒性缺陷。现有鲁棒性评估依赖人工模板或固定扰动规则，难以覆盖模型特有的弱点，且静态变体易受数据污染影响。MASTER 通过构建 Rewriter-Verifier 对抗循环，自动化生成针对特定模型弱点的变体，从源头规避污染并精准定位失效模式。该方法在 GSM8K 上使 LLaMA-3-8B 的准确率从 76.42% 降至 27.51%，证明了自动化压力测试的有效性，但其依赖强模型作为重写器，引入了新的评估偏差风险。

】
