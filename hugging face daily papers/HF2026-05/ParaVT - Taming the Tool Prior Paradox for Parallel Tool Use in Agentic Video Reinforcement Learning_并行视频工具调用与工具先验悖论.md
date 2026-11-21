# HuggingFace最新推荐论文 ｜ParaVT: Taming the Tool Prior Paradox for Parallel Tool Use in Agentic Video Reinforcement Learning ｜并行视频工具调用与工具先验悖论

研究机构：新加坡南洋理工大学

作者：Zuhao Yang、Kaichen Zhang、Sudong Wang 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.20342)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.20342)

> 长视频理解中的工具增强强化学习（RL）旨在让模型自主裁剪关键片段以解决细粒度定位难题，但现有串行调用范式存在误差累积与上下文污染瓶颈。本文指出工具原生大语言模型（LMM）在RL训练中面临“工具先验悖论”，即预训练先验既驱动探索又破坏格式稳定性。ParaVT通过单轮并行分发架构与PARA-GRPO算法解决该矛盾，在长视频基准上平均提升7.9%，但其对纯时序定位精度的提升有限，且依赖特定的并行工具轨迹数据。

## 研究背景

当模型面对90分钟足球比赛视频时，均匀采样帧无法捕捉决定性的射门瞬间，这要求模型具备主动裁剪时间窗口的能力。这种能力通常通过监督微调（SFT）学习工具调用格式，再经RL优化实现。然而，SFT学到的结构格式在RL的温度采样下极易崩溃，模型会回退到预训练阶段的`<tool_code>`标签，导致无法解析的工具调用。

长视频理解的主流路线已从被动问答转向代理式视频推理，LongVT、Zoom-Zero等方法通过串行工具调用实现“定位-检查”循环。这种串行范式存在三个致命缺陷：单点定位错误无法被同伴纠正、多轮上下文累积导致视觉Token饱和、推理延迟随轮数线性增长。现有RL方法如GRPO在处理此类工具调用时，暴露出格式脆弱性与工具必要性缺口，即模型倾向于跳过工具直接回答，因为概览帧往往足以应对简单问题。

ParaVT的切入点在于重构工具调用的执行架构与训练算法。它不再将工具调用视为多轮对话，而是作为单轮内的并行子任务分发，同时针对工具原生LMM的预训练先验与SFT格式冲突，设计专门的锚定与门控机制，以在保持格式稳定的同时激发工具探索。

## 核心方法

### 单轮并行分发架构

ParaVT将串行工具调用重构为单轮分治步骤。主智能体在单轮内发出$K$个并行的`crop_video`调用，分发给$K$个共享权重的子智能体。每个子智能体仅处理分配的时间窗口，返回文本摘要而非重采样帧。这一设计解决了串行调用中视觉Token随轮数累积导致的上下文污染问题，且由于子智能体并行执行，推理延迟由最慢的子智能体决定，而非累加。

### Exploration Anchoring

针对RL训练中格式崩溃问题，Exploration Anchoring在结构Token边界施加选择性奖励。其核心公式为：

$$ R_{anchor} = \lambda_{anchor} \left( \alpha \cdot \mathbb{I}[\text{close } \text{think}] + \beta \cdot \mathbb{I}[\text{close } \text{answer}] + \gamma \cdot \mathbb{I}[\text{valid tool}] \right) $$

该公式仅在`</think>`、`</answer>`及有效工具标签位置触发，避免干扰内容Token。设计动机在于SFT学到的格式在RL温度采样下易被预训练先验覆盖，通过锚定结构边界，确保Rollout可解析，从而恢复GRPO的优势信号计算。

### nFrames Gating

针对工具必要性缺口，nFrames Gating随机化每个Prompt的概览帧预算。其机制可表示为：

$$ P(\text{tool} | \text{prompt}) \propto \frac{R_{tool} - R_{skip}}{\sigma_{group}} $$

通过限制部分Prompt的概览帧数量，使得仅靠概览帧无法回答问题，从而在“调用工具”与“跳过工具”的Rollout间产生非零奖励差。这一设计解决了标准GRPO中因概览帧信息充足导致的工具调用优势信号归零问题，迫使模型学习何时必须使用工具。

## 实验评估

ParaVT在六个长视频基准上评估，对比了直接回答、推理增强及工具增强三类开源基线，以及GPT-4o与Gemini-1.5-Pro。基线覆盖较全面，但缺少部分早期VLP基线，符合当前MLLM范式。

| 模型 | VideoMME (w/o sub) | LongVideoBench | LVBench | Charades-STA (mIoU) |
| :--- | :--- | :--- | :--- | :--- |
| Qwen3-VL-8B | 59.9 | 52.2 | 33.1 | — |
| LongVT-RFT-7B | 49.3 | 38.2 | 25.4 | — |
| ParaVT-8B | **62.1** | **60.4** | **39.8** | **50.1** |

ParaVT在所有测试分割上均超越Qwen3-VL基线，其中LongVideoBench提升8.2点，LVBench提升6.7点。Charades-STA上达到50.1 mIoU，低于TempR1的59.8 mIoU，表明其优势在于长上下文证据聚合而非单一时间戳精度。

| 设置 | 格式奖励 ($f_\tau$) | 工具调用率 ($\kappa$) | LongVideoBench |
| :--- | :--- | :--- | :--- |
| + GRPO | 0.13 | 0.02 | 57.5 |
| + Exploration Anchoring | 0.35 | 0.19 | 59.6 |
| + nFrames Gating | 0.10 | 1.36 | 58.4 |
| Full PARA-GRPO | 0.41 | 0.21 | **60.4** |

消融实验显示，Exploration Anchoring将格式奖励从0.13提升至0.35，是恢复可解析性的关键；nFrames Gating单独使用会导致工具调用率过高（1.36）但精度未达最优，表明两者需协同作用。并行分发模式比串行模式在LongVideoBench上高2.7点，验证了架构改进的有效性。

评估协议采用统一的64帧自适应采样，但Charades-STA结果受限于并行摘要可能丢失细粒度时间边界信息。代码、数据与模型权重已公开，训练使用8块NVIDIA GPU，超参数完整披露，可复现性良好。

## 关联研究分析

从问题动机看，ParaVT与LongVT同属工具增强RL路线，但LongVT聚焦于串行“定位-检查”循环的轨迹学习，而ParaVT针对工具原生LMM的预训练先验冲突。LongVT未处理格式在RL温度采样下的崩溃问题，导致其工具调用稳定性依赖SFT质量；ParaVT通过Exploration Anchoring直接干预结构Token，解决了这一特定失效。根源在于LongVT基于非工具原生模型，而ParaVT基于Qwen3-VL等工具原生模型，后者预训练先验更强，冲突更显著。

从方法设计看，ParaVT与Zoom-Zero同属长视频推理框架，但Zoom-Zero采用单次粗到细缩放，缺乏多窗口交叉验证。Zoom-Zero在LongVideoBench上达到46.3 Acc，低于ParaVT的60.4 Acc，表明并行多窗口证据聚合在细粒度推理上更具鲁棒性。然而，Zoom-Zero未涉及RL训练中的格式稳定性问题，其优势可能部分源于单次调用的简洁性，而非多智能体协作。ParaVT的并行架构是否在所有长视频任务中均优于串行，论文未给出全面对比，仅在特定基准上验证。

## 总结

ParaVT旨在解决工具原生LMM在RL训练中因预训练先验导致的格式崩溃与工具跳过问题。其切入点在于识别“工具先验悖论”，并通过单轮并行分发架构与PARA-GRPO算法实现格式锚定与奖励门控。实验证明其在长视频基准上平均提升7.9%，Charades-STA达到50.1 mIoU。然而，其Charades-STA性能低于TempR1，且并行摘要可能损失细粒度时间边界信息，表明其在纯时序定位任务上仍有局限。当概览帧信息极度稀疏时，nFrames Gating的随机化预算是否会导致工具调用率不稳定，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.20342)