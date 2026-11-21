# HuggingFace最新推荐论文 ｜CtrlVTON: Controllable Virtual Try-On via Visual-Instance-Prompt Segmentation ｜可控虚拟试穿：基于实例级视觉提示分割与编辑范式的空间控制框架

研究机构：韩国科学技术院

作者：Seungyong Lee、Hyun Jun Jang、Sangoh Kim 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.09362)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.09362)

> 虚拟试穿（Virtual Try-On, VTO）旨在生成人物穿着指定服装的真实图像，但现有系统普遍缺乏对服装穿着方式（如尺寸、风格、空间位置）的精细控制。Inpainting范式因掩码紧度与身份保持的固有冲突导致复杂姿态下伪影频发，而Editing范式虽解决此问题却丧失了像素级空间控制能力。本文通过将VTO重构为图像编辑问题，并引入实例级视觉提示分割（VIP-Seg）任务获取精确掩码，实现了在编辑框架下的空间可控性。该框架在保真度上匹配最强专有编辑系统，但在视频时序一致性与物理合身性维度上未作验证。

## 研究背景

当用户希望调整服装的穿着状态（如将衬衫塞入裤腰或改变外套的开合状态）时，传统VTO方法无法响应此类细粒度指令。这一困境源于Inpainting范式对掩码的依赖：掩码过小会泄漏原服装像素，掩码过大则擦除身份线索迫使模型幻觉，且输出受掩码形状及外部上下文（如阴影）偏置。为解决此权衡，近期研究转向Editing范式，通过全图条件化让模型自由修改图像同时从参考图保留身份与背景，但代价是用户失去了指定服装具体位置与形态的能力。

VTO领域的演进主线是从显式几何对齐向隐式特征引导迁移。早期GAN方法依赖薄板样条（TPS）变形，易产生纹理模糊；潜空间扩散模型（LDM）引入后，问题重构为条件生成，保真度显著提升。随着扩散Transformer（DiT）架构普及，OmniTry等Editing方法利用全图条件化避免了Inpainting的掩码误差，但M&M VTO等仅提供粗粒度文本布局，无法表达精确空间放置，更不支持服装层叠。本文切入点在于：如何在Editing范式下恢复Inpainting模型的像素级空间控制，同时避免其身份漂移与伪影缺陷。

## 核心方法

### 编辑范式重构与三元组数据构建

本文VTO任务与标准Inpainting流程的关键差异在于输入形式：Inpainting输入为擦除服装区域后的图像 $p_{masked}$，而本文输入为穿着不同服装的参考人物图像 $p_{ref}$。设计动机是消除掩码紧度与身份保持的脆弱权衡。数据构建需合成三元组 $(p_{ref}, g_{ref}, p)$，其中 $p$ 为目标图像，$g_{ref}$ 为参考服装，$p_{ref}$ 为同一人物、姿态、背景但穿着不同服装 $g_{unpaired}$ 的图像。$p_{ref}$ 通过现成Inpainting系统填充 $p$ 中 $g_{unpaired}$ 对应的掩码区域生成，确保姿态与背景一致性。该设计使模型学习从 $p_{ref}$ 选择性传递身份、姿态与背景，仅修改目标区域以匹配 $g_{ref}$，从根本上规避了Inpainting中掩码边界导致的结构畸变。

### 实例级视觉提示分割（VIP-Seg）

VIP-Seg任务定义为：给定支持图像 $I_S$（如平铺服装），在查询图像 $I_Q$（如穿着该服装的人物）中分割出该特定实例。与类别级视觉参考提示分割（VRP-Seg）不同，VIP-Seg需在同类别干扰项（如颜色相似的层叠衬衫）、重度遮挡及非刚性变形下区分特定实例。设计动机是解决VRP-SAM等现有方法在层叠服装场景下因冻结编码器无法消歧而导致的分割失败。VIP-SAM架构将支持图像特征通过交叉注意力适配器注入SAM或SAM2骨干的中间层，使查询编码器从早期阶段即受支持图像条件化，而非仅在提示层匹配。

$$
\tilde{z}_{X} = \bigl[\, z_{X} \;\Vert\; z_{M_X} \,\bigr ], \qquad X \in \{p,\; p_{\text {ref}},\; g_{\text {ref}}\}
$$

该公式表示掩码注入机制：将图像 $X$ 的VAE编码潜变量 $z_X$ 与其对应掩码 $M_X$ 的潜变量 $z_{M_X}$ 进行通道级拼接。此操作在潜空间加倍通道维度，但不改变 $H \times W$ 的Token网格，因此注意力计算成本与条件Token数量均不增加，实现了像素级空间控制而不引入额外计算开销。

### 掩码条件化LoRA适配器

CtrlVTON在CtrlVTON-base（基于预训练图像编辑DiT微调）之上，通过训练LoRA适配器实现像素级控制。设计动机是解决Editing范式缺乏空间控制的问题，同时保持基座模型的生成质量。LoRA参数 $\Delta\theta$ 附加于MMDiT和Single-DiT块的线性投影层，优化标准流匹配目标：

$$
L_{\text{ctrl}} = \mathbb{E}_{\substack{x_1 \sim p_{\text{data}} \\ x_0 \sim \mathcal{N}(0, I) \\ t \sim \mathcal{U}[0, 1]}}\!\left [\,\bigl \| v_{\theta + \Delta \theta } \!\bigl (x_t, t \mid \tilde{c}\bigr ) - (x_1 - x_0) \bigr \|_2^2\,\right ]
$$

其中 $\tilde{c} = (z_{M_p}, \tilde{z}_{p_{ref}}, \tilde{z}_{g_{ref}}, \tau_{cls}, \tau_{task})$ 为增强条件，包含三个掩码潜变量及服装类别Token $\tau_{cls}$ 与任务Token $\tau_{task}$。该损失函数训练模型预测速度场 $v$，使其在给定掩码约束下生成符合指定穿着方式的目标图像。多服装场景下，通过RGB颜色编码掩码实现逐服装控制，无需架构修改。

## 实验评估

实验在VITON-HD、OmniTry Bench、DressCode-MR及Garments2Look上进行，基线覆盖Inpainting（IDM-VTON, CatVTON, Voost, CORAL）与Editing（Any2Any Tryon, OmniTry）两类路线，但未对比RefTon等最新DiT-based Inpainting方法。

| 方法 | 范式 | M-DINO↑ | M-CLIP-I↑ | GTC↑ | PBC↑ | PR↑ |
|---|---|---|---|---|---|---|
| IDM-VTON | Inpainting | 0.7198 | 0.8134 | 3.6798 | 4.0876 | 4.0882 |
| OmniTry | Editing | 0.7421 | 0.8823 | 4.0876 | 4.5876 | 4.0187 |
| CtrlVTON-base | Editing | 0.8054 | 0.8845 | 4.2057 | 4.7301 | 4.3753 |

CtrlVTON-base在VITON-HD上M-DINO达0.8054，显著高于OmniTry的0.7421与IDM-VTON的0.7198，表明编辑范式在保真度上优于Inpainting。在VITON-HD-edit掩码可控任务中，CtrlVTON的IoU达0.961，dHu为0.0022，优于Nano Banana Pro（IoU 0.871, dHu 0.0044）与GPT Image 1.5（IoU 0.811, dHu 0.0074），验证了掩码控制的空间精度。

VIP-SAM在Fashion-val数据集上mIoU达97.2（Hiera-L + DINOv3-H配置），高于VRP-SAM的94.4与ProSAM的94.6，证实早期特征注入对实例级分割的有效性。消融实验未单独报告，但多服装扩展无需架构修改，表明颜色编码掩码策略的通用性。

评估指标包含M-DINO、M-CLIP-I、GTC、PBC、PR及分割IoU/dHu，但未报告FID，可能因编辑范式下FID计算协议与Inpainting不同。代码已开源，但合成 $p_{ref}$ 的具体Inpainting模型版本与超参数未在正文详述，可复现性依赖补充材料。

## 关联研究分析

从问题动机看，CtrlVTON与OmniTry同属编辑范式，但OmniTry仅支持语义级控制（服装类别与任务类型），无法指定服装在身体上的具体位置与形态。CtrlVTON通过引入VIP-Seg获取实例级掩码，将控制粒度从语义级提升至像素级，解决了Editing范式“有保真度无控制力”的缺陷。这一差异源于任务特性：电商场景需精确控制服装穿着方式（如塞入/不塞入），而OmniTry面向通用图像编辑，未考虑此类细粒度需求。

从方法设计看，CtrlVTON与RefTon等Inpainting方法在掩码使用上存在根本分歧。RefTon依赖精确掩码指定试穿区域，但掩码误差导致结构畸变；CtrlVTON将掩码作为空间控制接口而非区域擦除工具，通过全图条件化保留身份线索，仅在掩码区域施加修改约束。这一设计选择使CtrlVTON在复杂姿态下更鲁棒，但代价是依赖VIP-SAM的分割精度。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

本文核心矛盾是Editing范式缺乏像素级空间控制与Inpainting范式掩码误差的冲突。切入点在于将掩码从“区域擦除工具”重构为“空间控制接口”，并通过VIP-Seg解决实例级分割精度瓶颈。方法上，通过合成三元组数据训练编辑模型，并添加LoRA适配器注入掩码条件。实验证明CtrlVTON-base在VITON-HD上M-DINO达0.8054，CtrlVTON在掩码可控任务上IoU达0.961，均优于对比基线。边界在于：合成 $p_{ref}$ 的质量可能限制复杂背景下的身份保持，且未验证视频时序一致性。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.09362)