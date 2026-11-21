# HuggingFace最新推荐论文 ｜ProRL Agent: Rollout-as-a-Service for RL Training of Multi-Turn LLM Agents ｜ProRL Agent：基于服务化架构的多轮智能体强化学习基础设施

作者：Hao Zhang、Mingjie Liu、Shaokun Zhang 等 13 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.18815)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.18815)

> 多轮智能体强化学习（Agentic RL）训练面临的核心瓶颈在于Rollout生成与策略优化在资源特性上的根本冲突：前者I/O密集且延迟不可控，后者GPU密集且需同步梯度。现有框架将二者紧耦合于同一进程，导致资源干扰与迁移困难。ProRL Agent提出“Rollout-as-a-Service”范式，通过HTTP接口将Rollout全生命周期独立为服务，实现资源隔离与模块解耦。该设计在SWE-Bench Verified上显著提升了Qwen3系列模型的性能，但其增益归因于基础设施优化还是训练框架本身，仍需更严格的对照实验验证。

## 研究背景

多轮智能体任务要求模型在代码仓库、Web浏览器或操作系统等外部环境中进行数十轮交互，每次交互涉及工具调用与环境反馈，轨迹长度可达数万Token。这种长程依赖使得Rollout生成成为训练瓶颈：单次Rollout包含大量顺序环境交互，延迟随执行结果波动剧烈，且不同任务的环境异构性要求基础设施具备高度灵活性。传统RL框架将Rollout逻辑嵌入训练循环，导致I/O密集的环境管理与GPU密集的前向/反向传播在同一进程内竞争资源，造成GPU利用率低下与长尾延迟。

Agentic RL训练基础设施的演进始于对同步RL资源闲置问题的回应。VeRL（Sheng et al., 2024）提出基于Ray的分布式框架，支持异步执行但未充分处理多轮交互中的上下文动态增长；AgentRL（Zhang et al., 2025）通过解耦环境部署与训练引擎实现全异步轨迹生成，但侧重多节点调度而非单节点资源隔离；CoPRIS（Qu et al., 2025）引入并发控制与重要性采样校正，解决Off-policy偏差但系统复杂度增加。这些方法均将Rollout作为训练栈的进程内组件，导致迁移至新训练后端时需重新实现整个Agent执行管道。ProRL Agent的切入点在于识别出Rollout与训练在资源特性上的根本差异，借鉴LLM推理引擎的“Inference-as-a-Service”理念，将Rollout独立为HTTP服务，从架构层面消除耦合带来的工程摩擦。

## 核心方法

### 方法参照系

现有Agentic RL框架的标准流程是将Rollout编排（环境初始化、工具执行、轨迹收集、评估）实现为训练循环内的进程内库。该流程的关键差异在于：ProRL Agent将Rollout视为独立服务，训练框架仅通过HTTP接口提交任务实例并接收完成轨迹，无需管理任何Rollout生命周期细节。

### 三阶段异步流水线

传统实现中，单个Worker负责完整Rollout流程（容器启动→Agent执行→结果评估），导致吞吐量受限于最慢阶段。ProRL Agent将三阶段映射至独立Worker池，实现跨任务重叠执行。容器初始化I/O密集，Agent执行受LLM推理瓶颈限制，评估耗时从毫秒级（数学题）到分钟级（完整测试套件）不等。独立队列允许初始化Worker持续拉取新任务并移交至Rollout队列，而评估Worker并行处理已完成轨迹，消除阶段间阻塞。该设计使系统吞吐量不再受单一任务最慢阶段制约，而是由各阶段Worker池的并行度共同决定。

$$
\text{Throughput} = \min_{s \in \{INIT, RUN, EVAL\}} \left( \frac{N_s}{T_s} \right)
$$

其中 $N_s$ 为阶段 $s$ 的Worker数量，$T_s$ 为平均处理时间。该公式表明，通过独立配置各阶段Worker池大小，可针对资源特性优化整体吞吐量，而非受限于最慢阶段的串行等待。

### Min-Heap负载均衡与Token级通信

LLM后端池采用Min-Heap结构存储各后端分配计数器，每次Rollout阶段发起LLM调用时，自动选择计数器最低的后端并分配整个任务。计数器按任务（而非按调用）递增，确保同一任务内所有后续调用路由至同一后端，最大化前缀缓存复用。该机制无需全局同步，仅通过单锁保护堆操作，在高并发下保持负载均衡。同时，ProRL Agent采用Token-in/Token-out通信，训练框架直接消费Token级轨迹，避免重分词漂移导致的训练不稳定。

$$
s^* = \arg\min_{s \in \mathcal{S}} w_s
$$

其中 $w_s$ 为后端 $s$ 自注册以来分配的总任务数。选择与分配计数成比例，使高流量后端优先级降低，实现类轮询平衡。该设计解决了动态注册后端时的负载不均问题，同时通过Token级通信确保轨迹数据保真度，间接提升训练稳定性。

## 实验评估

实验在SWE-Bench Verified的293实例子集上进行，使用Qwen3-4B-Instruct2507、Qwen3-8B和Qwen3-14B模型，DAPO作为默认RL算法，32张NVIDIA H100 GPU。基线对比SkyRL-v0，但缺失CoPRIS、Earl等同类系统基线，且未报告置信区间。

| 模型规模 | 模型 | 复现性能 | 报告性能 |
| :--- | :--- | :--- | :--- |
| 4B | Qwen3-4B-Instruct-2507 | 14.8 | – |
| 4B | **ProRL Agent-4B (RL)** | **21.2** | – |
| 8B | Qwen3-8B | 9.6 | – |
| 8B | SkyRL-Agent-8B-v0 | – | 9.4 |
| 8B | **ProRL Agent-8B (RL)** | **18.0** | – |
| 14B | Qwen3-14B | 15.4 | – |
| 14B | SkyRL-Agent-14B-v0 | – | 21.6 |
| 14B | **ProRL Agent-14B (RL)** | **23.6** | – |

ProRL Agent-8B在SWE-Bench Verified上达到18.0%，较SkyRL-v0的9.4%提升近2倍；14B模型达23.6%，较SkyRL-v0的21.6%提升2.0个点。4B模型从14.8%提升至21.2%，增益6.4个点。

消融实验验证了系统组件对吞吐量的影响：

| 负载均衡 | 高效Bash | 陈旧任务清理 | 动作时间(s) | GPU利用率(%) | 吞吐量(instance/sec) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ✓ | ✓ | ✓ | 0.42 | 78 | 0.37 |
| ✓ | ✓ | | 0.42 | 42 | 0.25 |
| ✓ | | | 0.78 | 68 | 0.29 |
| | | | 0.42 | 65 | 0.30 |

移除负载均衡导致GPU利用率从78%降至42%，吞吐量下降32%；移除高效Bash使动作时间从0.42秒增至0.78秒，吞吐量下降22%。负载均衡对GPU利用率的影响最大，表明Min-Heap机制对资源隔离至关重要。

评估边界存在显著局限：未报告计算效率指标（Training Throughput、Sample Efficiency）；SWE-Bench Verified仅覆盖软件工程任务，未验证Web导航、数学推理等异构环境的泛化性；代码开源但超参数配置（如KL系数 $1 \times 10^{-4}$、学习率 $1 \times 10^{-6}$）未提供完整复现脚本。

## 关联研究分析

从问题动机看，ProRL Agent与AgentRL均针对异步解耦，但AgentRL侧重多节点间任务调度，解决异构环境下的并行轨迹生成；ProRL Agent聚焦单节点内资源隔离，通过HTTP服务化实现I/O密集与GPU密集负载的物理分离。这一差异源于任务特性：AgentRL面向大规模集群部署，需协调多节点资源；ProRL Agent面向HPC共享集群，需适配Slurm调度器的无根权限约束。ProRL Agent采用Singularity而非Docker，支持Fake Root与Per-container Loopback IP，解决了HPC环境中Docker守护进程不可用的问题，这是AgentRL未覆盖的工程盲区。

从方法设计看，ProRL Agent与CoPRIS均解决Rollout长尾问题，但CoPRIS通过重要性采样校正Off-policy偏差，侧重算法稳定性；ProRL Agent通过三阶段流水线与Min-Heap负载均衡，侧重系统吞吐量。CoPRIS的并发控制机制在保持On-policy效果的同时提升Rollout吞吐量，但系统复杂度增加；ProRL Agent的HTTP服务化引入网络开销，但通过Token级通信避免重分词漂移，确保训练保真度。HTTP服务化的网络开销是否抵消资源隔离收益，论文未提供量化对比，仅通过GPU利用率提升（78% vs 42%）间接验证。

## 总结

ProRL Agent要解决的核心矛盾是Agentic RL训练中Rollout与策略优化在资源特性上的根本冲突，现有框架因紧耦合导致资源干扰与迁移困难。本文抓住的切入点是识别出Rollout的I/O密集与训练的GPU密集特性，借鉴Inference-as-a-Service范式，通过HTTP接口将Rollout独立为服务，实现资源隔离与模块解耦。该方法在SWE-Bench Verified上使Qwen3-8B性能从9.4%提升至18.0%，14B从21.6%提升至23.6%。本文的边界在于：实验仅覆盖软件工程任务，未验证异构环境泛化性；性能增益归因于基础设施优化还是ProRL训练框架本身，缺乏严格对照实验。当Rollout服务与训练算法的联合优化成为可能时，HTTP服务化的网络开销是否可通过更轻量级的IPC机制进一步降低，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.18815)