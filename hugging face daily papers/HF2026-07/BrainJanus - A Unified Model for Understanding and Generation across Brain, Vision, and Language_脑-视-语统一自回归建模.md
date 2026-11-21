# HuggingFace最新推荐论文 ｜BrainJanus: A Unified Model for Understanding and Generation across Brain, Vision, and Language ｜脑-视-语统一自回归建模

研究机构：天津大学、香港中文大学

作者：Haitao Wu、Qirui Zhang、Zhouheng Yao 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.30319)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.30319)

> 现有脑解码方法将神经信号与视觉/语言模态割裂处理，依赖外部先验补偿语义缺失，无法捕捉大脑作为多模态整合系统的内在特性。BrainJanus 通过专用离散化器将 fMRI 映射至共享 Omni 空间，以单一 Transformer 实现脑、视、语三模态的双向任意转换。该框架在脑-文解码 BERTScore 上达到 38.12，脑-图解码 CLIP 相似度达 94.4%，验证了纯自回归路径在神经信号建模上的可行性，但其对高分辨率视觉细节的保留能力仍受限于离散化瓶颈。

## 研究背景

神经信号建模面临的核心困境在于连续动力学与离散计算架构的兼容性。fMRI 数据本质上是高维连续时间序列，而主流生成模型依赖离散 Token 进行 Next-token Prediction。直接量化会丢失高频神经振荡信息，而保留连续表征则无法与文本、图像 Token 在同一序列中交错建模。这一矛盾导致现有方法要么采用专用扩散模型重建图像，要么依赖冻结的 CLIP 特征进行语义对齐，两者均无法在单一架构内实现双向映射。

脑解码领域长期存在“任务隔离”与“模态割裂”两大瓶颈。主流路线如 MindEye2 和 UMBRAE 将脑-图重建与脑-文描述视为独立任务，各自训练专用编码器，且均依赖外部大模型（如 Stable Diffusion 或 LLaMA）作为生成先验。这种设计忽视了神经科学证据：大脑皮层语义表征是跨模态整合的，视觉刺激同时激活语言与概念区域。现有方法对神经信号的多模态语义利用不足，导致解码结果缺乏深层语义一致性。BrainJanus 的切入点在于构建一个统一的离散 Token 空间，将脑、视、语信号映射至同一 Omni 空间，通过共享参数实现跨模态知识迁移，从而摆脱对外部先验的过度依赖。

## 核心方法

### 统一脑 Tokenizer 预训练

在纯自回归统一架构中，视觉与语言模态已有成熟的离散化方案，但神经信号缺乏对应的 Tokenizer。BrainJanus 引入 Unified Brain Tokenizer，采用 VQ-VAE 架构将连续 fMRI 信号量化为离散 Token。其训练目标为：

$$ \mathcal{L} = \log p(x | z_q(x)) + \| \text{sg}(z_e(x)) - e_k \|^2 + \beta \| z_e(x) - \text{sg}(e_k) \|^2 $$

该公式第一项鼓励解码器从量化潜变量 $z_q(x)$ 重构原始信号，第二项更新码本向量 $e_k$ 使其接近编码器输出，第三项通过承诺损失（commitment loss）约束编码器输出稳定在码本附近。这一设计解决了连续神经信号无法直接参与自回归预测的问题，使脑信号能与视觉、语言 Token 在同一序列中交错。

### 全模态自回归生成

在 Omni 空间中，BrainJanus 定义统一自回归模型 $p_\theta$，对交错多模态 Token 序列进行 Next-token Prediction。给定前缀 $(z_1, \dots, z_{t-1})$，模型预测下一 Token：

$$ p_\theta(z_t | z_{<t}) = \text{softmax}(W \cdot h_t) $$

其中 $h_t$ 为 Transformer 隐藏状态，$W$ 为输出投影矩阵。该模型通过 LoRA 微调 Janus-7B 骨干，在四个任务（脑-图、脑-文、图-脑、文-脑）上联合训练。设计动机在于：共享参数迫使模型学习跨模态的内在语义关联，而非依赖外部对齐器。相比任务隔离方法，该架构允许脑信号解码时直接利用视觉与语言模态的上下文信息，实现零样本跨任务泛化。

## 实验评估

实验基于 NSD 数据集，使用 4 名被试的 9,000 张训练图像和 1,000 张测试图像。基线覆盖 MindEye2、UMBRAE、MindLLM 等脑解码 SOTA 方法，但缺乏与纯视觉统一模型（如 BAGEL、Transfusion）的直接对比。

| 方法 | BERTScore (Qwen GT) | CLIP Score (Qwen GT) |
|---|---|---|
| MindEye2 | 29.12 | 93.0% |
| UMBRAE | 30.91 | 94.7% |
| MindLLM | 30.62 | 88.9% |
| BrainJanus | 38.12 | 96.2% |

BrainJanus 在详细 Qwen 标注下 BERTScore 达 38.12，较 MindEye2 提升 9.00 点；CLIP 相似度 96.2% 亦为最高。在脑-图解码中，BrainJanus 的 CLIP 相似度 94.4% 超过 MindEye2 的 93.0%，但像素级指标（PixCorr 0.173）仍低于扩散模型基线（MindEye2 0.322），表明纯自回归路径在低层细节重建上存在固有劣势。

消融实验显示，码本大小超过 128 后收益递减，压缩率 1/128 在语义保留与序列长度间取得平衡。零样本泛化验证了跨任务迁移能力：仅训练脑-文任务即可零样本执行脑-图生成，连贯性得分 3.13（GRPO 优化后）。

评估边界方面，论文未报告计算效率指标，且仅使用 4 名被试，跨被试鲁棒性未充分验证。代码已开源，但 LoRA 超参数（rank 16, dropout 0.2）的敏感性分析缺失，可复现性依赖特定骨干初始化。

## 关联研究分析

从问题动机看，BrainJanus 与 Chameleon、Emu3 同属纯自回归统一架构，但将模态范围从外部感官数据扩展至内部神经信号。关键差异在于：Chameleon 依赖预训练视觉 Tokenizer，而 BrainJanus 需从零训练脑 Tokenizer，这引入了新的信息损失风险。论文通过 VQ-VAE 承诺损失缓解量化漂移，但未探讨脑信号高频成分丢失对神经动力学建模的影响。

从方法设计看，BrainJanus 与 Janus 共享解耦编码器思路，但 Janus 针对视觉理解与生成的梯度冲突，而 BrainJanus 针对神经信号离散化与语义对齐的冲突。Janus 采用双编码器分离理解与生成路径，BrainJanus 则通过共享 Omni 空间实现模态融合。这一设计选择暗示：神经信号的多模态整合特性可能比视觉任务的表征冲突更依赖共享参数，但论文未提供表征空间分析的定量证据，无法确认脑、视、语 Token 在隐藏层中是否真正融合而非模块隔离。

## 总结

BrainJanus 解决了神经信号离散化与多模态统一建模的矛盾，通过专用 Tokenizer 和共享 Omni 空间实现脑-视-语双向映射。其核心贡献在于验证了纯自回归架构在神经科学任务上的可行性，脑-文解码 BERTScore 38.12 和脑-图解码 CLIP 94.4% 表明语义对齐能力超越专用扩散模型。然而，像素级重建质量（PixCorr 0.173）仍显著低于扩散基线，暴露了离散化对高频神经信息的损失。当被试数量增加至 8 名时，脑 Tokenizer 的跨被试泛化能力是否衰减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.30319)