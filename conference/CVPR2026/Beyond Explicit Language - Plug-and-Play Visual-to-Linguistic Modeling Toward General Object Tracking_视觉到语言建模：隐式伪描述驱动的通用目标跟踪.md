# CVPR2026最新论文 ｜Beyond Explicit Language: Plug-and-Play Visual-to-Linguistic Modeling Toward General Object Tracking ｜视觉到语言建模：隐式伪描述驱动的通用目标跟踪

研究机构：浙江大学

作者：Kaiyang Lan、Ying Cui、Chenchen Jing 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ad6819cd01f5)

> 视觉语言跟踪（Vision-Language Tracking, VLT）旨在利用自然语言描述辅助目标定位，但现有范式依赖静态文本，导致描述与动态场景失配，且在无文本输入时性能崩溃。本文切入点在于摒弃显式文本依赖，直接从视觉特征逆推隐式语义表征。通过文本反转模块生成伪描述，并结合多层语义注入机制，该方法在不增加外部输入的前提下提升了跟踪鲁棒性。其价值在于实现了语义引导的“自给自足”，但伪描述在极端遮挡下的语义保真度仍存疑。

## 研究背景

当目标在视频中发生剧烈形变或背景干扰时，仅靠视觉外观匹配极易失效，此时引入自然语言描述可提供高层语义约束以区分相似目标。然而，传统VLT方法依赖预定义的静态文本，这种“文本-视觉”对齐在目标状态动态变化时会产生语义漂移。例如，描述“池中的熊”在熊上岸后便失去指导意义，甚至误导模型。为解决这一矛盾，研究者尝试在线生成描述，但依赖大型语言模型（LLM）推理会引入不可接受的延迟，且人工标注无法覆盖所有帧。

主流VLT路线如DUTrack（Wang et al., 2024）通过动态更新视觉与语言参考来缓解不一致，但仍需显式文本输入；JointNLT（Li et al al., 2023）则统一了定位与跟踪架构，却未解决文本缺失时的鲁棒性问题。现有方案的核心瓶颈在于：语义信息的获取要么依赖低效的外部生成，要么依赖静态且易过时的标注。本文抓住的正是这一被忽略的“语义自生成”可能性——既然视觉特征已包含目标的当前状态，是否可以直接从视觉嵌入中“反转”出等效的语言表征，从而消除对显式文本的依赖？

## 核心方法

### 方法参照系

本文基于主流的单流Transformer跟踪框架（如SeqTrack、MCITrack），其标准流程为：Patch Embedding → 视觉骨干（Vision Backbone）→ 预测头。与标准VLT不同，本文不引入独立的文本编码器处理显式输入，而是将视觉骨干与冻结的CLIP文本编码器并行处理，通过新增的文本反转模块（Textual Inversion Module, TIM）和多层语义注入机制（Multi-Layer Semantic Injection Mechanism）实现跨模态交互。

### 文本反转模块：视觉到语义的逆映射

TIM位于Patch Embedding之后，负责将视觉特征映射至CLIP文本嵌入空间。设计动机在于解决静态文本无法反映目标实时状态的问题。模块首先将模板（Template）与搜索区域（Search Region）的视觉嵌入拼接，通过投影（Projection）、多层感知机（MLP）和对齐（Alignment）操作生成伪描述（Pseudo-description）。这一过程相当于一个可学习的Tokenizer和Embedding Lookup层，将每个视觉Patch映射为一个语义Token。

$$
\mathbf{E}_{pseudo} = \text{Align}(\text{MLP}(\text{Proj}([\mathbf{P}_{template}; \mathbf{P}_{search}]))
$$

该公式表明，伪描述嵌入 $\mathbf{E}_{pseudo}$ 由模板与搜索区域的拼接视觉特征经非线性变换得到。关键在于，此映射在Patch级别进行，确保生成的语义线索具有细粒度的空间对应性，从而捕捉目标的局部状态变化，而非仅依赖全局平均特征。

### 多层语义注入机制：跨层特征调制

生成的伪描述送入冻结的CLIP文本编码器，提取出多层文本特征 $\mathbf{F}^s_i$。视觉骨干同样被划分为 $N$ 个V-Block，产生对应的视觉特征 $\mathbf{F}^v_i$。设计动机在于浅层视觉特征缺乏语义完整性，而深层文本特征富含抽象语义，需通过逐层注入实现互补。对于每一对 $(\mathbf{F}^v_i, \mathbf{F}^s_i)$，通过语义引导的交叉注意力（Cross-Attention）调制视觉特征分布。

$$
\mathbf{F}^v'_i = \mathbf{F}^v_i + \alpha_i \cdot \text{MHCA}(\text{Norm}(\mathbf{F}^v_i), \text{Norm}(\mathbf{F}^s_i), \text{Norm}(\mathbf{F}^s_i))
$$

其中 $\alpha_i$ 为可学习缩放因子，MHCA为多头交叉注意力。该机制允许深层语义信息反向丰富浅层视觉特征，同时保持视觉骨干的原始结构不变。这种逐层注入策略确保了跨模态对齐的准确性，避免了仅在顶层融合导致的语义-几何错位。

## 实验评估

实验在LaSOT、GOT-10K、TrackingNet和TNL2K四个基准上进行，基线包括SeqTrack、MCITrack和DUTrack。本文方法以插件形式集成，仅训练TIM、注入模块和Decoder，视觉与文本骨干均冻结。

| 方法 | LaSOT AUC | GOT-10K AO | TNL2K AUC |
| :--- | :--- | :--- | :--- |
| SeqTrack-B256 | 69.9 | 74.7 | 54.9 |
| SeqTrack-B256* | 71.0 | 76.6 | 56.5 |
| MCITrack-B224 | 75.3 | 77.9 | - |
| MCITrack-B224* | 76.1 | 79.4 | - |
| DUTrack-B256 | 73.0 | 77.5 | 63.7 |
| DUTrack-B256* | 73.6 | 77.7 | 67.2 |

*注：DUTrack-B256在TNL2K上的原始值据领域综述为63.7，本文表格中未直接列出该基线原始值，但文中提及DUTrack-B256*提升3.5%。*

主结果显示，本文方法在所有骨干上均带来稳定增益。MCITrack-B224*在LaSOT上AUC提升0.8%，在GOT-10K上AO提升1.5%；DUTrack-B256*在TNL2K上AUC提升3.5%。这表明隐式伪描述在视觉-语言混合任务中比显式文本更具鲁棒性。

| 消融设置 | LaSOT AUC | $\Delta$ AUC |
| :--- | :--- | :--- |
| Baseline (Text-only) | 73.0 | - |
| Without description | 72.3 | -0.7 |
| Pseudo-description only | 73.4 | +0.4 |
| Text + Pseudo-description | 73.6 | +0.6 |

消融实验揭示了关键设计决策：仅使用伪描述（Pseudo-description only）比无描述提升1.1%，证明视觉逆推语义的有效性；同时使用文本与伪描述进一步提升0.2%，说明两者互补而非冗余。在注入层数消融中，3层注入达到最佳AUC 70.7%，6层注入性能回落至70.6%，表明过度交互会增加复杂度并可能引入噪声。

评估边界方面，本文未报告FPS等实时性指标，仅定性指出CLIP文本编码器带来约7 FPS的延迟。代码声明将公开，但未提供具体URL。评估协议未包含长序列遮挡或极端光照场景，限制了鲁棒性的全面验证。

## 关联研究分析

从问题动机看，本文与DUTrack（Wang et al., 2024）形成鲜明对比。DUTrack依赖BLIP在线生成显式描述，虽解决了静态文本问题，但引入了推理延迟和风格不一致；本文则直接从视觉特征逆推伪描述，消除了外部生成依赖。这一差异源于任务特性的不同侧重：DUTrack追求语义的显式可解释性，而本文追求语义引导的效率与一致性。根源在于，显式文本生成需要额外的语言模型推理，而隐式伪描述仅需轻量级投影，这在实时跟踪场景中更具优势。

从方法设计看，本文与CLIP（Radford et al., 2021）的用法存在本质区别。CLIP通常用于图文匹配或零样本分类，而本文将CLIP文本编码器作为“语义空间载体”，仅借用其对齐先验，未使用其生成能力。这种“借用空间而非借用模型”的策略，使得本文方法可即插即用于任意Transformer跟踪器，而不受限于CLIP的特定架构。与ViPT（Zhu et al., 2023）等PEFT方法相比，本文不仅微调参数，更引入了跨模态的特征注入机制，实现了更深层的语义-几何对齐。

## 总结

本文旨在解决视觉语言跟踪中静态描述失效与语言依赖的矛盾，切入点在于从视觉特征逆推隐式伪描述，从而消除对显式文本的依赖。通过文本反转模块和多层语义注入机制，该方法在LaSOT上使MCITrack的AUC从75.3提升至76.1，在TNL2K上使DUTrack的AUC提升3.5%。其边界在于，伪描述生成依赖视觉特征的完整性，在极端遮挡或纹理缺失场景下，视觉嵌入可能无法提供足够的语义线索，导致伪描述退化为噪声。当目标在长序列中经历剧烈外观变化时，仅靠当前帧视觉特征逆推的伪描述是否仍能维持身份一致性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ad6819cd01f5)