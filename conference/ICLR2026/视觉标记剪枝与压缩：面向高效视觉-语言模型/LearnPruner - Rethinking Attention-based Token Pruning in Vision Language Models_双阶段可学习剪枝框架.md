# ICLR2026最新论文 ｜LearnPruner: Rethinking Attention-based Token Pruning in Vision Language Models ｜双阶段可学习剪枝框架

作者：Rinyoichi Takezoe、Yaqian Li、Zihao Bo 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.23950)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.23950)

> 视觉语言模型（VLMs）在高分辨率输入下因视觉Token激增导致推理成本高昂，现有基于注意力分数的剪枝方法因信号失真而在极端压缩率下性能崩塌。本文指出视觉编码器的[CLS]注意力存在“注意力下沉”且LLM浅层注意力受位置偏差干扰，提出LearnPruner框架，通过可学习模块替代[CLS]信号并在LLM中层利用文本引导注意力进行二次筛选。该方法在保留5.6% Token时维持94.8%性能，但依赖额外训练且未解决视频时序冗余问题。

## 研究背景

VLMs将图像编码为离散Token序列输入LLM，但高分辨率图像（如LLaVA-NeXT的2880 Token）引发二次方注意力计算瓶颈。视觉内容信息密度远低于文本，存在大量空间冗余，这为Token剪枝提供了理论可能。然而，剪枝效果高度依赖重要性评估信号的准确性，当前主流方法依赖视觉编码器或LLM的注意力分数，其可靠性存疑。

早期研究如FastV（Chen et al., 2024）在LLM浅层基于平均注意力剪枝，VisionZip（Yang et al., 2025）在视觉编码器侧结合显著性评分与合并策略。这些Training-free方法虽即插即用，但忽视了注意力机制的内在缺陷：视觉编码器的[CLS]Token常将注意力分配给低信息背景区域，而LLM浅层注意力受位置编码局部性影响，对图像下半部分产生系统性偏差。这种信号失真导致在保留Token极少（<10%）时，关键前景信息被误删，性能急剧下降。

本文切入点在于解构注意力信号的失效机制，并引入可学习组件与中层文本引导注意力。不同于固定比率的启发式剪枝，LearnPruner通过训练轻量级模块直接预测Token重要性，并利用LLM中层文本到视觉注意力的鲁棒性进行任务感知筛选，旨在平衡计算效率与语义保真度。

## 核心方法

### 方法参照系

标准VLM剪枝流程为：视觉编码器输出Token → 基于某信号（如[CLS]注意力或LLM浅层注意力）计算重要性 → 保留Top-K Token → 输入LLM。本文的关键差异在于将单一剪枝点拆分为Pre-LLM与Intra-LLM双阶段，并替换了Pre-LLM阶段的信号源。

### 可学习剪枝模块（LPM）

Pre-LLM阶段通常使用[CLS]注意力作为重要性代理，但本文实验表明[CLS]Token对前景聚焦不足。为此，本文引入轻量级多层感知机（MLP）作为可学习剪枝模块（LPM），直接预测每个视觉Token的二值保留掩码。设计动机是摆脱[CLS]注意力的“注意力下沉”缺陷，通过端到端优化使剪枝决策对齐任务目标。LPM接收视觉编码器输出的Token特征 $X_v^{(0)}$，通过STE（Straight-Through Estimator）技巧实现可微分二值化：

$$
M_{hard} = \mathbb{1}[\sigma(f(X_v^{(0)})) > 0.5], \quad M_{soft} = \sigma(f(X_v^{(0)}))
$$

其中 $f(\cdot)$ 为MLP函数，$\sigma$ 为Sigmoid。前向传播使用 $M_{hard}$ 执行硬剪枝，反向传播使用 $M_{soft}$ 传递梯度。此外，为防止背景信息丢失，LPM保留少量基于特征相似度的多样性Token，确保全局视觉覆盖。

### 中层文本引导剪枝

Intra-LLM阶段通常在浅层（如第2层）基于平均注意力剪枝，但本文发现浅层视觉注意力受位置偏差影响严重，而中层（第12层）文本到视觉注意力能有效聚焦查询相关区域。设计动机是利用文本查询的语义引导，剔除与任务无关的视觉Token。本文在LLM第12层提取文本Token对视觉Token的注意力分数 $A_{text-vision}$，将其作为重要性评分，保留Top-$R_2$ Token。该阶段无需额外训练，直接利用LLM内部已有的跨模态交互信息，弥补了Pre-LLM阶段缺乏文本上下文的局限。

## 实验评估

| 方法 | 保留Token数 (↓77.8%) | RelAcc (%) | 保留Token数 (↓88.9%) | RelAcc (%) |
|---|---|---|---|---|
| SparseVLM | 640 | 95.4% | 320 | 92.3% |
| VisionZip | 640 | 97.1% | 320 | 93.9% |
| TwigVLM | 640 | 99.1% | 320 | 96.3% |
| LearnPruner | 640 | 99.3% | 320 | 97.5% |

实验在LLaVA-v1.5-7B、LLaVA-NeXT-7B、Video-LLaVA-7B及Qwen2.5-VL-7B上进行，覆盖GQA、VQAv2、MME等8个图像基准及3个视频基准。基线包括FastV、SparseVLM、VisionZip等Training-free方法，以及TwigVLM、DivPrune等Training-based方法。在LLaVA-v1.5上，LearnPruner在保留640 Token时相对准确率为99.3%，高于TwigVLM的99.1%；在保留320 Token时达97.5%，显著优于VisionZip的93.9%。在Qwen2.5-VL-7B上，当压缩率88.9%时，FastV性能降至71.4%，而LearnPruner保持94.1%，验证了可学习信号在极端压缩下的鲁棒性。

消融实验显示，LPM替代[CLS]注意力带来1.7%的性能提升，而第二阶段文本引导剪枝进一步贡献了0.8%的增益。值得注意的是，在LLM内部插入额外LPM模块并未带来性能提升，表明中层注意力信号已足够可靠，无需额外学习组件。效率分析表明，在LLaVA-NeXT-7B上将Token从2880降至160，Prefill时间加速6.0倍，KV Cache减少8.9倍。

评估边界方面，论文未报告置信区间，且视频实验仅评估前1000样本并使用GPT-4.1辅助评分，存在主观性风险。代码与检查点承诺发布，但训练仅使用10% LLaVA-665K数据，超参数（如LPM层数、STE阈值）未在正文详细列出，复现需依赖附录。

## 关联研究分析

从信号源选择看，LearnPruner与SparseVLM（Zhang et al., 2025b）均利用文本引导注意力，但SparseVLM依赖LLM浅层注意力并自适应调整比率，而LearnPruner证明浅层注意力受位置偏差干扰，转而使用中层文本-视觉注意力。这一差异源于SparseVLM未深入分析注意力随层数的变化规律，而本文通过实验发现中层注意力在语义聚焦上更稳定。LearnPruner的LPM模块与Dynamic-LLaVA（Huang et al., 2024）类似，均使用学习预测器，但Dynamic-LLaVA侧重复杂度估计以调整预算，LearnPruner侧重二值化重要性预测，两者在可微分机制上存在技术竞争：前者可能使用软阈值，后者使用STE硬掩码。

从剪枝位置看，LearnPruner的双阶段设计与VisionZip（Yang et al., 2025）的Pre-LLM单阶段形成对比。VisionZip通过Token合并保留小目标信息，而LearnPruner通过多样性Token选择实现类似效果，但避免了合并带来的特征扭曲。与端到端方法VisionSelector（Zhu et al., 2025）相比，LearnPruner仅训练轻量LPM，冻结骨干网络，训练成本更低，但VisionSelector通过可微分Top-K优化全局目标，理论上性能上限更高。LearnPruner未探索LPM与LLM联合微调的可能性，其性能是否受限于冻结骨干的表达能力，论文未给出回答。

## 总结

LearnPruner针对注意力信号失真导致的极端压缩性能崩塌问题，通过解构视觉编码器与LLM中注意力的失效机制，提出双阶段可学习剪枝框架。该方法以LPM替代[CLS]注意力消除视觉冗余，利用中层文本引导注意力剔除任务无关Token，在保留5.6% Token时维持94.8%性能，实现2.3倍Prefill加速。其边界在于依赖额外训练且仅验证于LLaVA系列与Qwen2.5-VL，未覆盖视频长序列的时序冗余建模，也未探索LPM与量化技术的协同效应。当输入序列长度进一步增加至视频级别时，中层文本注意力的计算开销是否成为新的瓶颈，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.23950)