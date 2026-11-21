# HuggingFace最新推荐论文 ｜Depth-adaptive Inference of Looped Language Models via Continuous Depth Batching ｜连续深度批处理

研究机构：德国慕尼黑工业大学、英国帝国理工学院

作者：Kristian Schwethelm、Daniel Rueckert、Georgios Kaissis

论文原文见 [arXiv](https://arxiv.org/abs/2608.09444)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.09444)

> 循环语言模型（Looped LM）通过迭代共享层实现深度自适应推理，但Token在循环内动态退出破坏了标准批处理的统一前向传播假设，导致现有推理框架无法高效调度。本文切入点在于将调度粒度从Token级细化至循环迭代级，提出连续深度批处理（CDB）机制，通过队列化调度、深度感知KV缓存与异步执行解决阶段异质性与关键路径阻塞问题。CDB在Ouro 1.4B与Huginn 3.5B上实现了理论最大加速的99%，但其在通用非循环架构上的泛化能力与长期语义一致性仍存疑。

## 研究背景

循环语言模型将Transformer层划分为预lude、recurrent core与coda三部分，其中recurrent core可迭代可变次数以精炼潜在表示。这种架构允许“简单”Token提前退出循环以节省计算，但导致同一批次内不同Token遵循不同的计算路径。标准连续批处理（Continuous Batching, CB）仅在Token边界进行调度，假设每个前向传播是原子操作，无法处理循环内部分Token已退出而其他Token仍在迭代的情况。此外，早期退出导致KV缓存出现空洞，标准按层索引的缓存布局无法支持这种深度不一致的状态。

现有深度自适应方法主要分为学习式退出门与无训练式收敛检测，但均聚焦于模型架构设计，忽视推理服务端的调度挑战。Bae et al. (2025a) 提出了连续深度批处理的概念，但未实现端到端系统，忽略了预填充、调度与KV缓存更新等关键工程细节。主流推理框架如vLLM基于PagedAttention管理内存，但其调度逻辑仍绑定于固定深度的前向传播，无法适配循环架构的动态特性。本文旨在解决循环LM推理中的调度与内存一致性问题，填补从理论概念到实际系统实现的空白。

## 核心方法

### 方法参照系

标准LLM推理采用Token级连续批处理，每个解码步骤生成一个Token，批次在请求完成时更新。本文问题与该通用流程的关键差异在于：循环LM的解码过程包含多个内部迭代步骤，Token可能在任意迭代后退出，导致批次内计算路径异质化，需引入循环迭代级调度机制。

### 队列化解码调度器

传统CB调度器将前向传播视为单一单元，无法处理循环内部分Token退出的情况。CDB将解码路径分解为四个独立队列：预填充、prelude、recurrent core与coda。调度器在每个tick选择一个队列，批量处理其中的Token，实现阶段解耦。在refill模式下，退出Token释放的recurrent core槽位可立即被新Token填充，维持高批次大小。该设计解决了阶段异质性问题，允许不同阶段以不同频率与批次大小执行。

$$
\text{Scheduler}(t) = \arg\max_{q \in \{Q_{prefill}, Q_{prelude}, Q_{core}, Q_{coda}\}} \text{Priority}(q, t)
$$

该公式表示调度器在每个时间步$t$根据优先级规则选择执行队列，其中优先级由队列类型、KV缓存限制与批次大小共同决定。

### 深度感知KV缓存与异步执行

早期退出导致KV缓存中对应深度槽位为空，标准布局无法处理。CDB提出两种深度感知布局：last-exited cache将最后状态复制到跳过步骤的槽位，shared cache则每层仅保留一个KV槽位，每次迭代覆盖更新。shared cache节省$r_{max}$倍内存，但改变注意力语义。为解决CPU调度与GPU执行间的同步开销，CDB引入lookahead gate，提前一个循环步骤做出退出决策，使CPU可并行准备下一批次。

$$
t(N_c, N_b) = \delta + \gamma N_b + \alpha N_c
$$

该roofline模型估计recurrent step延迟，其中$\delta$为权重重载固定成本，$\gamma N_b$为核心计算成本，$\alpha N_c$为KV缓存流式成本。该模型识别出内存受限与计算受限的批次大小阈值$B^*$，指导refill模式的最优应用区间。

## 实验评估

实验在Ouro 1.4B与Huginn 3.5B两个循环LM架构上进行，评估离线吞吐量与在线服务延迟。基线包括固定深度解码与no-refill模式，未对比主流非循环LLM（如LLaMA）或Sarathi-Serve等阶段解耦方法，限制了跨架构性能比较。

| 模型 | 模式 | 离线吞吐量提升 | 在线归一化延迟降低 |
| --- | --- | --- | --- |
| Ouro 1.4B | Refill | 1.5–1.9× | 45–90% |
| Huginn 3.5B | Refill | 1.5–1.9× | 45–90% |

CDB实现了理论最大加速的99%，表明调度开销已最小化。消融实验显示，lookahead gate将GPU空闲时间从40.0%降至0.67%，其中静态形状减少28.9个百分点，lookahead gate进一步减少10.4个百分点。shared cache相比last-exited cache节省$r_{max}$倍内存，但可能影响长文本一致性，论文未量化此影响。

评估边界在于：实验仅覆盖两个特定循环架构，未验证CDB在通用Transformer上的适用性；未报告置信区间，数值比较需谨慎；代码未公开，可复现性受限。

## 关联研究分析

从问题动机看，CDB与Sarathi-Serve均解决阶段干扰问题，但Sarathi针对预填充与解码阶段的资源冲突，通过分块预填充与无停顿调度实现；CDB则针对循环架构内部prelude/core/coda的阶段异质性，通过队列化调度实现。差异根源在于任务特性：Sarathi处理的是固定深度Transformer的阶段间冲突，CDB处理的是动态深度循环模型阶段内冲突。CDB的lookahead gate机制在Sarathi中无对应物，因为Sarathi的调度决策不依赖循环内动态退出信号。

从方法设计看，CDB与Mixture-of-Depths（MoD）均实现深度自适应，但MoD路由固定子集Token通过每个循环步骤，Token深度依赖于序列中其他Token；CDB逐Token动态退出，深度仅依赖于自身退出信号。MoD的固定子集路由导致批次大小恒定，CDB的refill模式允许批次大小动态变化。CDB的shared cache布局改变了注意力语义，而MoD保持标准注意力，这可能导致CDB在长文本任务中精度下降，论文未提供相关消融实验。

## 总结

循环语言模型深度自适应推理的核心矛盾在于Token级动态退出与批处理统一前向传播假设的冲突。现有方法聚焦模型架构设计，忽视推理服务端调度挑战，导致理论加速无法转化为实际吞吐提升。CDB通过将调度粒度细化至循环迭代级，结合队列化调度、深度感知KV缓存与异步执行，解决了阶段异质性与关键路径阻塞问题。实验证明CDB在Ouro 1.4B与Huginn 3.5B上实现了理论最大加速的99%，离线吞吐量提升1.5–1.9×。其边界在于仅验证于特定循环架构，未评估shared cache对长文本一致性的影响，且缺乏与非循环LLM的跨架构对比。当支持集增大或上下文长度超过$B^*$阈值时，refill模式的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.09444)