# ICLR2026最新论文 ｜MASKPRO: LINEAR-SPACE PROBABILISTIC LEARNING FOR STRICT (N:M)-SPARSITY ON LLMS ｜MaskPro：基于线性空间概率松弛的 (N:M) 稀疏掩码学习

研究机构：澳大利亚悉尼大学、新加坡南洋理工大学

作者：Yan Sun、Qixin ZHANG、Zhiyuan Yu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_68009882)

> 导读 大语言模型（LLM）的半结构化稀疏化旨在通过保留每 $M$ 个权重中的 $N$ 个来实现硬件友好的加速，但现有方法面临两难困境：规则基方法因局部贪心导致性能上限低，而学习基方法 MaskLLM 因存储所有掩码概率分布导致内存开销呈指数级增长。MaskPro 提出了一种线性空间概率松弛框架，将 (N:M) 稀疏掩码生成重构为在 $M$ 个连续元素上的 $N$-way 无放回采样过程，从而将 logits 存储需求从 $O(\binom{M}{N} d)$ 降至 $O(d)$。该方法结合基于损失残差的策略梯度估计器（Policy Gradient Estimator, PGE）与移动平均追踪器，在显著降低训练成本的同时提升了掩码质量。尽管实验显示其在多个基准上优于规则基与全量学习基方法，但其对单样本鲁棒性的声称及在高稀疏率下的泛化能力仍存疑。

## 研究背景

理解本文需厘清半结构化稀疏化中的组合优化本质。当 LLM 权重被划分为 $M$ 个一组并保留 $N$ 个时，掩码选择空间大小为 $\binom{M}{N}^{d/M}$，这一巨大搜索空间使得直接梯度下降不可行。传统规则基方法（如 Wanda）通过最小化层内重构误差 $\min_{\mathbf{m}} \|\mathbf{w}\mathbf{x} - (\mathbf{m} \odot \mathbf{w})\mathbf{x}\|$ 来贪心选择掩码，但忽略了端到端损失与层内误差之间的偏差。学习基方法 MaskLLM 试图通过 Gumbel-Max 重参数化直接优化端到端损失，但其为每个可能的掩码分配独立概率分布，导致内存需求随 $M$ 指数增长，在 $N \approx M/2$ 时达到 $O(M^d)$ 量级，严重限制了其在大规模模型上的可扩展性。

现有半结构化剪枝路线在精度与效率间存在显著割裂。规则基方法虽免重训练且内存友好，但受限于局部启发式指标，难以捕捉层间依赖关系，性能天花板较低；MaskLLM 虽能逼近理论最优解，但其训练成本甚至超过微调 LLM 本身，且内存瓶颈使其无法应用于大尺寸权重矩阵。这种“精度-成本”的权衡困境促使研究者探索介于两者之间的中间路径：既保留端到端优化的全局视角，又避免组合爆炸带来的资源开销。MaskPro 的切入点在于重新参数化掩码空间，通过概率松弛将离散组合问题转化为连续分布学习问题，从而在保持端到端优化能力的同时实现线性内存复杂度。

## 核心方法

### 线性空间概率松弛框架

MaskPro 的核心创新在于对 (N:M) 掩码集合 $S_{[N]}^{[M]}$ 的稀疏表示。传统方法将掩码视为 $\binom{M}{N}$ 个独立类别，而 MaskPro 利用坐标概率和运算 $\oplus$，将每个掩码 $\mathbf{m}_i$ 表示为 $N$ 个基向量 $\{\mathbf{a}_{i,1}, \dots, \mathbf{a}_{i,N}\}$ 的和，其中 $\mathbf{a}_{i,j} \in \{\mathbf{e}_1, \dots, \mathbf{e}_M\}$ 且互不相同。这一表示将参数规模从 $\binom{M}{N} d$ 降至 $Nd$。进一步地，MaskPro 为每组变量分配一个类别分布 $\mathbf{p}_i = (p_{i,1}, \dots, p_{i,M})$，并通过 $N$-way 无放回采样生成掩码。该设计动机在于解决 MaskLLM 中 logits 存储的指数级增长问题，使得内存需求仅依赖于权重维度 $d$，即 $O(d)$。

$$
\mathbf{m}_i = \bigoplus_{j=1}^N \mathbf{a}_{i,j}, \quad \text{where } \mathbf{a}_{i,j} \sim \text{Categorical}(\mathbf{p}_i) \text{ (w/o replacement)}
$$

此公式表明，掩码生成过程完全由 $M$ 维概率向量 $\mathbf{p}_i$ 驱动，而非 $\binom{M}{N}$ 维的独立概率分布，从而实现了内存效率的根本性提升。

### 基于损失残差的策略梯度更新

在获得概率松弛后，MaskPro 采用策略梯度（PGE）进行端到端优化。标准 PGE 使用原始损失 $f(\mathbf{m} \odot \mathbf{w}, \xi)$ 作为更新信号，但在 LLM 训练中，不同 mini-batch $\xi$ 的损失基线差异远大于掩码选择带来的损失变化，导致梯度信号被噪声淹没。MaskPro 引入损失残差 $f(\mathbf{m}_t \odot \mathbf{w}, \xi) - f(\mathbf{m}_0 \odot \mathbf{w}, \xi)$ 作为更新依据，其中 $\mathbf{m}_0$ 为初始掩码。为进一步抑制方差，引入移动平均追踪器 $\delta$，更新规则为：

$$
\pi_{t+1} = \pi_t - \eta \left( f(\mathbf{m}_t \odot \mathbf{w}, \xi) - f(\mathbf{m}_0 \odot \mathbf{w}, \xi) - \delta \right) \nabla \log p(\mathbf{m}_t | \pi_t)
$$

其中 $\delta = \alpha \delta + (1-\alpha)(f(\mathbf{m}_t \odot \mathbf{w}, \xi) - f(\mathbf{m}_0 \odot \mathbf{w}, \xi))$，$\alpha=0.99$。该设计动机在于解决标准 PGE 在大规模组合空间中因高方差导致的训练不稳定问题。通过减去基线损失和动态追踪的残差均值，MaskPro 能够区分掩码选择带来的真实改进与数据批次带来的噪声波动，从而加速收敛并提升数值稳定性。

## 实验评估

实验在 Gemma-7B、Vicuna-1.3-7B、Llama-2-7B 和 DeepSeek-7B 上进行，评估 (2:4) 稀疏化在 WikiText-2、HellaSwag、MMLU 等基准上的零样本性能。基线覆盖规则基（Magnitude, SparseGPT, Wanda, GBLM, Pruner-Zero）和学习基（MaskLLM）。在 Llama-2-7B 上，MaskPro 在 WikiText-2 困惑度（PPL）上取得 17.17，优于 Wanda 的 23.44 和 SparseGPT 的 21.07；在 HellaSwag 上准确率为 46.18%，显著高于 Wanda 的 41.32% 和 SparseGPT 的 43.20%。在 Vicuna-1.3-7B 上，MaskPro 的 WikiText-2 PPL 为 21.10，优于所有规则基方法，且内存使用量仅为 25.00 GB，远低于 MaskLLM 的 331.16 GB。

| Model | Method | WikiText-2 PPL | HellaSwag Acc (%) | Memory (GB) |
| :--- | :--- | :--- | :--- | :--- |
| Llama-2-7B | Wanda | 23.44 | 41.32 | 22.20 |
| Llama-2-7B | SparseGPT | 21.07 | 43.20 | 22.20 |
| Llama-2-7B | MaskPro | 17.17 | 46.18 | 26.87 |
| Vicuna-1.3-7B | MaskLLM | 11.86 | 56.32 | 331.16 |
| Vicuna-1.3-7B | MaskPro | 21.10 | 46.81 | 25.00 |

消融实验表明，引入移动平均追踪器显著提升了训练稳定性，损失残差曲线在迭代 1000 次后趋于平稳，而标准 PGE 在 5000 次迭代后仍存在大幅波动。数据集大小敏感性分析显示，MaskPro 在仅使用 1 个训练样本时仍能保持与全量数据相近的性能，验证了其声称的鲁棒性。然而，该鲁棒性仅在 7B 规模模型上验证，且在 (2:4) 稀疏率下表现最佳，未探索更高稀疏率（如 1:4）下的性能边界。

评估协议主要关注零样本静态性能，缺乏对动态推理场景（如长文本生成）的测试。代码已开源，但超参数 $\alpha$ 和 $C$ 的敏感性分析未在正文中详细展开，仅提及在附录中讨论。可复现性方面，论文提供了 GitHub 链接，但未报告具体 GPU 型号和训练时间，限制了跨硬件环境的对比。

## 关联研究分析

从问题动机看，MaskPro 与 MaskLLM 均致力于解决 (N:M) 稀疏掩码的端到端优化，但 MaskPro 通过线性空间松弛解决了 MaskLLM 的内存瓶颈。MaskLLM 的 Gumbel-Max 重参数化虽实现了可微性，但其为每个掩码分配独立概率的设计导致内存开销随 $M$ 指数增长，而 MaskPro 的 $N$-way 无放回采样将参数规模压缩至 $O(d)$。这一差异源于对掩码空间结构的利用：MaskPro 认识到 (N:M) 掩码可由 $N$ 个基向量组合而成，从而避免了显式枚举所有组合。相比之下，规则基方法如 Wanda 虽内存友好，但其层内贪心策略无法捕捉层间依赖，导致在 HellaSwag 等复杂推理任务上性能落后于 MaskPro。

从方法设计看，MaskPro 的策略梯度更新与强化学习中的 REINFORCE 算法类似，但引入了损失残差和移动平均追踪器以应对 LLM 训练中的高方差问题。这与传统剪枝方法（如 LLM-Pruner）的梯度引导结构化剪枝不同，后者依赖于梯度幅值评估通道重要性，而 MaskPro 直接优化端到端损失。与低秩分解方法（如 SVD-LLM）相比，MaskPro 属于稀疏化路线，直接移除权重而非近似权重矩阵，因此在硬件加速上更具优势，但可能在高稀疏率下损失更多信息。MaskPro 对单样本鲁棒性的声称挑战了“校准数据量显著影响性能”的共识，但其机制可能依赖于 PGE 的方差抑制能力，而非数据本身的多样性，这一假设在更大规模模型上是否成立尚不明确。

## 总结

MaskPro 旨在解决半结构化稀疏化中掩码搜索空间巨大与训练成本高昂之间的矛盾。通过线性空间概率松弛，它将 (N:M) 掩码生成重构为 $N$-way 无放回采样，将 logits 存储从 $O(\binom{M}{N} d)$ 降至 $O(d)$，并结合基于损失残差的 PGE 与移动平均追踪器，有效抑制了策略梯度的方差。实验表明，在 Llama-2-7B 上，MaskPro 的 WikiText-2 PPL 为 17.17，HellaSwag 准确率为 46.18%，均优于 Wanda 和 SparseGPT，且内存使用量仅为 26.87 GB，远低于 MaskLLM 的 331.16 GB。然而，其实验仅覆盖 7B 规模模型和 (2:4) 稀疏率，未验证在更高稀疏率或更大模型上的泛化能力。当稀疏率提升至 1:4 时，线性空间松弛是否仍能保持性能优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_68009882)