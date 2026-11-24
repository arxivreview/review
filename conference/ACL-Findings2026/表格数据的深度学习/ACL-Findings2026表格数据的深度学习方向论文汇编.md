# ACL-Findings2026 · 表格数据的深度学习方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【MaskTab: Scalable Masked Tabular Pretraining with Scaling Laws and Distillation for Industrial Classification ｜MaskTab：面向工业级高缺失表格数据的自监督预训练与蒸馏框架

研究机构：浙江大学

作者：Bo Zheng、Yudong Chen、Zihua Xiong 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.11408)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.11408)

> 导读 工业级表格数据面临高维稀疏、缺失值蕴含信号且标签稀缺的三重困境，传统梯度提升树（GBDT）虽鲁棒但缺乏自监督预训练机制，而现有表格基础模型受限于中小规模数据假设，难以处理大规模真实分布。MaskTab 将缺失值编码为可学习令牌，通过双路径混合预训练联合优化掩码重建与任务监督，并利用混合专家（MoE）路由处理高维特征交互。该框架在工业基准上实现了超越 GBDT 的性能，并验证了数据、特征与模型规模的扩展规律，但其对私有数据的依赖与合成数据范式的偏离使其泛化边界尚存疑。

】
