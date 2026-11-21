# ACL-Findings2026最新论文 ｜BOLT: Benchmarking Open-World Learning for Text Classification ｜开放世界文本分类基准与LLM后验评分

研究机构：中国科学院、中国科学院大学

作者：Chuan Qin、Xi Chen、Jinpeng Li 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5bc5e30a56ca)

> 开放世界文本分类（Open-World Text Classification, OTC）旨在让模型在仅见部分已知类别时，既能准确分类已知样本，又能拒绝或发现未知类别。现有评测多局限于单一意图识别数据集且缺乏统一协议，导致方法间无法公平比较，且大语言模型（Large Language Models, LLMs）在其中的潜力未被系统探索。BOLT通过构建涵盖12个数据集、统一已知类别比例（Known Class Ratio, KCR）与标注比例（Labeled Ratio, LAR）的基准，并引入LLM后验评分机制，填补了这一空白。该工作验证了LLM在未知类别检测上的优势，但其对LLM规模效应的非线性发现及纯文本模态的局限，使其结论的普适性仍存疑。

## 研究背景

文本分类长期依赖闭世界假设，即训练时所有类别已知且完全可观测。当面对真实场景中持续涌现的新类别时，这种假设导致模型无法区分分布内（In-Distribution, ID）样本与分布外（Out-of-Distribution, OOD）样本，进而产生错误分类。为解决此问题，开放世界学习范式被引入自然语言处理（Natural Language Processing, NLP），其核心在于打破闭集限制，要求模型在缺乏新类别标注的情况下，具备识别ID样本并处理OOD样本的能力。

OTC主要包含两个子任务：开放集文本分类（Open-Set Text Classification, OSTC）和广义类别发现（Generalized Category Discovery, GCD）。OSTC要求模型在仅使用已知类别标注数据训练后，能正确分类ID输入并拒绝OOD输入；GCD则进一步要求模型利用无标签数据中的聚类结构，发现并区分已知与未知类别。现有研究多集中于意图识别数据集（如Banking, CLINC），且实验协议不一致，例如已知类别比例和标注数据量各异，导致方法间难以公平比较。此外，尽管LLMs在语义理解上表现优异，但其在OTC任务中的角色——是作为判别骨干还是后验评分器——尚未得到系统验证，低资源场景下的表现更是鲜有探索。

## 核心方法

### 统一评测框架与开放世界构建

BOLT将OSTC与GCD整合至单一评测框架，通过KCR和LAR两个参数控制开放程度。KCR将标签空间划分为已知与未知子集，模拟不同开放程度；LAR指定已知类别中标注样本的比例，反映监督信号强弱。这种设计使得不同方法在相同开放条件下可比，解决了以往评测中协议碎片化的问题。

### LLM后验评分机制

传统OSTC方法依赖阈值或能量函数区分ID/OOD，但这类方法在细粒度语义上表现不佳。BOLT引入LLM作为判别骨干，并采用后验评分策略。具体而言，模型微调LLM以输出类别logits，随后使用MaxLogit或Energy等指标计算OOD分数。MaxLogit取最大logit值作为置信度，Energy则基于logits的负和计算能量值。这种设计利用了LLM强大的语义表征能力，使OOD检测不再依赖浅层特征距离，而是基于深层语义一致性。

$$
S_{\text{MaxLogit}}(x) = \max_{k \in Y_k} \log p(y=k|x)
$$

该公式表明，MaxLogit通过选取已知类别中概率最高的logit值作为ID置信度，若该值低于阈值则判定为OOD。

$$
S_{\text{Energy}}(x) = -\log \sum_{k \in Y_k} \exp(\log p(y=k|x))
$$

Energy函数通过计算已知类别概率分布的负对数和，反映样本与已知类别集合的整体偏离程度，值越低表示越可能为ID。

### GCD中的LLM增强聚类

在GCD任务中，伪标签噪声是主要瓶颈。BOLT对比了传统聚类方法（如DPN, TAN）与LLM增强方法（如LOOP, ALUP）。LOOP利用LLM细化邻居关系，ALUP则通过LLM生成示例进行对比。这些方法将LLM的语义先验注入聚类过程，缓解了纯几何距离在短文本或低资源场景下的失效问题，提升了新类别发现的准确性。

## 实验评估

实验在12个数据集上进行，涵盖主题分类、意图检测和本体分类三大场景，语言包括英语、中文及多语言。基线覆盖传统方法（DOC, DeepUnk）、PLM方法（ADB, KNNCon, DyEn）及LLM增强方法（LOOP, ALUP）。OSTC任务中，LLM-MaxLogit在平均N-F1上达到74.05，显著优于最强PLM基线KNNCon的58.27，表明LLM后验评分在未知类别检测上具有显著优势。然而，在K-F1上，PLM方法如ADB（65.61）和KNNCon（69.34）仍优于LLM-MaxLogit（56.10），说明LLM在已知类别分类上并未全面超越PLM。

| 方法 | K-F1 (Avg) | N-F1 (Avg) |
| :--- | :--- | :--- |
| KNNCon | 69.34 | 58.27 |
| ADB | 65.61 | 64.09 |
| LLM-MaxLogit | 56.10 | 74.05 |
| LLM-Energy | 59.83 | 63.77 |

GCD任务中，LLM增强方法ALUP和LOOP在短文本意图检测数据集（如CLINC, BANKING）上表现优于PLM方法，但在长文本主题分类数据集（如20NG, DBPedia）上，PLM方法TAN和DPN仍具竞争力。消融实验显示，LLM规模并非单调提升性能：Qwen2.5-3B在平均K-F1（52.89）上优于32B（51.82），而32B在N-F1（65.86）上略优于3B（65.60），7B模型则在多数指标上表现最差。这表明LLM规模效应在OTC任务中存在非线性关系，中等规模模型可能因过拟合或语义覆盖不足而表现不佳。

评估协议采用5折交叉验证，KCR设为{0.25, 0.50, 0.75}，LAR设为{0.10, 0.50, 1.00}。代码与数据已开源，但论文未报告计算开销细节，仅提及LLM增强方法训练时间显著长于PLM方法（如LOOP需1小时22分20秒，而SDC仅需11分20秒）。指标完备性方面，OSTC使用K-F1和N-F1，GCD使用K-ACC和N-ACC，但未提供置信区间，数值比较需谨慎。

## 关联研究分析

从问题动机看，BOLT与视觉领域的开放词汇检测（OVOD）共享“已知/未知”区分的核心思想，但模态与任务形式不同。OVOD依赖视觉-语言模型（如CLIP）的跨模态对齐，而BOLT仅利用LLM的文本语义能力。这种差异源于任务特性：文本分类无需视觉特征，LLM的纯文本语义理解已足以支撑OOD检测。然而，BOLT未探索视觉-语言对齐在文本任务中的潜在增益，例如结合图像上下文是否有助于提升短文本的OOD检测精度，这一盲区限制了其结论在跨模态场景的适用性。

从方法设计看，BOLT的LLM后验评分机制与视觉领域的能量函数（Energy-based OOD Detection）原理相似，均基于logits分布计算OOD分数。但BOLT的MaxLogit和Energy实现更简洁，未引入额外的温度缩放或校准步骤。相比之下，视觉领域常用温度缩放（Temperature Scaling）来优化logits分布，而BOLT未报告此类校准对性能的影响。此外，BOLT的GCD任务中LLM增强方法（如LOOP）依赖LLM生成伪标签，这与视觉领域基于原型聚类的GCD方法（如DPN）形成对比。前者利用LLM的生成能力细化语义边界，后者依赖几何距离聚类，两者在短文本与长文本上的表现差异揭示了语义先验与几何结构在不同文本长度下的互补性。

## 总结

BOLT旨在解决开放世界文本分类中评测协议碎片化及LLM潜力未系统探索的问题。通过构建统一基准并引入LLM后验评分，BOLT证明了LLM在未知类别检测上的优势（N-F1 74.05 vs 58.27），但其在已知类别分类上未全面超越PLM方法。该工作的边界在于仅关注纯文本模态，未探索跨模态对齐的增益，且LLM规模效应的非线性关系揭示了中等规模模型在OTC任务中的潜在劣势。当支持集增大或文本长度变化时，LLM后验评分与PLM判别方法的性能交叉点是否稳定，论文未给出明确回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_5bc5e30a56ca)