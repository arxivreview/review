# ICLR2026最新论文 ｜JQBENCH: A BENCHMARK FOR READING AND EDITING JSON FROM NATURAL LANGUAGE AND/OR EXAMPLES ｜JSON查询基准JQBENCH：自然语言到jq表达式的评估与失败模式分析

作者：Gust Verbruggen、Chris Parnin、Vu Le 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_87629602)

> 自然语言到结构化查询（NL2SQL）领域长期聚焦于关系型数据库的SQL生成，但现代AI工作流中JSON作为数据交换标准，其查询与转换需求日益增长，却缺乏联合捕捉自然语言提示与可执行JSON查询的基准。现有NL2SQL方法假设数据干净且Schema较小，难以处理JSON的嵌套灵活性与jq语言的生僻性，导致模型在真实开发者场景下性能显著下降。本文通过自动管道从Stack Overflow和Spider数据集构建JQBENCH基准，揭示低资源语言下LLM的语法习得瓶颈与代理式工作流的“文档陷阱”。该基准填补了NL2JSON评估空白，但jq任务难度是否源于语言生僻而非逻辑复杂，仍需更多证据支持。

## 研究背景

当LLM处理JSON数据时，其嵌套结构与动态键名导致传统SQL的刚性模式链接失效——这一现象称为Schema链接噪声。Schema链接噪声使模型无法准确识别深层嵌套路径，而jq作为JSON查询语言，其管道操作与函数组合进一步加剧了语法生僻性，这恰好构成了低资源语言学习的条件：模型需在极少训练数据下掌握陌生语法的语义边界。解决此类问题的经典框架是执行反馈循环，它通过编译与执行结果迭代修正表达式，但现有NL2SQL方法如AskDB（Phan et al., 2025）仅针对SQL，未考虑jq的表达式简洁性与函数稀有性差异。

NL2SQL领域已形成“Schema链接是准确性主要瓶颈”的共识，动态Schema子集选择比全量Schema更有效（Datalake Agent, Jehle et al., 2025）。然而，当数据形态从关系型表转向嵌套JSON时，Schema链接问题演变为JSON Schema生成与嵌套路径识别的双重挑战，现有方法如text2ql（Kumar, 2026）的中间表示架构未针对jq的管道链设计。本文切入点在于构建首个联合自然语言与可执行jq查询的基准，通过Stack Overflow真实问题与Spider数据库转换，揭示低资源语言下LLM的失败模式，而非仅优化SQL生成准确率。

## 核心方法

### 方法参照系

NL2SQL标准流程包含Schema链接、SQL生成与执行验证三阶段，本文问题与该通用流程的关键差异在于：目标语言jq的函数稀有性（116种操作符 vs SQL的56种）与嵌套路径的动态性，使Schema链接从静态表列选择变为JSON Schema生成与路径遍历的联合优化。

### 自动基准构建管道

JQBENCH构建流程在Schema链接阶段引入JSON Schema生成，通过LLM将SQL表结构转换为嵌套JSON Schema，利用jsonschema包提供验证反馈。设计动机是解决SQL Schema到JSON Schema的语义映射失效，传统符号启发式无法生成复杂嵌套结构。该管道通过迭代执行反馈修正转换错误，公式为：

$$
\text{Score}(s) = \frac{1}{|T|} \sum_{t \in T} \mathbb{I}[\text{jq.all}(e, i_t) = [o_t]]
$$

其中$T$为测试集，$e$为jq表达式，$i_t$、$o_t$为输入输出对，$\mathbb{I}$为指示函数。该公式计算表达式在所有测试用例上的值匹配率，忽略键名与顺序，更贴近JSON数据交换的实际效用。

### 隐式反馈与文档陷阱机制

在代理式工作流中，本文对比隐式反馈（基于示例的执行结果）与显式反馈（工具调用）的差异。设计动机是解决高能力模型在文档检索中的“文档陷阱”——Opus 4.1访问文档后性能从76%降至31%，因陷入请求文档循环而非解决问题。该机制通过SELF-DEBUG循环提供编译与执行反馈，公式为：

$$
\Delta P_{\text{doc}} = P_{\text{no-doc}} - P_{\text{doc}} = 0.76 - 0.31 = 0.45
$$

其中$P_{\text{no-doc}}$、$P_{\text{doc}}$分别为无文档与有文档时的值匹配率。该公式量化了文档辅助的负迁移效应，揭示模型能力与工具使用策略的匹配机制：当模型jq熟练度超过阈值时，SELF-DEBUG比检索增强生成更有效。

## 实验评估

实验在JQSTACK（1496任务）与JQSPIDER（859任务）上进行，基线覆盖Opus 4.1、GPT-5、Phi-4等模型，但缺失专用微调小模型或符号归纳编程基线。主结果显示Opus 4.1在JQSTACK达76%值匹配率，JQSPIDER达81%，显著高于GPT-5的68%与59%，表明高能力模型在低资源语言下的优势。

| 模型 | JQSTACK值匹配率 | JQSPIDER值匹配率 |
| :--- | :--- | :--- |
| Opus 4.1 | 0.76 | 0.81 |
| GPT-5 | 0.68 | 0.75 |
| GPT-5-mini | 0.59 | 0.72 |
| Phi-4 | 0.10 | 0.43 |

消融实验揭示关键设计决策：从隐式反馈转向显式工具调用导致GPT-5性能下降53%，Opus 4.1下降22%，因模型未充分利用示例（GPT-5输入覆盖率仅27.8% vs Opus 4.1的68.5%）。文档陷阱效应中，Opus 4.1的文档请求率是GPT-5 mini的5倍，导致性能负迁移。

评估边界在于：值匹配率忽略键名与顺序，可能高估实际效用；未报告置信区间，数值比较需谨慎；代码与超参数已开源，但GPU资源未说明，可复现性受限于模型API访问。

## 关联研究分析

从问题动机看，JQBENCH与AskDB（Phan et al., 2025）同属代理式架构，但AskDB针对SQL的静态Schema链接，本文针对jq的动态嵌套路径，差异根源在于JSON的灵活结构使Schema链接从表列选择变为路径遍历，AskDB的ReAct循环未处理jq函数稀有性导致的语法习得瓶颈。从方法设计看，JQBENCH与text2ql（Kumar, 2026）均涉及中间表示，但text2ql的QueryIR解耦自然语言理解与SQL生成，本文直接用jq，差异根源在于jq的管道链比SQL更简洁，中间表示可能引入额外转换错误，text2ql未评估jq场景下的必要性。

## 总结

本文要解决的核心矛盾是JSON查询缺乏联合自然语言与可执行表达式的基准，现有NL2SQL方法无法处理jq的低资源语言特性。本文抓住的切入点是自动构建真实开发者问题与数据库转换任务，通过执行反馈揭示失败模式。本文构建了JQBENCH基准，证明了Opus 4.1在JQSTACK达76%值匹配率，文档辅助导致性能下降45%。本文的边界在于值匹配率忽略键名与顺序，且未对比符号归纳编程基线。当jq任务难度因语言生僻而非逻辑复杂导致时，执行反馈循环的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_87629602)