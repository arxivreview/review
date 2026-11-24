# ACL-Findings2026 · AI生成视频评估与编辑方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Detecting AI-Generated Video: A Vision–Language Dual-View Survey ｜AI生成视频检测：从伪影匹配到事实保真度验证

研究机构：中国人民大学、美国哈佛大学

作者：Dylan Xinming Hou、Juntian Zhang、Xu Gu 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fd5ea6ac87df)

> 现有AI生成视频检测依赖低层视觉伪影，但高保真生成模型已消除这些痕迹，导致检测器失效。本文提出“事实保真度验证”范式，将检测重构为对视频内容是否符合真实世界物理与逻辑规则的语义校验。通过构建视觉-语言双视图四层分类体系，整合从像素级伪影到世界知识推理的证据链。该框架为可解释检测提供了结构化路线图，但其作为综述未提供统一基准下的量化对比，各层方法的实际增益边界尚不明确。

】

---

【MSVBench: Towards Human-Level Evaluation of Multi-Shot Video Generation ｜多镜头视频生成评估基准

研究机构：哈尔滨工业大学

作者：Haoyuan Shi、Yunxin Li、Nanhao Deng 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.23969)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.23969)

> 多镜头视频生成正从单片段拼接向长叙事演进，但现有评估体系仍锚定单镜头范式，无法捕捉跨镜头的时序逻辑与主体一致性断裂。MSVBench 通过构建层级化脚本架构与混合评估器，将评估粒度从全局标量下沉至镜头级时空定位。该框架实现了与人类判断 94.4% 的斯皮尔曼相关系数，并验证了评估轨迹向监督信号转化的可行性。其核心局限在于对连续生成模型镜头边界缺失的适配困难，以及故事样本量对统计稳健性的潜在制约。

】
