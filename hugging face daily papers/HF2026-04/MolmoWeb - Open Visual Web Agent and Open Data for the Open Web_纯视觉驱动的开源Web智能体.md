# HuggingFace最新推荐论文 ｜MolmoWeb: Open Visual Web Agent and Open Data for the Open Web ｜纯视觉驱动的开源Web智能体

研究机构：美国艾伦人工智能研究所、美国华盛顿大学

作者：Tanmay Gupta、Piper Wolters、Zixian Ma 等 16 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.08516)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.08516)

> 开放网络中的Web智能体面临闭源模型黑盒化与DOM解析脆弱性的双重困境，导致研究可复现性差且动态页面接地误差高。现有开源方案多依赖结构化文本输入或大规模参数，而本文切入点在于证明高质量数据混合可补偿模型规模与输入模态的缺失。通过构建MolmoWebMix数据集并训练纯视觉动作策略，MolmoWeb在保持4B/8B小参数量下超越了依赖AxTree的闭源大模型。其价值在于确立了开源Web智能体的性能基线，但Pass@k机制对单步鲁棒性的掩盖效应仍存疑。

## 研究背景

Web智能体在动态网页中执行任务时，需将自然语言指令映射为像素级操作。这一过程依赖感知接地（Grounding），即准确定位UI元素。传统方法依赖文档对象模型（DOM）或无障碍树（AxTree），但这类结构化表示在动态渲染页面中易出现节点缺失或坐标偏移，且单页AxTree输入可消耗数万token，导致上下文窗口爆炸。为解决此问题，研究转向视觉语言模型（VLM），直接以截图作为观察空间，利用视觉模态的紧凑性规避结构化解析的脆弱性。

当前领域主流路线分为两类：一是基于闭源前沿模型（如GPT-4o）的Set-of-Marks（SoM）提示策略，通过叠加标记增强视觉输入，但依赖专有API且不可复现；二是开源小模型（如Fara-7B）结合DOM文本输入，虽可复现但受限于结构化数据的噪声。MolmoWeb的切入点在于彻底摒弃文本结构输入，仅使用截图，并通过大规模多源数据混合（合成+人类+感知）训练小参数模型，验证数据质量能否替代模型规模与丰富输入。

## 核心方法

### 方法参照系

本文遵循ReAct范式，即推理-行动交替循环。与标准流程的关键差异在于观察空间仅包含截图，排除了DOM/AxTree文本，且动作空间为归一化像素坐标，要求模型具备纯视觉接地能力。

### 多源数据混合策略

MolmoWebMix通过四类数据源构建训练集，旨在同时教会模型“看懂”截图与“执行”任务。设计动机在于解决单一合成数据分布偏差与人类数据标注成本高的矛盾。数据混合比例如下：

$$
\mathcal{D}_{mix} = 0.80 \cdot \mathcal{D}_{traj} + 0.20 \cdot \mathcal{D}_{perc}
$$

其中 $\mathcal{D}_{traj}$ 包含278.5K条轨迹（合成与人类），$\mathcal{D}_{perc}$ 包含10.5M条感知数据。轨迹生成采用AxTree代理、多智能体（Planner/Operator/Verifier）及节点遍历三种管线，经VLM裁判过滤失败样本。感知数据包含7M+接地对（Grounding）与2.2M截图问答（Screenshot QA），接地坐标采用截断高斯分布采样，鼓励空间鲁棒性。

### 纯视觉动作策略

MolmoWeb基于Molmo2架构，输入为任务指令、动作历史与当前截图，输出为JSON格式的Thought与Action。设计动机在于规避AxTree的token开销与结构脆弱性，使模型行为更贴近人类视觉交互。动作坐标归一化至[0, 100]，执行时反归一化为视口像素：

$$
a_t = \text{Denormalize}(\hat{a}_t, W, H)
$$

其中 $\hat{a}_t$ 为模型预测的归一化坐标，$W, H$ 为视口尺寸。该设计使模型无需访问底层HTML，仅依赖视觉界面，提升了跨网站泛化能力与可解释性。

## 实验评估

实验在WebVoyager、Online-Mind2Web、DeepShop及WebTailBench四个实时网站基准上进行。基线覆盖开源模型（Fara-7B, Holo1-7B）与闭源SoM代理（GPT-4o, o3）。MolmoWeb-8B在WebVoyager上取得78.2% Pass@1，超越GPT-4o SoM代理；在Online-Mind2Web上取得48.5%，略高于Avenir-Web的48.0%（据领域综述）。

| 策略 | WebVoyager Pass@1 (%) |
| :--- | :--- |
| Greedy (temp=0.0) | 61.4 |
| Top-k (temp=0.7, k=20) | 67.4 |
| Top-p (temp=0.7, p=0.8) | 68.5 |

采样策略消融显示，Top-p采样比Greedy提升7.1个百分点，表明随机性有助于克服局部状态停滞。Pass@k实验显示，MolmoWeb-8B在WebVoyager上Pass@4达94.7%，Online-Mind2Web达60.5%，远超Pass@1的78.2%与35.3%。

评估边界方面，论文未报告WebArena成绩，缺失与Branch-and-Browse等长程规划方法的直接对比。Pass@k机制依赖VLM裁判选择最佳轨迹，可能掩盖单步决策的高错误率。可复现性上，论文承诺发布代码与数据，但训练细节（如64 H100 GPU, 50K steps）已披露，超参数透明。

## 关联研究分析

从问题动机看，MolmoWeb与Fara-7B同属开源小模型路线，但Fara依赖AxTree文本输入，而MolmoWeb纯视觉。差异根源在于对“输入丰富度”的假设：Fara认为结构化文本提供精确语义，MolmoWeb认为视觉模态更紧凑且鲁棒。实验证明，在数据质量足够高时，纯视觉策略可超越依赖文本的闭源大模型，挑战了“输入越丰富越好”的共识。

从方法设计看，MolmoWeb与WebCoach（记忆机制代表）形成对比。WebCoach引入外部记忆存储（EMS）以解决长程任务中的“迷失在中间”问题，而MolmoWeb仅依赖上下文窗口内的10步动作历史。MolmoWeb未探索长期记忆，其Pass@k机制通过多次尝试弥补单步规划的脆弱性，而非通过记忆优化规划连贯性。这种取舍在短程任务中有效，但在需要跨会话一致性的长程任务中，缺乏记忆机制可能成为瓶颈。

## 总结

MolmoWeb解决的核心矛盾是开源Web智能体在性能与可复现性之间的失衡。其切入点在于证明数据质量可补偿模型规模与输入模态的缺失，通过MolmoWebMix混合数据训练纯视觉策略，在4B/8B规模下超越闭源SoM代理。实验证明MolmoWeb-8B在WebVoyager Pass@1达78.2%，Pass@4达94.7%。边界在于Pass@k机制对单步鲁棒性的掩盖，以及缺乏长期记忆对长程任务的限制。当任务步骤超过上下文窗口容量时，纯视觉策略在无记忆支持下的规划连贯性是否仍能维持，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.08516)