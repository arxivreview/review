# ACL-Findings2026 · 表现力与可控文本到语音合成方向论文汇编

> 本方向共 4 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Beyond Sentence-level Labels: Integrating Conversational Context and Personal Experience for Natural Emotional Expression ｜语境感知情感语音合成

作者：Haiyang Sun、Chenyang Le、Wei Wang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dbafea524340)

> 情感文本转语音（Emotional Text-to-Speech, E-TTS）的核心矛盾在于合成语音缺乏人类情感表达的因果逻辑，导致自然度不足。现有方法依赖句级离散标签或简短指令，无法捕捉个体经历与对话语境对情感生成的深层影响。本文提出将认知评估理论中的“个人经历”与“对话语境”作为显式条件注入生成过程，并构建大规模语境感知数据集进行验证。该工作证明了语境信息对情感自然度的关键作用，但其评估局限于自建数据集，缺乏跨基准的通用性验证。

】

---

【Comprehensive Benchmarking of Long-Form Speech Generation in Diverse Scenarios ｜长文本语音生成基准

研究机构：浙江大学

作者：Changhao Pan、Rui Yang、Han Wang 等 15 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.28618)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.28618)

> 长文本语音合成面临韵律漂移与表达力缺失，但现有评估指标在长序列下失效且缺乏细粒度诊断能力。本文切入点在于构建覆盖17种场景、解耦声学/语义/表达维度的自动化评估协议。通过分层指标与LALM评分，量化了模型在时间稳定性与叙事动态上的具体差距。该基准填补了长文本评估空白，但LALM评分的主观对齐度与闭源模型的数据规模优势仍存疑。

】

---

【Computational Narrative Understanding for Expressive Text-to-Speech ｜叙事感知数据驱动的表达性文本转语音

作者：Gaspard Michel、Elena V. Epure、Christophe Cerisara

论文原文见 [arXiv](https://arxiv.org/abs/2509.04072)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.04072)

> 表达性文本转语音（Expressive TTS）旨在解决合成语音缺乏情感与风格多样性的问题，但现有大规模有声书数据集通常将中性叙述与角色对话混合，导致模型难以捕捉细粒度韵律变化。本文切入点在于利用叙事文本中的隐式风格线索（如言语动词和副词）构建大规模表达性数据集，验证其对TTS模型微调的有效性。通过提取小说对话中的上下文伪标签，本文证明了流匹配架构在表达性微调上的优势。该工作填补了数据源情感多样性的空白，但自回归模型在相同数据下的表现差异仍存疑。

】

---

【ReStyle-TTS: Relative and Continuous Style Control for Zero-Shot Speech Synthesis ｜解耦引导与正交融合：零样本TTS的相对风格控制

研究机构：浙江大学、厦门大学

作者：Haitao Li、Chunxiang Jin、Chenglin Li 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.03632)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03632)

> 零样本TTS的核心困境在于，模型在克隆说话人音色的同时，不可避免地继承了参考音频中的韵律与情感风格，导致合成语音被参考音频“锁定”。现有可控TTS方法多依赖绝对文本指令或额外风格音频，缺乏对参考音频风格的相对、连续调节能力。ReStyle-TTS通过解耦分类器自由引导（Decoupled Classifier-Free Guidance, DCFG）降低参考音频依赖，结合正交LoRA融合（Orthogonal LoRA Fusion, OLoRA）实现多属性独立控制，并引入音色一致性优化（Timbre Consistency Optimization, TCO）防止音色漂移。该框架在矛盾风格场景下表现优异，但其相对控制机制在长文本一致性上的有效性尚未得到充分验证。

】
