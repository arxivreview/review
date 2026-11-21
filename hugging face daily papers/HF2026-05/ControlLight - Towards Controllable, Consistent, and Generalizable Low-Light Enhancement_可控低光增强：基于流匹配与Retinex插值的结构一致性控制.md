# HuggingFace最新推荐论文 ｜ControlLight: Towards Controllable, Consistent, and Generalizable Low-Light Enhancement ｜可控低光增强：基于流匹配与Retinex插值的结构一致性控制

研究机构：中国科学院、浙江大学

作者：Yufeng Yang、Jianzhuang Liu、Jisheng Chu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.25569)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.25569)

> 低光图像增强旨在从曝光不足且伴随噪声的视觉数据中恢复自然光照外观，但现有方法通常仅学习单一固定强度的映射，缺乏对增强程度的细粒度控制。这种“黑盒”式增强在需要用户根据场景偏好调整亮度的实际应用中显得僵化，且基于扩散模型的生成式方法虽能恢复细节，却常引入结构幻觉。ControlLight 通过构建连续光照强度的伪配对数据集 Light100K，并引入失配感知加权流匹配损失，在 FLUX.2-klein 骨干上实现了平滑可控的低光增强。该方法在感知质量与可控性上优于现有基线，但其对像素级保真度的牺牲及依赖伪标签的构造方式，限制了其在严格参考指标下的竞争力。

## 研究背景

低光增强面临的核心困境是信号退化与物理模型失效的耦合。当传感器在弱光下采集图像时，光子匮乏导致信号低于噪声底限，图像不仅亮度不足，还伴随散粒噪声与运动模糊。Retinex 理论将图像分解为光照（Illumination）与反射率（Reflectance）分量，认为低光图像是正常光照与反射率乘积的退化结果。这一物理模型将增强任务从“像素映射”转化为“分量估计与重建”，使得去噪与去模糊可以独立处理。然而，传统 Retinex 方法在极端低光下光照估计对噪声极度敏感，且多数监督学习方法依赖严格配对的低光/正常光数据，而真实场景中此类数据难以获取且存在采集偏差。

主流路线分为回归式与生成式两类。回归式方法如 RetinexFormer 利用 Transformer 捕获全局依赖，在 LOLv1 上取得 20.88 dB 的 PSNR，但受限于固定监督，无法提供连续控制；生成式方法如 CLE Diffusion 尝试通过条件扩散实现可控增强，但受限于模型容量与简单数据构造，泛化能力不足且易产生伪影。大型图像编辑模型如 FLUX.2-klein 具备强大的生成先验，能恢复视觉合理的细节，但其指令式交互仅提供单一增强强度，且生成特性导致结构漂移。ControlLight 的切入点在于利用 Retinex 理论构造连续光照轨迹的伪配对数据，结合流匹配损失抑制边缘失配，从而在保留生成模型细节恢复能力的同时，实现基于 LoRA 强度的连续可控增强。

## 核心方法

### 方法参照系

本文问题属于低光图像增强中的可控生成任务。标准流程通常采用监督学习，从低光输入映射到固定正常光目标，或使用条件扩散模型以亮度参数为条件生成图像。本文的关键差异在于：不依赖真实配对数据，而是通过 Retinex 分解在潜空间构造连续光照强度的伪标签，并将增强强度 $s$ 直接作为 LoRA 缩放因子嵌入训练循环，而非仅在推理时应用。

### Retinex 引导的连续伪标签构造

设计动机在于解决真实配对数据稀缺及传统 Alpha 混合插值导致的局部对比度丢失问题。Alpha 混合在 RGB 空间直接平均，混淆了光照、反射率与色彩，无法反映真实低光退化的物理过程。ControlLight 采用 Retinex 模型 $I = R \odot L$，将连续增强建模为光照分量的过渡。首先将输入 $I_0$ 与增强目标 $I_1$ 转换为线性 RGB，计算亮度图 $Y$ 并通过双边滤波估计平滑光照图 $L_0, L_1$。反射率图估计为 $R_0 = I_0/L_0$ 和 $R_1 = I_1/L_1$。中间伪标签 $I_s$ 通过在对数域插值光照分量获得：

$$ L_s = \exp((1-s)\log(L_0) + s\log(L_1)) $$

反射率采用保守插值 $R_s = (1-\beta_s)R_0 + \beta_s R_1$，其中 $\beta_s = 0.5s$，以避免依赖含噪的 $R_0$ 或含伪影的 $R_1$。最终重建 $I_s = \text{clip}(R_s \odot L_s, 0, 1)$。该策略确保了伪标签在光照轴上的物理一致性，保留了局部阴影与对比度变化，为连续控制提供了更丰富的退化线索。

### 失配感知加权流匹配损失

设计动机在于解决扩散生成的伪目标中存在的细微边缘失配问题。尽管经过边缘一致性过滤，伪目标 $I_s$ 与输入 $I_0$ 之间仍存在高频结构偏差。标准流匹配损失对所有空间区域同等加权，导致模型继承并放大这些不可靠的边缘结构，产生结构漂移。ControlLight 引入失配感知加权流匹配损失 $\mathcal{L}_{wFM}$，通过距离变换识别目标边缘中与输入边缘距离超过阈值 $d$ 的不可靠像素，生成软权重图 $W_s$。损失函数定义为：

$$ \mathcal{L}_{wFM} = \mathbb{E}_{t, z_0, z_1} \left[ \sum_u W_s(u) \| v_\theta(z_t, I_0, s) - v^* \|^2 \right] $$

其中 $v^* = z_1 - z_0$ 为真实速度场，$W_s(u)$ 在不可靠边缘区域降低权重。该机制允许模型在不可靠区域仅接收弱外观监督，而非强制拟合失配结构，从而在保持生成细节的同时锚定输入图像的结构一致性。

## 实验评估

ControlLight 在 LOL-v1、LWSR、DICM、LIME 及 RealIR-Bench 五个基准上评估，对比 RetinexFormer、CIDNet、LLFormer、DarkIR、QuadPrior 及 CLE Diffusion 等基线。评估指标侧重无参考感知质量（NIQE, CLIP-IQA, MANIQA, MUSIQ），未报告 PSNR/SSIM。在 LOL-v1 上，ControlLight 的 CLIP-IQA 为 0.553，MANIQA 为 0.512，MUSIQ 为 70.20，均优于 RetinexFormer（0.429, 0.383, 63.16）；在 LWSR 上，ControlLight 的 CLIP-IQA 为 0.589，MUSIQ 为 68.39，同样领先。在真实世界数据集 DICM 上，ControlLight 的 NIQE 为 3.522，CLIP-IQA 为 0.698，显著优于所有基线，表明其在真实退化下的泛化能力。

| 方法 | LOL-v1 NIQE↓ | LOL-v1 CLIP-IQA↑ | LOL-v1 MUSIQ↑ | LWSR NIQE↓ | LWSR CLIP-IQA↑ | LWSR MUSIQ↑ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| RetinexFormer | 3.455 | 0.429 | 63.16 | 3.778 | 0.420 | 58.48 |
| CLE Diffusion | 4.893 | 0.581 | 68.84 | 4.265 | 0.491 | 62.63 |
| ControlLight | 4.567 | 0.553 | 70.20 | 4.232 | 0.589 | 68.39 |

消融实验验证了 $\mathcal{L}_{wFM}$ 的有效性。在 RealIR-Bench 上，使用标准流匹配损失 $\mathcal{L}_{FM}$ 的基线 LI-LPIPS 为 0.2237，NIQE 为 5.6242；引入 $\mathcal{L}_{wFM}$ 后，LI-LPIPS 降至 0.2148，NIQE 降至 4.5367，MUSIQ 升至 62.5262。这表明加权损失有效减少了结构不一致性，同时提升了感知质量。数据插值对比显示，Retinex 插值比 Alpha 混合提供更丰富的退化线索，其质量梯度更符合物理规律，有助于模型学习增强映射。

评估边界方面，论文未报告 PSNR/SSIM，无法与 DST-Net（25.64 dB）等回归式 SOTA 进行像素保真度对比。代码与超参数已开源，训练分辨率为 1024×1024，LoRA 参数量约 300M。由于依赖 FLUX.2-klein 骨干，推理效率受限于扩散模型的多步采样特性，尽管 LoRA 降低了训练成本，但实时部署仍面临挑战。

## 关联研究分析

从问题动机看，ControlLight 与 CLE Diffusion 均致力于可控低光增强，但数据构造策略存在根本差异。CLE Diffusion 采用亮度 Alpha 混合生成条件目标，这种线性插值在 RGB 空间混淆了光照与反射率，导致模型难以学习物理一致的光照过渡，且在真实场景泛化时产生伪影。ControlLight 将 Retinex 分解应用于数据构造阶段，通过对数域光照插值确保伪标签沿光照轴平滑变化，保留了局部对比度。这一差异源于对“可控性”定义的不同：CLE Diffusion 视控制为亮度参数的线性映射，而 ControlLight 视控制为物理光照强度的连续过渡。Retinex 插值是否在所有光照条件下均优于 Alpha 混合，论文未提供极端低光下的对比实验。

从方法设计看，ControlLight 与 ConceptSlider 均利用 LoRA 实现连续控制，但训练机制截然不同。ConceptSlider 通过文本引导的分数匹配优化 LoRA 方向，缩放因子 $s$ 仅在推理时应用，线性控制是假设而非强制。ControlLight 将 $s$ 嵌入训练循环，每个 $s$ 值对应特定的伪标签 $I_s$，并通过 $\mathcal{L}_{wFM}$ 校准 LoRA 方向。这种物理轨迹校准使得 ControlLight 在 RealIR-Bench 上的 $\delta_{smooth}$ 为 0.2195，显著优于 ConceptSlider 的 0.9237，表明其增强轨迹更平滑。然而，ConceptSlider 依赖文本嵌入的插值，而 ControlLight 依赖图像伪标签，后者对数据构造质量更敏感。当伪标签边缘失配严重时，$\mathcal{L}_{wFM}$ 的降权策略是否会导致高频纹理过度平滑，论文未深入探讨。

## 总结

ControlLight 旨在解决低光增强中固定强度映射缺乏可控性及生成模型结构漂移的矛盾。其切入点在于利用 Retinex 理论构造连续光照轨迹的伪配对数据，并将增强强度作为 LoRA 缩放因子嵌入训练，通过失配感知加权流匹配损失抑制边缘失配。该方法在 LOL-v1 上取得 70.20 的 MUSIQ，在 DICM 上取得 0.698 的 CLIP-IQA，证明了其在感知质量与可控性上的优势。然而，论文未报告 PSNR/SSIM，且依赖 FLUX.2-klein 骨干，推理效率受限。当伪标签边缘失配超过阈值 $d$ 时，$\mathcal{L}_{wFM}$ 的降权机制是否会导致局部细节丢失，论文未给出定量分析。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.25569)