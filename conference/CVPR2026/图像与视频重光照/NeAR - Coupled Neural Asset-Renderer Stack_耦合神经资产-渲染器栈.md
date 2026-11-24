# CVPR2026最新论文 ｜NeAR: Coupled Neural Asset-Renderer Stack ｜耦合神经资产-渲染器栈

研究机构：新加坡南洋理工大学

作者：Hong Li、Chongjie Ye、Houyuan Chen 等 15 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.18600)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.18600)

> 单图3D重光照面临资产生成与渲染解耦导致的误差累积困境，现有方法或依赖病态的PBR分解，或受限于2D扩散缺乏多视角一致性。NeAR通过共设计资产表示与渲染器，利用光照归一化潜空间（LH-SLAT）作为中间契约，实现了前馈式实时重光照。该方法在多个基准上超越了传统3D生成与神经渲染基线，但其对复杂非朗伯效应的处理能力及对几何先验的依赖仍存疑。

## 研究背景

单图3D重光照的核心难点在于从单一观测中解耦几何、材质与光照。传统计算机图形学将资产制作与渲染分离，前者定义场景属性，后者模拟光传输。这种分离导致逆向重建时，资产分解中的微小误差（如反照率误判）经非线性渲染过程放大，产生烘焙阴影或光照不一致。结构化3D潜变量（SLAT）通过稀疏体素网格高效编码3D资产，但标准SLAT盲目编码输入外观，包含阴影与高光，无法直接支持重光照。

主流3D生成方法如Trellis和HY3D-2.1依赖显式PBR分解，但单图输入下该问题病态，导致材质歧义（如将面包误判为高金属度）。2D扩散模型如DiLightNet虽能生成逼真光照，但缺乏3D感知，无法保证多视角一致性。NeAR的切入点在于打破资产与渲染的孤立开发模式，提出耦合栈：通过光照归一化SLAT（LH-SLAT）将任意光照输入映射至规范潜空间，再由光照感知神经渲染器合成可重光照3D高斯场，从而在保持几何一致性的同时实现实时重光照。

## 核心方法

### 方法参照系

标准3D重光照流程为“生成PBR资产+物理渲染”，本文问题与该流程的关键差异在于：资产生成与渲染器独立优化，导致分解误差累积。NeAR将两者共设计，以LH-SLAT为共享潜空间，替代静态纹理预测。

### 光照归一化SLAT生成

标准SLAT编码包含阴影的高光外观，导致重光照时材质-光照纠缠。NeAR引入LH-SLAT，通过整流流模型将任意光照输入映射至均匀白色环境光下的规范潜空间。设计动机是消除瞬态光照效应，保留几何-材质交互的稳定基底。训练采用条件流匹配损失：

$$ \mathcal{L}_{\text{stage1}} = \mathbb{E}_{t, \mathbf{z}_0, \boldsymbol{\epsilon}} \left[ \| \mathbf{v}_\theta((1-t)\mathbf{z}_0 + t\boldsymbol{\epsilon}, t) - (\boldsymbol{\epsilon} - \mathbf{z}_0) \|^2 \right] $$

该公式学习从噪声到归一化潜变量的向量场，确保LH-SLAT抑制烘焙阴影，为后续渲染提供鲁棒“契约”。

### 光照感知神经渲染器

LH-SLAT缺乏视角与光照信息，无法直接生成视图依赖外观。NeAR设计两级解码器：内在感知解码器（IAD）提取视图无关内在特征 $\mathbf{h}$，光照感知解码器（LAD）注入视角嵌入与光照条件。LAD摒弃球谐函数（SH）烘焙光照，改用光照分词器编码HDR环境图。光照条件Token $\mathbf{C}_L$ 通过空间交叉注意力融合方向编码与视觉特征：

$$ \mathbf{C}_L = \text{SelfAttn}\left( \text{Concat}(\text{PosEnc}(\mathbf{E}_{\text{dir}}), \text{ConvNeXt}(\mathbf{E}_{\text{ldr}}, \mathbf{E}_{\text{log}})) \right) $$

该设计显式嵌入方向信息，使渲染器能动态响应视角变化，解决SH烘焙导致的静态光照问题，实现任意HDR环境下的实时重光照。

## 实验评估

实验在ADT、DTC、Objaverse及Glossy Synthetic数据集上评估，基线涵盖DiffusionRenderer、DiLightNet、HY3D-2.1等神经渲染与3D生成方法，但缺乏纯2D扩散SOTA（如IC-Light）在3D任务上的直接对比。

| 任务 | 数据集 | 方法 | PSNR (dB) | LPIPS | SSIM |
|---|---|---|---|---|---|
| 新视角重光照 | ADT | Ours | 22.87 | 0.0693 | 0.9023 |
| 新视角重光照 | ADT | HY3D-2.1 | 22.30 | 0.0727 | 0.9017 |
| 未知光照重光照 | DTC | Ours | 23.47 | 0.0642 | 0.9177 |
| 未知光照重光照 | DTC | DiffusionRenderer | 22.99 | 0.0691 | 0.9078 |

NeAR在ADT新视角重光照中PSNR达22.87 dB，较HY3D-2.1提升0.57 dB；在DTC未知光照重光照中PSNR 23.47 dB，较DiffusionRenderer提升0.48 dB，表明耦合栈在3D一致性上优于解耦范式。

消融实验显示，LH-SLAT输入较Shaded SLAT提升PSNR 3.07 dB（32.02 vs 28.95），验证光照归一化的关键作用。解码器深度从12+1增至12+6时，PSNR从31.56升至32.54，但FPS从48降至30，存在效率-质量权衡。

评估指标限于PSNR/SSIM/LPIPS，缺乏物理一致性定量指标（如阴影方向误差）。代码未公开，超参数细节仅部分披露，可复现性受限。

## 关联研究分析

从问题动机看，NeAR与GR3EN同属3D场景重光照，但GR3EN依赖视频扩散模型蒸馏至3D表示，侧重时序一致性；NeAR聚焦单图前馈，通过LH-SLAT规避视频时序建模。差异根源在于任务特性：GR3EN处理动态场景需时间注意力，NeAR处理静态资产需几何-材质解耦。NeAR未探索动态场景，其LH-SLAT在视频帧间是否保持光照语义一致，论文未给出回答。

从方法设计看，NeAR与Trellis共享SLAT架构，但Trellis预测静态纹理，NeAR改造为动态光照感知解码。Trellis的资产生成假设固定渲染器，NeAR的耦合设计允许渲染器反馈影响资产表示。NeAR未对比Trellis+物理渲染的解耦基线，仅与HY3D-2.1等3D生成方法对比，可能低估解耦范式的优化潜力。

## 总结

NeAR解决单图3D重光照中资产-渲染解耦导致的误差累积矛盾，通过LH-SLAT共设计资产与渲染器，实现前馈实时重光照。在ADT新视角重光照中PSNR 22.87 dB，较HY3D-2.1提升0.57 dB，验证耦合栈优势。其边界在于依赖几何先验（如HY3D网格）且对透明等复杂效应处理有限，LH-SLAT在缺乏精确几何输入时是否仍能保持材质一致性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.18600)