# CVPR2026 · 情感与运动解码中的EEG和EMG信号处理方向论文汇编

> 本方向共 2 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Reading Your Actions: Learning Generalizable Action Representations via Pre-training AEMG ｜神经收缩分词器与掩码重建：EMG通用表示学习框架

研究机构：华南理工大学

作者：Zhenghao Huang、Huilin Yao、Kaikai Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f08949baee17)

> 表面肌电（sEMG）解码长期受限于数据异构性与标注稀缺，导致模型难以跨被试、跨设备泛化。现有方法或依赖特定任务格式，或采用固定滑动窗口，无法捕捉肌肉协同的生理语义。本文提出AEMG，通过神经收缩分词器将连续信号离散为“生理语言”，并基于向量量化与掩码重建进行大规模自监督预训练。该框架在零样本留一法交叉验证中较基线提升5.79–9.25%，但离散化过程对连续运动解码精度的潜在影响尚未得到充分验证。

】

---

【Translating Signals to Languages for sEMG-Based Activity Recognition ｜将sEMG信号转化为类语言表示以驱动大语言模型活动识别

研究机构：英国兰卡斯特大学、澳大利亚莫纳什大学

作者：Ming Wang、Haoxuan Qu、Qiuhong Ke 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.22403)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.22403)

> sEMG活动识别的核心瓶颈在于连续生理信号与大语言模型（LLM）离散文本输入格式间的表征鸿沟，直接微调LLM易导致预训练语义先验的灾难性遗忘。本文切入点在于不修改LLM权重，而是通过“语言涌现”机制将sEMG转化为具备人类语言统计特性的“sEMG语言”。具体做法是结合VQ-VAE离散化、Lewis Signaling Game迭代学习与人类语言偏置正则化，构建信号到语言的映射。该方法在GRABMyo数据集上取得95.14%准确率，但缺乏跨被试泛化评估，其语义推理能力的实际贡献仍存疑。

】
