# HuggingFace最新推荐论文 ｜Federation of Experts: Communication Efficient Distributed Inference for Large Language Models ｜联邦专家架构

研究机构：美国斯坦福大学

作者：Muhammad Shahir Abdurrahman、Chun Deng、Azalia Mirhoseini 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.06206)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.06206)

> 稀疏混合专家（Sparse Mixture-of-Experts, SMoE）在分布式推理中面临专家并行（Expert Parallelism, EP）引发的 All-to-All 通信瓶颈，该开销可占端到端延迟的 68% 以上。现有调度优化方法受限于全局 EP 组的拓扑约束，无法从根本上消除跨节点通信。本文提出联邦专家（Federation of Experts, FoE）架构，通过将专家与 KV 头划分为独立组，将全局 All-to-All 替换为组内通信与轻量级组间 All-Reduce。该架构在单节点部署中完全消除 All-to-All，在多节点部署中将其限制在节点内，实现了推理延迟的显著降低，但其有效性依赖于从头预训练，且未验证对现有开源模型的适配能力。

## 研究背景

专家并行（EP）是部署大规模 SMoE 模型的核心系统技术，其要求 Token 激活通过 All-to-All 通信发送至持有目标专家的 GPU。随着集群规模扩大，Token 与专家共置的概率急剧下降，导致通信开销成为主要瓶颈。本地激活率（Local Activation Rate, LAR）衡量无需网络传输即可在本地 GPU 解决的专家选择比例，是评估 EP 效率的关键指标。在标准 MoE 中，LAR 随 GPU 数量增加而降低，迫使多数 Token 离开驻留 GPU，引发显著的网络延迟。

SMoE 领域已确立稀疏激活解耦容量与成本的共识，但分布式通信瓶颈与负载均衡问题仍是核心痛点。主流优化路线包括调度框架（如 MoETuner、Sem-MoE）通过预测 Token-专家亲和性优化静态分配，以及系统级优化（如 FlashMoE、COMET）通过算子融合与计算-通信重叠掩盖延迟。这些方法均在全局 EP 组内操作，受限于跨节点通信的物理带宽上限。本文切入点在于架构级重构：通过改变专家与 KV 头的分布模式，从结构上保证高 LAR 与完美负载均衡，而非依赖动态调度或低维投影近似。

## 核心方法

### 方法参照系

标准 MoE 架构中，每个 Transformer 层包含一个全局 EP 组，Token 通过全局 Top-k 路由从所有专家中选择，并通过全局 All-to-All 进行分发与合并。本文问题与该通用流程的关键差异在于：将全局 EP 组拆分为 H 个独立专家组，每组拥有 1/H 的 KV 头与专家，路由与通信严格限制在组内。

### 分组路由与表示解耦

标准 MoE 在层边界维护单一表示 $x \in \mathbb{R}^{S \times d}$，而 FoE 维护 H 倍表示 $x \in \mathbb{R}^{H \times S \times d}$，每个专家组独立处理其对应的 KV 头与专家。设计动机在于解决标准 MoE 中注意力计算与 FFN 计算物理位置不匹配导致的强制 All-to-All 问题。每组独立执行 Top-k/H 路由：

$$
I_h[i], w_h[i] = \text{Router}(\bar{r}[i])
$$

其中 $\bar{r}[i] = \frac{1}{H} \sum_{h} r_{h,i}$ 为跨组平均后的残差，作为共享路由输入。该设计将全局 Top-k 路由分解为 H 个独立的组内 Top-k/H 路由，确保每个 Token 在每组中都有专家被激活，从而在结构上保证每组接收相同数量的 Token，实现完美负载均衡。

### 通信拓扑重构

标准 MoE 的 All-to-All 通信量与 k 成正比，而 FoE 通过组内 All-to-All 与组间 All-Reduce 重构通信拓扑。设计动机在于解决多节点部署中跨节点 InfiniBand 带宽远低于节点内 NVLink 带宽（约 18 倍差距）的问题。FoE 的组内 All-to-All 严格限制在节点内，组间 All-Reduce 通信量仅与 H 相关，与 k 无关：

$$
V_{\text{foe}} = 2 \cdot \frac{G-1}{G} + 2 \cdot \frac{H-1}{H} \cdot \frac{1}{N}
$$

其中 G 为总 GPU 数，N 为节点数。该公式表明，当 G ≤ H 时（单节点常见场景），FoE 的 All-to-All 项消失，仅保留轻量级 All-Reduce，通信量比标准 MoE 减少 k 倍。

## 实验评估

实验在 8-GPU H100 单节点与双节点 InfiniBand 配置上进行，使用 LongBench 数据集与 Poisson 到达过程模拟真实请求分布。基线为标准 EP（vLLM/SGLang 行为），未包含 MoETuner、Sem-MoE 等调度方法的端到端对比，仅在 LAR 指标上交叉比较。

| 部署模式 | 到达规模 | 架构 | TTFT (s) Mean | TBT (s) Mean | E2E (s) Mean |
|---|---|---|---|---|---|
| 单节点 | 0.5 | MoE | 3.710 | 0.780 | 202.7 |
| 单节点 | 0.5 | FoE | 1.394 | 0.566 | 145.7 |
| 单节点 | 0.75 | MoE | 3.233 | 0.841 | 217.7 |
| 单节点 | 0.75 | FoE | 1.041 | 0.458 | 117.9 |
| 多节点 | 0.5 | MoE | 3.883 | 0.736 | 191.5 |
| 多节点 | 0.5 | FoE | 1.128 | 0.543 | 139.5 |

单节点 0.75 规模下，FoE 的 TTFT 加速比达 3.11×，TBT 加速比 1.83×；多节点 0.5 规模下，TTFT 加速比从单节点的 2.66× 提升至 3.44×，表明架构优势在跨节点场景下放大。生成质量方面，7B FoE 模型在 MMLU 上取得 66.0% 准确率，与 MoE 基线的 65.0% 相当；1B 模型在 GSM8K 上取得 63.8%，略低于 MoE 的 63.9%。

FoE 的 LAR 在 EP=8 时达到 1.0，而 Sem-MoE、ExFlow、MoETuner 分别为 0.39、0.21、0.12。GPU 负载不均衡率方面，标准 MoE 平均为 1.64×，FoE 为 1.0，表明结构保证优于启发式调度。

评估边界方面，实验仅使用 LongBench 单一数据集，未覆盖多模态或代码生成任务；未报告置信区间，数值比较需谨慎；FlexServe 推理引擎声明开源但未提供具体 URL，可复现性依赖后续发布。

## 关联研究分析

从问题动机看，FoE 与 MoETuner、Sem-MoE 等调度方法解决同一通信瓶颈问题，但路线根本不同。调度方法通过预测 Token-专家亲和性优化静态分配，试图在全局 EP 组内最大化 LAR，但受限于跨节点通信的物理带宽上限；FoE 通过架构重构将通信限制在节点内，从拓扑上消除跨节点 All-to-All。这一差异源于任务特性：调度方法假设专家分布固定，仅优化分配策略；FoE 假设专家分布可重构，通过改变 KV 头与专家的绑定关系实现局部性。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

从方法设计看，FoE 与 DeepSeek-MoE 的共享专家机制同属架构级优化，但目标不同。DeepSeek-MoE 引入共享专家以减少通信开销，但保留全局路由；FoE 通过分组路由完全消除全局 All-to-All，但要求每组独立处理 KV 头。这一差异暗示：共享专家机制在保持全局路由灵活性的同时降低通信，而 FoE 以牺牲全局路由灵活性为代价换取通信拓扑的结构性优化。分组路由在任务难度差异大的场景下，是否会导致部分组专家利用率不足，论文未给出回答。

## 总结

SMoE 分布式推理的核心矛盾在于稀疏激活解耦容量与成本的同时，EP 引发的 All-to-All 通信开销随集群规模扩大而急剧增加。现有调度与系统优化方法受限于全局 EP 组的拓扑约束，无法从根本上消除跨节点通信瓶颈。FoE 通过架构级重构，将专家与 KV 头划分为独立组，将全局 All-to-All 替换为组内通信与轻量级组间 All-Reduce，在结构上保证高 LAR 与完美负载均衡。实验证明，FoE 在单节点与多节点部署中分别实现 TTFT 3.11× 与 3.44× 加速，生成质量与 MoE 基线相当。其边界在于：FoE 修改底层架构（路由、WQ 投影分区），无法直接评估现有开源 MoE 检查点，需从头预训练验证收敛性。当支持集增大到 5-shot 时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.06206)