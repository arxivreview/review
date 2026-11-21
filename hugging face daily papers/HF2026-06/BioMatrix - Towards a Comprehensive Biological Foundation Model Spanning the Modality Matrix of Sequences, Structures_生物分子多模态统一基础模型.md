# HuggingFace最新推荐论文 ｜BioMatrix: Towards a Comprehensive Biological Foundation Model Spanning the Modality Matrix of Sequences, Structures, and Language ｜生物分子多模态统一基础模型

研究机构：中国人民大学、浙江大学

论文原文见 [arXiv](https://arxiv.org/abs/2606.22138)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.22138)

> 生物分子设计面临序列、结构与功能描述割裂的困境，现有模型要么仅覆盖单一实体类型，要么缺乏原生结构生成能力。BioMatrix 通过统一离散化词表将分子与蛋白质的序列、3D 结构及自然语言映射至同一解码器架构，实现了跨模态与跨实体的联合建模。其核心价值在于验证了单一骨干网络在 80 项任务上匹配专用模型的能力，但离散 Token 在精细几何重建上的精度瓶颈及小数据任务的不稳定性仍存疑。

## 研究背景

生物分子表征存在固有的多模态互补性：序列提供符号身份，结构决定物理相互作用，语言承载设计意图与文献知识。然而，传统模型往往将这三种视图隔离处理，导致无法直接利用自然语言描述引导结构生成，或无法在单一架构中同时处理小分子与蛋白质的交互关系。解决这一割裂的关键在于构建原生多模态（Native Multimodality）能力，即让模型将序列、结构和文本视为同等地位的一等公民输入与输出，而非通过适配器进行后期融合。

现有研究沿两条独立轴线演进：一是生物分子内容与自然语言的耦合，二是多实体类型的覆盖。在耦合轴线上，适配器范式（如 BioMedGPT）存在输入输出不对称，难以原生生成非文本模态；原生 Token 化范式（如 ESM3）虽能统一序列与结构，但局限于蛋白质单一实体。在覆盖轴线上，AlphaFold3 和 LOGOS 实现了多实体建模，但缺乏自然语言接口或显式结构建模。BioMatrix 的切入点在于同时满足这两条轴线：通过统一的离散 Token 化方案，将分子（SMILES/SELFIES/3D）和蛋白质（氨基酸/3D）以及自然语言整合进单一词表，填补了“原生多模态”与“广实体覆盖”不可兼得的技术空白。

## 核心方法

### 统一多模态 Token 化架构

BioMatrix 基于 Qwen3 解码器架构，核心差异在于将所有生物分子模态离散化为共享词表中的 Token，摒弃了外部编码器或投影适配器。分子结构采用 MolStrucTok 方案，蛋白质结构采用 GCP-VQVAE 方案，两者均输出离散几何代码。这种设计使得折叠、逆折叠、结构生成等任务转化为同一 Next-Token 预测目标下的不同条件生成模式，消除了模态间的架构壁垒。

### 分支解耦分子结构解码器

针对 MolStrucTok 原始解码器在处理异构几何目标时的干扰问题，BioMatrix 引入了分支解耦（Branch-decoupled）解码器。原始方案使用共享主干回归距离、极角、方位角及其符号，导致不同物理量纲的目标相互干扰。BioMatrix 移除共享主干，为每个几何分量设置独立的 MLP 头，直接基于量化代码进行预测。

$$ \mathbf{g}_i = (d_i, \theta_i, |\phi_i|, \text{sgn}(\phi_i)) $$

该公式表示原子 $i$ 的局部球面坐标描述符，其中 $d_i$ 为径向距离，$\theta_i$ 和 $\phi_i$ 为角度。通过解耦预测，平均分量 RMSD 在 QM9-2014 上改善了约 0.1 Å，提升了结构重建保真度，同时保持了词表大小和接口不变。

### 蛋白质结构 Token 对齐机制

蛋白质结构 Token 化采用 GCP-VQVAE，将骨架几何编码为每残基一个的离散代码，词表大小为 4096。关键在于保持残基级序列与结构 Token 的一一对应关系。BioMatrix 引入专用的 26 个氨基酸 Token，避免 Qwen3 分词器将氨基酸合并为子词，从而破坏与结构 Token 的对齐。这种因子化表示（Factored Representation）避免了构建巨大的联合残基-结构词表，使得折叠（从 AA Token 生成结构 Token）和逆折叠（反向）能在同一自回归框架下高效执行。

## 实验评估

实验覆盖 80 项任务，基线包括 ESM3、RFDiffusion、FoldFlow 及通用 LLM（GPT-4, Claude）。BioMatrix 在 77 项任务上达到 SOTA 或具有竞争力。在分子生成任务中，BioMatrix-4B 在 MOSES 数据集上 Validity 达 0.998，Novelty 达 0.925，优于 MolGPT 和 OMG-GPT。在蛋白质骨架生成中，BioMatrix-4B 在 TS50 基准上取得 scTM 0.963，超过 RFDiffusion (0.914) 和 FoldFlow (0.540)，接近原生 PDB 上限 0.969。

| 任务 | 模型 | 指标 | 数值 |
| :--- | :--- | :--- | :--- |
| 分子生成 (MOSES) | BioMatrix-4B (SELFIES) | Validity | 0.998 |
| 分子生成 (MOSES) | BioMatrix-4B (SELFIES) | Novelty | 0.925 |
| 骨架生成 (TS50) | BioMatrix-4B | scTM | 0.963 |
| 骨架生成 (TS50) | RFDiffusion | scTM | 0.914 |

消融实验显示，SMILES 与 SELFIES 具有互补性，SMILES 在精确匹配任务（如名称转换）上表现更优，而 SELFIES 在生成多样性上略胜。从 1.7B 到 4B 的缩放收益在知识密集型任务（如分子名称转换、文本生成）上显著，I2F EM 提升 14-15 点；但在小数据任务上，混合 SFT 训练导致性能不稳定，需采用任务组变体而非单一全任务模型。

评估边界方面，论文未报告 ProteinGym 适应度预测结果，无法直接对比 Protriever 等 SOTA。离散 Token 方案在精细侧链构象上的表达能力受限，3D 几何精度依赖 Token 化器的重建上限。代码与权重已开源，训练使用 64 块 H100 GPU，预训练 304.4B Token，具备可复现性。

## 关联研究分析

从生成机制看，BioMatrix 的离散 Token 自回归路线与 RFDiffusion 和 FoldFlow 的连续坐标扩散/流匹配路线形成鲜明对比。RFDiffusion 在 SE(3) 群上操作连续坐标，物理稳定性高但采样慢；BioMatrix 将结构离散化，牺牲了部分几何连续性以换取与语言模型的无缝集成。这种差异源于任务目标：BioMatrix 强调跨模态交互（如文本引导设计），而 RFDiffusion 侧重从头骨架生成的物理可行性。离散化是否必然导致几何精度低于连续扩散，论文未提供直接消融对比，仅在 scTM 上展示了竞争力。

从实体覆盖看，BioMatrix 与 ESM3 和 AlphaFold3 存在显著差异。ESM3 仅覆盖蛋白质且缺乏自然语言生成能力，BioMatrix 是其超集，增加了小分子和文本模态。AlphaFold3 覆盖多实体但无自然语言接口，BioMatrix 通过统一词表实现了语言与结构的直接映射。这种设计使得 BioMatrix 能直接利用文献中的文本知识进行设计，而 AlphaFold3 需通过结构化配置指定意图。然而，BioMatrix 在跨实体交互任务（如蛋白-配体亲和力预测）上的优势是否源于统一的表示空间，还是仅得益于大规模预训练数据，论文未完全解耦这两者的贡献。

## 总结

BioMatrix 解决了生物分子建模中多模态割裂与实体覆盖狭窄的矛盾，通过统一离散 Token 化方案在单一解码器架构中实现了分子与蛋白质的原生多模态生成。其核心贡献在于验证了 304.4B Token 预训练下，单一骨干网络在 80 项任务上匹配专用模型的能力，尤其在文本引导生成和跨模态交互上表现突出。然而，离散 Token 在精细 3D 几何重建上的精度瓶颈及小数据任务训练的不稳定性暴露了该路线的边界。当支持集增大或任务复杂度提升时，离散化表示能否持续保持对连续扩散模型的竞争力，论文未给出明确回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.22138)