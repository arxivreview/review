# ACL-Findings2026 · 多模态情感计算方向论文汇编

> 本方向共 4 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Beyond Polarity: Continuous Affect-Enhanced Multimodal Aspect-Based Sentiment Classification ｜连续情感增强的多模态方面级情感分类

研究机构：北京理工大学

作者：Ling-Ang Meng、Tianyu Zhao、Dawei Song 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b0c5e7d97b84)

> 多模态方面级情感分类（MABSC）旨在从图文数据中预测特定方面词的情感极性，但现有方法多依赖离散极性模式与通用视觉嵌入，难以捕捉隐式或细微的情感表达。本文切入点在于将连续效价-唤醒度-支配度（VAD）信号引入方面级推理，并通过构建情感增强数据集微调视觉编码器以获取情感敏感表示。具体做法是设计VAD编码器提取文本连续情感向量，利用FiLM调制机制注入文本特征，并在Senti-COCO数据集上微调CLIP图像编码器。该框架在Twitter-15和Twitter-17上取得了SOTA结果，但其对VAD弱监督标签噪声的敏感性以及未涉及复杂推理场景的局限性，使其在应对高歧义情感时仍存疑。

】

---

【Fast Retrieval and Slow Reasoning for Explainable Multimodal Sentiment Analysis ｜快速检索与慢速推理的多模态情感分析

研究机构：合肥工业大学

作者：Aoqiang Zhu、Min Hu、Yan Xing

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_faa68de3ea41)

> 多模态情感分析（Multimodal Sentiment Analysis, MSA）旨在通过融合文本、音频和视觉信号预测情感极性，但现有全序列融合方法将冗余噪声与有效情感线索混合处理，导致模型对无关模式敏感且决策过程不透明。FRSR 借鉴双过程理论，将建模拆解为证据检索与结构化推理两个阶段，通过稀疏化输入降低计算开销并提升可解释性。该框架在三个基准上取得了有竞争力的性能，但其精度未超越基于大语言模型的最新方法，且 Top-K 稀疏化对长程依赖的影响尚存疑。

】

---

【JX4MEI: Multimodal Semantically-Enhanced LLM for Joint Multimodal Emotion-Intent Explanation and Classification ｜联合情感意图解释与分类

研究机构：美国东北大学

作者：YiJie Huang、Xiaocui Yang、Shi Feng 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1b51a061b85a)

> 多模态情感计算长期受困于“黑盒分类”困境，模型能预测用户情绪却无法解释成因，导致在心理健康等高利害场景中缺乏可信度。现有大语言模型（MLLM）方案虽引入生成式推理，但特征对齐机制粗糙，难以捕捉细粒度因果线索。本文提出 JX4MEI 任务与 XMEI-Qwen 模型，通过语义引导的查询机制强化模态特征与高层语义的对齐。该工作填补了情感与意图联合解释的空白，但其依赖人工精修数据，模型对真实噪声的鲁棒性尚存疑。

】

---

【Uncertainty-Calibrated Elastic Alignment for Multimodal Sentiment Analysis with Missing Modalities ｜不确定性校准弹性对齐

研究机构：武汉大学

作者：Kang He、Yuzhe Ding、Rao Fu 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_447194c7ee00)

> 多模态情感分析在真实场景中常遭遇模态动态缺失，现有确定性补全方法将语义歧义强行拟合为单一目标，导致特征空间扭曲与决策边界漂移。EASE 将补全重构为条件密度估计，利用学习到的方差信号在再生核希尔伯特空间中动态调节对齐强度，并引入跨视图预测一致性约束以稳定判别逻辑。该方法在缺失率高达 0.9 时仍保持优于基线的性能下限，但其弹性机制是否会在完整数据下牺牲精度，论文未提供直接对照。

】
