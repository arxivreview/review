# CVPR2026最新论文 ｜SALMUBench: A Benchmark for Sensitive Association-Level Multimodal Unlearning ｜敏感关联级多模态遗忘基准

作者：Cai Selvas-Sala、Lei Kang、Lluis Gomez

论文原文见 [arXiv](https://arxiv.org/abs/2603.26316)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.26316)

> 多模态嵌入模型在训练过程中会记忆敏感个人信息，但现有遗忘方法仅能抑制输出层预测，无法区分“有效遗忘”与“过泛化损害”。本文切入点在于构建首个针对CLIP类对比学习模型的关联级遗忘评估基准，通过从预训练两个大规模模型（Compromised与Clean）并设计结构化保留集，实现细粒度失效诊断。其价值在于揭示了当前方法无法同时满足遗忘有效性与效用保留的根本缺陷，但合成数据的生态效度仍存疑。

## 研究背景

当CLIP模型从网络语料中训练时，其对比学习机制会将人脸图像与电话号码、邮箱等敏感属性绑定，形成难以通过简单微调移除的语义关联。这种记忆并非显式存储，而是嵌入在图像与文本编码器的共享表示空间中，导致输出层准确率下降并不等同于内部知识被清除。要验证遗忘是否彻底，必须引入表示层探针或重构攻击，但现有基准缺乏针对嵌入空间关联强度的量化协议，使得评估停留在“是否还能检索到”的粗粒度层面。

机器遗忘领域长期以重训为金标准，但大规模模型的全量重训成本高昂，近似遗忘方法成为主流。然而，针对多模态嵌入模型的遗忘研究相对滞后，现有基准如TOFU、FIUBench主要聚焦于生成式多模态大语言模型（MLLM）的视觉问答任务，且通过微调注入敏感知识，难以隔离预训练工件对遗忘效果的影响。本文针对这一空白，提出SALMUBench，专门评估CLIP类模型在“被遗忘权”场景下的关联级遗忘能力，通过从预训练两个大规模模型（Compromised与Clean）并设计结构化保留集，实现细粒度失效诊断。

## 核心方法

### 方法参照系

本文问题属于多模态机器遗忘的评估体系构建，而非具体遗忘算法设计。与单模态遗忘基准（如CIFAR-10上的类别级遗忘）不同，本文聚焦于对比学习嵌入空间中的关联级遗忘，核心差异在于需同时评估图像-文本对的语义关联强度与跨身份/跨关联的副作用，而非仅关注分类准确率或检索命中率。

### 合成数据构建与模型预训练

SALMUBench的核心创新在于构建一个可控的、从预训练的双模型环境，以隔离遗忘效果与预训练工件。数据构建遵循五阶段流水线：从SFHQ数据集选取1,000张人脸作为身份锚点，使用IP-Adapter-FaceID Plus生成约100张/人的图像，经CLIP过滤后保留774个连贯身份，为每个身份分配唯一PII属性（姓名、电话、邮箱等），最后通过LLM对60K图像进行多样化标题改写。关键设计是训练两个ViT/B-16 CLIP模型：Clean模型仅在400M保留集上训练，Compromised模型在保留集+60K敏感集上训练，两者使用相同随机种子和32个epoch。这一设计确保了任何行为差异 solely 归因于敏感数据，而非优化器状态或预训练偏差。

$$
\mathcal{L}_{\text{CLIP}} = -\frac{1}{N} \sum_{i=1}^{N} \log \frac{\exp(\text{sim}(x_i, t_i) / \tau)}{\sum_{j=1}^{N} \exp(\text{sim}(x_i, t_j) / \tau)}
$$

该公式为CLIP的对比损失，其中$\text{sim}$为余弦相似度，$\tau$为温度参数。Clean与Compromised模型均最小化此损失，但Compromised模型额外拟合敏感关联，导致其在敏感集上的余弦相似度显著高于Clean模型（见图5），为遗忘评估提供了明确的“污染”基线。

### 结构化保留集与失效诊断协议

本文的另一核心创新是引入holdout identity和holdout association两个结构化保留集，以诊断过泛化失效。敏感集被划分为两个387人的组：一组用于身份级遗忘（forget identity），另一组用于关联级遗忘（forget association）。forget set包含身份级组中一半人的所有关联，以及关联级组中每人50%的关联。holdout identity包含身份级组中另一半人的所有关联，用于检测跨身份副作用；holdout association包含关联级组中未遗忘的50%关联，用于检测同身份内跨关联副作用。评估协议基于两大支柱：遗忘有效性（RetFail、AssocStr、ACS）和效用影响（GenKnow、InterIdSim、IntraIdSim、VisIdInt、FragSim）。

$$
\text{RetFail} = \frac{1}{|F|} \sum_{i \in F} \frac{1}{\text{rank}(x_i, t_i)}
$$

该公式计算检索失败率（RetFail），其中$F$为forget set，$\text{rank}$为正确标题在2001个候选中的排名。RetFail越低表示遗忘越有效，但需结合holdout集指标判断是否过泛化。例如，若RetFail接近Clean模型目标值（0.001）但InterIdSim显著低于目标值（0.321），则表明方法擦除了无关身份的关联，属于过泛化失效。

## 实验评估

实验在SALMUBench上评估9种遗忘方法，计算预算为5×。基线覆盖梯度上升（Negative Gradient）、直接相似度最小化、微调（Generic/Shuffled Captions）、蒸馏（DELETE、CLIPErase）等主流路线，但缺失SISA等精确遗忘方法（因计算不可行）。主结果显示，DELETE和CLIPErase在RetFail上达到目标值0.001，但InterIdSim和IntraIdSim降至0.024，远低于目标值0.321，证实过泛化；Shuffled Captions和Direct Similarity Minimization虽降低RetFail，但GenKnow从0.638降至0.548和0.615，属于灾难性损害。

| 方法 | RetFail | AssocStr | GenKnow | InterIdSim | IntraIdSim |
| --- | --- | --- | --- | --- | --- |
| Target Scores | 0.001 | 0.142 | 0.638 | 0.321 | 0.321 |
| DELETE | 0.001 | 0.022 | 0.632 | 0.023 | 0.023 |
| CLIPErase | 0.001 | 0.023 | 0.634 | 0.024 | 0.024 |
| Shuffled Captions | 0.004 | 0.212 | 0.548 | 0.212 | 0.212 |
| Direct Sim. Min. | 0.001 | -0.429 | 0.615 | -0.420 | -0.425 |

消融实验显示，当AssocStr低于Clean模型基线0.142时，方法会过度纠正并擦除未遗忘关联，这一阈值效应揭示了过泛化的机制。评估边界方面，合成人脸与真实人脸的KS检验p>0.05，但样本量仅100张，统计功效有限；代码和模型已公开，但训练需128块H100 GPU约65小时，复现成本高。

## 关联研究分析

从问题动机看，SALMUBench与TOFU、FIUBench等生成式MLLM基准的根本差异在于评估对象：本文针对嵌入空间的检索任务，而非生成式问答。TOFU通过微调注入虚构作者知识，评估VQA准确率；SALMUBench通过从预训练Compromised模型，评估检索失败率。这一差异源于任务特性：嵌入模型的遗忘需切断图像-文本对的语义关联，而非抑制生成概率，因此RetFail比VQA准确率更直接反映遗忘效果。但RetFail能否完全替代成员推断攻击（MIA）评估隐私风险，论文未给出回答。

从方法设计看，SALMUBench与MultiDelete、CLIPErase等CLIP遗忘方法的关键差异在于评估粒度：后者仅评估forget set和retain set的准确率，缺乏holdout集检测副作用。MultiDelete的三目标损失（解耦、保留单模态、保持对齐）在SALMUBench的细粒度评估下暴露出对关联级遗忘的不足：其RetFail虽低，但InterIdSim显著下降，表明其擦除了无关身份的关联。这一差异源于任务特性：MultiDelete设计于类别级遗忘，未考虑同身份内跨关联的副作用，而SALMUBench的holdout association集专门检测此问题。

## 总结

SALMUBench要解决的核心矛盾是多模态嵌入模型遗忘评估的粗粒度问题，现有方法无法区分有效遗忘与过泛化损害。本文抓住的切入点是构建从预训练的双模型环境和结构化保留集，通过隔离预训练工件和细粒度副作用检测，实现失效诊断。本文证明了DELETE和CLIPErase在RetFail上达到目标值0.001，但InterIdSim降至0.024，证实过泛化；Shuffled Captions的GenKnow降至0.548，证实灾难性损害。本文的边界在于合成人脸的生态效度依赖KS检验，样本量仅100张，统计功效有限；评估协议未包含成员推断攻击，隐私风险量化不完整。当holdout集规模扩大时，过泛化检测的统计显著性是否提升，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.26316)