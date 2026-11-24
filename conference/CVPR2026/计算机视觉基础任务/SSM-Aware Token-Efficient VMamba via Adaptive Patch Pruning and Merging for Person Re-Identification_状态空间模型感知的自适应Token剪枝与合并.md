# CVPR2026最新论文 ｜SSM-Aware Token-Efficient VMamba via Adaptive Patch Pruning and Merging for Person Re-Identification ｜状态空间模型感知的自适应Token剪枝与合并

作者：Huiyuan Huang、Sang Min Yoon

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_701d84b24c52)

> 行人重识别（Person Re-Identification, ReID）在追求高精度特征判别的同时，必须满足边缘设备实时部署的计算效率约束。现有视觉状态空间模型（Visual State Space Model, VSSM）虽具备线性复杂度，但其密集Token处理机制导致实际推理时GPU利用率低下，且直接迁移Transformer的Token剪枝策略会破坏SSM的递归扫描动态。本文提出TE-VMamba，通过提取SS2D状态更新幅度作为Token重要性指标，结合输入自适应阈值实现浅层剪枝与深层合并。该方法在Market-1501上将FLOPs降低超60%并保持SOTA精度，但其对严重遮挡场景下身份线索稀疏性的鲁棒性仍存疑。

## 研究背景

当ReID模型部署于资源受限的边缘设备时，高分辨率输入与批量大小为1的推理场景下，计算延迟与内存占用成为硬约束。视觉状态空间模型（VSSM）通过选择性扫描（Selective Scan）实现线性时间复杂度，理论上优于Transformer的二次复杂度，但其核心机制SS2D（2D-Selective-Scan）仍需在密集的$H \times W$ Token网格上执行顺序状态更新，且交替的水平-垂直扫描引入了显著的数据移动开销，导致实际GPU利用率受限。

ReID领域的主流骨干已从CNN演进至Transformer，近期VSSM（如VMamba）因线性复杂度优势受到关注。然而，现有Token效率优化方法（如DynamicViT、ToMe）均基于全局注意力机制设计，直接应用于SSM时忽略了其方向性与递归特性，可能破坏扫描路径上的身份承载结构。本文切入点在于：SSM的状态更新步长$\Delta_k$本身即为Token参与递归动态强度的量化指标，这一内在信号可被直接用于定义与SSM动力学对齐的Token重要性，从而在不依赖外部启发式规则的前提下实现输入自适应的Token稀疏化。

## 核心方法

### 方法参照系

标准VMamba将图像划分为固定数量的Patch，通过四阶段VSS Block处理，每个SS2D Block对全量Token执行双向扫描。本文问题与该通用流程的关键差异在于：固定Token数导致大量背景或低显著性区域参与递归计算，而身份线索在ReID中本质上是稀疏的，需动态调整Token数量以匹配输入复杂度。

### SS2D状态更新引导的自适应剪枝

剪枝模块位于每个SS2D Block之后，替代了传统基于注意力分数的Token选择。设计动机在于解决ViT剪枝方法在SSM中因忽略递归动态而导致的身份结构破坏问题。Token重要性由状态更新步长$\Delta_k$的绝对值定义，其计算遵循：

$$ \Delta_k = \text{Softplus}(W_\Delta x_k + U_\Delta h_{k-1}) $$

该公式表明$\Delta_k$由当前输入$x_k$与前一隐状态$h_{k-1}$共同决定，直接控制$x_k$对状态更新的贡献幅度。$|\Delta_k|$接近零意味着该Token在递归动态中参与度极低。基于此，计算层内自适应阈值：

$$ \theta = \mu - \alpha\sigma $$

其中$\mu, \sigma$为$|\Delta_k|$的批次统计量，$\alpha$为剪枝激进度。满足$|\Delta_k| < \theta$的Token被移除。这一机制将剪枝转化为模型内在操作，仅移除递归不活跃Token，在去除冗余的同时保持扫描稳定性，避免了外部阈值设定的数据分布依赖。

### 语义相似性驱动的自适应Token合并

合并模块紧随剪枝之后，处理剪枝后仍存在的语义冗余（如均匀背景或衣物纹理）。设计动机在于解决单纯剪枝导致的局部细节丢失问题，通过整合相似Token提升表示紧凑性。对固定偶-奇Token对$(a_k, b_k)$，计算归一化点积相似度：

$$ s_k = \frac{a_k^\top b_k}{\|a_k\|_2 \|b_k\|_2} $$

自适应阈值$\theta_m$由轻量级两层MLP门控头预测，输入为全局特征统计量，输出经Sigmoid激活。当$s_k > \theta_m$时，执行均值融合$z_k = a_k + b_k$。该机制在浅层保守合并以保留局部细节，深层激进合并以整合语义一致区域。MLP门控替代了手动调参常数，实现实例感知的Token压缩，在不破坏空间连贯性的前提下，与剪枝协同实现超60%的FLOPs降低。

## 实验评估

实验在Market-1501、CUHK03-NP、MSMT17及Occluded-ReID上进行，基线覆盖CNN（OSNet、HAT）、Transformer（TransReID、DC-Former）及Mamba类方法。对比方法缺失跨模态及域泛化基线，但单模态RGB ReID主流路线覆盖完整。

| 方法 | Market-1501 Rank-1 | Market-1501 mAP | CUHK03-NP (Labeled) Rank-1 | CUHK03-NP (Labeled) mAP | MSMT17 Rank-1 | MSMT17 mAP |
|---|---|---|---|---|---|---|
| TransReID (no RK) | 95.2 | 88.9 | 81.7 | 79.6 | 79.6 | 77.0 |
| DC-Former | 96.0 | 90.6 | 84.4 | 83.3 | 79.6 | 77.5 |
| TE-VMamba-Base | 96.7 | 87.1 | 97.3 | 94.0 | 83.3 | 62.7 |

TE-VMamba-Base在Market-1501与CUHK03-NP上超越Transformer基线，但在MSMT17上mAP（62.7%）低于DC-Former（77.5%），表明其在大规模数据集上的泛化能力存在波动。

| 配置 | Rank-1 | mAP | FLOPs (G) |
|---|---|---|---|
| VMamba-Base (无剪枝/合并) | 98.2 | 91.6 | 15.46 |
| 仅剪枝 | 96.7 | 87.2 | 3.83 |
| 仅合并 | 98.5 | 92.1 | 15.46 |
| 剪枝+合并 | 96.7 | 87.1 | 3.82 |

消融显示，仅合并可提升精度（+0.3 Rank-1）但不降低FLOPs；仅剪枝大幅降低FLOPs但损失精度（-1.5 Rank-1）；剪枝+合并实现精度-效率最优权衡。Prune→Merge顺序优于Merge→Prune（后者FLOPs为7.69G），因先剪枝可避免冗余Token在合并前改变特征分布。

评估协议采用单查询设置，报告Rank-1与mAP。代码开源，超参数（如$\alpha=0.7$、$\lambda=1.0$）公开，实验在单张NVIDIA RTX 5080 GPU上完成。局限在于未报告置信区间，且Occluded-ReID上Rank-1（95.5%）虽高，但未与专门针对遮挡的局部特征方法进行细粒度对比。

## 关联研究分析

从方法设计看，TE-VMamba与ToMe（Token Merging）均采用Token合并策略，但ToMe基于注意力权重计算相似度，而本文基于点积并引入SSM状态更新引导的剪枝。差异根源在于任务特性：ToMe面向通用视觉任务，注意力权重反映全局依赖；ReID中身份线索稀疏且局部，SSM的$\Delta_k$更直接反映Token对递归动态的贡献，因此基于$\Delta_k$的剪枝比基于注意力的选择更契合SSM动力学。

从问题动机看，TE-VMamba与DynamicViT均解决Token冗余问题，但DynamicViT通过可学习门控动态选择Token，适用于Transformer的全局注意力架构；本文针对SSM的递归扫描特性，将剪枝与合并解耦并强制Prune→Merge顺序。差异根源在于架构约束：Transformer中Token间交互是并行的，剪枝与合并可独立进行；SSM中Token间交互是顺序的，合并前必须剪枝以维持递归关系$h_t = \bar{A}h_{t-1} + \bar{B}x_t$的稳定性，否则冗余Token会污染后续状态更新。

## 总结

TE-VMamba解决的核心矛盾是VSSM线性复杂度理论与实际推理效率之间的落差，其切入点在于利用SSM内在的状态更新步长$\Delta_k$作为Token重要性指标，避免了外部启发式规则对递归动态的干扰。该方法通过浅层剪枝去除低显著性Token、深层合并整合语义冗余，在Market-1501上实现96.7% Rank-1与3.82G FLOPs的权衡。其边界在于MSMT17上mAP显著低于Transformer基线，且Occluded-ReID实验未充分验证在严重遮挡导致身份线索极度稀疏时，基于$\Delta_k$的剪枝是否会误删关键局部特征。当遮挡比例超过50%时，$\Delta_k$分布是否仍能可靠区分身份线索与背景噪声，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_701d84b24c52)