# ICLR2026最新论文 ｜MC-Search: Evaluating and Enhancing Multimodal Agentic Search with Structured Long Reasoning Chains ｜多模态智能体检索增强生成基准

研究机构：美国伊利诺伊大学厄巴纳-香槟分校、IBM研究院

作者：Xuying Ning、Dongqi Fu、Tianxin Wei 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.00873)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.00873)

> 多模态大语言模型（MLLMs）在处理跨模态知识密集型查询时，常因固定检索-生成范式而陷入浅层证据整合，无法应对需要多步自适应规划的复杂推理。现有基准局限于1-2跳的简单视觉问答，缺乏对长链推理中每步检索保真度与规划忠实性的细粒度评估。本文构建首个包含长链、步骤级标注的多模态智能体检索增强生成（MM-RAG）基准MC-SEARCH，并提出过程级评估指标与对齐框架SEARCH-ALIGN。该工作填补了多模态过程评估空白，但闭源模型在长链上的性能瓶颈及评估者偏差问题仍存疑。

## 研究背景

当MLLMs面对包含图像与文本交织的复杂查询时，传统检索增强生成（RAG）的固定“先检索后生成”流程往往失效，因为此类任务要求模型在视觉与文本证据间动态切换，进行迭代式子问题分解。这种动态规划能力被称为智能体行为，它要求模型不仅检索证据，还需决定何时检索、检索何种模态以及如何整合多步中间结果。然而，现有MM-RAG基准如MMSearch和Dyn-VQA主要聚焦于1-2跳的浅层视觉证据获取，其评估协议将多模态证据坍缩为单一文本通道，且缺乏对推理拓扑结构的显式标注，导致无法区分模型是真正执行了跨模态推理，还是通过模式匹配侥幸答对。

领域共识指出，仅依赖最终答案准确率的评估范式已不足以反映LLMs的真实推理能力，必须引入过程级评估指标。在文本多跳推理领域，HotpotQA等基准确立了基于证据链的评估标准，但其在多模态场景下的迁移面临根本性障碍：图像证据的非结构化特性使得“证据唯一性”难以保证，且视觉检索的模态依赖性导致推理路径呈现串行与并行混合的复杂拓扑。主流路线如CRAFT通过强化学习优化文本轨迹忠实度，NovelHopQA通过长叙事上下文诊断位置偏差，但这些方法均未解决多模态证据归因与跨模态规划验证的核心难题。本文切入点在于构建一个具备步骤级标注、经过证据必要性验证的多模态长链基准，以实现对智能体MM-RAG中检索规划与推理质量的细粒度诊断。

## 核心方法

### 方法参照系

本文问题属于多跳QA基准构建与推理过程评估的交叉领域。标准流程包括数据生成、质量过滤、评估协议设计三个环节。与文本基准的关键差异在于：多模态证据的非唯一性导致推理路径可能冗余或幻觉，且跨模态依赖关系使得简单的线性链无法覆盖真实推理结构，需引入拓扑约束与模态归因机制。

### 推理拓扑定义与HAVE验证机制

针对现有基准缺乏显式推理结构的问题，本文定义了五种推理拓扑：Image-Initiated Chain、Text-Initiated Chain、Parallel Image-Text Fork、Multi-Images Fork和Text-Only Chain。其中，Parallel Image-Text Fork要求图像与文本检索并发执行且无特定跳数依赖，Multi-Images Fork要求多图像视觉比较后转向文本事实支持。为确保每跳必要且非冗余，引入HAVE（Hop-wise Attribution and Verification of Evidence）机制。该机制通过计算移除某步证据后答案准确率的下降量来衡量上下文效用，同时检查该步中间答案中的实体是否出现在下游子问题中以评估导航作用。

$$
\text{Util}(t) = \text{F1}(A_{\text{golden}}, A_{\text{generated}}) - \text{F1}(A_{\text{golden}}, A_{\text{generated}} \setminus r_t)
$$

$$
\text{Nav}(t) = \mathbb{I}[\text{Ent}(a_t) \cap \bigcup_{j>t} \text{Ent}(q_j) \neq \emptyset]
$$

若$\text{Util}(t)$低于阈值且$\text{Nav}(t)=0$，则该步被标记为冗余并过滤。这一设计解决了MLLMs生成推理链时常见的幻觉步骤与冗余步骤问题，确保基准中每条推理路径的结构意义与证据必要性，为步骤级评估提供了可靠基础。

### 过程级评估指标与SEARCH-ALIGN对齐

在评估协议上，本文超越最终答案准确率，提出三个过程级指标：LLM-as-a-Judge（LJ）评估推理质量，Structure-Aware per Step Hit Rate（HPS）量化每步检索保真度，Rollout Deviation（RD）衡量执行偏差。HPS定义为预测图中成功恢复黄金步骤证据的比例，RD定义为预测图与黄金图步长之差的绝对值。

$$
\text{HPS} = \frac{|\{t \in G : \exists t' \in \hat{G}, r_t = \hat{r}_{t'}\}|}{|G|}
$$

$$
\text{RD} = ||\hat{G}| - |G||
$$

基于HAVE验证的推理链，本文进一步提出SEARCH-ALIGN框架，通过监督微调（SFT）将步骤级轨迹作为过程监督信号，而非仅优化最终答案。该框架利用验证链强化开源模型在跨模态规划与检索上的能力，解决了开源模型在智能体MM-RAG中检索规划与步骤级推理对齐薄弱的问题，使其性能接近闭源模型。

## 实验评估

实验在MC-SEARCH基准上进行，覆盖五种推理拓扑，共3,333个样本，平均链长3.7跳。基线包括GPT-4o-Mini、Gemini-2.5-Flash、Gemini-2.5-Pro、Claude-3.7-Sonnet等闭源模型，以及InternVL3.5-8B、Qwen2.5-VL-7B等开源模型。评估协议采用统一的智能体MM-RAG管道，使用相同嵌入模型进行多模态检索。

| 模型 | Image-Initiated F1 | Text-Only F1 | Parallel Fork F1 | Multi-Images F1 |
| :--- | :--- | :--- | :--- | :--- |
| Gemini-2.5-Pro | 47.61 | 34.47 | 34.83 | 40.37 |
| InternVL3.5-8B | 39.11 | 34.82 | 29.74 | 33.08 |
| InternVL3.5-8B + SEARCH-ALIGN | 42.27 | 38.45 | 30.72 | 36.53 |
| Qwen2.5-VL-7B | 26.30 | 23.54 | 22.94 | 26.13 |
| Qwen2.5-VL-7B + SEARCH-ALIGN | 45.70 | 37.54 | 32.73 | 38.01 |

Gemini-2.5-Pro在多数拓扑上表现最佳，但Parallel Image-Text Fork是所有模型的最难拓扑，F1值普遍最低。SEARCH-ALIGN对开源模型带来显著提升，Qwen2.5-VL-7B在Text-Initiated Chain上F1从31.47提升至45.07，InternVL3.5-8B在Image-Initiated Chain上F1从39.11提升至42.27。这表明开源模型的主要弱点在于检索规划与步骤级推理对齐，而非基础感知能力，且这些能力可通过高质量搜索增强推理数据训练改善。

消融分析显示，链长增加导致性能一致下降，GPT-4o-Mini和Claude-3.7-Sonnet在超过3跳后性能急剧下降，而Gemini-2.5-Pro在长链上保持相对稳健。模态覆盖分析揭示，图像检索覆盖率高度依赖显式图像输入，Gemini-2.5-Pro在有图像查询时覆盖率为87.35%，无图像时降至29.50%，InternVL3.5-8B则从63.84%骤降至0.66%。这一发现表明模型存在固有的模态偏好，缺乏在无显式视觉提示时主动发起图像检索的能力。

评估边界方面，LLM-as-a-Judge使用Gemini-2.5-Pro作为评估者，可能引入评估者偏差，论文未报告评分稳定性验证。HAVE过滤机制使用Qwen2.5-VL-7B和Gemini-2.5-Pro进行多阶段验证，但过滤阈值未公开，可能影响基准的泛化性。代码与超参数未完全公开，可复现性受限。

## 关联研究分析

从问题动机看，CRAFT通过双奖励设计生成结构化可审计推理轨迹，聚焦文本RL优化轨迹忠实度，而MC-SEARCH聚焦多模态SFT，利用验证链进行过程监督。两者均强调轨迹忠实度，但CRAFT的奖励信号来自文本逻辑一致性，MC-SEARCH的验证信号来自跨模态证据归因。这一差异源于任务特性：文本推理的忠实性可通过逻辑蕴含验证，而多模态推理的忠实性需同时验证视觉证据与文本事实的对应关系，HAVE机制正是为此设计。

从方法设计看，PAR2-RAG通过分离覆盖获取与推理承诺解决过早承诺问题，采用控制链精炼策略，而MC-SEARCH通过拓扑约束（如Parallel Image-Text Fork）显式建模并发检索，要求模型同时覆盖文本与图像分支。PAR2-RAG的控制链是动态的，根据充分性检查调整检索策略，MC-SEARCH的拓扑是静态的，预先定义推理结构。这一差异暗示，静态拓扑约束可能限制模型在真实场景中自适应调整推理路径的能力，而动态控制链可能更适合开放域查询，但两者在长链多模态推理中的优劣尚无直接对比。

## 总结

本文要解决的核心矛盾是多模态智能体MM-RAG中缺乏长链、步骤级标注的基准，导致无法区分有效跨模态推理与表面模式匹配。现有方法如CRAFT和NovelHopQA分别聚焦文本RL与长上下文诊断，但未解决多模态证据归因与跨模态规划验证问题。本文通过构建MC-SEARCH基准，引入HAVE验证机制过滤冗余跳，定义五种推理拓扑，并提出HPS、RD等过程级指标，实现了细粒度诊断。实验证明SEARCH-ALIGN可显著提升开源模型性能，Qwen2.5-VL-7B在Text-Initiated Chain上F1提升13.6，但闭源模型在Parallel Image-Text Fork上仍表现最差，F1仅34.83。本文的边界在于HAVE过滤可能偏向特定推理模式，且LLM-as-a-Judge的评估者偏差未验证。当支持集增大或查询复杂度进一步增加时，静态拓扑约束是否仍能准确捕捉模型的自适应规划能力，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.00873)