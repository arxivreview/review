# ACL-Findings2026 · 基于文本的人物搜索与再识别方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Bridging the Pose-Semantic Gap: A Cascade Framework for Text-Based Person Anomaly Search ｜结构-语义解耦级联框架

研究机构：浙江大学、新加坡国立大学

作者：Zequn Xie、Guijin Luo、Chuxin Wang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.23282)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.23282)

> 文本驱动行人异常检索（Text-based Person Anomaly Search, TPAS）旨在通过自然语言描述定位监控档案中的特定行为事件，其核心难点在于几何结构相似但语义截然不同的动作（如跌倒与俯卧撑）极易被传统姿态模型混淆。现有方案要么依赖轻量级模型牺牲语义精度，要么直接部署多模态大语言模型（MLLM）导致推理延迟无法满足实时需求。本文提出结构-语义解耦级联框架（Structure-Semantic Decoupled Cascade, SSDC），通过轻量级结构粗筛与多智能体语义验证的两阶段解耦，在保持高精度的同时大幅降低计算开销。该框架在PAB基准上取得了具有竞争力的性能，但其绝对精度仍低于当前SOTA，且多智能体协作的必要性缺乏充分的消融对比。

】

---

【Iterative Self-Correction for Text-Driven Person Re-Identification with Large Vision-Language Models ｜自主闭环迭代修正的视觉语言模型行人重识别

研究机构：浙江大学、新加坡国立大学

作者：Guijin Luo、Zequn Xie、Sihang Cai 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7bd4fc5dea5b)

> 行人重识别（ReID）旨在跨摄像头匹配同一身份，但现有基于视觉语言模型（VLM）的方法多采用单次编码-匹配范式，导致初始描述错误无法修正且细粒度特征丢失。本文提出 Auto-ReID，将 ReID 重构为“思考-精炼”的迭代闭环，通过分层渐进微调赋予 VLM 属性推理与纠错能力。该方法在遮挡与换装场景下显著优于静态基线，但其性能增益高度依赖迭代深度与候选集规模，且未验证在大规模开放世界中的泛化边界。

】
