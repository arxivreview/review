# HuggingFace最新推荐论文 ｜Woosh: A Sound Effects Foundation Model ｜音效生成基础模型：Woosh

研究机构：索尼AI

作者：Gaëtan Hadjeres、Marc Ferras、Khaled Koutini 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.01929)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.01929)

> 音效生成领域长期面临开源模型采样率低、专业场景适配性差的困境，现有开源方案如StableAudio-Open虽提供权重但难以满足48kHz高保真需求。本文切入点在于构建一套针对专业音效优化的全链路开源工具包，通过非量化STFT编码器与MeanFlow蒸馏实现高保真与低延迟的平衡。其价值在于填补了专业音效开源生态的空白，但私有数据依赖与指标争议限制了其通用性验证。

## 研究背景

音频生成模型需在低维潜空间进行去噪以平衡计算成本与信号保真度。传统离散量化编解码器（如EnCodec）虽压缩率高，但量化误差导致高频瞬态丢失，而连续潜空间模型（如StableAudio-Open）虽保真度较高，却受限于多步采样延迟，难以满足实时交互需求。

当前开源音频生成模型存在显著断层：多数高性能模型未开放权重，而开放权重的模型（如AudioLDM2、TangoFlux）多聚焦通用音频或音乐，缺乏针对音效（Sound Effects）瞬态特性的优化。专业音效制作要求48kHz采样率与极低延迟，现有开源方案在编码器压缩率与推理效率上均存在瓶颈。Woosh模型旨在解决这一矛盾，通过定制化的音频编码器与蒸馏策略，在保持高保真的同时实现即时生成。

## 核心方法

### 非量化STFT音频编码器

Woosh-AE基于VOCOS架构，摒弃了主流编解码器中常见的残差向量量化（RVQ）离散化步骤，直接预测STFT复数系数。这一设计动机在于避免量化误差对音效中高频瞬态成分的破坏，同时利用iSTFT逆变换消除转置卷积上采样带来的混叠伪影。

$$
\mathbf{X} = \text{softplus}(\mathbf{m}) \cdot (\frac{\mathbf{x}'}{\sqrt{\mathbf{x}'^2 + \mathbf{y}'^2}} + j \frac{\mathbf{y}'}{\sqrt{\mathbf{x}'^2 + \mathbf{y}'^2}})
$$

该公式表明模型预测幅度$\mathbf{m}$及归一化的实部$\mathbf{x}'$、虚部$\mathbf{y}'$，通过软限制函数保证幅度非负，同时通过归一化避免相位包裹问题。相比SAO-VAE的64维潜空间，Woosh-AE采用128维潜空间与100Hz帧率，压缩率仅为0.26（SAO-VAE为0.03），以更低的压缩比换取更高的重建保真度。

### 多模态流匹配与蒸馏

Woosh-Flow采用FLUX-Kontext扩展架构，通过联合自注意力机制融合文本、视频与音频潜变量。视频条件通过SynchFormer提取24Hz帧率特征，经线性投影后与文本、音频流在MultiStream块中进行联合注意力计算。

$$
\mathbf{Z}_m = \text{FFN}_m(\text{LN}(\mathbf{Z}_{\text{joint}}))
$$

其中$\mathbf{Z}_{\text{joint}}$为三模态拼接后的注意力输出，$\text{FFN}_m$为模态特定的前馈网络。这种设计允许视频模态独立处理注意力输出，避免跨模态干扰。为加速推理，模型采用MeanFlow蒸馏，将100步教师模型压缩为4步学生模型，通过重噪声策略（权重[0, 0.5, 0.5, 0.3]）在少步采样中保持分布匹配质量。

## 实验评估

实验在AudioCaps（950样本）与私有InternalSFX（5000样本）上进行，基线包括SAO、TangoFlux、Descript及EnCodec。在AudioCaps上，Woosh-AE-Public的MelDist为0.032，较SAO-VAE的0.217降低85%，SI-SDR达20.79dB，显著优于SAO-VAE的-0.08dB。在InternalSFX上，Woosh-AE-Private的SI-SDR为16.03dB，而SAO-VAE仅为-2.92dB，表明专业数据训练对高保真重建至关重要。

| 模型 | 数据集 | MelDist | STFTDist | SI-SDR (dB) |
|---|---|---|---|---|
| SAO-VAE | AudioCaps | 0.217 | 1.55 | -0.08 |
| Woosh-AE-Public | AudioCaps | 0.032 | 1.18 | 20.79 |
| SAO-VAE | InternalSFX | 0.121 | 0.462 | -2.92 |
| Woosh-AE-Private | InternalSFX | 0.024 | 0.288 | 16.03 |

在T2A生成任务中，Woosh-Flow-Public在AudioCaps上的FD为109.1，较TangoFlux的131.9降低17%，CLAP分数0.3719较TangoFlux的0.3471提升6%。蒸馏模型Woosh-DFlow-Public在4步推理下，FD为282.7，虽高于原始模型，但仍优于SAO的341.0。在V2A任务中，Woosh-VFlow在FoleyBench上的FD为24.136，低于MMAudio-M的30.480，但DeSync指标存在争议，论文指出SynchFormer指标可能无法可靠反映人类感知同步。

| 模型 | 数据集 | FD | KL | CLAP |
|---|---|---|---|---|
| TangoFlux | AudioCaps | 131.9 | 1.700 | 0.3471 |
| Woosh-Flow-Public | AudioCaps | 109.1 | 1.599 | 0.3719 |
| MMAudio-M | FoleyBench | 30.480 | 1.983 | 0.292 |
| Woosh-VFlow | FoleyBench | 24.136 | 1.774 | 0.325 |

评估边界方面，KL与CLAP指标内部使用公开数据训练的模型，对私有商业数据可能存在偏差。SynchFormer同步指标在OGameData上预测去同步大于900ms，但人工检查未发现感知问题，表明该指标可靠性存疑。代码与权重已开源，但私有模型仅限内部使用，限制了可复现性。

## 关联研究分析

从编码器设计看，Woosh-AE的非量化STFT预测与主流离散量化Codec（如EnCodec、DAC）形成鲜明对比。离散量化通过RVQ将波形压缩为离散令牌，虽压缩率高但引入量化误差，而Woosh-AE以更高压缩率（0.26 vs 0.03）换取保真度，这暗示在音效瞬态敏感场景中，压缩率与保真度的权衡可能不同于通用音频。然而，非量化设计是否导致潜空间语义正则性下降，论文未提供消融实验验证。

从V2A同步机制看，Woosh-VFlow依赖SynchFormer特征作为视频条件，而MMAudio-M直接优化该指标。论文指出MMAudio-M的高同步分数可能源于架构对指标的过拟合，而非真实同步能力。这种指标与感知的脱节揭示了当前V2A评估体系的缺陷：自动化指标可能无法捕捉人类感知的微妙差异。Woosh-VFlow在FD/KL上的优势是否转化为感知同步优势，缺乏主观实验支持。

## 总结

Woosh模型旨在解决专业音效生成中开源模型保真度与效率的双重瓶颈，通过非量化STFT编码器与MeanFlow蒸馏实现高保真即时生成。在AudioCaps上，其FD较TangoFlux降低17%，SI-SDR较SAO-VAE提升20dB以上，证明了专业数据训练与编码器优化的有效性。然而，私有数据依赖与SynchFormer指标争议限制了其通用性验证。当非量化编码器在长音频生成中是否会导致潜空间漂移，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.01929)