# HuggingFace最新推荐论文 ｜MintAct: A Unified Visual Agent for Digital Environments ｜统一视觉智能体

作者：Mingfei Gao、Rui Tian、Haiming Gang 等 14 人

论文原文见 [arXiv](https://arxiv.org/abs/2609.22083)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.22083)

> 导读 多域GUI智能体长期面临“单域专家模型碎片化”与“统一模型性能折损”的矛盾，现有方案要么维护多个独立模型导致部署成本高昂，要么简单混合训练引发域间干扰。MintAct的切入点是构建一套显式控制跨域训练分布的异步强化学习（RL）基础设施，结合多阶段监督微调（SFT）与拒绝采样微调（RFT）蒸馏，在2B-8B轻量级规模下实现UI定位、多步导航与视觉工具调用的统一。其价值在于证明了统一架构无需牺牲单域性能，但联合RL阶段仅覆盖移动与桌面域，Web域的性能增益是否源于跨域迁移而非直接优化，论文未提供直接证据。

## 研究背景

GUI智能体从像素截图直接操作数字设备时，必须同时处理UI元素定位（Grounding）、跨平台多步导航及外部工具调用。定位精度决定操作成功率，而多步导航中的错误累积会放大早期微小偏差，工具调用则要求模型将视觉上下文映射为结构化API请求。这三类能力在观察空间、动作类型与环境反馈机制上存在本质差异，构成了统一建模的核心挑战。

当前主流路线将上述能力解耦为独立模型：移动导航依赖MAI-UI等端云协同架构，桌面控制依托UI-TARS的高分辨率定位，Web导航由Weblica等可复现环境驱动。这种碎片化导致服务成本随域数量线性增长，且在端侧部署时难以维持多模型并行。更关键的是，简单合并各域动作空间或混合训练数据会引发域间干扰，导致单域性能下降。MintAct的切入点在于，不追求动作空间的物理合并，而是通过提示词条件化与显式分布控制，在单一权重集合中实现能力解耦与协同优化。

## 核心方法

### 统一策略架构与提示词条件化

MintAct将UI定位、导航与工具调用统一为单一策略函数 $\pi_\theta(a_t | s)$，其中状态 $s$ 包含系统提示 $c$、指令 $g$、历史观察 $o_{\leq t}$ 及先前动作 $a_{<t}$。设计动机在于避免朴素合并动作空间导致的域间干扰：不同域的动作集通过域特定的系统提示 $c$ 条件化，模型在推理时根据目标域提示生成对应动作，而非在混合动作空间中盲目选择。这一设计使得感知与定位能力（基于归一化像素坐标）可直接跨域迁移，而动作生成则保持域特异性。

### 异步RL框架与截断重要性比率

多域混合训练的核心瓶颈在于异构环境后端的延迟差异：同步流水线需等待最慢环境，而异步流水线中快速环境会主导数据分布，破坏训练平衡。MintAct的异步RL框架通过消息队列解耦轨迹生成与策略优化，并引入截断重要性比率 $\rho_{i,t}$ 处理off-policy漂移：

$$
\rho_{i,t} = \exp\left(\text{clip}\left(\log \pi_{\text{prox}}(a_{i,t} | s_{i,t}) - \log \pi_{\text{roll}}(a_{i,t} | s_{i,t}), \pm\kappa\right)\right)
$$

该公式对rollout策略与proximal策略的对数概率差进行截断，防止数值不稳定。设计动机在于，异步训练中轨迹可能由过期策略生成，且rollout与训练引擎间存在数值差异，直接优化会导致策略崩溃。截断机制将重要性权重限制在 $[1/C, C]$ 范围内（$C=2$），确保梯度更新稳定，同时通过显式采样比例控制跨域数据分布，避免快速域主导训练。

### RFT蒸馏与联合RL

单域RL专家在各自域上优化后，通过拒绝采样微调（RFT）蒸馏回单一模型：每个专家在其域SFT任务上生成轨迹，VLM评判器筛选成功轨迹，SFT模型在筛选数据上微调。设计动机在于，单域RL专家可能过拟合特定域，而RFT通过高质量轨迹蒸馏保留各域优势，同时维持单一权重集合。最终联合RL阶段在移动与桌面域上进一步优化，验证了跨域迁移的有效性。

## 实验评估

MintAct在OSWorld-Verified、AndroidWorld、Weblica等基准上对比Qwen3-VL、UI-TARS、MAI-UI等基线。基线覆盖单域专家与通用模型，但缺失SeeClick等早期纯SFT基线，可能低估SFT的贡献。主实验显示，MintAct-8B在OSWorld-Verified达48.9，AndroidWorld达67.0，Weblica达74.7，均优于同规模开源模型，但低于知识库中OS-Symphony（GPT-5骨干）的65.84%。

| 模型 | OSWorld-Verified | AndroidWorld | Weblica | MMToolSandBox |
| :--- | :--- | :--- | :--- | :--- |
| Qwen3-VL-8B | 47.6 | 65.2 | 55.5 | 3.1 |
| MintAct-8B-Final | 48.9 | 67.0 | 74.7 | 24.5 |
| MAI-UI-8B | – | 69.1 | – | – |
| EvoCUA-8B | – | – | – | – |

消融实验揭示关键设计决策的影响：Stage 1（高分辨率单步SFT）单独训练时UI-Vision达59.3，但OSWorld-Verified仅9.4；Stage 2（低分辨率多步SFT）单独训练时OSWorld-Verified恢复至41.5，但UI-Vision降至25.0。两阶段结合后UI-Vision为56.9，OSWorld-Verified为42.6，证明两阶段互补性。RFT阶段在移动域上超越单域RL专家（AndroidWorld 68.1 vs. 67.8），表明蒸馏有效保留单域优势。

| 阶段 | UI-Vision | OSWorld-Verified | AndroidWorld |
| :--- | :--- | :--- | :--- |
| Stage 1 only | 59.3 | 9.4 | 70.0 |
| Stage 2 only | 25.0 | 41.5 | 60.7 |
| Stage 1 + 2 | 56.9 | 42.6 | 71.0 |

评估边界方面，论文未报告置信区间，数值比较需谨慎。联合RL仅优化移动与桌面域，Web域性能增益（Weblica从72.8至74.7）可能源于跨域迁移而非直接优化，论文未提供Web域联合RL的消融。代码未公开，但环境基础设施基于OSWorld与AndroidWorld，可复现性依赖这些开源基准。

## 关联研究分析

从问题动机看，MintAct与MAI-UI均关注端侧部署与在线RL，但MAI-UI侧重单域（移动）的端云协同，而MintAct追求多域统一。这一差异源于任务特性：MAI-UI假设移动域为唯一目标，而MintAct需处理跨域泛化。MintAct的提示词条件化设计解决了MAI-UI未涉及的域间干扰问题，但代价是增加了系统提示的复杂度，且未验证提示词对长程任务记忆的影响。

从方法设计看，MintAct与AsyncWebRL同属异步RL框架，但AsyncWebRL仅针对Web域，而MintAct扩展至多域混合分布控制。这一差异源于环境异构性：Web环境延迟相对均匀，而移动/桌面/Web混合训练需显式控制采样比例。MintAct的截断重要性比率机制处理了AsyncWebRL未涉及的off-policy漂移问题，但论文未对比不同截断参数 $\kappa$ 对性能的影响，该参数选择是否敏感，论文未给出回答。

## 总结

MintAct解决的核心矛盾是多域GUI智能体的碎片化部署与统一模型性能折损。其切入点在于通过提示词条件化与显式分布控制的异步RL，在单一权重中实现能力解耦。方法上，MintAct结合多阶段SFT、RFT蒸馏与联合RL，在8B规模下OSWorld-Verified达48.9，AndroidWorld达67.0。边界在于联合RL仅覆盖移动与桌面域，Web域增益来源不明，且未报告置信区间。当Web域引入联合RL后，其性能是否进一步提升，还是因跨域干扰而下降，论文未提供直接证据。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.22083)