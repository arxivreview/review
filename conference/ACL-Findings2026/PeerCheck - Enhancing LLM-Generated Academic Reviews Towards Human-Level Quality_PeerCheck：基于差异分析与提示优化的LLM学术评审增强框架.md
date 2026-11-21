# ACL-Findings2026最新论文 ｜PeerCheck: Enhancing LLM-Generated Academic Reviews Towards Human-Level Quality ｜PeerCheck：基于差异分析与提示优化的LLM学术评审增强框架

作者：Zeyuan Chen、Ziqing Yang、Yihan Ma 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.20897)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.20897)

> 导读
> 学术出版量激增导致同行评审系统面临人力瓶颈，而大语言模型（LLM）生成的评审意见常因缺乏方法论深度和存在系统性偏见，难以达到人类专家标准。现有方法多依赖端到端生成或简单检索增强，但未能解决LLM评审在评分分布、关键词偏好及可检测性上与人类评审的结构性错位。PeerCheck框架通过对比人类与LLM评审的差异，设计包含思维链（Chain-of-Thought, CoT）和检索增强生成（Retrieval-Augmented Generation, RAG）的迭代提示工程，旨在提升评审的人类相似度并降低机器生成痕迹。该框架揭示了RAG对部分模型性能产生负迁移的“RAG悖论”，其价值在于提供了量化LLM评审与人类对齐程度的实验证据，但将“低可检测性”作为质量指标是否混淆了学术严谨性与文本伪装，仍存疑。

## 研究背景

当LLM被用于生成学术评审时，其输出文本在统计特征上与人类写作存在显著差异，这种差异不仅体现在语言风格上，更反映在评估逻辑的偏差中。这种偏差导致LLM生成的评审容易被检测器识别，且其评分往往偏离人类专家的标准，例如对弱论文的评分过高或对特定修辞风格过度敏感。解决这一问题的关键在于理解人类评审与LLM评审在语义空间中的具体错位，并据此调整LLM的生成策略，使其在保持逻辑一致性的同时，更贴近人类专家的评估范式。

同行评审自动化领域的主流路线包括基于监督微调（Supervised Fine-Tuning, SFT）的深度模型和多智能体协作系统。SFT方法如DeepReview通过强化学习将复杂推理内化，但在标准化基准上表现稳定却缺乏对实时文献的适应性；多智能体系统如ScholarPeer通过角色分工提升深度，但计算成本高且推理过程不透明。这些方法大多假设“更多信息或更强推理即更好”，却忽视了LLM模型架构差异对检索增强效果的异质性影响。PeerCheck的切入点在于，不改变模型权重，而是通过精细化的提示工程，针对特定LLM的弱点进行定向优化，从而在低成本下实现评审质量的提升。

## 核心方法

### 方法参照系

本文问题归属于同行评审自动化中的提示工程与检索增强路线。与端到端生成或微调方法不同，PeerCheck的核心差异在于其“分析-优化-验证”的闭环流程，将人类评审作为外部知识源和评估基准，而非仅作为训练数据。

### 差异驱动提示工程

传统提示工程通常采用静态模板，缺乏对LLM与人类评审差异的针对性修正。PeerCheck首先通过关键词、评分分布和主题分析，量化LLM与人类评审的错位。例如，LLM倾向于关注“理论”而忽视“实验”，评分分布更分散且对拒稿论文评分偏高。基于此，PeerCheck设计了包含三个反思阶段的CoT提示模板：

$$
\text{Review} = f_{\text{CoT}}(\text{Paper}, \text{Persona}, \text{Keywords}_{\text{Human}})
$$

其中，$f_{\text{CoT}}$ 表示包含“思考-写作-评分”三阶段的生成函数，$\text{Keywords}_{\text{Human}}$ 为从高质量人类评审中提取的关键词。该设计动机在于，通过强制LLM在生成前进行结构化反思，并注入人类评审的语言特征，弥补LLM在方法论细节关注上的不足。

### RAG增强与模型特异性

在提示工程基础上，PeerCheck引入RAG，从1,920篇非检测论文的人类评审中检索相关片段，作为外部知识注入生成过程：

$$
\text{Review}_{\text{RAG}} = f_{\text{LLM}}(\text{Paper}, \text{Prompt}, \text{Retrieved}_{\text{Human}})
$$

其中，$\text{Retrieved}_{\text{Human}}$ 为检索到的人类评审片段。这一设计的动机在于，通过提供真实的人类评审范例，引导LLM生成更符合学术规范的反馈。然而，实验发现RAG对GPT-4o性能提升显著，但对Claude-3.7-Sonnet产生负迁移，揭示了检索源与模型训练分布不匹配的问题。

## 实验评估

实验基于ICLR 2024/2025和NeurIPS 2024的1,920篇论文进行分析，480篇论文用于验证。基线包括GPT-4o、Claude-3.7-Sonnet和DeepSeek-V3的Normal、Revised、RAG版本，但未对比SFT或RL微调方法如DeepReview。

| 模型 | 指标 | Normal | Revised | RAG+Revised |
|---|---|---|---|---|
| GPT-4o | Cosine | 0.379 | 0.518 | 0.645 |
| Claude-3.7-Sonnet | Cosine | 0.431 | 0.688 | 0.630 |
| DeepSeek-V3 | Cosine | 0.407 | 0.620 | 0.641 |

GPT-4o的Cosine相似度从0.379提升至0.645，表明RAG与Revised提示的组合效果最佳；Claude-3.7-Sonnet在Revised提示下达到0.688，但RAG导致其性能下降至0.630，验证了“RAG悖论”。

消融实验显示，CoT提示显著降低了RoBERTa检测率40.3%，但RAG对检测率的影响因模型而异。GPT-4o的LRR检测率从0.801降至0.593，而Claude-3.7-Sonnet的检测率变化较小。这一反直觉发现表明，RAG并非普遍有效，其效果取决于模型对检索信息的利用能力。

评估边界方面，本文使用BLEU、ROUGE、Cosine和RoBERTa F1作为指标，但未报告置信区间或计算效率。代码已开源，但超参数细节有限，可复现性受限于LLM API的版本稳定性。

## 关联研究分析

从问题动机看，PeerCheck与Reviewer2同属多阶段评审生成，但Reviewer2侧重流水线标注，而PeerCheck聚焦于提示优化。Reviewer2通过PGE流水线提升评审覆盖度，但缺乏对LLM与人类差异的细粒度分析；PeerCheck通过差异驱动提示工程，更直接地解决评分偏差问题。这一差异源于任务特性：Reviewer2面向大规模数据集标注，而PeerCheck面向单篇论文的深度评审，前者更关注效率，后者更关注质量。

从方法设计看，PeerCheck与CiteGuard均关注内容真实性，但CiteGuard侧重引用验证，PeerCheck侧重整体评审风格对齐。CiteGuard通过检索增强验证降低幻觉引用率，而PeerCheck通过RAG提升评审的人类相似度。这一差异反映了学术评审的不同维度：CiteGuard解决“引用是否真实”，PeerCheck解决“评审是否像人类”。查询侧增强在数据充足时是否仍有增益，论文未给出回答，但RAG悖论暗示，检索源的质量与模型匹配度是关键。

## 总结

PeerCheck旨在解决LLM评审与人类专家标准之间的结构性错位，通过差异分析与提示优化实现低成本的质量提升。其核心贡献在于揭示了RAG对模型性能的异质性影响，证明了CoT提示在降低可检测性方面的有效性。实验表明，GPT-4o的Cosine相似度从0.379提升至0.645，RoBERTa检测率降低40.3%。然而，本文的边界在于将“低可检测性”作为质量指标，可能混淆了学术严谨性与文本伪装；且未对比SFT或RL微调方法，无法证明提示工程优于深度学习方法。当检索源与模型训练分布不匹配时，RAG的负迁移是否可通过动态检索策略缓解，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.20897)