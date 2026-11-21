# HuggingFace最新推荐论文 ｜BRDFusion: Physics Meets Generation for Urban Scene Inverse Rendering ｜物理与生成融合的城市场景逆渲染

研究机构：国立阳明交通大学、美国伊利诺伊大学厄巴纳-香槟分校

作者：Yi-Ruei Liu、Jie-Ying Lee、Zheng-Hui Huang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.17049)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.17049)

> 城市驾驶视频逆渲染旨在从稀疏观测中解耦几何、材质与光照，以支持可重光照的仿真与编辑。现有物理方法受限于病态反演导致的伪影，而纯生成方法缺乏对局部光照的精确控制，两者难以兼得。BRDFusion 通过 SDEdit 机制将生成模型嵌入物理渲染循环，在保持物理可控性的同时消除蒙特卡洛噪声。该框架在合成城市场景的重光照任务上显著优于基线，但其对发射体材质的缺失限制了夜间主动光源的逆渲染能力。

## 研究背景

逆渲染的核心困境在于图像形成过程中几何、材质与光照的非线性耦合，导致多种场景配置可产生相同像素观测，即病态反演。为约束这一歧义，物理基于渲染（Physically-Based Rendering, PBR）通过渲染方程提供可微分的光传输模型，但其依赖蒙特卡洛积分，在几何重建不完美时会产生显著噪声。与此同时，预训练视频扩散模型能生成高保真图像，却缺乏显式的三维结构，无法响应光照参数的变化。

城市动态场景的逆渲染面临更严峻的挑战：无界空间、高动态范围（HDR）阳光以及稀疏视角加剧了解耦难度。早期方法如 UrbanIR 和 InvRGB+L 采用神经辐射场或三维高斯泼溅（3D Gaussian Splatting, 3DGS）进行优化，虽具备物理可控性，但常因优化歧义产生渲染伪影，尤其在局部光照（如车灯）模拟中表现不佳。另一方面，DiffusionRenderer 等生成式方法虽视觉真实，但无法保证长序列的时间一致性，且无法精确控制光照方向与强度。BRDFusion 的切入点在于将生成模型从独立的生成器转变为物理渲染循环中的去噪器与正则化项，通过 SDEdit 机制锚定物理渲染结果，从而在动态城市场景中同时实现物理准确性与视觉真实性。

## 核心方法

### 混合前向渲染管线

BRDFusion 的场景表示基于 3DGS，每个高斯 $\mathbf{g} = (o, \boldsymbol{\mu}, \mathbf{q}, \mathbf{s}, \mathbf{n}, \mathbf{c}, \mathbf{a}, r, m)$ 编码不透明度、位置、旋转、尺度、法线、颜色、反照率、粗糙度与金属度。光照由 $512 \times 1024 \times 3$ 的 HDR 环境图 $\mathbf{E}$ 表示。前向渲染包含三个通道：体积渲染、PBR 渲染与生成渲染。体积渲染通过 Alpha 混合快速生成 G-buffer（法线、深度、反照率等），但不模拟全局光传输。PBR 通道评估渲染方程，利用 Cook-Torrance BRDF 与重要性采样计算 HDR 辐射度，随后通过 Tone-mapping 转换为 LDR。生成通道引入预训练视频扩散模型作为去噪器，解决 PBR 通道的蒙特卡洛噪声问题。

### SDEdit 锚定的生成细化

传统生成模型从纯噪声开始去噪，易产生与物理光照不一致的幻觉。BRDFusion 借鉴 SDEdit 思想，将 PBR 渲染结果作为去噪轨迹的起点，而非最终输出。设 PBR 视频为 $\mathbf{C}_{pbr}^{1:F}$，生成过程定义为：

$$ \mathbf{C}_{gen}^{1:F} = \mathcal{D}(\mathbf{F}_{\theta}^{fwd}(\mathcal{E}(\mathbf{C}_{pbr}^{1:F}) + \epsilon, \tau, \mathbf{G})) $$

其中 $\mathcal{E}$ 与 $\mathcal{D}$ 为 VAE 编解码器，$\mathbf{F}_{\theta}^{fwd}$ 为潜在空间去噪器，$\tau$ 为噪声水平，$\mathbf{G}$ 为条件输入（包含 G-buffer 序列与环境图）。该设计确保生成结果既保留 PBR 的光照结构，又具备扩散模型的视觉细节，实现了物理可控性与视觉真实性的统一。

### 多阶段交替优化

逆渲染采用四阶段交替优化策略，以解决联合优化的病态性。第一阶段体积渲染优化几何与材质，损失函数包含光度损失 $\mathcal{L}_{rgb}$、不透明度损失 $\mathcal{L}_O$ 以及基于生成先验的正则化项：

$$ \mathcal{L}_{vol} = \mathcal{L}_{rgb} + \mathcal{L}_O + \lambda_D \mathcal{L}_D + \lambda_N \mathcal{L}_N + \lambda_A \mathcal{L}_A + \lambda_R \mathcal{L}_R + \lambda_M \mathcal{L}_M $$

其中 $\mathcal{L}_D, \mathcal{L}_N, \mathcal{L}_A, \mathcal{L}_R, \mathcal{L}_M$ 分别为深度、法线、反照率、粗糙度、金属度与生成先验 $\mathbf{X}_g$ 的 L1 距离。第二阶段生成细化利用 SDEdit 锐化 G-buffer，消除时间不一致性。第三阶段冻结几何与材质，通过 PBR 渲染匹配输入图像以恢复光照，损失函数为：

$$ \mathcal{L}_{pbr} = \|\mathbf{C}_{pbr} - \mathbf{C}_{gt}\|_1 + \lambda_E \|\log \mathbf{E} - \log \mathbf{E}_g\|_1 $$

第四阶段联合优化所有参数。这种顺序设计确保光照解耦仅在几何与材质可靠后进行，避免了早期光照估计对材质解耦的干扰。

## 实验评估

实验在 Waymo Open Dataset（真实）与 6 个合成城市场景上进行，基线包括 UrbanIR、InvRGB+L 及 Gen3C+DR。合成数据上，BRDFusion 在反照率估计（si-PSNR 26.21）、粗糙度（RMSE 0.187）、金属度（RMSE 0.174）及法线（MAE 16.88）上均优于所有基线。新视角重光照 PSNR 达 21.93，显著高于 UrbanIR（15.61）与 InvRGB+L（14.55），验证了混合框架在光照控制上的优势。

| 方法 | Albedo (si-PSNR↑) | Roughness (RMSE↓) | Metallic (RMSE↓) | Normal (MAE↓) | Relighting PSNR↑ |
|---|---|---|---|---|---|
| UrbanIR | 16.55 | 0.329 | - | 17.67 | 15.61 |
| InvRGB+L | 18.17 | 0.206 | 0.321 | 21.93 | 14.55 |
| Gen3C+DR | - | - | - | 110.8 | 14.83 |
| Ours | 26.21 | 0.187 | 0.174 | 16.88 | 21.93 |

消融实验显示，移除 PBR 优化导致新视角合成 PSNR 从 20.54 降至 13.58，表明物理模型对几何一致性的关键作用；移除生成优化则导致法线 MAE 激增至 110.8，证实生成先验对病态反演正则化的必要性。移除生成渲染阶段虽不影响逆渲染指标，但显著降低新视角合成质量，说明生成去噪对最终视觉保真度的贡献。

评估协议存在局限：合成数据仅 6 个场景，真实数据缺乏材质真值，导致定量评估受限。代码未开源，超参数（如 30,000 次迭代）依赖单卡 RTX A6000，训练耗时 10-11 小时，限制了大规模复现。此外，评估未涵盖计算效率对比，且未与最新前馈方法（如 MVInverse）进行直接比较，可能低估了前馈路线在特定场景下的竞争力。

## 关联研究分析

从问题动机看，BRDFusion 与 DiffusionRenderer 均利用扩散先验解决逆渲染歧义，但前者将生成模型嵌入物理优化循环，后者作为独立的 2D 视频生成器。这一差异源于任务特性：城市场景需要精确的局部光照控制（如车灯方向），纯生成模型无法提供显式光照参数，而 BRDFusion 通过 PBR 通道保留了这一可控性。然而，BRDFusion 依赖 SDEdit 的噪声水平 $\tau$ 平衡物理与生成，该参数在极端光照条件下（如夜间）是否鲁棒，论文未给出系统性分析。

从方法设计看，BRDFusion 与 InvRGB+L 共享 3DGS 动态场景图结构，但后者依赖 LiDAR 反射模型进行材质估计，前者引入生成先验正则化。InvRGB+L 在材质估计上存在模糊与伪影，BRDFusion 通过生成细化阶段锐化 G-buffer，提升了材质细节。但 BRDFusion 未显式建模发射体材质，导致无法逆渲染主动光源（如车灯），而 InvRGB+L 虽支持局部光照，但缺乏生成先验的视觉保真度。这种取舍反映了当前领域在“物理完整性”与“视觉真实性”之间的权衡，尚未有方法能同时解决发射体逆渲染与生成式去噪。

## 总结

BRDFusion 旨在解决城市动态场景逆渲染中物理准确性与视觉真实性的矛盾，通过 SDEdit 机制将生成模型嵌入 PBR 优化循环，实现了可控的重光照与高保真渲染。在合成城市场景上，其重光照 PSNR 达 21.93，显著优于物理基线，验证了混合框架的有效性。然而，该方法未显式建模发射体材质，导致无法逆渲染夜间主动光源（如车灯），仅支持插入虚拟光源。当输入视频包含强发射体时，PBR 通道是否仍能准确解耦被动材质与主动光照，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.17049)