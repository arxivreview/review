# ACL-Findings2026 · 多语言与低资源情感分析方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Exploring Multilingual Pre-trained Language Model for Aspect-based Sentiment Analysis ｜跨语言知识融合框架

作者：Ye Wang、Ruijun Jiang、Zhongqing Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b923637bc516)

> 方面级情感分析（ABSA）在低资源语言中受限于标注数据稀缺，导致模型难以捕捉细粒度语义依赖。现有跨语言迁移方法多依赖静态嵌入或单一翻译策略，缺乏对源语言与目标语言语义对齐的动态建模。本文提出跨语言知识融合框架，通过设计单轮与双轮双语预训练任务，结合LoRA参数融合，增强多语言模型对ABSA的泛化能力。该方法在英、中、日、德四语数据集上显著优于基线，但其性能增益是否源于翻译质量而非预训练机制本身，仍需进一步验证。

】

---

【Human-Centered Supervision for Sentiment Analysis in Telugu: A Systematic Inquiry Beyond Accuracy ｜泰卢固语情感分析中的人类理由监督

研究机构：美国马里兰大学帕克分校

作者：Vallabhaneni Raj Kumar、Ashwin S、Supriya Manna 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d60afe03df54)

> 导读 泰卢固语等低资源语言的情感分析长期受困于标注数据匮乏与模型黑盒化，导致预测结果缺乏可解释性且难以评估社会偏见。现有基准仅记录最终标签，忽略了标注者决策背后的主观推理过程，使得模型无法对齐人类价值观。本文通过构建包含多标注者理由的 TeSent 数据集，并引入基于理由向量的辅助损失函数，将人类主观解释转化为训练信号。这一方法在提升分类精度的同时显著增强了模型解释与人类推理的对齐度，但其对特定预训练模型（如 XLM-R）的性能负面影响及理由监督的泛化边界仍存疑。

】
