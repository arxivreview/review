# ICLR2026 · AI科学家与自主科学发现方向论文汇编

> 本方向共 4 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AstaBench: Rigorous Benchmarking of AI Agents with a Scientific Research Suite ｜科学代理基准测试的标准化与成本感知评估

研究机构：美国艾伦人工智能研究所、美国亚利桑那大学

作者：Jonathan Bragg、Mike D'Arcy、Nishant Balepur 等 39 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.21652)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.21652)

> 现有AI科学代理评估体系存在工具环境不统一、混淆变量（如算力成本）未控制及接口非标准化等缺陷，导致无法区分代理的真实推理能力与信息源优势。本文通过构建包含生产级搜索工具的统一环境Asta Environment，并引入时间不变的成本核算机制，实现了受控的横向对比。其核心贡献在于确立了“环境-工具-代理-排行榜”的全栈标准化协议，但实验同时揭示了当前代理在端到端科研闭环中全链路成功率极低的事实，表明科学自动化仍远未解决。

】

---

【DeepScientist: Advancing Frontier-Pushing Scientific Findings Progressively ｜目标驱动贝叶斯优化科研系统

研究机构：西湖大学

作者：Yixuan Weng、Minjun Zhu、Qiujie Xie 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.26603)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.26603)

> 自动化科研的核心瓶颈在于缺乏明确目标导致的盲目探索与低效试错。现有端到端系统虽能生成论文，但多陷入对已有知识的简单重组，难以产出具备实质科学价值的突破。DeepScientist 将科研发现形式化为高成本黑盒函数的贝叶斯优化问题，通过分层验证机制平衡探索与利用。该系统在三个前沿任务上超越了人类 SOTA，但其极低的创新成功率揭示了验证过滤才是当前自动科学的新瓶颈。

】

---

【HeurekaBench: A Benchmarking Framework for AI Co-scientist ｜基于代码验证的开放式科学代理基准

研究机构：瑞士洛桑联邦理工学院、瑞士苏黎世联邦理工学院

作者：Siba Smarak Panigrahi、Jovana Videnović、Maria Brbić

论文原文见 [arXiv](https://arxiv.org/abs/2601.01678)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.01678)

> 现有科学代理评估多聚焦于单步计算或事实检索，无法衡量代理在真实科研中自主规划、探索数据并生成新洞察的能力。本文指出，缺乏基于真实实验数据与代码执行验证的开放式问题基准，导致评估结果无法反映代理作为“共同科学家”的实际效用。HEUREKABENCH 通过构建“洞察提取-代码验证-问题生成”的半自动流水线，将已发表的科研成果转化为可复现的开放式研究问题，并引入原子事实分解评估机制。该框架在单细胞生物学实例化后，揭示了当前代理在开放式推理上的显著短板，但其评估依赖 LLM 裁判的稳定性仍存疑。

】

---

【SciNav: A General Agent Framework for Scientific Coding Tasks ｜科学编码智能体：基于相对判断的Top-K树搜索

研究机构：美国俄亥俄州立大学

作者：Tianshu Zhang、Huan Sun

论文原文见 [arXiv](https://arxiv.org/abs/2603.20256)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.20256)

> 科学编码任务要求生成可执行且结果正确的程序，但现有端到端科研智能体多聚焦于假设生成等开放性问题，缺乏针对可验证代码输出的结构化搜索框架。通用智能体如OpenHands依赖逐步执行，而专用框架如AIDE则预设了明确的评估指标，这在真实科研场景中往往不可用。本文提出SciNav，通过引入相对判断（Relative Judgments）引导的Top-K比较树搜索（TKCTS），在受限预算下无需预定义指标即可高效筛选最优代码分支。该框架在ScienceAgentBench上将成功率提升至18.6%，但其在非代码类科学假设评估中的泛化能力仍存疑。

】
