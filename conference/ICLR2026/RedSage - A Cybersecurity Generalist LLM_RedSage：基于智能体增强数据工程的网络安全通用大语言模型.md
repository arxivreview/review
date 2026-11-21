# ICLR2026最新论文 ｜RedSage: A Cybersecurity Generalist LLM ｜RedSage：基于智能体增强数据工程的网络安全通用大语言模型

研究机构：德国波恩大学、美国纽约大学

作者：Naufal Suryanto、Muzammal Naseer、Pengfei Li 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.22159)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.22159)

> 导读 网络安全运营面临专家技能短缺与敏感数据隐私合规的双重约束，现有方案要么依赖存在数据泄露风险的专有API，要么使用缺乏深度领域适配的开源模型。本文切入点在于构建一个完全本地化、开源且覆盖知识、技能与工具操作全维度的8B参数安全专用模型。通过大规模领域持续预训练结合智能体驱动的多轮对话数据增强，RedSage在保持通用推理能力的前提下实现了安全任务的性能突破。其价值在于提供了可复现的端到端数据工程范式，但智能体生成数据的潜在幻觉偏差及缺乏检索增强生成机制对时效性知识的处理仍是存疑点。

## 研究背景

安全运营中心（SOC）分析师在处理海量异构遥测数据时，亟需能够理解非结构化日志并执行复杂推理的智能系统。大语言模型（Large Language Models, LLMs）的引入旨在通过自然语言处理能力桥接低层遥测数据与高层战术意图之间的语义鸿沟。然而，通用LLM在安全术语理解上存在严重不足，且其参数化知识无法实时获取最新漏洞信息，导致在复杂威胁归因和战术映射任务中表现不佳。解决这一问题的核心在于领域适应预训练（Domain-Adaptive Pretraining, DAP）与高质量指令微调，即通过专用语料库弥补通用模型的知识缺口，并通过指令数据提升其在特定工作流中的执行能力。

2020-2023年，研究主要聚焦于验证LLM在安全任务中的可行性，CyBERT和SecureBERT等基于BERT架构的编码器模型通过DAP证明了专用语料库的关键作用，但受限于编码器架构，其在生成复杂推理链条方面能力有限。2024-2025年，随着生成式LLM的成熟，研究重心转向如何利用其生成能力处理非结构化情报，小型语言模型（Small Language Models, SLMs）开始受到关注。然而，现有安全专用模型大多强调单一训练阶段，例如PRIMUS仅提供835个监督微调样本，Foundation-Sec-8B虽收集了5.1B tokens但数据未公开，DeepHat则缺乏预训练阶段来强化领域知识。这种训练流程的碎片化导致模型在知识、技能与工具操作能力上存在显著短板，且现有基准测试往往只覆盖部分维度，缺乏对工具熟练度和自由回答质量的系统评估。

## 核心方法

### 方法参照系

构建安全专用LLM的通用流程通常包括领域语料过滤、持续预训练（Continual Pretraining, CPT）和监督微调（Supervised Fine-Tuning, SFT）。本文问题与该通用流程的关键差异在于，传统SFT数据多为静态问答对，缺乏对专家工作流中多轮交互、工具调用及上下文依赖的模拟，导致模型在复杂任务编排中表现不佳。

### 大规模领域持续预训练

设计动机在于解决通用模型在安全术语语义理解上的根本缺失，以及避免领域预训练导致的通用知识灾难性遗忘。本文首先从FineWeb中过滤出约125M篇网络安全文档，构建CyberFineWeb语料库。为防止通用能力退化，引入30%的FineWeb-Edu通用教育数据作为回放（Replay）机制。最终通过MinHash-LSH去重，得到约11.7B tokens的混合语料。该阶段的训练目标函数为标准的交叉熵损失：

$$
\mathcal{L}_{CPT} = -\sum_{t=1}^{T} \log P(x_t | x_{<t}, \theta)
$$

其中 $\theta$ 为模型参数，$x_t$ 为当前token。这一公式的物理含义是最大化模型在混合语料（安全+通用）上预测下一个token的对数似然，通过30%的通用数据回放，确保模型在吸收安全领域知识的同时，维持其在通用推理任务上的基线性能。

### 智能体增强数据生成

设计动机在于解决静态SFT数据无法模拟专家-助手多轮交互工作流的问题，从而提升模型在复杂任务中的指令遵循与工具调用能力。本文提出Agentic Augmentation管道，利用Planner Agent分析种子数据（如CAPEC攻击模式）并生成技能集与增强计划，再由Augmenter Agent将这些计划实例化为基于角色的多轮对话。该过程将28.6K个种子样本扩展为266K个多轮对话，样本量扩大9.2倍。生成的对话数据用于SFT，其损失函数同样为交叉熵：

$$
\mathcal{L}_{SFT} = -\sum_{i=1}^{N} \sum_{t=1}^{T_i} \log P(y_{i,t} | x_i, y_{i,<t}, \theta)
$$

其中 $x_i$ 为用户输入，$y_{i,t}$ 为模型生成的第t个token。该公式确保了模型在模仿专家工作流时，能够准确学习多轮上下文中的依赖关系。随后，使用Tulu 3数据集进行直接偏好优化（Direct Preference Optimization, DPO），以进一步提升回答质量。DPO的损失函数为：

$$
\mathcal{L}_{DPO} = -\mathbb{E}_{(x, y_w, y_l)} \left[ \log \sigma \left( \beta \log \frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)} - \beta \log \frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)} \right) \right]
$$

其中 $y_w$ 和 $y_l$ 分别为偏好和非偏好回答，$\pi_{ref}$ 为参考模型。该公式通过优化偏好回答与非偏好回答的对数似然差，使模型输出更符合人类专家的质量标准，而非仅仅追求事实正确性。

## 实验评估

实验在RedSage-Bench（30K MCQs + 240 open-ended Q&A）、CyberMetric、CTI-Bench、SECURE等安全基准及Open LLM Leaderboard通用基准上进行。基线覆盖Llama-3.1-8B、Qwen3-8B、Foundation-Sec-8B、Llama-Primus等开源模型，以及GPT-5和Qwen3-32B作为强参照。

| 模型 | RedSage-Bench Macro Acc (%) | CyberMetric 500 Acc (%) | CTI-Bench MCQ Acc (%) | MMLU CSec Acc (%) |
| :--- | :--- | :--- | :--- | :--- |
| Llama-3.1-8B-Instruct | 77.05 | 68.00 | 43.60 | 35.37 |
| Foundation-Sec-8B-Instruct | 76.12 | 59.66 | 68.50 | 65.46 |
| Qwen3-8B | 81.85 | 83.80 | 68.20 | 65.46 |
| **RedSage-8B-Ins** | **85.73** | **79.00** | **70.56** | **72.48** |
| **RedSage-8B-DPO** | 84.83 | **80.06** | **76.70** | **74.22** |
| GPT-5 | 88.68 | 95.60 | 76.48 | 86.00 |

RedSage-8B-Ins在RedSage-Bench上达到85.73%，超越Qwen3-8B 3.88个点，但在CyberMetric上（79.00%）低于Qwen3-8B（83.80%），表明其在特定知识检索任务上仍有差距。RedSage-8B-DPO在CTI-Bench MCQ上达到76.70%，显著优于Foundation-Sec-8B-Instruct的68.50%，验证了DPO在复杂推理任务中的增益。

消融实验显示，仅使用CyberFineWeb预训练的RedSage-8B-CFW在RedSage-Bench上达到84.86%，而加入RedSage-Seed后（RedSage-8B-Seed）提升至85.21%，表明高质量种子数据对框架知识（+3.00）和Kali工具操作（+1.04）有显著提升。SFT阶段，RedSage-8B-Ins相比Base模型（85.05）进一步提升至85.73，而DPO阶段（RedSage-8B-DPO）在RedSage-Bench上略降（84.83），但在开放问答的质量评分上优于Ins版本，说明DPO主要优化了回答的有用性和相关性，而非单纯的事实准确性。

评估边界方面，RedSage-Bench的MCQ部分采用0-shot normalized log-likelihood accuracy，开放问答采用LLM-as-Judge评分，可能存在评估者偏差。数据去污染通过语义相似度>0.9过滤，消除了2.96%的训练数据，但无法完全排除训练-测试集间的隐性重叠。可复现性方面，论文提供了完整的Axolotl训练配置、32×A100-64GB GPU的超参数及开源代码，但智能体增强管道的具体Prompt模板仅在附录中提供，复现成本较高。

## 关联研究分析

从数据工程范式看，RedSage与CyberPal 2.0同属SLM路线，但CyberPal 2.0依赖SecKnowledge 2.0管道生成高保真推理轨迹，侧重思维链（Chain-of-Thought, CoT）的注入，而RedSage通过Agentic Augmentation模拟专家-助手多轮对话，侧重工作流交互与工具调用。这一差异源于任务特性：CyberPal聚焦于CTI知识问答，需要深度推理；RedSage则覆盖工具操作，需要多轮上下文管理。RedSage未与CyberPal 2.0直接对比，可能是因为两者评估基准不同，且CyberPal 2.0未完全开源，导致无法在统一协议下进行公平比较。

从训练流程完整性看，RedSage与Foundation-Sec-8B均基于Llama-3.1-8B进行CPT，但Foundation-Sec-8B的SFT数据仅28K且未公开，而RedSage通过智能体增强生成266K多轮对话，并引入通用指令数据（SmolLM3）以保持泛化能力。RedSage在MMLU CSec上（72.48%）显著优于Foundation-Sec-8B-Instruct（65.46%），表明其通用能力保留策略更有效。然而，RedSage未集成检索增强生成（Retrieval-Augmented Generation, RAG）模块，完全依赖参数化知识，这在处理最新漏洞等时效性信息时可能面临知识过时问题，而Foundation-Sec-8B虽未显式集成RAG，但其闭源架构可能隐含了实时数据接入能力，这一差异在论文中未得到充分讨论。

## 总结

RedSage旨在解决安全专用LLM在训练流程碎片化与数据隐私合规之间的矛盾，通过大规模领域CPT与智能体增强SFT，在8B参数规模下实现了安全任务与通用能力的平衡。其核心贡献在于构建了11.7B tokens的CyberFineWeb语料和266K多轮对话数据集，证明了Agentic数据工程在提升工具操作能力上的有效性，RedSage-8B-Ins在RedSage-Bench上达到85.73%，CTI-Bench MCQ上达到70.56%。然而，其边界在于缺乏RAG机制，无法动态获取最新威胁情报，且智能体生成数据可能引入LLM自身的幻觉偏差，导致在开放问答中虽质量评分高，但事实准确性仍有提升空间。当面对零日攻击或最新CVE漏洞时，仅依赖参数化知识的RedSage能否保持有效的威胁识别与响应能力，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.22159)