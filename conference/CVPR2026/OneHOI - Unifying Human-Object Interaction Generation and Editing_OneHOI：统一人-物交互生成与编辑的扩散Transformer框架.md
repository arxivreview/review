# CVPR2026最新论文 ｜OneHOI: Unifying Human-Object Interaction Generation and Editing ｜OneHOI：统一人-物交互生成与编辑的扩散Transformer框架

研究机构：新加坡南洋理工大学、中山大学

作者：Jiun Tian Hoe、Weipeng Hu、Xudong Jiang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14062)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14062)

> 人-物交互（Human-Object Interaction, HOI）建模旨在从视觉观测中恢复人类与物体间的语义关系及空间配置，其核心价值在于弥合视觉感知与物理交互控制之间的鸿沟。现有生成式方法将HOI任务割裂为布局条件生成与文本引导编辑两个独立分支，前者无法处理混合条件输入，后者难以解耦姿态与接触且不支持多实例交互。OneHOI通过引入关系扩散Transformer（Relational Diffusion Transformer, R-DiT），在单一条件去噪流程中统一了生成与编辑任务，实现了布局引导、无布局、任意掩码及混合条件的灵活控制。该框架在2D图像生成与编辑任务上取得了显著性能提升，但其对3D几何精度与物理动力学一致性的验证仍属空白。

## 研究背景

当扩散模型（Diffusion Model）被应用于图像合成时，其核心挑战在于如何从噪声中恢复出符合语义约束的结构化场景。传统布局条件生成方法（如InteractDiffusion）通过指定物体边界框来引导生成，但这种“物体级”控制仅解决了实体定位问题，未能捕捉实体间的交互关系。例如，模型可能正确放置了人与手机，却无法生成“打电话”这一特定动作所需的姿态与接触几何。这种语义与几何的解耦导致生成结果在关系层面缺乏合理性，表现为姿态僵硬或接触穿透。

HOI领域的研究长期聚焦于检测与3D重建，前者关注三元组识别，后者追求几何精度与物理合理性。然而，生成式HOI研究在2023年后才逐渐兴起，并分化为两条互不兼容的路线：一是基于布局的生成，二是基于文本的编辑。生成路线受限于封闭的布局输入格式，无法处理仅包含物体或混合条件的场景；编辑路线则依赖隐式模型先验，缺乏对交互结构的显式建模，导致在多实例场景中发生角色混淆或交互混合。这种碎片化发展使得单一模型无法同时满足生成时的空间可控性与编辑时的语义灵活性，构成了当前HOI生成领域的核心瓶颈。OneHOI的切入点在于将生成与编辑视为同一条件去噪过程的不同视图，通过显式建模交互结构，实现了对多模态输入的统一处理。

## 核心方法

### 方法参照系

OneHOI基于多模态扩散Transformer（Multi-Modal Diffusion Transformer, MM-DiT）骨干网络，继承自Flux.1 Kontext架构。与标准布局条件DiT（如Eligen）相比，本文的关键差异在于引入了显式的交互结构建模模块，将扩散过程从“像素排列”重构为“关系实现”。标准DiT将场景视为独立物体的集合，缺乏对动词介导的交互拓扑的感知，导致生成结果在关系层面浅薄。

### 动作接地与HOI编码器

标准布局模型仅对物体进行空间接地，缺乏对动作本身的语义与空间感知。OneHOI引入动作接地（Action Grounding, AG）模块，将动作区域定义为主体与物体区域的并集 $R_n^a = R_n^s \cup R_n^o$，而非InteractDiffusion中使用的交集或跨度矩形。这一设计动机在于，动作的注意力足迹通常覆盖主体与物体的联合区域，并集定义更贴合DiT的自然注意力模式，且在重叠与分离场景下均具鲁棒性。

为消除多实例场景中的角色混淆，HOI编码器向HOI令牌流注入细粒度的身份线索。对于实例 $n$ 和角色 $r \in \{s, o, a\}$，增强后的令牌 $\tilde{h}_n^r$ 通过门控残差连接计算：

$$ \tilde{h}_n^r = h_n^r + \lambda \cdot \text{MLP}(\text{LN}(h_n^r) \oplus e_{role}(r) \oplus e_{inst}(n) \oplus e_{box}(b_n^r)) $$

其中 $\lambda$ 为可学习门控，$e_{role}$、$e_{inst}$ 和 $e_{box}$ 分别为角色嵌入、实例正弦嵌入和边界框傅里叶嵌入。该设计确保了模型明确知晓每个令牌的角色归属与实例身份，防止了如“人1持猫”这类错误交互的生成。

### 结构化HOI注意力与HOI RoPE

结构化HOI注意力通过掩码机制强制动词介导的注意力拓扑。在HOI令牌间，禁止主体与物体的直接连接，强制信息流经动作令牌 $A_n$，从而显式编码交互结构。在HOI与图像间，当提供布局时，约束注意力仅在对应区域 $R_n^s, R_n^o, R_n^a$ 内流动：

$$ M_{HI}(q, k) = \mathbb{I}[q \in \{S_n, A_n, O_n\} \land k \in I \land \text{pos}(k) \in R_n^{role(q)}] $$

此约束确保了空间接地与语义结构的一致性。

为解决多实例间的特征串扰，HOI RoPE为每个交互实例分配独特的位置索引。与标准3D RoPE不同，HOI RoPE将同一实例的所有HOI令牌映射到图像网格中的单一独特位置，从而在位置编码层面隔离不同实例，防止属性交换或交互混合。

## 实验评估

实验在IEBench、HICO-DET及新提出的MultiHOIEdit基准上进行，基线覆盖InteractDiffusion、HOIEdit、Eligen等生成与编辑方法。在布局无关HOI编辑任务中，OneHOI在Editability-Identity指标上达到0.638，较最强基线InteractEdit提升10.0%；在HOI生成任务中，Spatial Score达到0.6104，超越InteractDiffusion的0.5768。

| 任务 | 方法 | Editability-Identity | HOI Editability | Spatial | HOI Acc |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 布局无关编辑 | InteractEdit | 0.573 | 0.514 | - | - |
| 布局无关编辑 | OneHOI | **0.638** | **0.596** | - | - |
| 布局引导编辑 | InteractEdit+InteractDiff | 0.559 | 0.520 | 0.749 | - |
| 布局引导编辑 | OneHOI | **0.638** | **0.570** | **0.822** | - |
| HOI生成 | InteractDiffusion | - | - | 0.5768 | 0.4505 |
| HOI生成 | OneHOI | - | - | **0.6104** | **0.4528** |

消融实验显示，HOI编码器的引入对HOI生成精度的提升最为显著，从基线的0.3061提升至0.4254，表明显式身份线索对多实例解耦至关重要。结构化注意力进一步将HOI精度提升至0.4504，而HOI RoPE在Multi-HOI编辑任务中贡献了最大的ImageReward提升，从0.1944增至0.2046，验证了位置隔离对减少串扰的有效性。

评估边界方面，本文主要依赖2D图像质量指标（PickScore, HPS, ImageReward）与2D空间对齐指标（Spatial Score, HOI Acc），缺乏3D几何精度（如Chamfer Distance）与物理合理性（如Penetration Depth）的验证。代码已开源，但训练细节（如LoRA秩、学习率）未在正文中详述，可能影响复现性。

## 关联研究分析

从问题动机看，OneHOI与InteractDiffusion均关注布局条件生成，但前者将布局视为刚性约束，后者则通过动作接地与结构化注意力实现了布局的柔性解释。InteractDiffusion的“Between”区域定义在主体与物体分离时失效，而OneHOI的并集定义通过覆盖联合区域解决了这一几何歧义。这一差异源于任务特性的不同：InteractDiffusion聚焦于单一交互的精确生成，而OneHOI需处理多实例场景下的交互解耦，因此需要更鲁棒的空间接地策略。

从方法设计看，OneHOI与HOIEdit同属编辑任务，但HOIEdit依赖隐式文本引导，缺乏对交互结构的显式建模，导致在多实例场景中发生角色混淆。OneHOI通过HOI编码器与结构化注意力显式编码角色与实例身份，实现了可靠的交互解耦。然而，HOIEdit在单实例编辑中的身份保持能力可能优于OneHOI，因为后者在联合训练中可能牺牲部分身份细节以换取交互结构的准确性。这种权衡在论文中未通过身份保持指标（如ID-Sim）进行量化对比，仅通过Editability-Identity复合指标间接反映。

## 总结

OneHOI旨在解决HOI生成与编辑任务割裂、多实例交互解耦困难的核心矛盾。其切入点在于将生成与编辑统一为单一条件去噪过程，并通过R-DiT显式建模交互结构，克服了现有方法依赖隐式先验或刚性布局输入的局限。该方法通过动作接地、HOI编码器、结构化注意力与HOI RoPE四个模块，实现了布局引导、无布局、任意掩码及混合条件的灵活控制。实验表明，OneHOI在布局无关编辑的Editability-Identity指标上达到0.638，在HOI生成的Spatial Score上达到0.6104，均超越现有基线。然而，本文的评估局限于2D图像质量与空间对齐，未验证3D几何精度与物理动力学一致性。当交互涉及复杂接触力学时，2D空间对齐是否足以保证3D物理合理性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14062)