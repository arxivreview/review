# ACL2026最新论文 ｜CT-FineBench: A Diagnostic Fidelity Benchmark for Fine-Grained Evaluation of CT Report Generation ｜CT-FineBench：基于细粒度属性问答的CT报告评估基准

研究机构：阿里巴巴集团、复旦大学

作者：Ruifeng Yuan、Wanxing Chang、Weiwei Cao 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.24001)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.24001)

> 放射学报告生成（Radiology Report Generation, RRG）的评估长期受困于词汇重叠指标与临床事实脱节的矛盾。现有实体匹配或大语言模型整体打分方法无法捕捉CT报告中病灶大小、位置等细粒度属性的错误，导致“语言流畅但临床错误”的报告获得高分。本文提出CT-FineBench，将评估重构为针对临床属性的问答（QA）事实核查任务，通过属性级答案比对量化报告准确性。该基准在CT-RATE上实现了与专家判断0.622的Pearson相关性，显著优于现有指标，但其数值误差阈值的临床验证缺失及跨模态泛化能力仍存疑。

## 研究背景

CT报告的信息密度远超胸部X光，单个病灶的位置、形态或严重度描述错误即可导致误诊。这种对诊断保真度的严苛要求，使得传统自然语言生成（NLG）中基于n-gram重叠的BLEU或ROUGE指标完全失效，因为它们无法区分“左肺上叶”与“左肺下叶”的临床差异。即便引入基于嵌入相似度的BERTScore，其语义对齐机制仍缺乏医学先验知识，无法识别关键临床信息的缺失或错误。

当前评估路线分为两类：实体级指标（如RadGraph、RaTEScore）通过提取解剖结构和发现实体计算F1分数，但受限于粗粒度实体类型，无法覆盖密度、边缘等细粒度属性；大语言模型（LLM）作为裁判（如GREEN）虽能捕捉语义错误，但其黑盒特性导致评估过程不可解释，且缺乏统一的医学评估标准，判断结果具有不可预测性。CT-FineBench的切入点在于：将模糊的报告整体评估转化为可验证的属性级事实核查，通过结构化QA对将临床知识显式嵌入评估流程，从而在保持可解释性的同时实现细粒度错误检测。

## 核心方法

### 方法参照系

现有CT报告评估遵循“文本相似度→实体匹配→LLM整体判断”的演进路径。本文问题与该通用流程的关键差异在于：评估对象从报告整体或实体存在性，下沉至实体的细粒度临床属性（如大小、位置、密度），且评估机制从相似度计算或整体打分，转变为基于属性的问答事实核查。

### 属性定义与QA构建

属性定义阶段通过命名实体识别（NER）从参考报告中提取（发现，属性，内容）三元组，经频率阈值过滤（阈值设为50）后由4名标注员进行临床相关性筛选、属性拆分、同义合并及注释，形成层级化属性模式。QA构建阶段利用Qwen3-Max将参考报告中的发现-属性对转化为问答对，仅针对阳性发现生成问题，若报告未提及某属性则移除对应QA对。该设计解决了实体级指标忽略细粒度属性的失效，将评估粒度从“是否存在肺结节”细化至“肺结节直径是否为12mm”。

$$
D_{QA} = \{(q_i, a_i)\}_{i=1}^{N}, \quad q_i = \text{Query}(\text{finding}_j, \text{attribute}_k), \quad a_i = \text{Extract}(\text{report}, \text{finding}_j, \text{attribute}_k)
$$

该公式表示QA数据集由N个问答对组成，每个问题针对特定发现的特定属性生成，答案从参考报告中提取，确保每个QA对对应一个可验证的临床事实。

### 属性感知答案比对

在线评估阶段，QA模块从候选报告中提取答案，若属性未提及则输出[NULL]。答案比对模块根据属性类型采用差异化评分策略：对于位置/分类属性，同义词精确匹配得1.0分，部分正确或过度指定得0.5分，错误得0分；对于数值属性，解析并标准化数值与单位后，相对误差<10%得1.0分，10%-30%得0.5分，≥30%得0分；[NULL]视为漏报错误得0分。最终分数为所有QA对得分的平均值。该设计解决了LLM整体打分不可解释的失效，通过类型感知的分级评分实现细粒度错误的精确定位。

$$
\text{Score}(\hat{x}, x) = \frac{1}{N} \sum_{i=1}^{N} \phi_{\text{Compare}}(\hat{a}_i, a_i), \quad \phi_{\text{Compare}}(\hat{a}_i, a_i) = \begin{cases} 1.0 & \text{if } \text{err} < 10\% \text{ (numeric)} \text{ or } \text{exact match} \text{ (categorical)} \\ 0.5 & \text{if } 10\% \le \text{err} < 30\% \text{ (numeric)} \text{ or } \text{partial match} \text{ (categorical)} \\ 0 & \text{otherwise or } \hat{a}_i = [\text{NULL}] \end{cases}
$$

该公式表示最终评估分数为所有QA对比较得分的平均值，比较函数根据属性类型（数值/分类）和答案匹配程度（精确/部分/错误）分配0、0.5或1分，数值属性的误差阈值（10%/30%）为启发式设计，可通过修改提示词调整。

## 实验评估

实验在CT-RATE（1564测试报告）和Merlin（5082测试报告）上进行，对比基线覆盖词汇重叠（BLEU-2, ROUGE-L）、嵌入相似度（BERTScore）、实体匹配（RadGraph, RaTEScore）及LLM裁判（GREEN）四类路线，未包含CheXbert（仅适用于胸片）。主实验结果显示，CT-FineBench在CT-RATE上与人类专家判断的Pearson相关性达0.622，显著高于RaTEScore（0.521）和GREEN（0.158）；在Merlin上Pearson相关性为0.369，高于RaTEScore（0.334）和GREEN（0.311）。

| 数据集 | 指标 | BLEU-2 | ROUGE-L | BERTScore | RadGraph | RaTEScore | GREEN | CT-FineBench |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| CT-RATE | Pearson τ | 0.495 | 0.353 | 0.479 | 0.170 | 0.521 | 0.158 | **0.622** |
| CT-RATE | Kendall τ | 0.262 | 0.163 | 0.137 | 0.171 | 0.320 | 0.063 | **0.378** |
| Merlin | Pearson τ | 0.168 | 0.124 | 0.114 | 0.124 | 0.334 | 0.311 | **0.369** |
| Merlin | Kendall τ | 0.089 | 0.070 | 0.097 | 0.097 | 0.227 | 0.179 | **0.251** |

敏感性分析表明，CT-FineBench是唯一在改写报告（-pos）上保持高分（CT-RATE 74.5，Merlin 86.9）且在对抗报告（-neg）上显著降分（CT-RATE 39.1，Merlin 45.6）的指标，而BLEU-2和ROUGE-L呈现相反趋势，RadGraph和RaTEScore对两类报告得分相近，证实了CT-FineBench对细粒度临床错误的敏感性。消融实验显示，使用Qwen3-32b替代Qwen3-Max时，CT-RATE上Pearson相关性从0.622降至0.521，Merlin上从0.369降至0.334，但绝对分数接近（CT-RATE 15.9 vs 15.8，Merlin 22.9 vs 22.4），表明较小模型可维持评估质量。

评估边界方面，数值误差阈值（10%/30%）为启发式设计，未经临床专家验证；评估协议仅覆盖CT模态，未测试MRI等其他影像；代码未公开，但提供了CT-FineData（439,665 QA对）作为训练语料，可复现性受限于Qwen3-Max的API访问。

## 关联研究分析

从问题动机看，CT-FineBench与RadGraph的核心差异在于评估粒度：RadGraph关注实体存在性及关系正确性，而CT-FineBench聚焦实体属性的细粒度值。这一差异源于CT报告的信息密度远超胸片，实体存在性正确但属性错误（如结节大小误报）在CT中更具临床危害。RadGraph的粗粒度实体类型无法覆盖此类错误，而CT-FineBench通过属性级QA实现了细粒度检测。然而，CT-FineBench的属性定义依赖人工标注和LLM辅助，其属性模式的泛化性是否足以覆盖所有CT发现类型，论文未给出系统性验证。

从方法设计看，CT-FineBench与GREEN的差异在于评估机制的可解释性：GREEN使用LLM整体判断并解释错误，但判断过程为黑盒；CT-FineBench通过结构化QA将评估分解为可验证的事实核查步骤，每个QA对的得分均可追溯至具体属性。这一设计解决了LLM裁判不可预测性的问题，但引入了QA模块的依赖：若QA模块未能从候选报告中正确提取答案（如报告表述模糊），评估分数将产生偏差。论文未分析QA模块的提取错误率对最终评估分数的影响，这一潜在偏差在临床部署中可能成为新的风险点。

## 总结

CT-FineBench要解决的核心矛盾是CT报告评估中细粒度临床属性错误检测的缺失。现有实体级指标和LLM整体打分方法无法捕捉病灶大小、位置等属性的错误，而CT-FineBench通过将评估重构为属性级QA事实核查，实现了细粒度错误的可解释检测。该基准在CT-RATE上实现了与专家判断0.622的Pearson相关性，显著优于RaTEScore（0.521）和GREEN（0.158），并在敏感性分析中证实了对细粒度错误的检测能力。其边界在于数值误差阈值的启发式设计未经临床验证，且评估协议仅覆盖CT模态。当属性定义从胸部CT扩展至腹部CT时，属性模式的覆盖率是否足以捕捉所有临床关键属性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.24001)