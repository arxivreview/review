# ACL-Findings2026 · 基于大语言模型的程序合成与验证方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Beyond Superficial Tests: Adversarial Refinement for Reliable Property-Based Testing ｜对抗性精炼的属性测试生成框架

研究机构：北京航空航天大学

作者：Xiao Li、Runlin Liu、Zhe Zhang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_60306a166b2a)

> 现有基于大语言模型（LLM）的属性测试（Property-Based Testing, PBT）生成方法存在“表面性鸿沟”，即生成的测试脚本虽语法正确，但往往包含语义空泛的弱属性，无法有效区分正确实现与错误实现。本文切入点在于利用“构造比证伪更难”的语义不对称性，将PBT生成重构为生成器与验证器之间的对抗博弈。PROBE通过构建跨函数语义图定位全局依赖，并让验证器主动构造满足当前属性但语义错误的反实现，以此迭代强化属性强度。该框架在真实Python库中发现了45个未知Bug，但其在非Python生态及并发系统下的泛化能力仍存疑。

】

---

【Efficient PRM Training Data Synthesis via Formal Verification ｜形式化验证驱动的过程奖励模型数据合成

研究机构：美国宾夕法尼亚州立大学、美国哥伦比亚大学

作者：Ryo Kamoi、Yusen Zhang、Nan Zhang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2505.15960)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_28436e84e902)

> 导读 过程奖励模型（Process Reward Model, PRM）旨在通过细粒度监督提升大语言模型（LLM）的推理能力，但现有训练数据构建依赖昂贵的人工标注或噪声较大的蒙特卡洛采样。本文提出FOVER框架，利用Z3和Isabelle等形式化验证工具对形式化推理任务中的步骤进行自动、精确的错误标注，从而高效合成高质量PRM训练数据。实验表明，基于该数据微调的PRM在非形式化逻辑与数学基准上显著优于基线，验证了形式化到非形式化的迁移有效性。尽管数据效率与跨任务泛化能力突出，但方法受限于形式化任务的覆盖范围，且离线标注策略未解决在线推理时的动态适应问题。

】

---

【Improving LLM Code Reasoning via Semantic Equivalence Self-Play with Formal Verification ｜基于形式化验证的语义等价自博弈训练

研究机构：英国爱丁堡大学

作者：Antonio Valerio Miceli Barone、Poon Tsz Nok

论文原文见 [arXiv](https://arxiv.org/abs/2604.17010)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17010)

> 现有LLM在代码生成中常因缺乏深层语义理解而产生逻辑错误，传统测试套件无法覆盖所有边界情况，导致程序重构与优化中的等价性判定不可靠。本文切入点在于利用Haskell语言的纯函数特性与Liquid Haskell的形式化证明能力，构建一个生成器与评估器对抗的自博弈闭环，通过形式化证明作为确定性监督信号来训练模型识别程序语义等价性。该方法在EquiBench上实现了最高13.3个百分点的准确率提升，并验证了等价性证明监督对语义推理能力的独特贡献。然而，该方法局限于Haskell生态，且在小模型规模下证明生成率极低，其跨语言泛化能力与大规模系统适用性仍存疑。

】
