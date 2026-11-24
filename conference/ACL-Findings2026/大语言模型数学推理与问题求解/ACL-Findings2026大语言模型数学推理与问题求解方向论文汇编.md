# ACL-Findings2026 · 大语言模型数学推理与问题求解方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning ｜轨迹融合：利用错误信号增强数学推理微调

作者：Jie Deng、Hanshuang Tong、Jun Li 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_602c04c6deae)

> 数学推理微调长期依赖拒绝采样，仅保留正确轨迹，导致模型无法从失败模式中习得纠错逻辑。现有数据合成方法聚焦于增加正确解的多样性或难度，却系统性丢弃了蕴含丰富诊断信息的错误路径。本文提出TrajFusion，通过自适应融合错误与正确轨迹构建试错式监督信号，在不改变训练目标的前提下提升推理鲁棒性。该方法在低数据量下显著优于基线，但其增益是否源于结构化的错误监督而非单纯的序列长度增加，仍需更严格的控制实验验证。

】

---

【CoTEvol: Self-Evolving Chain-of-Thoughts for Data Synthesis in Mathematical Reasoning ｜基于遗传算法的思维链自进化合成

研究机构：复旦大学、香港中文大学

作者：Zhuo Wang、Zhuo Zhang、Yafu Li 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14768)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14768)

> 大语言模型（LLM）在数学推理中的表现受限于高质量思维链（Chain-of-Thought, CoT）数据的稀缺与标注成本。现有蒸馏方法存在收益递减，而测试时搜索方法因采样独立性导致计算效率低下。COTEVOL将CoT合成重构为种群进化搜索问题，通过反射全局交叉与不确定性引导局部变异迭代优化推理轨迹。该方法以较低计算成本提升了合成数据的正确率，但其在小模型上的增益是否受限于骨干网络本身的推理上限，仍存疑。

】

---

【EngiBench: A Benchmark for Evaluating Large Language Models on Engineering Problem Solving ｜工程问题求解基准 EngiBench

研究机构：新加坡南洋理工大学、澳大利亚悉尼大学

作者：Xiyuan Zhou、Xinlei Wang、Yirui He 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.17677)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.17677)

> 现有数学推理基准无法评估大语言模型在真实工程场景中的不确定性处理与多目标决策能力。EngiBench 通过构建三级难度层级与受控问题变体，系统性地诊断模型在信息提取、领域推理、权衡决策及不确定性处理上的具体短板。该基准揭示了当前模型在开放工程任务上远落后于人类专家，且对输入扰动极度敏感。其价值在于提供了细粒度的能力诊断工具，但受限于专家评分的主观性与样本规模，其结论的普适性仍需进一步验证。

】

---

【MathAgent: Adversarial Evolution of Constraint Graphs for Mathematical Reasoning Data Synthesis ｜MathAgent：基于约束图对抗进化的数学数据合成框架

研究机构：清华大学、哈尔滨工业大学

作者：Zixiong Yu、Jun Rao、Guhan Chen 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.11188)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11188)

> 导读 数学推理数据合成旨在解决高质量人工标注数据稀缺导致的模型能力天花板问题。现有种子扩展法受限于初始语义半径，零样本生成法则因缺乏结构引导而陷入模式崩溃。MathAgent 将数据合成重构为约束图上的无监督优化问题，通过“立法者-执行者”分层架构解耦结构设计与语言实现。该框架在1K样本规模下优于主流开源数据集，但其优势是否源于结构复杂度而非单纯难度提升，仍需更严格的归因分析。

】

---

【MathMixup: Boosting LLM Mathematical Reasoning with Difficulty-Controllable Data Synthesis and Curriculum Learning ｜难度可控数据合成与课程学习

作者：Xuchen Li、Jing Chen、Xuzhao Li 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.17006)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.17006)

> 大语言模型在数学推理上的提升受限于训练数据缺乏显式且可控的难度梯度，导致课程学习无法有效实施。现有合成方法要么仅增加问题复杂度而忽略难度分层，要么生成语义高度相似的变体，无法支撑从易到难的渐进训练。MathMixup通过混合与分解策略生成具有三级难度梯度的数据，并据此实施课程学习，在SFT范式下显著提升了小模型的推理能力。该方法验证了数据难度结构对训练效率的关键作用，但其性能上限仍受限于监督微调范式，未能触及强化学习带来的推理深度突破。

】
