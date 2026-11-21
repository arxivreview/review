# CVPR2026最新论文 ｜From Intuition to Investigation: A Tool-Augmented Reasoning MLLM Framework for Generalizable Face Anti-Spoofing ｜工具增强推理面部反欺骗

研究机构：中国科学院

作者：Haoyuan Zhang、Keyao Wang、Guosheng Zhang 等 14 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.01038)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.01038)

> 面部反欺骗（Face Anti-Spoofing, FAS）旨在区分真实人脸与打印、重放或3D面具等物理呈现攻击，其核心挑战在于跨域泛化能力不足。现有基于多模态大语言模型（MLLMs）的方法虽提供了可解释性，但受限于对低层视觉特征的“盲视”，难以捕捉细微伪造伪影。本文提出TAR-FAS框架，通过让MLLM在思维链中自适应调用外部视觉工具（如LBP、FFT）进行细粒度调查，弥补语义直觉的缺陷。该框架在One-to-Eleven协议下显著提升了跨域检测精度，但其推理延迟与工具依赖的泛化边界尚存疑。

## 研究背景

面部反欺骗系统部署于支付与身份验证场景，常面临训练域与测试域在传感器、光照及攻击类型上的分布偏移。这种偏移导致传统深度分类器性能衰退，而近期引入的CLIP等基础模型虽改善了泛化，但多模态大语言模型（MLLMs）在感知低层视觉特征时存在固有缺陷。MLLMs倾向于关注粗粒度语义线索（如屏幕边框），却忽略皮肤纹理不规则性或频域周期性等细粒度伪造痕迹，这限制了其在高保真攻击下的鲁棒性。

早期FAS研究依赖手工特征（如LBP、HOG）与浅层分类器，虽在域内有效，但难以应对开放世界部署。随着深度学习普及，卷积神经网络（CNN）提升了域内精度，但跨域瓶颈迫使领域转向域泛化（Domain Generalization, DG）研究。2021年后，CLIP与DINOv2等基础模型的引入成为关键转折，通过参数高效微调（Parameter-Efficient Fine-Tuning, PEFT）增强了对未见攻击的鲁棒性。然而，现有MLLM-FAS方法（如I-FAS）仅生成单句解释，未能引导模型主动探索隐藏视觉线索。本文切入点在于利用MLLM的工具调用能力，将传统视觉算子封装为外部工具，实现从“被动感知”到“主动调查”的范式转变。

## 核心方法

### 方法参照系

标准MLLM-FAS流程为“图像输入→语义编码→单句分类/解释”，其关键差异在于缺乏对低层视觉证据的主动获取机制。本文问题与该通用流程的关键差异在于：模型需在推理过程中动态决定调用何种视觉工具，并基于工具输出进行多轮迭代判断，而非一次性静态分类。

### 工具增强数据标注与CoT-VT范式

设计动机在于解决MLLM对低层伪影的盲视，通过显式引入传统FAS中验证有效的视觉算子作为外部工具。本文构建ToolFAS-16K数据集，包含多轮工具调用推理轨迹。标注流程中，引入专家模型引导机制（Expert-Model-Guided Mechanism），为每个工具输出提供置信度指导，确保标注可靠性。形式化地，对于工具 $T_k$ 的输出 $T_k(I)$，专家网络 $E_k$ 计算伪造痕迹存在概率 $p_k$：

$$ p_k = E_k(T_k(I)) $$

该概率转化为文本指导 $G[T_k(I)]$（如“专家预测87%存在伪造痕迹”），注入提示词以约束通用MLLM的推理路径。此机制使模型在生成推理链时，能结合专家置信度与视觉证据，避免幻觉导致的错误工具选择。

### DT-GRPO训练策略

设计动机在于使模型自主学会高效、多样的工具使用，而非依赖固定规则。本文提出Diverse-Tool Group Relative Policy Optimization (DT-GRPO)，通过工具多样性奖励函数鼓励模型探索不同工具组合。训练分为三阶段：FAS知识迁移（KT）、工具调用格式注入（FI）及DT-GRPO强化学习（RL）。DT-GRPO的目标函数包含快奖励（Fast Reward）、推理奖励（Reasoning Reward）及工具奖励（Tool Reward）：

$$ \mathcal{L}_{DT-GRPO} = \beta_{fast} R_{fast} + \beta_{rsn} R_{rsn} + \beta_{tool} R_{tool} $$

其中 $\beta_{fast}=0.1, \beta_{rsn}=0.5, \beta_{tool}=0.4$。工具奖励 $R_{tool}$ 基于工具使用的多样性与有效性，促使模型在仅凭查询-标签对的情况下，自主学习何时调用LBP、FFT或ZoomIn等工具，从而在未见攻击类型上实现自适应细粒度调查。

## 实验评估

实验采用One-to-Eleven协议，以CelebA-Spoof为源域，测试11个目标域（含SIW、CASIA-MFSD等）。基线覆盖ViT-L、FLIP及I-FAS，但缺失最新DG方法（如DINOv2-based FAS）及纯CNN基线（如CDCN++）的对比，限制了与领域SOTA的绝对精度比较。

| 方法 | 平均HTER(%) | 平均AUC | CASIA-MFSD HTER(%) | SIW HTER(%) |
| :--- | :--- | :--- | :--- | :--- |
| I-FAS | 11.30 | 93.71 | 1.11 | 4.02 |
| TAR-FAS | **7.54** | **96.67** | **0.00** | 8.35 |

TAR-FAS在平均HTER上比I-FAS降低3.76%，但在SIW数据集上HTER为8.35%，高于I-FAS的4.02%，表明其在特定域（如SIW）的泛化能力仍受局限。

| 训练阶段 | HTER(%) | AUC |
| :--- | :--- | :--- |
| FI only | 16.80 | 89.65 |
| FI + RL | 13.29 | 91.46 |
| KT + FI + RL | **7.54** | **96.67** |

消融实验显示，DT-GRPO（RL阶段）带来5.46% HTER提升，而知识迁移（KT）额外贡献1.81%。值得注意的是，仅使用FI阶段时HTER高达16.80%，表明格式注入本身不足以驱动有效推理，必须结合强化学习才能激发工具调用的自适应能力。

评估边界方面，论文未报告置信区间，且HTER与APCER/BPCER指标不可直接换算，导致与知识库中DINOv2+Registers（0.00% APCER）的数值不可比。代码未公开，超参数（如LoRA rank=16, LR=1e-4）虽详细列出，但缺乏GPU资源与训练时间报告，影响可复现性。

## 关联研究分析

从问题动机看，TAR-FAS与I-FAS同属MLLM-FAS路线，但I-FAS依赖单句语义解释，而TAR-FAS引入多轮工具调查。差异根源在于任务特性：I-FAS假设语义线索足以区分真假，而TAR-FAS承认MLLM低层感知缺陷，需外部工具补偿。这种设计使TAR-FAS在CASIA-MFSD（0.00% HTER）上超越I-FAS（1.11%），但在SIW上表现较差，暗示工具调用对特定攻击类型（如SIW中的打印攻击）的泛化能力可能受限于工具集的覆盖范围。

从方法设计看，TAR-FAS与DINOv2+Registers代表不同技术路线：前者依赖语义推理+工具调用，后者依赖纯视觉特征微调。DINOv2在SIW上取得0.00% APCER，而TAR-FAS在SIW上HTER为8.35%，表明纯视觉特征在特定域仍具优势。TAR-FAS的可解释性优势（提供推理链）是否足以抵消其精度劣势，取决于应用场景对可审计性的需求。此外，TAR-FAS的工具集（LBP/FFT/HOG）固定，未探索工具自动发现机制，这可能限制其应对全新攻击类型的能力。

## 总结

TAR-FAS旨在解决MLLM在FAS中对低层视觉特征盲视导致的跨域泛化瓶颈。其切入点在于利用MLLM的工具调用能力，将传统视觉算子封装为外部工具，实现从语义直觉到细粒度调查的转变。通过构建ToolFAS-16K数据集与DT-GRPO训练策略，TAR-FAS在One-to-Eleven协议下将平均HTER从11.30%降至7.54%。然而，其在SIW数据集上的HTER（8.35%）高于I-FAS（4.02%），暴露了工具调用在特定域泛化上的局限。当面对完全超出预训练分布的新物理介质攻击时，固定工具集能否提供足够的细粒度证据，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.01038)