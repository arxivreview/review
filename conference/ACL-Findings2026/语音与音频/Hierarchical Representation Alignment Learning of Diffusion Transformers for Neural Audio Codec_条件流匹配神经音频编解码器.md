# ACL-Findings2026最新论文 ｜Hierarchical Representation Alignment Learning of Diffusion Transformers for Neural Audio Codec ｜条件流匹配神经音频编解码器

作者：Sang-Hoon Lee、Ha-Yeong Choi

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_55e4b6e26a0a)

> 极低码率下，传统生成对抗网络（GAN）解码器因信息压缩过度导致语义丢失与高频重建崩塌。现有单码本方案虽简化了大语言模型（LLM）接口，但缺乏概率式生成机制对缺失细节的补偿能力。FlowTokenizer 将条件流匹配（Conditional Flow Matching, CFM）引入解码器，并设计分层表征对齐（REPA-H）与稠密向量量化（DVQ），在 25 TPS 下实现 24 kHz 波形重建。该方法在语义一致性上优于同码率 GAN 基线，但绝对重建质量仍受限于低帧率信息瓶颈，其流式推理延迟与说话人相似度损失尚存疑。

## 研究背景

当音频信号被压缩至极低比特率时，离散 Token 序列承载的信息量急剧减少。此时，解码器面临的核心挑战是如何从稀疏的离散表征中恢复出高保真的连续波形。传统方法依赖 GAN 的判别器反馈来锐化波形细节，但在低码率下，判别器往往引导模型生成过度平滑的频谱，导致语音中的音素细节丢失，进而引发高词错误率（Word Error Rate, WER）。为缓解这一问题，研究者引入自监督学习（Self-Supervised Learning, SSL）特征作为语义先验，试图在量化阶段保留高层语义信息。然而，单纯的语义蒸馏无法解决声学细节的重建问题，且 GAN 训练在低数据量或低码率场景下易出现模式坍塌，导致训练不稳定。

神经音频编解码器的研究脉络从早期的残差向量量化（Residual Vector Quantization, RVQ）主导的多码本架构，逐步转向适配 LLM 的单码本低帧率设计。RVQ 通过级联量化器提升保真度，但产生的长 Token 序列显著增加了 LLM 的自回归预测成本。BigCodec 和 WavTokenizer 等后续工作采用单量化器策略，虽降低了序列长度，但在 25 TPS 等极端低帧率下，确定性解码器难以恢复 24 kHz 采样率下的高频成分。FlowTokenizer 的切入点在于利用 CFM 的概率式生成特性，替代 GAN 的对抗训练机制，通过迭代采样逐步细化波形，同时引入分层对齐机制以稳定训练过程并增强语义保留能力。

## 核心方法

### 方法参照系

本文遵循“编码器-量化器-解码器”的标准神经音频编解码范式，但将解码器从 GAN 替换为基于 DiT 的 CFM 模型。与通用流程的关键差异在于，本文不依赖判别器进行波形锐化，而是通过向量场估计实现从噪声到波形的连续映射，并在量化阶段采用因子化设计以分离语义与声学表征。

### 分层表征对齐学习（REPA-H）

**设计动机**：解决 CFM 在低码率下无法同时保证语义一致性与声学保真度的问题，以及 REPA 损失干扰向量场估计导致的训练不稳定。

在 DiT 解码器中，早期层负责语义对齐，后期层负责声学重建。REPA-H 通过分层对齐机制，将 SSL 模型（如 Wav2Vec 2.0）的语义嵌入与 DiT 中间层特征进行匹配。语义对齐损失定义为：

$$
\mathcal{L}_{semantic} = \mathbb{E}\left[\|h_t - \hat{h}_t\|_1 + \left(-\log \sigma\left(\cos(h_t, \hat{h}_t)\right)\right)\right]
$$

其中 $h_t$ 为教师嵌入，$\hat{h}_t$ 为 DiT 预测嵌入。该公式通过 L1 范数与余弦相似度联合约束，确保 DiT 早期层捕捉语义信息。同时，引入声学对齐损失，利用多分辨率 Mel 谱损失监督 DiT 输出层的波形重建。这种分层策略避免了单一损失函数在语义与声学目标间的冲突，提升了训练稳定性。

### 稠密向量量化（DVQ）

**设计动机**：解决单码本量化中语义与声学表征纠缠导致的信息损失，以及传统线性投影破坏表征完整性的问题。

DVQ 将语义与声学特征拼接后，通过分组卷积层映射至 FSQ 空间，而非直接线性投影。量化后的表征表示为：

$$
\mathbf{z}_{quant} = \text{FSQ}\left(\text{GroupConv}(\mathbf{z}_{semantic} \oplus \mathbf{z}_{acoustic})\right)
$$

其中 $\oplus$ 表示拼接，FSQ 配置为 8 维 4 级，生成 65,536 个 Token。该设计保留了语义与声学维度的独立性，允许从量化表征中提取 256 个辅助语义 Token，用于计算额外的语义损失，从而为 LLM 提供更清晰的语义引导。

## 实验评估

| 方法 | 采样率 | TPS | WER (↓) | PESQ (↑) | SPK-SIM (↑) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Mimi | 24k | 75 | 2.96 | 2.25 | 0.73 |
| WavTokenizer | 24k | 40 | 3.98 | 2.13 | 0.65 |
| FlowTokenizer w/o Prompt | 24k | 25 | 3.38 | 1.56 | 0.41 |
| FlowTokenizer w/ 3s Prompt | 24k | 25 | 2.91 | 1.61 | 0.60 |

实验在 LibriTTS 和 LibriSpeech 上进行，对比了 EnCodec、Mimi、WavTokenizer 等基线。FlowTokenizer 在 25 TPS 下，WER 为 3.38（无提示）和 2.91（3秒提示），优于同码率的 WavTokenizer（WER 3.98）和 Mimi（WER 2.96，但帧率更高）。然而，其 PESQ 值（1.56-1.61）显著低于 Mimi（2.25）和 WavTokenizer（2.13），表明在极低帧率下，CFM 解码器在感知质量上仍有差距。

| 消融配置 | CER (↓) | WER (↓) | PESQ (↑) | UTMOS (↑) |
| :--- | :--- | :--- | :--- | :--- |
| FlowTokenizer (REPA-H) | 2.57 | 5.87 | 1.556 | 4.000 |
| w/o REPA | 17.59 | 29.49 | 1.647 | 3.724 |
| w/o DVQ (Only FSQ) | 3.65 | 7.35 | 1.551 | 3.900 |
| w/o Adversarial Fine-tuning | 3.00 | 6.00 | 1.390 | 3.535 |

消融实验显示，移除 REPA 导致 WER 从 5.87 飙升至 29.49，证明语义对齐对低码率下语义保留至关重要。移除 DVQ 后，WER 从 5.87 升至 7.35，表明因子化量化优于简单 FSQ。对抗微调虽提升了 PESQ（1.390 至 1.556），但 WER 略有上升（6.00 至 5.87），显示生成质量与语义一致性存在权衡。

评估协议采用 PESQ、WER、CER 和 SPK-SIM，但未报告置信区间。代码未公开，仅提供 Demo 链接，可复现性受限。模型在 8 块 H100 GPU 上训练，超参数细节部分披露，但 DiT 结构的具体层数与维度未在正文中完整列出。

## 关联研究分析

从问题动机看，FlowTokenizer 与 BigCodec 均致力于单码本低帧率编码，但 BigCodec 依赖 GAN 解码器，而 FlowTokenizer 采用 CFM。这一差异源于 GAN 在低码率下易产生频谱平滑伪影，而 CFM 通过迭代采样能更好地恢复高频细节。然而，FlowTokenizer 的 SPK-SIM（0.41-0.60）低于 Mimi（0.73），暗示 CFM 在保留说话人特征方面可能不如 GAN 稳定，这或许是概率式生成在身份一致性上的固有局限。

从方法设计看，FlowTokenizer 的 DVQ 与 X-codec2 的语义-声学拼接策略相似，但 X-codec2 使用线性投影，而 FlowTokenizer 采用分组卷积。这一设计选择旨在保留表征维度的独立性，避免线性混合导致的语义信息稀释。然而，论文未对比 DVQ 与 RVQ 在相同比特率下的性能，无法确定单码本因子化是否在所有场景下优于多码本级联，这一盲区限制了结论的普适性。

## 总结

FlowTokenizer 旨在解决极低码率下 GAN 解码器的语义丢失与训练不稳定问题。其切入点在于利用 CFM 的概率式生成机制替代 GAN，并通过 REPA-H 分层对齐与 DVQ 因子化量化增强语义保留。实验证明，在 25 TPS 下，FlowTokenizer 的 WER（2.91-3.38）优于同码率 GAN 基线，但 PESQ（1.56-1.61）显著低于高帧率模型。其边界在于，CFM 解码器在说话人相似度上表现较弱，且流式推理的延迟优势未充分验证。当帧率进一步降低至 12.5 TPS 时，CFM 的迭代采样成本是否会抵消其语义优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_55e4b6e26a0a)