# ACL2026最新论文 ｜WebAggregator: Enhancing Compositional Reasoning Capabilities of Deep Research Agent Foundation Models ｜深度研究智能体中的组合推理瓶颈与数据合成解法

作者：Rui Wang、Ce Zhang、Jun-Yu Ma 等 13 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e529f7ff7600)

> 深度研究智能体（Deep Research Agents, DRA）旨在自动化科学发现，但现有系统普遍存在“重检索、轻推理”的结构性缺陷，导致其在需要多步逻辑聚合的任务中表现受限。本文指出，当前基准中大量任务仅需简单的实体定位，掩盖了模型在组合推理（Compositional Reasoning）上的真实短板。为此，作者构建了WebAggregator框架，通过主动探索与逻辑命题生成合成约10K个可验证的训练对，利用拒绝采样微调模型。该方法证明了高质量推理数据能根本性改变智能体行为，使32B模型在GAIA等基准上超越GPT-4.1，但其在极端复杂逻辑下的泛化能力仍存疑。

## 研究背景

当智能体面对“计算面积大于200万平方公里国家的GDP标准差”这类问题时，其失败往往并非源于无法找到数据，而是无法将分散的数值通过集合过滤、数学运算转化为最终答案。这一过程涉及组合推理，即整合分布式异构信息以解码底层逻辑结构的能力。然而，传统检索增强生成（RAG）及现有基准多聚焦于单跳或浅层多跳问答，缺乏对这种深层逻辑聚合的考察，导致模型倾向于通过频繁调用工具来掩盖推理能力的不足。

现有主流路线分为两类：一类是依赖提示工程的零样本智能体，另一类是基于强化学习（RL）的策略优化。前者受限于底层模型能力，后者虽能优化长程决策，但往往陷入“检索效率”的局部最优，忽略了“推理深度”这一核心瓶颈。例如，WebWalkerQA中30.79%的任务仅需实体定位，TaskCraft中43.2%同理，这种任务难度失衡使得智能体无需进行复杂的逻辑合成即可得分。WebAggregator的切入点在于重构训练数据分布，通过强制要求多源信息聚合与复杂逻辑操作，迫使模型从“信息获取者”转变为“逻辑合成者”，从而突破检索中心范式的天花板。

## 核心方法

### 方法参照系

本文问题属于智能体训练数据合成范畴，但区别于通用的随机探索轨迹收集。标准流程通常从随机URL开始，通过ReAct循环收集轨迹，但本文的关键差异在于引入了“逻辑导向”的探索与命题生成，确保生成的任务必须包含特定的组合推理路径，而非简单的信息查找。

### 主动探索与信息收集

Proactive Explorer模块负责从锚点URL出发，利用搜索、静态解析、动态交互等工具收集互联信息。设计动机在于解决现有数据源单一、缺乏动态元素（如JavaScript、文件）的问题。该模块通过强制最少页面访问次数，确保知识池的丰富性。其核心逻辑可形式化为信息集合的扩展：

$$ I_{final} = \bigcup_{i=1}^{n} T_i(U_{anchor}) $$

其中 $T_i$ 为第 $i$ 次工具调用，$U_{anchor}$ 为锚点URL。这一过程确保了后续问题构建拥有足够的多源异构数据基础，避免了因信息缺失导致的逻辑断裂。

### 组合逻辑命题生成

Compositional Logic Proposer将收集到的原始信息转化为复杂的推理挑战。设计动机在于现有基准缺乏对逻辑操作类型的显式控制，导致任务难度不可控。该模块基于Element、Set、Scientific Analysis、Temporal Reasoning四大类12种子类型，将逻辑模式实例化为具体问题。例如，将“Set->Filter”实例化为“筛选面积大于200万平方公里的国家”。其生成过程可表示为：

$$ Q = \text{Instantiate}(G, I_{final}) $$

其中 $G$ 为高层逻辑指导，$I_{final}$ 为收集的信息。这种灵活引导机制确保了生成的问题既具有逻辑深度，又具备可验证性，从而为后续SFT提供高质量的监督信号。

## 实验评估

实验在GAIA-text、WebWalkerQA、XBench及新提出的WebAggregatorQA上进行，基线涵盖GPT-4.1、Claude-3.7-Sonnet及WebThinker等微调模型。主实验结果显示，WebAggregator-32B在GAIA-text上达到69.2%的Pass@1，显著优于GPT-4.1的51.3%和WebShaper的61.5%。在WebAggregatorQA上，Claude-3.7-Sonnet仅得28.3%，而WebAggregator-32B达到26.4%，表明新基准对现有模型构成严峻挑战。

| 方法 | GAIA-text Pass@1 | WebAggregatorQA Pass@1 |
| :--- | :--- | :--- |
| GPT-4.1 | 51.3 | 25.8 |
| Claude-3.7-Sonnet | 74.4 | 28.3 |
| WebShaper (Qwen2.5-32B) | 61.5 | — |
| WebAggregator (Qwen3-32B) | 69.2 | 26.4 |

消融分析揭示了行为模式的根本转变：微调后，8B模型的推理比率（Type B）从18.6%提升至26.2%，而工具调用密度显著下降。这表明模型不再依赖冗余的工具执行，而是优先进行内部逻辑合成。值得注意的是，即使提供所有参考URL，Claude-3.7-Sonnet在WebAggregatorQA上的准确率仅为42.1%，证实了组合推理而非检索是当前的性能瓶颈。

评估协议采用GPT-4.1作为评判者，可能存在偏差。代码已开源，但训练数据的具体分布细节（如各逻辑类型的比例）未完全披露，限制了跨骨干模型的复现性。此外，实验主要基于Qwen系列模型，缺乏对Llama等其他骨干的验证，SFT效果的泛化性有待进一步确认。

## 关联研究分析

从问题动机看，WebAggregator与ASearcher形成鲜明对比。ASearcher通过大规模端到端RL优化长程搜索策略，侧重于“如何找到信息”；而WebAggregator通过SFT注入推理模式，侧重于“如何处理信息”。这种差异源于对瓶颈的不同判断：ASearcher认为策略次优是主要问题，WebAggregator则认为逻辑合成能力缺失是核心障碍。在GAIA上，WebAggregator-32B（69.2%）超越了ASearcher（53.2%），暗示在组合推理密集型任务中，高质量SFT数据可能比RL策略优化更具效率。

从方法设计看，WebAggregator与WebThinker同属智能体微调框架，但WebThinker依赖通用轨迹，而WebAggregator引入逻辑类型约束。WebThinker在GAIA上达到56.4%，低于WebAggregator的69.2%，表明逻辑导向的数据合成比随机探索更能提升推理密度。然而，WebAggregator未探索RL与SFT的结合，若将组合推理奖励引入RL循环，是否能进一步突破26.4%的WebAggregatorQA上限，论文未给出回答。

## 总结

本文针对深度研究智能体“重检索、轻推理”的矛盾，通过构建逻辑导向的数据合成框架WebAggregator，证明了高质量组合推理数据能根本性提升模型性能。WebAggregator-32B在GAIA-text上达到69.2%，在WebAggregatorQA上虽仅26.4%，但揭示了现有模型在逻辑合成上的严重短板。其边界在于仅验证了SFT在Qwen骨干上的有效性，且未解决极端复杂逻辑下的泛化问题。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_e529f7ff7600)