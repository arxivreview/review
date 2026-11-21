# CVPR2026最新论文 ｜LRDUN: A Low-Rank Deep Unfolding Network for Efficient Spectral Compressive Imaging ｜低秩深度展开网络

研究机构：武汉大学

作者：He Huang、Yujun Guo、Wei He

论文原文见 [arXiv](https://arxiv.org/abs/2511.18513)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.18513)

> 高光谱压缩成像重建面临病态逆问题与高维计算开销的双重瓶颈。现有深度展开网络直接在全维高光谱立方体上迭代，导致每阶段需从有限二维测量推断海量未知数，病态性严重且算力冗余。本文切入点在于将低秩分解从正则化项提升为前向模型重构基础，通过交替优化谱基与子空间图像两个低维分量来恢复高光谱数据。该策略在保持物理一致性的同时大幅降低计算复杂度，但其对低秩假设的强依赖在复杂纹理场景下的鲁棒性存疑。

## 研究背景

CASSI系统通过编码孔径调制与色散元件将三维高光谱立方体压缩为二维测量，其前向模型可表述为 $\mathbf{y} = \Phi \mathbf{x} + \mathbf{n}$。由于感知矩阵 $\Phi$ 的秩远小于未知向量 $\mathbf{x}$ 的维度，该逆问题具有无数解，必须引入先验约束解空间。高光谱数据固有的跨波段低秩结构——即光谱曲线可由少数基向量线性组合表示——成为正则化重建的核心先验，但传统方法仅将其作为辅助约束，未改变全维求解的本质。

主流深度展开网络（DUNs）如GAP-Net、RDLUF均基于全维高光谱成像模型，交替执行数据保真与先验正则步骤。这种范式存在根本缺陷：巨大的维度差距迫使求解器在每一展开阶段从有限测量中推断 $H \times W \times B$ 个未知数，导致严重的病态性；同时直接处理高维数据立方体带来沉重的计算负担，限制了网络效率与可扩展性。尽管部分工作尝试将低秩先验融入DUNs，如TLPLN集成张量CP分解，但仍在全维空间处理，未能紧密耦合先验与感知物理。本文的切入点在于显式重构感知模型本身，通过低秩分解将高维重建转化为低维分量估计，从根本上缓解病态性并降低计算开销。

## 核心方法

### 方法参照系

本文问题属于CASSI压缩光谱重建，标准流程为基于全维高光谱模型的深度展开网络，交替优化数据保真项与可学习先验模块。本文的关键差异在于不直接恢复全维高光谱立方体，而是将低秩分解嵌入前向模型，将优化变量从全维 $\mathbf{x}$ 替换为低维谱基 $\mathbf{E}$ 与子空间图像 $\mathbf{A}$。

### 低维成像模型重构

传统DUNs在全维空间迭代，导致病态性严重。本文通过显式集成低秩分解与CASSI感知模型，推导出两个新型成像模型。设高光谱图像 $\mathcal{X} \in \mathbb{R}^{H \times W \times B}$ 可分解为 $\mathcal{X} = \mathbf{A} \times_3 \mathbf{E}^T$，其中 $\mathbf{E} \in \mathbb{R}^{B \times k}$ 为谱基，$\mathbf{A} \in \mathbb{R}^{H \times W \times k}$ 为子空间图像，物理秩 $k \ll B$。利用向量化性质 $\text{vec}(\mathbf{UVW}) = (\mathbf{W}^T \otimes \mathbf{U})\text{vec}(\mathbf{V})$，原模型 $\mathbf{y} = \Phi \mathbf{x}$ 被重构为两个低维子问题：

$$
\mathbf{y} = \Phi_E \mathbf{e} + \mathbf{n}, \quad \mathbf{y} = \Phi_A \mathbf{a} + \mathbf{n}
$$

其中 $\mathbf{e} = \text{vec}(\mathbf{E}^T)$，$\mathbf{a} = \text{vec}(\mathbf{A})$，$\Phi_E = \Phi (\mathbf{E} \otimes \mathbf{I}_{HW})$，$\Phi_A = \Phi (\mathbf{I}_B \otimes \mathbf{A})$。这一重构将未知量从 $H \times W \times B$ 降至 $B \times k + H \times W \times k$，显著缓解病态性。设计动机在于解决全维DUNs中维度灾难导致的每阶段严重病态性，通过低维分量估计实现高效重建。

### 广义特征展开机制（GFUM）

低维模型重构后，直接展开优化算法会导致物理秩 $k$ 与ProxyNet特征维度耦合，限制表征能力。本文引入GFUM，将 $k$ 维优化变量提升至 $C$ 维特征表示（$C \geq k$），其中 $k$ 维物理分量执行数据保真，$(C-k)$ 维辅助分量作为信息载体保留在数据保真项中，协助ProxyNet细化物理分量。E-problem的GFUM更新为：

$$
\mathbf{E}_{i+1}^{\text{feat}} = \mathbf{E}_{i+1/2}^{\text{feat}} + \text{ProxyNet}_E(\mathbf{E}_{i+1/2}^{\text{feat}})
$$

其中 $\mathbf{E}_{i+1/2}^{\text{feat}}$ 包含物理分量与辅助分量。设计动机在于解耦物理秩与网络特征维度，使ProxyNet能在更高维空间学习复杂空间-光谱依赖，提升表征容量与适应性。

## 实验评估

实验在10个模拟场景上进行，基线覆盖模型驱动（TwIST、GAP-TV、DeSCI）、端到端（λ-Net、TSA-Net）、PnP（DIP-HSI）及DUNs（GAP-Net、RDLUF、MiJUN等）四类方法。缺失最新Mamba类基线的直接对比，但MiJUN已列入DUNs组。

| 方法 | 参数量 (M) | FLOPs (G) | 平均 PSNR (dB) | 平均 SSIM |
| :--- | :--- | :--- | :--- | :--- |
| RDLUF-9stg | 1.81 | 115.34 | 39.57 | 0.974 |
| MiJUN-9stg | 0.56 | 73.67 | 40.86 | 0.982 |
| LRDUN-9stg | 2.04 | 30.58 | 40.96 | 0.982 |

LRDUN-9stg以30.58 G FLOPs取得40.96 dB平均PSNR，较RDLUF降低73%计算量，PSNR提升1.39 dB；与MiJUN相比，PSNR略高0.10 dB，FLOPs降低58%。

消融实验验证低秩嵌入策略与GFUM有效性。低秩嵌入策略对比显示，LRDUN较基线（全维处理）PSNR提升1.28 dB，FLOPs降低61.9%。GFUM中，特征维度 $C$ 从11增至16时PSNR持续上升，但FLOPs增加，故默认 $C=16$。物理秩 $k$ 在11时达到性能饱和，过小导致光谱多样性建模不足，过大则削弱辅助分量维度。

评估边界方面，实验仅基于模拟数据，未报告真实CASSI数据的定量指标，仅通过定性图展示泛化性。指标仅包含PSNR/SSIM，缺乏FID等感知质量指标。代码未公开，超参数（$k=11, C=16$）固定，未提供不同场景下的自适应机制。

## 关联研究分析

从方法设计看，LRDUN与RDLUF同属PGD展开框架，但RDLUF在全维高光谱空间迭代，而LRDUN在低维谱基与子空间图像空间交替优化。这一差异源于对病态性根源的不同认知：RDLUF认为通过参数共享与高效注意力可缓解全维计算负担，而LRDUN认为维度差距本身是病态性的主因，必须从模型层面降维。这种范式转移使得LRDUN在FLOPs上显著占优，但可能牺牲全维空间的全局非线性建模能力，论文未提供复杂纹理场景下的定量对比来验证这一权衡。

从问题动机看，LRDUN与MiJUN均追求效率-精度平衡，但路径不同：MiJUN引入Mamba状态空间模型降低长程依赖计算复杂度，而LRDUN通过低秩重构降低问题维度。MiJUN的改进在于骨干网络效率，LRDUN的改进在于问题结构简化。两者代表了DUNs效率优化的两条路径：前者优化算法复杂度，后者优化问题规模。LRDUN的低秩假设对非低秩场景（如高纹理、多材料混合）的鲁棒性，论文未通过消融实验或跨域测试给出明确回答。

## 总结

LRDUN要解决的核心矛盾是CASSI重建中病态逆问题与高维计算开销的耦合。现有全维DUNs无法同时缓解这两者，因为维度差距既是病态性的根源也是算力冗余的来源。本文抓住低秩分解可重构前向模型这一被忽略的点，将优化变量从全维立方体替换为低维谱基与子空间图像，通过交替PGD展开实现高效重建。实验证明LRDUN-9stg在模拟基准上取得40.96 dB PSNR与30.58 G FLOPs，较SOTA DUNs实现显著效率提升。其边界在于低秩假设的刚性：当场景光谱多样性超出物理秩 $k$ 的表达能力时，辅助分量的补偿能力有限，且模拟与真实数据间的域差距未被定量评估。当物理秩 $k$ 固定为11时，面对光谱复杂度远超该秩的场景，辅助分量能否有效补偿低秩近似带来的信息损失，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.18513)