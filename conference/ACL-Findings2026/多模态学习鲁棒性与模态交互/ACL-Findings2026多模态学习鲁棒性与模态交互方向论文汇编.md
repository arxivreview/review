# ACL-Findings2026 · 多模态学习鲁棒性与模态交互方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【DEAR: Distributional Error-Aware Reliability for Robust Multimodal Sentiment Analysis with Missing Modalities ｜分布误差感知可靠性框架

研究机构：华中科技大学

作者：Shihao Zou、Wei Wei、Yongshuo Zhang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3f1e1a3ad750)

> 多模态情感分析（Multimodal Sentiment Analysis, MSA）在模态缺失时性能骤降，根源并非单纯信息丢失，而是重构特征偏离原始分布流形导致的语义漂移。现有方法多依赖逐点匹配损失或固定融合规则，无法感知样本级不确定性，导致高缺失率下决策崩溃。DEAR 通过层级分布约束重构修复流形，并引入样本级不确定性估计驱动双流动态仲裁，实现从激进协同到保守回退的自适应切换。该方法在 MOSI 和 MOSEI 数据集的 F1 与相关性指标上优于主流基线，但其对随机缺失的依赖及未报告的计算开销限制了其在系统性缺失场景下的适用性。

】

---

【SCOPE: Preserving Modality-Specific Cues to Mitigate Modality Laziness in Multimodal Learning ｜结构一致对齐与扩散融合缓解多模态懒惰

研究机构：武汉大学

作者：Jingfan Yang、Rui Zhang、Liang Hong 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a684ce7a84f3)

> 多模态学习常陷入“模态懒惰”，即模型过度依赖主导模态而忽略互补信号，导致融合性能受限。现有架构正则化或动态协调方法虽能提升融合精度，却往往牺牲非主导模态的独立表征能力，造成表示坍缩。SCOPE 通过互信息引导解耦、参数-free语义图对齐及扩散注意力融合，在保留模态特定线索的同时实现结构级对齐。该框架在五个基准上取得最高27.10%的准确率提升，但其对预训练骨干的依赖及未涵盖缺失场景的局限，使其在动态异构环境下的鲁棒性存疑。

】
