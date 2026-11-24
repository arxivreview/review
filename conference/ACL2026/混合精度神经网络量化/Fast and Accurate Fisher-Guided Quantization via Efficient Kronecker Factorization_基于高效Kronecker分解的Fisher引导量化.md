# ACL2026最新论文 ｜Fast and Accurate Fisher-Guided Quantization via Efficient Kronecker Factorization ｜基于高效Kronecker分解的Fisher引导量化

作者：Viktoriia A. Chekalina、Gerasin Timofey、Andrey Kuznetsov 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3088c65f056b)

> 大语言模型在极低比特压缩下，二阶曲率信息是维持精度的关键，但现有全Hessian分解方法计算开销巨大，阻碍了其在时间敏感场景中的实际应用。FastKron 通过引入 Lanczos 算法替代 Power Iteration 计算 Kronecker 因子，将因子计算加速 10 倍，并在保持全 Hessian 精度的同时实现了 SOTA 性能。该方法证明了在 LLM 谱结构下，Lanczos 收敛速度优于 Power Iteration，为二阶量化提供了高效且准确的曲率估计方案。其价值在于解决了二阶量化中“精度-效率”的矛盾，但实验未覆盖动态负载或异构硬件场景，且对非 Transformer 架构的普适性未作验证。

## 研究背景

当 LLM 权重被压缩至 2-4 bit 时，量化误差不再均匀分布，而是与损失曲面的局部曲率强相关。忽略二阶信息（Hessian）的量化方法在低比特下精度崩塌，而直接计算全 Hessian 矩阵因维度爆炸（$O(N^2)$）而不可行。因此，研究界转向 Kronecker 因子分解，将 Hessian 近似为行/列协方差矩阵的 Kronecker 积，但现有方法（如 YAQA）依赖 Power Iteration 计算因子，收敛速度慢，7-8B 模型需数天完成校准。

二阶量化领域长期存在“对角近似”与“全 Hessian 分解”的路线之争。对角近似（如 QTIP）计算高效但丢失特征间相关性，导致 2-bit 下精度损失 14-16%；全 Hessian 方法（如 YAQA）精度更优，但 Power Iteration 的收敛速度受谱间隙 $q = \lambda_2/\lambda_1$ 限制，在 LLM 中 $q$ 中位数为 0.34，导致迭代次数激增。FastKron 的切入点在于：LLM Hessian 的谱结构特性使得 Lanczos 算法在积分范数与逐点收敛上均优于 Power Iteration，从而在保持全曲率信息的同时，将因子计算开销降低一个数量级。

## 核心方法

### 方法参照系

标准二阶 PTQ 流程包含两步：(1) 在校准集上估计 Hessian 因子 $H_I, H_O$；(2) 利用因子修正权重舍入目标。YAQA 采用 Power Iteration 计算因子，QTIP 仅用对角近似。FastKron 保留 YAQA 的 Kronecker 分解框架与 TCQ 舍入流程，核心改动在于因子计算算法从 Power Iteration 替换为 Lanczos，并证明其在 LLM 谱结构下的收敛优势。

### Kronecker 因子的高效 Lanczos 分解

Power Iteration 的收敛率由 $q^k$ 决定，而 Lanczos 的 Ritz 向量误差界为 $\left(\frac{1-q}{1+q}\right)^k$。由于 LLM 层谱间隙 $q$ 中位数为 0.34，且多数层 $q > 0.29$（Lanczos 与 Power Iteration 的交叉点），Lanczos 在积分范数与逐点收敛上均更快。FastKron 利用 Kronecker 积的置换性质，避免构造完整 $(m^2 \times n^2)$ Hessian，将每次 SVD 迭代简化为三个线性层尺寸矩阵的乘法：

$$ \tilde{H}v = \sum_{i=1}^{|D|} \text{vec}(G_i^\top \text{reshape}(v) G_i) $$

该公式表明，Hessian-向量乘积可通过校准梯度 $G_i$ 的在线累加实现，无需存储完整 Hessian。Lanczos 迭代 $K$ 次后，通过 Ritz 值 $\sigma$ 与特征向量 $v$ 重构因子 $H_I, H_O$，计算复杂度从 $O(N^2)$ 降至 $O(N)$，实现 10 倍加速。

### 曲率引导的 TCQ 权重舍入

因子计算后，FastKron 将 $H_I, H_O$ 的 LDL 分解矩阵 $L_I, L_O$ 注入 TCQ 舍入过程。对于权重块 $W_k$，量化目标修正为：

$$ W_k = Q\left( W_k^\star + L_O^\top \Delta W_{k-1} L_I + L_O^\top \Delta W_{k-1} + \Delta W_{k-1} L_I \right) $$

其中 $\Delta W_{k-1}$ 为前序块累积量化误差。该公式通过曲率信息加权误差补偿，使当前块量化决策感知全局损失曲面形状。相比 QTIP 的对角近似，全 Hessian 因子捕捉了特征维度间的相关性，在 2-bit 下将 LLaMA-2 平均准确率提升 0.3%，Qwen-4B 提升 12.8%，验证了非对角项在极端压缩下的关键作用。

## 实验评估

实验在 LLaMA-2-7B、LLaMA-3-8B 及 Qwen3 系列（0.6B-8B）上进行，校准集为 FineWeb（batch size 128），评估指标包括 WikiText-2/C4 困惑度及 Commonsense、GSM8K、IFEval 零样本准确率。基线覆盖 QTIP（对角 Hessian）、YAQA（全 Hessian，Power Iteration）及 NoHess（无曲率），但缺失 GPTQ、AWQ 等主流 PTQ 基线，限制了与工业界标准的直接对比。

| 模型 | 位宽 | 方法 | Wiki PPL ↓ | AVG Acc ↑ | GPU h ↓ | Tokens ↓ |
|---|---|---|---|---|---|---|
| LLaMA-2-7B | 4-bit | FastKron | 5.18 | 0.663 | 0.7 M | ↓96% |
| LLaMA-2-7B | 4-bit | YAQA | 5.17 | 0.659 | 16 M | – |
| LLaMA-2-7B | 2-bit | FastKron | 6.40 | 0.624 | 0.9 M | ↓94% |
| LLaMA-2-7B | 2-bit | YAQA | 6.18 | 0.622 | 16 M | – |
| Qwen3-8B | 4-bit | FastKron | 5.18 | 0.713 | 0.7 M | ↓96% |
| Qwen3-8B | 4-bit | YAQA | 5.17 | 0.712 | 16 M | – |
| Qwen3-8B | 2-bit | FastKron | 9.11 | 0.653 | 0.9 M | ↓94% |
| Qwen3-8B | 2-bit | YAQA | 8.98 | 0.643 | 16 M | – |

在 4-bit 下，FastKron 与 YAQA 性能持平（PPL 差 <0.01），但校准 token 数减少 96%（0.7M vs 16M）；在 2-bit 下，FastKron 平均准确率优于 YAQA 0.3%-12.8%，且 PPL 略高（如 LLaMA-2 6.40 vs 6.18），表明其收敛更稳定但非严格占优。消融实验显示，OnlyDiag（仅对角因子）性能介于 NoHess 与 FastKron 之间，证实非对角项贡献 0.5-2% 精度提升。

评估边界方面，论文未报告置信区间，且所有实验为一次性量化（one-shot），未测试持续学习或动态负载场景。代码已开源（GitHub），但超参数（如 Lanczos 迭代次数 $K$）未详细披露，可复现性依赖官方实现。

## 关联研究分析

从方法设计看，FastKron 与 YAQA 同属全 Hessian Kronecker 分解路线，但 YAQA 依赖 Power Iteration，其收敛速度受谱间隙 $q$ 限制，而 FastKron 利用 Lanczos 的 Krylov 子空间性质，在 LLM 谱结构下实现更快收敛。这一差异源于 LLM Hessian 的谱分布特性：多数层 $q > 0.29$，使得 Lanczos 的逐点收敛优势得以体现。YAQA 未探索此谱结构特性，导致其因子计算成为瓶颈，而 FastKron 通过算法替换而非架构改动解决了此问题，体现了“算法优化”而非“模型改进”的路径。

从问题动机看，FastKron 与 QTIP 均关注二阶信息在量化中的作用，但 QTIP 采用对角近似以牺牲精度换取效率，FastKron 则通过加速全 Hessian 计算实现精度与效率的平衡。QTIP 的对角假设在 2-bit 下导致 14-16% 精度损失，而 FastKron 的全 Hessian 方案将损失控制在 5-6%，表明在极端压缩下，特征间相关性不可忽略。然而，FastKron 未测试非 Transformer 架构（如 CNN、SNN），其谱结构假设是否普适，论文未给出回答。

## 总结

FastKron 解决了二阶量化中全 Hessian 分解计算开销过大的核心矛盾，其切入点在于 LLM Hessian 的谱结构特性使得 Lanczos 算法收敛速度优于 Power Iteration。通过 Kronecker 因子的高效 Lanczos 分解，该方法在保持全曲率信息的同时，将因子计算加速 10 倍，并在 2-bit 下实现 0.3%-12.8% 的准确率提升。其边界在于实验仅覆盖 Transformer 架构，且未测试动态负载或异构硬件场景，校准 token 数虽减少 96%，但绝对值（0.7M）仍高于部分对角近似方法。当模型规模扩展至 70B 以上时，Lanczos 迭代的内存开销是否成为新瓶颈，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_3088c65f056b)