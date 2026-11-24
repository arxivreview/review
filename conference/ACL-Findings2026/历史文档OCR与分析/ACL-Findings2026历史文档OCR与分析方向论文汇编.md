# ACL-Findings2026 · 历史文档OCR与分析方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Benchmarking Vision-Language Models on Chinese Ancient Documents: From OCR to Knowledge Reasoning ｜中文古籍多任务理解基准

研究机构：复旦大学

作者：Haiyang Yu、Yuchuan Wu、Fan Shi 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_191ac04eaab5)

> 视觉语言模型（VLMs）在处理中文古籍时，因竖排版式、繁体异体字及物理退化导致视觉接地失效，且现有基准仅覆盖现代印刷文档或简化字，无法评估从字符识别到知识推理的全链路能力。本文构建了首个涵盖OCR、翻译及三类问答的古籍基准AncientDoc，通过LLM辅助标注与人工校验生成3000页多任务数据。该基准揭示了通用VLMs在古籍OCR阶段的严重瓶颈，但其单一数据源与缺乏领域适配模型对比的局限，使其结论的普适性存疑。

】

---

【HisDoc-OCR: Restoring Visual Grounding in MLLMs for Chinese Historical Document OCR ｜中文历史文档OCR中的视觉接地恢复

研究机构：华南理工大学

作者：Jiahuan Cao、Yongxin Shi、Zeyu Shan 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c38988444613)

> 多模态大语言模型（MLLMs）在处理中文历史文档时，因视觉证据退化与语言先验冲突，常产生字符伪造与重复等幻觉。现有通用模型缺乏针对历史版式与古字体的对齐机制，导致识别精度与稳定性双低。本文通过布局注入、首次出现增强与自蒸馏注意力聚焦，在训练阶段重塑视觉-文本对齐。该方法在幻觉抑制上表现突出，但在纯识别精度上未超越专用布局感知模型，其通用性仍存疑。

】

---

【Leveraging External Knowledge for Historical Document Restoration via Retrieval-Augmented Large Language Models ｜基于检索增强大语言模型的历史文档受损字符复原

作者：Gabeen Kim、Kyeongpil Kang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c9f32802b601)

> 导读 历史档案因物理侵蚀导致大量字符不可读，传统掩码语言建模方法仅依赖单篇文档内部上下文，难以恢复需外部历史知识支撑的命名实体。本文切入点在于将大语言模型的隐式知识与显式检索增强生成结合，构建专门针对古代语料的复原框架。具体做法是微调Qwen3模型，利用BM25检索相关文档并引入时间元数据，以因果语言建模方式生成复原字符。该框架在命名实体恢复上显著优于通用大模型，但其评估仅依赖Top-1准确率，未涵盖结构完整性与语义一致性维度。

】
