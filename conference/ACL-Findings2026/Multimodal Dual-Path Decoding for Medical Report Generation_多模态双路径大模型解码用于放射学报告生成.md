# ACL-Findings2026最新论文 ｜Multimodal Dual-Path Decoding for Medical Report Generation ｜多模态双路径大模型解码用于放射学报告生成

研究机构：厦门大学、北京大学

作者：Jinghan Sun、Dong Wei、Zhihong Zhu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a6f825379f32)

> 放射学报告生成（RRG）旨在从医学图像自动产生结构化临床文本，其核心价值在于缓解影像检查量激增与放射科医生短缺之间的结构性矛盾。现有方法多依赖大型视觉语言模型（LVLM）或大型语言模型（LLM）单一路径，前者视觉接地强但缺乏细粒度临床知识，后者语义丰富但易产生幻觉。本文提出在解码阶段对LVLM与LLM进行token级概率加权融合，并引入多标签分类提示以增强LLM的临床约束。该框架在MIMIC-CXR上提升了临床实体指标，但缺乏对融合权重动态调整机制的探索，且未解决3D体积数据的空间连续性难题。

## 研究背景

放射学报告生成（Radiology Report Generation, RRG）的核心挑战在于视觉证据与临床语义的严格对齐。大型视觉语言模型（Large Vision-Language Models, LVLMs）通过端到端预训练实现了图像-文本联合处理，但其通用语言能力强于专业医学知识编码，导致生成报告常缺乏细粒度病理描述。大型语言模型（Large Language Models, LLMs）虽具备丰富的医学先验知识，但缺乏直接视觉输入，易产生与图像不符的幻觉文本。

传统编码器-解码器架构受限于数据标注成本，而单一LVLM或LLM路径均存在固有缺陷：LVLM在临床准确性上落后于传统Transformer方法，LLM则无法直接提取视觉证据。现有集成方法多聚焦于多个LLM的组合，忽视了视觉模态与语言模态在解码阶段的动态互补性。本文切入点在于利用LVLM的视觉接地能力与LLM的临床推理能力，在推理时通过概率融合实现双路径协同，以克服单模型在事实一致性与语义完整性上的局限。

## 核心方法

### 方法参照系

本文问题属于多模态报告生成中的模型集成范畴。标准流程为独立训练LVLM与LLM后，在推理时进行输出级或权重级集成。本文关键差异在于摒弃了传统的输出聚合或参数插值，转而采用解码阶段的token级概率加权融合，并引入多标签分类结果作为LLM的显式结构化提示，以解决单模型在视觉证据提取与临床知识注入上的互补性缺失。

### 结构化提示与双路径训练

设计动机在于解决LVLM生成报告召回率低及LLM缺乏视觉约束的问题。本文构建了三部分生成目标：Impression（诊断印象）、Disease（疾病类别）和Findings（影像发现）。对于LVLM，采用标准交叉熵损失进行指令微调，使其学习从图像中提取结构化报告：

$$ \mathcal{L}_V = -\sum_{m=1}^{M} \log p_{\theta_V}(r_m | x, P_V, r_{<m}; \theta_V) $$

其中 $P_V$ 为包含图像占位符及格式约束的提示。对于LLM，引入PromptMRG提供的18类多标签分类结果（positive, negative, uncertain, not mentioned）构建提示 $P_L$，训练其生成符合临床逻辑的报告：

$$ \mathcal{L}_L = -\sum_{m=1}^{M} \log p_{\theta_L}(r_m | x, P_L, r_{<m}; \theta_L) $$

该设计通过显式注入疾病状态信息，弥补了LLM在视觉证据缺失下的知识盲区，同时LVLM的训练目标扩展至疾病类别列表，提升了召回率。

### Token级概率融合解码

设计动机在于解决单模型解码时的信息损失与语义对齐不足。在推理阶段，对于每个解码步 $m$，LVLM与LLM独立计算词汇表 $V$ 上的概率分布。本文提出加权平均融合策略，由超参数 $\alpha \in [0, 1]$ 控制：

$$ p_{fusion} = \alpha \cdot p_{\theta_V}(V | X, P_V, r_{<m}; \theta_V) + (1 - \alpha) \cdot p_{\theta_L}(V | X, P_L, r_{<m}; \theta_L) $$

下一token $r^*_m$ 通过 $\arg\max p_{fusion}$ 选取。该机制允许模型在生成过程中动态平衡视觉证据（LVLM）与临床知识（LLM），避免了简单输出集成中共享模式利用不足的问题，实现了细粒度的多模态协同。

## 实验评估

实验基于MIMIC-CXR（270,790训练样本）和IU-Xray数据集，评估指标包括临床效率（CE，基于CheXbert）、临床语义完整性（CSI，基于RadGraph）及自然语言生成（NLG）指标。基线覆盖Transformer方法（PromptMRG）、LVLM方法（MLRG, Qwen2-VL）及LLM方法。本文方法在CE指标上取得最高Precision（0.591）和F1（0.527），较SOTA Transformer方法PromptMRG提升0.051 F1，较最佳LVLM方法MLRG提升0.022 F1。

| 方法 | Precision | Recall | F1 | RaTEScore | RadGraph |
| :--- | :--- | :--- | :--- | :--- | :--- |
| PromptMRG | 0.501 | 0.509 | 0.476 | - | - |
| MLRG | 0.549 | 0.468 | 0.505 | - | - |
| Qwen2-VL-7B-IDF | 0.535 | 0.464 | 0.497 | 0.486 | 0.210 |
| Ours | 0.591 | 0.476 | 0.527 | 0.557 | 0.249 |

消融实验显示，仅使用LLM时Recall较高（0.517）但Precision低，仅使用LVLM时Precision较高（0.535）但Recall低，双路径融合在两者间取得最佳平衡。然而，本文RadGraph F1（0.249）与领域综述中2025年SOTA方法RadHiera（0.245）持平，表明概率融合在语义结构一致性上未显著超越强化学习路线。

评估边界方面，本文未报告置信区间，且未覆盖2025-2026年基于强化学习（如OraPO）或多智能体（如MARCH）的最新SOTA。代码未公开，超参数 $\alpha$ 的敏感性分析缺失，限制了可复现性。

## 关联研究分析

从问题动机看，本文与PromptMRG共享多标签提示策略，但PromptMRG仅依赖Transformer提取特征，而本文引入LVLM进行视觉接地。差异根源在于任务特性：PromptMRG假设视觉特征可被传统编码器充分提取，而本文认为LVLM的端到端预训练能捕捉更细粒度的视觉-语义对齐。然而，本文未探索LVLM与LLM在特定token上的冲突机制，概率加权可能掩盖了视觉证据与临床知识的矛盾。

从方法设计看，本文与RadHiera同属MIMIC-CXR SOTA，但RadHiera采用强化学习显式抑制幻觉，而本文采用监督微调结合概率融合。RadHiera的RadGraph F1（0.245）与本文（0.249）接近，暗示RL并非提升该指标的唯一路径，但本文缺乏RL对临床逻辑一致性的显式约束，可能在复杂病例中表现受限。本文未对比基于多智能体协作的框架（如MARCH），后者通过工具调用实现可审计性，而本文的概率融合缺乏中间推理过程的透明性。

## 总结

本文核心矛盾在于LVLM视觉接地与LLM临床知识的互补性整合。切入点在于利用解码阶段token级概率融合，克服了单模型在事实一致性与语义完整性上的局限。方法通过结构化提示与双路径训练，在MIMIC-CXR上实现CE F1 0.527，较PromptMRG提升0.051。边界在于RadGraph F1与RL SOTA持平，未显著超越2025年后的方法，且缺乏对融合权重动态调整及3D数据处理的探索。当支持集增大或引入3D CT数据时，静态概率加权是否仍能保持临床准确性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_a6f825379f32)