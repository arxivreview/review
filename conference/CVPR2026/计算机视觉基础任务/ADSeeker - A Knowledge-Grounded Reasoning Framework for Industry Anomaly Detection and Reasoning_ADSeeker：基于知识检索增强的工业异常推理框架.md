# CVPR2026最新论文 ｜ADSeeker: A Knowledge-Grounded Reasoning Framework for Industry Anomaly Detection and Reasoning ｜ADSeeker：基于知识检索增强的工业异常推理框架

研究机构：山东大学、香港城市大学

作者：Kai Zhang、Zekai Zhang、Xihe Sun 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ee24e0f51dd9)

> 工业异常检测长期受困于缺陷样本稀缺与模型泛化能力不足的双重约束，传统零样本方法虽能跨域部署，却缺乏对缺陷成因与后果的语义推理能力。现有基于多模态大语言模型（MLLM）的方案在微调时易陷入过拟合与灾难性遗忘，导致细粒度描述与定位精度双低。ADSeeker 通过构建视觉文档知识库 SEEK-M&V 并引入 Q2K RAG 检索机制，在不进行大规模预训练的前提下，将外部领域知识注入 MLLM 推理流程。该框架在异常推理任务上显著优于通用 MLLM，但其对知识库覆盖范围的依赖限制了其在未知缺陷类型上的泛化边界。

## 研究背景

工业质检的核心困境在于，真实缺陷样本极度稀缺且标注成本高昂，导致监督学习模型难以训练。为突破数据瓶颈，零样本异常检测（Zero-Shot Anomaly Detection, ZSAD）范式应运而生，其核心假设是预训练视觉-语言模型（Vision-Language Model, VLM）已具备足够的跨域表征能力。然而，现有 ZSAD 方法如 WinCLIP 和 AnomalyCLIP 主要依赖对象级提示（如“wood”或“leather”），这些提示仅能识别物体类别，无法捕捉“scratch”或“hole”等缺陷类型级特征，导致模型在细粒度缺陷定位与描述上表现乏力。

随着多模态大语言模型（Multimodal Large Language Models, MLLMs）的兴起，研究者尝试将其应用于异常推理，即不仅检测异常，还需解释缺陷成因与后果。然而，标准微调策略在有限数据集上极易导致过拟合，且会破坏模型原有的通用对齐能力，使其无法生成技术精确且上下文感知的语言。ADSeeker 的切入点在于，不通过微调改变模型参数，而是通过外部知识检索增强生成（Retrieval-Augmented Generation, RAG）机制，动态注入领域知识，从而在保持 MLLM 通用泛化能力的同时，提升其在工业异常检测（Industry Anomaly Detection, IAD）任务中的专业推理能力。

## 核心方法

### 方法参照系

ADSeeker 建立在 Qwen2.5-VL 骨干与 CLIP 编码器之上，其基础流程与标准 ZSAD 一致：利用 CLIP 对齐视觉与文本特征，计算相似度以定位异常。关键差异在于，ADSeeker 不依赖模型内部参数存储缺陷知识，而是通过外部知识库检索与层级稀疏提示（Hierarchical Sparse Prompt, HSP）机制，将缺陷类型级特征显式注入推理过程。

### Q2K RAG 知识检索机制

针对 MLLM 预训练阶段缺乏 IAD 领域知识的问题，ADSeeker 引入 Q2K RAG 模块。该模块将查询图像 $I_q$ 与知识库文档 $I_k$ 分别编码为键特征 $K_Q$ 与锁特征 $L$，在联合特征空间中进行多模态检索。为处理知识库中分布不均的领域知识，论文采用高斯混合模型（GMM）对相似度分数进行聚类，推断最佳类别数 $K$ 并执行聚类：

$$
N = \{ I_n \sim G(\mu_n, \sigma_n^2) | I_n \in S \}
$$

其中 $G$ 表示高斯分布，$\mu_n, \sigma_n^2$ 为第 $n$ 个簇的均值与方差。该设计解决了简单 top-k 策略难以检索到产品相关场景信息的问题，通过非均匀采样确保检索到的知识文档在语义上与查询图像高度相关，从而为 MLLM 提供精确的缺陷类型与分析依据。

### 层级稀疏提示与 AD Expert 融合

HSP 机制旨在提取类型级特征（如“crack”或“hole”），以弥补对象级提示的不足。AD Expert 模块通过计算补丁嵌入 $E_p$ 与正负文本嵌入 $E_p^t, E_n^t$ 的余弦相似度，生成异常定位信息 $Loc$：

$$
Loc = Unsample\left( \frac{\cos(E_p, E_n^t)}{\cos(E_p, E_p^t) + \cos(E_p, E_n^t)} \right)
$$

该公式量化了每个图像区域与正常/异常文本描述的偏离程度，将细粒度的定位与判别信息转化为视觉令牌 $V_{is}$，并与 $Loc$ 融合为异常先验特征 $E_c$。这一设计使得 MLLM 在生成文本时，能够基于精确的视觉证据进行推理，而非依赖模糊的全局语义，从而显著提升了缺陷定位与描述的准确性。

## 实验评估

ADSeeker 在 MVTec AD、VisA、BTAD、MPDD 等 12 个工业与医疗数据集上进行了零样本异常检测评估，基线包括 CLIP、WinCLIP、AnomalyCLIP、AdaCLIP 及 AnomalyOV。实验协议采用 1-shot 设置，其中 ADSeeker 使用检索到的知识文档替代正常样本作为模板。

| 方法 | MVTecAD | VisA | BTAD | MPDD | Average |
| :--- | :--- | :--- | :--- | :--- | :--- |
| WinCLIP | 91.8 | 78.8 | 68.2 | 63.6 | 80.8 |
| AnomalyCLIP | 91.5 | 82.1 | 88.3 | 77.0 | 88.2 |
| AdaCLIP | 89.2 | 85.8 | 88.6 | 76.0 | 89.1 |
| AnomalyOV | 94.0 | 91.1 | 89.0 | 81.7 | 91.8 |
| ADSeeker | 94.3 | 91.5 | 94.0 | 85.9 | 94.0 |

ADSeeker 在平均 I-AUROC 上达到 94.0%，超越 AnomalyOV 的 91.8% 和 AdaCLIP 的 89.1%。在异常推理任务（MMAD 基准）上，ADSeeker 在缺陷分类、定位与异常判别子任务上表现突出，平均准确率为 69.90%，显著高于 LLaVA-OV 的 63.19% 和 InternVL2 的 63.14%。

消融实验表明，Q2K RAG 与 AD Expert 模块均对性能有正向贡献。在 Wood 类别上，仅使用 Q2K RAG 时 I-AUROC 为 78.6%，加入 AD Expert 后提升至 82.8%。然而，LoRA 微调在增加训练轮次后性能出现下降，证实了小规模数据集上微调易导致过拟合与灾难性遗忘。效率分析显示，ADSeeker 相比基础模型增加约 27% 的内存消耗和 2 秒的推理延迟，在实时工业应用中具有可行性。

评估边界方面，论文未报告像素级定位指标（如 AUPRO），仅关注图像级分类与推理准确率。此外，SEEK-M&V 知识库的构建依赖 DeepSeek-R1 生成的描述，其质量可能影响检索效果。代码未公开，且未提供置信区间，数值比较需谨慎。

## 关联研究分析

从问题动机看，ADSeeker 与 WinCLIP 和 AnomalyCLIP 同属零样本异常检测路线，但前者聚焦于跨域泛化，后者则致力于语义推理。WinCLIP 通过多尺度滑动窗口计算相似度，缺乏对缺陷类型的细粒度区分；AnomalyCLIP 引入对象级提示，但仍无法捕捉“scratch”与“hole”等类型级差异。ADSeeker 通过 HSP 机制提取类型级特征，解决了对象级提示在细粒度缺陷识别上的失效。然而，这种对类型级特征的依赖可能限制了其在未见过的缺陷类型上的泛化能力，因为 HSP 的聚类中心基于 MulA 数据集预定义，若新缺陷类型不在聚类中心附近，检索效果可能下降。

从方法设计看，ADSeeker 与 AnomalyGPT 和 Anomaly-OV 同属基于 MLLM 的异常推理框架，但前者采用微调策略，后者采用知识注入策略。AnomalyGPT 通过直接微调注入领域知识，易导致过拟合；Anomaly-OV 结合视觉与语言模态，但缺乏外部知识检索机制。ADSeeker 的 Q2K RAG 模块通过动态检索知识文档，避免了微调带来的参数改变，保持了 MLLM 的通用能力。这种设计在知识库覆盖范围内具有优势，但在知识库外的缺陷类型上，其性能可能退化为通用 MLLM 的水平，论文未对此进行充分测试。

## 总结

ADSeeker 旨在解决 MLLM 在工业异常检测中缺乏领域知识与细粒度推理能力的问题。其切入点在于，通过外部知识库检索而非参数微调，将缺陷类型级特征与领域知识动态注入推理流程，从而在保持通用泛化能力的同时提升专业性。该方法在 12 个数据集上实现了 94.0% 的平均 I-AUROC，并在 MMAD 基准上达到 69.90% 的推理准确率。然而，其性能高度依赖 SEEK-M&V 知识库的覆盖范围与质量，且未报告像素级定位指标，限制了其在精确定位任务中的应用。当查询图像对应的缺陷类型在知识库中缺乏精确匹配时，Q2K RAG 的检索效果是否会显著下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ee24e0f51dd9)