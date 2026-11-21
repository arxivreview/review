# HuggingFace最新推荐论文 ｜VepAgent: Bridging Causal-Transition via Tool-Augmented Reinforcement Learning for Video Event Prediction ｜视频事件预测中的因果-逻辑间隙与工具增强强化学习

研究机构：南开大学、美国卡内基梅隆大学

作者：Qiutong Chen、Yuchan Guo、Zhenlong Yuan 等 13 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.06293)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.06293)

> 视频事件预测（Video Event Prediction, VEP）要求模型基于部分观测视频推断未来事件，但现有多模态大语言模型（MLLMs）常依赖历史摘要与语言先验，无法桥接未观测的中间状态转换。VepAgent 通过构建因果-逻辑间隙推理链，并引入工具增强强化学习（Tool-Augmented RL）与反先验奖励，将被动预测转化为主动的视觉证据获取与因果分析。该方法在 FutureBench 和 NEPBench 上显著提升了预测精度，但其对工具调用频率的依赖及在复杂长视频中的泛化能力仍存疑。

## 研究背景

当 MLLMs 面对部分观测视频时，其核心困境在于无法从终端帧直接跳跃至未来事件，中间存在未观测的状态转换。这一现象被称为因果-逻辑间隙（Causal-Logic Gap），即模型缺乏对“当前未完成动作如何演变为下一状态”的结构化推理能力。为弥补这一缺口，模型往往退化为依赖语言先验（Language-Prior Shortcut），即选择与查询文本相似度最高的选项，而非基于视觉证据进行推断。这种捷径导致预测在视觉证据缺失或模糊时失效，构成了 VEP 任务的主要瓶颈。

现有 VEP 方法主要依赖脚本事件归纳或动作预测，如 VidEvent 和 EventFormer，它们通过节点图注意力机制建模语义层次，但仍未解决 MLLMs 在推断未来轨迹时的视觉利用不足问题。主流 MLLMs 如 Qwen-VL 系列虽在视频对话和时序定位上表现强劲，但在 VEP 任务中，其回顾性摘要能力无法转化为前瞻性因果推理。VepAgent 的切入点在于将 VEP 重构为主动感知过程：通过显式建模因果-逻辑间隙，并引入诊断工具库动态补全缺失的时空证据，从而打破语言先验的束缚。

## 核心方法

### 方法参照系

VepAgent 基于 MLLMs 的强化学习后训练范式，与 TempR1 等时序定位方法共享 GRPO 框架，但关键差异在于任务目标从“定位过去”转向“预测未来”，且动作空间扩展至工具调用。标准流程仅优化最终答案，而 VepAgent 将工具调用作为推理过程中的中间动作，要求模型在预测前动态获取视觉证据。

### 因果-逻辑间隙推理与工具增强

设计动机在于解决 MLLMs 在部分观测下无法桥接未观测状态转换的问题。VepAgent 引入两阶段代理工作流：第一阶段，模型识别终端观测状态 $S_{final}$ 和正在进行但未完成的动作 $A_{ongoing}$，并构建未来轨迹的因果假设；第二阶段，针对模糊或遮挡的状态转换，模型从诊断工具库 $\mathcal{T}$ 中选择子集 $\mathcal{C} \subseteq \mathcal{T}$ 执行一次，将返回的证据 $V_{aug}$ 和 $E_{aug}$ 集成到推理上下文中。最终预测由增强后的输入条件化生成：

$$ p(y|V \oplus V_{aug}, Q \oplus E_{aug}) = \pi_\theta(V \oplus V_{aug}, Q \oplus E_{aug}) $$

该公式表明，模型不再直接基于原始视频 $V$ 预测，而是基于工具增强后的视觉和文本证据，从而显式建模因果-逻辑间隙。

### 复合反先验奖励机制

设计动机在于抑制语言先验捷径，鼓励模型依赖视觉证据而非文本相似度。VepAgent 设计复合奖励 $R(\tau)$，包含准确性奖励 $R_{acc}$、因果间隙奖励 $R_{cau}$ 和反先验奖励 $R_{ant}$，并由格式奖励 $R_{format}$ 门控：

$$ R(\tau) = R_{format}(\tau) \cdot (0.65R_{acc}(\tau) + 0.20R_{cau}(\tau) + 0.15R_{ant}(\tau)) $$

其中，反先验奖励 $R_{ant}$ 定义为：

$$ R_{ant}(\tau) = \begin{cases} \frac{k-1}{K-1}, & \text{if } R_{acc}(\tau) = 1 \text{ and } K > 1 \\ 0, & \text{otherwise} \end{cases} $$

$k$ 为正确选项与查询 $Q$ 的文本相似度排名，$K$ 为候选选项总数。该公式赋予“文本上最不明显”的正确选项最高奖励，从而惩罚依赖表面词汇模式的预测，强制模型通过工具获取视觉证据以验证因果推理。

## 实验评估

实验在 FutureBench 和 NEPBench 上进行，基线覆盖 Qwen3-VL、InternVL3 等主流 MLLMs，但缺失专用定位模型如 Moment-DETR 变体。VepAgent-4B 在 FutureBench 上取得 81.44% 的平均准确率，较最强基线 Qwen3-VL-30B-A3B（66.86%）提升 14.58 个百分点；在 NEPBench 上取得 70.20% 的整体准确率，较 Qwen2.5-VL-72B（47.50%）提升 22.70 个百分点。

| 方法 | FutureBench AVG (%) | NEPBench Overall (%) |
| :--- | :--- | :--- |
| Qwen3-VL-30B-A3B | 66.86 | — |
| Qwen2.5-VL-72B | — | 47.50 |
| VepAgent-4B | 81.44 | 70.20 |

消融实验显示，SFT 与 RL 结合将平均准确率从 59.09%（Qwen3-VL-4B 基线）提升至 75.09%，完整工具增强模型进一步达到 78.79%。增加 GRPO 生成数量从 2 到 8，平均准确率从 78.60% 提升至 81.44%，但 1-Hop 准确率在生成数量为 2 时最高（84.39%），表明工具调用频率与预测深度存在权衡。

评估边界方面，论文未报告置信区间，且未在 Charades-STA 等定位基准上验证，限制了与定位任务的横向对比。代码已开源，训练使用 8 块 NVIDIA RTX A5000 GPU，SFT 1 个 epoch，RL 250 步，超参数透明，可复现性较好。

## 关联研究分析

从问题动机看，VepAgent 与 TempR1 同属 GRPO 框架，但 TempR1 聚焦时序定位，奖励函数仅关注最终答案正确性，而 VepAgent 引入反先验奖励以抑制语言捷径。这一差异源于任务特性：定位任务依赖视觉边界证据，而预测任务需桥接未观测状态，语言先验在预测中更易导致错误。VepAgent 的工具增强机制借鉴了 CogniGPT 的代理式工具调用，但 CogniGPT 用于长视频问答，工具调用频率较低，而 VepAgent 将工具调用作为核心推理步骤，频率更高，这可能导致在简单任务上过度依赖工具，降低效率。

从方法设计看，VepAgent 与 SEASON 均针对语言先验，但 SEASON 通过对比解码在推理时抑制幻觉 Token，而 VepAgent 通过反先验奖励在训练阶段惩罚语言捷径。SEASON 无需重新训练，部署成本低，但效果有限；VepAgent 效果更持久，但计算成本高。VepAgent 的因果间隙奖励 $R_{cau}$ 要求模型显式建模中间状态转换，这与 SEASON 的解码阶段干预形成互补，但 VepAgent 未深入分析模型内部时序表征机制，反先验奖励是否真正解决了幻觉的内在机制，还是仅掩盖了问题，论文未给出回答。

## 总结

VepAgent 要解决的核心矛盾是 MLLMs 在 VEP 任务中依赖语言先验而非视觉证据，导致无法桥接因果-逻辑间隙。其切入点在于将 VEP 重构为主动感知过程，通过工具增强 RL 动态补全缺失的时空证据，并设计反先验奖励抑制语言捷径。该方法在 FutureBench 和 NEPBench 上分别提升 14.58 和 22.70 个百分点，证明了工具增强与反先验奖励的有效性。然而，论文未报告置信区间，且未在定位基准上验证，限制了泛化能力的评估。当支持集增大到 5-shot 时，工具调用频率的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.06293)