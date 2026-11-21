# HuggingFace最新推荐论文 ｜OmniXRef: A Unified Framework for Multimodal Multi-Reference Video Editing ｜OmniXRef：多模态多参考视频编辑的统一框架

研究机构：美国布朗大学、Adobe研究院

作者：Xiaoyan Cong、Tianyu Wang、Hyeonho Jeong 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.22744)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.22744)

> 导读：视频编辑正从单一文本指令驱动向多模态参考驱动演进，核心挑战在于如何统一处理可变数量、不同模态（文本、图像、视频）且属性各异（相机、运动、内容等）的参考输入，同时防止参考内容泄漏。现有方法多局限于单参考或固定模态，缺乏对视频作为动态控制信号的统一建模。OmniXRef 提出统一参考库接口，结合多模态大语言模型与单流扩散 Transformer，通过 Mix-Patchify 和 R2-RoPE 解决计算效率与泛化瓶颈。该框架在自建基准上显著优于商业模型与专家基线，确立了视频参考编辑的新范式，但其对大规模合成数据的依赖及实时性表现仍需进一步验证。

## 研究背景

当用户希望修改视频中的动态属性（如相机轨迹、光影变化）时，纯文本指令往往难以精确描述时空演变，而单张图像参考又无法承载时间维度的信息。这一困境促使研究重心从文本/图像指令驱动转向视频参考驱动。视频参考能提供相机运动、动态光照等时序信息，但如何将这些信息从参考视频解耦并迁移至源视频，同时保持源视频其余内容不变，构成了“参考属性迁移”的核心难题。现有方法如 CamCloneMaster 和 RefVFX 仅针对单一任务（如相机或特效）设计，缺乏统一框架支持多参考组合。

随着扩散 Transformer (DiT) 架构的兴起，统一多任务编辑成为可能。然而，现有统一框架（如 EditVerse, VIVA）主要支持文本或图像参考，对视频参考的支持有限，且难以处理多参考输入时的位置编码冲突与计算开销激增问题。OmniXRef 针对这一空白，提出多模态多参考视频编辑的统一建模，旨在通过一个模型同时处理文本、图像和视频参考，实现相机、运动、内容、风格及视觉特效的灵活组合编辑。

## 核心方法

### 统一参考库接口与模型架构

OmniXRef 将文本、图像和视频参考统一抽象为“参考库”（Reference Bank）。每个参考库 $B_i$ 包含任务定义 $T_i^{task}$、编辑指令 $T_i^{edit}$ 和可选的视觉参考 $V_i$。模型首先使用冻结的 Qwen3-VL-8B 多模态大语言模型 (MLLM) 编码包含系统提示、源视频及所有参考库的交错序列，提取语义上下文 $X$。随后，单流 DiT 接收语义上下文、源视频 VAE 潜变量及噪声目标视频 token，通过全自注意力机制联合处理，生成编辑后的视频。该架构继承了 EditVerse 的单流 DiT 设计，但通过参考库接口扩展了对多模态、多数量参考的支持。

### Mix-Patchify：任务自适应的参考 Token 压缩

在 DiT 中，参考视频通常被编码为大量 token，导致计算复杂度随参考数量线性甚至二次方增长。传统做法对所有视觉输入使用统一的细粒度 patch 大小（如 $1 \times 1 \times 1$），这保留了所有细节但也引入了冗余。OmniXRef 提出 Mix-Patchify (MP)，根据编辑任务类型动态调整参考视频的 patch 粒度 $p = (p_t, p_h, p_w)$。对于需要保留外观细节的任务（如 Content），使用细粒度 patch；对于主要关注全局或动态属性的任务（如 Camera, Motion, Style, VFX），使用粗粒度 patch（如 $1 \times 2 \times 2$ 或更大），但始终保持时间维度 $p_t=1$ 以保留动态信息。

$$
\text{Token Count Reduction} \propto p_t \cdot p_h \cdot p_w
$$

该公式表明，通过增大空间 patch 尺寸，参考 token 数量可大幅减少。MP 不仅降低了训练和推理成本，还作为一种空间先验，帮助模型更快收敛，因为模型无需从冗长的参考序列中自行学习如何提取全局属性。

### R2-RoPE：预留槽位的位置编码泛化

多参考编辑面临训练-推理分布不一致问题：训练时参考数量固定，推理时可能更多。默认 4D RoPE 使用顺序索引 $\rho_s$ 标识资产，当推理时参考数量超过训练最大值时，会产生分布外索引。OmniXRef 提出 R2-RoPE (RoPE with Reserved Reference Slots)，为系统提示、源视频和噪声 token 预留固定槽位，并为参考库预留一个大于训练最大参考数的槽位池（如 8 个）。

$$
q_j = (y_j, x_j, \tau_j, \rho_i), \quad \rho_i \in \text{Reserved Slots}
$$

训练时，每个参考库 $B_i$ 随机分配一个预留槽位 $\rho_i$，所有属于该库的 token 共享此第四轴坐标。这种设计确保推理时即使参考数量增加，其位置索引仍在训练见过的分布范围内，从而支持比训练时更多的参考输入，解决了泛化瓶颈。

## 实验评估

OmniXRef 在自建基准 OmniXRef-Bench（125 个样本，涵盖 Camera, Motion, Content, Style, VFX）上进行评估，并与商业模型（Seedance 2.0/2.5, MiniMax-H3）及任务特定专家模型（CamCloneMaster, MotionFollower, RefVFX）对比。评估指标包括参考遵循度 (RA)、视觉质量 (VQ) 和源保留度 (SP)，由 Gemini 3.8 Flash 作为 VLM 裁判打分。

| 模型 | Content Score | Style Score | VFX Score | Camera Score | Motion Score | Overall Avg. Score |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| RefVFX | 1.98 | 2.24 | 2.49 | - | - | - |
| CamCloneMaster | - | - | - | 3.20 | - | - |
| MotionFollower | - | - | - | - | 2.14 | - |
| MiniMax-H3 | 2.23 | 0.94 | 1.32 | 2.07 | 0.69 | 1.45 |
| Seedance 2.0 | 3.73 | 3.22 | 2.92 | 3.27 | 2.45 | 3.12 |
| Seedance 2.5 | 4.04 | 2.30 | 2.22 | 3.07 | 2.00 | 2.73 |
| **OmniXRef** | **4.49** | **3.75** | **3.55** | **3.81** | **3.30** | **3.78** |

OmniXRef 在总体平均得分 (3.78) 上显著优于 Seedance 2.5 (2.73) 和 MiniMax-H3 (1.45)，并在 Content, Style, Motion 等类别上领先。在相机轨迹误差方面，OmniXRef 的旋转误差 (RotErr) 为 0.874，远低于 CamCloneMaster 的 2.086 和 Seedance 2.5 的 4.373，表明其更精确地遵循了参考相机运动。

消融实验显示，移除 Mix-Patchify 导致 Content 类别得分从 4.48 降至 2.97，证明任务自适应 patch 对细节保留至关重要。移除 R2-RoPE 导致整体得分从 3.77 降至 3.18，验证了预留槽位对多参考泛化的必要性。课程学习策略的移除也使整体得分从 3.77 降至 3.13，表明分阶段训练有助于模型稳定收敛。

评估边界方面，OmniXRef-Bench 为自建基准，其 VLM 评分标准可能与领域通用基准（如 FiVE-Bench）存在差异。此外，论文未提供与免训练方法（如 TokenFlow）的直接对比，因任务设定不同。推理延迟分析显示，Mix-Patchify 在参考数量增加时能显著降低计算成本，但高分辨率长视频的实时性仍具挑战。

## 关联研究分析

从问题动机看，OmniXRef 与 VIVA 和 EditVerse 同属统一多任务编辑框架，但 VIVA 和 EditVerse 主要处理文本和图像参考，缺乏对视频参考这一动态控制信号的统一建模。OmniXRef 将视频提升为一等公民参考模态，填补了视频作为控制信号在统一框架中的空白。这一差异源于任务特性的根本不同：视频参考包含时序动态，需要模型具备时空解耦能力，而文本/图像参考主要提供静态语义或外观。

从方法设计看，OmniXRef 的 R2-RoPE 与 CamCloneMaster 的相机控制机制形成对比。CamCloneMaster 针对相机任务专门设计，而 OmniXRef 通过统一的位置编码机制支持多任务。然而，OmniXRef 依赖大规模合成数据（10M 样本）进行训练，这与领域共识中强调的“数据稀缺”瓶颈相呼应，但也引发了对合成数据真实性的担忧。合成数据中的相机轨迹和运动模式是否足以覆盖真实世界的复杂动态，论文未给出充分验证。

## 总结

OmniXRef 解决了多模态多参考视频编辑中参考模态不统一、计算开销大及泛化能力弱的问题。通过统一参考库接口、Mix-Patchify 和 R2-RoPE，该框架在 OmniXRef-Bench 上取得了 3.78 的总体得分，显著优于商业基线，并实现了 0.874 的低相机轨迹误差。其核心贡献在于确立了视频作为动态控制信号的统一建模范式。然而，该框架依赖大规模合成数据，且仅支持最多两个视觉参考的组合，当参考数量进一步增加或面对真实世界复杂动态时，其泛化边界与合成数据偏差的影响，仍有待进一步验证。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.22744)