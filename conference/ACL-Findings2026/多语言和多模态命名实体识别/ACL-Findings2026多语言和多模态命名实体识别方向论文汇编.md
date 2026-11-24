# ACL-Findings2026 · 多语言和多模态命名实体识别方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Beyond Unimodal Shortcuts: MLLMs as Cross-Modal Reasoners for Grounded Named Entity Recognition ｜超越单模态捷径：基于模态感知一致性推理的接地多模态命名实体识别

研究机构：哈尔滨工业大学、中国科学院

作者：Jinlong Ma、Yu Zhang、Xuefeng Bai 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2ba68439dda1)

> 接地多模态命名实体识别（Grounded Multimodal Named Entity Recognition, GMNER）要求模型在提取文本实体的同时，将其定位到图像中的对应区域，其核心难点在于多模态大语言模型（MLLMs）常依赖单模态启发式规则而非严格的跨模态验证，导致实体定位或类型错误。现有方法多将MLLMs作为流水线中的辅助工具进行特征对齐，未能充分利用其跨模态推理潜力以消除模态偏差。本文提出模态感知一致性推理（Modality-aware Consistency Reasoning, MCR）框架，通过多风格推理模式注入与约束引导可验证优化，强制模型执行显式的跨模态一致性检查。该框架在多个基准上显著超越了现有基线，但其对特定推理模板的依赖及在长尾实体上的泛化边界仍需进一步检验。

】

---

【E2E-GMNER: End-to-End Generative Grounded Multimodal Named Entity Recognition ｜端到端生成式接地多模态命名实体识别

研究机构：大连理工大学

作者：Meng Zhang、Jinzhong Ning、Xiaolong Wu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17319)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17319)

> 接地多模态命名实体识别（Grounded Multimodal Named Entity Recognition, GMNER）旨在从图文对中同时提取文本实体、语义类型及对应的视觉区域。现有主流方法依赖独立的命名实体识别（NER）模块与对象检测器，这种解耦架构导致误差在级联过程中累积，且无法进行联合优化。本文提出 E2E-GMNER，将 GMNER 重构为单一多模态大语言模型（Multimodal Large Language Models, MLLMs）的指令微调生成任务，通过思维链（Chain-of-Thought, CoT）推理与高斯风险感知框扰动（Gaussian Risk-Aware Box Perturbation, GRBP）实现端到端联合优化。该方法在无外部知识依赖下超越了所有流水线基线，但在绝对性能上仍低于依赖重型外部检索的 SOTA 方法，其推理延迟与长尾泛化能力尚存疑。

】

---

【Memory-Guided Hard Data Augmentation for Multimodal Named Entity Recognition ｜记忆引导的硬数据增强

研究机构：东华大学、复旦大学

作者：Xinyu Liu、Kai fu、Yinghan Shi 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cd5277b2a723)

> 多模态命名实体识别（Multimodal Named Entity Recognition, MNER）面临数据稀缺与模型架构特异性盲点的双重制约，现有通用数据增强方法因忽略模型内部状态而难以系统性修复复杂缺陷。本文切入点在于将数据增强从“无状态随机扰动”转变为“模型感知的逻辑修复”，通过构建记忆树归纳宏观错误模式来指导针对性合成。该框架在Twitter基准上验证了模型感知增强的有效性，但其对特定架构盲点的依赖性及离线计算成本限制了其通用性。

】

---

【SAM-NER: Semantic Archetype Mediation for Zero-Shot Named Entity Recognition ｜语义原型中介的零样本命名实体识别

作者：Ruichu Cai、Juntao Gan、Miao Mai 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.03706)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.03706)

> 零样本命名实体识别（Zero-shot NER, ZS-NER）旨在无目标域监督下识别新领域实体，但大语言模型（LLM）的内在语义与细粒度目标标签常错位，导致系统性语义漂移。现有指令微调与检索增强方法分别受限于语义对齐假设失效与外部知识覆盖不足，难以在异构标签体系下稳定泛化。SAM-NER 通过引入领域不变的“语义原型”中间层，将实体发现、抽象中介与定义校准解耦为三阶段流程，以稳定跨域推理。该方法在 CrossNER 基准上取得 66.3 的平均 F1，验证了中介范式的有效性，但其对固定原型空间的依赖及在语义距离较近类型上的性能衰减，仍构成泛化边界。

】

---

【Scaling Performance and Low-Resource Annotation with Many-Shot In-Context Learning for Named Entity Recognition ｜多示例上下文学习驱动的低资源实体识别标注

作者：Qi Zhang、Fangping Lan、Cornelia Caragea 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.21890)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.21890)

> 导读 低资源命名实体识别（Named Entity Recognition, NER）面临标注数据稀缺与领域术语专业性强导致的模型泛化失效问题。现有方法或依赖大规模人工标注训练小型模型，或直接用大语言模型（Large Language Models, LLMs）进行少样本推理，但后者在结构化任务上精度不足且推理成本高。本文切入点在于将LLM从“推理器”转变为“标注器”，利用多示例上下文学习（In-Context Learning, ICL）生成高质量训练数据以微调轻量级模型。通过构建包含置信度筛选与错误感知修正的框架，该方法在低资源基准上显著提升了下游模型性能，但其在非拉丁脚本语言及多模态场景下的适用性仍存疑。

】
