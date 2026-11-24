# CVPR2026最新论文 ｜MatPedia: A Universal Generative Foundation for High-Fidelity Material Synthesis ｜MatPedia：基于联合RGB-PBR潜空间的统一材质生成基础模型

研究机构：南开大学、南京大学

作者：Di Luo、Shuhui Yang、Mingxin Yang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.16957)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.16957)

> 导读
> 现有PBR材质生成方法受限于任务碎片化与训练数据规模，难以兼顾高分辨率合成与大规模RGB视觉先验的利用。MatPedia通过构建联合RGB-PBR潜空间表示，将RGB外观与四张PBR图编码为两个相互依赖的潜变量，并复用视频扩散架构学习其联合分布。该框架在单一模型内统一了文本到材质、图像到材质及内在分解三项任务，实现了原生1024×1024分辨率的生成。尽管其在语义对齐与感知相似度指标上优于现有扩散基线，但缺乏对生成材质物理一致性的直接验证，其作为“基础模型”的泛化边界仍存疑。

## 研究背景

当计算机图形学追求物理准确的重光照资产时，双向反射分布函数（BRDF）的参数化表示成为核心。空间变化双向反射分布函数（SVBRDF）通常被分解为反照率（Basecolor）、法线（Normal）、粗糙度（Roughness）与金属度（Metallic）四张纹理图，遵循Cook-Torrance微表面模型。然而，从单张RGB图像恢复这些物理属性是一个病态反演问题，因为光照与材质在像素观测中非线性耦合，导致多种材质-光照组合可产生相同图像。传统逆渲染方法依赖多视图几何约束或物理优化，计算成本高且难以处理复杂反射；而基于扩散模型的材质生成方法虽能利用数据先验，但往往将RGB与PBR视为独立模态，导致无法有效利用大规模无标注RGB数据，且任务被割裂为独立的生成或分解流水线。

当前PBR材质生成领域的主流路线包括基于GAN的无条件生成与基于扩散模型的条件生成。MatFuse等扩散方法虽支持多模态输入，但受限于小规模PBR数据集，生成多样性不足；MaterialPicker采用视频骨干但独立压缩帧，限制了分辨率至256×256；RGB↔X通过模态切换实现分解，但推理时间较长。这些方法的共同瓶颈在于缺乏一个统一的潜空间表示，能够同时捕捉RGB外观与PBR物理属性之间的内在耦合关系，从而阻碍了大规模RGB视觉先验向材质物理属性的有效迁移。MatPedia的切入点在于利用RGB图像已包含丰富视觉线索、而PBR图仅编码互补物理信息这一不对称性，将二者视为物理耦合的“帧序列”，通过视频压缩范式实现紧凑联合编码，从而在单一架构中统一多种材质任务并复用大规模RGB数据。

## 核心方法

### 方法参照系

本文问题可置于“基于扩散模型的材质生成”通用流程中，其标准步骤为：编码输入条件→在潜空间去噪→解码输出材质图。关键差异在于，传统方法将RGB与PBR作为独立通道处理，而MatPedia将二者建模为具有时序依赖关系的5帧序列，利用视频变分自编码器（VAE）的因果卷积结构捕捉跨模态相关性，从而支持混合数据训练与统一任务接口。

### 联合RGB-PBR潜空间表示

设计动机在于解决独立编码导致的冗余与先验割裂问题：RGB已包含纹理与结构信息，PBR仅需编码增量物理属性，独立编码浪费容量且无法共享视觉先验。MatPedia将RGB图像 $\mathbf{I}_{rgb}$ 与四张PBR图 $\{\mathbf{a}, \mathbf{n}, \mathbf{r}, \mathbf{m}\}$ 沿时间维拼接为5帧序列，输入预训练视频VAE编码器。编码器产生两个潜变量：RGB潜变量 $\mathbf{z}_{rgb}$ 独立编码，PBR潜变量 $\mathbf{z}_{pbr}$ 利用RGB编码分支缓存的特征 $F_{enc}$ 进行条件编码：

$$
\mathbf{z}_{pbr} = E_{pbr}(\mathbf{a}, \mathbf{n}, \mathbf{r}, \mathbf{m} | F_{enc})
$$

该公式表明PBR潜变量仅表示相对于RGB外观的互补物理信息，实现紧凑压缩。解码器采用对称结构，PBR潜变量解码时同样利用RGB解码器缓存特征 $F_{dec}$，确保空间对齐。此设计使PBR分支可继承RGB分支从大规模数据学到的视觉先验，同时保持PBR潜变量分布由配对数据主导，避免RGB-only数据污染物理属性分布。

### 基于视频DiT的统一生成架构

设计动机在于解决任务碎片化与高分辨率生成瓶颈：独立任务模型无法共享参数，且2D扩散架构难以原生支持1024×1024分辨率。MatPedia采用视频扩散Transformer（DiT）作为骨干，初始化自预训练视频生成模型，并通过低秩适应（LoRA）微调适应材质任务。所有任务共享同一DiT架构，通过不同条件信号区分：文本到材质以文本嵌入为条件，图像到材质以输入图像VAE编码为条件，内在分解以RGB潜变量为条件仅生成PBR潜变量。训练采用整流流目标：

$$
\mathcal{L} = \mathbb{E}_{t, \mathbf{x}_0, \mathbf{x}_1} \left[ \| v_\theta(\mathbf{x}_t, t, \mathbf{c}) - (\mathbf{x}_1 - \mathbf{x}_0) \|^2 \right]
$$

其中 $\mathbf{x}_t = (1-t)\mathbf{x}_0 + t\mathbf{x}_1$，$\mathbf{c}$ 为条件信号。对于RGB-only样本，损失仅施加于RGB潜变量，使模型从大规模RGB数据学习视觉先验而不影响PBR潜变量分布。此架构通过LoRA实现任务特定适配，同时保留预训练视频模型的时空一致性先验，支持原生1024×1024生成，推理时经RealESRGAN上采样至4K。

## 实验评估

实验在MaterialPicker测试集上进行，基线包括MatFuse（扩散材质生成）、Material Palette（PBR分解）与RGB↔X（模态切换分解）。基线覆盖扩散生成与分解两条路线，但缺乏逆渲染类方法（如NeRFactor）对比，且未包含ControlMat等强基线的定量结果（仅定性对比）。

| 任务 | 指标 | MatFuse | Material Palette | RGB↔X | MatPedia |
|---|---|---|---|---|---|
| 文本到材质 | CLIP↑ | 0.261 | - | - | **0.283** |
| 文本到材质 | DINO-FID↓ | 1.90 | - | - | **1.31** |
| 图像到材质 | CLIP (Basecolor)↑ | 0.833 | 0.813 | 0.780 | **0.943** |
| 图像到材质 | DINO (Basecolor)↑ | 0.649 | 0.543 | 0.448 | **0.907** |
| 材质分解 | MSE (Basecolor)↓ | - | 0.058 | 0.122 | **0.009** |
| 材质分解 | LPIPS (Basecolor)↓ | - | 0.716 | 0.770 | **0.664** |

MatPedia在文本到材质任务中CLIP分数0.283高于MatFuse的0.261，DINO-FID 1.31低于1.90，表明语义对齐与分布相似度更优。图像到材质任务中，Basecolor通道CLIP 0.943显著高于MatFuse的0.833，DINO 0.907高于0.649，显示在几何畸变输入下恢复内在颜色的能力更强。材质分解任务中，Basecolor MSE 0.009远低于Material Palette的0.058与RGB↔X的0.122，LPIPS 0.664低于0.716与0.770，验证了联合潜空间在像素级重建精度上的优势。

消融实验显示，移除RGB Appearance Dataset（仅用PBR配对数据训练）导致CLIP从0.283降至0.275，DINO-FID从1.31升至1.62，证实混合训练策略对语义对齐与感知真实性的增益。3D VAE解码器微调后，Normal通道PSNR提升3.55 dB，Roughness提升5.20 dB，表明解码器适配对关键物理属性重建至关重要。

评估边界方面，指标仅涵盖语义对齐（CLIP）、感知相似度（DINO/LPIPS）与像素误差（MSE），缺乏物理一致性指标（如重光照PSNR或BRDF参数误差）。测试集限于MaterialPicker，未覆盖高反射、透明或动态场景。代码未公开，超参数（LoRA rank 128，学习率1e-4）已报告，但GPU资源与训练时长未说明，可复现性受限。

## 关联研究分析

从问题动机看，MatPedia与MatFuse同属扩散材质生成路线，但MatFuse将RGB与PBR作为独立条件处理，导致无法利用大规模RGB-only数据；MatPedia通过联合潜空间将PBR编码为RGB的条件变量，使RGB分支可从无标注数据学习视觉先验，而PBR分支保持物理分布纯净。这一差异源于任务特性：MatFuse侧重多模态编辑，需独立控制各通道；MatPedia侧重统一生成，需共享视觉先验。MatPedia未验证联合编码是否导致RGB分支对PBR分支的过度依赖，即在RGB-only训练阶段，PBR潜变量分布是否真正保持独立。

从方法设计看，MatPedia与MaterialPicker同用视频骨干，但MaterialPicker独立压缩各帧，限制分辨率至256×256；MatPedia利用视频VAE的因果卷积捕捉RGB与PBR的时序依赖，实现1024×1024原生生成。这一差异源于架构选择：MaterialPicker将材质视为独立图像序列，MatPedia视为物理耦合的帧序列。与逆渲染方法（如NeRFactor）相比，MatPedia不显式解耦光照，隐含假设光照已烘焙或需后续处理，其生成材质在重光照场景下的物理一致性未经验证。MatPedia的边界在于其作为“基础模型”的泛化能力仅在同分布测试集上验证，跨域（如高反射、SSS材质）性能未知。

## 总结

MatPedia旨在解决PBR材质生成中任务碎片化与数据规模受限的矛盾，通过联合RGB-PBR潜空间表示，将PBR编码为RGB的条件变量，复用视频扩散架构统一文本到材质、图像到材质及内在分解任务。该框架在MaterialPicker测试集上实现CLIP 0.283与Basecolor MSE 0.009，优于MatFuse与Material Palette。其边界在于缺乏物理一致性验证，且泛化能力仅在同分布数据上评估。当输入图像包含强几何畸变或复杂光照时，联合潜空间能否准确分离物理属性与视觉外观，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.16957)