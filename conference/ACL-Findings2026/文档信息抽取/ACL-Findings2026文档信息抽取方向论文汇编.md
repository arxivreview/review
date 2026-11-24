# ACL-Findings2026 · 文档信息抽取方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Infinity-Parser: Layout-Aware Reinforcement Learning with High-quality Document Parsing Dataset ｜布局感知强化学习文档解析器

研究机构：英国利物浦大学

作者：Baode Wang、Biao Wu、Weizhen Li 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_02734a87777b)

> 端到端文档解析旨在将扫描图像直接转换为结构化Markdown，但现有视觉语言模型（VLM）在监督微调（SFT）下易过拟合表面模式，导致分布外（OOD）泛化能力不足。Infinity-Parser通过构建400,066页高质量数据集Infinity-Doc-400K，并引入基于编辑距离、段落计数与阅读顺序的多面奖励强化学习（RL）框架，解决了SFT在复杂布局下的结构一致性退化问题。该方法在OmniDocBench上取得0.122的英文整体编辑距离，验证了RL在文档解析中的有效性，但其绝对性能仍低于部分最新SOTA，且对合成数据依赖性的边界尚存疑。

】

---

【Switching Heads and Softening Tokens: Turnkey Solutions to Visually Grounded Document QA ｜视觉定位文档问答中的离散-连续监督解耦

作者：Ximing Wen、Wenbo Li、Sudipta Paul 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ab5c6044d923)

> 视觉定位文档问答（Visually Grounded Document Question Answering, VGDQA）要求模型不仅回答自然语言查询，还需在文档图像中精确定位答案对应的边界框。现有方法要么依赖刚性后处理导致多答案场景失效，要么将坐标视为普通文本token而丧失空间距离感知，导致细粒度定位收敛缓慢。本文通过引入可微分软token机制与双头回归架构，在统一LLM骨干中实现了结构鲁棒性与空间精度的互补集成。该方案在基准测试中确立了新的性能上限，但其对OCR输入质量的强依赖及长文档下的注意力衰减，限制了其在复杂真实场景中的泛化边界。

】
