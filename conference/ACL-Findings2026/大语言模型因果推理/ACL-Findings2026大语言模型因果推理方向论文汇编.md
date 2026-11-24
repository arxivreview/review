# ACL-Findings2026 · 大语言模型因果推理方向论文汇编

> 本方向共 8 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【C2DLM: Causal Concept-Guided Diffusion Large Language Models ｜因果概念引导扩散语言模型

研究机构：浙江大学、华为

作者：Kairong Han、Nuanqiao Shan、Ziyu Zhao 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dce2daf01ed5)

> 扩散语言模型（DLM）因丢弃因果顺序而陷入训练低效与推理深度受限的瓶颈，自回归模型（AR）则受限于单向信息流导致的全局结构理解缺失。本文切入点在于识别注意力机制建模先验与自然语言底层因果先验之间的错位，提出C2DLM范式。通过教师模型提取概念级因果图，并利用V-aware Reattention机制在SFT阶段对齐注意力权重，实现因果结构引导。该范式在合成基准上验证了架构改进的有效性，但其对真实世界复杂因果结构的泛化能力仍存疑。

】

---

【Can Post-Training Transform LLMs into Causal Reasoners? ｜后训练能否将大语言模型转化为因果推理器

研究机构：复旦大学、同济大学

作者：Junqi Chen、Sirui Chen、Chaochao Lu

论文原文见 [arXiv](https://arxiv.org/abs/2602.06337)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.06337)

> 因果推理要求模型区分统计关联与真实机制，但大语言模型（LLM）在数值因果估计上常因依赖记忆或表面模式而失效。现有后训练方法虽能提升通用推理能力，却缺乏针对因果结构内化与鲁棒性的系统验证。本文构建CauGym数据集，系统对比五种后训练策略在因果任务上的表现，发现在线强化学习（Online RL）能显著增强模型对因果定理的内化能力。该工作证实了小规模模型经特定训练可超越大规模基线，但其高分是否掩盖了深层结构理解的缺失仍存疑。

】

---

【Causal-Audit: Explicit and Auditable Graph-based Reasoning via Target-Aware Causal Chain Construction ｜目标感知因果图构建与路径审计

研究机构：澳大利亚格里菲斯大学

作者：Su Lan、Xuefei Yin、Yanming Zhu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ef450afdf263)

> 无上下文因果问答要求模型在缺乏外部证据时，判断干预变量对目标变量的方向性影响，这迫使模型依赖内部参数知识而非表面关联。现有链式思维或图思维方法虽能组织推理路径，但缺乏显式因果结构约束，导致推理过程不可审计且易受语义噪声干扰。本文提出一种推理时动态构建目标感知因果图并进行路径级反事实审计的框架，将隐式语言推理转化为显式符号化因果评估。该框架在多个基准上显著提升了方向预测准确率，但其效果依赖于LLM生成因果三元组的初始质量，且未解决模型内部是否真正编码因果方向的根本问题。

】

---

【CausalityCheck: A Framework for Evaluating Causal Reasoning in Large Language Models ｜因果链过程评估框架

作者：Jiang Li、Zehua Duo、Guanglai Gao 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_458b67c2a007)

> 大语言模型在因果推理任务中常出现“答案正确但过程错误”的假阳性，传统仅评估答案准确率的基准无法区分模型是真正理解因果机制还是依赖训练数据记忆。现有基准如CLadder侧重层级测试，但缺乏对推理过程忠实度与抗干扰鲁棒性的细粒度诊断。本文提出CausalityCheck框架，通过构建4×4维度的任务泛化与推理鲁棒性清单，将单一问答扩展为36种变体以量化因果链误识与经验推理依赖。该框架揭示了当前主流模型在过程正确性上的显著短板，但其评估指标是否真正捕捉了因果结构而非仅解释风格，仍需进一步验证。

】

---

【Diagnosing and Mitigating Sycophancy and Skepticism in LLM Causal Judgment ｜递归因果审计（RCA）：诊断LLM因果判断中的输出层偏差

研究机构：美国斯坦福大学

作者：Edward Y. Chang

论文原文见 [arXiv](https://arxiv.org/abs/2601.08258)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.08258)

> 大语言模型（LLM）在因果推理任务中常表现出“因果鹦鹉”现象，即依赖统计模式而非结构推理，导致在干预和反事实层级上性能断崖。现有基准测试多聚焦于最终答案的正确性，却混淆了真实推理能力与拒绝、对冲及压力诱导的漂移，使得难以区分模型是“不知道”还是“不敢说”。本文提出递归因果审计（RCA），一种无金标访问的过程完整性评估器，通过验证模型最终标签是否由其自身推导轨迹所蕴含，来隔离输出层偏差。该框架揭示了“怀疑陷阱”与“规模悖论”，证明推理时验证可显著改善操作点，但其能否真正内化因果结构仍存疑。

】

---

【Generating Effective CoT Traces for Mitigating Causal Hallucination ｜事件因果识别中的因果幻觉缓解

研究机构：加拿大康考迪亚大学

作者：Yiheng Zhao、Jun Yan

论文原文见 [arXiv](https://arxiv.org/abs/2604.12748)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d200380ef242)

> 事件因果识别（Event Causality Identification, ECI）旨在判断文本中两个事件间是否存在真实因果机制，但小参数大语言模型（LLM）常因依赖统计关联而将非因果对误判为因果对，即因果幻觉。现有ECI数据集仅含二元标签，缺乏中间推理步骤，导致微调无法纠正模型的逻辑断裂；而通用思维链（Chain-of-Thought, CoT）准则在ECI任务中失效，无法指导有效训练数据的构建。本文通过实证分析证伪了困惑度选择、短CoT偏好等通用准则，提出基于语义丰富度与分布对齐的CoT生成管线，并引入因果幻觉率（Causal Hallucination Rate, CHR）量化指标。该工作在小模型上显著降低了幻觉率，但其结论是否适用于大模型或结构化因果图任务尚存疑。

】

---

【MDC-Bench: A Multidisciplinary Causal Benchmark Based on Causal Structures for Evaluating Large Language Models ｜多学科因果基准 MDC-Bench

研究机构：哈尔滨工业大学、华为

作者：Peng Wang、Yuxiong Yan、Xiao Ding 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_18840408d140)

> 现有因果评估基准多基于常识领域，模型常通过预训练记忆匹配而非逻辑推导得出答案，导致对深层因果能力的评估失真。MDC-Bench 通过引入 7 个学科的专业论文数据与复杂因果拓扑结构，阻断了知识匹配路径，迫使模型进行真实的因果推理。该基准构建了包含理解、干预、反事实三层级的 8,422 道题目，并引入复合操作增加难度。实验显示，即便最先进的模型在硬模式下准确率仍不足 60%，揭示了当前大语言模型在深层因果理解上的显著局限，但其评估协议中关于因果强度梯度的定义尚存争议。

】

---

【SERE: Structural Example Retrieval for Enhancing LLMs in Event Causality Identification ｜结构感知示例检索增强大语言模型事件因果识别

作者：Zhifeng Hao、Zhongjie Chen、Junhao Lu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.03701)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.03701)

> 事件因果识别（ECI）旨在判定文本中两个事件间是否存在因果关系，但大语言模型（LLM）在此任务上常因过度预测而产生因果幻觉。现有少样本方法依赖语义检索，易被表面词汇误导而忽略深层结构差异，导致推理偏差。SERE框架通过融合概念路径、句法结构与因果模式三种结构信号，检索结构对齐的示例以引导LLM推理。该方法在多个基准上显著提升了F1分数，但其效果高度依赖外部知识图谱的覆盖度与句法解析的准确性，在长尾或复杂语境下的泛化能力仍存疑。

】
