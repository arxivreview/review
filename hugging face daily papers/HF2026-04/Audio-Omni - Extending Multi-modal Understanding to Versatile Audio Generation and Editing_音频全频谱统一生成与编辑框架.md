# HuggingFace最新推荐论文 ｜Audio-Omni: Extending Multi-modal Understanding to Versatile Audio Generation and Editing ｜音频全频谱统一生成与编辑框架

研究机构：香港科技大学、北京大学

作者：Zeyue Tian、Binxin Yang、Zhaoyang Liu 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.10708)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10708)

> 现有音频模型在理解、生成与编辑能力上彼此割裂，且无法同时覆盖通用声音、音乐与语音三个分布差异显著的子域。Audio-Omni 通过冻结多模态大语言模型（MLLM）与可训练扩散 Transformer（DiT）的解耦架构，配合分离高层语义与低层信号的双流条件机制，在单一端到端框架内实现了全频谱的统一处理。该设计使模型在多项生成任务上达到或超越专用模型水平，但其编辑能力仅依赖自建数据集验证，跨域泛化性存疑。

## 研究背景

当模型需要同时处理“识别鸟鸣”与“将鸟鸣替换为雨声”两类指令时，理解任务依赖高层语义表征，而编辑任务依赖帧级声学对齐，二者在特征空间中天然冲突。解决这一矛盾的关键在于潜空间建模：通过变分自编码器（VAE）将高维波形压缩至低维潜变量，使生成过程在平滑的连续空间中执行。然而，潜空间的不规则性会导致去噪轨迹漂移，因此 Rectified Flow 通过直线化噪声到数据的 ODE 轨迹，以恒定速度场 $v = x_1 - x_0$ 替代传统扩散的随机路径，显著提升了少步生成的稳定性。

音频领域长期面临“专用模型碎片化”困境：通用声音、音乐与语音各自拥有独立的生成器，且理解与生成能力通常由不同模型承担。现有统一模型如 Ming-Omni 仅覆盖语音子域，MuMuLLaMA 局限于音乐与通用声音，且多采用工具调用式集成，缺乏端到端优化。Audio-Omni 的切入点在于：不追求单一 Transformer 端到端处理所有任务，而是将 MLLM 冻结为语义推理核心，仅训练 DiT 作为生成/编辑执行器，通过混合条件机制桥接两者，从而在保留 MLLM 多模态知识的同时，实现全频谱音频的生成与编辑。

## 核心方法

### 解耦架构与双流条件注入

统一音频生成与编辑的通用流程通常采用单一 Transformer 同时处理理解与生成，但音频三子域的分布差异导致任务冲突。Audio-Omni 的关键差异在于：MLLM 完全冻结，仅提取倒数第二层隐状态 $F_{mm} \in \mathbb{R}^{L_{mm} \times D_{mm}}$ 作为条件，DiT 独立训练。该设计动机是：冻结 MLLM 可保留其预训练的多模态世界知识，避免生成任务微调破坏理解能力，同时通过特征投影器将语义信号解耦至生成模块。

### 混合条件机制

高层语义流 $c_{high}$ 由 $F_{mm}$ 与转录编码器特征 $F_{trans}$ 拼接而成，通过交叉注意力注入 DiT，提供全局指令引导；低层信号流 $c_{low}$ 由 Mel 频谱特征 $F_{mel}$ 与 Synchformer 同步特征 $F_{sync}$ 拼接，与时间嵌入相加后直接拼接至噪声潜变量 $x_t$。该机制解决了单一条件注入无法同时满足“语义对齐”与“帧级时序控制”的失效：交叉注意力允许模型在每步生成中灵活查询抽象指令，而拼接操作提供强逐帧引导，确保编辑与同步任务的精确对齐。

$$
c_{high} = \text{Concat}(F_{mm}, F_{trans}), \quad c_{low} = \text{Concat}(F_{mel}, F_{sync})
$$

DiT 以 $[x_t, c_{low} + e_t]$ 为主输入，$c_{high}$ 为交叉注意力上下文，预测速度场 $v_\theta(x_t, t, c)$。训练目标为 Rectified Flow 的均方误差：

$$
\mathcal{L} = \mathbb{E}_{t, x_0, x_1} \left[ \| v_\theta(x_t, t, c) - (x_1 - x_0) \|^2 \right]
$$

该公式要求网络学习从噪声 $x_1$ 到数据 $x_0$ 的恒定速度，直线化轨迹使少步采样（如 4 步）即可收敛，避免了传统扩散模型多步采样的延迟瓶颈。

## 实验评估

实验在 AudioCaps（T2A）、Musicaps（T2M）、VGGSound（V2A）、Seed-TTS（TTS）及自建 AudioEdit（编辑）上评测，基线覆盖专用模型（Tango2、MusicGen、F5-TTS）与统一模型（Ming-Omni、Unified-IO2），但缺失 PrismAudio、AudioX-Turbo 等最新 SOTA。主结果显示，Audio-Omni 在 T2A（FAD 1.86）、T2M（FAD 1.94）、TTS（WER 1.77%）上均优于或持平专用模型，在 V2A（FAD 1.71）上优于 MMAudio（2.04），但低于 AudioX（1.13）。

| 任务 | 指标 | Audio-Omni | 最强专用基线 | 最强统一基线 |
|---|---|---|---|---|
| T2A | FAD↓ | 1.86 | 1.86 (AudioX) | 7.81 (Unified-IO2) |
| T2M | FAD↓ | 1.94 | 3.23 (Stable-Audio-Open) | 3.17 (Unified-IO2) |
| TTS | WER↓ | 1.77 | 1.83 (F5-TTS) | 4.31 (Ming-Omni) |
| 编辑 | FAD↓ | 3.27 | 3.51 (SDEdit) | - |

消融实验揭示关键设计决策：仅用真实数据训练编辑任务时 FAD 为 2.67，仅用合成数据时 FAD 为 3.80，混合数据（1:3 比例）降至 2.48，表明合成数据虽引入域差距，但规模优势可被真实数据校准。条件注入策略消融显示，将 $F_{mm}$ 与 $F_{trans}$ 作为交叉注意力、$F_{sync}$ 与 $F_{mel}$ 作为拼接输入时，T2A FAD 为 28.90，若全部拼接则升至 40.91，验证了双流分离对语义-信号解耦的必要性。

评估边界存在明显局限：编辑任务仅在自建 AudioEdit 上评测，缺乏跨数据集泛化验证；V2A 任务未报告 CLAP Score 与 DeSync Score，无法与 PrismAudio（CLAP 0.47）直接对比；代码与模型虽承诺开源，但论文未披露训练超参数与 GPU 配置，可复现性依赖后续发布。

## 关联研究分析

从问题动机看，Audio-Omni 与 PrismAudio 均针对 V2A 任务，但 PrismAudio 侧重认知推理驱动的美学与空间优化，通过 LLM 生成思维链提升感知质量；Audio-Omni 侧重统一框架，通过解耦架构实现多任务覆盖。差异根源在于任务特性：PrismAudio 假设视频-音频对齐是核心瓶颈，故引入推理机制；Audio-Omni 假设多域分布差异是核心瓶颈，故采用冻结 MLLM 保留跨域知识。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

从方法设计看，Audio-Omni 与 Ming-Omni 同属统一多模态模型，但 Ming-Omni 采用端到端 Transformer 处理语音生成，Audio-Omni 采用解耦架构处理全频谱。差异根源在于架构选择：Ming-Omni 的端到端设计允许深层特征交互，但易受任务冲突影响；Audio-Omni 的解耦设计牺牲了交互深度，但通过混合条件机制补偿了语义-信号对齐的不足。冻结 MLLM 是否违背了“端到端优化”的统一模型共识，论文未给出回答。

## 总结

Audio-Omni 要解决的核心矛盾是音频三子域分布差异导致的统一模型任务冲突。其切入点在于：不追求单一 Transformer 端到端处理，而是冻结 MLLM 保留多模态知识，仅训练 DiT 执行生成/编辑，通过混合条件机制解耦语义与信号。该设计使模型在 T2A（FAD 1.86）与 TTS（WER 1.77%）上达到专用模型水平，在编辑任务（FAD 3.27）上超越 SDEdit（3.51）。其边界在于：编辑能力仅依赖自建 AudioEdit 验证，V2A 任务未报告同步指标，且冻结 MLLM 限制了深层特征交互。当支持集增大到 5-shot 时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10708)