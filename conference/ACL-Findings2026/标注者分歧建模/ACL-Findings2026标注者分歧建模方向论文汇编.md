# ACL-Findings2026 · 标注者分歧建模方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Beyond Black-Box Labels: Interpretable Criteria for Diagnosing Subjective NLP Tasks ｜标注模式诊断：从标签聚合到标准有效性审计

作者：Nisrine Rair、Alban Goupil、Valeriu Vrabie 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a4324666abc3)

> 主观NLP任务中，将多标注者判断聚合为单一金标准会掩盖标准本身的模糊性，导致模型拟合错误模式或丢失有效信号。现有分歧建模方法多在标签层分析，假设标注模式（Schema）已足够清晰，无法区分分歧源于标准边界模糊还是标注者随机噪声。本文切入点在于前置审计：在构建金标准前，通过多标注者对二元标准的判断，量化标准的稳定性与类别的可分离性。其核心是提出基于条件重叠率与近平局率的模式诊断框架。该框架在商业文档采购场景下验证了分歧的结构化特征，但缺乏跨任务泛化验证，且依赖LLM面板可能引入模型同质化偏差。

】

---

【Modeling Human Perspectives with Socio-Demographic Representations ｜社会人口统计对比学习

研究机构：德国图宾根大学

作者：Leixin Zhang、Cagri Coltekin

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_65df7c2d8c5b)

> 标注者分歧建模旨在将人类标注中的不一致从需消除的噪声重构为反映价值观多样性的信号，其核心在于构建能预测判断分布而非单一标签的模型。现有社会感知方法多依赖单属性分组或独立输出头，在稀疏标注数据下难以捕捉复杂社会背景对视角的联合影响，导致模型在主观任务上存在公平性偏差。本文提出 Socio-Contrastive Learning，通过对比损失联合优化社会人口统计表征与标签预测，以解决多属性组合下的稀疏数据建模难题。该方法在仇恨言论与毒性检测任务上显著优于基线，验证了社会特征对视角预测的贡献，但其评估指标仍基于分类准确率而非分布对齐，且未涵盖最新 LLM 对齐框架。

】

---

【Position: From Noise to Signal to Selbstzweck - Reframing Human Label Variation in the Era of Post-training in NLP ｜从噪声到目的：人类标签变异在LLM后训练中的本体论重构

研究机构：丹麦哥本哈根大学、德国慕尼黑大学

作者：Shanshan Xu、Santosh T.Y.S.S、Barbara Plank

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3f1e994b21f1)

> 标注者分歧长期被视为需清洗的噪声，导致主观任务模型系统性丢失少数派视角。现有分布预测方法虽能建模分歧，但忽略了分歧在数据源头被聚合丢弃的根本原因。本文提出将人类标签变异（Human Label Variation, HLV）升格为“目的本身”（Selbstzweck），主张在偏好数据构建阶段保留标注者级原始数据，而非仅在后端建模。该立场论文未提供算法验证，其价值在于确立了数据治理的伦理边界，但缺乏量化证据证明数据端多样性保留能直接转化为模型性能提升。

】
