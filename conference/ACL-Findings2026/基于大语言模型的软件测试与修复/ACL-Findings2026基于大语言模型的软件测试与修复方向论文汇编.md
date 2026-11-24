# ACL-Findings2026 · 基于大语言模型的软件测试与修复方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Program Structure-aware Language Models: Targeted Software Testing beyond Textual Semantics ｜图增强语言建模框架：分支定向测试生成

作者：Khang Tran、Khoa Nguyen、Cristian Borcea 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17715)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17715)

> 软件测试的核心痛点在于如何精准覆盖高风险执行路径，而非仅追求代码行数覆盖。现有基于大语言模型（LLM）的测试生成方法依赖提示工程启发式，受限于模型随机性，难以稳定命中特定分支。GLMTest 提出将代码属性图（CPG）结构嵌入与 LLM 文本语义在共享空间联合训练，实现分支定向生成。该方法在 TestGenEval 上将分支准确率从 27.4% 提升至 50.2%，但仅验证了 Python 单语言场景，且未对比专用测试生成 SOTA，其泛化边界尚存疑。

】
