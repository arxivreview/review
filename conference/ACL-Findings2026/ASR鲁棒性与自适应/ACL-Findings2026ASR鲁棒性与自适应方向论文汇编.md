# ACL-Findings2026 · ASR鲁棒性与自适应方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Pseudo2Real: Task Arithmetic for Pseudo-Label Correction in Automatic Speech Recognition ｜伪标签系统偏差的参数空间校正

研究机构：国立台湾大学、新加坡南洋理工大学

作者：Yi-Cheng Lin、Yu-Hsuan Li Liang、Hsuan Su 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.08047)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.08047)

> 当ASR模型面对无标注的新口音域时，伪标签微调会继承教师模型的系统性偏差，导致性能停滞。现有置信度过滤或迭代自训练仅能抑制随机噪声，无法消除结构化错误。Pseudo2Real通过计算源域真实标签与伪标签微调模型的参数差，构建校正向量并直接加到目标域模型上，实现无真值下的偏差修正。该方法在AFRISPEECH-200上取得显著相对提升，但其跨语言家族迁移稳定性与校正向量可解释性仍存疑。

】
