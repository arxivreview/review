# ACL-Findings2026 · 大语言模型中的神经符号逻辑推理方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【LSEG: A Fine-tuning Free Method for NL2FOL via Logic-Structure and Entropy Guided Inference Controlling ｜逻辑结构与熵引导推理控制

研究机构：中国科学院、中国科学院大学

作者：Yuwei Huang、Shi Wang、Kangli Zi 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ea6cd163bec2)

> 自然语言到一阶逻辑（NL2FOL）翻译的核心痛点在于大语言模型（LLM）内部表示漂移导致的逻辑幻觉，即生成语法正确但语义错误的公式。现有微调或代码生成方法虽能提升一致性，但依赖高昂训练成本或特定架构，且无法在推理时动态修正内部状态偏差。LSEG通过构建逻辑保持扰动向量并引入熵引导机制，在免微调条件下校正隐藏状态。该方法在FOLIO和MALLS上取得了与强监督模型相当的性能，但其对复杂量词交互的覆盖能力及统计显著性仍存疑。

】

---

【PrefRAG: Correcting Semantic Errors in Auto-Formalization for Logical Reasoning with Program Preference RAG ｜程序偏好检索增强生成

研究机构：中山大学

作者：Yuyin Zhou、Yongmei Liu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a22e11893b78)

> 神经符号逻辑推理的核心瓶颈在于自动形式化阶段的语义错误，现有方法仅能处理语法报错或约束级验证，缺乏程序级语义错误的系统性修正机制。本文通过构建语义错误分类法与偏好数据集，将检索增强生成（RAG）引入自精炼模块，使大语言模型（LLM）能自主识别并修复深层语义缺陷。该方法在分布内（ID）与分布外（OOD）基准上均超越基线，证明了语义偏好检索对推理鲁棒性的提升作用，但其性能增益在复杂数据集上趋于平缓，且依赖特定领域的错误模式覆盖度。

】
