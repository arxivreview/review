# ICLR2026最新论文 ｜From Large to Small: Transferring CUDA Optimization Expertise via Reasoning Graph ｜基于推理图与蒙特卡洛图搜索的小模型CUDA代码生成

研究机构：中国科学院、中国科学院大学

作者：Junfeng Gong、Zhiyi Wei、Junying Chen 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.19873)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.19873)

> 本文旨在解决小语言模型（SLM）在复杂CUDA代码生成中因多步推理能力不足导致的性能瓶颈。现有微调与检索增强生成（RAG）方法仅能补充上下文知识，无法直接提升SLM的逻辑推理深度，导致其在高难度并行优化任务上表现远逊于大语言模型（LLM）。ReGraphT通过离线提取LLM的优化轨迹构建CUDA推理图，并利用蒙特卡洛图搜索（MCGS）引导SLM进行状态转移，实现了推理能力的非参数化迁移。该方法在CUDAEval基准上显著缩小了SLM与LLM的性能差距，但其效果高度依赖离线构建的推理图质量，且未验证在动态或未知优化场景下的泛化能力。

## 研究背景

CUDA编程的核心难点在于将串行逻辑转化为高效并行内核，这要求开发者掌握内存合并、共享内存使用等复杂优化技术。大语言模型（LLM）虽能生成高质量CUDA代码，但本地部署算力成本高昂，云端调用则存在代码泄露风险。小语言模型（SLM）因轻量化和隐私友好成为替代方案，但其在需要多步逻辑推理的复杂优化任务上表现不佳。

现有提升SLM性能的主流路线包括监督微调（SFT）和检索增强生成（RAG）。SFT通过领域数据微调可提升基础能力，但难以增强多步推理能力且泛化性差；RAG通过注入外部知识丰富上下文，但无法直接改善模型的逻辑推理机制。这两种方法在处理需要长程依赖和复杂状态转移的CUDA优化任务时均存在瓶颈，导致SLM在复杂基准上的性能显著低于LLM。

ReGraphT的切入点在于将LLM的推理能力外化为结构化知识，而非试图通过参数更新内化到SLM中。该框架利用LLM提取CUDA优化轨迹，构建包含优化技术节点与状态转移边的推理图，并通过图搜索算法引导SLM在图中进行决策，从而在不增加SLM训练成本的前提下，赋予其接近LLM的多步推理能力。

## 核心方法

### 方法参照系

本文问题属于推理时计算扩展（Inference-Time Scaling）范畴，旨在通过增加推理阶段的计算开销提升生成质量。标准流程通常采用链式思维（CoT）或最佳N选（Best-of-N）策略，但CoT受限于SLM自身的推理深度，Best-of-N则缺乏对中间状态的引导。本文的关键差异在于引入离线构建的结构化推理图作为先验知识，将生成过程建模为图上的状态转移搜索，而非单纯的序列生成。

### CUDA推理图构建

设计动机在于解决SLM无法自主生成完整优化路径的问题。ReGraphT首先利用LLM对串行代码进行逐步优化，提取包含优化方法、代码片段及推理过程的轨迹。由于LLM输出的随机性，相同优化方法可能有不同表述，系统通过重标记（relabel）机制统一优化方法表示。随后，轨迹被合并为有向图 $G=(V, E)$，其中节点 $v \in V$ 代表特定的CUDA优化技术（如循环展开、内存合并），边 $u \in E$ 代表优化技术的状态转移关系。

$$
G = (V, E), \quad v \in V \text{ denotes optimization technique}, \quad u \in E \text{ denotes transition}
$$

该公式定义了推理图的拓扑结构，将离散的优化步骤转化为可遍历的状态空间。通过合并多条LLM轨迹，ReGraphT捕获了不同优化路径的共性，形成了覆盖多种优化组合的知识图谱，为后续搜索提供了结构化的先验约束。

### 蒙特卡洛图搜索（MCGS）

设计动机在于解决枚举搜索在复杂优化组合下时间复杂度 $O(n^k)$ 过高的问题。ReGraphT将CUDA优化建模为图上的状态转移过程，并引入MCGS进行引导式探索。MCGS结合了蒙特卡洛树搜索（MCTS）的探索-利用平衡机制与图结构的循环特性。在Rollout阶段，为避免图循环导致模拟不终止，引入了基于访问次数的正则化项：

$$
\epsilon_t = \frac{1}{1 + \log(1 + N_t)}
$$

其中 $N_t$ 为当前节点的访问次数。该公式动态调整探索率，随着节点访问次数增加，探索率降低，从而在早期阶段充分探索新路径，后期阶段聚焦于高价值路径。Rollout过程中，每一步生成的CUDA代码需通过编译验证、功能验证及性能基准测试，形成层级奖励信号，驱动搜索向高性能解收敛。

## 实验评估

实验在单张A100-80GB GPU上进行，使用vLLM部署模型。基线包括标准提示、CoT、RAG及微调模型HPC-Coder-V2。主实验结果显示，ReGraphT-MCGS在CUDAEval基准上表现最优。

| 模型 | 方法 | CUDAEval pass@1 | CUDAEval speedup@1 | ParEval pass@1 | ParEval speedup@1 |
|---|---|---|---|---|---|
| DeepSeek-Coder-V2-Lite | Standard | 61.7 | 6.54 | 40.0 | 4.61 |
| DeepSeek-Coder-V2-Lite | CoT | 63.9 | 6.76 | 42.1 | 4.82 |
| DeepSeek-Coder-V2-Lite | RAG | 64.9 | 7.23 | 43.3 | 4.94 |
| DeepSeek-Coder-V2-Lite | ReGraphT | 68.1 | 7.86 | 48.3 | 5.35 |
| DeepSeek-Coder-V2-Lite | ReGraphT-MCGS | 73.2 | 13.02 | 51.7 | 10.06 |
| HPC-Coder-V2 | ReGraphT-MCGS | 72.5 | 14.39 | 53.3 | 10.61 |

ReGraphT-MCGS在CUDAEval上的pass@1达到73.2%，较Standard基线提升11.5个百分点，speedup@1达到13.02，较Standard提升近一倍。在更具挑战性的ParEval基准上，ReGraphT-MCGS的pass@1为51.7%，speedup@1为10.06，同样显著优于基线。

消融实验表明，MCGS策略在固定搜索预算下优于纯ReGraphT。在CUDAEval上，ReGraphT-MCGS较ReGraphT平均提升2.2% pass@n和1.33% speedup@n。难度分层分析显示，在Easy级别任务上，ReGraphT与CoT/RAG无显著差异；但在Medium和Hard级别，ReGraphT的优势显著扩大，Hard级别pass@1达到54.9%，较Standard提升10.8个百分点。这表明推理图对复杂多步推理任务的增强效果更为明显。

评估边界方面，CUDAEval基于真实CUDA文件构建，包含313个任务，按推理轨迹长度分为Easy/Medium/Hard三级。ParEval仅包含60个CUDA实例，规模较小。实验未报告置信区间，且ReGraph构建依赖LLM质量，若LLM轨迹存在错误，可能误导图搜索。代码已开源，但ReGraph构建过程未提供自动化在线更新机制。

## 关联研究分析

从问题动机看，ReGraphT与HPC-Coder-V2代表了两种不同的SLM增强路线。HPC-Coder-V2通过高质量合成数据微调，试图将领域知识内化到模型参数中，但受限于SFT在提升多步推理能力上的固有缺陷，其在复杂任务上的泛化性较差。ReGraphT则采用外部知识注入策略，通过推理图将LLM的推理能力“蒸馏”为结构化先验，避免了参数更新的成本，但引入了对离线构建图质量的依赖。这种差异源于任务特性：CUDA优化涉及多步非线性依赖，参数微调难以捕捉复杂的组合逻辑，而结构化图能显式编码这些依赖关系。

从方法设计看，ReGraphT与RAG方法（如EVOR）的关键区别在于知识表示形式。RAG通过向量检索注入非结构化文本，仅丰富上下文，不改变模型的推理机制；ReGraphT通过图结构注入结构化推理路径，直接干预模型的决策过程。MCGS的引入使得搜索过程具有全局视野，能够评估不同优化组合的长期收益，而RAG缺乏这种前瞻能力。然而，ReGraphT的图结构是静态的，无法适应动态变化的优化需求，而RAG可通过更新索引库实现动态知识注入。这种静态图与动态检索的权衡，在需要实时适应新优化技术的场景中可能成为瓶颈。

## 总结

ReGraphT旨在解决SLM在复杂CUDA代码生成中因推理能力不足导致的性能瓶颈。现有微调与RAG方法无法直接提升SLM的多步推理深度，而ReGraphT通过构建CUDA推理图并引入MCGS，将LLM的推理能力外化为结构化先验，实现了非参数化的推理迁移。实验表明，该方法在CUDAEval上使SLM的pass@1达到73.2%，speedup@1达到13.02，显著缩小了与LLM的差距。然而，ReGraphT的效果高度依赖离线构建的推理图质量，且图结构是静态的，无法适应动态优化需求。当面对未包含在推理图中的新型优化技术或动态变化的硬件架构时，ReGraphT的泛化能力是否依然有效，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.19873)