# ACL-Findings2026最新论文 ｜H-MAS: Hierarchical Multi-Agent Scheduling for Multi-Tenant LLM Serving ｜分层多智能体调度

研究机构：北京师范大学、东南大学

作者：Yuhan Liu、Cong Xu、Qi Jia 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4f086419b3f5)

> 多租户大语言模型服务（MaaS）面临非平稳负载下的服务质量（QoS）不稳定问题，现有固定策略调度器无法同时应对毫秒级突发、分钟级漂移与小时级结构变化。本文指出单一策略在时间尺度上的错配是QoS波动的根源，提出H-MAS分层多智能体调度器，通过解耦慢速策略选择与快速执行调节实现自适应控制。该架构在Azure生产轨迹上验证了Goodput提升1.2×–3.0×的有效性，但其LLM决策延迟与保形校准的泛化边界尚存疑。

## 研究背景

多租户MaaS场景中，异构请求竞争有限GPU资源，调度器需动态调整请求排序与并发度以维持QoS。Time-To-First-Token (TTFT) 与 Time-Per-Output-Token (TPOT) 是核心SLO指标，其稳定性依赖于对负载动态的实时响应。然而，实际负载呈现多时间尺度非平稳性：秒级RPS突发（峰值176 RPS，1秒阶跃140 RPS）、分钟级请求组成漂移（长请求占比波动0.1565）及小时级结构变化（长上下文占比峰值9.2%）。

传统LLM推理引擎（如vLLM、SGLang）采用固定单一策略（如FCFS），其结构刚性导致无法在负载漂移时切换调度逻辑，多尺度处理扁平化使同一决策逻辑难以兼顾突发与持久变化。强化学习（RL）虽能自适应，但黑盒特性阻碍运维信任，且泛化受限于训练分布。本文切入点在于将调度重构为分层闭环：感知层提取请求属性，反馈层聚合多尺度QoS状态，控制层解耦慢速策略选择与快速参数调节，执行层实施细粒度控制。

## 核心方法

### 分层控制空间建模

H-MAS将调度建模为随机控制问题，状态空间 $S$ 由感知、预测与QoS智能体构建，包含请求特征 $x_r$ 与系统视图 $V_{long}, V_{short}$。动作空间分为结构指令 $A_t \in \Omega$（如FCFS、EDF、Two-lane）与执行控制 $C_t = (N_{run}, B_{token}, \text{admission})$。目标函数最大化加权Goodput，仅当TTFT与TPOT同时满足SLO时计数：

$$
\max \mathbb{E} \sum_{r \in R_t^{done}} \text{Utility}(r) \cdot \mathbb{I}[\text{OK}(r)]
$$

其中 $\text{OK}(r)$ 表示 $t_r^{ttft} \leq \text{SLO}_r^{ttft} \wedge t_r^{tpot} \leq \text{SLO}_r^{tpot}$。该设计将SLO合规性转化为可优化的吞吐量指标，避免事后惩罚。

### 慢速结构自适应

Meta Controller作为慢速循环，每 $\Delta T_{meta}$ 秒基于长时视图 $V_{long}$ 选择活跃调度结构 $A_t$。其决策函数 $\Pi_{meta}(\cdot)$ 采用LLM解释工作负载漂移模式：当长请求引发队头阻塞（HOL blocking）时启用Two-lane隔离；当违规由截止期缺失驱动时切换至EDF；当存在持续不公平时采用WFQ/Stride。设计动机在于解决固定策略在结构性漂移下的失效，LLM仅用于慢速决策以规避毫秒级延迟瓶颈。若输出无效，系统回退至基于历史统计的保守策略，确保鲁棒性。

### 快速稳定性调节

Statera Agent管理执行控制空间 $D_{ctrl}$，通过两层反馈控制器维持利用率在目标区间 $[u_{low}, u_{high}]$。内环P控制器调节Token预算 $B_{token}$ 抑制瞬时抖动，外环并发控制器限制并行序列数 $N_{run}$。内存安全通过保形校准实现：基于预测长度 $\hat{l}_r^{pred}$ 与误差分布 $D_b$ 计算 $(1-\epsilon)$ 分位上界 $\hat{l}_r^{upper} = \hat{l}_r^{pred} + q_{1-\epsilon}(D_b)$，准入约束为：

$$
\sum_{r \in Q_{run}(t)} m_{KV}(\hat{l}_r^{upper}) \leq M_{cap}(1 - \delta_{frag})
$$

该机制将OOM风险转化为确定性准入围栏，解决长请求导致的内存碎片化问题。

## 实验评估

实验在8×NVIDIA A100 (80GB)集群上评估Qwen3-8B/14B/30B与Llama-3.3-70B，使用Azure、ShareGPT及Coding轨迹。基线覆盖vLLM、SGLang、LightLLM，但缺失DRL（如PPO/DQN）与启发式（First-Fit变体）对比，无法直接验证LLM慢速决策优于DRL快速适应的假设。

| 场景 | 时间尺度 | Mismatch (mean/p95) vLLM | Mismatch (mean/p95) H-MAS | TTFT合规率 vLLM | TTFT合规率 H-MAS | Goodput (norm.) vLLM | Goodput (norm.) H-MAS |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Burst | Fast | 1.560 / 3.588 | 1.203 / 2.767 | 19.24% | 81.76% | 0.2557 | 0.6831 |
| Drift | Medium | 1.835 / 2.110 | 1.415 / 1.627 | 28.96% | 88.03% | 0.2896 | 0.7199 |
| Shift | Slow | 2.202 / 5.606 | 1.798 / 4.094 | 11.25% | 60.12% | 0.1125 | 0.4357 |

消融实验显示，禁用Two-lane使ESG降至0.88×，冻结Statera使ESG降至0.23×，表明感知预测质量对下游调度高度敏感（规则替代后ESG降至0.28×）。评估边界在于：未报告置信区间，保形校准在不同模型规模下的泛化能力未验证，代码未开源。

## 关联研究分析

从问题动机看，COMLLM侧重拓扑无关的MEC卸载决策，而H-MAS聚焦多租户MaaS下的QoS稳定性。两者均利用LLM进行调度，但COMLLM将LLM作为核心决策引擎，面临毫秒级边缘卸载的延迟挑战；H-MAS将LLM限制在慢速层，通过规则/控制论主导快速调节，规避了实时性瓶颈。这一差异源于任务特性：MEC卸载需快速响应网络波动，MaaS调度可容忍秒级策略切换。

从方法设计看，vLLM通过PagedAttention解决显存碎片化，H-MAS继承其内存管理思想，但引入Two-lane隔离与保形校准进一步治理长请求导致的HOL blocking。vLLM的内存管理是静态页面分配，H-MAS的保形校准是动态统计安全机制，后者能自适应模型特定的长度不确定性。然而，H-MAS未对比vLLM的PagedAttention与保形校准在相同负载下的内存利用率差异，无法量化两种机制的相对贡献。

## 总结

H-MAS解决的核心矛盾是多时间尺度非平稳负载与固定策略调度器的错配。其切入点在于解耦慢速结构选择与快速执行调节，LLM仅用于慢速决策以规避延迟瓶颈，保形校准提供内存安全保证。实验证明在Azure轨迹上，H-MAS的TTFT合规率在Fast slice下从vLLM的19.24%提升至81.76%，Goodput提升1.2×–3.0×。边界在于缺失DRL基线对比，无法验证LLM慢速决策优于DRL快速适应的假设；保形校准的泛化能力未在不同模型规模下验证。当负载漂移速度超过 $\Delta T_{meta}$ 时，Meta Controller的响应延迟是否导致QoS退化，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_4f086419b3f5)