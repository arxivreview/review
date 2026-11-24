# ACL-Findings2026最新论文 ｜MobileBench-OL: A Comprehensive Chinese Benchmark for Evaluating Mobile GUI Agents in Real-World Environment ｜移动图形用户界面智能体真实环境基准

研究机构：小米、北京大学

作者：Qinzhuo Wu、Zhizhuo Yang、Hanhao Li 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.20335)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.20335)

> 移动图形用户界面智能体（Mobile GUI Agent）需在动态、含噪的真实设备上执行多步操作，但现有在线基准多依赖模拟器且忽略环境噪声，导致评测与部署存在断层。本文提出MobileBench-OL，通过80个中文应用中的1080个任务及5个子集，覆盖基础能力、长程推理、GUI探索与噪声鲁棒性。其核心机制是结合基于XPath规则的自动评估框架与细粒度重置机制，确保评测的可重复性。该基准揭示了当前智能体在真实噪声下的显著性能衰减，但其缺乏跨应用任务且仅限中文生态，限制了结论的普适性。

## 研究背景

GUI智能体的评测面临从“静态截图匹配”向“动态交互验证”的范式转移。早期基准如Mind2Web依赖预定义轨迹，无法处理多路径解；随后的AndroidWorld引入模拟器动态环境，解决了状态反馈问题，但模拟器环境与真实设备在资源调度、网络延迟及广告干扰上存在系统性差异。这种差异导致在模拟器上表现优异的模型，在真实设备上可能因无法处理非结构化干扰（如弹窗、加载延迟）而失败。

现有在线基准的瓶颈在于任务设计的“刚性”与环境的“洁净”。AndroidWorld等基准的任务多为原子操作或步骤明确的指令遵循，缺乏对智能体自主探索与错误恢复能力的考察。同时，真实移动端环境充满不可预测性，如广告弹窗阻断操作流、网络延迟导致元素不可见，这些噪声在现有基准中被忽略。MobileBench-OL的切入点正是填补这一空白：它不满足于测试“能否完成”，而是测试“在混乱中能否完成”，通过引入随机噪声注入与长程探索任务，构建了一个更接近真实部署场景的评测坐标系。

## 核心方法

### 基准架构与子集设计

MobileBench-OL将评测维度解耦为五个子集，以覆盖从基础执行到复杂推理的全谱系。Base与Long-Tail子集评估基础能力，其中Long-Tail聚焦68个长尾应用，测试模型在陌生UI结构下的泛化性；Long-Horizon子集包含60个至少20步的任务，考察长程记忆与子任务分解；GUI-Reasoning子集通过权重机制量化探索难度；Noise-Robust子集则在推理过程中随机注入噪声。这种设计打破了单一成功率指标的局限，通过多维诊断揭示模型失效的具体环节。

### 噪声注入与鲁棒性评估

Noise-Robust子集的核心创新在于将真实环境噪声形式化为可控制的实验变量。在轨迹生成过程中，每一步以20%的概率触发四种噪声之一：Repeat（动作重复执行）、Unexecuted（动作未执行）、Delay（页面加载延迟）及Pop-up（弹窗阻断）。噪声注入机制可形式化为：

$$
\mathcal{N}(s_t, a_t) = \begin{cases}
a_t \text{ executed twice}, & \text{if } \mathcal{N} = \text{Repeat} \\
\emptyset \text{ (no state change)}, & \text{if } \mathcal{N} = \text{Unexecuted} \\
s_{t+1} = s_t \text{ (loading state)}, & \text{if } \mathcal{N} = \text{Delay} \\
s_{t+1} = s_{popup}, & \text{if } \mathcal{N} = \text{Pop-up}
\end{cases}
$$

其中 $s_t$ 为当前状态，$a_t$ 为动作。该设计动机在于解决现有基准中“环境静止”假设的失效问题。通过随机注入，模型必须学会区分“动作未生效”与“环境变化”，从而评估其状态估计与恢复能力，而非仅依赖确定性轨迹。

### 自动评估与重置机制

为解决真实设备状态漂移导致的评测不可复现问题，MobileBench-OL引入了基于XPath规则的自动评估框架（Auto-Eval）与细粒度重置机制。任务成功条件定义为基于GUI属性（如text, resource-id, package）的逻辑表达式，例如：

$$
\text{Success} = \bigwedge_{i=1}^{k} \left( \exists e \in \mathcal{E} : \text{XPath}(e) \land \text{bbox\_contains\_point}(e, p_i) \right)
$$

其中 $\mathcal{E}$ 为界面元素集合，$p_i$ 为交互点坐标。该公式确保评估的完备性（所有成功轨迹满足条件）与健全性（无失败轨迹满足条件）。重置机制通过执行逆向任务（如“关闭高级模式”）恢复设备状态，其成功率经人工验证超过90%，解决了真实设备评测中“状态污染”这一关键工程难题。

## 实验评估

实验在12个主流GUI智能体上进行，包括GPT-4o、UI-TARS-1.5等闭源与开源模型。基线覆盖了基于SFT的专用模型（如UI-TARS）与通用多模态大模型（如GPT-4o），但缺失了近期基于强化学习（RL）的最新方法（如MobileRL、UI-S1），这可能低估了当前SOTA在动态环境中的真实水平。

| 模型 | Base SR (%) | Long-Horizon SR (%) | GUI-Reasoning SR (%) | Noise-Robust SR (%) |
| :--- | :--- | :--- | :--- | :--- |
| GPT-4o | 30.32 | 0.00 | 21.67 | 27.10 |
| UI-TARS-1.5-7B | 60.97 | 15.00 | 38.33 | 56.77 |
| Qwen2.5-VL-7B | 42.35 | 1.67 | 30.77 | 41.84 |
| Mobile-Agent-V2 | 23.74 | 3.33 | 25.00 | 16.45 |

UI-TARS-1.5在Base子集取得60.97%的成功率，但在Long-Horizon子集骤降至15.00%，表明长程记忆与子任务分解是当前模型的主要瓶颈。在Noise-Robust子集中，UI-TARS-1.5的56.77%虽为最高，但相比Base子集仍有显著下降，证实了噪声对智能体鲁棒性的负面影响。

消融分析显示，GUI-Reasoning子集中，随着探索权重增加，成功率从Easy任务的38.46%（M3A）降至Hard任务的26.09%（M3A），说明模型在深层菜单导航与隐藏功能发现上存在系统性缺陷。Long-Horizon错误分析表明，属性错误（Attribute Errors）占比25.0%，远高于子任务遗漏（6.7%），揭示模型在长轨迹中难以维持对关键属性（如选中状态、数值）的跟踪。

评估边界方面，Auto-Eval框架经人工验证准确率达97.50%，但存在少量假阴性（FN），可能低估部分成功轨迹。重置机制依赖逆向任务的定义，对于不可逆操作（如服务器交互）需扩展成功条件，这可能引入评估偏差。代码与数据声明将在接收后发布，当前缺乏开源实现，限制了第三方复现与扩展。

## 关联研究分析

从问题动机看，MobileBench-OL与AndroidWorld的核心差异在于环境真实性的定义。AndroidWorld基于模拟器，强调动态状态反馈，但忽略了真实设备的非确定性干扰；MobileBench-OL则通过噪声注入模拟真实世界的“混乱”，但其任务仍限于单应用内，未涉及跨应用工作流。这种差异源于任务特性的不同：模拟器便于控制变量，而真实设备评估需处理不可控因素。MobileBench-OL的噪声机制虽新颖，但其20%的固定概率是否反映真实分布，论文未提供实证支持，这可能影响鲁棒性评估的外部效度。

从方法设计看，MobileBench-OL的Auto-Eval框架与ProBench的过程级评估理念一致，均强调中间步骤的正确性，但MobileBench-OL依赖XPath规则，而ProBench使用MLLM评估器。XPath规则具有确定性高、成本低的优势，但灵活性差，难以处理语义模糊的任务；MLLM评估器则相反。MobileBench-OL选择XPath规则，反映了其对“可复现性”的优先考量，但这可能限制了其对复杂语义任务的覆盖。此外，MobileBench-OL未对比基于RL的最新方法，如MobileRL，这可能因其真实设备评估的高成本与RL训练的不稳定性所致，但这也使得基准的SOTA定位存在滞后性。

## 总结

MobileBench-OL旨在解决GUI智能体评测中“模拟器与真实环境断层”的核心矛盾，通过引入噪声鲁棒性与长程探索维度，构建了更贴近部署场景的评测体系。其Auto-Eval框架与重置机制确保了评测的可重复性，实验揭示当前模型在长程任务（15.00% SR）与噪声环境（56.77% SR）下的显著性能衰减。然而，基准局限于中文单应用生态，且缺乏跨应用任务与最新RL方法的对比，限制了其作为通用SOTA参照系的地位。当噪声概率从20%提升至更真实的分布时，智能体的鲁棒性是否呈现非线性衰减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.20335)