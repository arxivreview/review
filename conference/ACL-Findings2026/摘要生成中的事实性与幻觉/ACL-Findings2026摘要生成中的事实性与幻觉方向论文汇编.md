# ACL-Findings2026 · 摘要生成中的事实性与幻觉方向论文汇编

> 本方向共 6 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Comprehensiveness Metrics for Automatic Evaluation of Factual Recall in Text Generation ｜基于语料库的LLM输出完整性自动评估

研究机构：英国帝国理工学院、IBM研究院

作者：Adam Dejl、James Barry、Alessandra Pascale 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.07926)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ac108736783c)

> 大语言模型在安全关键领域不仅会编造事实，更会遗漏关键信息或片面呈现冲突证据，而现有事实性评估指标主要关注“说了什么是否对”（Precision），缺乏对“该说的说了多少”（Recall）的量化能力。本文提出三种基于背景语料库的完整性评估指标，通过原子事实分解与自然语言推理（NLI）构建覆盖图，直接识别模型输出中缺失的具体信息。实验表明，最简的端到端（E2E）方法在平均性能上优于复杂的图结构方法，但鲁棒性显著下降。该工作填补了事实性评估中“遗漏检测”的空白，但其结论依赖于特定语料库质量，且E2E方法的稳定性存疑。

】

---

【Enhancing Factuality through Consensus and Consistency in Summarization Using Minimum Bayes Risk Decoding ｜基于共识与一致性的摘要重排序

研究机构：日本东京科学大学

作者：Riza Setiawan Soetedjo、Yusuke Sakai、Hidetaka Kamigaito 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.29336)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3cd6383f5931)

> 摘要生成中的事实性幻觉源于模型对源文档的偏离，而现有重排序方法仅依赖源文档进行无参考评分，因指标粒度粗且存在偏差，无法有效惩罚特定事实错误。本文指出单一信号重排序的局限性，提出结合候选摘要间共识与对源文档一致性的双信号重排序框架。该方法利用最小贝叶斯风险解码计算共识，结合无参考事实性指标计算一致性，通过加权组合选出最优摘要。实验表明该方法在事实性指标上显著优于基线，但绝对得分仍远低于生成式优化方法，且伪参考引入的自生成偏差尚未被量化。

】

---

【Learning to Control Summaries with Score Ranking ｜基于排序对齐的摘要多维质量控制

研究机构：美国杜克大学、澳大利亚悉尼大学

作者：Hongye Liu、Liang Ding、Ricardo Henao

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_acb9882786cd)

> 导读 摘要生成领域长期面临完整性与简洁性之间的固有冲突，单一目标优化往往导致另一维度性能下降，即“对齐税”现象。现有基于直接偏好优化（DPO）的方法在排序任务上表现低效且计算成本高，难以实现细粒度的维度特异性控制。本文提出一种结合边缘排序损失、最大评分损失与控制导向损失的联合训练框架，将模型似然与细粒度模型评分对齐，实现了对摘要质量的动态权衡。该方法在多个开源模型上验证了可控性优势，但其在事实一致性维度上的表现及与主流幻觉抑制方法的兼容性仍存疑。

】

---

【SCURank: Ranking Multiple Candidate Summaries with Summary Content Units for Enhanced Summarization ｜基于摘要内容单元的候选排序蒸馏

研究机构：国立成功大学、国立清华大学

作者：Bo-Jyun Wang、Ying-Jia Lin、Hung-Yu Kao

论文原文见 [arXiv](https://arxiv.org/abs/2604.19185)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.19185)

> 摘要蒸馏训练依赖候选摘要的质量排序来构建对比学习信号，但现有基于大语言模型（LLM）的直接排序方法存在严重的输入顺序敏感性与评估不一致性，而传统词汇重叠指标无法捕捉语义丰富度。本文提出 SCURank，通过提取摘要内容单元（Summary Content Units, SCUs）并利用聚类频率量化信息重要性，实现了对候选摘要的稳定排序。该方法在 CNN/DailyMail 和 XSum 数据集上显著优于 GPTRank 基线，但仅验证了词汇与语义相似度指标的提升，未直接证明事实一致性（Factual Consistency）的改善。

】

---

【TRAC: Token-level Reward Assignment for Coherent Abstractive Summarization ｜基于过程奖励模型的词元级摘要生成优化

研究机构：华南理工大学、澳门大学

作者：陈宣齐、容梓莹、Xinfeng Liao 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ce9d5b0b3e0c)

> 导读 摘要生成领域长期面临强化学习奖励信号稀疏导致的连贯性与事实性缺失问题。现有序列级奖励无法捕捉词元间依赖，而人工工程化词元奖励成本高昂且泛化性差。TRAC 框架通过迁移数学推理中的过程奖励模型（Process Reward Model, PRM），利用句间注意力将全局语义信号分解至词元级，实现了高效且可迁移的细粒度监督。该方法在流畅度与相关性上显著优于基线，但其对事实性幻觉的抑制能力尚未在独立基准上得到充分验证。

】

---

【Understanding LLMs’ summarization capabilities: an analysis of biomedical abstract and lay summary generation ｜轻量级大语言模型在生物医学摘要生成中的零样本能力诊断

研究机构：美国佐治亚理工学院

作者：Batuhan Nursal、Cassie S. Mitchell

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7a9d96586901)

> 生物医学文献的指数级增长要求将复杂研究转化为可访问的格式，但现有评估多聚焦于微调模型在自动化指标上的排名，忽视了轻量级模型在零样本场景下的内容来源与效用差异。主流方法依赖参考摘要计算重叠度，无法解释模型为何选择特定信息，且缺乏对非专家读者视角下内容“可答性”的量化。本文通过引入句子级来源分类与问答对评估，诊断了小于8B参数模型在生成科学摘要与通俗摘要时的信息分布偏差。该研究揭示了轻量级模型在事实性上优于人类参考摘要的反直觉现象，但其评估样本量极小，结论的统计稳健性存疑。

】
