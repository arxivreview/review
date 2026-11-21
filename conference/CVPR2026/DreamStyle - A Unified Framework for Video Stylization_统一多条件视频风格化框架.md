# CVPR2026最新论文 ｜DreamStyle: A Unified Framework for Video Stylization ｜统一多条件视频风格化框架

作者：Mengtian Li、Jinshu Chen、Songtao Zhao 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.02785)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.02785)

> 视频风格化旨在将输入视频转换为特定艺术风格，同时保留原始运动与内容。现有方法受限于单一模态条件（文本或图像）的模糊性或获取难度，且缺乏高质量配对训练数据，导致风格一致性与时序连贯性难以兼得。本文提出DreamStyle，通过统一I2V模型架构与Token-specific LoRA机制，将文本、风格图像及首帧三种条件整合至单一前向过程，并构建合成数据流水线解决数据稀缺问题。该框架在风格一致性上显著优于专用模型，但其依赖合成数据的泛化边界及长视频扩展能力尚存疑。

## 研究背景

视频风格化任务的核心难点在于平衡风格迁移的保真度与原始视频运动的稳定性。潜在扩散模型（Latent Diffusion Models, LDMs）通过在变分自编码器（Variational Autoencoder, VAE）压缩的潜在空间执行去噪，降低了高分辨率视频生成的计算复杂度，成为当前主流范式。然而，LDMs通常基于U-Net架构，其局部感受野限制了长序列时空依赖的建模能力。随着扩散Transformer（Diffusion Transformer, DiT）的引入，全局自注意力机制使得模型能够统一建模时空特征，为复杂视频生成任务提供了更强的扩展性基础。

早期视频风格化方法多依赖DDIM反转或图像风格化技术的时序传播，如TokenFlow和AnyV2V，但这些方法无法独立执行风格化，且依赖耗时的反转过程。StyleMaster等基于DiT的方法虽提升了质量，但需额外引入时间注意力模块以弥补图像到视频的差距，偏离了主流架构设计。更关键的是，现有研究普遍缺乏高质量的风格化-原始视频配对数据集，导致模型在训练时面临风格一致性与运动动态性之间的权衡。DreamStyle的切入点在于构建一个无需额外时间模块的统一V2V框架，并通过系统化的数据合成流水线解决数据瓶颈，从而在保留I2V模型效率的同时实现多条件风格控制。

## 核心方法

### 方法参照系

本文问题属于视频到视频（Video-to-Video, V2V）生成中的条件控制任务。标准I2V模型通常仅接受首帧图像和文本提示作为条件，通过交叉注意力注入语义信息。本文的关键差异在于将V2V任务重构为多条件I2V问题，需同时处理原始视频、风格图像及首帧三种异构条件，且需在单一模型中解耦不同条件的语义干扰，避免特征纠缠导致的内容失真。

### 统一条件注入机制

在标准I2V流程中，条件通常通过交叉注意力或通道拼接注入，但多条件共存时易产生语义混淆。DreamStyle在Wan14B-I2V骨干的基础上，设计了四种条件注入路径：文本条件复用原始交叉注意力层；首帧条件通过图像通道注入并设置掩码为1.0；风格图像条件通过通道拼接与帧拼接结合，既保留像素级细节又通过CLIP分支注入高层语义；原始视频条件则通过通道拼接与掩码0.0注入，以最小化对基础模型的修改。这种设计使得模型能在单次前向中同时感知内容结构与风格特征，解决了单一模态条件无法精确描述抽象风格或获取困难的问题。

$$
\mathbf{z}_{v}^{t} = \text{add\_noise}(\mathbf{z}_{raw}, t) \oplus_c \mathbf{1}_{4 \times F \times H \times W}
$$

该公式表示原始视频潜变量在时间步 $t$ 添加噪声后，与全1掩码张量进行通道拼接，形成模型输入的视频条件部分，确保模型能区分“需保留的内容”与“需生成的风格”。

### Token-specific LoRA模块

标准LoRA在所有层共享低秩矩阵，当输入包含不同语义角色的Token（如首帧、风格图、视频帧）时，共享矩阵会导致跨Token的特征干扰。DreamStyle引入Token-specific LoRA，在全注意力和前馈网络（FFN）层中，使用共享的下投影矩阵 $\mathbf{W}_{down}$ 和针对不同Token类型 $i \in \{0, 1, 2\}$ 的独立上投影矩阵 $\mathbf{W}_{up[i]}$。这种结构类似于手动路由的LoRA混合专家（Mixture of Experts, MoE），使模型能为每种条件学习自适应特征，同时因共享大部分参数而保持训练稳定性。

$$
\mathbf{x}_{out} = \mathbf{W}_{up[i]} \mathbf{W}_{down} \mathbf{x}_{in}
$$

该公式表明，输入Token $\mathbf{x}_{in}$ 经共享下投影后，根据Token类型 $i$ 选择特定的上投影矩阵进行残差计算，从而在轻量级微调中实现多任务解耦，避免了标准LoRA中不同风格条件间的语义混淆。

## 实验评估

实验在480P分辨率、最长81帧的视频上进行，测试集包含50个文本引导样本、90个风格图像引导样本及90个首帧引导样本。基线覆盖商业模型（Luma, Pixverse, Runway）及开源模型（StyleMaster, VACE, VideoX-Fun），但缺乏与最新SOTA主体一致性方法（如Kaleido, Aura）的直接对比，可能低估了统一框架在复杂身份保持场景下的竞争力。

| 条件 | 方法 | CLIP-T/CSD Score | DINO Score | Dynamic Degree | Image Quality |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Text | DreamStyle | **0.167** | **0.584** | 0.738 | **0.952** |
| Text | Runway | 0.154 | 0.504 | 0.725 | 0.940 |
| Style Image | DreamStyle (V2V) | 0.515 | 0.867 | 0.704 | 0.938 |
| Style Image | StyleMaster (T2V) | 0.198 | 0.289 | **0.723** | 0.936 |
| First Frame | DreamStyle | **0.851** | 0.856 | **0.731** | 0.919 |
| First Frame | VACE | 0.689 | **0.889** | 0.716 | **0.922** |

在文本引导任务中，DreamStyle的CLIP-T得分0.167高于Runway的0.154，表明其语义遵循能力更强；在风格图像引导任务中，DreamStyle (V2V)的CSD得分0.515显著优于StyleMaster (T2V)的0.198，验证了V2V范式在风格一致性上的优势。然而，在动态度指标上，DreamStyle (V2V)的0.704略低于StyleMaster (T2V)的0.723，暗示统一框架可能在运动动态性上存在轻微妥协。

消融实验未单独报告，但训练策略采用两阶段：CT阶段使用40K大规模数据建立基础能力，SFT阶段使用5K高质量数据提升上限。这种设计表明数据规模与质量对风格化效果均有贡献，但缺乏对Token-specific LoRA各组件（如共享下矩阵 vs 独立上矩阵）的独立消融，无法量化解耦机制的具体贡献度。

评估指标涵盖CSD、ViCLIP、DINOv2及VBench子项，但缺乏针对长视频叙事连贯性的统一标准。代码未公开，超参数（如LoRA rank 64, 学习率 $4 \times 10^{-5}$）已披露，但GPU配置未明确，可能影响复现性。合成数据流水线依赖InstantStyle和Seedream 4.0，其风格多样性受限于上游图像模型，可能限制DreamStyle对未见风格的泛化能力。

## 关联研究分析

从问题动机看，DreamStyle与StyleMaster均基于DiT骨干，但StyleMaster依赖StillMoving模块显式建模时间注意力，而DreamStyle通过统一条件注入机制在原生I2V架构上实现V2V功能，避免了额外时间模块的计算开销。这一差异源于任务定义：StyleMaster将风格化视为图像到视频的扩展，需弥补时序差距；DreamStyle则将风格化视为多条件视频生成，利用I2V模型固有的时空建模能力。然而，DreamStyle在动态度指标上的轻微劣势（0.704 vs 0.723）暗示，移除显式时间模块可能在复杂运动场景中损失部分时序一致性，这一权衡在论文中未深入探讨。

从方法设计看，DreamStyle的Token-specific LoRA与HydraLoRA思路相似，但应用于视频风格化的多条件解耦场景。与Kaleido等主体一致性方法相比，DreamStyle关注风格条件的解耦，而非身份特征的保持。Kaleido通过多参考图像特征解耦身份编码，而DreamStyle通过Token类型区分风格条件。两者均面临特征干扰问题，但解决路径不同：Kaleido依赖参考图像质量，DreamStyle依赖Token-specific矩阵的容量。当风格条件与内容条件高度相关时（如风格图像中包含特定人物），Token-specific LoRA是否足以解耦风格与身份，论文未提供实验证据。

## 总结

DreamStyle旨在解决视频风格化中多模态条件统一与数据稀缺的矛盾。现有方法受限于单一条件模态或依赖耗时的反转过程，而DreamStyle通过统一I2V架构与Token-specific LoRA，在保留基础模型效率的同时实现多条件控制。实验显示，其在文本引导任务中CLIP-T得分0.167，风格图像引导任务中CSD得分0.515，均优于基线。然而，其动态度指标略低于专用模型，且合成数据流水线依赖上游图像模型的风格多样性，可能限制对未见风格的泛化。当输入视频包含复杂人物交互时，Token-specific LoRA能否有效解耦风格与身份特征，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.02785)