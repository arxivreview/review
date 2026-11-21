# HuggingFace最新推荐论文 ｜AdaPreLoRA: Adafactor Preconditioned Low-Rank Adaptation ｜AdaPreLoRA：基于Adafactor预条件的低秩适配优化器

研究机构：香港科技大学

作者：Ziyun Liu、Fengmiao Bian、Jian-Feng Cai

论文原文见 [arXiv](https://arxiv.org/abs/2605.08734)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.08734)

> 导读 低秩适配（LoRA）在因子空间优化时面临雅可比矩阵秩亏导致的预条件子奇异问题，现有方法要么牺牲梯度统计结构，要么付出高昂内存代价。本文指出，尽管因子空间预条件子不可逆，但对应的线性方程组始终一致，其解集构成一个仿射子空间。通过引入Adafactor对角Kronecker预条件子并设计$H_t$-平衡准则，本文在保持$O((m+n)r)$内存预算下，以闭式解唯一确定因子更新。该方法在7B规模模型上验证了低内存梯度统计预条件子的有效性，但其对动态秩分配场景的适用性尚未探索。

## 研究背景

当LoRA冻结预训练权重$W_0$并仅训练低秩因子$B, A$时，优化器需在因子空间$[B, A]$中计算更新方向。然而，生成映射$G: [B, A] \to BA$的雅可比$J_G$存在非平凡核空间，导致任何$W$空间预条件子$F_t$诱导的因子空间算子$J_G^* F_t J_G$必然奇异。这一秩亏特性使得标准链式法则无法唯一地将$W$空间预条件方向映射回因子空间更新，构成了LoRA优化器的根本性障碍。

现有LoRA优化器沿两条路线应对此障碍：廉价因子空间方案（如Vanilla LoRA、LoRA+）保持$O((m+n)r)$内存，但丢弃$W$空间梯度统计结构，仅使用恒等或块对角近似；伪逆方案（如LoRA-Pro）保留梯度统计，但需维护$O(mn)$内存的$W$空间矩，在LLM规模下不可行。本文切入点在于：尽管$J_G^* F_t J_G$奇异，但线性方程组$J_G^* F_t J_G [\Delta B_t, \Delta A_t] = J_G^*(G_t)$始终一致，其解集为$r^2$维仿射子空间。通过选择特定的$F_t$和仿射解集元素选择规则，可在低内存约束下恢复梯度统计结构。

## 核心方法

### 方法参照系

LoRA优化器的标准流程是在因子空间$[B, A]$中计算梯度$[G_B^t, G_A^t]$，并通过预条件子调整更新方向。本文问题与该通用流程的关键差异在于：因子空间预条件子$J_G^* F_t J_G$的奇异性使得标准预条件更新无定义，需引入仿射解集选择机制。

### 奇异算子的一致性与仿射解集

设计动机：解决$J_G^* F_t J_G$奇异导致的更新方向非唯一性问题。本文证明，尽管该算子不可逆，但方程组$J_G^* F_t J_G [\Delta B_t, \Delta A_t] = J_G^*(G_t)$的解集非空，且构成一个$r^2$维仿射子空间。该子空间中的每个元素都诱导相同的$W$空间更新（即$F_t^{-1}G_t$在$T_t = \text{range}(J_G)$上的$H_t$-正交投影），但对应不同的因子轨迹。这一发现将优化器设计分解为两个耦合选择：(i) $W$空间预条件子$F_t$的选择，(ii) 仿射解集元素的选择规则。

### Adafactor预条件子与$H_t$-平衡准则

设计动机：在保持$O((m+n)r)$内存预算下，引入非平凡梯度统计结构。本文采用Adafactor对角Kronecker形式$F_t = L_t \otimes R_t$，其算子平方根$H_t = F_t^{1/2}$定义为$H_t Y = L_t^{1/2} Y R_t^{1/2}$，内存成本仅为$O(m+n)$。对于仿射解集元素选择，本文提出$H_t$-平衡准则，最小化两个因子贡献之间的$H_t$-范数不平衡：

$$\min_{[\Delta B_t, \Delta A_t] \in \mathcal{S}} \|\Delta B_t A_t - B_t \Delta A_t\|_{2, H_t}$$

其中$\mathcal{S}$为仿射解集。该准则在$H_t$-加权内积下平衡$B$和$A$的更新幅度，避免了Moore-Penrose伪逆的Frobenius最小范数解可能导致的因子轨迹失衡。结合$H_t$-平衡准则，AdaPreLoRA的因子更新具有闭式解，额外计算成本为$O(r^3)$，优化器状态保持$O((m+n)r)$。

## 实验评估

实验在GPT-2（E2E）、Mistral-7B和Qwen2-7B（GLUE、ARC、GSM8K）及扩散模型个性化任务上进行，基线覆盖Vanilla LoRA、Scaled AdamW、LoRA-Pro AdamW、SOAP等代表性优化器。

| 模型 | 方法 | RTE | CoLA | MRPC | ARC | GSM8K |
| --- | --- | --- | --- | --- | --- | --- |
| Mistral-7B | AdamW | 89.4 | 69.4 | 88.8 | 75.1 | 85.3 |
| Mistral-7B | Scaled AdamW | 89.5 | 71.5 | 88.9 | 74.2 | 84.8 |
| Mistral-7B | LoRA-Pro AdamW | 89.1 | 68.5 | 88.9 | 74.2 | 84.8 |
| Mistral-7B | AdaPreLoRA AdamW | 89.5 | 71.4 | 90.0 | 76.4 | 85.6 |
| Qwen2-7B | AdamW | 90.6 | 84.3 | 89.7 | 80.9 | 75.7 |
| Qwen2-7B | Scaled AdamW | 90.0 | 85.6 | 90.6 | 80.9 | 73.2 |
| Qwen2-7B | LoRA-Pro AdamW | 84.3 | 85.3 | 88.1 | 75.7 | 86.3 |
| Qwen2-7B | AdaPreLoRA AdamW | 91.0 | 85.6 | 90.4 | 76.4 | 85.6 |

在Mistral-7B上，AdaPreLoRA在6/7设置中取得最佳准确率，仅CoLA落后Scaled AdamW 0.1点；在Qwen2-7B上，LoRA-Pro AdamW和SOAP在多个任务上性能低于Vanilla AdamW，表明高内存梯度统计方法在7B规模下未转化为性能增益。

消融实验显示，AdaPreLoRA-SGD在Mistral-7B GLUE-RTE上峰值内存为21.5 GB，低于所有基线；AdaPreLoRA-AdamW峰值内存26.0 GB，与Scaled AdamW持平，而LoRA-Pro AdamW需50.4 GB（约2倍）。这一内存优势源于Adafactor的$O(m+n)$二阶矩估计，避免了LoRA-Pro的$O(mn)$全权重矩维护。

评估边界：论文未报告置信区间，数值比较需谨慎；实验未覆盖动态秩分配场景（如AdaLoRA、PrunedLoRA），仅验证固定秩下的优化器改进；代码未开源，超参数通过网格搜索独立调优，可复现性受限。

## 关联研究分析

从问题动机看，本文与LoRA-Pro共享仿射解集框架，但关键差异在于预条件子度量的一致性。LoRA-Pro AdamW使用Frobenius残差$\|J_G[\Delta B_t, \Delta A_t] - F_t^{-1}G_t\|_F$，而本文使用$H_t$-加权残差$\|J_G[\Delta B_t, \Delta A_t] - F_t^{-1}G_t\|_{H_t}$。这一差异源于LoRA-Pro的度量不匹配：其AdamW变体在$W$空间使用非平凡$F_t$，但在因子空间使用Frobenius范数，导致预条件子几何与优化目标不一致。本文通过$H_t$-加权残差修正了这一不匹配，使得因子更新方向在$H_t$-加权内积下成为$W$空间预条件方向的最优LoRA近似。

从方法设计看，本文与Riemannian Preconditioned LoRA同属块对角近似路线，但本文引入了非平凡$F_t$。Riemannian Preconditioned LoRA取$F_t = I$，仅使用块对角近似$J_G^* J_G$，丢弃了梯度统计结构；本文采用Adafactor对角Kronecker$F_t$，在$O(m+n)$内存下恢复了部分梯度统计信息。这一设计选择反映了任务特性：在7B规模下，$O(m^2+n^2)$内存的Shampoo预条件子（SOAP）不可行，而$O(m+n)$的Adafactor提供了梯度统计与内存效率的平衡点。

## 总结

本文要解决的核心矛盾是LoRA因子空间预条件子奇异性与低内存预算的冲突。现有方法要么丢弃梯度统计结构（廉价因子空间方案），要么付出$O(mn)$内存代价（LoRA-Pro），无法同时满足两个约束。本文抓住的切入点是：尽管$J_G^* F_t J_G$奇异，但对应线性方程组始终一致，其解集构成仿射子空间，可通过选择规则唯一确定。本文采用Adafactor对角Kronecker预条件子$H_t$和$H_t$-平衡准则，在$O((m+n)r)$内存下以闭式解实现梯度统计感知的因子更新。实验证明，在Mistral-7B上，AdaPreLoRA在6/7设置中取得最佳准确率，峰值内存与Scaled AdamW持平（26.0 GB），而LoRA-Pro AdamW需50.4 GB。本文的边界在于：实验仅覆盖固定秩场景，未验证$H_t$-平衡准则在动态秩分配（如AdaLoRA、PrunedLoRA）中的有效性；当秩$r$动态变化时，仿射解集的维度和$H_t$-平衡准则的最优性是否保持，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.08734)