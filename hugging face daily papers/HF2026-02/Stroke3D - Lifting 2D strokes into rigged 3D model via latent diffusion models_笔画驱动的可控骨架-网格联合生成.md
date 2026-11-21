# HuggingFace最新推荐论文 ｜Stroke3D: Lifting 2D strokes into rigged 3D model via latent diffusion models ｜笔画驱动的可控骨架-网格联合生成

研究机构：浙江大学、美国哈佛大学

作者：Ruisi Zhao、Haoren Zheng、Zongxin Yang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.09713)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.09713)

> 可动画化3D资产生成旨在从静态几何中解耦出骨骼层级与蒙皮权重，以支持实时变形与动画。现有方法或依赖稀缺的骨架-网格配对数据，或采用端到端范式导致骨架结构不可控。Stroke3D 通过引入用户绘制的2D笔画作为显式拓扑约束，构建了“骨架优先”的两阶段生成管线。该框架在结构对齐度上显著优于基线，但其解耦架构在网格细节多样性与复杂拓扑鲁棒性上仍存疑。

## 研究背景

当3D资产需要进入物理仿真或动画引擎时，静态网格必须被赋予骨骼层级（Skeletal Hierarchy）与蒙皮权重（Skinning Weights）。这一过程称为绑定（Rigging），其核心难点在于几何拓扑与骨骼结构的一致性：若骨骼位置偏离关节中心，或骨骼数量与网格语义不匹配，后续的动画变形将产生撕裂或穿模。传统绑定依赖专家手动操作，成本高昂且难以规模化，因此自动化生成成为关键。

主流自动化路线分为两类：一是基于网格的逆向绑定，如 RigNet 和 SKDream，它们从已有网格推断骨架，但受限于高质量配对数据的稀缺，且无法在生成前控制骨架形态；二是端到端的骨架-网格联合生成，如 MagicArticulate 和 UniRig，它们通过自回归或扩散模型直接输出骨架，但缺乏显式结构约束，导致骨架常出现在非关节位置或缺失关键关节，结果不可预测。Stroke3D 的切入点在于将用户意图显式化：通过2D笔画定义骨架拓扑，将“结构控制”从隐式学习转化为显式输入，从而在生成阶段即锁定骨架的几何与拓扑形态。

## 核心方法

### 方法参照系

Stroke3D 属于“动画 Rigged 资产”生成路线，但区别于 AniGen 等采用统一场表示的联合生成方法，其核心差异在于采用“骨架优先”的解耦架构：先生成骨架，再基于骨架生成网格。这种解耦使得骨架生成可以独立引入显式结构条件，而网格生成则复用成熟的骨架到网格（Skeleton-to-Mesh）模型，避免了在单一潜空间中同时优化几何与骨骼的复杂性。

### 骨架图变分自编码器与扩散生成

骨架生成阶段的核心是将离散图结构映射到连续潜空间。Stroke3D 将3D骨架表示为无向图 $G = (\mathbf{X}, \mathbf{E})$，其中 $\mathbf{X} \in \mathbb{R}^{N \times 3}$ 为关节坐标，$\mathbf{E}$ 为边集。Sk-VAE 编码器通过图卷积网络（GCN）和 TransformerConv 聚合邻域信息，将图编码为潜变量 $z$。训练目标包含重建损失与KL散度正则项，以约束潜空间分布：

$$
\mathcal{L}_{\text{VAE}} = \| \mathbf{X} - \hat{\mathbf{X}} \|_2^2 + \beta \cdot D_{\text{KL}}(q(z|\mathbf{X}, \mathbf{E}) \| \mathcal{N}(0, I))
$$

该公式确保潜变量 $z$ 既保留骨架的几何细节，又具备扩散模型所需的平滑先验。在生成阶段，Sk-DiT 在潜空间中执行去噪，其关键创新在于结构条件注入：将用户绘制的2D笔画坐标 $\mathbf{J}_{xy}$ 与噪声潜变量拼接，并通过交叉注意力融合文本语义。这一设计解决了纯文本生成中骨架拓扑模糊的问题，使生成的3D骨架在拓扑上与用户输入的2D图同构，从而实现了显式的结构控制。

### 基于偏好优化的网格合成增强

骨架生成后，Stroke3D 复用 SKDream 模型进行网格合成，但针对其纹理缺失与对齐度不足的问题，引入了两项增强。首先，构建 TextuRig 数据集，从 Objaverse-XL 中筛选具备纹理与骨架的资产，并通过 VLM 重新标注，解决了训练数据中纹理信息缺失的问题。其次，应用 SKA-DPO（Skeleton Alignment Direct Preference Optimization）策略。该策略利用骨架对齐分数（SKA Score）作为奖励信号，构建偏好对进行直接偏好优化：

$$
\mathcal{L}_{\text{DPO}} = -\mathbb{E}_{(x, y_w, y_l)} \left[ \log \sigma \left( \beta \left( \log \frac{\pi_\theta(y_w|x)}{\pi_{\text{ref}}(y_w|x)} - \log \frac{\pi_\theta(y_l|x)}{\pi_{\text{ref}}(y_l|x)} \right) \right) \right]
$$

其中 $y_w$ 和 $y_l$ 分别为高对齐度和低对齐度的网格样本。该公式通过最大化高对齐样本与低对齐样本的对数似然差，引导模型生成与骨架结构更一致的网格，显著提升了最终资产的几何保真度与结构连贯性。

## 实验评估

| 方法 | CD-J2J (All) | CD-J2B (All) | CD-B2B (All) | Mean_Inst. SKA |
| :--- | :--- | :--- | :--- | :--- |
| RigNet | 0.078 | 0.066 | 0.065 | - |
| SKDream | 0.111 | 0.092 | 0.083 | 80.43 |
| MagicArticulate | 0.052 | 0.041 | 0.034 | - |
| UniRig | 0.063 | 0.051 | 0.041 | - |
| **Stroke3D** | **0.048** | **0.039** | **0.034** | **87.83** |

Stroke3D 在 MagicArticulate 和 SKDream 基准上评估，基线覆盖 RigNet、SKDream、MagicArticulate 和 UniRig，但缺失 AniGen 和 Rigel3D 等最新联合生成方法的直接对比。在骨架生成任务中，Stroke3D 的 CD-J2J 为 0.048，低于 UniRig 的 0.063 和 SKDream 的 0.111，表明其在关节位置预测上具有优势。在网格生成任务中，Stroke3D 的 Mean_Inst. SKA 分数为 87.83，显著高于 SKDream 的 80.43 和 SDEdit 的 72.11，验证了 TextuRig 数据增强与 SKA-DPO 策略的有效性。

| Margin | Mean_Inst. SKA | Mean_Class SKA |
| :--- | :--- | :--- |
| 0.05 | 86.95 | 83.03 |
| **0.10** | **87.83** | **84.36** |
| 0.15 | 87.84 | 84.21 |
| 0.20 | 86.96 | 83.12 |

消融实验显示，SKA-DPO 的偏好分数边际（Margin）为 0.10 时性能最优，Mean_Inst. SKA 达到 87.83。当 Margin 增大至 0.20 时，分数下降至 86.96，表明过大的偏好间隔可能抑制模型对细微几何差异的学习。此外，结构条件（Jxy）的缺失导致模型收敛速度显著变慢，验证了显式拓扑约束对训练效率的关键作用。

评估指标主要依赖 Chamfer Distance (CD) 和 SKA Score，缺乏对网格纹理质量、动画平滑度及物理稳定性的量化评估。论文未报告代码开源状态，但提供了项目页面。由于未与 AniGen 等统一场方法对比，无法直接判断解耦架构在复杂拓扑下的鲁棒性是否弱于联合生成。

## 关联研究分析

从问题动机看，Stroke3D 与 UniRig 和 MagicArticulate 的核心差异在于控制粒度。UniRig 和 MagicArticulate 依赖大规模骨架-网格数据集进行端到端学习，其骨架结构由数据分布隐式决定，用户无法在生成前干预。Stroke3D 通过2D笔画显式定义拓扑，将控制权从数据分布转移至用户交互。这一差异源于任务特性：UniRig 追求通用性，而 Stroke3D 追求可控性。然而，Stroke3D 的笔画输入要求用户具备基本的3D结构认知，这是否限制了其在非专业用户中的普及，论文未给出回答。

从方法设计看，Stroke3D 与 AniGen 的架构差异显著。AniGen 采用统一场表示（S3 Fields）联合生成形状、骨骼和蒙皮，旨在保证拓扑一致性；Stroke3D 采用解耦的两阶段架构，先骨架后网格。AniGen 的联合生成可能更擅长处理复杂拓扑，但缺乏显式结构控制；Stroke3D 的解耦架构便于引入笔画条件，但可能牺牲网格细节的多样性。Stroke3D 在 SKA Score 上的优势（87.83 vs AniGen 未报告）表明其在结构对齐上有效，但 AniGen 在 PartNet-Mobility VBench 上的 0.92 分数暗示其在动画质量上可能更优。解耦策略在复杂拓扑下的鲁棒性是否弱于联合生成，论文未提供对比实验。

## 总结

Stroke3D 旨在解决可动画化3D资产生成中骨架结构不可控与数据稀缺的矛盾。其切入点在于将用户绘制的2D笔画作为显式拓扑约束，通过“骨架优先”的解耦架构，将结构控制从隐式学习转化为显式输入。方法上，Sk-VAE 和 Sk-DiT 实现可控骨架生成，TextuRig 和 SKA-DPO 增强网格合成。实验表明，Stroke3D 在 CD-J2J 上达到 0.048，Mean_Inst. SKA 达到 87.83，显著优于 SKDream 和 UniRig。然而，其评估仅覆盖几何对齐度，缺乏对动画质量与物理稳定性的验证，且未与 AniGen 等联合生成方法对比。当笔画输入存在噪声或拓扑错误时，解耦架构的鲁棒性是否弱于联合生成，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.09713)