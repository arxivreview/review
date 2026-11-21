# HuggingFace最新推荐论文 ｜Agentic Discovery of Neural Architectures: AIRA-Compose and AIRA-Design ｜智能体驱动的神经架构搜索：AIRA-Compose 与 AIRA-Design

作者：Alberto Pepe、Chien-Yu Lin、Despoina Magka 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.15871)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.15871)

> 高效大语言模型架构研究旨在突破 Transformer 自注意力机制的二次方计算复杂度与内存瓶颈，但混合架构（Transformer + SSM/Linear Attention）的设计空间呈组合爆炸，人工探索极易遗漏非平凡配置。现有神经架构搜索（NAS）方法受限于固定搜索空间或优化目标，难以发现全新计算原语。本文提出 AIRA-Compose 与 AIRA-Design 双框架，将 LLM 智能体部署为架构搜索与代码生成的执行者，在 1B 规模下发现优于 Llama 3.2 的混合架构。该工作验证了智能体在架构发现上的有效性，但其发现的新颖性是否超越搜索广度，仍存疑。

## 研究背景

当模型规模向千亿级扩展时，Softmax 注意力的 $O(N^2)$ 复杂度与键值缓存（KV Cache）的线性内存增长成为部署瓶颈。为缓解此问题，状态空间模型（SSM）如 Mamba 提供了线性复杂度推理，但其在长程精确检索任务上表现不及 Softmax 注意力。这种性能差距促使研究者转向混合架构，将注意力层与 SSM 层以特定模式交织，以平衡效率与精度。然而，混合架构的设计空间随原语种类与排列方式呈组合爆炸，人工试错难以覆盖所有潜在高效配置。

传统 NAS 方法通过梯度优化或贝叶斯搜索在预定义空间内寻找最优结构，但受限于搜索空间的刚性，无法生成全新计算原语。同时，LLM 智能体在代码生成与迭代调试上的能力，为突破固定搜索空间提供了新路径。本文切入点在于将 NAS 重构为智能体任务：AIRA-Compose 在预定义原语（Attention, MLP, Mamba2）中搜索最优排列，AIRA-Design 则要求智能体从零实现新注意力机制。这一转变将架构设计从“优化问题”推向“开放式代码生成”，旨在发现人类直觉难以触及的非平凡架构组合。

## 核心方法

### 方法参照系

本文问题属于神经架构搜索（NAS）范畴，但与传统 NAS 的关键差异在于执行主体与搜索机制。传统 NAS 依赖固定优化算法在参数化空间内搜索，而本文采用 LLM 智能体作为搜索代理，通过 AIRA-dojo 框架执行树状探索。智能体不仅评估架构，还自主调试代码、修改超参数，甚至引入文献知识优化训练策略，突破了传统 NAS 的被动搜索模式。

### AIRA-Compose：原语排列搜索

AIRA-Compose 在预定义原语池中搜索 16 层架构的最优排列。智能体通过 Draft、Improve、Debug 算子迭代生成候选架构，并在小规模（百万参数）上评估验证损失。设计动机在于解决人工设计混合架构时易陷入局部最优的问题，通过智能体的假设驱动探索覆盖更广的设计空间。架构评估采用交叉熵损失与下游任务准确率，最优架构外推至 350M、1B、3B 规模。该流程的核心公式为验证损失最小化：

$$ \mathcal{L}_{val} = -\frac{1}{N} \sum_{i=1}^{N} \log p(y_i | x_i; \theta_{arch}) $$

其中 $\theta_{arch}$ 为架构参数，$p(y_i | x_i; \theta_{arch})$ 为模型预测概率。智能体通过最小化 $\mathcal{L}_{val}$ 筛选架构，确保小规模评估与大规模性能的关联性。

### AIRA-Design：机制实现与训练优化

AIRA-Design 要求智能体从零实现新注意力机制（LRA 任务）或优化训练脚本（Autoresearch 任务）。设计动机在于突破预定义原语的局限，探索全新计算原语的可能性。智能体通过代码生成实现子二次方复杂度注意力，并在固定 GPU 预算内训练。对于 Autoresearch 任务，智能体优化 GPT 训练脚本以最小化验证比特每字节（BPB）。关键公式为 BPB 计算：

$$ \text{BPB} = \frac{1}{T} \sum_{t=1}^{T} \log_2 p(x_t | x_{<t}; \theta_{train}) $$

其中 $T$ 为序列长度，$p(x_t | x_{<t}; \theta_{train})$ 为自回归预测概率。智能体通过调整学习率、批次大小、损失函数（如引入 focal loss）等超参数，迭代降低 BPB，实现训练效率的自主优化。

## 实验评估

实验在 DCLM、BabiStories、MAD 数据集上评估 AIRA-Compose，在 LRA 与 Autoresearch 基准上评估 AIRA-Design。基线覆盖 Llama 3.2、Nemotron-2、Composer-found 模型，但缺失纯 SSM 基线（如 Mamba 单独）与最新稀疏注意力方法（如 ProxyAttn）。

| 模型 | 验证损失 | 6任务平均准确率 (%) | DCLM Core 分数 (%) |
| :--- | :--- | :--- | :--- |
| Llama 3.2 | 2.815 | 58.4 | 46.9 |
| AIRAformer-D (Str.) | 2.734 | 60.8 | 48.9 |
| AIRAhybrid-D (Str.) | 2.719 | 62.2 | 49.3 |

AIRAformer-D 与 AIRAhybrid-D 在验证损失与下游任务上均优于 Llama 3.2，其中 AIRAhybrid-D 的 DCLM Core 分数提升 2.4%。LRA 任务中，智能体设计的架构在文档匹配与文本分类上达到人类 SOTA 的 82% 与 91%，差距分别为 2.3 与 2.6 个百分点。Autoresearch 任务中，Greedy Opus 4.5 实现 0.968 验证 BPB，超越 Karpathy 参考值 1.012。

消融实验显示，引入文献知识显著改变优化策略：Opus 4.5 +Literature 通过引入 focal loss 实现单步最大改进（$\Delta=0.036$），而 Opus 4.6 +Literature 通过渐进调整深度与批次大小获得稳定收益。这表明文献访问引导智能体采用定性不同的优化路径，而非仅增加搜索步数。

评估边界方面，LRA 任务中智能体最佳准确率（0.79）低于 Gemini 3 Pro 的 SOTA（0.88），差距可能源于搜索步数不足或架构表达力上限。可复现性受限于 24 小时 GPU 预算与 10-20 个随机种子，未报告置信区间。代码未公开，但 AIRS-Bench 任务结构标准化，便于复现评估流程。

## 关联研究分析

从问题动机看，本文与 Composer 框架共享“小规模搜索-大规模外推”范式，但差异在于执行主体。Composer 依赖优化算法在固定空间内搜索，而本文采用 LLM 智能体，其“创造性”可能源于搜索广度与代码生成能力，而非真正的架构洞察。智能体在 LRA 上的差距是否源于搜索步数不足，还是架构表达力上限，论文未给出回答。

从方法设计看，本文与 LLM-driven NAS（如 Khalid et al., 2026）同属智能体驱动搜索，但本文聚焦基础模型架构，而后者侧重高效神经架构。本文引入文献增强机制，使智能体优化策略从“盲目搜索”转向“知识引导”，这与传统 NAS 的无先验搜索形成对比。然而，文献访问是否导致过拟合特定优化模式，论文未充分验证。

## 总结

本文核心矛盾在于混合架构设计空间的组合爆炸与人工探索的局限性。切入点在于将 NAS 重构为智能体任务，利用 LLM 的代码生成与迭代调试能力突破固定搜索空间。方法上，AIRA-Compose 搜索原语排列，AIRA-Design 实现新机制，两者互补。实验证明，智能体发现的架构在 1B 规模下优于 Llama 3.2（验证损失 2.719 vs 2.815），并在 Autoresearch 任务中超越参考值（BPB 0.968 vs 1.012）。边界在于 LRA 任务中智能体最佳准确率（0.79）仍低于人类 SOTA（0.88），且未验证智能体在 >3B 规模预训练中的可扩展性。当支持集增大到 3B 参数时，智能体发现的架构是否仍能保持 isoFLOP 缩放优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.15871)