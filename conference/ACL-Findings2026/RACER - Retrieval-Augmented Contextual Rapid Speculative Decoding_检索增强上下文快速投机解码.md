# ACL-Findings2026最新论文 ｜RACER: Retrieval-Augmented Contextual Rapid Speculative Decoding ｜检索增强上下文快速投机解码

研究机构：武汉大学、上海交通大学

作者：Zihong Zhang、Zuchao Li、Lefei Zhang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14885)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14885)

> 投机解码旨在通过并行验证打破自回归解码的串行瓶颈，但无训练方法面临检索信号稀疏与Logits信号局部性互补失效的困境。RACER通过构建Logits Tree与Retrieval Tree双树结构，将精确模式匹配作为结构锚点，将历史Logits复用作为动态外推线索，实现了无需额外模型训练的无损加速。该方法在多个基准上稳定超越纯检索与纯Logits基线，但其加速比仍低于训练式方法，且对长上下文下的内存管理缺乏深入验证。

## 研究背景

自回归解码中，目标模型每步仅生成一个Token，导致推理延迟随序列长度线性增长。投机解码（Speculative Decoding, SD）通过草稿模型并行生成候选Token，再由目标模型一次性验证，将串行过程转化为并行验证。验证阶段需保证输出分布与目标模型严格一致，这要求草稿Token必须通过拒绝采样检验，接受长度（Mean Accepted Tokens, MAT）直接决定了加速比的上限。在无训练场景下，草稿生成不依赖独立模型，而是利用推理时已有的信号，如上下文中的重复模式或目标模型输出的Logits分布。

现有无训练SD方法分为两类：基于检索的方法（如PLD、REST）依赖精确的N-gram匹配，在代码生成等模式重复场景中有效，但在开放域文本中因匹配稀疏而失效；基于Logits的方法（如LogitSpec、TR）利用目标模型最后一步的Logits预测后续Token，但缺乏外部结构引导，预测范围狭窄且易受局部噪声干扰。两类方法单独使用时均存在显著局限：检索无法覆盖未见模式，Logits无法跨越长距离依赖。RACER的切入点在于将两者统一为互补信号，检索提供“已见信息”的结构约束，Logits提供“未见信息”的外推能力，从而在无训练约束下最大化草稿质量。

## 核心方法

### 方法参照系

无训练SD的标准流程是直接从上下文或Logits生成线性草稿序列，再由目标模型验证。本文的关键差异在于将草稿生成结构化为双树并行搜索，而非单一线性路径，并通过动态机制协调两棵树的资源分配。

### Logits Tree与Copy-Logit策略

Logits Tree负责外推未见Token，其核心创新是Copy-Logit策略。传统方法（如Last-Logit）复用当前步Logits预测下一步，假设Token空间局部平滑；但实验表明，相同Token在不同上下文中语义倾向相似，因此RACER复用最近一次出现相同Token时的Logits作为代理分布。设验证前缀为 $x_{<t}$，目标模型输出Logits $z_t = f(x_{<t})$，Copy-Logit策略定义代理分布 $\tilde{z}_{t+1} = z_{i+1}$，其中 $i < t$ 是满足 $x_i = x_t$ 的最近索引。该公式的物理含义是：利用历史相同Token的上下文Logits近似当前Token的后续分布，比复用当前Logits更准确。实验显示，Copy-Logit的MAT从Last-Logit的1.57提升至1.87，且接受Token高度集中于头部（Rank-1占比超50%），验证了其分布锐度优势。

### Retrieval Tree与LRU驱逐机制

Retrieval Tree负责捕获已见模式，其创新在于引入LRU（Least Recently Used）驱逐策略管理有限内存。传统后缀数组或自动机随上下文长度线性增长，无法丢弃过时状态；RACER将检索结构限制为固定容量（如10,000节点），当新N-gram插入导致容量溢出时，驱逐最久未使用的叶节点。设当前匹配状态为 $S$，新N-gram为 $G$，若 $G$ 不在 $S$ 中且容量已满，则移除 $S$ 中访问频率最低的叶节点 $u$，插入 $G$ 并更新访问标记。该机制确保检索树始终保留近期高频模式，避免长上下文中关键模式被稀释。在MGSM-ZH等推理任务中，重复模式提供强预测线索，LRU机制使检索组件在长序列中保持有效性，MAT较纯Logits方法提升0.7-1.3个Token。

## 实验评估

| 模型 | 方法 | Spec-Bench MAT | Spec-Bench Speedup | HumanEval MAT | HumanEval Speedup | MGSM-ZH MAT | MGSM-ZH Speedup |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Vicuna 7B | PLD | 1.71 | 1.50 | 1.58 | 1.40 | 2.57 | 2.27 |
| Vicuna 7B | REST | 1.82 | 1.77 | 2.06 | 2.17 | 1.29 | 1.06 |
| Vicuna 7B | TR | 2.34 | 2.06 | 2.22 | 2.17 | 3.55 | 2.30 |
| Vicuna 7B | RACER | 3.00 | 2.21 | 3.11 | 2.29 | 3.71 | 2.77 |
| LLaMA3.1 8B | EAGLE-3 | 3.76 | 2.51 | 4.41 | 3.06 | 1.54 | 1.06 |
| LLaMA3.1 8B | RACER | 2.82 | 2.41 | 3.22 | 2.87 | 3.33 | 2.89 |

实验覆盖Spec-Bench、HumanEval和MGSM-ZH三个基准，基线包括纯检索（PLD、REST）、纯Logits（LogitSpec、TR）及训练式方法（EAGLE-3）。RACER在Vicuna-7B上平均Speedup达2.42x，显著高于TR的2.18x和REST的1.87x；在LLaMA3.1-8B上，RACER的Speedup（2.72x）虽低于EAGLE-3（2.89x），但在MGSM-ZH上反超（2.89x vs 1.06x），表明无训练方法在中文推理任务上更具鲁棒性。

| 模型 | 方法 | Spec-Bench Speedup | HumanEval Speedup | MGSM-ZH Speedup |
| :--- | :--- | :--- | :--- | :--- |
| Vicuna 7B | w/o logits | 1.43 | 1.52 | 2.11 |
| Vicuna 7B | w/o retrieval | 2.72 | 2.68 | 2.95 |
| Vicuna 7B | RACER | 3.00 | 3.11 | 3.71 |
| Vicuna 13B | w/o logits | 1.38 | 1.43 | 1.95 |
| Vicuna 13B | w/o retrieval | 2.68 | 2.70 | 2.98 |
| Vicuna 13B | RACER | 2.95 | 3.09 | 3.64 |

消融实验显示，移除Logits组件导致Speedup下降0.78-1.04x，移除检索组件下降0.19-0.59x，证实Logits是加速主干，检索在推理任务中提供关键补充。在Spec-Bench子任务中，RACER在Translation上表现弱于TR（1.61x vs 1.84x），因检索组件对翻译任务贡献有限，甚至抵消部分Logits优势；但在Math和RAG上全面领先，验证了双树结构在模式密集任务中的有效性。

实验在NVIDIA RTX 4090（24GB）和A800（80GB）上进行，使用PyTorch 2.8.0和HuggingFace Transformers，未应用量化或专用内核优化。代码已开源，超参数（如Logits Tree最大宽度8、Retrieval Tree节点数10,000）基于初步分析确定，但未报告置信区间。评估协议限于batch_size=1，未验证高并发场景下的性能退化，且未覆盖长上下文（>1024 Token）下的内存开销。

## 关联研究分析

从问题动机看，RACER与REST同属无训练路线，但REST仅依赖后缀数组匹配，在开放域文本中因匹配稀疏导致MAT低于1.5；RACER通过Logits Tree补充未见模式，将MAT提升至3.0以上。这一差异源于任务特性：REST假设上下文存在足够长的重复N-gram，而RACER承认匹配稀疏性，转而利用Logits的外推能力。然而，RACER的Logits Tree依赖Copy-Logit策略，隐含假设相同Token在不同上下文中语义倾向稳定，这一假设在低资源语言或专业术语密集场景中是否成立，论文未给出验证。

从方法设计看，RACER与EAGLE-3同采用树状验证，但EAGLE-3依赖训练的特征对齐草稿模型，RACER则完全基于推理时信号。EAGLE-3在Spec-Bench上MAT达3.76，但Speedup仅2.51x，因草稿模型引入额外推理开销；RACER MAT较低（2.82x），但Speedup达2.41x，且无需训练。这一对比揭示训练式方法的效率瓶颈：草稿模型的前向传播成本随模型规模增长，而无训练方法的草稿生成成本近乎恒定。RACER在MGSM-ZH上超越EAGLE-3（2.89x vs 1.06x），表明训练式方法在分布外任务上易失效，而无训练方法因不依赖训练数据覆盖，更具鲁棒性。

## 总结

RACER解决的核心矛盾是无训练SD中检索信号稀疏性与Logits信号局部性的互补失效。其切入点在于将两者统一为双树结构，检索提供结构锚点，Logits提供动态外推，从而在无训练约束下最大化草稿质量。通过Copy-Logit策略和LRU驱逐机制，RACER在Vicuna-7B上实现2.42x平均Speedup，在MGSM-ZH上达2.77x，显著优于纯检索与纯Logits基线。然而，其加速比仍低于训练式方法EAGLE-3（2.89x），且实验限于batch_size=1和短上下文，未验证高并发与长序列下的性能。当上下文长度超过1024 Token时，LRU驱逐策略是否导致关键模式丢失，进而影响MAT稳定性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14885)