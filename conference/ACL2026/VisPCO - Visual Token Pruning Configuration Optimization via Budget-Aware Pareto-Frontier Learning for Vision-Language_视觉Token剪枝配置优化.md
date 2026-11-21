# ACL2026最新论文 ｜VisPCO: Visual Token Pruning Configuration Optimization via Budget-Aware Pareto-Frontier Learning for Vision-Language Models ｜视觉Token剪枝配置优化

研究机构：上海交通大学、英国爱丁堡大学

作者：Huawei Ji、Yuanhao Sun、Yuan Jin 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.15188)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.15188)

> 视觉语言模型处理高分辨率图像时，视觉Token数量激增导致二次方计算成本，现有剪枝方法依赖固定或启发式配置，无法保证在给定计算预算下达到性能最优。VisPCO将剪枝配置搜索形式化为Pareto优化问题，通过可微分代理网络自动预测层间保留比率，以梯度下降替代网格搜索。该方法在8个基准上验证了跨架构泛化性，但训练成本与极端压缩率下的鲁棒性尚未充分验证。

## 研究背景

当VLM处理高分辨率图像时，视觉Token从数百激增至数千，二次方注意力计算成为部署瓶颈。视觉Token存在空间冗余，但冗余程度随层深和输入复杂度动态变化，固定剪枝比率无法适应这种非均匀性。Pareto最优性是多目标优化中的经典概念，指无法在不牺牲一个目标的情况下改进另一个目标的状态，连接这些最优点的曲线称为Pareto前沿。

视觉Token剪枝领域已形成Pre-LLM与Intra-LLM两条主要路线，前者在编码器侧降低输入长度，后者在LLM内部利用注意力信号剪枝。FastV、SparseVLM等方法通过预设比率或启发式规则确定剪枝位置与比例，但缺乏机制验证这些配置是否达到计算-性能权衡的最优解。VisPCO的切入点在于：将配置搜索从离散网格采样转化为连续可微优化问题，使模型能自动发现特定预算下的Pareto最优配置。

## 核心方法

### 方法参照系

传统剪枝方法将配置优化视为离散搜索问题：在层位置与比率构成的网格空间中采样，评估每个配置的性能与FLOPs，选取最优。该流程的关键局限在于搜索空间随层数指数增长，网格采样成本不可接受，且无法保证找到全局最优。VisPCO将配置参数化为连续变量，通过代理网络预测，使优化过程可微分。

### 可微分配置搜索

传统方法中，保留Token数量 $k_i = \lfloor r_i \cdot N_v \rfloor$ 涉及取整操作，导致梯度消失，无法反向传播更新比率 $r_i$。VisPCO采用高斯核软插值估计选择阈值，替代硬阈值：

$$\tau_i = \sum_{j=1}^{N_v} w_{ij} s_{ij}, \quad w_{ij} = \frac{\exp(-\frac{(j - \tilde{k}_i)^2}{2\sigma^2})}{\sum_{l=1}^{N_v} \exp(-\frac{(l - \tilde{k}_i)^2}{2\sigma^2})}$$

其中 $\tilde{k}_i = r_i \cdot N_v$ 为浮点保留数量，$\sigma$ 控制核宽度。该公式通过加权平均平滑阈值估计，使 $\tau_i$ 对 $r_i$ 的梯度在所有 $r_i \in (0,1)$ 上良定义，解决了离散化导致的梯度阻断问题。

### 增广拉格朗日约束优化

剪枝配置需满足FLOPs预算约束 $F(\mathbf{r}) \leq B$，该约束为非凸不等式。VisPCO引入辅助变量 $y$ 将其转化为等式约束，并采用增广拉格朗日法求解：

$$\phi(\mathbf{r}, w, \lambda) = \mathcal{L}_{distill}(\mathbf{r}) + \frac{\lambda}{2} \left( B - F(\mathbf{r}) + \frac{w}{\lambda} \right)^2 - \frac{w^2}{2\lambda}$$

其中 $w$ 为拉格朗日乘子，$\lambda$ 为惩罚参数。该公式通过迭代更新 $w$ 和 $\lambda$，在满足预算约束的同时最小化性能损失，避免了二次惩罚方法的病态性和标准拉格朗日法的收敛困难。

## 实验评估

实验基于Qwen2.5VL-3B，训练集从LLaVAInstruct-150K下采样30K样本，评估覆盖A-OKVQA、VizWiz、SEEDBench、MMBench、MME、ChartQA、OCRBench、TextVQA八个基准。基线包括FastV、SparseVLM、FitPrune等Intra-LLM剪枝方法，但缺失VisionZip等Pre-LLM代表方法，也未与GRIP-VLM等SOTA端到端方法直接对比。

| 方法 | 预算 | Avg (%) |
|---|---|---|
| FastV | 50% | 63.1±9.5 |
| FastV + VisPCO | 50% | 71.5 |
| SparseVLM | 50% | 64.5±8.4 |
| SparseVLM + VisPCO | 50% | 71.8 |
| FitPrune | 50% | 65.4±7.9 |
| FitPrune + VisPCO | 50% | 72.2 |

在50% FLOPs预算下，VisPCO将FastV的平均准确率从63.1%提升至71.5%，SparseVLM从64.5%提升至71.8%，FitPrune从65.4%提升至72.2%，表明配置优化能显著恢复剪枝导致的性能损失。

| 模式 | 核函数 | Avg (%) |
|---|---|---|
| Single-Layer | - | 77.3 |
| Multi-Layer | Linear | 76.1 |
| Multi-Layer | Exponential | 75.7 |
| Multi-Layer | P-Sigmoid | 75.2 |
| Multi-Layer | Multi-Step | 77.8 |

多步剪枝模式（77.8%）优于单层剪枝（77.3%）和其他多核模式，揭示VLM在多个关键层进行信息压缩的层级结构。该发现与Ebbinghaus遗忘曲线假设一致，但线性衰减（76.1%）和指数衰减（75.7%）表现较差，表明均匀或单调递减的压缩策略并非最优。

评估协议未报告置信区间，数值比较需谨慎。代码已开源，超参数包括 $\lambda=100$、$\epsilon=0.01$、$\sigma=10$、$T=0.1$，训练使用8块NVIDIA H20 GPU。硬件效率测试显示，VisPCO在50%预算下保持与FastV相当的TTFT（76 vs 74 ms）和吞吐量（20 vs 20 tokens/s），确认配置优化不引入额外延迟开销。

## 关联研究分析

从问题动机看，VisPCO与AutoPrune均将剪枝视为全局资源分配问题，但AutoPrune联合优化Token选择、分配与复活策略，而VisPCO仅优化层间保留比率，不涉及Token级选择。这一差异源于任务特性：AutoPrune针对固定预算下的最大性能，VisPCO针对可变预算下的Pareto前沿逼近。VisPCO未探索Token复活机制，可能在极端压缩率下损失关键信息，论文未给出回答。

从方法设计看，VisPCO与FitPrune均使用二分搜索或优化策略确定层间比率，但FitPrune基于注意力统计的分布散度最小化，VisPCO基于端到端性能损失梯度。FitPrune是Training-free方法，VisPCO需要训练代理网络。这一差异暗示：当模型架构或任务分布变化时，FitPrune的启发式规则可能失效，而VisPCO的端到端优化能自适应调整，但训练成本限制了其部署灵活性。VisPCO未验证在未见模型上的零样本泛化能力，训练-推理一致性评估协议缺失。

## 总结

VisPCO解决的核心矛盾是固定剪枝配置无法保证计算-性能最优，其切入点在于将离散配置搜索转化为连续可微优化，通过增广拉格朗日法处理非凸预算约束，使梯度下降能自动发现Pareto最优配置。实验证明在50%预算下，VisPCO将FastV平均准确率从63.1%提升至71.5%，多步剪枝模式（77.8%）优于单层（77.3%）。边界在于：训练需要30K样本和8块GPU，未验证在极端压缩率（<10%）下的鲁棒性，且缺失与Pre-LLM剪枝方法的对比。当输入复杂度分布发生显著偏移时，代理网络预测的配置是否仍能逼近Pareto前沿，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.15188)