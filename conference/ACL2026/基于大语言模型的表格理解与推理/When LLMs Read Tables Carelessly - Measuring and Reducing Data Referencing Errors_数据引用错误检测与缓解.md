# ACL2026最新论文 ｜When LLMs Read Tables Carelessly: Measuring and Reducing Data Referencing Errors ｜数据引用错误检测与缓解

研究机构：美国南加州大学、亚马逊网络服务人工智能

作者：Yuqing Yang、Qi Zhu、Zhen Han 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.32029)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.32029)

> 表格理解任务中，大语言模型（LLM）常因密集相似结构导致数值引用错位或遗漏，即数据引用错误（Data Referencing Errors, DREs），现有评估仅关注最终答案准确率，无法捕捉中间推理步骤的可靠性缺陷。本文提出基于LLM-as-a-Judge的DRE自动检测框架，并训练轻量级Critic模型通过过滤与重采样机制降低DRE发生率。该方法在不修改生成模型权重的前提下提升推理质量，但受限于依赖外部强模型标注且未验证结构表示改进对DRE的协同效应。

## 研究背景

表格问答要求模型准确定位并引用单元格值，但LLM在处理密集相似行/列时易发生引用错位（Incorrect Citation）或遗漏关键行（Omitted Information）。此类错误无法被最终答案准确率完全捕获，例如SciTab任务中65.57%的DRE响应仍得出正确二元判断，暴露了过程级评估的缺失。

现有表格理解研究聚焦于结构表示重构（如TABGR的属性图建模）或推理机制增强（如Table-R1的RLVR训练），但均假设模型能正确解析结构后准确引用数据。Zhang et al. (2025c) 在50个WTQ样本中发现80%以上错误源于定位失败，但缺乏系统性度量。本文切入点在于将DRE定义为独立于结构解析的检索/引用能力缺陷，并建立可自动化的检测与缓解流程。

## 核心方法

### 方法参照系

本文问题对应“推理忠实性审计”路线，标准流程为生成响应→评估最终答案。关键差异在于：本文在生成与评估间插入DRE检测环节，将评估粒度从答案级细化到引用级，且Critic仅判断引用准确性而非答案正确性。

### DRE分类与自动检测

DRE检测需区分两种错误类型：Incorrect Citation指引用不匹配的单个值（如混淆列名），Omitted Information指遗漏必需子集（如跳过某行）。设计动机在于解决人工标注成本高且无法覆盖长响应的问题。采用Sonnet-3.7作为Judge模型，通过提供Ground Truth辅助交叉验证，解决强模型被错误响应误导导致的假阴性问题。检测指标定义为：

$$
\text{DRE Rate} = \frac{|\text{DRE}|}{|\text{Total}|}
$$

其中 $|\text{DRE}|$ 为包含至少一个DRE的响应数。该公式量化了DRE的整体频率，但无法区分错误类型，需结合DRE-in-Incorrect Ratio（错误答案中DRE占比）与Correct-in-DRE Ratio（含DRE但答案正确的占比）进行多维评估。

### 轻量级Critic训练与推理时缓解

Critic训练采用两阶段流程：SFT阶段使用Sonnet-3.7标注的2,000个平衡样本（正/负各1,000）进行格式对齐与启发式迁移；RLVR阶段使用5,712个样本，以验证的二分类标签为奖励信号，不约束CoT格式以增强泛化性。设计动机在于解决大模型Critic的黑盒性与高成本问题，同时避免SFT直接训练导致的输出格式崩溃。推理时缓解通过Critic-based Filtering（从N=8个采样响应中选择DRE最少的子集）与Rejection Sampling（分段重采样直至Critic接受，最大重试N=8）实现。Rejection Sampling的改进价值在于：针对推理模型长响应特性，仅在“Wait”分隔符处分段重采样，避免全响应重新生成，降低计算开销同时防止错误跨段传播。

## 实验评估

实验覆盖WTQ、TableBench、FinQA、SciTab、ToTTo五个数据集，基线包括Qwen3系列（1.7B-8B）、Llama4-Scout、Distill系列及gpt-oss-20b，但未对比TABGR等结构表示SOTA。主结果显示DREs普遍存在：Qwen3-8B在WTQ上DRE Rate为14.04%，即使添加提示词仍为12.50%；Llama4-Scout作为非推理模型DRE Rate高达46.48%。Critic-4B在DRE检测任务上平均F1为78.16%，较未训练基线Qwen3-4B-Instruct（69.51%）提升8.65%。

| 模型 | 数据集 | Accuracy (%) | DRE Rate (%) |
|---|---|---|---|
| Qwen3-8B | WTQ | 77.14 | 14.04 |
| Qwen3-8B | FinQA | 63.21 | 33.57 |
| Llama4-Scout | WTQ | 55.71 | 46.48 |
| gpt-oss-20b | WTQ | 78.38 | 5.71 |

Critic-based Filtering在DRE子集上显著提升准确率：Qwen3-8B在WTQ上从64.59%（平均）提升至73.49%（CF+MV）；Distill-Qwen-7B在TableBench上从55.06%提升至71.65%。Rejection Sampling在DRE子集上最大提升15.27%（Distill-Qwen-7B在TableBench），全数据集上最大提升11.96%。

评估边界：指标未报告置信区间，数值比较需谨慎；Critic训练数据仅来自Qwen3-8B在WTQ训练集上的响应，跨模型泛化性依赖实验验证；代码已开源但超参数与GPU配置未在正文披露。

## 关联研究分析

从问题动机看，TABGR通过属性图结构保留二维拓扑，旨在从源头减少结构丢失导致的引用错误；本文则假设结构解析正确后仍存在引用缺陷，通过事后检测缓解。二者差异根源在于：TABGR针对复杂层级表格的结构保真度，本文针对密集相似表格的检索准确性，任务特性决定了两者的正交性。结构表示改进能否同时降低DRE Rate，论文未给出回答。

从方法设计看，Table-R1使用RLVR优化生成模型的推理策略，奖励信号来自最终答案正确性；本文使用RLVR训练独立Critic，奖励信号来自DRE二分类标签。差异在于：Table-R1将引用准确性内化到生成过程，本文将其外化为独立评估模块。这种解耦设计使Critic可即插即用于任意生成模型，但牺牲了生成模型对引用错误的内生修正能力。

## 总结

本文核心矛盾在于LLM表格推理中过程级引用错误无法被最终答案准确率捕获。切入点在于将DRE定义为独立能力缺陷，通过LLM-as-a-Judge建立自动化检测流程，并训练轻量级Critic实现推理时缓解。方法证明了DREs普遍存在且可缓解：Critic-4B平均F1达78.16%，Rejection Sampling在DRE子集上最大提升15.27%。边界在于Critic训练依赖外部强模型标注，且未验证结构表示改进与DRE检测的协同效应。当支持集从WTQ扩展到TableBench时，Critic-4B的F1是否因表格结构差异而显著下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.32029)