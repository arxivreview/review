# ICLR2026最新论文 ｜TETRAGT: TETRAHEDRAL GEOMETRY-DRIVEN EXPLICIT TOKEN INTERACTIONS WITH GRAPH TRANSFORMER FOR MOLECULAR REPRESENTATION LEARNING ｜四面体几何驱动显式Token交互图Transformer

研究机构：中国人民大学

作者：Jinjia Feng、Zhewei Wei、Taifeng Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_49321847)

> 分子性质预测长期受制于3D几何参数隐式编码导致的误差累积与手性歧义，现有图Transformer仅通过原子与键的间接组合推导键角和二面角，无法捕捉高阶几何结构的物理依赖关系。TetraGT将键角与二面角直接建模为一等公民Token，通过空间四面体注意力机制强制满足几何约束，实现了从零预测3D构象并提升量子化学性质精度。该架构在PCQM4Mv2和OC20 IS2RE上刷新了SOTA，但其对大规模分子的计算复杂度及构象噪声鲁棒性边界仍需进一步验证。

## 研究背景

分子构象稳定性由键角与二面角共同决定，这些几何参数直接控制酶催化活性与药物生物活性。然而，传统分子图神经网络（GNN）仅将原子作为节点、化学键作为边，通过消息传递机制聚合局部拓扑特征，这种2D表征无法捕捉空间构效关系。当引入3D坐标时，现有方法如SchNet和Equiformer虽能处理距离信息，但键角与二面角仍作为原子坐标的衍生量隐式存在，导致几何偏差在间接表征中传播并累积。

当前3D分子表征学习的主流路线依赖原子/边Token的全局注意力机制，如TGT和Uni-Mol+引入三角不等式约束以增强几何一致性，但仍未解决三个核心瓶颈：局部手性歧义（不同手性分子可能产生相同距离矩阵）、高阶几何结构隐式建模（四/五原子交互仅通过组合操作间接编码）、以及几何参数间结构依赖关系的缺失。TetraGT的切入点在于打破“坐标即输入”的范式，将几何参数本身作为结构化Token，通过显式建模其物理约束关系，从源头消除误差累积并实现手性区分。

## 核心方法

### 方法参照系

TetraGT基于图Transformer（GT）架构，继承TGT的三角不等式约束思想，但关键差异在于将建模对象从边级几何扩展至角级几何。标准GT流程中，原子和边Token通过全局注意力交互，键角和二面角仅作为位置编码或辅助特征存在；TetraGT则将其提升为独立Token，并设计专用注意力机制处理高阶结构交互。

### 空间四面体注意力机制

该机制解决了高阶几何结构隐式建模导致的误差累积问题。在标准GT中，四原子交互需通过多次原子/边Token组合间接实现，偏差随组合深度累积。TetraGT基于四面体几何理论，对共享顶点的相邻键角和共享面的相邻二面角进行直接注意力交互。对于中心键角 $(i,j,k)$，其与顶点 $k$ 处相邻键角 $(l,k,j)$ 的交互计算为：

$$
\mathbf{v}_{lkj}^{f} = \text{softmax}\left(\frac{\mathbf{q}_{ijk}^{f} (\mathbf{p}_{lkj}^{f})^T}{\sqrt{d_h}} + \mathbf{b}_{lkj}^{f} + \mathbf{g}_{lkj}^{f}\right) \mathbf{v}_{lkj}^{f}
$$

其中偏置项 $\mathbf{b}^{f}$ 和门控项 $\mathbf{g}^{f}$ 嵌入Lemma 1(a)的面角约束，确保交互满足物理有效性。局部采样策略将复杂度从 $O(N^3)$ 降至 $O(wN^2)$，在保持几何一致性的同时实现高效计算。

### 定向环角度损失与层级虚拟节点

定向环角度损失（DCA Loss）解决了局部手性歧义问题。传统角度预测限制在 $[0, \pi]$ 范围，无法区分手性变化（$\sigma$ 与 $2\pi - \sigma$）。TetraGT将角度范围扩展至 $(0, 2\pi)$，采用定向循环分箱损失：

$$
\mathcal{L}_{DCA} = -\sum_{i} \log p(y_i | \hat{y}_i)
$$

其中分箱边界考虑周期性，避免 $359^\circ$ 与 $1^\circ$ 的过度惩罚。层级虚拟节点架构则缓解信息瓶颈，为原子、边、键角、二面角各设专用虚拟节点，通过FFN、三元组交互、四面体交互分别聚合，最终分子级虚拟节点连接四者输出预测结果，实现多尺度结构信息的无损传递。

## 实验评估

实验在PCQM4Mv2、OC20 IS2RE、QM9、PDBBind、Peptides和LIT-PCBA六个基准上评估，基线覆盖SchNet、Equiformer、TGT、Uni-Mol+等3D几何模型，但缺失LLM类基线（如MPPReasoner）和最新等变网络（如Geoformer）。主实验结果显示，TetraGT在PCQM4Mv2 valid集上MAE为65.9 meV，优于TGT的67.1 meV和Uni-Mol+的69.3 meV；在OC20 IS2RE上平均能量MAE为397.7 meV，低于TGT的403.0 meV和Uni-Mol+的408.8 meV。

| 数据集 | 指标 | TetraGT | TGT | Uni-Mol+ |
| :--- | :--- | :--- | :--- | :--- |
| PCQM4Mv2 | MAE (meV) | 65.9 | 67.1 | 69.3 |
| OC20 IS2RE | Avg. MAE (meV) | 397.7 | 403.0 | 408.8 |
| QM9 | $\epsilon_H$ (meV) | 8.5 | 15.6 | 20.3 |
| LIT-PCBA | ROC-AUC (%) | 82.4 | 81.5 | 77.2 |

消融实验表明，四面体交互模块贡献最大，移除后PCQM4Mv2 MAE从68.8 meV升至73.6 meV；DCA Loss和层级虚拟节点分别带来0.6 meV和0.4 meV的改进。距离损失与角度损失比例为4:1时性能最优，8:1时性能下降至70.1 meV，表明角度预测对整体性能有显著正向贡献。

评估边界方面，论文未报告置信区间，QM9数值单位为meV而非eV，与领域综述中3D-GSRD的0.0583 eV（58.3 meV）不可直接比较。代码已开源，但预训练成本（33 A100 GPU days）仅为Uni-Mol+的1/3，未提供超参数敏感性分析。

## 关联研究分析

从问题动机看，TetraGT与TGT共享几何约束增强3D表征的目标，但TGT仅建模边级三角不等式，TetraGT扩展至角级四面体约束。这一差异源于对“几何参数依赖关系”的不同理解：TGT假设边长决定构象，TetraGT认为键角与二面角的相互约束才是构象稳定性的根本。TGT在OC20 IS2RE上MAE为403.0 meV，TetraGT的397.7 meV改进验证了角级约束的必要性，但两者在QM9上的差距（15.6 vs 8.5 meV）是否完全归因于手性区分，论文未提供消融证据。

从方法设计看，TetraGT与Equiformer同属等变/几何约束路线，但Equiformer通过旋转等变操作隐式保持几何一致性，TetraGT通过显式Token交互强制满足约束。Equiformer在OC20 IS2RE上MAE为465.7 meV，显著高于TetraGT，表明显式建模高阶几何结构比隐式等变操作更有效。然而，TetraGT的局部采样策略（$w$ 近邻）可能丢失长程几何依赖，而Equiformer的全局等变注意力理论上能捕捉任意距离的相互作用，这一权衡在论文中未量化。

## 总结

TetraGT解决的核心矛盾是3D几何参数隐式编码导致的误差累积与手性歧义。其切入点在于将键角与二面角提升为一等公民Token，通过空间四面体注意力机制显式建模其物理约束关系，这是现有方法未做到的。方法上，TetraGT引入定向环角度损失和层级虚拟节点，实现了从零预测3D构象并提升性质预测精度。实验证明，其在PCQM4Mv2上MAE为65.9 meV，OC20 IS2RE上平均MAE为397.7 meV，均优于TGT和Uni-Mol+。边界在于，局部采样策略可能丢失长程几何依赖，且未验证在超大规模分子（>1000原子）上的可扩展性。当分子尺寸增大时，$O(wN^2)$ 复杂度的实际开销是否仍具优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_49321847)