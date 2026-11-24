# ICLR2026 · 文本到SQL生成方向论文汇编

> 本方向共 3 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【BIRD-INTERACT: RE IMAGINING TEXT TO-SQL EVAL UATION VIA LENS OF DYNAMIC INTERACTIONS ｜动态交互文本到SQL基准

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_28598225)

> 现有文本到SQL（Text-to-SQL）评估依赖静态转录或单轮查询，无法捕捉真实场景中歧义消解、执行调试与意图演变的动态过程。本文通过构建包含函数驱动用户模拟器与双评估模式的交互环境，将SQL生成任务转化为多轮协作问题。实验表明前沿大语言模型（LLM）在该基准上成功率极低，揭示了生成能力与交互策略间的巨大鸿沟。该基准填补了动态评估空白，但其低成功率是否完全归因于任务难度而非模拟器偏差，仍需进一步验证。

】

---

【LEARNAT: LEARNING NL2SQL WITH AST-GUIDED - TASK DECOMPOSITION FOR LARGE LANGUAGE MOD ELS ｜AST引导任务分解与边际感知强化学习

研究机构：北京大学、北京邮电大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_10944731)

> 复杂NL2SQL查询的生成瓶颈在于LLM难以将高层语义意图映射为底层数据库结构，现有提示工程路线依赖大模型上下文能力或高成本测试时缩放，而小模型自主分解能力不足导致性能停滞。LearNAT通过AST引导的可验证分解数据合成与边际感知强化学习，将分解能力内化至小模型参数中。该方法在7B参数规模下实现了接近GPT-4的跨域性能，但其AST静态验证机制在复杂语义歧义场景下的泛化边界尚存疑。

】

---

【SpotIt: Evaluating Text-to-SQL Evaluation with Formal Verification ｜基于形式化验证的Text-to-SQL评估

研究机构：加拿大西蒙弗雷泽大学

作者：Rocky Klopfenstein、Yang He、Andrew Tremante 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.26840)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.26840)

> 当前Text-to-SQL领域依赖静态测试库比对执行结果来判定模型正确性，这种测试式评估存在系统性假阳性，导致SOTA方法的真实性能被高估。本文切入点在于将评估从“单点测试”升级为“反例搜索”，利用SMT有界等价验证主动构造能区分生成SQL与金标准SQL的数据库实例。通过扩展VERIEQL引擎支持字符串与日期操作，SPOTIT在BIRD基准上揭示了现有方法准确率被高估11.3%–14.2%的事实。该工作挑战了执行准确率（EX）作为唯一金标准的共识，但其有界验证的计算开销与对标注质量的依赖仍构成应用边界。

】
