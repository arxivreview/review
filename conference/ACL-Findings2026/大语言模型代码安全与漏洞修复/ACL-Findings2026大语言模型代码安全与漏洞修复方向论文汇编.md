# ACL-Findings2026 · 大语言模型代码安全与漏洞修复方向论文汇编

> 本方向共 8 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AutoSUIT Bench - Automated Security UnIt Test Benchmark for LLM Coding ｜自动化安全单元测试基准

研究机构：美国马萨诸塞大学阿默斯特分校

作者：Samuel Osebe、Fan Yang、Junyi Li 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d44dd828310a)

> 大语言模型生成的代码普遍存在安全漏洞，但现有评估手段要么依赖静态分析导致高误报，要么依赖人工编写动态测试导致覆盖不足。AutoSUIT 通过 LLM 自动化生成代码、测试及修复代码，并嵌入迭代验证闭环，解决了动态基准扩展性瓶颈。该范式实现了 232 类 CWE 的细粒度评估，但缺乏与主流安全对齐方法的直接性能对比，其作为评估工具的区分度尚待验证。

】

---

【Learning from Failures: Error Notebook-guided Secure Code Generation ｜错误笔记引导的安全代码生成

研究机构：中南大学

作者：Xinyu Zhong、Peng Lan、Zhifang Liao

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_968c13d1a977)

> 大语言模型（LLM）在生成代码时面临功能正确性与安全性的内在冲突，现有检索增强生成（RAG）方法仅注入静态安全指南，缺乏对模型自身历史失败经验的动态利用，导致在未见过的漏洞类型上泛化能力不足。SAFENOTE 通过构建安全与功能双维度的错误笔记，将模型的历史失败转化为对比性指导，在不重新训练模型的前提下提升安全性。该方法在 GPT-4o-mini 上将 CodeGuard+ 基准的 SecurePass@1 从 60.21% 提升至 66.70%，但其在部分开源模型上的功能性能出现显著退化，暴露了经验积累机制对模型基线能力的依赖。

】

---

【MultiCodeAttack: Iterative Jailbreak Attacking on LLMs with Multi-Code Prompt Injection ｜多语言代码模板越狱攻击

作者：Weifeng Sun、Meng Yan、Zhou Yang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_83217a6cfeee)

> 现有结构化越狱方法依赖单一编程语言和静态模板，导致攻击面受限且易被防御机制识别。本文指出不同编程语言对同一模型的安全对齐强度存在显著差异，且静态模板缺乏适应性。MultiCodeAttack 通过多臂老虎机动态选择语言，结合语义保持变异与响应感知反馈，实现了跨语言的迭代优化攻击。该方法在恶意代码生成任务上取得了 92.51% 的攻击成功率，但其在推理增强模型上的鲁棒性验证仍显单薄。

】

---

【SynthFix: Adaptive Neuro-Symbolic Code Vulnerability Repair ｜自适应神经符号漏洞修复框架

研究机构：美国范德堡大学、美国芝加哥大学

作者：Yifan Zhang、Jieyu Li、Kexin Pei 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17184)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17184)

> 自动化代码修复面临的核心矛盾是：监督微调（SFT）能高效学习常见语法模式但缺乏深层语义推理，而奖励微调（RFT）能处理复杂语义但计算成本高昂且收敛缓慢。现有方法通常固定选择单一训练策略或采用静态混合比例，无法根据代码复杂度动态调整，导致简单漏洞浪费算力或复杂漏洞修复不足。SYNTHFIX 通过引入基于编译器特征的自适应路由器，在训练阶段动态调度 SFT 与 RFT 路径，并结合 AST、CFG 和 Semgrep 构建密集符号奖励信号。该框架在 FixJS 和 CodeFlaws 基准上实现了 CodeBLEU 最高 18% 的相对提升，但评估局限于静态代码特征，未验证运行时动态语义下的泛化能力。

】

---

【Train in Vain: Functionality-Preserving Poisoning to Prevent Unauthorized Use of Code Datasets ｜功能性保持的代码数据集投毒

作者：Yuan Xiao、Jiaming Wang、Yuchen Chen 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.22291)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e595236c6d67)

> 代码大语言模型（CodeLLMs）的预训练依赖海量公开代码，但数据所有者缺乏阻止未授权微调的技术手段。现有投毒方法如 CoProtector 通过破坏语法或语义来降低模型效用，导致代码无法编译或功能失效，无法在真实发布场景中部署。本文提出 FUNPOISON，通过向执行路径注入可编译、无副作用的弱用代码片段，在保持 100% 功能正确性的前提下，仅污染 10% 数据集即可显著抑制未授权微调收益。该方法在隐蔽性和鲁棒性上优于基线，但其对语义级异常检测的抵抗能力及跨语言泛化性仍存疑。

】

---

【Understanding Secret Leakage Risks in Code LLMs: A Tokenization Perspective ｜代码大语言模型中的乱码偏差：分词器视角下的秘密泄露风险

研究机构：香港中文大学、新加坡南洋理工大学

作者：Meifang Chen、Zhe Yang、Huang Nianchen 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17814)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17814)

> 代码大语言模型（Code LLMs, CLLMs）在自动化软件开发中广泛部署，但其训练语料中混杂的API密钥等敏感信息构成了严重的隐私泄露隐患。现有安全对齐与漏洞修复方法聚焦于生成代码的功能正确性与漏洞消除，却忽视了底层分词器对高熵随机字符串的结构性处理缺陷。本文通过信息论视角揭示Byte-Pair Encoding（BPE）分词器将高字符熵秘密转化为低Token熵序列的“乱码偏差”（Gibberish Bias），并论证该偏差加剧了模型对秘密的记忆与泄露风险。该发现将LLM安全研究的边界从模型权重与提示工程延伸至输入预处理架构，但缺乏对缓解策略的量化验证。

】

---

【Watch Out Your Industrial Copilots: Stealthy Backdoor Attack Against LLM-Based PLC Code Generation ｜面向LLM生成PLC代码的隐蔽后门攻击框架

作者：Xinyuan An、Liu Xiaoxia、Dongxia Wang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_49dfe324e63a)

> 工业控制领域正引入大语言模型（LLM）自动生成PLC代码，但这一趋势引入了供应链层面的新型攻击面。现有针对通用代码的后门攻击依赖显性关键词触发，在PLC严格的实时与功能约束下极易被静态分析拦截，且无法造成物理危害。STBack通过设计适配PLC逻辑的六类恶意注入模式与语义集成触发器，构建了隐蔽性精炼流水线。该框架证明了在通过常规安全验证的前提下，LLM生成的PLC代码可被植入导致物理灾难的后门，揭示了现有防御机制在逻辑恶意代码检测上的盲区。

】

---

【中大南洋理工阿里联合发布RealSec-bench：基于真实Java仓库评估LLM安全代码生成，揭示跨过程漏洞短板

研究机构：中山大学、新加坡南洋理工大学

作者：Yanlin Wang、Ziyao Zhang、Chong Wang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_217605fc06c1)

> 现有安全代码生成基准多依赖合成片段或孤立函数，无法捕捉真实软件中跨过程数据流引发的漏洞，导致对模型安全能力的评估存在系统性高估。本文切入点在于构建基于真实高风险 Java 仓库的基准，通过 SAST 筛选与多 LLM 裁决机制解决静态分析高误报与上下文缺失的双重难题。其核心做法是构建包含 105 个实例的 RealSec-bench，并引入联合指标 SecurePass@k 同时评估功能与安全性。该基准揭示了当前主流 LLM 在仓库级安全生成上的显著短板，但其仅覆盖 Java 语言且实例规模有限，跨语言泛化性存疑。

】
