# HuggingFace最新推荐论文 ｜WeLM-Image: A Unified Image Generation Model towards Visual Intelligence ｜WeLM-Image：面向单GPU部署的统一图像生成与编辑基础模型

作者：Canmiao Fu、Chen Li、Guohui Zhang 等 16 人

论文原文见 [arXiv](https://arxiv.org/abs/2611.07392)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2611.07392)

> 指令式图像编辑（Instruction-Based Image Editing, IBIE）旨在通过自然语言指令对图像进行精确、可控的视觉修改，其核心价值在于连接人类意图与视觉生成。现有方法多依赖多模态大语言模型（Multimodal Large Language Model, MLLM）进行显式推理与规划，虽提升了复杂指令的遵循度，却因多步迭代与密集计算导致推理延迟高，难以满足大规模消费级应用的实时性需求。WeLM-Image 提出一种双路径混合专家（Mixture-of-Transformers, MoT）架构，将理解与生成路径解耦，通过共享注意力机制实现细粒度控制，并在单GPU上实现高效部署。该模型在保持高编辑质量的同时显著降低了推理成本，但其单次前向传播的架构设计在处理复杂组合指令时是否牺牲了推理深度，仍需进一步验证。

## 研究背景

当用户要求模型“将图1中的鳄鱼公仔放到图2的沙发上，并调整光影”时，模型需同时处理多张参考图像、理解空间关系、执行语义编辑并保持非编辑区域一致性。这一任务要求模型具备强大的多模态理解能力与精细的视觉控制能力。传统扩散模型通过微调建立文本到像素的映射，但在处理涉及多对象交互、隐含意图的长指令时，常出现语义偏差或背景意外修改。为解决此问题，领域内引入了MLLM作为推理引擎，通过“推理-规划-执行”范式提升复杂场景下的可控性。然而，这种显式推理机制通常依赖多步迭代与密集计算，导致推理延迟高，难以在大规模消费级应用中部署。

当前IBIE领域面临的核心矛盾是：如何在保证非编辑区域像素级一致性与复杂指令遵循度的前提下，实现低延迟、低成本的实时编辑。现有方法在表示质量、适应效率与计算成本之间做出了不同取舍。端到端微调模型（如InstructPix2Pix）效率高但复杂指令理解不足；显式推理代理（如MIRA）可解释性强但计算成本高。WeLM-Image 的切入点在于：通过架构级设计（MoT-MoE）在单次前向传播中融合MLLM的语义理解能力与扩散模型的生成能力，从而在效率与质量之间取得平衡。

## 核心方法

### 方法参照系：统一交错序列表示

WeLM-Image 将文本问答、视觉理解、文本到图像生成、指令引导编辑和多参考生成统一为交错文本-图像序列。每个样本被序列化为保留源顺序的文本和视觉片段：

$$S = [S_1; S_2; \dots; S_K], \quad S_k \in \{\text{text segment}, \text{image segment}\}$$

其中 $K$ 为片段数，$S_k$ 为第 $k$ 个片段。文本使用预训练语言模型分词器，视觉片段作为连续ViT或VAE嵌入。所有片段共享模型隐藏宽度并进入同一骨干网络。该表示消除了任务特定输入管线的需求，通过总令牌数打包平衡计算。

### 核心创新1：双路径MoT-MoE架构

传统统一模型常因理解与生成任务的优化目标冲突导致性能下降。WeLM-Image 采用双路径MoT架构，为理解（UND）和生成（GEN）路径分配独立参数，并通过共享注意力连接两条路径。UND路径处理文本和ViT图像特征，GEN路径处理VAE图像潜变量。每条路径内部进一步引入混合专家（Mixture-of-Experts, MoE）模块，通过稀疏专家激活扩展容量。

该架构的设计动机在于：通过参数分离减少优化干扰，同时通过共享注意力允许目标潜变量联合利用文本指令、语义图像特征和详细视觉参考。在31.7B存储参数中，每个目标潜变量令牌仅激活约5.4B生成参数，实现了容量与效率的平衡。

### 核心创新2：噪声感知在线策略蒸馏

为将生成和编辑任务的专用强化学习（Reinforcement Learning, RL）策略合并为统一模型，WeLM-Image 引入噪声感知在线策略蒸馏。在去噪过程的高噪声阶段，提示增强教师预测指导全局语义和布局；在低噪声阶段，标准RL教师预测监督局部细化。

该机制解决了RL后训练中不同任务奖励信号冲突的问题。生成任务使用基于评分标准的提示对齐、美学、文本渲染和视觉自然性奖励；编辑任务使用指令特定检查清单评估请求变更、内容保持和视觉质量。通过噪声水平感知的蒸馏，模型在不同去噪阶段吸收不同任务的最优策略，最终在单一模型中实现生成与编辑能力的统一。

## 实验评估

WeLM-Image 在多个基准上进行了评估，包括文本到图像生成（GenEval, OneIG-Bench, TIIF-Bench, DPG-Bench, Qwen-Image-Bench, WeGenBench, LongText-Bench, CVTG-2K）和图像编辑（GEdit, ImgEdit, UnicBench, WeGenEditBench）。基线覆盖主流开源模型（Qwen-Image, FLUX, HunyuanImage等）及闭源模型（GPT-Image-2, Nano-Banana-Pro等）。

| 基准 | 指标 | WeLM-Image | WeLM-Image-Turbo-8step | 最佳开源基线 |
| :--- | :--- | :--- | :--- | :--- |
| GenEval | Overall | 0.8509 | 0.8357 | 0.8863 (Qwen-Image) |
| OneIG-Bench | Overall | 7.32 | 7.40 | 7.78 (Qwen-Image) |
| TIIF-Bench | Overall (short) | 0.8078 | 0.7908 | 0.8547 (Qwen-Image) |
| DPG-Bench | Overall | 0.8748 | 0.8659 | 0.8881 (Qwen-Image) |
| Qwen-Image-Bench | Overall | 54.15 | 55.99 | 55.31 (Qwen-Image) |
| WeGenBench | Overall | 0.5337 | 0.5196 | 0.5538 (ERNIE-Image-Turbo-PE) |
| LongText-Bench | Overall | 0.931 | 0.933 | 0.975 (Qwen-Image) |
| CVTG-2K | Word Accuracy | 0.899 | 0.872 | 0.914 (Qwen-Image) |

在图像编辑基准上，WeLM-Image 在UnicBench和WeGenEditBench上取得开源模型最佳成绩，在GEdit和ImgEdit上排名前三。效率方面，WeLM-Image-Turbo在单NVIDIA H20 GPU上以8步无引导采样生成1024×1024图像仅需4.98秒，比WeLM-Image快11.4倍。

消融实验显示，MoT-MoE架构在保持高编辑质量的同时显著提升了推理效率。与Qwen-Image-Edit-2511相比，WeLM-Image在单输入编辑上快1.96倍，四输入编辑上快5.10倍。然而，论文未提供与显式推理代理（如MIRA）的直接对比，无法评估单次前向传播架构在复杂组合指令上的推理深度是否不足。

评估边界方面，论文未报告置信区间，且部分基准（如PICABench）未覆盖，无法评估物理一致性。代码未开源，可复现性受限。

## 关联研究分析

从方法设计看，WeLM-Image 与MIRA代表了IBIE领域的两条不同路线。MIRA通过MLLM进行显式迭代推理，将复杂指令分解为原子编辑指令，以闭环方式逐步执行，牺牲效率换取复杂指令的分解与反馈能力。WeLM-Image 则通过MoT架构在单次前向传播中融合理解与生成，通过架构分离而非显式Agent循环实现控制。该差异源于任务特性：MIRA针对复杂组合指令，WeLM-Image 针对大规模消费级应用的实时性需求。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

从问题动机看，WeLM-Image 与EditReward均引入RL优化编辑质量，但EditReward构建大规模人类偏好数据集训练专用奖励模型，侧重细粒度编辑质量评估；WeLM-Image 采用任务特定检查清单奖励，并通过噪声感知蒸馏合并策略，侧重效率与统一性。该差异反映了论文对部署成本的约束：单GPU部署要求模型在保持质量的同时最小化推理延迟。

## 总结

WeLM-Image 要解决的核心矛盾是：如何在保证非编辑区域像素级一致性与复杂指令遵循度的前提下，实现低延迟、低成本的实时编辑。现有方法或依赖显式推理导致效率低下，或依赖端到端微调导致复杂指令理解不足。WeLM-Image 通过双路径MoT-MoE架构在单次前向传播中融合MLLM的语义理解能力与扩散模型的生成能力，并通过噪声感知在线策略蒸馏合并生成与编辑的专用RL策略。该模型在UnicBench和WeGenEditBench上取得开源模型最佳成绩，在单GPU上实现4.98秒生成1024×1024图像。然而，论文未提供与显式推理代理的直接对比，无法评估单次前向传播架构在复杂组合指令上的推理深度是否不足。当支持集增大到多参考图像时，单次前向传播的MoT架构是否仍能保持与Agent路线相当的复杂指令分解能力，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2611.07392)