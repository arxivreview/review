# ACL-Findings2026 · 低资源多语言语音识别方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Hard to Be Heard: Phoneme-Level ASR Analysis of Phonologically Complex, Low-Resource Endangered Languages ｜极端音系低资源语言的音素级识别分析

研究机构：德国图宾根大学

作者：V.S.D.S.Mahesh Akavarapu、Michael Daniel、Gerhard Jäger

论文原文见 [arXiv](https://arxiv.org/abs/2604.18204)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_adc95ab6e412)

> 东高加索语言如Archi拥有73至81个辅音音位，其音系复杂度远超常规低资源语言，导致现有自动语音识别（ASR）系统无法区分错误源于内在音系难度还是数据稀缺。通用多语言模型在缺乏针对性适配时，对这类极端音系结构的泛化能力存在盲区，且传统词错误率（WER）指标掩盖了音素层面的系统性偏差。本文通过构建标准化语料并引入语言特定音素词表与启发式初始化，揭示了音素识别准确率随训练频率呈Sigmoid增长的规律。该研究验证了数据稀缺主导错误模式的核心假设，但受限于极小样本规模，其结论在更大规模数据下的普适性尚存疑。

】

---

【Multimodal In-context Learning for ASR of Low-resource Languages ｜多模态上下文学习驱动的低资源语音识别

研究机构：德国卡尔斯鲁厄理工学院

作者：Zhaolin Li、Jan Niehues

论文原文见 [arXiv](https://arxiv.org/abs/2601.05707)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05707)

> 低资源语音识别（ASR）长期受困于标注数据稀缺，传统自监督预训练与微调范式在极端低资源场景下泛化能力受限。本文切入点在于利用语音大语言模型（Speech LLM）的多模态上下文学习（MICL）能力，在推理时通过提示工程动态适配未见语言，而非依赖参数更新。具体做法是结合声学模型生成假设，并利用语音 LLM 进行基于 MICL 的重排序。该架构在三种濒危语言上验证了跨语言迁移的有效性，但其性能提升是否主要源于声学模型 N-best 列表的质量，而非 LLM 的深层语义理解，仍存疑。

】

---

【PUMA: Projected Universal Multilingual ASR for Low-Resource Settings. Application to Diverse African Languages ｜通用语言投影多语言语音识别

研究机构：法国国家科学研究中心

作者：Ilyes Oukid、Bilal Faye、Hanane Azzag 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b1a315d6aa26)

> 低资源多语言语音识别（LR-ML-ASR）面临的核心矛盾是语言多样性与计算资源有限性之间的结构性冲突，现有基于适配器的多语言模型在扩展新语言时参数呈线性增长，阻碍了边缘部署与长尾语言覆盖。PUMA 通过引入通用语言投影（ULP）模块，以单一可学习语言令牌替代语言特定适配器，在保持全参数共享的同时实现语言感知。该架构在 10 种非洲低资源语言上以约 30M 可训练参数超越了 1B 参数的 MMS 基线，但其性能优势是否源于架构创新还是数据特性，以及其在形态更复杂语言上的泛化能力，仍存疑。

】
