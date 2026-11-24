# ACL-Findings2026 · 大型语言模型中的后门攻击与防御方向论文汇编

> 本方向共 6 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【ATAAT: Adaptive Threat-Aware Adversarial Tuning Framework against Backdoor Attacks on Vision-Language-Action Models ｜视觉-语言-动作模型后门攻击中的梯度干扰与优化去冲突

研究机构：中国科学院、中国科学院大学

作者：Kewei Chen、Yayu Long、Shuai Li 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.08612)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_17792f2053db)

> 具身智能模型在供应链环节面临训练时后门植入风险，传统攻击范式因良性指令与恶意动作的优化目标冲突而失效。ATAAT 框架通过构建正交优化子空间解决这一“梯度干扰”问题，分别在数据投毒与模型微调场景下实现隐式与显式去冲突。该工作填补了受限访问条件下 VLA 模型后门攻击的空白，但其对休眠神经元假设的依赖及物理世界泛化性仍存疑。

】

---

【BackdoorAgent: A Unified Framework for Backdoor Attacks on LLM-based Agents ｜智能体工作流后门传播分析框架

研究机构：复旦大学、新加坡管理大学

作者：Yunhao Feng、Yige Li、Yutao Wu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.04566)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.04566)

> 大语言模型智能体通过规划、记忆与工具调用执行多步任务，其状态持久化特性使得单点注入的触发器可跨阶段传播，但现有研究多在孤立模块下评估，无法刻画这种工作流级的动态风险。本文提出 BackdoorAgent，一个阶段感知的统一框架，通过组件局部扰动与轨迹日志，系统量化了触发器在规划、记忆、工具三个阶段的激活与传播机制。该工作填补了智能体后门从静态注入到动态演化的分析空白，但其仅聚焦攻击表征，未提供防御算法，且评估依赖特定任务验证器，泛化性存疑。

】

---

【DiSec: Mitigating Backdoors in Pre-trained Language Models via Disentanglement of Adversarial Weights for Secure Fine-Tuning ｜预训练语言模型后门净化：基于梯度残差解耦的权重修正

研究机构：美国阿肯色大学

作者：Sunanda Das、Qinghua Li

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fd850f9bb64f)

> 预训练语言模型（Pre-trained Language Models, PLMs）在供应链分发中面临任务无关后门威胁，即攻击者在预训练阶段植入触发器，导致模型在下游微调后仍保留恶意行为。现有防御方法多依赖下游标签或干净参考模型，无法在真实部署场景中独立净化被污染的预训练检查点。DiSec 利用无标签辅助文本计算梯度残差，通过奇异值分解（SVD）与变分自编码器（VAE）联合检测异常权重行，并采用层内原型均值修正替代剪枝，在无需下游监督的情况下抑制攻击成功率。该方法在 BERT 和 RoBERTa 上实现了效用保持与攻击抑制的平衡，但其对非线性复杂后门结构的鲁棒性及在生成式大语言模型上的泛化能力仍存疑。

】

---

【P2P: A Poison-to-Poison Remedy for Reliable Backdoor Defense in LLMs ｜以良性后门覆盖恶意后门：P2P 防御框架

研究机构：新加坡南洋理工大学、上海交通大学

作者：Shuai Zhao、Xinyi Wu、Shiqian Zhao 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.04503)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.04503)

> 微调阶段的数据投毒后门攻击使大语言模型在特定触发器下输出恶意内容，而现有防御方法往往局限于特定任务或攻击类型，缺乏跨场景泛化能力。P2P 算法通过向训练集注入带有安全标签的良性触发器，利用提示学习将模型输出空间重定向至安全标签，从而在无需知道恶意触发器具体形态的前提下抑制其激活。该方法在分类与生成任务上均实现了攻击成功率（Attack Success Rate, ASR）的显著降低，但其对生成任务输出多样性的潜在影响及良性触发器设计的依赖性仍存疑。

】

---

【Rethinking Reasoning: A Survey on Reasoning-based Backdoors in LLMs ｜推理级后门攻击的认知分类学

研究机构：新加坡南洋理工大学

作者：Man Hu、Xinyi Wu、Zuofeng Suo 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.07697)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.07697)

> 大语言模型（Large Language Models, LLMs）的推理能力在提升任务性能的同时，引入了针对思维链（Chain-of-Thought, CoT）中间步骤的隐蔽攻击面，现有综述多孤立讨论后门或推理安全，缺乏针对“推理劫持”机制的系统性框架。本文切入点在于区分攻击对模型认知过程的不同操纵方式，而非仅关注输入输出映射。通过构建关联式、被动式与主动式三类认知中心分类法，论文梳理了从触发器植入到推理路径污染的完整攻击谱系。该分类法填补了推理级后门机制研究的空白，但作为纯综述工作，其价值取决于分类维度的完备性，且未提供量化防御对比数据，分类边界在连续潜在推理等新架构下的适用性存疑。

】

---

【SAFER: A Controllable Safeguard for LLMs against Backdoor Attacks ｜统计保障的推理时后门防御

研究机构：新加坡南洋理工大学

作者：Zirui Hu、Zheng Zhang、Yingjie Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_67768403d2df)

> 大语言模型在金融、医疗等高利害场景中部署时，推理时后门防御面临的核心矛盾是：现有评分函数虽能区分干净与投毒样本，但缺乏对假接受率（False Acceptance Rate, FAR）的显式统计控制，导致安全阈值无法量化。本文切入点在于，将后门检测重构为多重假设检验问题，通过估计样本为干净的局部似然概率，求解约束优化问题以在满足用户指定FAR阈值的同时最大化干净样本接受率。该方法无需已知后门样本校准，仅依赖干净校准集与混合测试集。其价值在于提供了渐近FAR保证，但实验仅覆盖词法触发器，对语义级攻击的鲁棒性存疑。

】
