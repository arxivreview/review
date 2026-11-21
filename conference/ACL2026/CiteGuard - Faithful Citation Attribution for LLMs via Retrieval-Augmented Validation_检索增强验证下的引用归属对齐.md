# ACL2026最新论文 ｜CiteGuard: Faithful Citation Attribution for LLMs via Retrieval-Augmented Validation ｜检索增强验证下的引用归属对齐

研究机构：加拿大滑铁卢大学、美国伊利诺伊大学厄巴纳-香槟分校

作者：Yee Man Choi、Xuehang Guo、Yi R. Fung 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.17853)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ee5728609901)

> 学术写作中LLM生成的引用常出现虚构或错误归属，现有验证方法要么依赖静态的LLM-as-a-Judge导致高误判率，要么受限于PDF解析失败而无法获取深层证据。CiteGuard将引用验证重构为基于工具调用的迭代检索任务，通过扩展Agent的动作空间实现更忠实的引用归属。该方法在CiteME基准上接近人类专家水平，但其跨域泛化能力与实时部署成本仍存疑。

## 研究背景

当LLM生成科学声明时，其引用的文献往往并非真实存在或内容与声明不匹配，这一现象被称为引用幻觉。检测此类幻觉的传统手段是LLM-as-a-Judge，它假设模型具备足够的领域知识来评判引用的正确性。然而，由于预训练数据的局限，LLM对特定领域的细微术语差异极度敏感，导致其在验证正确引用时频繁出现漏判，召回率极低。这种验证机制的失效，使得基于LLM的学术辅助工具在事实准确性上缺乏可信度，阻碍了其在正式出版流程中的落地。

引用完整性验证旨在解决LLM生成文本中引用的真实性与忠实性问题。主流路线分为生成前检索增强与生成后验证两类。生成前方法如RAG在训练或推理时注入外部知识，但难以处理复杂推理与长文本中的细微不一致；生成后方法如CiteAgent通过工具调用检索文献，但其依赖PDF读取动作，在Semantic Scholar等数据库中常因PDF访问失败而退化为仅基于标题和摘要的匹配，导致准确率远低于人类水平。此外，现有基准如CiteME仅包含单一正确引用，无法评估模型发现替代有效引用的能力。CiteGuard的切入点在于，将引用验证从静态判断转变为动态的检索增强验证过程，通过引入不依赖PDF解析的全文片段搜索和上下文获取动作，解决证据获取的鲁棒性问题，并扩展基准以支持多引用评估。

## 核心方法

### 方法参照系

CiteGuard基于CiteAgent的ReAct框架，利用Semantic Scholar API进行文献检索。与CiteAgent仅依赖标题和摘要匹配不同，CiteGuard将任务形式化为在候选池中寻找与摘录语义对齐的引用，并引入迭代排除机制以支持多引用建议。

### 扩展检索动作空间

CiteAgent的检索动作受限于PDF解析的可靠性，当PDF不可用时，Agent无法获取正文证据，导致引用匹配失败。CiteGuard引入了两个关键动作以解决此失效：`ask_for_more_context`用于获取摘录在源论文中的上下文，`search_text_snippet`用于直接在论文全文中搜索查询字符串。

$$
\text{Search}_{sni}(q, D) = \text{argsort}_{p \in P, P \in D} (\text{rel}(q, p))
$$

该公式表示在文档集合$D$中，根据查询$q$与文本片段$p$的相关性进行排序。这一设计使得Agent无需依赖PDF解析，即可从正文中提取证据，显著提升了在PDF缺失或解析失败场景下的检索鲁棒性。

### 迭代排除与多引用建议

单一引用往往不足以全面支撑科学声明，CiteAgent仅输出单一结果，无法提供对比分析所需的文献集合。CiteGuard引入迭代检索机制，每次选定引用后将其从候选池中排除，支持多次运行以发现替代有效引用。

$$
D_k := D \setminus E_{k-1}, \quad E_k := E_{k-1} \cup \{P^{(k)}\}
$$

其中$D_k$为第$k$次迭代时的可搜索数据库，$E_k$为已选引用的排除集。这一机制允许研究者审计Agent的多次建议，并在Agent拒绝建议时介入，体现了人机协作的辅助定位。通过排除已选引用，CiteGuard能够发现与原始引用具有同等或更强证据力的替代文献，提升了引用归属的全面性。

## 实验评估

实验在CiteME（130个计算机科学摘录）和自建CiteMulti（50个跨域及长段落样本）上进行，对比基线包括CiteAgent、AI2 Paper Finder及人类专家。CiteGuard在CiteME上显著优于CiteAgent，且接近人类水平。

| 方法 | Easy (%) | Medium (%) | Med-Hard (%) | Hard (%) | All (%) |
|---|---|---|---|---|---|
| CiteAgent+GPT-4o | 69.7 | 52.2 | 15.4 | 2.9 | 35.4 ± 2.3% |
| CiteGuard+GPT-4o | 86.4 | 65.2 | 20.5 | 6.5 | 45.1 ± 2.7% |
| CiteGuard+DeepSeek-R1 | 95.5 | 87.0 | 71.8 | 15.2 | 68.1 ± 5.8% |
| Human | 95.5 | 80.4 | 69.2 | 21.7 | 69.2 |

CiteGuard+DeepSeek-R1的整体准确率为68.1%，与人类专家的69.2%差距仅为1.1个百分点，表明检索增强验证在引用归属任务上的有效性。

消融实验显示，`search_text_snippet`动作带来的增益（57.7%）大于`ask_for_more_context`（53.1%），两者结合达到59.7%（Kimi-K2）。这表明全文片段搜索对获取深层证据至关重要，而上下文获取主要解决初始片段不足的问题。在CiteMulti基准上，CiteGuard在生物医学（28.3% vs 26.6%）和长段落（46.6% vs 40.0%）场景下均优于CiteAgent，但增益幅度小于CiteME，暗示跨域分布偏移对检索效果的影响。

评估协议存在局限：CiteMulti仅50个样本，统计显著性有限；未对比RAG微调类基线（如OpenScholar），无法区分推理时验证与训练时注入的贡献差异。代码已开源，但`search_text_snippet`依赖Semantic Scholar的全文索引，在私有数据库中的适用性未验证。

## 关联研究分析

从问题动机看，CiteGuard与CiteAgent同属引用完整性验证路线，但CiteAgent依赖PDF读取，而CiteGuard通过`search_text_snippet`规避了PDF解析的脆弱性。这一差异源于任务特性：科学文献的正文往往包含标题和摘要未涵盖的细节，PDF访问失败时，仅基于标题的匹配无法提供足够证据。CiteGuard的设计选择反映了在真实学术数据库中，全文索引比PDF解析更可靠这一现实约束。

从方法设计看，CiteGuard与AI2 Paper Finder同属检索增强框架，但AI2 Paper Finder输出排序列表，而CiteGuard输出单一建议并支持迭代排除。AI2 Paper Finder的Top-10准确率（60.0%）低于CiteGuard+DeepSeek-R1的Top-1准确率（65.4%），表明上下文感知的单一建议比纯排序更可靠。这一差异可能源于CiteGuard整合了摘录的上下文信息，而AI2 Paper Finder仅基于查询排序。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

CiteGuard旨在解决LLM生成引用中的幻觉与错误归属问题，其切入点在于将静态的LLM-as-a-Judge验证转变为动态的检索增强验证，通过扩展Agent的动作空间克服PDF解析失败的瓶颈。该方法在CiteME基准上达到68.1%的准确率，接近人类专家的69.2%，证明了检索增强验证在引用归属任务上的有效性。然而，CiteMulti基准仅50个样本，跨域泛化能力的统计显著性有限，且`search_text_snippet`对Semantic Scholar全文索引的依赖限制了其在私有数据库中的适用性。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ee5728609901)