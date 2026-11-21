# HuggingFace最新推荐论文 ｜Illuminating Unified Multimodal Model for Free-form Interleaved Text-Image Generation ｜自由形式交错多模态生成

研究机构：哈尔滨工业大学、南开大学

作者：Chonghuinan Wang、Zhikai Chen、Chunwei Wang 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.30054)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.30054)

> 统一多模态模型旨在单一架构内融合视觉理解与图像生成，但现有方法多局限于固定模态顺序或单一目标模态，难以处理任意序列的文本-图像交错生成。ILLUME-X 通过构建高保真交错数据管线与专用注意力掩码机制，实现了自由形式 N-to-M 交错生成，并提出了针对该任务的 ILScore 评估协议。该工作验证了统一架构在交错任务上可匹敌专用 Agent 系统，但其通用生成能力仍略逊于专用扩散模型，且缺乏对“视觉思维”因果贡献的量化验证。

## 研究背景

当模型需要生成包含图像与文本的复杂叙事时，传统自回归模型将视觉离散化为 Token 进行 Next-token Prediction，导致高频细节丢失，生成保真度远低于专用扩散模型。为兼顾语义抽象与像素保真，混合 AR-Diffusion 架构成为主流，如 Transfusion 结合自回归语言建模与扩散图像生成目标，BAGEL 采用 Mixture-of-Transformers (MoT) 架构分离理解与生成路径。然而，这些模型通常被限制在预定义的模态序列中，缺乏对自由形式交错序列的结构稳定性与数据支撑。

现有统一模型在交错生成任务上存在两大瓶颈：一是训练数据缺乏高保真且结构一致的交错序列，CoMM 和 Zebra-CoT 等数据集在质量与一致性上不足，导致训练不稳定；二是评估指标缺失，ISG-Bench 等基准依赖固定输出结构，当生成结果偏离模板时评估失效。ILLUME-X 的切入点在于构建专门针对自由形式 N-to-M 交错生成的数据管线与评估协议，通过架构改造与训练策略优化，解决交错序列中的模态转换与跨模态连贯性问题。

## 核心方法

### 混合 AR-Diffusion 架构参照系

ILLUME-X 属于混合 AR-Diffusion 路线，其核心假设是视觉与语言可在统一 Transformer 中通过不同目标联合优化。标准流程包括：双编码器提取视觉特征（ViT 用于语义，VAE 用于细节），共享自注意力层处理交错 Token 序列，文本 Token 采用 Cross-Entropy (CE) 损失，视觉 Token 采用扩散或流匹配损失。本文的关键差异在于针对交错序列引入专用注意力掩码与噪声掩码机制，以处理任意长度的多模态 Token 序列。

### 交错注意力与噪声掩码机制

在标准 MoT 架构中，所有 Token 共享自注意力，但缺乏对模态转换的显式约束。ILLUME-X 引入 BOI（begin-of-image）、EOI（end-of-image）和 EOS（end-of-sequence）特殊 Token 明确标记模态边界。注意力掩码设计为：文本与特殊 Token 采用因果注意力以维持自回归性质，视觉 Token 采用双向注意力以捕获全局空间信息。为缓解噪声干扰导致的误差累积，模型在生成下一组样本时对当前噪声图像 Token 应用掩码操作。该机制解决了此前方法在长序列交错生成中因噪声传播导致的结构崩溃问题，确保了模态转换的稳定性。

$$
\mathcal{L}_{total} = \mathcal{L}_{CE}(\text{Text, Special}) + \mathcal{L}_{MSE}(\text{Vision}_{clean}, \text{Vision}_{noisy})
$$

该公式表明，训练目标联合优化文本语言建模与视觉重构，其中视觉损失基于 Rectified Flow 框架下的均方误差，确保生成图像的高保真度。

### 自由形式 N-to-M 训练策略

现有方法多针对固定模态比例或单一目标模态进行训练，难以泛化到任意输入输出组合。ILLUME-X 采用渐进式训练策略，结合自适应性目标函数，支持自由长度的多模态 Token 序列。数据管线整合了来自视频数据的真实交错序列与多模态大语言模型生成的合成数据，共 100K 高保真样本。该策略解决了此前方法在 N-to-M 场景下因数据分布偏差导致的性能退化问题，使模型能够灵活处理从单图生成到多轮叙事的各种任务。

## 实验评估

实验在 ISG-Bench、GenEval 和 DPG-Bench 上进行，基线覆盖 BAGEL、OmniGen2、Janus-Pro 等混合架构模型，以及 Emu 3.5 等纯自回归模型。在 ISG-Bench 交错生成任务上，ILLUME-X 平均得分 6.26，持平非统一 Agent 系统 ISG-AGENT，显著优于 Anole（2.81）和 MiniGPT-5（2.79）。在 GenEval 文生图任务上，ILLUME-X 整体得分 0.85，高于 BAGEL（0.82）和 OmniGen2（0.80），但低于知识库中 UniDFlow 的 0.95。在 DPG-Bench 上，ILLUME-X 整体得分 86.38，高于 BAGEL（85.07），但低于 CE-Router 的 87.95。

| 基准 | 指标 | ILLUME-X | BAGEL | OmniGen2 | Janus-Pro |
|---|---|---|---|---|---|
| ISG-Bench | AVG | 6.26 | — | — | — |
| GenEval | Overall | 0.85 | 0.82 | 0.80 | 0.80 |
| DPG-Bench | Overall | 86.38 | 85.07 | 83.57 | 84.19 |

消融实验显示，Classifier-Free Guidance (CFG) 文本引导尺度 8.0、图像引导尺度 1.0 并启用 Chain-of-Thought (CoT) 时，Visual Storytelling 得分最高（7.28）。CoT 的引入提升了叙事连贯性，但图像引导尺度增加至 1.5 时得分下降至 6.85，表明过强的图像引导可能干扰文本语义对齐。

评估边界方面，ILScore 虽填补了交错生成评估空白，但依赖人工标注或 LLM 评分，缺乏客观量化指标。可复现性方面，论文提供 GitHub 链接，但未报告 GPU 数量与训练时长，仅提及 7B+7B 参数架构与 81.33 秒/图的推理时间。

## 关联研究分析

从问题动机看，ILLUME-X 与 BAGEL 同属 MoT 架构路线，但 BAGEL 聚焦通用多模态理解与生成，而 ILLUME-X 特化于交错生成任务。BAGEL 通过大规模交错数据训练实现通用能力，但缺乏针对交错序列结构的专用注意力机制；ILLUME-X 通过噪声掩码与模态边界 Token 解决结构稳定性问题，但通用生成能力略逊于 BAGEL。这一差异源于任务特性：交错生成对时序连贯性与模态转换的敏感性高于通用生成，迫使架构设计向结构约束倾斜。

从方法设计看，ILLUME-X 与 ISG-AGENT 在交错生成任务上性能持平，但 ISG-AGENT 是非统一 Agent 系统，依赖外部工具调用与多步推理，而 ILLUME-X 是单一模型端到端生成。ISG-AGENT 的优势在于灵活性与可解释性，劣势在于推理延迟高且依赖外部模型；ILLUME-X 的优势在于推理效率（81.33 秒/图 vs Emu 3.5 的 409.50 秒/图），劣势在于缺乏显式推理步骤。查询侧增强在数据充足时是否仍有增益，论文未给出回答，但 ILLUME-X 的 100K 数据管线表明数据质量比数量更关键。

## 总结

ILLUME-X 要解决的核心矛盾是统一多模态模型在自由形式交错生成任务上的结构稳定性与评估缺失问题。其切入点在于构建高保真交错数据管线与专用注意力掩码机制，通过噪声掩码缓解误差累积，通过模态边界 Token 明确转换逻辑。方法上，ILLUME-X 采用 MoT 架构结合 CE 与 Rectified Flow MSE 损失，支持 N-to-M 自由形式生成。实验证明，其在 ISG-Bench 上达到 6.26 分，匹敌专用 Agent 系统，且在 GenEval 上取得 0.85 分，高于 BAGEL。然而，其通用生成能力仍低于 UniDFlow 等 SOTA 模型，且缺乏对“视觉思维”因果贡献的量化验证。当支持集增大到 5-shot 时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.30054)