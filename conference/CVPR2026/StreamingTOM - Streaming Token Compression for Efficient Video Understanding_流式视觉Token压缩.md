# CVPR2026最新论文 ｜StreamingTOM: Streaming Token Compression for Efficient Video Understanding ｜流式视觉Token压缩

研究机构：西湖大学、香港中文大学

作者：Xueyi Chen、Keda Tao、Kele Shao 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.18269)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.18269)

> 流式视频理解面临因果性约束与内存累积的双重瓶颈，现有免训练方法仅优化LLM后端的KV缓存，忽视了前端预填充的计算开销。StreamingTOM通过引入严格因果的预LLM Token缩减机制，在固定预算下平衡计算与内存。该方法以15.7倍压缩比和2倍TTFT加速证明了免训练流式处理的可行性，但其固定Token预算在动态场景下的信息保留能力仍存疑。

## 研究背景

流式视频理解要求模型在时间 $t$ 仅访问 $t$ 之前的观测，这一因果性约束使得离线视频理解中依赖未来帧的全局Token压缩技术失效。同时，随着视频流无限延伸，视觉Token数量线性增长，导致Transformer的注意力计算复杂度呈二次方上升，KV缓存内存占用线性膨胀，最终超出GPU显存限制。解决这一矛盾的关键在于如何在无法预知未来查询分布的前提下，对视觉Token进行不可逆的压缩。

现有流式视频理解方法主要分为训练式与免训练式两类。训练式方法如Flash-VStream通过重训模型适配流式场景，但成本高昂；免训练式方法如LiveVLM和StreamMem聚焦于LLM后端的KV缓存检索与驱逐，虽然缓解了内存压力，但所有视觉Token仍须完整遍历Transformer堆栈，预填充阶段的 $O(tNLd^2)$ 计算开销未被削减。StreamingTOM的切入点在于填补“免训练且严格因果的预LLM Token缩减”这一空白，将压缩动作前移至视觉编码器与LLM之间，从源头降低计算复杂度。

## 核心方法

### 方法参照系

流式视频理解的通用流程为：视觉编码生成Token序列，经LLM预填充生成KV缓存，最后通过解码器响应查询。该流程的关键差异在于，离线方法可全局优化Token分布，而流式方法必须在单帧处理完毕后立即固化状态，且不能访问未来帧。StreamingTOM在此流程中插入预LLM压缩模块，改变了Token进入LLM前的数量与形态。

### 因果时序缩减（CTR）

CTR模块位于视觉编码器之后、LLM预填充之前，其设计动机是消除现有免训练方法中“全量Token遍历LLM”导致的预填充延迟。CTR利用相邻帧 $t-1$ 和 $t$ 的特征差异，将Token划分为静态与动态两类。静态Token通过密度聚类合并，动态Token基于注意力显著性选取，最终输出固定数量 $G$ 的Token组。该过程通过以下公式实现自适应预算分配：

$$
G_s = G \cdot \frac{|S_{static}|}{|S_{static}| + |S_{dynamic}|}, \quad G_d = G - G_s
$$

其中 $G_s$ 和 $G_d$ 分别为静态与动态Token的保留配额。这一机制确保每帧计算量恒定，将预填充复杂度从 $O(TNLd^2)$ 降至 $O(TGLd^2)$，解决了变长压缩导致的延迟不可预测问题。

### 在线量化记忆（OQM）

OQM模块承接CTR输出的Token组，其设计动机是解决LLM后端KV缓存随时间线性增长导致的显存溢出。OQM将每帧的 $G$ 个Token量化为4-bit格式存储，并在查询时按需检索相关组进行反量化。该过程通过帧对齐的组抽象实现，确保检索内容保持时间连贯性。量化存储的内存占用公式为：

$$
\text{Memory} = T \cdot G \cdot d \cdot 4 \text{ bits}
$$

相比FP16基线的 $T \cdot N \cdot d \cdot 16$ bits，该设计实现了15.7倍的压缩比。OQM与CTR通过固定预算 $G$ 耦合，前者负责计算优化，后者负责内存约束，共同构成端到端的流式压缩框架。

## 实验评估

实验在VideoMME、MLVU、EgoSchema（离线）及RVS（在线流式）基准上进行，基线覆盖免训练方法（LiveVLM, StreamMem）与训练式方法（Dispider-7B, Flash-VStream）。StreamingTOM在免训练类别中取得最优性能，离线平均准确率63.8%，RVS准确率55.8%。

| 方法 | VideoMME | MLVU | EgoSchema | Avg |
| :--- | :--- | :--- | :--- | :--- |
| StreamMem | 60.7 | 66.3 | 59.0 | 63.1 |
| **StreamingTOM** | **59.9** | **67.9** | **63.7** | **63.8** |

| 方法 | RVS-Ego Acc | RVS-Movie Acc | Avg Acc |
| :--- | :--- | :--- | :--- |
| StreamMem | 57.0 | 53.1 | 55.2 |
| **StreamingTOM** | **58.3** | **53.2** | **55.8** |

消融实验显示，50 Token/帧与4-bit量化的组合在精度与内存间取得最佳平衡。减少至40 Token导致细节丢失，增加至60 Token则因固定内存预算限制时间覆盖范围，均降低准确率。2-bit量化虽进一步减半内存，但精度显著下降，验证了4-bit为最优压缩率。

评估边界方面，论文未对比2026年最新SOTA方法（如VST-7B），且RVS评估受限于28GB显存约束，未包含CPU卸载场景。代码未开源，超参数（如相似度阈值0.9）的敏感性分析缺失，可复现性依赖单一A6000 GPU环境。

## 关联研究分析

从方法设计看，StreamingTOM与LiveVLM的核心差异在于压缩位置。LiveVLM仅在LLM后端管理KV缓存，而StreamingTOM在LLM前端执行Token缩减。这一差异源于对瓶颈的不同判断：LiveVLM假设内存是主要约束，而StreamingTOM指出预填充计算是实时性的关键瓶颈。然而，CTR的固定预算 $G$ 是否在所有动态场景下均优于自适应预算，论文未提供对比实验，这可能限制了其在高运动视频中的泛化能力。

从问题动机看，StreamingTOM与VisionZip等离线压缩方法共享Token选择思路，但关键区别在于因果性约束。VisionZip利用全局上下文进行双向注意力选择，而StreamingTOM仅依赖相邻帧。这一约束导致CTR无法利用未来帧信息修正当前帧的压缩决策，可能在场景切换瞬间产生信息丢失。论文未量化这种因果性约束带来的精度损失，仅通过RVS基准的55.8%准确率间接验证，该数值与StreamMem持平，暗示预LLM压缩在严格因果场景下的收益可能低于预期。

## 总结

StreamingTOM旨在解决流式视频理解中预填充计算与KV缓存内存的双重瓶颈，其切入点在于首次实现免训练且严格因果的预LLM Token缩减。通过CTR与OQM的协同，该方法在LLaVA-OV-7B上实现15.7倍KV缓存压缩与2倍TTFT加速，同时保持免训练方法中的SOTA精度。然而，其固定Token预算 $G$ 的静态分配机制未能适应动态场景的变化，且4-bit量化在长程语义一致性上的误差累积未被充分评估。当视频流包含高频场景切换时，固定预算下的信息保留能力是否足以支撑复杂推理，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.18269)