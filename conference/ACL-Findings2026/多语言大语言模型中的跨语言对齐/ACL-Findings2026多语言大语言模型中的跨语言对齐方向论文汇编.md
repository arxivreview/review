# ACL-Findings2026 · 多语言大语言模型中的跨语言对齐方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Can Multi-agent Help Disambiguation in Multi-domain Translation? ｜多智能体协作消歧框架

作者：Zhibo Man、Shaoyang Xu、Yujie Zhang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_22f70caf059b)

> 多领域翻译（Multi-Domain Translation, MDT）面临的核心挑战是同一词汇在不同领域语境下需映射至截然不同的语义，导致翻译歧义。现有基于提示工程的方法虽能注入领域信息，但受限于单一提示上下文的长度与角色混淆，难以有效解耦通用语义与领域特异性。本文提出多智能体协作消歧框架（MACD），通过领域分配、通用翻译、领域消歧及融合四个智能体的分工协作，显式化消歧过程。该框架在多个领域上提升了翻译质量与消歧准确率，但其依赖人工设计的提示交互，且在长文本语境下的消歧增益机制尚需进一步厘清。

】

---

【Mending the Holes: Mitigating Reward Hacking in Reinforcement Learning for Multilingual Translation ｜修补质量估计漏洞：多语言翻译强化学习中的混合奖励机制

作者：Yifeng Liu、Siqi Ouyang、Yatish H R 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9dd6243e6880)

> 多语言大语言模型在低资源语言翻译上性能滞后，而现有后训练方法依赖稀缺的平行数据。直接利用无参考质量估计（QE）模型进行强化学习（RL）会因指标缺陷导致“奖励黑客”，使模型退化。本文提出 WALAR，通过引入词对齐与语言对齐分数构建混合奖励，仅使用单语数据即可提升翻译质量。该方法在 FLORES-101 上显著优于基线，但绝对性能仍受限于单语数据的语义覆盖度。

】

---

【No One Fits All: From Fixed Prompting to Learned Routing in Multilingual LLMs ｜多语言提示策略的自适应路由

研究机构：国立台湾大学、新加坡南洋理工大学

作者：Wei-Chi Wu、Sheng-Lun Wei、Hen-Hsen Huang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.16937)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f9c48911b33b)

> 导读 多语言大语言模型（Multilingual Large Language Models, mLLMs）在处理低资源语言时，常因预训练数据中英语的主导地位而依赖“翻译至英语再推理”的提示策略，但该策略在高资源语言或文化敏感任务中往往失效。现有研究多聚焦于优化单一提示范式，缺乏对“何时翻译、何时原生”这一决策问题的系统性建模。本文提出基于轻量级分类器的提示策略路由框架，通过响应特征差异预测最优提示方式，在四个基准上实现统计显著的性能提升。该框架验证了语言资源等级而非翻译质量是决定策略有效性的核心变量，但其仅优化输入端策略，未触及模型内部表征对齐的根本缺陷。

】

---

【One Script Instead of Hundreds? On Pretraining Romanized Encoder Language Models ｜罗马化预训练对高资源语言性能的影响评估

作者：Benedikt Ebing、Lennart Keller、Goran Glavaš

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e030b58cf730)

> 多语言编码器模型在跨语言迁移中常受限于脚本壁垒，即不同书写系统间的词汇重叠被阻断。现有研究多聚焦于低资源语言从拉丁脚本高资源语言迁移的场景，却忽略了罗马化（Romanization）对高资源语言自身性能可能造成的信息损失与表征稀释。本文通过受控预训练实验，量化了将六种高资源语言统一为拉丁脚本后的下游任务性能变化，发现分段脚本损失可忽略，而形态音节脚本存在显著退化。这一发现为大规模多语言模型的脚本统一策略提供了实证依据，但其在更大规模模型下的鲁棒性仍存疑。

】

---

【Scripts Through Time: A Survey of the Evolving Role of Transliteration in NLP ｜转写作为跨脚本迁移的锚点机制：从词汇重叠到多脚本感知

作者：Thanmay Jayakumar、Deepon Halder、Raj Dabre

论文原文见 [arXiv](https://arxiv.org/abs/2604.18722)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fa08d6da4b9e)

> 跨语言迁移在低资源语言上常因书写系统差异而失效，即“脚本壁垒”。现有方法多聚焦于模型内部语义空间对齐或全量数据增强，却忽视了输入形态层面的词汇重叠缺失这一直接障碍。本文系统梳理了转写（Transliteration）作为打破该壁垒的技术路径，将其从统计机器翻译时代的OOV处理工具，重构为大语言模型时代的多脚本感知辅助信号。其价值在于提供了无需平行语料、计算高效的实践指南，但转写引入的歧义性与语义损失风险使其并非万能解，且在复杂推理任务中的有效性存疑。

】
