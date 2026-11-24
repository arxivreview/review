# ACL-Findings2026 · 大语言模型内部表示的可解释性方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Beyond Neural Incompatibility: Cross-Scale Knowledge Transfer in Large Language Models through Latent Semantic Alignment ｜基于潜空间语义对齐的跨尺度参数知识迁移

研究机构：澳大利亚莫纳什大学、德国慕尼黑工业大学

作者：Jian Gu、Aldeida Aleti、Chunyang Chen 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c08b3ddcd68c)

> 大语言模型（LLM）内部蕴含大量参数化知识，但将其从大模型迁移至小模型时，架构差异导致的“神经不兼容性”使得直接参数复用失效。现有方法多依赖参数提取与注入，忽略了激活空间几何结构的对齐，导致迁移不稳定且计算成本高。本文提出 SemAlign，通过词汇定义的语义基将源模型层输出分解并重组为目标空间的监督信号，实现无参数注入的跨尺度迁移。该方法在 Llama-2 系列模型上验证了有效性，但其对同族模型的依赖及缺乏因果机制验证限制了通用性。

】

---

【Concept Tokens: Learning Behavioral Embeddings Through Concept Definitions ｜概念令牌：基于定义文本的行为嵌入学习

作者：Ignacio Sastre、Aiala Rosá

论文原文见 [arXiv](https://arxiv.org/abs/2601.04465)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.04465)

> 大语言模型（LLM）内部计算的黑盒特性使得通过外部提示精确控制特定行为变得困难，尤其是当模型缺乏对抽象概念（如“幻觉”或“重述”）的显式理解时。现有软提示方法依赖任务标签或长上下文，无法仅凭概念定义实现行为引导，且长上下文易导致指令遵循能力下降。本文提出概念令牌，通过优化单一输入嵌入向量，使冻结模型从概念定义中内化行为模式。该方法在幻觉抑制和教学反馈场景中展现了方向性控制能力，但其对复杂事实细节的编码可靠性存疑，且未验证内部激活的因果必要性。

】

---

【Conceptual Hierarchies within LLMs ｜概念层级在LLM中的因果定位

研究机构：美国史蒂文斯理工学院

作者：Tiago Almeida、Zining Zhu、Yue Ning

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5c1814416acd)

> 导读 机制可解释性（MI）旨在逆向工程大语言模型（LLMs）内部计算结构，以解释其行为并支持安全对齐。现有研究多依赖探针等相关性方法或针对单一事实的因果干预，缺乏对多粒度语义概念在模型内部组织结构的因果性验证。本文采用对称令牌替换（STR）激活补丁，结合重心（Center-of-Gravity）指标，在六个LLM中因果定位细粒度与粗粒度概念的存储顺序。该工作提供了概念层级存储的因果证据，但受限于特定词汇库与统计显著性的边界，其结论的普适性仍需更广泛的语义网络验证。

】
