# ICLR2026最新论文 ｜Omni-Weather: A Unified Multimodal Model for Weather Radar Understanding and Generation ｜统一生成与理解的气象雷达基础模型

研究机构：同济大学、上海交通大学

作者：Zhiwang Zhou、Yuandong Pu、Xuming He 等 13 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.21643)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.21643)

> 气象建模长期面临预测精度与机制解释割裂的困境，现有生成模型无法输出诊断文本，理解模型无法合成物理场。Omni-Weather 通过共享自注意力骨干统一这两类任务，并引入思维链（Chain-of-Thought, CoT）推理以增强可解释性。该模型在雷达短临预报与卫星反演任务上超越了专用基线，验证了生成与理解任务的互益效应，但其评估局限于雷达尺度，未触及全球数值天气预报中的物理守恒约束。

## 研究背景

雷达短临预报（Nowcasting）旨在从历史垂直积分液态水（Vertically Integrated Liquid, VIL）序列预测未来降水演变，其核心挑战在于捕捉对流系统的非线性运动与形态变化。传统方法如 CasCast 和 DiffCast 专注于像素级重建，但缺乏对气象物理机制的语义理解；而 RadarQA 等理解模型虽能生成诊断报告，却无法合成新的雷达场。这种任务割裂导致模型无法同时提供“预测结果”与“预测依据”，限制了其在极端天气预警中的决策支持能力。

气象领域现有方案分为两条互斥路线：生成路线（如 WeatherGFM）通过 Transformer 架构实现跨模态映射，但输出为黑盒数值，缺乏可审计性；理解路线（如 RadarQA）利用大语言模型（LLM）解析雷达图像，但无法进行物理场生成。这种二元对立源于架构设计的根本差异：生成任务需要连续值解码器，理解任务需要离散文本解码器。Omni-Weather 的切入点在于借鉴多模态基础模型（如 Bagel-7B-MoT）的统一范式，将两类任务映射至同一序列到序列框架，通过共享骨干学习可迁移的对流演化表征，从而打破生成与理解的壁垒。

## 核心方法

### 统一序列到序列范式

Omni-Weather 将雷达预报、反演及理解任务统一为条件序列生成问题。给定任务提示 $p_t$、输入序列 $x_t$ 和目标输出 $y_t$，模型学习映射：

$$ y_t = F_\theta(p_t, x_t) $$

其中 $F_\theta$ 为共享 Transformer 骨干。该设计动机在于消除任务特异性架构，使模型通过提示词动态切换任务模式，而非依赖独立网络。与 WeatherGFM 的上下文学习不同，Omni-Weather 采用端到端监督微调，确保生成与理解任务在表征空间中对齐。

### 多模态编码器与思维链推理

针对雷达序列的时间动态特性，Omni-Weather 引入 EarthFormer 作为雷达序列编码器，生成运动感知 Token 以稳定长程预测。对于理解任务，视觉输入经理解编码器处理后与文本提示拼接，由文本解码器生成自然语言描述。关键创新在于构建 CoT 数据集，将生成任务转化为因果推理过程：

$$ \mathcal{L}_{total} = \sum_{t \in T_{gen}} \lambda_t \mathcal{L}_{gen}(y_t, G_\phi(z_t)) + \sum_{t \in T_{under}} \lambda_t \mathcal{L}_{under}(y_t, L_\psi(z_t)) $$

其中 $G_\phi$ 和 $L_\psi$ 分别为 VAE 解码器和文本解码器。CoT 微调迫使模型在生成前显式推理气象属性（如运动方向、强度变化），这一设计解决了纯生成模型缺乏物理可解释性的问题，同时通过推理监督提升了感知质量。

## 实验评估

实验基于 SEVIR 数据集，对比 CasCast、DiffCast、EarthFormer（生成）及 RadarQA、GPT-5（理解）。Omni-Weather 在雷达预报任务上 CRPS 降低 15% 以上，LPIPS 改善 25%，表明统一架构在保持像素精度的同时提升了结构一致性。在雷达反演任务中，其 CSI 得分在所有阈值上均超越 WeatherGFM，高值区域增益达 20%。

| 任务 | 方法 | CSI-Mean | CRPS (↓) | LPIPS (↓) | GPT4-Score |
|---|---|---|---|---|---|
| 雷达预报 | CasCast | 0.384 | 0.031 | 0.207 | - |
| 雷达预报 | Omni-Weather | 0.384 | 0.026 | 0.179 | - |
| 雷达预报 | Omni-Weather-thinking | 0.353 | 0.028 | 0.166 | - |
| 雷达理解 | RadarQA | - | - | - | 6.85 |
| 雷达理解 | Omni-Weather | - | - | - | 7.48 |

消融实验显示，联合训练（U+G）优于单任务训练，验证了生成与理解任务的互补性。CoT 微调与思维推理结合后，LPIPS 降至 0.163，GPT4-Score 升至 7.82，但 CSI-Mean 略有下降（0.335 vs 0.347），表明推理过程在提升感知质量的同时对像素精度存在轻微权衡。

评估边界在于：SEVIR 数据集仅覆盖雷达尺度，未涉及全球 NWP 中的物理守恒律（如质量、能量守恒）。指标侧重感知质量（LPIPS）与语义一致性（GPT4-Score），缺乏对概率校准的严格评估。代码已开源，但训练需 8×H200 GPU 20k 步，资源门槛较高。

## 关联研究分析

从问题动机看，Omni-Weather 与 NeuralGCM 均旨在提升模型的可解释性，但路径截然不同。NeuralGCM 通过嵌入物理方程约束确保动力学一致性，而 Omni-Weather 依赖 LLM 的语义推理能力生成因果解释。这种差异源于任务尺度：NeuralGCM 面向全球气候模拟，物理守恒是硬约束；Omni-Weather 面向雷达短临预报，语义解释更贴近业务需求。然而，Omni-Weather 未验证其 CoT 推理是否真正捕捉了物理机制，还是仅学习了数据中的统计相关性，这一盲区限制了其在极端事件预测中的可靠性。

从方法设计看，Omni-Weather 与 Swift 均追求高效推理，但目标不同。Swift 通过一致性模型实现单步概率生成，优化计算效率；Omni-Weather 通过共享骨干实现任务统一，优化功能完整性。Swift 的 CRPS 优化直接针对概率校准，而 Omni-Weather 的 CRPS 仅作为辅助指标，未展示完整概率分布。这暗示 Omni-Weather 在不确定性量化方面存在不足，其“理解”能力可能受限于 LLM 的幻觉问题，尤其在训练数据稀疏的极端天气场景中。

## 总结

Omni-Weather 解决了气象建模中生成与理解任务割裂的核心矛盾，通过共享 Transformer 骨干和 CoT 推理实现了功能统一与可解释性提升。实验证明联合训练带来互益效应，CRPS 降低 15% 且 GPT4-Score 超越专用理解模型。然而，其评估局限于雷达尺度，未触及全球 NWP 的物理守恒约束，且 CoT 推理的物理有效性未获独立验证。当雷达序列包含未见过极端对流形态时，CoT 生成的因果解释是否仍能保持物理一致性，而非退化为语言模板，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.21643)