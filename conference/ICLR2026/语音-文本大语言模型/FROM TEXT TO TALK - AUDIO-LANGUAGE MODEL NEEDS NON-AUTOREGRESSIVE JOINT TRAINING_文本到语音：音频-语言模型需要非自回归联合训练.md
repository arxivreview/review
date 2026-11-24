# ICLR2026最新论文 ｜FROM TEXT TO TALK: AUDIO-LANGUAGE MODEL NEEDS NON-AUTOREGRESSIVE JOINT TRAINING ｜文本到语音：音频-语言模型需要非自回归联合训练

研究机构：北京大学

作者：Tianqiao Liu、Xueyi Li、Hao Wang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_20777631)

> 语音-文本多模态大语言模型（MLLM）旨在统一语音理解与生成，但现有端到端架构对文本和音频均采用自回归（AR）目标，忽视了二者生成依赖结构的根本差异。这种统一目标导致音频生成受文本因果链干扰，加剧误差传播并限制并行效率。本文提出 Text-to-Talk (TtT)，通过混合 AR-NAR 架构，将文本 AR 生成与音频非自回归（NAR）离散扩散统一于单一 Transformer，并证明其训练目标为联合分布负对数似然的上界。该设计在 3B 规模下显著优于同规模 AR/NAR 基线，但其在长上下文语音对话中的稳定性及与最新对齐方法的对比尚存疑。

## 研究背景

当多模态模型处理交错的文本与音频序列时，文本 token 的生成严格遵循目标-目标（Target-Target）依赖，即每个 token 显式条件于前序生成内容，形成强因果链。然而，音频 token 的生成主要受源-目标（Source-Target）依赖驱动，即音频输出主要条件于源文本而非前序音频 token。这种依赖结构的不对称性意味着，若对音频施加与文本相同的 AR 约束，会引入不必要的顺序限制，导致训练动态次优并放大误差传播。

当前主流端到端 S2S 系统（如 Moshi, GLM-4-Voice）采用统一 AR 目标训练，虽实现了模态统一，但未能区分两种模态的生成本质。这种“一刀切”的策略导致音频生成质量受限，且无法利用 NAR 模型的并行解码优势以降低延迟。领域共识认为 AR 能更好地捕捉长距离依赖，但这一观点主要针对文本语义，未充分考量音频的声学特性。

本文切入点在于识别并形式化文本与音频依赖结构的根本不对称性。通过引入吸收式离散扩散（Absorbing Discrete Diffusion）建模音频，利用其“任意顺序 AR”性质，TtT 在保留文本推理能力的同时，实现了音频的高效并行生成，解决了统一 AR 目标导致的模态干扰问题。

## 核心方法

### 方法参照系

本文问题置于端到端 S2S 多模态生成框架下。标准流程通常采用单一 Transformer 对交错文本-音频 token 进行统一 AR 训练。关键差异在于，本文解耦了模态生成目标：文本保持 AR，音频改用 NAR 离散扩散，并引入模态感知注意力机制以支持混合解码。

### 混合 AR-NAR 联合分布建模

设计动机：解决统一 AR 目标对音频源-目标依赖的干扰。在参照系中，所有 token 均按左到右顺序生成。本文创新在于构建部分序（Partial Order）因子化，其中文本 token 保持全序，音频 span 内 token 构成反链（Antichain）。联合分布定义为：

$$
p_\theta(x) = \prod_{m=1}^M p_\theta(T_m | T_{<m}, A_{<m}) \cdot \tilde{p}_\theta(A_m | T_{\le m}, A_{<m})
$$

其中 $\tilde{p}_\theta$ 为音频 span 的序边际化条件概率，即对 span 内所有排列取平均。该公式表明，音频生成在给定跨模态上下文（前序文本与音频）下，可任意顺序生成，从而消除不必要的顺序约束，实现并行解码。

### 训练目标与上界分析

设计动机：确保混合训练目标的理论合理性。在参照系中，AR 损失直接最小化负对数似然。本文创新在于证明混合目标 $L_{Unified}$ 是理论联合分布负对数似然的上界。具体推导为：

$$
L_{Unified}(x) = L_{AR}(x) + L_{AO}(x) \ge -\log \tilde{p}_\theta(x)
$$

其中 $L_{AO}$ 为音频的任意顺序 AR 损失，等价于吸收式离散扩散的去噪目标。该不等式表明，最小化 $L_{Unified}$ 不会偏离理论最优目标，为混合架构提供了严格的理论保证，避免了因目标不一致导致的训练不稳定。

## 实验评估

实验在 Audio-QA、ASR、AAC 及 URO-Bench 上进行，基线覆盖 Moshi、SpeechGPT、Kimi-Audio 等 7B 大模型及 Mini-Omni 等 0.5B 小模型。本文 Pretrain+TtT (3B) 在 Audio-QA 和 ASR 上达到 SOTA，但在 AAC 上略低于 SLAM-Omni（后者依赖 7B Vicuna 辅助）。

| 模型 | 规模 | Audio-QA (WQ) ↑ | ASR (WS) ↓ | AAC (Clo) ↑ |
|---|---|---|---|---|
| Moshi | 7B | 16.85 | - | 4.32 |
| SpeechGPT | 7B | 24.53 | 123.15 | 2.10 |
| Pretrain+TtT | 3B | 21.43 | 19.85 | 11.55 |
| GLM-4-Voice | 9B | 48.47 | - | 13.15 |

Pretrain+TtT 在 ASR (WS) 上 WER 为 19.85%，显著优于 SpeechGPT 的 123.15%，但高于 GLM-4-Voice 的未报告值（推测因规模差异）。在 Audio-QA (WQ) 上，Pretrain+TtT 得 21.43，低于 GLM-4-Voice 的 48.47，但高于同规模 Qwen2.5-3B (AR) 的 11.61。

消融实验显示，移除 BANOM、PPM 或 SST 任一策略均导致性能下降。例如，移除 BANOM 后 Audio-QA (WQ) 从 21.43 降至 17.46，ASR (WS) 从 19.85 升至 26.73，表明训练-测试差异的缓解对生成质量至关重要。

评估边界：指标涵盖任务性能与感知质量（NMOS/UTMOS），但缺乏长上下文连贯性专项测试。代码开源，超参数完整，可复现性高。

## 关联研究分析

从问题动机看，TtT 与 SALAD 形成方法论对比。SALAD 通过两阶段蒸馏解决模态不等价导致的知识遗忘，侧重输入端对齐；TtT 则通过架构设计解耦生成依赖，侧重输出端生成效率。SALAD 在 LibriSpeech ASR 上 WER 2.5%，而 TtT 在 WS 上 WER 19.85%，差异源于任务侧重（纯 ASR vs S2S 生成）及骨干规模。TtT 的高 WER 是否源于 NAR 生成对转录精度的牺牲，论文未给出直接回答。

从方法设计看，TtT 与 DiffuSpeech 同属扩散路线，但 DiffuSpeech 侧重“静默思考”范式，TtT 侧重依赖结构解耦。DiffuSpeech 在 LibriSQA 上准确率 62.1%，TtT 在 URO-Bench Pro Reasoning 上得分 43.76，两者评估基准不同，难以直接对比。TtT 的模态感知注意力机制是否能在视频-文本等其他多模态任务中泛化，论文未探索。

## 总结

TtT 解决的核心矛盾是统一 AR 目标对音频源-目标依赖的干扰。其切入点在于利用吸收式离散扩散的任意顺序 AR 性质，将文本 AR 与音频 NAR 统一于单一 Transformer，并证明训练目标的理论上限。实验表明，Pretrain+TtT (3B) 在 Audio-QA (WQ) 上得 21.43，ASR (WS) 上 WER 19.85，优于同规模 AR/NAR 基线。边界在于，其在 AAC 上略低于依赖大模型辅助的 SLAM-Omni，且缺乏长上下文连贯性测试。当支持集增大到 5-shot 时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_20777631)