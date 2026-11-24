# ACL2026 · 历史文档OCR与分析方向论文汇编

> 本方向共 2 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Beyond Atomic Characters: Glyph-Aware Sub-character Alignment for Low-Resource Multilingual OCR ｜超越原子字符：面向低资源多语言OCR的字形感知子字符对齐

研究机构：北京理工大学

作者：Mengxiao Zhu、Haixu Chen、Jiu Sha 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b929b329633e)

> 低资源多语言OCR面临字形拓扑复杂与标注数据稀缺的双重困境，导致现有模型在视觉相似字符间频繁混淆。传统流水线依赖昂贵标注且误差累积，通用多模态大语言模型（MLLMs）则因视觉接地粗粒度而丧失细粒度字形区分能力。本文提出BASA框架，通过引入字形感知细粒度适配器（GAFA）显式对齐子字符结构，并配合反向合成数据管道实现零成本组件级监督。该方案在复杂字形场景下显著优于强基线，但其在高资源通用文档上的泛化边界及跨脚本迁移能力仍存疑。

】

---

【Draft, Verify, Restore: Self-Refining Historical Inscription Restoration with a Unified MLLM ｜统一多模态大语言模型驱动的历史碑刻修复

研究机构：华南理工大学

作者：Yuyi Zhang、Junle Liu、Peirong Zhang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bd7b74645fcb)

> 历史碑刻因物理退化导致文字不可读，传统修复依赖人工或级联流水线，存在误差累积与局部修复割裂全局风格的问题。本文提出UniHIR，首个端到端统一多模态大语言模型（Unified MLLM），通过草稿引导定位与层级自精炼机制实现页级视觉-文本联合复原。该方法在严重损毁碑刻上将OCR准确率从55.68%提升至86.65%，验证了统一架构在复杂退化场景下的有效性，但其性能高度依赖自建基准，跨域泛化能力尚存疑。

】
