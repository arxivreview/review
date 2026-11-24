# ACL-Findings2026 · 大语言模型越狱抵抗的自卫与自我精炼机制方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense ｜解码时隐藏状态轨迹检测

作者：Cheng Liu、Xiaolei Liu、Xingyu Li 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.07727)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07727)

> 大语言模型（LLM）面临越狱攻击时，静态输入过滤常因语义伪装而失效，且后处理检测无法阻止有害内容生成。现有解码时防御多依赖额外训练的安全探针，成本高且仅做单点判断，忽略了风险在解码过程中的动态累积。TrajGuard 提出免训练的流式几何监控与条件触发的语义裁判级联框架，在解码过程中实时追踪隐藏状态轨迹以拦截越狱。该方法在开源模型上实现了高拦截率与低延迟，但其对黑盒 API 的适用性及免训练几何统计在分布外攻击下的鲁棒性仍存疑。

】
