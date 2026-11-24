# ACL-Findings2026 · 可控文本生成方向论文汇编

> 本方向共 4 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【DcLM: Output Length Control of Large Language Models via Dynamic Length Markers ｜动态长度标记驱动的长度可控生成

研究机构：华东师范大学

作者：Zhe Chen、Jiaao Yu、Honglin Li

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a7eb82e62e28)

> 长度可控文本生成（LCTG）旨在让大语言模型（LLMs）在输出流畅文本的同时，严格遵循指定的字数约束。现有方法多依赖提示工程或强制模型生成控制标记，前者受限于模型内在计数能力，后者易破坏语义连贯性。本文提出 DcLM，通过外部计数器在推理时注入动态长度标记，并将标记作为上下文信息而非生成目标进行掩码训练。该方法在长文本生成上显著降低了长度偏差，但缺乏与强化学习类方法的直接对比，其长期稳定性存疑。

】

---

【From Scaffolding to Assimilation: Progressive Structural Internalization for Format-Constrained Creative Text Generation ｜渐进结构内化

研究机构：清华大学

作者：Wenhao Li、Yuwei Yang、Xiaoqing Wu 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f406875253c5)

> 中文古典诗词生成要求同时满足字数、平仄、押韵三重硬约束，而现有提示工程无法保证合规，约束解码虽能强制合规却导致推理延迟激增与语义质量崩塌。本文切入点在于将外部规则转化为模型内部直觉，通过“结构脚手架”监督微调与“级联强化学习”两阶段训练，使模型在参数层面内化韵律规则。该方法在结构准确率上显著优于通用大模型，但受限于单一语言领域，其跨域泛化能力存疑。

】

---

【Progress Ratio Embeddings: An Impatience Signal for Robust Length Control in Neural Text Generation ｜进度比率嵌入

作者：Ivanhoé Botcazou、Tassadit Amghar、Sylvain Lamprier 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cb4b27fa06d2)

> 神经语言模型在生成文本时，精确控制输出长度长期面临技术瓶颈，尤其是小语言模型（SMLs）在域特定数据上训练时，缺乏通过提示工程实现长度控制的能力。现有基于离散剩余计数的方法在训练分布外失效，导致无法泛化至未见过的目标长度。本文提出进度比率嵌入（Progress Ratio Embeddings, PRE），通过向解码器注入连续的正弦“不耐烦”信号，实现架构级的鲁棒长度控制。该方法在摘要任务上验证了长度保真度，但其对大语言模型推理时干预范式的适用性存疑。

】

---

【UniCreative: Unifying Long-form Logic and Short-form Sparkle via Reference-Free Reinforcement Learning ｜统一长短文本创意写作：参考无关强化学习框架

研究机构：北京航空航天大学、中国人民大学

作者：Xiaolong Wei、Zerun Zhu、Simin Niu 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.05517)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05517)

> 创意写作面临长文本结构崩塌与短文本表达平庸的双重困境，现有对齐范式依赖昂贵的监督数据且无法动态适配任务类型。UniCreative 将规划视为可动态调用的计算资源，通过自适应约束偏好优化（ACPO）实现无监督数据的参考无关强化学习。该框架验证了模型在特定规模下涌现出自主区分任务范式的元认知能力，但小模型容量瓶颈与长上下文训练成本仍制约其普适性。

】
