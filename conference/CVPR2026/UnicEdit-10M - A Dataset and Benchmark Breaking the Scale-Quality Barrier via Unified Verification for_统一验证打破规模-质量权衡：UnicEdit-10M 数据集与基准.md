# CVPR2026最新论文 ｜UnicEdit-10M: A Dataset and Benchmark Breaking the Scale-Quality Barrier via Unified Verification for Reasoning-Enriched Edits ｜统一验证打破规模-质量权衡：UnicEdit-10M 数据集与基准

研究机构：浙江大学、上海交通大学

作者：Keming Ye、Zhipeng Huang、Canmiao Fu 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.02790)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.02790)

> 指令式图像编辑（IBIE）面临数据规模与质量的根本矛盾：人工标注数据保真度高但规模受限，自动化流水线规模大但引入系统性噪声。现有方案卡在多工具链误差传播与后验证维度单一两个瓶颈上，导致开源模型与闭源模型差距持续拉大。本文切入点是用端到端编辑模型替代多工具链，并训练一个7B双任务专家模型统一执行失败过滤与指令重述，从而在10M规模下维持高数据质量。该工作提供了可复用的数据构建管道与更全面的复杂编辑基准，但其评估指标对风格迁移等任务的适用性存疑，且未验证该数据直接训练模型后的性能增益。

## 研究背景

当自动化数据流水线依赖多个视觉模块串联时，早期阶段的微小定位或语义错误会在下游编辑步骤中被放大，形成难以追溯的伪影，这一现象称为误差传播。误差传播导致合成数据中指令与图像不匹配的比例显著上升，而传统后验证往往只检查图像是否发生变化，无法捕捉语义层面的错位。要解决这一问题，需要一种既能高效过滤失败案例，又能修正指令语义的验证机制，这构成了大规模高质量编辑数据构建的核心技术挑战。

指令式图像编辑领域长期受困于数据瓶颈。MagicBrush等人工标注数据集保真度高但仅约10K规模，而UltraEdit、ImgEdit等自动化流水线虽达百万级，却因多工具链架构引入系统性噪声。现有基准如GEdit-Bench侧重基础编辑任务，对空间推理、多对象协调等复杂任务覆盖稀疏，且VLM评估指标对非编辑区域的意外变化不敏感。本文针对这一双重缺口，提出统一验证管道与专用基准，旨在同时解决数据质量与评估盲区问题。

## 核心方法

### 方法参照系

本文问题属于大规模编辑数据构建与验证范畴。标准流程为：指令生成→图像编辑→后验证。与InstructPix2Pix等早期方法不同，本文不依赖多工具链拼接，而是采用端到端编辑模型，并将后验证从单一失败检测扩展为失败过滤与指令重述的双任务统一框架。

### 端到端编辑与统一后验证

传统流水线使用多个视觉模块串联，误差在模块间累积。本文改用FLUX.1-Kontext和Qwen-Image-Edit作为端到端编辑模型，避免模块间误差传播。后验证阶段由Qwen-Verify执行，该模型基于Qwen2.5-VL-7B训练，通过链式推理同时完成失败检测与指令重述。对于每个三元组，模型首先描述原图与编辑图的细粒度差异，判断是否发生有效编辑，若有效则重写指令以精确匹配视觉修改。这一设计解决了传统后验证只检测“是否变化”而忽略“变化是否正确”的局限，确保保留的数据在语义上对齐。

### D²PO 偏好对齐训练

SFT阶段赋予模型区分失败编辑与生成准确指令的基础能力，但对指令质量的细微差异不敏感。为提升模型对幻觉指令的识别能力，本文引入Differential Direct Preference Optimization (D²PO)。D²PO将视觉差分上下文 $c_v = V(I_o, I_e)$ 作为条件，其中 $V$ 是处理图像对的视觉编码器，$c_v$ 封装了从原图 $I_o$ 到编辑图 $I_e$ 的变换信息。偏好优化目标定义为：

$$ \mathcal{L}_{D^2PO} = -\mathbb{E}_{(I_o, I_e, p_w, p_l) \sim \mathcal{D}} \left[ \log \sigma \left( \beta \log \frac{\pi_\theta(p_w | c_v)}{\pi_{ref}(p_w | c_v)} - \beta \log \frac{\pi_\theta(p_l | c_v)}{\pi_{ref}(p_l | c_v)} \right) \right] $$

其中 $\pi_\theta$ 是可训练策略，$\pi_{ref}$ 是冻结的SFT副本，$\beta$ 控制偏离程度，$p_w$ 和 $p_l$ 分别是偏好（修正后）和拒绝（幻觉）指令。该公式通过最大化偏好指令与拒绝指令在视觉差分条件下的策略优势差，使模型学会区分语义细微差异，从而降低幻觉率。

## 实验评估

实验在UnicBench和VIEScore协议上进行，基线覆盖InstructPix2Pix、MagicBrush、FLUX.1-Kontext、Qwen-Image-Edit等开源模型及GPT-4o、Nano Banana等闭源模型。数据集质量对比中，UnicEdit-10M在VIEScore Overall得分8.0768，高于GPT-Image-Edit-1.5M的7.7451和SEED-Data-Edit的5.0043，面部一致性得分0.89显著优于GPT-Image-Edit-1.5M的0.3025。

| 数据集 | VIEScore SC | VIEScore PQ | VIEScore Overall | Aesthetic Source | Aesthetic Target |
| :--- | :--- | :--- | :--- | :--- | :--- |
| SEED-Data-Edit | 5.7884 | 6.3430 | 5.0043 | 5.72 | 5.74 |
| GPT-Image-Edit-1.5M | 8.6780 | 7.1560 | 7.7451 | 7.52 | 7.54 |
| UnicEdit-10M | 8.4500 | 8.1950 | 8.0768 | 8.00 | 7.76 |

Qwen-Verify在Normal、No Edit、Hallucination三类任务上的准确率分别为6.32、9.80、6.22，全面超越Qwen2.5-VL-72B的5.25、9.60、6.12。D²PO训练后，模型在Hallucination任务上的准确率从SFT阶段的5.47提升至6.22，表明偏好对齐对幻觉抑制有显著贡献。

| 模型 | Normal Acc. | No Edit Acc. | Hallucination Acc. |
| :--- | :--- | :--- | :--- |
| Qwen2.5-VL-7B | 4.39 | 4.84 | 3.95 |
| Qwen2.5-VL-72B | 5.25 | 9.60 | 6.12 |
| Qwen-Verify | 6.32 | 9.80 | 6.22 |

评估边界方面，UnicBench引入Non-edit Consistency (NC)和Reasoning Accuracy (RA)指标，但NC在风格迁移任务中可能将全局风格变化误判为非编辑区域意外修改。RA依赖VLM推导预期结果，可能受评估者偏差影响。论文未报告训练Qwen-Verify的GPU资源与超参数细节，可复现性受限。

## 关联研究分析

从问题动机看，本文与Step1X-Edit同属自构建高质量数据路线，但Step1X-Edit侧重模型微调，本文聚焦数据管道本身。关键差异在于验证机制：Step1X-Edit依赖人工标注或简单过滤，本文用7B专家模型统一执行过滤与重述。这一差异源于任务特性：Step1X-Edit数据规模较小，人工验证可行；本文10M规模下，人工验证成本不可承受，必须自动化。但自动化验证的可靠性是否随规模扩大而下降，论文未给出回答。

从方法设计看，本文与GPT-Image-Edit-1.5M同用指令重述提升数据质量，但GPT-Image-Edit-1.5M依赖GPT-4o API，成本高且无法本地部署。本文用Qwen-Verify替代，计算成本大幅降低。然而，Qwen-Verify在Hallucination任务上的准确率仅6.22，低于Qwen2.5-VL-72B的6.12仅0.10个点，提升幅度有限。这暗示7B模型在细粒度语义判断上仍有瓶颈，D²PO的增益可能受限于基础模型容量。

## 总结

本文要解决的核心矛盾是编辑数据规模与质量的权衡。现有方法因多工具链误差传播和单一后验证无法在大规模下维持质量，本文凭端到端编辑模型与统一双任务验证管道突破这一瓶颈。通过Qwen-Verify，本文在10M规模下实现VIEScore Overall 8.0768，面部一致性0.89，显著优于现有开源数据集。但论文未验证用UnicEdit-10M训练模型后的编辑性能增益，且Qwen-Verify在幻觉检测上的准确率提升有限。当数据规模进一步扩大时，7B验证模型的幻觉率是否会随规模增长而上升，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.02790)