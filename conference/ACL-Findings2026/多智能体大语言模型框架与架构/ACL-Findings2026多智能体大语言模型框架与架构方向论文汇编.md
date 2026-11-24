# ACL-Findings2026 · 多智能体大语言模型框架与架构方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Learning Optimal Message Representations for Agentic Communication ｜动态学习最优消息表示的多智能体通信系统

研究机构：微软研究院

作者：Shashwat Gupta、Anson Bastos、Mayukh Das 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4b83a079407a)

> 多智能体协作中，自然语言（NL）作为默认通信介质存在歧义与冗余，导致推理偏差在智能体间级联放大。现有方案依赖静态格式或大语言模型（LLM）先验选择结构，无法适应动态任务分布。本文提出OPTiMACS，将消息格式选择建模为扩展马尔可夫决策过程（EMDP），通过强化学习从环境反馈中动态发现并优化最优表示。该方法在多个基准上提升了任务准确率并降低了Token消耗，但其增益是否源于格式本身而非骨干模型能力，仍需更严格的控制实验验证。

】

---

【Self-Evolving Multi-Agent Systems via Textual Backpropagation ｜智能体神经网络

研究机构：德国慕尼黑大学、德国慕尼黑工业大学

作者：Xiaowen Ma、Yunpu Ma、Chenyang Lin 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8741773b9ffa)

> 多智能体大语言模型框架（Multi-Agent LLM Frameworks）旨在通过结构化协作突破单一模型在长程任务中的推理瓶颈，但现有方案多依赖静态手动编排，难以适应动态任务且协调开销随规模非线性增长。本文切入点在于将经典神经网络的层级化反向传播机制迁移至智能体协作，以文本梯度替代数值梯度实现拓扑与提示的联合优化。具体做法是构建前向动态团队选择与后向工作流优化双阶段流程，在训练阶段学习可复用的智能体团队池，推理阶段冻结架构仅执行前向传播。该框架在多个基准上超越了静态基线，但其性能增益是否源于架构优化还是强骨干模型的固有优势，仍存疑。

】

---

【Single-Agent Generation Surpasses Multi-Agent Systems in Semantic Diversity ｜解耦提示与架构：单智能体多输出在语义多样性上的优势

作者：Encheng Cui、Shaowen Peng、Kazuhiro Ito 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_78737bc03f87)

> 导读 多智能体系统（MAS）常被用于提升大语言模型（LLM）的推理多样性，但现有研究往往将提示工程与架构设计混淆，导致增益来源不明。本文通过控制变量实验，在匹配提示条件与输出量的前提下，发现单智能体多输出（SI-MO）在语义多样性上优于串行与并行MAS。该研究通过解耦实例拓扑与输出多重性，揭示了信息可见性对生成多样性的关键作用。这一发现挑战了“多智能体即增效”的直觉，但受限于发散思维任务，其在通用推理任务中的普适性仍存疑。

】
