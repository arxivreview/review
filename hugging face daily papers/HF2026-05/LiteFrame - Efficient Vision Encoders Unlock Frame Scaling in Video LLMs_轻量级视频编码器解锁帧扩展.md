# HuggingFace最新推荐论文 ｜LiteFrame: Efficient Vision Encoders Unlock Frame Scaling in Video LLMs ｜轻量级视频编码器解锁帧扩展

研究机构：谷歌DeepMind、韩国首尔大学

作者：Jihwan Kim、Nikhil Parthasarathy、Danfeng Qin 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.17260)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.17260)

> 长视频理解面临计算成本随帧数指数级增长的困境，现有“后处理Token压缩”范式虽缓解了LLM侧压力，却将瓶颈转移至视觉编码器。LiteFrame通过内化时空压缩至轻量级ViT骨干，结合压缩Token蒸馏（CTD）训练，在降低端到端延迟的同时提升精度。该方法重新定义了效率-精度帕累托前沿，但其精度绝对值仍低于当前SOTA，且未验证在极端稀疏证据任务上的表现。

## 研究背景

视频大语言模型（Video LLMs）处理长视频时，视觉Token数量远超LLM上下文窗口限制。传统架构中，Vision Transformer（ViT）逐帧提取特征，随后由LLM进行推理。这种设计导致每增加一帧，ViT与LLM的计算成本同步上升，形成双重瓶颈。

主流解决方案聚焦于LLM侧的“提取-减少”范式，即保留冻结的重型ViT，在特征送入LLM前进行后处理Token压缩。然而，当压缩比达到16倍以容纳更多帧时，ViT的逐帧处理延迟成为新的主导瓶颈，限制了端到端效率的进一步提升。LiteFrame的切入点在于识别这一被忽略的编码器侧瓶颈，提出将Token压缩内化至轻量级视觉编码器内部，而非作为后处理步骤。

## 核心方法

### 方法参照系

现有高效Video LLM范式通常采用“重型ViT + 后处理压缩 + LLM”流程。其核心假设是LLM的二次方注意力复杂度为主要瓶颈，因此优先优化LLM输入Token数量。本文的关键差异在于指出，当后处理压缩生效时，ViT的固定计算成本成为新的效率下限，必须同时优化编码器本身。

### 加权平均池化（WAP）作为压缩原语

后处理压缩通常依赖注意力剪枝或Token合并，这些方法基于内容而非位置，破坏了时空连续性。LiteFrame提出加权平均池化（WAP），将输入特征张量 $\mathbf{X} \in \mathbb{R}^{[T] \times [H] \times [W] \times [C]}$ 划分为非重叠时空块 $\Omega_{u,v,s}$，计算压缩Token $\mathbf{Y}_{u,v,s}$：

$$
\mathbf{Y}_{u,v,s} = \sum_{(\tau,i,j) \in \Omega_{u,v,s}} \text{softmax}(\mathbf{x}_{\tau,cls} \cdot \mathbf{x}_{\tau,i,j}) \cdot \mathbf{x}_{\tau,i,j}
$$

该公式通过类Token与局部Token的相似度加权，保留高激活特征的同时维持结构规律性。实验表明，WAP在16倍压缩下显著优于ToMe、PruMerge等复杂方法，且能作为蒸馏目标生成信息密集的监督信号。

### 压缩Token蒸馏（CTD）与轻量级架构

CTD训练轻量级学生编码器直接预测教师模型经WAP压缩后的表示，而非模仿教师的密集输出。设教师密集特征为 $Z_T \in \mathbb{R}^{[N] \times [D]}$，学生输出为 $Z_S \in \mathbb{R}^{[N/r] \times [D]}$，最小化MSE损失：

$$
\mathcal{L}_{CTD} = \| Z_S - \mathcal{P}(Z_T) \|^2
$$

其中 $\mathcal{P}(\cdot)$ 为基于WAP的投影算子。学生架构采用12层ViT-Base（87M参数），在空间层间插入深度可分离1D时间卷积，并在第4、8块后引入步幅为 $[2,2,2]$ 和 $[2,1,1]$ 的深度可分离卷积，逐步下采样时空维度。这一设计将WAP的注意力加权机制内化至静态参数中，消除了运行时计算冗余，使编码器在64帧下比InternVL3-8B快5.3倍。

## 实验评估

实验基于InternVL3-8B作为教师，使用Video-MME、MLVU、LongVideoBench评估。基线覆盖后处理压缩方法（ToMe、FastVID、PruMerge）及高效编码器（AutoGaze、FastVLM），但未包含智能体推理类方法（如LongVT）。

| 方法 | 帧数 | 总延迟 (ms) | Video-MME (w/o subs) | MLVU | LongVideoBench | 平均准确率 (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| InternVL3-8B | 32 | 814.5 | 65.6 | 69.6 | 58.7 | 65.3 |
| +FastVID | 128 | 794.9 | 60.4 | 69.3 | 55.6 | 62.9 |
| +LiteFrame | 256 | 532.3 | 65.1 | 70.7 | 58.3 | 65.7 |

LiteFrame在256帧下总延迟降低34.6%，平均准确率提升0.4个百分点。消融实验显示，CTD结合DWTempConv比SpatioTempAttn延迟降低14.8ms，准确率提升0.9个百分点；LMA阶段进一步提升准确率0.6个百分点，但延迟不变。

评估边界方面，论文未报告置信区间，且仅在固定延迟预算下比较，未评估实时流式场景。代码仅提供项目页面，未明确开源链接，超参数细节见附录A。

## 关联研究分析

从问题动机看，LiteFrame与FastVID同属视频压缩路线，但FastVID聚焦后处理Token减少，而LiteFrame将压缩内化至编码器。这一差异源于对瓶颈位置的判断：FastVID假设LLM是主要瓶颈，而LiteFrame指出ViT延迟在帧数扩展时成为主导。根源在于任务特性：长视频理解中，帧数扩展带来的ViT计算累积效应被后处理范式低估。

从方法设计看，LiteFrame与AutoGaze均尝试轻量编码，但AutoGaze通过预过滤模块减少Token，引入额外自回归解码延迟。LiteFrame通过CTD直接预测压缩表示，避免了运行时过滤开销。这一设计选择牺牲了细粒度空间细节的显式保留，换取了端到端延迟的显著降低。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

LiteFrame解决了长视频理解中视觉编码器延迟瓶颈被后处理范式掩盖的问题。通过内化时空压缩至轻量级ViT，结合CTD训练，该方法在256帧下实现34.6%延迟降低与0.4%精度提升。其边界在于精度绝对值仍低于SOTA（如ReMoRa在MLVU上72.1%），且未验证在极端稀疏证据任务上的表现。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.17260)