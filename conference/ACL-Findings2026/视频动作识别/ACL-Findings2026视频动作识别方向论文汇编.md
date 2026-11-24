# ACL-Findings2026 · 视频动作识别方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A2O: LLM-based Agentic Learning of Action-to-Object Features for Video Action Recognition ｜代理式动作-物体特征学习

研究机构：OpenAI

作者：Taiki Sekii、Fumiaki Sato

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bd6930610105)

> 视频动作识别面临的核心矛盾是：基于视频体积的自监督模型易受背景捷径干扰，而基于物体检测的方法虽能抑制干扰却丢失场景上下文。现有方案在“保留信息”与“去除冗余”之间难以兼得，本文切入点在于利用大语言模型（LLM）的常识知识动态选择关注物体，通过上下文强化学习（ICRL）优化这一选择过程。具体做法是将LLM作为代理，结合开放词汇目标检测器（OVD）生成物体中心特征，注入视频基础模型以指导特征提取。该方法在抑制虚假相关方面表现优异，但在通用基准上的增益有限，且高度依赖LLM的推理稳定性。

】
