# ACL-Findings2026最新论文 ｜Automatic Paper Analysis and Categorisation for Systematic Reviews with Combined Reasoning-Augmented SFT and DAPO RL ｜低资源科学论文结构化标注：推理增强SFT与DAPO强化学习

作者：Michela Lorandi、Anya Belz、Simon Mille 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b652a2a95557)

> 系统性综述（Systematic Review）的核心瓶颈在于人工标注论文分类标签的高昂成本与时效性滞后。现有大语言模型（LLM）直接生成结构化标签时，常因缺乏逻辑推理过程导致多标签预测错误及格式合规性差，且单纯监督微调（SFT）难以捕捉字段间的依赖关系。本文切入点在于将标注任务重构为推理增强分类问题，通过合成推理轨迹进行SFT，并引入动态采样策略优化（Dynamic sAmpling Policy Optimisation, DAPO）强化学习以优化奖励信号。该方法在100样本低资源约束下显著提升了标注准确率，但受限于仅评估开源模型且未对比检索增强生成（RAG）基线，其结论在闭源模型及长文本场景下的泛化性存疑。

## 研究背景

系统性综述要求对海量文献进行多维度分类，传统人工标注耗时且易过时。大语言模型（LLM）虽能生成文本，但在处理结构化输出（如JSON格式的多标签分类）时，直接预测往往缺乏对证据的显式引用，导致逻辑链条断裂。为解决此问题，监督微调（Supervised Fine-Tuning, SFT）成为主流，但标准SFT仅优化最终标签，忽略了中间推理过程，导致模型在复杂多标签任务上表现不稳定。此外，强化学习（Reinforcement Learning, RL）在结构化预测中的应用尚处于早期，传统组相对策略优化（Group Relative Policy Optimisation, GRPO）在处理长思维链（Chain-of-Thought, CoT）时易出现熵坍缩，限制了其在低资源标注任务中的潜力。

该领域长期面临“数据效率”与“标注精度”的矛盾。现有自动化标注方法多依赖大规模预训练数据或检索增强生成（Retrieval-Augmented Generation, RAG），但在低资源场景下，RAG的检索噪声可能干扰分类判断，而纯SFT难以利用少量样本挖掘字段间依赖。本文针对此瓶颈，提出一种方案无关（Scheme-agnostic）的标注框架，通过合成推理轨迹增强SFT，并采用DAPO算法解决长CoT RL中的训练不稳定问题，旨在以极少样本实现高精度结构化标注。

## 核心方法

### 方法参照系

本文任务属于低资源结构化分类，标准流程为“输入文本-直接预测标签”。关键差异在于：本文不直接预测标签，而是先生成包含证据引用的推理轨迹（Reasoning Trace），再输出JSON标签，并将此过程纳入SFT与RL联合优化框架。

### 推理增强SFT与合成轨迹生成

标准SFT仅训练模型输出标签，缺乏对“为何选择该标签”的逻辑约束，导致多标签预测中部分正确但整体错误。本文在SFT阶段引入合成推理轨迹，利用LLaMA 3.3 70B Instruct生成解释性文本，强制模型在输出标签前引用论文证据。训练目标为最大化条件概率：

$$ L_{SFT}(\theta) = -\sum_{t=1}^{T} \log p_\theta(y_t | y_{<t}, x, q) $$

其中 $y_t$ 包含推理轨迹 $r$ 和结构化标签 $a$。此设计使模型学习“证据-标签”映射，而非仅记忆表面特征，显著提升了多标签字段（如Control Attributes）的精确匹配率。

### DAPO强化学习优化

SFT后模型仍可能在格式合规性与标签准确性间权衡不足。传统GRPO在长CoT中因奖励稀疏导致策略熵坍缩。本文采用DAPO，通过动态采样与Clip-Higher策略维持探索多样性，并设计复合奖励函数：

$$ R = w_{correct}R_{correct} + w_{format}R_{format} + w_{json}R_{json} $$

其中 $R_{correct}$ 基于精确匹配（EM）或Jaccard相似度，$w_{correct}=0.7$ 优先保证准确性。DAPO的Token级策略梯度损失：

$$ L_{DAPO}(\theta) = -\sum_{i=1}^{G} \frac{1}{|o_i|} \sum_{t=1}^{|o_i|} \hat{A}_{i,t} \log \frac{\pi_\theta(o_{i,t}|q, o_{i,<t})}{\pi_{old}(o_{i,t}|q, o_{i,<t})} $$

通过组内相对优势 $\hat{A}_{i,t}$ 平衡长序列奖励，避免早期token主导梯度，从而在保持推理长度的同时提升格式合规性。

## 实验评估

实验基于ACL Anthology中140篇CTG论文，其中99篇用于训练，29篇用于测试。基线包括Qwen3（8B/14B/32B）与LLaMA 3.1/3.3（8B/70B）的零样本推理。本文方法在CTG Control Type上达到84.1%准确率，超越最强基线LLaMA 3.3 70B（74.5%）10.6个百分点；在QCET Level 3层级分类中，SFT+RL实现33.3%精确匹配，而所有预训练模型均为0.0%。

| 模型 | Control Type Acc | Control Attributes EM | Control Implementation EM | QCET Level 3 EM |
|---|---|---|---|---|
| LLaMA 3.3 70B (Zero-shot) | 74.5 | 47.6 | 62.9 | 0.0 |
| Qwen3 8B SFT only | 71.7 | 32.4 | 40.0 | 21.3 |
| Qwen3 8B SFT+RL | 84.1 | 34.5 | 46.2 | 33.3 |

消融实验显示，推理增强SFT相比非推理SFT在Control Attributes上提升9.0点EM，验证了显式推理对多标签任务的增益。RL阶段将Control Type准确率从71.7%提升至84.1%，同时推理长度从656 tokens缩短至563 tokens，表明DAPO有效抑制了冗余推理。然而，RL单独训练（无SFT）效果不及SFT+RL，证明SFT提供的初始策略对RL收敛至关重要。

评估边界方面，测试集仅29篇论文，样本量较小可能导致统计波动。指标采用严格字符串匹配，未进行语义归一化，可能低估模型在开放词汇字段（如Control Attributes）上的实际能力。代码与数据已开源，但训练依赖3块NVIDIA A100 GPU，复现成本较高。

## 关联研究分析

从问题动机看，本文与AutoSurvey等综述生成方法不同，后者侧重内容合成，本文聚焦元数据提取。AutoSurvey依赖RAG处理长文本，而本文因资源限制采用全量输入（平均9k tokens），这暗示在短文本标注任务中，RAG的检索噪声可能不如直接上下文有效，但论文未提供RAG基线对比，无法确认此结论在长文本场景的普适性。

从方法设计看，本文与DeepReview共享RL优化逻辑，但DeepReview针对评审深度，本文针对标注精度。DeepReview使用标准PPO，本文采用DAPO以解决长CoT中的熵坍缩，这一选择源于标注任务输出长度可变且结构复杂，传统PPO的奖励稀疏问题更为突出。然而，本文未对比GRPO，DAPO相对于GRPO的具体增益幅度缺乏直接证据，仅通过性能提升间接推断。

## 总结

本文解决的核心矛盾是低资源约束下结构化标注的精度与效率平衡。切入点在于将标注重构为推理增强分类，通过合成轨迹提供密集监督信号，并利用DAPO优化长CoT训练稳定性。方法证明在100样本下，SFT+RL可将Control Type准确率提升至84.1%，QCET Level 3精确匹配达33.3%。边界在于仅评估开源模型，且未对比RAG基线，无法排除检索增强在更大规模数据下的潜在优势。当支持集扩大至数千篇时，合成推理轨迹的边际收益是否递减，以及DAPO相对于标准PPO的效率优势是否依然显著，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_b652a2a95557)