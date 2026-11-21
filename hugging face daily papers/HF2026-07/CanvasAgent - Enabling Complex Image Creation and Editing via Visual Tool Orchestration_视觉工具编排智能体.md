# HuggingFace最新推荐论文 ｜CanvasAgent: Enabling Complex Image Creation and Editing via Visual Tool Orchestration ｜视觉工具编排智能体

作者：Hairui Zhu、Yiying Yang、Tengjin Weng 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.05465)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.05465)

> 复杂图像创作往往涉及生成、定位、分割、合成等多步骤操作，单一模型调用难以协调异构工具间的状态依赖与视觉反馈。现有多模态智能体多聚焦于感知或搜索，缺乏针对可执行图像编辑轨迹的大规模监督。本文通过构建包含14万条执行轨迹的CanvasCraft数据集，并采用SFT+GRPO两阶段训练框架，使智能体能够自主编排11种视觉工具。该方案在自建基准上显著提升了轨迹质量与最终图像对齐度，但其评估局限于特定工具链，跨基准泛化能力存疑。

## 研究背景

当用户要求“将图中扭曲的招牌文字提取并重构到空白面板，再合成进雨景”时，任务不再局限于单次像素修改，而是涉及OCR识别、区域定位、图像编辑与透视合成的长程工作流。此类任务要求智能体在每一步工具调用后检查中间视觉产物，而非假设操作成功，这构成了状态依赖的轨迹学习问题。传统指令式图像编辑（Instruction-Based Image Editing, IBIE）将问题简化为源图像与指令到目标图像的端到端映射，依赖扩散模型内部的语义先验。然而，当指令涉及多对象交互、空间推理或需要调用外部工具（如超分辨率、几何变换）时，单一模型暴露出指令遵循能力不足与背景保持差的瓶颈。

领域主流路线正从“像素重绘”转向“推理-规划-执行”。MIRA（Zeng et al., 2025）和EditThinker（Li et al., 2025）引入多模态大语言模型（MLLM）作为推理引擎，通过强化学习优化单步或迭代编辑策略，解决了复杂指令的组合推理问题。然而，这些方法仍局限于单一编辑器的内部迭代，未处理异构工具间的显式状态管理。CanvasAgent的切入点在于将图像编辑重构为多工具编排问题，通过显式资产引用和闭环视觉验证，解决长程工作流中的工具依赖与中间状态追踪难题。

## 核心方法

### 方法参照系

本文问题属于多模态智能体工具使用（Tool-Augmented Multimodal Agents）范畴，但区别于ReAct（Yao et al., 2022）等通用推理框架，其核心差异在于视觉状态的显式管理与工具链的异构性。通用框架假设工具调用结果可被文本描述，而图像编辑要求智能体直接操作像素级资产（如掩码、裁剪图），并基于视觉反馈调整后续动作。

### 两阶段训练框架

SFT阶段旨在建立有效的工具调用格式与跨工具依赖关系。设计动机在于直接强化学习（RL）在可执行视觉工具上易导致无效调用与稀疏奖励，需通过专家轨迹初始化稳定策略。CanvasAgent基于Qwen3-VL-8B-Instruct，在CanvasCraft-SFT上进行下一词预测训练，学习JSON格式的工具调用与中间资产引用。该阶段确立了初始工具使用能力，但受限于模仿静态演示，无法探索更优的长程规划策略。

### 混合奖励强化学习

RL阶段通过GRPO（Group Relative Policy Optimization）优化多工具规划，解决SFT无法发现的动态任务分解策略。设计动机在于图像创作任务涉及主观视觉质量与客观可执行性，单一奖励信号无法兼顾。混合奖励函数定义为：

$$ R_{total} = \alpha R_{align} + \beta R_{aes} + \gamma R_{traj} + \delta R_{rule} - \lambda_{eff} P_{eff} $$

其中 $R_{align}$ 和 $R_{aes}$ 由LLM-as-judge评估最终图像与指令的对齐度及美学质量；$R_{traj}$ 评估轨迹合理性；$R_{rule}$ 包含格式、动作有效性与效率惩罚。该设计将结果信号与过程信号解耦，使智能体在优化最终图像的同时，学习避免冗余工具调用与无效参数。

## 实验评估

实验在CanvasCraft-RL评估集（250样本）上进行，基线包括通用MLLM（Qwen3-VL-8B/32B, LLaVA-OneVision-7B）及图像生成模型（GPT-Image-2, Wan2.7-Image）。缺失专用编辑智能体（如MIRA）作为直接对比，限制了跨方法可比性。

| 模型 | Overall Reward | Alignment Score | Aesthetic Score | Trajectory Score |
| :--- | :--- | :--- | :--- | :--- |
| Qwen3-VL-8B-Instruct | 0.426 | 0.493 | 0.667 | 0.092 |
| CanvasAgent (SFT) | 0.557 | 0.613 | 0.711 | 0.576 |
| CanvasAgent (SFT+RL) | 0.821 | 0.869 | 0.762 | 0.849 |
| GPT-Image-2 | - | 0.799 | 0.895 | - |

SFT+RL版本在Overall Reward上较SFT-only提升0.264，Alignment Score提升0.256，表明RL显著增强了复杂指令下的工具编排能力。GPT-Image-2在Aesthetic Score上领先（0.895 vs 0.762），但缺乏轨迹评估，无法反映其多步规划能力。

| 配置 | Overall Reward | Alignment Score | Trajectory Score |
| :--- | :--- | :--- | :--- |
| SFT Only | 0.557 | 0.613 | 0.576 |
| RL Only | 0.604 | 0.472 | 0.673 |
| w/o outcome reward | 0.636 | 0.320 | 0.907 |
| Hybrid Reward | 0.821 | 0.869 | 0.849 |

消融实验显示，移除结果奖励后Trajectory Score升至0.907，但Alignment Score骤降至0.320，证明过程奖励与结果奖励的互补性。RL-only配置在Alignment Score上低于SFT-only（0.472 vs 0.613），表明缺乏SFT初始化会导致探索不稳定，验证了两阶段训练的必要性。

评估协议局限于自建CanvasCraft基准，未采用GEdit-Bench或ImgEdit-Bench等通用指标，导致与领域SOTA无法直接对比。代码与数据集已开源，但训练依赖8块A800 GPU及7天周期，复现成本较高。

## 关联研究分析

从问题动机看，CanvasAgent与MIRA（Zeng et al., 2025）均利用MLLM进行复杂指令编辑，但MIRA聚焦单一编辑器的迭代优化，而CanvasAgent处理异构工具链的状态管理。这一差异源于任务特性：MIRA假设编辑可由单一模型完成，而CanvasAgent针对需调用OCR、超分辨率等外部工具的场景。MIRA未解决工具间资产引用问题，导致其在多工具场景下泛化能力受限。

从方法设计看，CanvasAgent与RePlan（Qu et al., 2025）均涉及空间定位，但RePlan依赖VLM思维链生成区域掩码，而CanvasAgent通过Grounding-DINO与SAM工具显式定位。RePlan的免训练注意力注入机制计算开销较低，但依赖VLM推理准确性；CanvasAgent的工具链方案更灵活，但引入了额外的推理延迟。规则奖励中的效率惩罚项是否限制了智能体探索非标准但有效的工具组合，论文未给出回答。

## 总结

本文核心矛盾在于长程视觉工作流中异构工具的状态依赖与闭环验证缺失。现有方法如MIRA局限于单模型迭代，无法处理多资产状态管理。CanvasAgent通过构建大规模可执行轨迹数据集与混合奖励RL框架，实现了工具编排的自动化。实验显示SFT+RL在Overall Reward上达到0.821，较SFT-only提升0.264。其边界在于评估局限于自建基准，且规则奖励可能抑制非标准工具组合的探索。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.05465)