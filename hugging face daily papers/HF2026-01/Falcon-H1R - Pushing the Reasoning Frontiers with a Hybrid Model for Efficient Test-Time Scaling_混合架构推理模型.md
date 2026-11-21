# HuggingFace最新推荐论文 ｜Falcon-H1R: Pushing the Reasoning Frontiers with a Hybrid Model for Efficient Test-Time Scaling ｜混合架构推理模型

作者：Falcon LLM Team、Iheb Chaabane、Puneesh Khanna 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.02346)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.02346)

> 测试时扩展（Test-Time Scaling, TTS）旨在通过增加推理阶段算力提升复杂任务准确率，但并行采样带来的高内存占用与延迟瓶颈限制了其在长序列场景下的实际部署。现有纯Transformer架构在大规模并行生成时面临KV Cache激增问题，导致算力效率与准确率难以兼得。本文切入点在于利用混合Transformer-Mamba架构的高吞吐特性，结合置信度动态剪枝策略，在相同算力预算下容纳更多并行推理链。该方案证明了小参数模型在TTS效率-准确率帕累托前沿上的优势，但其绝对准确率在部分开放域任务上仍落后于更大规模模型，且架构泛化性证据有限。

## 研究背景

当大语言模型执行复杂推理时，并行生成多条思维链（Chain-of-Thought, CoT）并聚合结果能显著提升准确率，但这一过程对硬件资源提出严苛要求。纯Transformer架构在处理长序列时，KV Cache内存随序列长度线性增长，导致高批量并行推理时吞吐量急剧下降。这种内存瓶颈使得模型无法在固定算力预算内生成足够多的候选路径，限制了TTS的效果上限。

TTS领域的主流路线分为算法优化与系统优化两类。算法路线如Self-Consistency和Best-of-Majority聚焦于聚合策略，但受限于骨干模型的推理速度；系统路线如Prefix Sliding通过修改注意力机制降低内存占用，但可能牺牲推理质量。当前研究缺乏一种既能保持推理能力又具备高吞吐特性的骨干架构，使得TTS在大规模并行场景下难以实现成本效率最大化。

Falcon-H1R针对这一缺口，采用混合Transformer-Mamba架构作为骨干，利用Mamba状态空间模型（State Space Model, SSM）的恒定内存特性解决长序列瓶颈。该架构在保持推理能力的同时，支持更高批量并行生成，为TTS提供了更高效的硬件基础。

## 核心方法

### 混合架构参照系

本文问题属于TTS系统效率优化范畴，与纯算法TTS方法的关键差异在于：不改变推理策略本身，而是通过架构级优化提升单位算力下的并行推理容量。标准TTS流程中，模型生成K条推理链后聚合答案，瓶颈通常在于生成阶段的内存与延迟，而非聚合逻辑。

### 混合Transformer-Mamba架构

传统Transformer在长序列推理时，KV Cache大小与序列长度成正比，导致高批量并行时内存溢出。Falcon-H1R采用并行混合架构，其中Mamba层以恒定内存处理序列依赖，Transformer层保留局部注意力能力。该设计使得模型在生成48K token长推理链时，内存占用不随序列长度线性增长，从而支持更大批量并行。架构优势直接转化为TTS效率：在相同算力预算下，可生成更多候选路径，提升聚合后的准确率上限。

### 置信度动态剪枝策略

固定预算TTS方法对所有推理链分配相同计算资源，导致简单问题过度思考、复杂问题资源不足。DeepConf方法通过实时监测模型置信度，动态终止低质量推理链。本文采用该策略，设置初始16条链确定置信度阈值$s$，后续496条链在置信度低于$s$时提前停止。该机制将计算资源集中到高潜力路径，减少无效token生成。实验显示，Falcon-H1R在AIME25上生成89.8M tokens达到96.7%准确率，而DeepSeek-R1-0528-Qwen3-8B需145.5M tokens达到82.8%准确率，token效率提升38%。

## 实验评估

实验覆盖数学（AIME24/25, HMMT25, AMO-Bench, MATH500）、代码（LiveCodeBench v6, SciCode）和通用推理（GPQA-Diamond, MMLU-Pro）基准。基线包括Qwen3-8B/32B、DeepSeek-R1-0528-Qwen3-8B、Phi-4-Reasoning-Plus-14B、GPT-OSS-20B等SOTA模型，但缺乏纯算法TTS方法（如BoM、Logit Averaging）的直接对比，无法分离架构贡献与算法贡献。

| 基准 | Falcon-H1R-7B | DeepSeek-R1-0528-Qwen3-8B | Qwen3-32B | GPT-OSS-20B |
|---|---|---|---|---|
| AIME24 Acc. (%) | 88.1 | 83.3 | 79.4 | 83.3 |
| AIME25 Acc. (%) | 83.1 | 75.8 | 71.0 | 84.4 |
| HMMT25 Acc. (%) | 64.9 | 54.3 | 49.8 | 64.8 |
| AMO-Bench Acc. (%) | 36.3 | 23.3 | 21.3 | 26.0 |
| MATH500 Acc. (%) | 97.4 | 96.8 | 96.8 | 94.8 |
| LiveCodeBench v6 Acc. (%) | 68.6 | 57.2 | 61.0 | 72.0 |
| GPQA-Diamond Acc. (%) | 61.3 | 61.4 | 67.3 | 61.2 |

Falcon-H1R-7B在数学基准上全面领先，AIME24达88.1%、AMO-Bench达36.3%，超越2-7倍参数规模的模型。但在代码和通用推理任务上表现相对较弱，LiveCodeBench v6为68.6%（低于GPT-OSS-20B的72.0%），GPQA-Diamond为61.3%（低于Qwen3-32B的67.3%）。

TTS效率评估显示，Falcon-H1R在DeepConf@512设置下，AIME25生成89.8M tokens达到96.7%准确率，GPQA-Diamond生成452.3M tokens达到70.2%准确率。相比DeepSeek-R1-0528-Qwen3-8B（174.5M tokens, 82.8%）和Qwen3-32B（174.8M tokens, 86.7%），Falcon-H1R在AIME25上token效率提升约48%，但准确率略低。消融实验表明，SFT阶段贡献了大部分推理能力增益，RL阶段主要优化输出质量而非扩展可解问题范围。

评估协议存在局限：未报告置信区间，多数论文未区分训练成本与推理成本；GPQA-Diamond差距可能源于骨干能力而非TTS策略；混合架构在开放域任务上的泛化性证据不足。代码已开源，但训练细节（如数据过滤标准）未完全披露，可复现性受限。

## 关联研究分析

从问题动机看，Falcon-H1R与Prefix Sliding均针对长序列推理效率，但前者通过架构替换（Mamba层）实现恒定内存，后者通过修改注意力机制（滑动窗口）降低计算复杂度。架构级优化可能更彻底地解决内存瓶颈，但牺牲了Transformer的全局注意力能力，这在需要长程依赖的开放域任务上可能成为劣势。论文未提供混合架构与纯Transformer在相同TTS策略下的直接对比，无法量化架构贡献。

从方法设计看，Falcon-H1R与SCALE在自适应计算分配上形成互补：SCALE通过难度评估器动态调整推理深度，Falcon-H1R通过架构支持更大并行度间接实现更细粒度分配。前者依赖外部评估器，引入额外开销；后者依赖模型自身置信度，但置信度校准质量直接影响剪枝效果。论文未验证置信度校准在不同任务难度下的稳定性，当模型对简单问题过度自信时，剪枝策略可能失效。

## 总结

Falcon-H1R要解决的核心矛盾是TTS中算力效率与准确率的权衡，现有纯Transformer架构在大规模并行推理时面临内存瓶颈，限制了单位算力下的候选路径数量。本文切入点在于利用混合Transformer-Mamba架构的恒定内存特性，结合置信度动态剪枝，在相同算力预算下生成更多有效推理链。实验证明，Falcon-H1R-7B在AIME24达88.1%、AMO-Bench达36.3%，超越2-7倍参数规模模型，且在AIME25上token效率提升38%。但论文边界在于：代码和通用推理任务上准确率落后于更大模型，混合架构在开放域任务上的泛化性未充分验证，且缺乏与纯算法TTS方法的直接对比。当模型在简单问题上置信度校准失准时，动态剪枝策略是否仍能保持效率优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.02346)