# ACL-Findings2026最新论文 ｜Understanding In-Context Learning Beyond Transformers: An Investigation of State Space and Hybrid Architectures ｜状态空间与混合架构中的上下文学习机制解析

研究机构：加拿大不列颠哥伦比亚大学

作者：Shenran Wang、Timothy Tin-Long Tse、Jian Zhu

论文原文见 [arXiv](https://arxiv.org/abs/2510.23006)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.23006)

> 现有理论多聚焦于Transformer内部隐式优化算法的数学等价性，但状态空间模型（SSM）及混合架构的上下文学习（In-Context Learning, ICL）内部机制尚属黑盒。本文切入点在于利用机制可解释性技术，实证对比不同架构中负责ICL的功能向量（Function Vectors, FVs）分布差异。通过行为探针与激活干预相结合，揭示了自注意力层在混合架构ICL中的主导作用及Mamba2可能存在的非FV机制。该工作填补了非Transformer架构ICL机制解释的空白，但其结论受限于1B参数规模及NLP任务类型，对大规模模型及非语言任务的普适性存疑。

## 研究背景

当模型面对未见过的任务时，仅凭提示词中的少量示例即可适应新任务，这一现象称为上下文学习（In-Context Learning, ICL）。ICL的核心挑战在于解释模型如何在无参数更新的前提下，从上下文中提取任务规则。早期研究将ICL视为Transformer自注意力头的一种涌现能力，特别是归纳头（Induction Heads）被证实负责“匹配-复制”行为。然而，随着状态空间模型（State Space Models, SSMs）如Mamba的兴起，其线性时间复杂度优势引发了对非注意力架构ICL能力的关注，但现有理论多基于线性注意力的简化假设，难以直接解释Softmax注意力及SSM状态更新机制下的ICL行为。

主流理论路线试图建立前向传播与梯度下降等优化算法的数学等价性，但这通常依赖于线性注意力或浅层模型的假设，与实际大规模LLM的Softmax非线性及深层残差结构存在“Softmax鸿沟”。同时，SSM的ICL能力虽被实证存在，但其内部是否同样依赖类似归纳头的特定电路，还是基于状态压缩的其他机制，缺乏微观层面的解释。本文的切入点在于跳出纯理论推导，直接对预训练的大规模Transformer、SSM及混合架构进行机制可解释性分析，通过定位功能向量（Function Vectors, FVs）在模型内部的分布，实证揭示不同架构在ICL任务中的机制差异。

## 核心方法

### 功能向量定位框架

本文沿用Todd et al. (2024)提出的功能向量（FVs）概念，将其从Transformer扩展至SSM及混合架构。FVs定义为特定注意力头或状态单元在任务相关输入上的激活方向，其核心假设是ICL能力由少数关键头驱动。与纯理论方法不同，本文不追求算法等价性证明，而是通过激活干预（Steering）和消融（Ablation）实验，量化每个头对ICL性能的贡献度。这一设计动机在于解决现有理论无法直接应用于Softmax及SSM架构的困境，通过实证手段建立架构-机制-性能的映射关系。

### 双维度任务区分与干预实验

本文引入参数知识检索（Parametric Knowledge Retrieval）与上下文知识理解（Contextual Knowledge Understanding）两类任务，以区分依赖预训练记忆与依赖上下文推理的ICL场景。对于每个任务，计算各头在提示词最后一个token上的任务依赖输出值，公式如下：

$$ \text{FV}_h = \mathbb{E}_{p \in P_t} [ \text{Output}_h(p) ] $$

该公式通过平均任务$t$中所有提示词$p$在第$h$个头的输出，提取该头对任务$t$的特异性响应。随后，通过Steering实验将FV注入模型，观察性能增益；通过Ablation实验移除FV，观察性能下降。这种双向验证确保了FV定位的因果性，而非仅仅是相关性。

### 混合架构中的流分离分析

针对Hymba（并行）与Zamba2（串行）混合架构，本文分别对自注意力流（Attention Stream）和Mamba流（Mamba Stream）进行独立的FV提取与干预。这一设计解决了混合架构中多流交互导致的机制混淆问题。通过对比两流的Steering增益，本文发现自注意力流在ICL中占据主导地位，而Mamba流的贡献相对有限。具体而言，在Hymba中，自注意力头的FV强度显著高于Mamba头，且Steering自注意力流带来的性能提升远超Mamba流。这一发现表明，混合架构的ICL能力主要继承自Transformer组件，SSM组件可能更多承担序列建模而非任务学习功能。

## 实验评估

实验在GLUE/SuperGLUE子集及合成任务上进行，对比了Qwen2.5-1.5B、Llama-3.2-1B、Gemma-3-1B-PT（Transformer），Mamba-1.4B、Mamba2-1.3B（SSM），以及Hymba-1.5B、Zamba2-1.2B（混合架构）。基线覆盖了主流架构，但缺乏纯理论模型（如线性注意力Transformer）的直接对比，限制了与理论预测的精确对齐。

| 模型 | 任务类型 | k=16 Gold Macro-F1 | k=16 0_correct Macro-F1 |
| :--- | :--- | :--- | :--- |
| Gemma-3-1B-PT | 上下文理解 | 72.7 | 18.7 |
| Hymba-1.5B | 上下文理解 | 60.4 | 8.6 |
| Mamba2-1.3B | 上下文理解 | 60.7 | 18.7 |
| Zamba2-1.2B | 上下文理解 | 62.6 | 13.1 |

数据显示，Transformer模型在Gold设置下表现最优，而混合架构与SSM模型性能接近但略低。值得注意的是，Mamba2在0_correct设置下的性能（18.7）与Gemma持平，但在Gold设置下（60.7）低于Gemma（72.7），暗示其ICL能力可能更依赖上下文噪声而非纯净任务信号。

消融实验显示，Steering自注意力流在混合架构中带来显著性能增益，而Steering Mamba流在Zamba2中甚至导致性能下降。这一反直觉发现表明，Mamba流在ICL中可能承担干扰抑制或状态稳定功能，而非直接的任务规则提取。此外，Mamba2的FV定位结果与其他模型差异显著，其Steering增益微弱，但Ablation影响较大，暗示Mamba2可能使用非FV机制（如状态压缩）实现ICL。

评估边界方面，本文仅使用1B参数模型，未验证结论在7B+模型中的普适性。任务类型局限于NLP分类与检索，未涵盖生成或数学推理任务。代码已开源，但超参数配置未完全披露，复现性依赖于特定预训练检查点。

## 关联研究分析

从问题动机看，本文与Von Oswald et al. (2023)的隐式梯度下降理论形成互补。后者通过数学证明建立Transformer前向传播与优化算法的等价性，但局限于线性注意力；本文则通过实证手段在Softmax及SSM架构中验证ICL机制，揭示了理论假设与实际模型间的差距。两者的差异根源在于任务特性：理论方法追求通用算法解释，而本文关注特定架构下的微观电路差异。这种差异暗示，SSM的ICL机制可能无法用单一的优化算法统一解释，需引入状态空间特有的动力学视角。

从方法设计看，本文与Olsson et al. (2022)的归纳头研究同属机制可解释性路线，但本文将分析对象从纯Transformer扩展至混合架构，并引入任务类型区分。与归纳头不同，FVs更侧重于任务特异性而非通用的匹配-复制行为。这一设计选择解决了归纳头在复杂任务中解释力不足的问题，但也引入了任务依赖性的局限。Mamba2的非FV机制发现，挑战了“所有ICL均依赖特定注意力头”的共识，提示SSM可能通过状态更新实现隐式学习，这一机制在现有理论框架中缺乏对应解释。

## 总结

本文要解决的核心矛盾是SSM及混合架构ICL机制的黑盒状态，现有理论无法直接解释非注意力架构的ICL行为。本文抓住的切入点是通过机制可解释性技术，实证定位功能向量在不同架构中的分布差异。通过双维度任务区分与流分离干预，本文证明了自注意力流在混合架构ICL中的主导作用，并发现Mamba2可能使用非FV机制。核心数字显示，Gemma-3-1B-PT在Gold设置下Macro-F1达72.7，而Mamba2仅为60.7，且Steering Mamba流在Zamba2中导致性能下降。本文的边界在于仅验证了1B参数模型及NLP任务，未探索大规模模型及非语言任务下的机制一致性。当模型规模扩大至7B以上时，Mamba2的非FV机制是否依然主导ICL，还是会被自注意力流重新覆盖，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.23006)