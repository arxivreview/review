# ACL-Findings2026 · 专利自然语言处理与人工智能分析方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【P-QuASAR: A Unified Probabilistic Framework for Holistic Patent Quality Assessment and Refinement ｜专利质量结构化评估与修复

研究机构：美国埃默里大学、西安电子科技大学

作者：Xinyuan Song、Ziyi Ni、Fred Yang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_862dfcb95c20)

> 专利说明书的质量评估长期面临多维缺陷相互独立检测导致的证据隔离与修复建议脱节问题。现有模块化流水线无法共享跨维度线索，且通用检测器缺乏针对法律与技术细节的校准能力。P-QuASAR 通过构建质量图（Quality Graph）进行联合概率推理，将缺陷检测转化为图上的后验分布估计，并基于此推导最优干预路径。该框架在自建数据集上显著提升了检测精度与修复效果，但其结论受限于单一司法管辖区的小规模样本，跨域泛化能力存疑。

】

---

【Reasoning for Hierarchical Text Classification: The Case of Patents ｜层级文本分类中的推理增强：以专利IPC分类为例

研究机构：英国剑桥大学、中国科学院

作者：Lekang Jiang、Wenjun Sun、Stefan Goetz

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a9a231a7c887)

> 专利IPC分类面临标签空间巨大且层级依赖复杂的问题，传统微调模型仅输出扁平标签，缺乏审查员所需的决策依据。现有方法在可解释性与跨域泛化上存在瓶颈，本文切入点在于将分类重构为逐步推理任务。通过冷启动对齐思维链格式并引入可验证奖励强化学习，RHC在保持高精度的同时生成了可审计的逻辑链条。该方法在USPTO与EPO数据集上验证了推理框架的有效性，但其对教师模型合成数据质量的依赖及跨司法管辖区性能衰减仍存疑。

】

---

【Towards IP Intelligence: Benchmarking Large Language Models on Intellectual Property Knowledge and Practice ｜知识产权大语言模型基准测试

研究机构：中国科学院、澳大利亚新南威尔士大学

作者：Qiyao Wang、Guhong Chen、Hongbo Wang 等 23 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8783dcbd7193)

> 现有专利自然语言处理基准多局限于单一专利文本的语义匹配或摘要生成，缺乏对商标、版权等多元知识产权机制及法律推理深度的覆盖，导致无法全面评估大语言模型在真实法律实务中的能力。IPBench 基于 Webb 的知识深度理论构建了四级任务分类法，填补了跨机制、跨认知层级的评估空白。该基准通过 10,374 个双语样本量化了通用模型与垂直模型在信息处理、逻辑推理及创造性生成上的表现差异。尽管其揭示了垂直模型在复杂推理任务上的泛化瓶颈，但评估结果对模型训练语言与司法管辖区的强依赖性仍存疑。

】
