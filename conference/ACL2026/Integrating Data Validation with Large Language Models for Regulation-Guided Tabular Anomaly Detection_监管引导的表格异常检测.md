# ACL2026最新论文 ｜Integrating Data Validation with Large Language Models for Regulation-Guided Tabular Anomaly Detection ｜监管引导的表格异常检测

研究机构：湖南大学、南京大学

作者：Haoliang Huang、Zihuang Cai、Zhuo Tang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_81e0ad159a60)

> 表格数据中的欺诈行为往往不表现为单条记录的统计离群，而是多条记录组合后违反业务逻辑，例如同一患者同日出现在两地。现有基于分布建模或单样本评分的方法无法捕捉这种跨样本违规，导致漏检。本文提出监管引导的表格异常检测（Regulation-guided Tabular Anomaly Detection, RTAD）任务，并设计免训练框架RegValidator，通过大语言模型（Large Language Model, LLM）将监管文本转化为SQL查询，再结合统计规则验证候选异常。该方法在自建数据集上显著优于现有基线，但其性能高度依赖监管文本的覆盖率与SQL生成的准确性，通用性存疑。

## 研究背景

表格异常检测的核心困境在于异常定义的复杂性。传统方法假设异常是单样本偏离正常分布的统计离群点，但在医疗、金融等受监管领域，异常往往由多条记录联合触发。例如，单条“纽约就医”记录在统计上完全正常，但与另一条“同日北京就医”记录组合后，违反了“一人不能同时出现在两地”的监管逻辑。这种跨样本违规无法通过单点评分捕捉，必须引入外部知识约束。

现有表格异常检测路线主要分为两类：一是基于分布建模的深度学习方法，如AnoLLM通过微调LLM计算负对数似然作为异常分数，擅长捕捉统计离群但忽略业务逻辑；二是基于提示工程的零样本方法，如ReTabAD将领域知识注入提示词，但受限于LLM上下文窗口，无法处理大规模数据的全局约束。这两类方法均未能有效整合监管文本中的显式规则，导致在合规性检测任务上表现不佳。本文的切入点在于将监管文本作为先验知识，通过程序化执行（SQL）而非语义推理来定位异常，从而突破上下文窗口限制并实现可解释的合规检测。

## 核心方法

### 方法参照系

表格异常检测的通用流程是学习正常数据分布 $P_{normal}$，计算样本 $x$ 的异常分数 $f(x)$。本文的关键差异在于：异常定义不再仅依赖 $P_{normal}$，而是引入监管规则集 $\mathcal{R}$，异常被定义为违反 $\mathcal{R}$ 中任意规则 $R \in \mathcal{R}$ 的样本组合。这要求方法具备从非结构化文本提取结构化规则，并在大规模数据上执行规则的能力。

### 多智能体监管规则提取与SQL生成

设计动机：直接让LLM判断异常易产生幻觉且无法处理大规模数据，需将语义规则转化为可执行的数据库查询。Ideation Agent从监管文本中提取检测想法 $I$，Query Agent将其转化为SQL查询 $Q$。为处理SQL语法错误与结果规模偏差，引入迭代自校正机制：

$$
Q_i = f_{LLM}^{query}(I, M, Q_{i-1}, H_{i-1}), \quad H_i = f_{review}(Q_i)
$$

其中 $H_i$ 包含执行反馈（语法错误、结果规模是否超出严格/中等/宽松阈值）。该机制通过执行反馈闭环修正查询，确保生成的SQL既能准确定位候选异常，又具备可执行性，解决了LLM直接生成SQL的高错误率问题。

### 预算约束下的异常验证与规则选择

设计动机：SQL查询返回的候选集包含大量误报，需通过统计规则验证其异常性，并在有限误报预算下最大化召回率。Rule Generation Agent为每个想法生成验证规则 $V$，Validation Agent计算候选集与参考集的统计差异（如KL散度）。规则选择被形式化为预算最大覆盖问题：

$$
\max_{V \subseteq \mathcal{R}} \text{Recall}(P(V)) \quad \text{s.t.} \quad \text{FPR}(P(V)) \le \delta
$$

其中 $P(V)$ 为规则集 $V$ 覆盖的异常样本并集，$\delta$ 为误报率预算。由于该问题是NP-hard，采用贪心算法求解，理论上保证 $(1 - \frac{1}{2e})$-近似最优。该设计将模糊的语义验证转化为可量化的统计约束，通过理论保证平衡了召回率与误报率，避免了纯LLM验证的主观性与不可控性。

## 实验评估

实验在三个自建数据集（RTAD-Healthcare, RTAD-FDTD, RTAD-Creditcard）上进行，基线覆盖经典统计（Isolation Forest）、深度学习（AnoLLM, DTE）及LLM方法（ReTabAD）。RegValidator在平均AUC-ROC上比SOTA方法AnoLLM高12.0%，F1-score高19.8%。

| 方法 | RTAD-Healthcare AUC-ROC | RTAD-Healthcare F1 | RTAD-FDTD AUC-ROC | RTAD-FDTD F1 | RTAD-Creditcard AUC-ROC | RTAD-Creditcard F1 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| AnoLLM | 0.544 | 0.576 | 0.870 | 0.793 | 0.649 | 0.033 |
| ReTabAD | 0.489 | 0.590 | 0.601 | 0.595 | 0.766 | 0.184 |
| RegValidator | 0.638 | 0.710 | 0.945 | 0.879 | 0.842 | 0.405 |

消融实验显示，移除数据验证模块后，平均AUC-ROC下降3.3%，F1-score下降5.4%。在RTAD-Creditcard上，无验证模块的F1-score从0.405降至0.339，表明统计验证对高不平衡数据至关重要。

评估边界方面，本文仅使用AUC-ROC和F1-score，未报告推理延迟与GPU内存占用，无法评估实时性。所有LLM步骤使用GPT-4o-mini，但SQL执行依赖数据库环境，未提供端到端耗时。代码已开源，但监管文本的获取依赖人工检索，自动化程度有限。

## 关联研究分析

从问题动机看，RegValidator与AnoLLM的根本差异在于异常定义。AnoLLM假设异常是分布离群，而RegValidator假设异常是规则违规。这一差异源于任务特性：医疗欺诈往往符合统计分布但违反业务逻辑，分布建模方法在此类场景下天然失效。RegValidator通过引入外部监管文本，将检测问题从统计推断转化为逻辑验证，这是其性能优势的核心来源。

从方法设计看，RegValidator与ReTabAD均利用LLM处理语义信息，但ReTabAD依赖上下文窗口内的语义推理，而RegValidator通过SQL执行实现程序化验证。这一设计选择解决了ReTabAD在大规模数据上的扩展性问题，但引入了新的依赖：SQL生成的准确性与数据库架构的兼容性。若监管规则无法转化为SQL（如涉及复杂时序逻辑），方法性能将退化。

## 总结

本文针对表格数据中跨样本违规难以检测的矛盾，提出监管引导的异常检测范式。通过LLM提取规则、SQL执行定位、统计验证过滤的三阶段流程，RegValidator在自建数据集上实现了AUC-ROC 0.808、F1-score 0.665的平均性能，显著优于AnoLLM。其边界在于：监管文本需人工检索且覆盖率有限，SQL生成依赖数据库架构，且未评估实时性。当监管规则无法转化为SQL查询时，该方法的检测能力如何退化，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_81e0ad159a60)