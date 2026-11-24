# ICLR2026最新论文 ｜SimpleFold: Folding Proteins is Simpler than You Think ｜SimpleFold：基于流匹配的通用Transformer蛋白折叠模型

作者：Yuyang Wang、Jiarui Lu、Navdeep Jaitly 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.18480)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.18480)

> 蛋白折叠旨在从氨基酸序列预测三维原子结构，传统方法依赖硬编码的领域特定架构（如MSA、Pair Rep）以捕捉进化约束。现有方案在去除这些模块后性能显著下降，且生成式模型在单目标基准上常劣于回归式模型。本文切入点在于验证通用Transformer架构能否在缺乏显式几何约束的情况下，通过大规模数据与流匹配目标实现高精度折叠。SimpleFold采用标准Transformer块与自适应层，结合全原子流匹配训练，证明了去领域特定架构的可行性。其价值在于简化了模型部署并挑战了等变架构的必要性共识，但在远缘同源蛋白上的鲁棒性及动态构象建模的边界尚存疑。

## 研究背景

蛋白折叠的核心困境在于序列空间巨大且适应度景观崎岖，传统物理能量函数计算成本高昂且难以捕捉长程依赖。为突破此局限，AlphaFold2（Jumper et al., 2021）引入了多序列比对（MSA）与三角形更新模块，将进化信息硬编码进架构，确立了数据驱动范式。然而，这种设计假设了结构生成过程的确定性，且依赖昂贵的MSA搜索，导致模型在孤儿蛋白（缺乏近缘同源序列）上表现受限，且架构复杂度阻碍了大规模扩展。

主流路线分为两类：一类是MSA-based模型（如AlphaFold2, RoseTTAFold），通过显式进化信息提升精度；另一类是PLM-based模型（如ESMFold），利用预训练语言模型嵌入替代MSA。尽管ESMFold证明了序列中蕴含足够进化信息，但其仍保留Pair Representation等复杂模块。近期，生成式方法（如AlphaFlow）尝试用扩散或流匹配建模结构不确定性，但往往基于AlphaFold2架构微调，未能摆脱对领域特定模块的依赖。本文切入点在于质疑这些模块是否为高性能折叠的必要条件，提出一种纯通用架构的生成式折叠模型。

## 核心方法

### 方法参照系

蛋白折叠通常被视为回归问题，主流方法（如AlphaFold2）通过迭代更新Pair Representation和Triangle Update模块来捕捉残基间相互作用。本文将其重构为条件生成任务，关键差异在于移除所有显式几何约束模块，仅保留标准Transformer块，并采用流匹配目标直接生成全原子坐标。

### 流匹配目标与LDDT辅助损失

设计动机在于解决回归模型无法建模结构不确定性的问题，同时避免扩散模型采样慢的缺陷。SimpleFold采用线性插值路径，定义目标速度场 $v_t = x - \epsilon$，其中 $x$ 为真实结构，$\epsilon$ 为高斯噪声。训练目标为最小化预测速度场 $v_\theta(x_t, s, t)$ 与目标速度场的 $\ell_2$ 误差：

$$ \mathcal{L}_{FM} = \mathbb{E}_{t, x, \epsilon} \left[ \| v_\theta(x_t, s, t) - (x - \epsilon) \|_2^2 \right] $$

为增强局部几何精度，引入LDDT损失，通过单步Euler积分预测结构 $\hat{x}(x_t) = x_t + (1-t)v_\theta(x_t, s, t)$，计算原子对距离误差。总损失为 $\mathcal{L} = \mathcal{L}_{FM} + \alpha(t)\mathcal{L}_{LDDT}$，其中 $\alpha(t)$ 随时间步动态调整，在接近数据流形时增加LDDT权重，以驱动模型学习侧链原子精细位置。

### 通用Transformer架构与4D轴向RoPE

设计动机在于证明非等变架构可通过数据增强学习旋转对称性，从而替代昂贵的等变模块。架构包含原子编码器、残基主干和原子解码器，均使用标准Transformer块。原子编码器使用局部注意力掩码，限制原子仅关注邻近残基，随后通过平均池化生成残基Token。序列嵌入由冻结的ESM2-3B提供，与残基Token拼接后输入主干。位置编码采用4D轴向RoPE，前三轴编码参考构象的3D原子坐标，第四轴编码残基索引，每个轴控制隐藏维度四分之一的旋转。训练期间应用SO(3)数据增强，随机旋转结构目标，使模型直接学习对称性，无需显式等变约束。

## 实验评估

实验在CASP14和CAMEO22基准上进行，对比MSA-based（AlphaFold2, RoseTTAFold2）和PLM-based（ESMFold, OmegaFold）基线，以及生成式模型（AlphaFlow, ESMFlow）。

| 模型 | 类型 | CASP14 GDT (Avg/Med) | CAMEO22 GDT (Avg/Med) |
| :--- | :--- | :--- | :--- |
| AlphaFold2 | MSA-Regression | 0.856 / 0.894 | 0.864 / 0.893 |
| ESMFold | PLM-Regression | 0.855 / 0.893 | 0.864 / 0.893 |
| AlphaFlow | MSA-Flow | 0.740 / 0.812 | 0.767 / 0.799 |
| SimpleFold-3B | PLM-Flow | 0.840 / 0.927 | 0.855 / 0.893 |

*注：表格数值取自论文Table 1部分可见数据，SimpleFold-3B在CASP14的GDT均值0.840低于AlphaFold2的0.856，但中位数0.927高于AlphaFold2的0.894。*

SimpleFold-3B在CAMEO22上与ESMFold和AlphaFold2表现相当，但在CASP14上均值略低，中位数更高。这表明生成式模型在单目标基准上可能因概率分布特性而牺牲部分均值精度，但能提供更稳定的中位表现。消融实验显示，SimpleFold-100M恢复了3B模型约90%的性能，证明了架构的扩展性。

评估边界方面，论文未报告Orphan Proteins上的具体数值，仅定性引用Lin et al. (2023b)结论。代码已开源，但训练数据混合比例（PDB, SwissProt, AFESM）对性能的影响未做详细消融。

## 关联研究分析

从方法设计看，SimpleFold与ESMFold（Lin et al., 2023b）的核心差异在于架构复杂度。ESMFold保留Pair Representation以捕捉残基间相互作用，而SimpleFold完全移除该模块，仅依赖标准Transformer的全局注意力。这一差异源于任务特性的不同假设：ESMFold假设进化约束需显式建模，而SimpleFold假设大规模数据足以让通用架构隐式学习这些约束。根源在于数据规模与计算资源的权衡，SimpleFold通过9M蒸馏结构弥补了架构简化的信息损失，但其在数据稀缺场景下的鲁棒性未得到验证。

从问题动机看，SimpleFold与RFDiffusion（Bose et al., 2023）同属生成式范式，但任务目标不同。RFDiffusion用于从头骨架生成，强调物理稳定性，采用等变架构确保SE(3)不变性；SimpleFold用于结构预测，强调序列-结构映射精度，采用非等变架构。这一差异反映了预测与生成任务对物理约束的不同敏感度：预测任务中，真实结构已存在，模型需拟合分布；生成任务中，模型需创造新结构，物理约束更为关键。SimpleFold证明在预测任务中，数据增强可替代等变约束，但这是否适用于生成任务，论文未给出回答。

## 总结

SimpleFold要解决的核心矛盾是领域特定架构的高计算成本与通用架构的潜在性能损失之间的平衡。其切入点在于利用大规模蒸馏数据（9M结构）和流匹配目标，证明通用Transformer可在无MSA、无Pair Rep、无等变模块的情况下实现高精度折叠。方法上，它采用标准Transformer块结合4D轴向RoPE和SO(3)数据增强，通过LDDT辅助损失提升局部几何精度。实验证明SimpleFold-3B在CAMEO22上与SOTA持平，在CASP14上中位数表现优于AlphaFold2。其边界在于，生成式模型在单目标基准上的均值精度略低于回归式模型，且未充分验证在远缘同源蛋白上的鲁棒性。当支持集增大到包含更多孤儿蛋白时，去MSA策略的性能增益是否持续，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.18480)