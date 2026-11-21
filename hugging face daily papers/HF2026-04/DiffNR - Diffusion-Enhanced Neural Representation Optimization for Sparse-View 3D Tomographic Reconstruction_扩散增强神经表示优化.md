# HuggingFace最新推荐论文 ｜DiffNR: Diffusion-Enhanced Neural Representation Optimization for Sparse-View 3D Tomographic Reconstruction ｜扩散增强神经表示优化

研究机构：澳大利亚莫纳什大学、澳大利亚国立大学

作者：Shiyan Su、Ruyi Zha、Danli Shi 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.21518)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.21518)

> 稀疏视图3D CT重建面临的核心矛盾是：神经表示（NR）能维持体积全局一致性，但在欠约束区域产生严重伪影；而传统扩散模型（NP）虽能修复细节，却导致切片间抖动且计算耗时。本文切入点在于将单步条件扩散模型作为“修复器”嵌入NR优化流程，而非作为独立生成器。通过周期性生成伪参考体积提供3D感知监督，DiffNR在保持体积一致性的同时抑制了伪影。该方法在ToothFairy数据集上平均提升PSNR 3.99 dB，但其在极端稀疏视图下的泛化能力及对预训练基础模型的依赖仍是存疑点。

## 研究背景

当投影视图数量减少至数十张时，CT重建成为高度病态的逆问题。此时，基于神经场或3D高斯泼溅的神经表示（Neural Representation, NR）通过可微渲染优化体积密度，虽能捕捉全局结构，但在缺乏投影约束的区域极易产生条纹伪影。为弥补这一缺陷，研究者引入扩散模型作为先验，但主流神经先验（Neural Prior, NP）方法将局部求解器嵌入多步去噪过程，导致推理时间长达数小时，且2D切片独立处理引发层间抖动，无法满足临床实时性与3D一致性需求。

现有方案在效率与一致性之间陷入两难：NP方法虽能利用数据分布先验抑制伪影，但其迭代去噪机制计算开销巨大，且缺乏3D体积约束；NR方法虽具备全局结构优势，但自监督优化无法填补信息缺失。本文的切入点在于解耦“生成”与“优化”：不将扩散模型作为逐步去噪的主干，而是将其微调为单步修复模型，仅在NR优化的特定阶段介入，通过生成伪参考体积提供辅助监督，从而在保留NR全局一致性的同时，以极低的计算代价修复局部伪影。

## 核心方法

### 方法参照系

本文问题属于稀疏视图3D CT重建中的神经表示优化范畴。标准NR流程通过最小化投影一致性损失（L1/SSIM）与低层正则化（如全变分TV）来优化神经场或高斯参数。本文的关键差异在于，在标准优化流程中引入了一个基于条件扩散模型的“修复-增强”模块，该模块不直接参与每一步梯度更新，而是周期性生成伪参考体积以提供高阶感知监督。

### SliceFixer：单步条件扩散修复器

SliceFixer基于SD-Turbo微调，旨在从NR查询的退化切片 $\tilde{\mathbf{S}}$ 中恢复无伪影切片 $\hat{\mathbf{S}}$。其设计动机在于解决传统NP方法中多步SDE采样导致的计算瓶颈及2D独立处理引发的层间不一致。SliceFixer采用单步推理机制，输入为退化切片、双平面X光投影及文本提示，通过LoRA适配器微调U-Net与VAE，保持基础模型参数冻结。其去噪目标函数定义为：

$$ \mathcal{L}_{\text{diff}} = \mathbb{E}_{\mathbf{x} \sim p_{\text{data}}, t \sim p_t, \boldsymbol{\epsilon} \sim \mathcal{N}(0, 1)} \left[ \|\boldsymbol{\epsilon} - \boldsymbol{\epsilon}_\theta(\mathbf{x}_t; \mathbf{c}, t)\|_2^2 \right] + \lambda_{\text{CLIP}} \mathcal{L}_{\text{CLIP}} + \lambda_{\text{GAN}} \mathcal{L}_{\text{GAN}} + \lambda_{\text{SSIM}} \mathcal{L}_{\text{SSIM}} $$

该公式表明，模型在预测噪声的同时，通过CLIP对齐、对抗损失及SSIM损失约束生成结果的语义一致性与结构保真度，确保修复后的切片既符合解剖结构又具备视觉合理性。

### 修复-增强优化策略

在NR优化过程中，DiffNR每 $\ell$ 次迭代查询当前体积 $\tilde{\mathbf{V}}_\ell$，将其切片上采样后送入SliceFixer生成伪参考体积 $\hat{\mathbf{V}}_\ell$。随后，在每 $\tau$ 次迭代中，计算查询体积与伪参考体积之间的3D SSIM损失作为辅助监督。这一策略的设计动机在于避免体素级L1损失对扩散模型可能引入的幻觉细节过拟合。3D SSIM损失定义为轴向、矢状及冠状平面2D SSIM的均值：

$$ \mathcal{L}_{\text{3D-SSIM}} = \frac{1}{3} \left( \text{SSIM}_{\text{axial}} + \text{SSIM}_{\text{sagittal}} + \text{SSIM}_{\text{coronal}} \right) $$

该损失函数促进结构连贯性而非像素级匹配，有效抑制了扩散模型在欠约束区域产生的高频幻觉，同时通过降低SliceFixer查询频率（每 $\tau$ 步一次）保证了整体优化效率。

## 实验评估

实验在ToothFairy（牙科）与LUNA16（胸部）数据集上进行，对比基线包括SART、ASD-POCS、NAF、R²-Gaussian及DiffusionMBIR。基线覆盖传统迭代、自监督NR及扩散迭代方法，但未包含最新的流匹配或泊松条件生成模型（如PoCGM、Efficient Flow Matching），这可能影响对当前SOTA的全面评估。

| 方法 | 36-view PSNR/SSIM | 24-view PSNR/SSIM | 12-view PSNR/SSIM |
| :--- | :--- | :--- | :--- |
| SART | 22.42 / 0.519 | 21.05 / 0.437 | 28.56 / 0.711 |
| ASD-POCS | 23.51 / 0.679 | 21.74 / 0.589 | 28.47 / 0.762 |
| DiffusionMBIR | 29.30 / 0.800 | 26.87 / 0.722 | 30.36 / 0.792 |
| R²-Gaussian | 24.67 / 0.645 | 21.55 / 0.494 | 26.92 / 0.677 |
| R²-Gaussian +DiffNR | 29.68 / 0.872 | 27.71 / 0.798 | 34.19 / 0.908 |

R²-Gaussian+DiffNR在12-view设置下PSNR达34.19 dB，显著高于DiffusionMBIR的30.36 dB，且SSIM提升至0.908，表明其在极端稀疏下具备更强的结构恢复能力。消融实验显示，将SliceFixer作为后处理模块仅提升PSNR至26.70 dB，而集成到优化流程中则提升至28.82 dB，证实了“修复-增强”策略优于“后处理”范式。此外，引入双平面X光条件使PSNR提升0.6 dB，验证了结构条件输入的有效性。

评估边界方面，论文未报告置信区间，且ToothFairy与LUNA16数据量较小（各25张测试图），统计显著性存疑。代码尚未公开，但提供了详细的超参数设置（如 $\tau=10$, $\lambda_{\text{diff}}=0.5$），具备可复现性基础。

## 关联研究分析

从方法设计看，DiffNR与Difix3D+同属“修复-增强”范式，但Difix3D+针对RGB视图合成，修复对象为渲染投影，而DiffNR针对CT体积，修复对象为查询切片。这一差异源于CT投影的穿透性导致误差在体积中累积，直接修复投影无法解决内部结构伪影，因此必须转向切片级修复。然而，DiffNR依赖SD-Turbo这一通用图像基础模型，其预训练数据主要为自然图像，缺乏医学解剖先验，这可能限制其在复杂病理结构下的修复精度。

从问题动机看，DiffNR与DiffusionMBIR代表了两种截然不同的物理约束嵌入方式。DiffusionMBIR将求解器嵌入去噪步骤，实现逐步数据一致性校正，但计算耗时11小时；DiffNR则将数据一致性约束保留在NR优化主循环中，扩散模型仅作为周期性感知监督源。这种解耦设计牺牲了逐步去噪的精细控制，但换取了数量级的效率提升。值得注意的是，DiffNR在12-view下PSNR（34.19 dB）高于DiffusionMBIR（30.36 dB），表明在极端稀疏下，全局体积一致性约束比逐步去噪更关键，但这一结论是否适用于其他解剖区域或扫描协议，论文未给出回答。

## 总结

DiffNR旨在解决稀疏视图3D CT重建中神经表示伪影与扩散模型效率/一致性冲突的矛盾。其切入点在于将单步条件扩散模型从“生成器”重构为“修复器”，通过周期性生成伪参考体积提供3D感知监督，而非逐步去噪。该方法在ToothFairy数据集上平均提升PSNR 3.99 dB，并在12-view设置下显著优于DiffusionMBIR。然而，其性能高度依赖SD-Turbo的预训练先验，且实验仅在牙科与胸部数据上验证，未涵盖腹部等复杂解剖区域。当投影视图进一步减少至12以下，或面对金属伪影等非线性物理效应时，单步修复策略能否维持结构完整性，仍是亟待验证的问题。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.21518)