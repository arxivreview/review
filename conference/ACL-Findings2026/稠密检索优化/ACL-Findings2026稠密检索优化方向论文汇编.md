# ACL-Findings2026 · 稠密检索优化方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AURORA: Neuro-Symbolic Continual Indexing for Evolving RAG Systems ｜神经符号持续索引框架

研究机构：美国弗吉尼亚理工大学、美国哥伦比亚大学

作者：Manoj Saravanan、Rohit Kumar Salla、Ramya Manasa Amancherla

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_78b787e89e90)

> 动态语料库下的检索基础设施面临分布漂移导致的性能坍塌，而全量重建索引的计算成本使其在实时场景不可行。现有方案要么牺牲精度换取速度，要么陷入灾难性遗忘。AURORA 将索引维护重构为少样本持续学习问题，通过冻结拓扑、更新度量参数实现高效适应。该框架在受控实验下验证了适应效率与召回恢复能力，但其对真实世界渐进式语言演化的泛化性仍存疑。

】

---

【Let Retrievers Think Before Action: Thought-Augmented Embedding for Dense Retrieval ｜让检索器先思考再行动：思维增强嵌入

研究机构：中国科学技术大学、北京大学

作者：Ruiran Yan、Wen Xiong、Ze Liu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_00e75b0f5cd9)

> 导读 稠密检索在处理多跳推理或零样本场景时，常因静态嵌入无法捕捉查询内部的逻辑推导而失效。现有方案要么依赖外部大语言模型重写查询导致部署复杂，要么采用隐式推理牺牲可解释性。本文提出O1 Embedder，将显式思维生成与嵌入计算统一于单一模型，通过“探索-精炼”数据合成与多任务联合训练解决思维数据缺失与模块冲突问题。该方法在推理密集型任务上显著优于基线，但其在垂直领域的增益有限，且显式推理的延迟成本未得到充分量化。

】

---

【The Overlooked Role of Graded Relevance Thresholds in Multilingual Dense Retrieval ｜多语言稠密检索中分级相关性阈值的校准机制

作者：Tomer Wullach、Ori Shapira、Amir David Nissan Cohen

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_10874e2023f6)

> 多语言稠密检索微调长期依赖二值化相关性标注，忽略了相关性本身的连续性与语言资源差异对正负样本分布的异质性影响。现有对比学习流程将分级标注简单截断为二值信号，导致低资源语言因正例多样性不足而性能受损，高资源语言则因噪声正例引入而区分度下降。本文通过系统性实验证明，阈值选择并非无关紧要的超参数，而是决定微调效率与泛化边界的关键变量。该研究揭示了阈值校准作为数据预处理核心环节的价值，但其结论局限于特定骨干模型与合成数据场景，对LLM嵌入模型的普适性存疑。

】
