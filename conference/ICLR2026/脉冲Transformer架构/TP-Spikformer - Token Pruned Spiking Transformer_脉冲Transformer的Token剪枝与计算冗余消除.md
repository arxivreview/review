# ICLR2026最新论文 ｜TP-Spikformer: Token Pruned Spiking Transformer ｜脉冲Transformer的Token剪枝与计算冗余消除

研究机构：电子科技大学、香港中文大学

作者：Wenjie Wei、Xiaolong Zhou、Malu Zhang 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.00527)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.00527)

> 脉冲Transformer（Spiking Transformer）在提升精度的同时引入了高参数量与密集计算，导致边缘部署困难。现有剪枝方法多依赖重训练或结构修改，缺乏通用性。本文提出无需重训练的时空信息保留准则与块级早停架构，在保持精度的同时大幅降低计算量。该方法在多种骨干网络上验证了效率优势，但其零微调策略在动态任务上的潜力存疑。

## 研究背景

脉冲Transformer利用脉冲神经网络（SNN）的事件驱动特性替代浮点运算，但大规模模型如SDT-V3拥有173M参数，推理时每秒执行28.4B次突触操作，内存占用1384MB，严重制约边缘设备部署。Token剪枝通过动态减少每个块处理的Token数量来降低存储与计算开销，其核心假设是视觉任务的最终预测仅依赖部分Token。然而，现有SNN剪枝方法存在两大局限：一是修改原始结构（如引入额外Token或可训练模块），二是需要重训练，导致应用成本高且泛化性差。

该领域正从“功能等价”向“原生高效设计”演进，但Token剪枝在SNN中的时空特性利用不足。STATA（Zhuge et al., 2024）虽在ImageNet上验证了剪枝效果，但需完整重训练并引入Anchor Token；SparseSpikformer（Liu et al., 2024）仅基于发放率剪枝，未利用时间动态。本文切入点在于设计一种无需重训练、不修改结构的剪枝方法，通过启发式准则评估Token的时空信息量，实现高效压缩。

## 核心方法

### 方法参照系

本文问题属于SNN模型压缩中的Token剪枝分支。标准流程为：评估Token重要性→选择保留/剪枝→调整网络结构。本文关键差异在于：不修改网络结构，不引入额外参数，且无需重训练，通过前向传播中的动态评分与早停实现压缩。

### 时空信息保留准则（IRToP）

**设计动机**：现有方法仅基于空间发放率或静态特征，忽略了SNN的时间动态特性，导致在动态任务中剪枝精度下降。IRToP通过结合空间显著性与时间变化率，全面评估Token的信息量。

空间评分器计算Token与局部窗口均值的差异，反映空间显著性：

$$ S_{t,h,w}^{(\ell)} = \frac{1}{D} \sum_{d=1}^{D} |X_{t,h,w,d}^{(\ell)} - Y_{t,h,w,d}^{(\ell)}| $$

其中 $Y$ 为 $k \times k$ 窗口内的均值表示。时间评分器计算相邻时间步的特征变化：

$$ T_{t,h,w}^{(\ell)} = \frac{1}{D} \sum_{d=1}^{D} |X_{t,h,w,d}^{(\ell)} - X_{t-1,h,w,d}^{(\ell)}| $$

最终评分为归一化后的空间与时间分数之和，高分Token被保留。该准则将生物视觉系统的选择性注意机制映射到SNN，使剪枝决策同时考虑空间与时间维度。

### 信息保留剪枝架构（IR-Arc）

**设计动机**：直接丢弃Token会改变特征图尺寸，破坏层级结构（如QKFormer的特征金字塔），且丢失未剪枝Token的原始信息。IR-Arc采用块级早停策略，未剪枝Token跳过SSA和MLP计算，但保留其原始特征值，最后重组恢复特征图尺寸。

前向传播中，信息丰富Token $\mathbf{I}$ 执行完整SSA和MLP，信息贫乏Token $\mathbf{U}$ 直接传递：

$$ \mathbf{X}_{t,\text{inf}}^{(\ell)} = \text{MLP}(\text{SSA}(\mathbf{I}_{t}^{(\ell)}) + \mathbf{I}_{t}^{(\ell)}) + \mathbf{I}_{t}^{(\ell)} $$

$$ \mathbf{X}_{t,\text{uni}}^{(\ell)} = \mathbf{U}_{t}^{(\ell)} $$

重组后 $\mathbf{X}_{t}^{(\ell)} = \text{Reassemble}(\mathbf{X}_{t,\text{inf}}^{(\ell)}, \mathbf{X}_{t,\text{uni}}^{(\ell)})$。该架构避免了结构修改，兼容特征金字塔网络，且通过跳过计算而非丢弃数据，保留了更多信息。

## 实验评估

实验在ImageNet-1K、CIFAR-10/100、COCO、ADE20K等基准上进行，对比Spikformer、SDT-V1/V3、QKFormer等骨干。基线覆盖STATA、SparseSpikformer等剪枝方法，但缺失CSDformer、SAGE等2025-2026年最新SOTA对比。

| 方法 | 架构 | $N_{avg}$ | OPs_block (G) | Power (mJ) | Acc. (%) | Thr (imgs/s) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SDT-V1-8-768 | Base | ×1 | 9.04 | 10.26 | 76.32 | 156 |
| TP-Spikformer | SDT-V1-8-768 | ×0.51 | 4.71 (↓48%) | 6.36 (↓38%) | 74.79 (-1.53) | 202 (↑29%) |
| QK-10-768 | Base | ×1 | 15.08 | 32.12 | 85.56 | 75 |
| TP-Spikformer | QK-10-768 | ×0.53 | 7.97 (↓47%) | 25.71 (↓20%) | 82.53 (-3.03) | 106 (↑41%) |

在SDT-V1上，保留51% Token时，OPs降低48%，功耗降低38%，精度仅降1.53%。QKFormer上保留53% Token，OPs降低47%，精度降3.03%。

| 架构 | Random, Drop | Random, IR-Arc | Spatial, IR-Arc | Temporal, IR-Arc | IRToP, IR-Arc |
| :--- | :--- | :--- | :--- | :--- | :--- |
| SDT-V1 ×0.52 | 59.88% | 60.02% | 73.52% | 70.95% | 73.78% |
| QKFormer ×0.65 | Fail | 74.45% | 58.93% | 79.69% | 81.16% |

消融显示，IRToP优于随机剪枝，空间评分在SDT-V1上更有效，时间评分在QKFormer上更重要。IR-Arc比Drop更支持变尺寸特征图。

评估边界：未报告置信区间，多数实验在单卡NVIDIA 4090或A800上进行，未提供代码URL。零微调策略在动态任务（如DVS）上的表现未充分验证，可能限制其在事件流数据上的潜力。

## 关联研究分析

从问题动机看，STATA（Zhuge et al., 2024）同样针对Token剪枝，但依赖重训练和Anchor Token，而本文通过IRToP准则实现零微调，根源在于STATA的剪枝决策与训练过程耦合，本文则将其解耦为前向传播中的启发式评估。从方法设计看，SparseSpikformer（Liu et al., 2024）基于发放率剪枝，忽略了时间动态，本文引入时间评分器，更契合SNN的时序特性，但本文未探索时间评分在长序列任务中的稳定性，查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

本文核心矛盾是脉冲Transformer的高计算开销与边缘部署需求之间的冲突。现有剪枝方法因依赖重训练或结构修改而缺乏通用性，本文通过IRToP准则和IR-Arc架构，在不修改结构、无需重训练的前提下实现高效压缩。实验证明，在SDT-V1上保留51% Token时，OPs降低48%，精度仅降1.53%。本文边界在于零微调策略在动态任务上的潜力未验证，且未与最新SOTA方法对比。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.00527)