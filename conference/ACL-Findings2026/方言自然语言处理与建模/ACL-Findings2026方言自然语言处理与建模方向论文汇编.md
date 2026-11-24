# ACL-Findings2026 · 方言自然语言处理与建模方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Arab Voices: Mapping Standard and Dialectal Arabic Speech Technology ｜Arab Voices：阿拉伯语方言语音数据的标准化与基准构建

研究机构：加拿大不列颠哥伦比亚大学

作者：Peter Sullivan、AbdelRahim A. Elmadany、Alcides Alcoba Inciarte 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c85e87f672ba)

> 阿拉伯语方言（Dialectal Arabic, DA）语音处理长期受困于数据碎片化，现有数据集在元数据标注、方言标签定义及录音条件文档化上缺乏统一标准，导致跨数据集比较与模型评估难以复现。本文切入点在于构建一个标准化的数据生态系统，通过自动化量化“方言度”与音频质量，解决异构语料库无法直接对齐的问题。其核心做法是聚合31个数据集，建立统一元数据框架并引入自动化特征化指标，进而对主流自动语音识别（ASR）模型进行零样本基准测试。该工作填补了DA语音数据基础设施的空白，但其评估仅覆盖零样本场景，未涉及微调后的性能上限，且自动化指标与人类感知的对齐度仍存疑。

】

---

【Idiom Understanding as a Tool to Measure the Dialect Gap ｜区域习语理解作为方言差距量化探针

作者：David Beauchemin、Yan Tremblay、Mohamed Amine Youssef 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.05026)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ff473a522c73)

> 方言自然语言处理长期面临标准语模型在低资源方言上性能崩塌的困境，但现有评估多聚焦于语音识别或通用文本分类，缺乏针对文化密集语义的细粒度探针。本文切入点在于论证区域习语无法从标准语语法中推断，因而成为衡量方言理解能力的有效指标。作者构建了魁北克法语与巴黎法语的习语基准，通过零样本评估111个大语言模型，量化了方言差距。该工作提供了首个魁北克法语习语评估工具，但零样本设置下专有模型的高分是否源于数据污染而非真实理解能力，仍存疑。

】

---

【Linear Semantic Segmentation for Low-Resource Spoken Dialects ｜低资源口语方言的线性语义分割

研究机构：阿联酋扎耶德大学、IBM研究院

作者：Kirill Chirkunov、Younes Samih、Abed Alhakim Freihat 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.06276)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.06276)

> 现有语义分割模型依赖标准书面语的结构线索，在缺乏标点与句法规范的阿拉伯语方言口语转录中性能崩塌。本文构建了首个覆盖多体裁、多方言的阿拉伯语口语语义分割基准，并验证了基于大语言模型微调的边界检测策略在噪声话语流中的有效性。通过引入“损坏-恢复”辅助任务与领域自适应提示，该模型在细粒度结构指标上稳定优于传统无监督与监督基线。其价值在于填补了从句子级分类到话语级结构建模的空白，但仅依赖文本转录而忽略声学韵律信息的局限，使其在真实口语场景的泛化能力仍存疑。

】

---

【WenetSpeech-Wu: Datasets, Benchmarks, and Models for a Unified Chinese Wu Dialect Speech Processing Ecosystem ｜吴语语音处理生态构建

研究机构：西北工业大学

作者：Chengyou Wang、Mingchen Shao、Jingbin Hu 等 14 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.11027)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.11027)

> 低资源方言语音处理长期受困于数据规模与标注维度的双重匮乏，导致通用模型在特定方言上性能崩塌。现有方案多聚焦单一子方言或仅覆盖基础识别任务，缺乏系统性评估基准。本文切入点在于构建首个覆盖八种吴语子方言、包含多维标注的大规模语料库及配套基准，通过统一的数据流水线与模型训练验证其有效性。该工作填补了吴语语音技术生态的空白，但自动标注噪声对下游任务精度的具体影响尚未被充分量化。

】

---

【Zero-Shot Context-Aware ASR for Diverse Arabic Varieties ｜零样本阿拉伯语方言ASR的上下文感知解码

研究机构：加拿大不列颠哥伦比亚大学、英国帝国理工学院

作者：Bashar Talafha、Amin Abu Alhassan、Muhammad Abdul-Mageed

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2971de2b614e)

> 零样本阿拉伯语方言自动语音识别（ASR）面临标准语模型在方言输入下性能骤降且缺乏标注数据微调的困境。现有推理时适应方法多局限于可提示的编码器-解码器架构，且直接提示易引发幻觉，无法覆盖非自回归模型。本文提出上下文感知解码范式，通过提示重排序、说话人一致前缀及代理引导n-best选择，在不更新参数的前提下引导解码。该策略在多方言条件下实现了显著的相对词错率（WER）降低，但其收益高度依赖外部代理质量，且在极端低资源方言上的绝对性能提升有限。

】
