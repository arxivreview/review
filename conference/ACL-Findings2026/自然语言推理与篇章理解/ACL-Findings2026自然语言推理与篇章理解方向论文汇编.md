# ACL-Findings2026 · 自然语言推理与篇章理解方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Agree, Disagree, Explain: Decomposing Human Label Variation in NLI through the Lens of Explanations ｜从标签内变异到标签间变异：基于解释分类法的NLI标注分歧解构

研究机构：奥地利维也纳大学、德国慕尼黑大学

作者：Pingjun Hong、Beiduo Chen、Siyao Peng 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.16458)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d58bc37a7611)

> 导读 自然语言推理（NLI）任务长期面临标注者间分歧（Annotation Divergence）的困扰，传统研究多聚焦于标签分布的统计特性，却忽视了标签背后推理逻辑的异质性。现有解释性方法如e-SNLI和LiveNLI虽提供了自由文本解释，但缺乏结构化框架来量化解释与标签的交互关系，导致无法区分“标签一致但推理不同”与“标签不同但推理相同”的本质差异。本文通过扩展LITEX分类法至标签间变异场景，结合条件Cohen’s κ分析，揭示了推理类别一致性比标签一致性更能反映解释语义相似度的核心发现。该工作为理解标注噪声提供了微观视角，但其结论是否足以指导模型训练中的软标签构建，仍需进一步验证。

】

---

【Commonsense Knowledge with Negation: A Resource to Enhance Negation Understanding ｜否定常识增强

研究机构：美国亚利桑那大学

作者：Zijie Wang、MohammadHossein Rezaei、Farzana Rashid 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.19921)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_376979318188)

> 自然语言模型在处理否定语义时普遍存在“肯定偏差”，导致在涉及否定的推理任务中性能骤降。现有常识知识库缺乏否定样本，而人工标注否定常识成本高昂且规模受限。本文切入点在于利用大语言模型自动对现有常识三元组进行否定变换，并训练专用验证器筛选有效样本，构建大规模否定常识语料。该方法通过预训练显著提升了模型在否定理解任务上的表现，但其自动验证器的精度瓶颈是否足以支撑更复杂的逻辑推理场景，仍存疑。

】

---

【Thunder-KoNUBench: A Corpus-Aligned Benchmark for Korean Negation Understanding ｜韩语否定理解基准

研究机构：韩国首尔大学

作者：Sungmok Jung、Yeonkyoung So、Joonhak Lee 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_167400b0a289)

> 大语言模型在处理否定语义时普遍存在性能退化，但现有评估资源高度集中于英语，导致低资源语言如韩语的否定处理能力处于盲区。本文通过构建反映韩语真实语料分布的句级多选基准，填补了这一系统性空白。其核心做法是结合大规模语料统计分析与47个模型的大规模评估，验证了否定导致的性能下降及微调策略的有效性。该工作确立了韩语否定评估的参照系，但受限于多选格式，无法直接衡量模型生成否定句的内在逻辑一致性。

】
