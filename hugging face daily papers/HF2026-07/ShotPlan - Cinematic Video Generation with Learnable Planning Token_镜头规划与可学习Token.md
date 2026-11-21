# HuggingFace最新推荐论文 ｜ShotPlan: Cinematic Video Generation with Learnable Planning Token ｜镜头规划与可学习Token

研究机构：哈尔滨工业大学

作者：Su Guo、Guangce Liu、Haosen Yang 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.17675)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.17675)

> 多镜头视频生成旨在通过显式镜头规划实现跨镜头的叙事连贯与视角切换，解决单镜头模型无法处理结构化叙事的问题。现有方法依赖关键帧独立生成或修改注意力掩码，导致跨镜头信息隔离或预训练先验破坏。ShotPlan 引入可学习规划Token与分数时间旋转位置编码，在单一去噪过程中实现帧级镜头切换控制。该方法在过渡精度与叙事连贯性上优于基线，但其对预训练位置编码结构的依赖及评估协议的单一性仍存疑。

## 研究背景

视频扩散模型基于潜空间扩散框架，通过3D变分自编码器（3D VAE）将视频压缩为时空潜变量，再由扩散Transformer（DiT）进行去噪。DiT利用旋转位置编码（RoPE）建模时空关系，但3D VAE的时间压缩因子（如4倍）导致潜空间时间步与物理帧存在粒度差异，使得基于离散潜索引的控制信号无法精确对齐用户指定的帧级时间戳。

多镜头视频生成要求模型在单一生成过程中处理不连续的镜头切换，同时保持主体与场景的一致性。主流路线分为两类：一是关键帧生成加图像到视频合成，但镜头间独立生成导致去噪阶段缺乏交互，稀疏关键帧难以捕捉瞬态元素；二是统一去噪过程中的架构修改，如ShotAdapter引入局部注意力掩码，CineTrans使用注意力掩码引导过渡，EchoShot与MultiShotMaster修改RoPE相位区分镜头。这些方法虽实现了镜头分离，但显式注意力约束限制了跨镜头信息传播，修改位置编码则可能破坏预训练时序先验，导致生成结果出现场景不一致或主体身份丢失。

ShotPlan的切入点在于将镜头切换显式表示为可学习的规划Token，作为时间锚点插入视频Token序列。通过保持视频Token的原始RoPE不变，仅对规划Token引入分数时间旋转位置编码（Fractional Temporal RoPE, FRoPE），该方法在不修改注意力结构或位置编码距离的前提下，实现了帧级精度的镜头切换控制，解决了架构修改导致的预训练-微调分布偏移问题。

## 核心方法

### 方法参照系

多镜头视频生成的通用流程是在DiT骨干上注入镜头结构条件。标准做法是通过修改注意力掩码或位置编码来区分镜头，如ShotAdapter使用局部注意力掩码，EchoShot修改RoPE相位。本文的关键差异在于不修改DiT的注意力结构或视频Token的位置编码，而是引入独立的规划Token作为上下文条件信号，通过自注意力机制与视频Token交互。

### 可学习规划Token

规划Token的设计动机在于解决静态语义Token与预训练DiT潜特征空间不兼容的问题。固定语义Token（如“scene cut”文本嵌入）迫使骨干网络适应刚性控制信号，导致性能下降。本文引入可学习规划Token $F_p \in \mathbb{R}^{M \times D}$，其中 $M$ 为镜头切换数量，$D$ 为Token维度。对于硬切，训练单一硬切Token $\mathbf{f}_{cut} \in \mathbb{R}^D$，复制 $M$ 次并分配各自的时间坐标；对于渐变过渡，训练起始与结束Token。

$$
X_{in} = \text{Concat}([X_\tau, F_p])
$$

该公式表示将规划Token与视频Token序列拼接，作为DiT的输入。规划Token通过自注意力与视频Token交互，作为上下文条件信号引导去噪过程。去噪完成后，丢弃规划Token，保留更新后的视频Token进行反Patchify与解码。这种设计允许规划Token与模型联合优化，更好地对齐底层特征空间，提供有效的时序局部化镜头控制。

### 分数时间旋转位置编码

FRoPE的设计动机在于解决VAE时间压缩导致的帧级对齐误差。标准RoPE使用离散潜索引，无法精确匹配用户指定的物理帧时间戳。本文保持视频Token的原始RoPE不变，仅对规划Token引入FRoPE。给定用户指定的过渡时间戳 $t_u$ 和VAE时间压缩因子 $s_t$，映射到分数潜坐标：

$$
\tilde{t}_u = \frac{t_u}{s_t}
$$

该公式将物理帧时间戳转换为连续的分数潜坐标。由于RoPE由正弦函数参数化，天然支持连续坐标，FRoPE使规划Token能够对齐精确的帧级过渡时间戳，而非粗粒度的潜索引。规划Token的空间坐标固定为 $(0, 0)$，视频Token的RoPE保持不变，确保与预训练视频扩散骨干的兼容性。

## 实验评估

实验基于Wan2.1-T2V-14B骨干，分辨率832×480，81帧/样本，使用8块NVIDIA H100 GPU训练3,500步。基线包括CineTrans、EchoShot、HoloCine和MultiShotMaster，覆盖多镜头叙事建模、角色中心过渡、长格式电影生成等路线，但缺失单镜头SOTA基线。

| 模型 | Transition Deviation↓ | Text Align↑ | Character↑ | Scene↑ | Narrative Coherence↑ |
|---|---|---|---|---|---|
| CineTrans | 4.73 | 0.25 | 0.32 | 0.21 | 0.48 |
| EchoShot | 6.95 | 0.26 | 0.31 | 0.23 | 0.51 |
| HoloCine | 2.71 | 0.28 | 0.39 | 0.32 | 0.85 |
| MultiShotMaster | 1.12 | 0.27 | 0.36 | 0.28 | 0.83 |
| ShotPlan | 0.64 | 0.26 | 0.46 | 0.37 | 0.88 |

ShotPlan在Transition Deviation上以0.64显著优于MultiShotMaster（1.12）和HoloCine（2.71），在Character Consistency（0.46 vs 0.39）和Scene Consistency（0.37 vs 0.32）上均领先最强基线，Narrative Coherence达到0.88，高于HoloCine的0.85。

| 消融项 | Transition Deviation↓ | Text Align↑ | Character↑ | Scene↑ |
|---|---|---|---|---|
| Static Semantic Tokens | 0.82 | 0.21 | 0.28 | 0.29 |
| Latent Addition | 1.76 | 0.25 | 0.42 | 0.36 |
| Global AdaLN | 5.64 | 0.28 | 0.39 | 0.37 |
| Local AdaLN | 4.39 | 0.26 | 0.37 | 0.36 |
| w/o Fractional RoPE | 2.13 | 0.27 | 0.37 | 0.34 |
| ShotPlan (Full) | 0.64 | 0.26 | 0.46 | 0.37 |

消融显示，移除FRoPE导致Transition Deviation从0.64升至2.13，验证了分数坐标对帧级对齐的关键作用。静态语义Token的Character Consistency（0.28）显著低于可学习Token（0.46），表明固定语义Token与潜特征空间不兼容。Global AdaLN的Transition Deviation高达5.64，说明全局调制无法提供有效的时序局部化控制。

评估协议存在局限：使用Gemini 2.5生成100条Prompt并指定镜头对，缺乏跨数据集泛化验证；Transition Deviation基于TransNet V2检测，可能受检测器精度影响；未报告置信区间，数值比较需谨慎。代码未公开，超参数（如规划Token初始化标准差0.02）未提供敏感性分析。

## 关联研究分析

从方法设计看，ShotPlan与ShotAdapter均使用可学习Token控制镜头切换，但ShotAdapter依赖局部注意力掩码限制跨镜头交互，而ShotPlan通过标准自注意力允许信息自由流动。这一差异源于任务特性：ShotAdapter关注镜头数量与时长控制，掩码有助于分离镜头；ShotPlan强调跨镜头一致性，掩码会削弱主体与场景的连贯性。ShotPlan的In-context注入策略是否在所有镜头切换类型中均优于掩码方法，论文未给出系统对比。

从问题动机看，ShotPlan与CameraCtrl均使用显式几何信号引导生成，但CameraCtrl控制空间运动（相机姿态），ShotPlan控制时间结构（镜头切换）。CameraCtrl通过Plücker嵌入将相机位姿编码为空间射线，注入注意力层；ShotPlan通过FRoPE将时间戳编码为分数坐标，注入规划Token。两者均面临预训练模型对几何/时间结构的隐含理解依赖问题，但ShotPlan的FRoPE设计更直接地解决了VAE压缩导致的粒度不匹配，而CameraCtrl的Plücker嵌入依赖预训练模型对几何结构的先验。

## 总结

ShotPlan解决的核心矛盾是单一去噪过程中帧级镜头切换控制与预训练位置编码结构的冲突。现有方法通过修改注意力掩码或RoPE相位实现镜头分离，但破坏了跨镜头信息流动或预训练时序先验。ShotPlan引入可学习规划Token与FRoPE，在不修改DiT架构的前提下实现帧级控制，Transition Deviation降至0.64，Narrative Coherence达0.88。其边界在于评估协议依赖Gemini生成的单一Prompt集，缺乏跨数据集验证；FRoPE的分数坐标假设RoPE正弦函数对连续坐标的线性响应，未探讨非线性的影响。当镜头切换频率极高或过渡类型复杂时，规划Token的时序局部化能力是否仍能保证跨镜头一致性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.17675)