# HuggingFace最新推荐论文 ｜Meta Expert: Cross-Layer Expert Sharing for Storage- and Retrieval-Efficient MoE ｜跨层专家共享的稀疏混合专家架构

研究机构：清华大学

作者：Ermo Hua、Xiangyu Hong、Baiting Wu 等 14 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.27598)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.27598)

> 稀疏混合专家（Sparse Mixture-of-Experts, SMoE）通过稀疏激活解耦模型容量与计算成本，但主流架构中各层专家独立，导致跨层参数冗余与存储效率低下。现有方法多聚焦于层内稀疏度优化或后训练压缩，忽视了层间知识复用潜力。本文提出 Meta Experts 架构，将部分专家跨层共享，在保持激活计算量不变的前提下降低总参数量。该架构通过引入激活层面的双向残差连接提升信息检索效率，在同等计算预算下显著降低交叉熵损失与专家冗余，为 SMoE 的存储效率优化提供了新的架构范式。

## 研究背景

当 SMoE 模型规模扩张时，前馈网络（Feed-Forward Network, FFN）占据绝大部分参数，其密集计算特性导致训练与推理成本激增。SMoE 通过将 FFN 拆分为多个专家子网络并仅激活 Top-K 专家，实现了单 Token 计算成本与总参数量的解耦。然而，这种解耦仅发生在宽度维度，深度维度上的参数冗余问题日益凸显。可解释性研究表明，不同层的 FFN 存储了高度相似的知识，这种层间冗余在主流架构中未被有效利用。

主流 SMoE 架构如 Switch Transformer 和 DeepSeek-MoE 采用层级隔离设计，每层拥有独立的 Local Experts。这种设计虽简化了路由逻辑，但迫使模型在每一层重复存储相似知识，导致显存占用远超计算需求。尽管 Looped Transformers 通过参数复用降低了参数量，但其增加的递归深度引入了额外的串行计算延迟。如何在保持 MoE 稀疏激活优势的同时，消除层间参数冗余并避免递归延迟，成为 SMoE 架构演进的关键瓶颈。

## 核心方法

### 方法参照系：层级隔离的 SMoE 架构

标准 SMoE 架构中，第 $l$ 层包含独立的路由器 $R_l$ 和 $N$ 个 Local Experts $\{\phi_e(\cdot; \theta_e^l)\}_{e=0}^{N-1}$。给定输入 $x_l$，经 RMSNorm 归一化后，路由器计算门控分数并选择 Top-K 专家，输出为 $y_l = \sum_{e \in \text{topk}(R_l, \hat{x}_l)} R_l(\hat{x}_l)_e \phi_e(\hat{x}_l; \theta_e^l)$。该架构的核心局限在于专家参数 $\theta^l$ 与路由器 $R_l$ 严格层私有，层间无参数共享，导致知识存储冗余。

### 跨层共享的 Meta Experts 机制

针对层间冗余，本文引入 Meta Experts，将部分专家参数 $\theta$ 和路由器 $R$ 跨所有层共享。在混合架构中，每层同时包含 $N$ 个 Local Experts 和 $M$ 个 Meta Experts。路由器分别计算两类专家的激活权重，输出为：

$$
y_l = \sum_{e \in \text{topk}(R_l, \hat{x}_l)} w_e^l \phi_e(\hat{x}_l; \theta_e^l) + \sum_{e \in \text{topk}(R, \hat{x}_l)} w_e \phi_e(\hat{x}_l; \theta_e)
$$

其中 $w_e^l$ 和 $w_e$ 为归一化后的门控权重。该设计动机在于：通过共享专家池，模型无需在每层重复存储相似知识，从而在固定激活专家数 $K$ 下，显著降低总参数量。实验表明，Meta Experts 比例达 75% 时，模型在同等 FLOPs 下损失最低，且专家冗余比显著下降。

### 激活层面的双向残差连接

Meta Experts 的有效性不仅源于参数共享，更在于其改变了信息流动路径。在标准 SMoE 中，深层信息仅通过梯度回传影响浅层参数，前向传播中浅层无法读取深层内容。Meta Experts 通过共享参数 $\theta$，使第 $l$ 层的参数更新 $\Delta \theta_l$ 直接影响第 $m$ 层的读取输出。第 $m$ 层读取第 $l$ 层写入内容的一阶影响为：

$$
I_{m \leftarrow l} \approx -\eta \gamma^2 \sum_{t<T} J_m^{(t)} J_l^{(t)\top} \bar{y}_l^{(t)}
$$

其中 $J_m^{(t)}$ 为第 $m$ 层专家输出对参数的雅可比矩阵。该公式表明，深层内容通过共享参数在激活层面直接传递至浅层，形成“反向残差连接”。这种双向访问机制使浅层能检索深层知识，深层能复用浅层特征，提升了信息检索效率。

## 实验评估

实验在 6B-A1.6B 模型规模上进行，训练 200B tokens，评估 MMLU、C-Eval 等下游任务。基线为 Vanilla MoE（仅 Local Experts）。消融实验验证了 Meta Experts 比例、拓扑结构（Loop 机制、首尾层隔离）的影响。

| 数据集 | Vanilla | MR75 | MR75 + Loop2 | MR75 + F2L2 | MR75 + F2L2 + Loop2 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| MMLU | 0.4087 | 0.4120 | **0.4175** | 0.3928 | 0.4052 |
| C-Eval | 0.4354 | 0.4443 | **0.4487** | 0.4160 | 0.4302 |
| CMMLU | 0.4203 | 0.4161 | **0.4344** | 0.4198 | 0.4249 |
| TriviaQA | 0.1924 | 0.1964 | 0.1932 | 0.2014 | **0.2042** |
| BBH | 0.2972 | 0.2912 | 0.3030 | **0.3061** | 0.2984 |
| OpenBookQA | 0.3500 | 0.3380 | **0.3640** | 0.3320 | 0.3540 |

主结果显示，MR75 + Loop2 在 MMLU 上达到 0.4175，较 Vanilla 提升 0.88 个百分点。消融实验表明，将 Meta Experts 划分为 2 个子池（Loop2）并限制首尾两层使用 Local Experts（F2L2）的组合策略在多数任务上表现最优。值得注意的是，F2L2 单独使用时性能下降，但与 Loop2 结合后产生协同效应，暗示浅层与深层专家功能特异性需与层级化共享机制配合。

评估边界方面，实验仅覆盖 200B tokens 训练量，未验证更大规模预训练下的稳定性。此外，未与 PuzzleMoE 等后训练压缩方法进行直接对比，无法评估 Meta Experts 与压缩技术的兼容性。代码未开源，复现需依赖论文描述。

## 关联研究分析

从问题动机看，本文与 Looped Transformers 均旨在通过参数复用降低冗余，但 Looped Transformers 通过增加递归深度实现复用，导致推理延迟线性增长。Meta Experts 利用 MoE 稀疏激活特性，在保持递归深度不变的前提下实现跨层共享，避免了串行计算瓶颈。这一差异源于 MoE 架构中专家激活的稀疏性，使得共享专家池的容量可远大于单层激活数，而 Looped Transformers 的共享参数必须全量参与计算。

从方法设计看，本文与 DeepSeek-MoE 均引入共享专家，但 DeepSeek-MoE 的共享专家仅用于层内通用知识处理，仍保持层间隔离。Meta Experts 则打破层间边界，实现全局共享。这种差异导致 DeepSeek-MoE 无法消除层间冗余，而 Meta Experts 通过全局共享显著降低冗余比。然而，DeepSeek-MoE 的层内共享更易实现负载均衡，Meta Experts 的全局共享可能加剧热点专家拥堵，论文未详细讨论极端负载不均下的表现。

## 总结

本文针对 SMoE 架构中层间参数冗余问题，提出 Meta Experts 跨层共享机制，通过激活层面的双向残差连接提升信息检索效率。在 6B-A1.6B 模型上，MR75 + Loop2 配置在 MMLU 上达到 0.4175，较 Vanilla 基线提升 0.88 个百分点，且专家冗余比显著降低。该架构在同等计算预算下实现了更高的参数效率，为 SMoE 存储优化提供了新路径。然而，实验仅覆盖 200B tokens 训练量，未验证大规模预训练下的稳定性，且未评估全局共享专家在极端负载不均下的负载均衡表现。当模型规模进一步扩张至万亿参数时，全局共享专家池的路由冲突与通信开销是否会抵消参数复用带来的收益，仍需更大规模实验验证。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.27598)