# ACL-Findings2026 · 多模态仇恨模因检测方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【DR-HM: Distill-then-Reinforce Training with Cognition-Aware Data Synthesis for Harmful Meme Detection ｜认知感知数据合成与蒸馏强化训练

研究机构：美国东北大学

作者：Zihan Cheng、Jianxiang Ma、Xiaocui Yang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c9d7c2e23e34)

> 多模态仇恨表情包检测的核心难点在于隐含语义依赖文化常识，而小模型缺乏此类知识，大模型则存在标签偏差。现有蒸馏方法因自由形式推理引入噪声，导致性能不及直接微调。本文切入点是将人类认知过程结构化为六步推理链，并引入自精炼机制校正大模型偏差。通过两阶段监督微调与自适应强化学习，使7B开源模型在FHM基准上达到84.7%准确率。该方法验证了结构化知识注入的有效性，但其静态蒸馏策略对动态新兴梗的泛化能力存疑。

】

---

【FigSIM: A Dataset for Fine-grained Suicide Severity and Figurative Language in Suicide Memes ｜自杀表情包细粒度风险分级与修辞干扰分析

研究机构：澳大利亚墨尔本大学

作者：Liuliu Chen、Elise R. Carrotte、Brian E. Chapman 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.02523)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.02523)

> 自杀表情包检测旨在从图文交互中识别隐含的自杀风险等级，其核心难点在于幽默修辞与临床风险信号的纠缠，导致传统二元分类无法支撑精准干预。现有通用仇恨检测模型在自杀垂直领域面临严重度低估与修辞误判瓶颈，本文切入点在于构建首个基于临床量表的多标签自杀表情包基准。通过整合修辞现象、自杀严重度及内容类型标注，并评测16种单模态与多模态模型，揭示了修辞对风险识别的系统性干扰。该工作确立了自杀表情包检测的性能下限，但数据源单一性与标注主观性限制了其泛化边界。

】

---

【More Than Sum of Its Parts: Deciphering Intent Shifts in Multimodal Hate Speech Detection ｜分层多模态交互与法庭辩论框架

研究机构：清华大学

作者：Runze Sun、Yu Zheng、Zexuan Xiong 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.21298)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.21298)

> 多模态仇恨检测的核心难点在于仇恨意图常由看似无害的图文组合通过隐喻或讽刺隐含生成，单一模态特征无法独立承载完整语义。现有方法多依赖静态特征融合或对称式多智能体投票，难以捕捉模态间的动态语义冲突与语境反转，导致在隐含仇恨样本上误判率高。本文通过构建分层多模态交互（Stratified Multimodal Interaction, SMI）范式明确意图转移机制，并提出非对称法庭辩论框架（ARCADE）强制模型进行对抗性推理。该工作提升了隐含样本的检测精度与解释性，但在绝对精度上仍低于部分强骨干基线，且未量化计算成本。

】
