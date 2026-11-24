# CVPR2026最新论文 ｜STAR-R1: Multi-View Spatial TrAnsformation Reasoning by Reinforcing Multimodal LLMs ｜多视角空间转换推理的强化学习框架

研究机构：中国人民大学、中国科学院

作者：Zongzhao Li、Zongyang Ma、Mingze Li 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_754513fa29c3)

> 多视角空间推理要求模型在不同视角图像间建立对象对应并重建场景语义，但现有方法在视角变化时普遍失效。监督微调（SFT）仅能记忆标注模式，缺乏跨视图一致性推理；纯强化学习（RL）则难以稳定识别关键参照对象。本文提出 STAR-R1，通过过程监督冷启动与参照感知 RL 的两阶段策略，将对象选择与答案正确性纳入细粒度奖励。该方法在 MindCube-Tiny Rotation 上达到 98.5%，但 MMSI-Bench 成绩低于领域记录值，其泛化边界尚存疑问。

## 研究背景

当模型面对同一场景的左右视角图像时，它必须识别哪些对象发生了属性变化，而非简单比对像素差异。这一任务称为转换驱动视觉推理（Transformation-Driven Visual Reasoning, TVR），其核心难点在于视角偏移导致对象位置与外观发生系统性位移，模型需先建立跨视图对象对应，再推断属性转换。若对应关系错误，后续推理必然失效，这构成了多视角空间理解的基础瓶颈。

多视角空间推理的主流路线依赖结构化思维链或显式几何接地。ViewFusion（Tao et al., 2026）通过多视图空间预思考链接视角，GeoWeaver（Miao et al., 2026）注入深度图作为硬约束，两者均假设模型可通过监督学习习得跨视图对齐。然而，SFT 模型在域外（OOD）视角变化下准确率骤降，表明其仅记忆了标注分布而非推理机制。本文切入点在于：RL 能否诱导模型自发形成人类样的对象锚定行为，从而在缺乏显式几何先验时实现鲁棒的跨视图验证。

## 核心方法

### 方法参照系

多视角空间推理的标准流程为：单视图局部分析 → 跨视图对齐 → 全局推理。本文问题与该流程的关键差异在于，对齐环节缺乏可微分的监督信号，SFT 无法优化“选择哪些对象作为参照”这一离散决策，而 RL 提供了非梯度优化的探索路径。

### 过程监督冷启动

SFT 阶段解决 RL 冷启动时对象选择不稳定、输出格式混乱的问题。通常做法是随机采样多视图数据微调，但本文采用 Gemini-2.5-Pro 生成严格遵循三步推理轨迹的高质量 CoT，并仅保留最终答案正确的样本。该设计确保初始策略已具备基本的跨视图对应能力，为 RL 探索提供可靠起点。

$$
\mathcal{D}_{\text{SFT}} = \{ (I^{\text{initial}}, I^{\text{final}}, Q, \text{CoT}) \mid \text{answer}(\text{CoT}) = \text{GT} \}
$$

此公式表示 SFT 数据集仅包含最终答案正确的 CoT 样本，通过结果导向过滤保证监督信号的一致性，避免模型学习错误的推理路径。

### 参照感知强化学习

RL 阶段解决 SFT 模型在 OOD 场景下跨视图验证不足的问题。通常 RL 使用二元奖励（正确/错误），但 TVR 任务中单一二元信号限制了探索效率。本文将奖励分解为参照选择奖励 $R_{\text{ref}}$ 与答案奖励 $R_{\text{ans}}$，并引入细粒度转换级奖励与双重惩罚机制。

$$
R^{\text{total}} = R^{\text{ans}} + R_{\text{ref}}
$$

该公式将总奖励解耦为答案正确性与参照对象选择准确性两项，引导模型同时优化最终输出与中间推理步骤。对于每个转换 $t_i$，奖励函数定义为：

$$
R^{\text{pos}}(t_i) = \begin{cases} 5.0, & \text{if } t_i \text{ exactly matches} \\ 1.5, & \text{if } (\text{index}_i, \text{attribute}_i) \text{ match} \\ 0.5, & \text{if only } \text{index}_i \text{ matches} \\ 0.0, & \text{otherwise} \end{cases}
$$

此公式通过部分匹配奖励鼓励渐进式学习，避免模型因单一错误而完全失去梯度信号。惩罚机制 $R^{\text{pun}}$ 对错误预测施加 -1.0 惩罚，并对预测数量不足施加额外惩罚，防止模型通过枚举所有可能三元组来规避错误。

## 实验评估

实验在 TVR、MMSI-Bench、MindCube-Tiny 和 SPAR-Bench 上进行，基线覆盖开源模型（Qwen2.5-VL、InternVL）与闭源模型（GPT-4o、o3），但缺失 GeoWeaver 等显式几何接地方法的直接对比。

| 模型 | TVR TAcc↑ | MMSI-Bench↑ | MindCube-Tiny Rotation↑ | SPAR-Bench ObjRel-OC-MV↑ |
| :--- | :--- | :--- | :--- | :--- |
| STAR-SFT | 48.7 | 27.3 | 54.0 | 67.8 |
| STAR-R1 | 61.4 | 31.4 | 98.5 | 86.0 |
| GPT-4o | 23.5 | - | 30.3 | 58.0 |
| o3 | 36.0 | - | 41.0 | - |

STAR-R1 在 TVR TAcc 上超越 o3 25.4%，在 MindCube-Tiny Rotation 上达到 98.5%，接近人类水平 97.2%。然而，MMSI-Bench 成绩 31.4% 低于领域综述中记录的 39.4%，存在协议差异或数据子集不一致的可能。

| 组件 | TVR TAcc↑ | MindCube-Tiny Rotation↑ |
| :--- | :--- | :--- |
| w/o obj | 58.0 | 89.8 |
| w/o pun | 54.3 | 85.5 |
| STAR-R1 | 61.4 | 91.0 |

移除对象选择奖励导致 TVR TAcc 下降 3.4%，移除惩罚机制下降 7.1%，表明惩罚机制对抑制错误探索至关重要。在 OOD 场景下，RL 模型在 81% 的案例中显式建立跨视图对应，显著高于 SFT 的 67%，验证了 RL 诱导的跨视图验证倾向。

评估协议局限在于：TVR 任务依赖合成数据，真实世界噪声未充分覆盖；MMSI-Bench 成绩与领域记录值冲突，需核实评估细节；论文未报告置信区间，数值比较需谨慎。代码未公开，复现依赖 8×H20 GPU 的特定配置，超参数细节仅在补充材料中提供。

## 关联研究分析

从问题动机看，STAR-R1 与 ViewFusion 均解决多视角对齐问题，但 ViewFusion 依赖结构化思维链的监督学习，假设模型可通过 CoT 数据习得对齐能力；STAR-R1 则通过 RL 探索发现对齐策略，其核心差异在于优化范式：监督学习优化固定轨迹，RL 优化探索过程。这一差异源于任务特性：TVR 任务的转换关系具有组合爆炸性，SFT 难以覆盖所有视角组合，而 RL 可通过奖励信号引导模型发现未见的对应模式。

从方法设计看，STAR-R1 与 GeoWeaver 构成显式 vs 隐式几何接地的对比。GeoWeaver 注入深度图作为硬约束，STAR-R1 通过对象锚点隐式学习几何关系。STAR-R1 在 MindCube-Tiny Rotation 上超越 GeoWeaver 的 57.9%（据领域综述），表明在特定任务上隐式学习可能优于显式接地。然而，MMSI-Bench 上 STAR-R1 的 31.4% 低于 GCA 的 64.8%（据领域知识），暗示隐式方法在复杂多图像推理中可能缺乏鲁棒性。RL 奖励中的对象选择项是否足以替代显式几何接地，在遮挡严重场景下尚无定论。

## 总结

STAR-R1 解决的核心矛盾是 SFT 模型在视角变化下跨视图验证不足，而纯 RL 缺乏稳定冷启动。本文抓住的切入点是：RL 可诱导模型自发形成对象锚定行为，通过过程监督冷启动与参照感知 RL 的两阶段策略实现鲁棒跨视图推理。实验证明其在 MindCube-Tiny Rotation 上达到 98.5%，TVR TAcc 超越 o3 25.4%。本文的边界在于 MMSI-Bench 成绩低于领域记录值，且缺失显式几何接地方法的直接对比。当支持集增大到 5-shot 时，参照选择奖励的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_754513fa29c3)