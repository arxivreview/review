# ACL-Findings2026 · 大语言模型中的多元价值对齐方向论文汇编

> 本方向共 7 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Beyond Marginal Distributions: A Framework to Evaluate the Representativeness of Demographic-Aligned LLMs ｜超越边际分布：基于相关结构的LLM代表性评估框架

研究机构：德国柏林洪堡大学、德国斯图加特大学

作者：Tristan Williams、Franziska Weeber、Sebastian Padó 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.15755)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4a0ad3eb59ee)

> 当前LLM对齐研究普遍依赖边际分布匹配来衡量模型对特定人口群体价值观的还原度，但这一单变量视角忽略了真实社会中不同议题间存在的深层依赖关系。现有方法如Persona Prompting与微调模型虽能改善单题回答的分布相似度，却可能掩盖了模型在多维价值空间中的结构性失效。本文提出一种结合边际分布与多变量相关结构的评估框架，通过对比问题间及主题间的相关矩阵来诊断模型的代表性。该框架揭示了现有主流引导方法在结构对齐上的系统性不足，为评估标准提供了更严格的诊断维度，但其结论是否受限于特定调查数据集的样本量仍需进一步验证。

】

---

【Choose Your Lens: Multi-Perspective Value Alignment of Chain-of-Thought Reasoning ｜价值图一致思维链

作者：Gejian Zhao、Hanzhou Wu、Xinpeng Zhang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_048abf0b17b3)

> 多元价值对齐旨在使大语言模型（LLM）输出反映人类价值观的多样性，而非收敛于单一共识。现有可引导对齐方法在文本空间操作，常导致模型为迎合特定视角而幻觉“便利事实”，破坏跨视角的事实一致性。本文提出VGC-CoT，将推理建模为多层价值图上的有向遍历，通过图结构约束强制事实共享与价值分歧的解耦。该方法在事实完整性上显著优于基线，但其依赖人工构建的规范子图，限制了在动态社会价值观场景下的可扩展性。

】

---

【Distributional Alignment for Large Language Models under Domain Shift ｜基于证据检索与价值签名的分布对齐

研究机构：澳大利亚莫纳什大学

作者：Viet Thanh Pham、Lizhen Qu、Zhuang Li 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8f8b98d03f88)

> 分布对齐旨在让大语言模型预测目标群体在多选题上的回答分布，而非输出单一共识答案。现有方法如Token概率估计对选项措辞敏感，直接生成分布则常因表面形式锚定而校准失效，尤其在跨文化域偏移下表现脆弱。Evi-DA通过检索世界价值观调查（WVS）中的相似问题分布作为证据，并预测选项的Welzel价值签名，实现结构化两阶段推理。该方法在域内和域外基准上显著降低了预测分布与真实分布的Jensen-Shannon Divergence (JSD)，但其效果高度依赖骨干模型的推理能力，小模型在强化学习后性能反而退化。

】

---

【Probing the Plasticity and Correlation of LLM Value Systems: LLM Value Rankings are Not Stable ｜大语言模型价值系统可塑性与相关性拓扑

研究机构：香港科技大学、南京大学

作者：Zhenheng Tang、Qihua Pan、Jingya Shen 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a10d873812d5)

> 大语言模型（LLM）在决策中依赖内部价值排序，但现有对齐研究多假设该排序是静态且鲁棒的，忽略了外部提示对价值优先级的系统性扰动。本文切入点在于量化这种“价值可塑性”，并揭示不同价值间存在内在的联动结构。通过设计六种提示策略对八款模型进行压力测试，发现场景化叙事能最有效地颠覆默认价值排序，且大模型比小模型更易受此影响。该工作揭示了基于提示的价值操纵风险，但缺乏对权重层面干预的对比，其防御性结论在动态对抗场景下的有效性存疑。

】

---

【V-RoLoRA: RLVR-Driven MoE Routing for Steerable Pluralistic Alignment ｜可引导价值对齐中的条件路由与可验证奖励

作者：Jing Wang、Yaomin Wu、Yinglin Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c4012c4a0550)

> 可引导价值对齐旨在使大语言模型（LLM）在生成时忠实遵循多维、组合式的价值观或道德准则，而非收敛于单一共识。现有方法多依赖提示工程或单适配器微调，在长尾价值组合下控制力脆弱且易产生语义幻觉。本文切入点是将控制信号从输入端迁移至权重端，通过多维价值向量路由混合专家（MoE）LoRA池，并引入外部判别器计算条件一致性奖励，以强化学习（RL）优化语义合规性。该方法在8B骨干上实现了可控性指标的提升，但其对长尾维度的覆盖不足及判别器偏差问题仍存疑。

】

---

【Value Alignment Tax: Measuring Value Trade-offs in LLM Alignment ｜价值对齐税（VAT）：量化LLM对齐中的系统性价值权衡

研究机构：美国纽约大学

作者：Jiajun Chen、Hua Shen

论文原文见 [arXiv](https://arxiv.org/abs/2602.12134)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.12134)

> 多元价值对齐旨在使大语言模型（LLM）输出反映人类群体价值观的多样性，但现有评估范式仅关注目标价值的增益，忽略了干预引发的非目标价值协同漂移。这种“静态、原子化”的度量掩盖了安全关键场景下对齐副作用的系统性风险。本文提出价值对齐税（Value Alignment Tax, VAT）框架，通过场景-动作对提取状态级价值向量，利用Spearman相关系数量化价值间的结构耦合。该框架揭示了SFT与DPO在对齐效率与系统稳定性上的本质差异，但缺乏对神经元级干预的评估，其诊断结论能否指导优化器设计尚存疑。

】

---

【Value-Action Alignment in Large Language Models under Privacy-Prosocial Conflict ｜隐私-亲社会冲突下的价值-行动对齐评估

研究机构：美国亚利桑那州立大学、美国南加州大学

作者：Guanyu Chen、Chenxiao Yu、Xiyang Hu

论文原文见 [arXiv](https://arxiv.org/abs/2601.03546)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03546)

> 当大语言模型（LLM）面临隐私保护与亲社会利他两种价值观的拉扯时，其数据共享决策往往呈现出复杂的内部权衡，但现有评估手段难以捕捉这种多态度联合预测行为的结构性关系。传统“价值-行动差距”（Value-Action Gap）指标将多维态度压缩为单一标量，在多值冲突场景下因参考系缺失而失效，无法区分模型是真正遵循人类行为逻辑还是仅表现出表面一致性。本文提出基于多群组结构方程模型（MGSEM）的评估框架，通过提取路径方向一致性来量化价值-行动对齐率（VAAR），揭示了模型间对齐能力的巨大异质性。该方法在特定冲突场景下提供了比标量差距更稳健的诊断视角，但其对标准化量表和固定样本量的依赖限制了其在通用价值评估中的泛化能力。

】
