# ACL-Findings2026最新论文 ｜CRAFTQA: A Code-Driven Adaptive Framework for Complex Structured Data Reasoning ｜代码驱动的结构化数据自适应推理框架

研究机构：浙江大学

作者：Chengtao Gan、Zhiqiang Liu、Long Jin 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.02170)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_41964b0b8a71)

> 统一结构化数据问答旨在让大语言模型在表格、知识图谱等异构数据源上执行自然语言查询，但现有方法受限于预定义函数集，无法处理超出该集合的复杂逻辑操作。CRAFTQA 通过生成可执行 Python 代码序列分离推理与计算，并引入动态函数定制模块突破预定义边界。该框架在复杂推理场景下显著优于基线，但其性能高度依赖底层 LLM 的代码生成能力，且未验证动态生成代码的逻辑正确性。

## 研究背景

当用户提出“计算某导演获得奥斯卡提名的电影数量”这类问题时，系统需先检索导演作品，再过滤特定奖项记录，最后执行计数。这一过程涉及多步依赖操作，若仅靠固定 API 调用，一旦遇到“过滤包含特定关键词的备注”等非标准操作，系统即陷入停滞。这种停滞源于预定义函数集的封闭性，而解决该问题需引入代码生成机制，使模型能动态编写逻辑分支。

统一结构化数据问答的主流路线包括迭代阅读-推理（如 StructGPT）和统一查询语言（如 TrustUQA）。StructGPT 通过多轮证据收集提升召回，但缺乏对复杂计算逻辑的显式建模；TrustUQA 利用条件图（Condition Graph）统一表示数据，但严格限制在预定义函数集内，导致面对“Out-of-Predefined”操作时准确率骤降。CRAFTQA 的切入点在于将代码生成作为一等公民，不仅用于数值计算，更用于动态扩展函数集，从而在保持结构化数据查询确定性的同时，获得处理复杂逻辑的灵活性。

## 核心方法

### 方法参照系

本文问题属于统一结构化数据问答，其通用流程是将自然语言问题转化为对结构化数据（表格、KG、TKG）的查询操作。与通用流程的关键差异在于，本文不直接生成最终答案或固定 API 调用序列，而是生成完整的可执行 Python 代码序列，将推理逻辑显式编码为程序步骤，并通过代码执行器获取确定性结果。

### CodeSTEP：步骤化代码生成范式

CodeSTEP 模块解决的是如何将自然语言问题分解为可执行的代码步骤。传统方法如 TrustUQA 直接映射问题到固定函数调用，无法处理步骤间的复杂依赖。CodeSTEP 采用两阶段生成：首先由 LLM $M_\theta$ 构建自然语言推理路径 $S = \{s_i\}_{i=1}^n$，然后为每个 $s_i$ 生成对应代码 $c_i$。每个代码步骤 $c_i$ 表示为函数调用：

$$
c_i = \begin{cases}
f_i(D_{cg}, \tilde{W}_i), & f_i \in F_{pred} \\
f_{craft}(T_i, W_i, F_{exp,i}), & \text{otherwise}
\end{cases}
$$

其中 $F_{pred}$ 为预定义函数集，$W_i$ 为前序步骤的中间结果。该设计将推理过程显式化为代码序列，使得每一步的输入输出可追踪，为后续动态函数生成提供了上下文基础。

### CRAFT：动态函数定制机制

CRAFT 模块解决的是预定义函数集无法覆盖“Out-of-Predefined”操作的问题。当 CodeSTEP 生成 $f_{craft}$ 调用时，CRAFT 触发动态函数合成。CRAFT 利用另一个 LLM $M_{\theta'}$ 基于五元组输入 $(Q, C, T_i, W_i, F_{exp,i})$ 生成自定义函数 $\hat{f}_i$：

$$
M_{\theta'}(Q, C, T_i, W_i, F_{exp,i}, P_c) \rightarrow \hat{f}_i
$$

其中 $Q$ 为原始问题，$C$ 为完整代码序列，$T_i$ 为当前任务描述，$W_i$ 为前序结果，$F_{exp,i}$ 为期望函数签名。生成的 $\hat{f}_i$ 被执行后，其结果 $w_i$ 返回至 CodeSTEP 主流程。该机制允许系统在运行时动态扩展功能边界，无需重新训练或修改预定义函数集，从而处理如“过滤包含特定文本的实体”等复杂逻辑。

## 实验评估

实验在 WikiSQL-E、TableBench（FC/NR）、WebQSP 和 CronQuestions 上进行，基线包括 PoT、StructGPT、Readi 和 TrustUQA。基线覆盖了代码生成、迭代阅读和统一查询三条路线，但缺失纯检索增强（RAG）基线，可能低估了 CRAFTQA 相对于简单检索方法的优势。

| 方法 | 骨干 LLM | TableBench-FC DA(%) | TableBench-NR DA(%) | WikiSQL-E CDA(%) | Overall |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TrustUQA | GPT-4o | 62.5 | 29.6 | 80.1 | 67.2 |
| CRAFTQA | GPT-4o | 68.8 | 51.3 | 85.6 | 76.6 |
| CRAFTQA | LLaMA-3.1-8B | 57.3 | 31.1 | 76.0 | 64.4 |

CRAFTQA 在 GPT-4o 骨干下，TableBench-NR 的 DA 从 TrustUQA 的 29.6% 提升至 51.3%，WikiSQL-E 的 CDA 从 80.1% 提升至 85.6%，表明动态函数生成在复杂推理场景下显著有效。值得注意的是，CRAFTQA-LLaMA-3.1-8B 的 Overall 分数（64.4%）高于 StructGPT-GPT-4o（44.3%），显示小模型结合代码驱动框架可超越大模型的传统方法。

消融实验未单独报告，但论文指出 CRAFT 模块对“Out-of-Predefined”场景的贡献是关键。设计决策上，CRAFT 采用延迟执行策略，确保动态函数生成时能访问前序步骤的实际中间结果 $W_i$，而非仅依赖静态上下文。这一决策避免了因中间结果格式变化导致的函数生成错误，但增加了执行延迟。

评估边界方面，CDA 指标仅针对调用“Out-of-Predefined”函数的子集，可能高估整体泛化能力。论文未报告代码生成失败率及重试次数对延迟的影响，且未提供开源代码，可复现性受限。

## 关联研究分析

从问题动机看，CRAFTQA 与 TrustUQA 共享统一结构化数据问答的目标，但 TrustUQA 强调查询的确定性和可验证性，严格限制在预定义函数集内，而 CRAFTQA 牺牲部分确定性以换取灵活性。这一差异源于任务特性：TrustUQA 面向标准查询，CRAFTQA 面向复杂逻辑推理。CRAFTQA 的动态函数生成是否引入新的安全漏洞或执行不确定性，论文未给出回答。

从方法设计看，CRAFTQA 与 PoT/PAL 同属代码驱动推理路线，但 PoT/PAL 聚焦数值计算，CRAFTQA 扩展至结构化数据查询。PoT 生成代码用于计算，CRAFTQA 生成代码用于数据操作和逻辑控制。这一差异源于数据结构的复杂性：数值计算逻辑相对固定，而结构化数据查询涉及实体对齐、关系遍历等动态操作，需要更灵活的代码生成机制。

## 总结

CRAFTQA 解决的核心矛盾是预定义函数集的封闭性与复杂逻辑推理需求之间的冲突。现有方法如 TrustUQA 因函数集固定而无法处理“Out-of-Predefined”操作，CRAFTQA 通过动态生成自定义函数突破这一限制。该方法在 TableBench-NR 上将 DA 从 29.6% 提升至 51.3%，在 WikiSQL-E 上将 CDA 从 80.1% 提升至 85.6%。其边界在于依赖 LLM 的代码生成能力，且未验证动态生成代码的逻辑正确性。当支持集增大到 5-shot 时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_41964b0b8a71)