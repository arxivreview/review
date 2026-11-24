# ICLR2026 · Segment Anything 模型适配与提示工程方向论文汇编

> 本方向共 1 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Efficient-SAM2: Accelerating SAM2 with Object-Aware Visual Encoding and Memory Retrieval ｜基于对象感知的稀疏计算调度加速 SAM2

研究机构：中国科学院、中国科学院大学

作者：Jing Zhang、Zhikai Li、Xuewen Liu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.08224)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.08224)

> 视频对象分割基础模型 SAM2 因庞大的图像编码器与帧级记忆交互产生高延迟，阻碍实时部署。现有加速方案多依赖重训轻量骨干或通用 Token 合并，前者成本高昂，后者因架构不匹配导致精度骤降。本文切入点在于发现 SAM2 内部存在“稀疏感知”与“密集计算”的矛盾，提出后训练稀疏加速框架。通过窗口级路由与记忆检索剪枝，在几乎不增加参数的情况下实现显著提速。该方案在速度-精度权衡上优于现有基线，但其对上一帧掩码的强依赖在长序列误差累积下的鲁棒性存疑。

】
