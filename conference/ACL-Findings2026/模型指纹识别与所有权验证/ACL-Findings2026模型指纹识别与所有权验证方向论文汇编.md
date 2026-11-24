# ACL-Findings2026 · 模型指纹识别与所有权验证方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Ghost in the Shell: Synonym-Aware Logit Shaping Fingerprint for Copyright Protection of Large Vision-Language Models ｜同义词感知Logits塑形指纹

研究机构：北京大学

作者：Xiaofan Zheng、Xinghao Wang、Xiaojun Wan

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e19cd7208267)

> 大型视觉语言模型（LVLMs）的黑盒所有权验证面临鲁棒性与无害性的固有冲突：现有后门范式通过扭曲显式输出嵌入指纹，导致模态对齐破坏与多模态能力退化。本文提出同义词感知Logits塑形指纹（SALSF），将指纹嵌入从显式文本输出迁移至隐式Logits长尾空间，通过提升同义词簇概率而锁定Top-1预测，在保持模型通用性能的同时增强对抗鲁棒性。该方法在LVLM指纹任务中显著优于当前SOTA，但其对Logprobs API的依赖及同义词集规模的敏感性限制了其在严格黑盒场景下的普适性。

】
