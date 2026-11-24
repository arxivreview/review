# ICLR2026最新论文 ｜TOWARDS ALL-ATOM FOUNDATION MODELS FOR BIOMOLECULAR BINDING AFFINITY PREDICTION ｜原子级扩散Transformer（ADiT）：面向生物分子结合亲和力预测的统一基础模型

研究机构：北京大学、加拿大蒙特利尔大学

作者：Liang Shi、Zuobai Zhang、Huiyu Cai 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_71531849)

> 生物分子结合亲和力预测旨在量化蛋白与配体、抗体与抗原等复合物的结合强度，但高质量实验标签稀缺且现有方法多针对单一交互类型，缺乏跨任务泛化能力。本文切入点在于将AlphaFold 3的生成式结构预测架构改造为判别式表征学习器，通过移除多序列比对（MSA）依赖并采用去噪预训练，构建统一处理多种生物分子交互的基础模型。ADiT采用非等变Transformer处理全原子结构，在蛋白-配体、药物-靶点等四类任务上达到SOTA或竞争性性能。其价值在于验证了结构预训练对缓解标签稀缺的有效性，但非等变设计在复杂构象下的鲁棒性及与专用几何模型的精度差距仍存疑。

## 研究背景

结合亲和力预测的核心困境在于实验数据稀缺与结构信息利用不足。早期序列基方法如DeepDTA（Öztürk et al., 2018）仅依赖一维序列特征，忽略了决定结合机制的全原子空间互补性；而后续结构基方法虽引入3D信息，但多针对特定交互类型（如RDE-Network专注蛋白-蛋白，ProFSA专注蛋白-配体），无法跨任务迁移。这种任务特异性限制了模型在新型靶点或化合物上的泛化能力，且未能充分利用AlphaFold 3等结构预测模型的突破。

领域主流路线在精度与通量间存在权衡：几何图判别式方法（如DeepGGL）在单一任务精度上占优，但依赖高质量3D结构且计算复杂度高；对比学习检索方法（如S2Drug）速度快但精度粗粒度。本文的切入点在于，当模型目标从“预测几何”转向“编码观测几何”时，AlphaFold 3中沉重的条件化模块（trunk）变得冗余，其Transformer架构反而成为联合编码序列与结构信息的通用框架。通过大规模结构去噪预训练，ADiT旨在以统一表征缓解亲和力标签稀缺问题，实现跨交互类型的泛化。

## 核心方法

### 方法参照系

ADiT属于结构基亲和力预测中的基础模型路线，其参照系为AlphaFold 3的生成式架构。关键差异在于：AlphaFold 3旨在从序列生成结构，依赖MSA和模板进行条件化；而ADiT旨在从观测结构提取表征，移除MSA/模板依赖，改用ESM-2序列特征和RDKit分子特征，并将生成目标替换为去噪表征学习。

### 统一Token化与特征初始化

**设计动机**：解决现有方法中蛋白与配体表征不一致、难以联合编码的问题。ADiT采用统一Token化方案，将蛋白残基和小分子重原子均编码为单一Token。Token级特征由ESM-2-650M嵌入（仅蛋白残基）和Token类型嵌入组成，配体Token的ESM特征置零。原子级特征分为条件表示 $c_{atom}$（含原子类型、名称及Token条件）和单原子表示 $s_{atom}$（含坐标）。原子对表示 $z_{atom}$ 通过RBF核嵌入欧氏距离，并整合Token对表示以捕获全局交互。

$$
z_{atom} = \text{Embed}(c_{atom}^i, c_{atom}^j) \oplus \text{RBF}(\|x_i - x_j\|) \oplus \mathbb{1}_{\text{same token}} \oplus z_{token}
$$

该公式表明，原子间交互不仅依赖局部几何距离，还通过Token对表示继承全局序列语义，实现了局部原子细节与全局生物化学信息的融合。

### 非等变分层表征学习

**设计动机**：克服等变GNN在捕获非几何特征（如静电、化学语义）时的局限性，同时降低计算复杂度。ADiT主干采用分层DiT模块：先通过 $N_{atom}$ 层原子注意力编码器更新原子表示，经“Atom2Token”平均池化生成Token表示，再通过 $N_{token}$ 层全局Token注意力精炼，最后经“Token2Atom”广播操作和另一组原子DiT层更新原子表示。多注意力头定义为：

$$
\text{Attn}_h(Q, K, V) = \text{Softmax}\left(\frac{Q_h K_h^T}{\sqrt{d}} + \beta_{ij}\right) V_h
$$

其中 $\beta_{ij}$ 控制交互范围：Token级 $\beta_{ij}=0$（全局注意力），原子级采用稀疏注意力（每组32原子关注邻近128原子）。ADiT摒弃SE(3)等变偏置，仅通过质心居中和随机旋转增强近似不变性，以换取架构简洁性和对非几何特征的捕捉能力。

## 实验评估

ADiT在PDBbind（SI 30%/60%）、SKEMPIv2、抗体数据集等基准上评估，基线覆盖DeepDTA、ProFSA、RDE-Network等，但缺失DeepGGL、RicciBind等最新几何图SOTA方法。

| 模型 | PDBbind SI 30% Pearson | PDBbind SI 60% Pearson | SKEMPIv2 Pearson |
|---|---|---|---|
| ProFSA | 0.743 | 0.743 | - |
| ADiT-S | 0.626 | 0.740 | 0.660 |
| ADiT-M | 0.622 | 0.764 | 0.683 |
| ADiT-L | 0.645 | 0.797 | 0.691 |

ADiT-L在PDBbind SI 60%上Pearson 0.797，优于ProFSA的0.743，但在SI 30%上（0.645）低于ProFSA（0.743），表明其在高序列同源性数据上泛化能力更强。

| 消融项 | Pearson | Spearman | RMSE | MAE |
|---|---|---|---|---|
| ADiT-M (Baseline) | 0.683 | 0.539 | 1.559 | 1.098 |
| w/o pre-training | 0.649 | 0.511 | 1.624 | 1.169 |
| w/o all-atom info. | 0.658 | 0.517 | 1.606 | 1.153 |
| w/ larger size (ADiT-L) | 0.691 | 0.560 | 1.540 | 1.088 |

消融显示，移除预训练导致Pearson下降5.2%，移除全原子信息下降3.8%，证实结构预训练和原子级建模是关键。模型规模从S到L，Pearson从0.660升至0.691，呈现清晰缩放效应。

评估边界方面，论文未报告计算效率（FLOPs/延迟），且PDBbind SI划分与领域综述中整体PDBbind协议不同，导致与DeepGGL（0.848 PCC）不可直接比较。代码已开源，但预训练超参数（如噪声尺度 $\sigma=0.5\text{Å}$）的敏感性分析缺失。

## 关联研究分析

从方法设计看，ADiT与DeepGGL的核心差异在于几何偏置的处理。DeepGGL采用多尺度几何图卷积，显式建模原子间空间距离和非共价相互作用，依赖强几何先验；而ADiT采用非等变Transformer，通过随机旋转增强近似不变性，更侧重捕获ESM-2和RDKit提供的化学语义。这种差异源于任务目标：DeepGGL追求单一任务精度上限，ADiT追求跨任务泛化。ADiT在PDBbind SI 30%上低于ProFSA，可能暗示非等变设计在低同源性、高构象多样性数据上，缺乏等变约束导致几何特征提取不够鲁棒。

从问题动机看，ADiT与S2Drug同属基础模型范式，但S2Drug聚焦虚拟筛选的序列-结构对比学习，而ADiT聚焦亲和力回归的结构去噪预训练。S2Drug在LIT-PCBA上AUROC 92.46，侧重排序能力；ADiT在SKEMPIv2上Pearson 0.691，侧重绝对值预测。ADiT移除MSA依赖改用ESM-2，可能损失部分进化信息，但避免了MSA计算开销，更适合大规模筛选场景。这种取舍使得ADiT在抗体-抗原任务上（Pearson 0.567）优于专用模型GearBind（0.515），但在蛋白-配体任务上未超越专用几何模型，反映基础模型在精度与泛化间的平衡点尚未完全找到。

## 总结

ADiT要解决的核心矛盾是生物分子结合亲和力预测中数据稀缺与任务特异性导致的泛化不足。其切入点在于利用AlphaFold 3架构的Transformer模块，通过移除MSA依赖和去噪预训练，将生成式模型改造为统一表征学习器。ADiT采用非等变分层DiT处理全原子结构，在四类交互任务上达到SOTA或竞争性性能，其中ADiT-L在PDBbind SI 60%上Pearson 0.797，在抗体任务上Pearson 0.567。其边界在于，非等变设计在低序列同源性数据上精度低于专用几何模型，且未量化计算效率。当蛋白构象高度柔性时，非等变Transformer通过随机旋转增强近似的不变性是否足以捕获诱导契合效应，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_71531849)