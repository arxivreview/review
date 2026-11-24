# ICLR2026最新论文 ｜LEARNPRUNER: RETHINKING ATTENTION BASED TOKEN PRUNING IN VISION LANGUAGE MODELS ｜视觉语言模型中基于可学习模块与中层文本注意力的两阶段Token剪枝

作者：Rinyoichi Takezoe、Yaqian Li、Zi-Hao Bo 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_96444484)

> 视觉语言模型处理高分辨率图像时，视觉Token数量激增导致二次方注意力计算成本成为部署瓶颈。现有剪枝方法依赖视觉编码器[CLS]注意力或LLM浅层注意力，但前者存在背景注意力沉陷，后者受位置偏差影响，导致极端压缩率下语义丢失严重。本文提出LearnPruner，通过可学习剪枝模块替代[CLS]注意力，并结合LLM中层文本到视觉注意力进行两阶段级联剪枝。该方法在保留5.6% Token时维持94.8%性能，但需额外训练轻量模块，其泛化边界尚不明确。

## 研究背景

视觉语言模型（Vision-Language Models, VLMs）将图像编码为离散Token序列输入大语言模型（Large Language Models, LLMs），但高分辨率输入使视觉Token从数百激增至数千。这一冗余源于视觉信息密度低于文本，且Transformer架构对长序列的处理效率低下。剪枝的核心在于准确评估Token重要性，而当前主流方法依赖注意力分数作为代理指标，其有效性直接决定剪枝后的任务性能上限。

该领域主流路线分为Pre-LLM与Intra-LLM剪枝。Pre-LLM方法如VisionZip在视觉编码器侧利用显著性评分，但[CLS]注意力常聚焦低信息背景区域；Intra-LLM方法如FastV在LLM浅层利用平均注意力，但受位置编码局部性影响产生注意力偏移。这两种信号在极端压缩率下均无法可靠区分“视觉显著”与“任务相关”，导致固定比率剪枝在复杂场景下性能崩塌。本文切入点在于揭示注意力机制在两个组件中的具体失效模式，并设计混合信号源的两阶段框架以兼顾效率与语义保真度。

## 核心方法

### 方法参照系

通用剪枝流程包含重要性评分、Top-K选择与预算分配三个环节。本文问题与该通用流程的关键差异在于：评分信号不再单一依赖注意力图，而是分解为视觉冗余消除与文本语义对齐两个独立阶段，且第一阶段引入可学习参数替代启发式规则。

### 可学习剪枝模块替代[CLS]注意力

传统Pre-LLM剪枝使用[CLS]注意力分数作为重要性指标，但该信号受Vision Transformer高范数离群Token影响，导致背景区域获得过高权重。本文在视觉编码器后插入轻量级多层感知机（Multi-Layer Perceptron, MLP）作为可学习剪枝模块（Learnable Pruning Module, LPM），直接预测每个Token的二分类重要性分数。由于二分类决策不可微，采用直通估计器（Straight-Through Estimator, STE）实现反向传播：

$$ \mathbf{M}_{hard} = \mathbb{I}(\mathbf{M}_{soft} > \tau), \quad \mathbf{M}_{soft} = \sigma(\mathbf{W}\mathbf{X}_v^{(0)} + \mathbf{b}) $$

其中 $\mathbf{X}_v^{(0)}$ 为视觉编码器输出的Token特征，$\sigma$ 为Sigmoid函数，$\tau$ 为阈值。该设计解决了[CLS]注意力在前景聚焦上的系统性偏差，使剪枝决策从“全局信息聚合”转向“前景显著性预测”，在保留640 Token时相对准确率从97.1%提升至99.3%。

### 中层文本到视觉注意力引导的语义对齐

LPM剪枝后剩余Token进入LLM，但浅层注意力受位置偏差影响，深层注意力则因信息过度聚合而失去区分度。本文发现LLM中层（第12层）的文本到视觉注意力对位置偏移具有鲁棒性，且能聚焦查询相关区域。在LLM第 $k$ 层执行第二阶段剪枝，保留文本注意力分数最高的 $R_2$ 个Token：

$$ \mathcal{S}_{text} = \{ v_i \mid A_{text}(v_i) \in \text{Top-}R_2 \} $$

其中 $A_{text}(v_i)$ 为文本Token对视觉Token $v_i$ 的平均注意力分数。该设计解决了Intra-LLM剪枝中视觉注意力受位置偏差干扰的问题，通过跨模态信号实现任务感知的Token选择，在保留32 Token时相对准确率从94.0%提升至94.8%。

## 实验评估

实验基于LLaVA-v1.5-7B、LLaVA-NeXT-7B、Video-LLaVA-7B及Qwen2.5-VL-7B，在GQA、VQAv2、MME等8个图像基准及3个视频基准上评估。基线覆盖FastV、SparseVLM、VisionZip、TwigVLM等主流方法，但缺失ZOO-Prune等梯度敏感性类方法。

| 方法 | 保留Token数 | 相对准确率 (%) |
|---|---|---|
| VisionZip | 640 | 97.1 |
| TwigVLM | 640 | 99.1 |
| LearnPruner | 640 | 99.3 |
| VisionZip | 320 | 93.9 |
| TwigVLM | 320 | 96.3 |
| LearnPruner | 320 | 97.5 |
| VisionZip | 160 | 90.1 |
| TwigVLM | 160 | 93.3 |
| LearnPruner | 160 | 94.0 |

LearnPruner在所有压缩率下均优于VisionZip，在640 Token时与TwigVLM持平但参数量更少。消融实验显示，LPM替代[CLS]注意力带来1.7%性能提升，而第二阶段文本注意力引导在64 Token预算下贡献0.8%增益，表明两阶段设计在极端压缩下具有互补性。

评估边界方面，论文未报告置信区间，且LPM训练仅使用LLaVA-665K数据集的10%子集，可能限制其对未见分布的泛化能力。代码与模型检查点承诺发布，但未提供具体URL，可复现性依赖后续开源实现。

## 关联研究分析

从信号源设计看，本文与SparseVLM均利用文本引导，但SparseVLM依赖LLM浅层注意力矩阵的秩自适应调整比例，而本文固定两阶段比例并引入可学习模块。差异根源在于：SparseVLM假设注意力分布的统计特性可反映任务复杂度，而本文认为注意力分布本身存在系统性偏差，需通过参数化预测器校正。这种选择暗示注意力信号在极端压缩下不可靠，但论文未验证LPM在分布外数据上的稳定性。

从剪枝位置看，本文与VisionZip同属Pre-LLM剪枝，但VisionZip使用显著性评分加上下文合并，本文使用LPM加多样性Token保留。差异在于：VisionZip的合并策略旨在保留小目标信息，而本文的多样性Token基于特征相似度选择，旨在补偿前景聚焦导致的背景信息损失。这种设计选择反映了任务对背景信息依赖程度的不同假设，但论文未在OCR等细粒度任务上验证多样性Token的有效性。

## 总结

本文要解决的核心矛盾是注意力信号在视觉编码器与LLM中的系统性偏差导致极端压缩率下语义丢失。切入点在于揭示[CLS]注意力的背景沉陷与LLM浅层注意力的位置偏移，并通过可学习模块与中层文本注意力的组合实现信号互补。方法上，LearnPruner通过LPM替代[CLS]注意力并在LLM中层执行文本引导剪枝，在保留5.6% Token时维持94.8%性能，实现2.3倍预填充加速。边界在于LPM需额外训练且仅基于10%数据，其泛化能力未充分验证；两阶段固定比例分配未考虑输入复杂度的动态变化。当LPM训练数据扩展至全量LLaVA-665K时，其性能增益是否饱和，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_96444484)