# CVPR2026最新论文 ｜Asynchronous Temporal Modeling with Two-Agent Framework for Streaming Dense Video Captioning ｜异步双代理流式密集视频描述

作者：Yolo Y. Tang、Chao Huang、Susan Liang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9d27ce4e6070)

> 流式密集视频描述需在实时处理连续视频流的同时，精准决定何时保持沉默、何时生成事件描述。现有方法依赖复杂外部记忆或固定解码点，且普遍面临“阈值门控差异”（Threshold-Gated Discrepancy, TGD）问题：训练时模型偏向预测沉默，推理时需引入阈值干预，导致训练-推理严重不匹配。本文提出 Takusen 框架，通过小模型（Oracle）稀疏采样检测事件边界、大模型（Listener）密集采样生成描述的双代理异步架构，从根本上消除阈值依赖。该设计在 ActivityNet Captions 上取得 43.7 CIDEr，显著优于现有流式方法，但其对 Oracle 边界预测稳定性的依赖及固定解码点（FDP）的补偿机制，在长程复杂场景下的鲁棒性仍存疑。

## 研究背景

流式密集视频描述的核心困境在于实时性与精度的矛盾。模型必须在帧到达时立即判断是否处于事件边界，并生成准确描述，但无法访问未来帧。这一约束导致传统离线密集描述方法失效，因为后者依赖完整视频上下文进行全局优化。为应对此问题，现有流式方法主要采用两条路线：一是设计复杂的外部记忆机制（如 CM2、Streaming Vid2Seq），通过显式存储历史帧特征来维持时序连贯性；二是使用固定解码点（Fixed Decoding Points, FDPs）或阈值触发机制，在预设时间点或当沉默概率低于阈值时强制生成描述。

然而，这两条路线均存在根本缺陷。外部记忆机制增加了系统复杂度与计算开销，且难以充分利用大语言模型（Large Multimodal Models, LMMs）固有的长上下文能力。更关键的是，基于阈值的触发机制面临 TGD 问题：由于流式任务中大部分帧处于非事件状态（数据不平衡），模型在训练时学会偏向预测沉默 Token，导致推理时需引入阈值来覆盖这一偏差。但训练过程中不存在阈值，这种训练-推理不匹配使得阈值需针对每个视频单独调整，且有效范围极窄，微小偏差即导致模型完全沉默或过度生成。本文切入点在于利用 LMMs 的长上下文能力，通过异步双代理架构将“边界检测”与“描述生成”解耦，从而消除阈值依赖。

## 核心方法

### 方法参照系

流式密集描述的标准流程通常采用单模型端到端架构，结合外部记忆模块处理长序列，并通过阈值或固定时间点触发描述生成。本文的关键差异在于摒弃外部记忆，转而利用 LMMs 的长上下文能力，并引入异步双代理机制替代阈值触发，将时序定位与语义生成解耦为两个并行但异步的过程。

### 异步双代理架构

针对 TGD 问题中阈值依赖导致的训练-推理不匹配，本文提出 Oracle-Listener 异步架构。Oracle 代理采用轻量级小多模态模型（Small Multimodal Model, SMM），以加速率处理稀疏视频帧，专注于检测事件边界 $(s_i, e_i)$。其速度优势使其能“看到”比 Listener 更远的未来，提前预判边界。Listener 代理采用大型多模态模型（LMM），接收密集视频帧，负责生成高质量描述。当 Listener 处理到 Oracle 预测的边界位置时，Oracle 发送预设消息（如“事件 $i$ 开始”或“事件 $i$ 结束，请描述”），引导 Listener 进行相应操作。这一设计将沉默/生成决策从基于概率阈值的隐式判断，转变为基于边界信号的显式指令，从根本上消除了 TGD。

### 混合损失与固定解码点

为对齐训练与推理过程，本文采用混合损失函数，同时优化事件边界处的文本生成与非事件帧的沉默预测：

$$
\mathcal{L} = \frac{1}{N} \sum_{j=0}^{N-1} \left( -\mathbb{I}^{[w_j \neq \varnothing]} \log P_j^{w_j} - \mathbb{I}^{[w_j = \varnothing]} \log P_j^{\varnothing} \right)
$$

其中 $\mathbb{I}$ 为条件指示器，$P_j$ 为第 $j$ 个 Token 的概率。该公式确保模型在边界处生成准确文本，同时在非边界处稳定预测沉默 Token $\varnothing$，无需推理时引入额外阈值。为应对 Oracle 边界预测的不稳定性（如边界对过多、过少或缺失），本文引入均匀分布的固定解码点（FDPs）。在 FDP 位置，系统向 Listener 发送额外提示，生成补充描述，以补偿 Oracle 可能漏检的事件，提升整体描述的完整性与鲁棒性。

## 实验评估

实验在 ActivityNet Captions（8,649 训练视频，平均 2 分钟）和 YouCook2（1,333 训练视频，平均 5.3 分钟）上进行，采用 CIDEr、F1、SODAc 等指标评估。基线覆盖流式方法（Streaming Vid2Seq、Streaming GIT）与非流式 Video-LLMs（VideoLLaMA3、TRACE-uni），但缺乏最新基于强化学习的时序定位模型（如 TempR1）作为对比，因任务侧重不同。

| 方法 | 设置 | ActivityNet CIDEr | ActivityNet F1 | YouCook2 CIDEr | YouCook2 F1 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Streaming Vid2Seq | Streaming | 37.8 | 52.9 | 32.9 | 24.1 |
| Streaming GIT | Streaming | 41.2 | 50.9 | 15.4 | 16.6 |
| VideoLLaMA3 | Non-Streaming | 26.8 | 39.2 | – | – |
| TRACE-uni | Non-Streaming | 29.2 | 40.4 | 35.5 | 31.8 |
| Takusen | Streaming | 43.7 | 54.0 | 40.7 | 37.0 |

Takusen 在 ActivityNet Captions 上 CIDEr 达 43.7，较 Streaming GIT 提升 2.5，较 Streaming Vid2Seq 提升 5.9；在 YouCook2 上 CIDEr 达 40.7，较 Streaming Vid2Seq 提升 7.8。这表明异步双代理架构在流式约束下显著优于现有方法，且性能接近非流式 SOTA。

消融实验显示，移除 Oracle 模型后，仅使用最佳 FDP 配置时 CIDEr 降至 30.4，平均 FDP 配置下仅 18.3，证明 Oracle 边界检测对性能提升至关重要。移除 FDP 后，CIDEr 降至 12.3，表明 FDP 对补偿 Oracle 漏检事件具有关键作用。边界感知基线（Boundary-aware）CIDEr 高达 107.5，但该设置可能包含理想化边界输入，与真实流式场景存在差距，需谨慎解读。

评估边界方面，论文未报告推理延迟、Token 数量等效率指标，无法评估实时性约束下的性能-效率权衡。代码未公开，超参数（如 Oracle 采样率、FDP 间隔）细节有限，可复现性受限。此外，实验仅基于视觉输入，未涉及音视频联合理解，限制了结论在更复杂多模态场景的适用性。

## 关联研究分析

从问题动机看，本文与 Streaming Vid2Seq 同属流式密集描述任务，但后者依赖固定解码点与外部记忆，而本文通过 Oracle-Listener 异步架构消除阈值依赖。这一差异源于对 TGD 问题的不同理解：Streaming Vid2Seq 将沉默/生成决策视为概率阈值问题，而本文将其重构为边界信号驱动问题。根源在于数据不平衡导致的训练-推理不匹配，本文通过架构设计而非参数调整解决，避免了阈值调优的脆弱性。

从方法设计看，本文与 VideoLLaMA3 等单模型 Video-LLMs 同属 LMM 框架，但后者采用端到端训练，缺乏显式时序定位机制。本文引入 Oracle 代理专门处理边界检测，实现了时序定位与语义生成的解耦。这一设计借鉴了时空解耦架构的思想，但应用于流式场景。差异在于，VideoLLaMA3 依赖 LLM 自注意力捕捉时序依赖，而本文通过异步交互显式注入边界信息。查询侧增强在数据充足时是否仍有增益，论文未给出回答，但本文实验表明，显式边界信号在流式约束下对性能提升更为关键。

## 总结

本文核心矛盾在于流式密集描述中实时性与精度的冲突，以及 TGD 问题导致的训练-推理不匹配。现有方法依赖外部记忆或阈值触发，无法充分利用 LMMs 长上下文能力，且阈值调优脆弱。本文通过 Oracle-Listener 异步架构，将边界检测与描述生成解耦，消除阈值依赖，在 ActivityNet Captions 上取得 43.7 CIDEr，YouCook2 上 40.7 CIDEr，显著优于现有流式方法。然而，实验仅基于视觉输入，未评估推理效率，且 FDP 补偿机制在 Oracle 边界预测严重失稳时的鲁棒性未充分验证。当视频流中事件边界高度模糊或 Oracle 预测错误率升高时，FDP 能否有效补偿漏检事件，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_9d27ce4e6070)