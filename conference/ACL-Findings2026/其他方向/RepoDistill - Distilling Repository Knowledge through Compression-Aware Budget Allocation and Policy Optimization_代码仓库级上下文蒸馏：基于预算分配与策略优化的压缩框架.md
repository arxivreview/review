# ACL-Findings2026最新论文 ｜RepoDistill: Distilling Repository Knowledge through Compression-Aware Budget Allocation and Policy Optimization ｜代码仓库级上下文蒸馏：基于预算分配与策略优化的压缩框架

研究机构：浙江大学、上海交通大学

作者：Xin Yin、Zixiang Ding、Yiang Zhang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2f34605a547f)

> 大语言模型在处理仓库级代码任务时，常因长上下文中的冗余信息导致注意力稀释与关键逻辑丢失。现有检索方法虽能定位相关片段，但无法在函数内部进一步剔除噪声，且静态压缩策略难以适应动态查询需求。RepoDistill 通过图结构检索结合强化学习驱动的细粒度预算分配，实现了从“片段级筛选”到“行级蒸馏”的跨越。该方法在代码问答与生成任务上显著优于基线，但其效果高度依赖预训练小模型的蒸馏质量，跨仓库泛化能力尚存疑。

## 研究背景

仓库级代码理解要求模型在跨越多个文件的复杂依赖网络中定位关键逻辑。这一过程面临“中间迷失”（Lost in the Middle）现象：当输入序列超过一定长度，模型对位于中间位置的信息利用率显著下降。更严峻的是，即使检索到了相关函数，其中大部分代码行与当前查询无关，这些冗余行占据了宝贵的上下文窗口，进一步加剧了注意力分散。

通用文本压缩方法（如基于困惑度的硬压缩或连续向量软压缩）在处理代码时存在结构性缺陷。代码具有严格的语法依赖和层级结构，简单的 Token 剔除易破坏依赖闭合，而通用软压缩难以捕捉函数调用链的逻辑流向。现有代码压缩方案如 LongCodeZip 采用固定预算的粗到细策略，但无法根据查询动态调整保留比例；而基于图的检索方法（如 GRACE）虽能获取结构上下文，却缺乏对片段内部噪声的精细过滤机制。RepoDistill 的切入点在于将上下文管理建模为多轮决策问题，通过强化学习让模型自主决定每个代码片段的保留预算，从而在结构完整性与信息密度之间取得动态平衡。

## 核心方法

### 方法参照系

RepoDistill 属于领域特定压缩与智能体上下文管理的交叉路线。其基础流程遵循“检索-压缩-推理”范式，但关键差异在于压缩环节：不同于通用压缩的固定比例或二值筛选，RepoDistill 引入连续预算分配机制，将压缩决策转化为可学习的策略优化问题。

### 图结构检索与重排序

设计动机在于解决通用语义检索无法捕捉代码逻辑依赖的问题。RepoDistill 首先构建代码依赖图 $G=(V, E)$，其中节点 $V$ 为代码结构单元，边 $E$ 包含 CONTAIN（包含）与 INVOKE（调用）两种关系。检索时，通过 Qwen3-Embedding-0.6B 计算查询 $q$ 与节点 $v_i$ 的相似度，选取 Top-K 锚点节点 $N_{Top-K}$：

$$ N_{Top-K} = \arg \max_{V' \subset V, |V'|=K} \sum_{v \in V'} \text{sim}(q, v) $$

随后，通过挖掘锚点间的最短路径及一阶子树扩展候选集，并利用统一相关性分数 $S(q, c) = \lambda \cdot \text{sim}(q, c) + (1-\lambda) \cdot \max_{v \in c} \text{sim}(q, v)$ 进行重排序。这一设计确保了检索结果不仅语义相关，且逻辑连贯，为后续压缩提供了结构化的输入基础。

### 压缩感知预算分配与策略优化

设计动机在于解决固定预算压缩无法适应查询复杂度的问题。CABA 模块采用 MMR（最大边际相关性）进行块级选择，其核心公式为：

$$ \text{MMR}(b) = \lambda \cdot \text{AMI}(b, q) - (1-\lambda) \cdot \max_{b_j \in S} \text{Sim}(b, b_j) $$

其中 $\text{AMI}(b, q) = \text{PPL}(q) - \text{PPL}(q|b)$ 衡量块 $b$ 对查询的信息增益。CAPO 模块则通过多轮强化学习优化预算分配策略。模型将上下文管理视为多步决策过程，每轮为代码片段分配 0%-100% 的保留预算，并更新记忆摘要。奖励函数包含任务准确性奖励 $R_{metric}$ 与效率奖励 $R_{efficiency}$，后者定义为：

$$ R_{efficiency} = R_{metric} \cdot \text{Sigmoid}\left(\ln \frac{L_{input}}{L_{used}}\right) $$

该公式鼓励模型在保持答案正确性的前提下，最大化压缩率。通过 SFT 蒸馏强模型策略后，利用 GRPO 进行多轮 RL 训练，使小模型学会自主校准预算，实现答案关键逻辑的精准保留。

## 实验评估

实验在 SWE-QA、CoderEval 和 LongCodeU 三个基准上进行，基线涵盖 Function Chunking RAG、Sliding Window RAG、RepoScope、GRACE 等检索方法及 LongCodeZip、Context-Picker 等压缩方法。缺失通用软压缩方法（如 ICAE）在代码任务上的对比，限制了跨范式比较。

| 方法 | SWE-QA Overall | CoderEval-Python Pass@10 | CoderEval-Java Pass@10 |
| :--- | :--- | :--- | :--- |
| Qwen3-4B-Instruct (Direct) | 5.12 | 32.1% | 34.8% |
| + GRACE | 31.53 | 39.3% | 51.4% |
| + RepoDistill | 35.19 | 42.6% | 56.2% |

RepoDistill 在 SWE-QA 上较最佳基线 GRACE 提升 3.66 分，在 CoderEval-Python Pass@10 上提升 10.5%，表明结构感知压缩优于纯语义检索。

| 消融变体 | SWE-QA Overall | CoderEval-Python Pass@10 | CoderEval-Java Pass@10 |
| :--- | :--- | :--- | :--- |
| RepoDistill | 35.19 | 42.6% | 56.2% |
| w/o CABA | 34.02 | 41.6% | 54.1% |
| w/o CAPO | 32.58 | 41.2% | 53.7% |
| w/ LongCodeZip | 34.77 | 40.7% | 54.6% |

消融实验显示，移除 CAPO 导致性能下降 2.61 分，移除 CABA 下降 1.17 分，表明策略优化比静态压缩机制贡献更大。替换为 LongCodeZip 后性能低于完整模型，验证了 MMR 动态选择优于固定预算的 0/1 背包问题。

评估协议采用 LLM-as-judge 框架，使用 DeepSeek-V3.2 和 Kimi-K2 进行五维评分，每实例五次独立评估取平均，有效缓解了位置偏差。代码已开源，训练使用 32 块 A100-80GB GPU，SFT 5 轮，GRPO 2 轮，超参数透明。局限在于 SWE-QA 数据集仅含 12 个项目，训练/测试集划分可能导致过拟合；且未报告计算延迟，无法评估压缩开销对推理速度的影响。

## 关联研究分析

从问题动机看，RepoDistill 与 LongCodeZip 均针对代码内部冗余，但 LongCodeZip 采用固定预算的粗到细策略，假设块价值独立，而 RepoDistill 通过 RL 学习动态预算，解决了固定策略在复杂查询下的适应性不足。这一差异源于代码依赖的非线性特性：不同查询对同一函数的关键行需求差异巨大，静态预算无法捕捉这种动态性。

从方法设计看，RepoDistill 借鉴了 MemGPT 的动态记忆管理思想，但将其具体化为代码片段的预算分配而非外部存储调度。与 GRACE 等图检索方法相比，RepoDistill 证明了轻量级 GraphRAG 结合有效压缩策略可媲美复杂图方法，暗示在代码压缩中，结构检索的边际收益可能低于压缩策略的优化空间。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

RepoDistill 旨在解决仓库级代码任务中长上下文冗余导致的注意力稀释问题。现有方法要么缺乏结构感知，要么压缩策略静态僵化，无法适应动态查询。本文通过图结构检索结合 RL 优化的预算分配，实现了细粒度代码蒸馏。实验表明，该方法在 SWE-QA 上较最佳基线提升 3.66 分，在 CoderEval-Python Pass@10 上提升 10.5%。其边界在于依赖小模型蒸馏质量，且未验证跨仓库泛化能力。当支持集增大到 5-shot 时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_2f34605a547f)