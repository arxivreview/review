# ICLR2026 · CLIP适配与提示学习方向论文汇编

> 本方向共 3 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CARPRT: CLASS-AWARE ZERO-SHOT PROMPT REWEIGHTING FOR BLACK-BOX VISION-LANGUAGE MODELS ｜类感知零样本提示重加权

研究机构：澳大利亚墨尔本大学、东南大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_52823765)

> 零样本视觉-语言模型（VLM）分类对提示词措辞高度敏感，现有加权集成方法假设所有类别共享同一套提示权重，忽略了不同类别对特定提示的语义亲和力差异。本文指出这种类无关假设限制了模型表达力，提出类感知零样本提示重加权（CARPRT），通过无训练的前向推断计算每个类别的独立提示权重矩阵。该方法在11个基准上超越类无关基线，但其在大规模通用数据集上的增益幅度小于细粒度数据集，且未解决提示池本身质量不足的根本问题。

】

---

【Memory-Free Continual Learning with Null Space Adaptation for Zero-Shot Vision-Language Models ｜零空间约束下的无存储持续学习

研究机构：韩国首尔大学

作者：Yujin Jo、Taesup Kim

论文原文见 [arXiv](https://arxiv.org/abs/2510.21175)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.21175)

> 视觉-语言模型在部署后面临数据分布与任务需求的动态演变，但静态骨干网络无法在不进行大规模重训练的情况下吸收新知识。现有持续学习方法要么依赖线性增长的存储缓冲，要么引入无限膨胀的适配器模块，导致资源开销随任务数累积而不可持续。NuSA-CL 通过奇异值分解（SVD）动态识别权重矩阵中的低能量零空间，并将低秩更新严格约束在该子空间内，实现了固定参数预算下的知识累积。该方法在资源受限场景下展现出优越的效率-性能权衡，但其零空间约束是否限制了新任务的学习上限，仍需进一步验证。

】

---

【PI-CCA: PROMPT-INVARIANT CCA CERTIFICATES FOR REPLAY-FREE CONTINUAL MULTIMODAL LEARNING ｜提示不变正交相关分析证书

研究机构：北京大学、中国科学院

作者：Jiayu Zhang、Chuangxin Zhao、Canran Xiao 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_70860843)

> 视觉-语言模型在动态任务流中持续适配时，标准微调会破坏预训练的对齐几何，导致零样本能力丧失与提示敏感性激增。现有方法通过蒸馏logit或对齐相似度等代理信号来抑制遗忘，但这些间接约束无法直接控制驱动跨模态泛化的核心对象——白化交叉协方差的谱结构。本文提出PI-CCA，将遗忘重构为对齐几何漂移，通过维护一个紧凑的“CCA证书”（包含前k个正交相关系数与子空间草图），在仅使用当前mini-batch统计量的条件下直接约束对齐不变量。该方法在多个无回放基准上取得了SOTA性能，但其对极端域偏移下的子空间稳定性及计算开销的边界尚需进一步验证。

】
