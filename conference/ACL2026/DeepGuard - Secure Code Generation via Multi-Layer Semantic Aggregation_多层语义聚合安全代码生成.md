# ACL2026最新论文 ｜DeepGuard: Secure Code Generation via Multi-Layer Semantic Aggregation ｜多层语义聚合安全代码生成

研究机构：重庆大学、北京大学

作者：Li Huang、Zhongxin Liu、Yifan Wu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.09089)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.09089)

> 现有安全对齐方法依赖最终层隐藏状态作为监督信号，但漏洞判别线索在Transformer深层中衰减，导致模型难以区分安全与脆弱代码。DEEPGUARD通过注意力机制聚合顶部多层表示，构建更敏感的安全分析器，并结合多目标训练与推理时偏置引导。该方法在五个代码大语言模型上将安全且正确的生成率平均提升11.9%，但仅验证了特定基准下的泛化性，未覆盖动态执行验证场景。

## 研究背景

代码大语言模型（Code LLM）在生成功能正确代码的同时，会复现训练数据中的不安全模式，如SQL注入或缓冲区溢出。Pearce等人（2025）发现Copilot生成的代码中约40%包含可利用漏洞，而开发者往往无法识别这些缺陷。安全对齐旨在通过模型适配消除这些漏洞，但主流方法如SVEN（He and Vechev, 2023）和SafeCoder（He et al., 2024）均依赖最终层隐藏状态作为训练信号。最终层表示主要优化下一词预测，而非细粒度漏洞判别，导致安全线索在输出层附近变得不可分。本文通过逐层线性探测证实，漏洞信号在中间至上层达到峰值，但在最终层显著衰减，这一“最终层瓶颈”限制了现有方法的安全增强能力。

## 核心方法

### 方法参照系

安全对齐的标准流程是通过参数高效微调（PEFT）更新模型，利用安全-功能配对数据优化生成行为。SVEN等基线方法仅使用最终层隐藏状态计算安全损失，忽略了Transformer内部表示的层次性：浅层捕获语法结构，深层编码抽象语义。本文的关键差异在于，安全判别需要整合跨层分布的线索，而非单一层的“点”表示。

### 多层注意力聚合

传统方法将最终层隐藏状态 $\mathbf{H}_L$ 直接输入安全分析器，但漏洞线索分散在顶部 $N$ 层。DEEPGUARD引入注意力聚合模块，对顶部 $N$ 层的隐藏状态 $\mathbf{H}_{\text{top-}N} = \{\mathbf{H}_{L-N+1}, \dots, \mathbf{H}_L\}$ 进行动态融合。对于每个token位置 $j$，计算堆叠状态 $\mathbf{h}_j = [\mathbf{h}_{L-N+1}^{(j)}, \dots, \mathbf{h}_L^{(j)}]^\top$，并以均值 $\bar{\mathbf{h}}_j$ 作为查询，通过注意力机制加权各层视图：

$$
\mathbf{h}_{\text{agg}}^{(j)} = \text{Attention}(\bar{\mathbf{h}}_j W_Q, \mathbf{h}_j W_K, \mathbf{h}_j W_V)
$$

该公式的物理含义是，均值提供跨层“共识”摘要，注意力则赋予对安全判别最 informative 的层更高权重。这一设计解决了最终层信号衰减问题，使安全分析器能捕获分布在多层中的安全关键线索，从而提升漏洞判别精度。

### 多目标训练与引导推理

聚合表示驱动安全分析器 $f_{\text{sa}}$，计算token级安全分数 $s_i(x)$。训练目标包含三项：安全对比损失 $\mathcal{L}_{\text{sec}}$ 鼓励安全变体得分高于脆弱变体，KL散度 $\mathcal{L}_{\text{kl}}$ 防止灾难性遗忘，生成损失 $\mathcal{L}_{\text{gen}}$ 保持流畅性。总损失为：

$$
\mathcal{L} = w_{\text{sec}} \mathcal{L}_{\text{sec}} + w_{\text{kl}} \mathcal{L}_{\text{kl}} + \mathcal{L}_{\text{gen}}
$$

推理时，DEEPGUARD基于提示词计算一次安全偏置 $\mathbf{b}$，并加到解码logits上，避免逐步重新评估。这一轻量级引导机制在不增加显著延迟的前提下，进一步抑制不安全输出，弥补了训练阶段可能残留的漏洞倾向。

## 实验评估

实验在Qwen2.5-Coder、DeepSeek-Coder和Seed-Coder五个模型上，采用He and Vechev（2023）协议评估。基线覆盖PEFT（SVEN、SafeCoder）和推理时防御（CoSec、CodeGuard+），但缺失RAG和强化学习路线的强基线，如RESCUE或SecCoderX。

| 模型 | 方法 | pass@1 | sec-pass@1 |
|---|---|---|---|
| Qwen2.5-Coder-3B | SVEN | 83.00 | 70.47 |
| Qwen2.5-Coder-3B | DEEPGUARD | 86.65 | 80.76 |
| DeepSeek-Coder-6.7B | SVEN | 85.71 | 68.06 |
| DeepSeek-Coder-6.7B | DEEPGUARD | 88.47 | 70.35 |

DEEPGUARD在sec-pass@1上全面超越基线，如在Qwen2.5-Coder-3B上从70.47%提升至80.76%，同时pass@1保持接近基线水平，验证了功能-安全权衡的缓解。

| 变体 | pass@1 | sec-pass@1 |
|---|---|---|
| DEEPGUARD (N=4) | 86.59 | 80.71 |
| 移除 L_sec | 64.94 | 59.12 |
| 仅最终层 (N=1) | 82.65 | 73.76 |
| 平均池化 (N=4) | 84.00 | 78.12 |

消融显示，移除安全对比损失导致sec-pass@1骤降21.59%，证实安全分析器监督的必要性；仅用最终层比多层注意力聚合低6.95%，验证了“最终层瓶颈”假设。注意力聚合优于平均池化，表明可学习权重能更精准地表征安全线索。

评估协议依赖静态分析工具（如CodeQL）检测CWE，未包含动态执行或PoC验证，可能高估安全性。代码开源，但超参数敏感性分析仅在附录中简要提及，未报告GPU资源或训练时间，可复现性细节有限。

## 关联研究分析

从问题动机看，DEEPGUARD与SVEN同属PEFT路线，但SVEN依赖最终层表示，而DEEPGUARD利用多层聚合。这一差异源于对Transformer内部表示层次性的不同理解：SVEN假设最终层已编码足够安全信息，而DEEPGUARD通过探测证实安全线索在中间层更丰富。根源在于任务特性——漏洞判别需要整合语法和语义线索，而最终层优化目标与这一需求冲突。

从方法设计看，DEEPGUARD与CoSec代表训练时与推理时防御的对比。CoSec通过协同解码在推理时验证安全性，但无法修正模型底层的不安全倾向；DEEPGUARD通过模型适配直接改变生成行为。DEEPGUARD在sec-pass@1上优于CoSec，表明训练时多层适配比推理时后处理更有效。然而，DEEPGUARD未探索与RAG方法的结合，如RESCUE通过外部安全知识注入提升安全性，两者是否互补，论文未给出回答。

## 总结

DEEPGUARD针对安全对齐中最终层信号衰减的瓶颈，通过多层注意力聚合构建更敏感的安全分析器，结合多目标训练与引导推理，在五个代码LLM上将安全且正确的生成率平均提升11.9%。实验证实了多层聚合对安全-功能权衡的缓解，但评估仅覆盖静态CWE检测，未验证动态执行场景下的鲁棒性。当模型规模扩大或漏洞类型更复杂时，多层聚合的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.09089)