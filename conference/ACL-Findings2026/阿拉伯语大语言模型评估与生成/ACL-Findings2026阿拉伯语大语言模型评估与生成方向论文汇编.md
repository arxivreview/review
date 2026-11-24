# ACL-Findings2026 · 阿拉伯语大语言模型评估与生成方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Candidate-Aware Retrieval and Reranking for Multiple-Choice Question Answering: Arabic as a Case Study ｜答案感知检索与重排序的阿语多选问答优化

作者：Yassine Bouziane、Youness Moukafih、Mounir Ghogho

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5f0f18ac73ba)

> 阿语大语言模型在多选问答（Multiple-Choice Question Answering, MCQA）任务中面临检索噪声与证据区分度不足的双重瓶颈，导致小模型在复杂推理上表现滞后。现有检索增强生成（Retrieval-Augmented Generation, RAG）方法仅基于问题检索，忽略了候选答案与上下文之间的交互作用，难以区分背景信息与决定性证据。本文提出一种答案候选感知的检索与重排序框架，通过联合建模问题、选项与上下文的三元组关系，提升小模型在阿语人文学科上的表现。该方法在资源受限条件下实现了与大模型相当的准确率，但其评估范围局限于人文学科，且未涵盖方言场景，泛化能力存疑。

】

---

【Instruction-Guided Poetry Generation in Arabic and Its Dialects ｜阿拉伯语诗歌指令微调

研究机构：阿联酋扎耶德大学

作者：Abdelrahman Sadallah、Kareem Elozeiri、Mervat Abassy 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.27766)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.27766)

> 阿拉伯语诗歌在文化传承中占据核心地位，但现有大语言模型（LLM）研究多局限于分析或分类任务，缺乏支持用户指定韵律、风格等约束的可控生成能力。通用模型在阿语诗歌生成上常出现结构松散与文化错位，而专用微调数据稀缺。本文通过构建覆盖现代标准阿拉伯语（MSA）及四种方言的大规模指令微调数据集，将诗歌创作转化为指令遵循问题。实验表明微调显著提升了模型在韵律合规与诗意质量上的表现，但方言泛化能力与长程格律一致性仍存疑。

】

---

【NeoAraBERT: A Modern Foundation Model for Arabic Embeddings with Diacritics-Aware Tokenization and POS-Targeted Masking ｜NeoAraBERT：基于变音符号感知分词与词性掩码的阿语编码器

作者：Chadi Abou Chakra、Hadi Khaled Hamoud、Osama Rakan Al Mraikhat 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_48b068fdbfaa)

> 阿语编码器长期受限于形态复杂性导致的表示碎片化，现有模型在古典阿语与语义嵌入任务上表现疲软。本文切入点在于将现代Transformer架构（NeoBERT）与阿语特有的变音符号分离机制结合，通过词性条件掩码优化预训练信号。具体做法是构建包含MSA、古典阿语及方言的混合语料，采用变音符号感知分词器与POS-targeted掩码策略进行预训练。该模型在23项任务中18项取得最优，但在方言任务上未全面超越专用模型，且未对比多语言大模型基线。

】
