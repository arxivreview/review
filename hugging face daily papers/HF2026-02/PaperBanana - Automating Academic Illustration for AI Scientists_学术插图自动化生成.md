# HuggingFace最新推荐论文 ｜PaperBanana: Automating Academic Illustration for AI Scientists ｜学术插图自动化生成

研究机构：北京大学

作者：Dawei Zhu、Rui Meng、Yale Song 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.23265)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.23265)

> 自主AI科学家在文献综述与代码执行上已展现能力，但将科学发现转化为符合顶级会议规范的可视化插图仍是人力密集瓶颈。现有代码生成范式难以表达复杂视觉元素，而通用图像生成模型又缺乏学术严谨性。本文提出PaperBanana，通过五智能体协作与参考驱动机制，将方法论描述映射为出版级插图。该框架在自建基准上显著优于基线，但其评估依赖VLM裁判，且连接错误等基础模型局限仍未解决。

## 研究背景

当AI科学家生成复杂方法论时，将其转化为直观的流程图或架构图是沟通的关键。这一过程要求同时满足内容忠实度（准确反映技术细节）与视觉美学（符合学术出版规范）。传统代码生成方法（如TikZ、SVG）虽能处理结构化内容，但面对现代AI论文中常见的定制图标、复杂形状时，表达力受限。反之，通用图像生成模型虽具备强大的指令遵循能力，却难以稳定产出符合学术标准的插图，常出现事实性错误或风格不协调。

当前AI科学家系统多聚焦于假设生成、实验迭代等核心科研环节，对“可视化沟通”这一必要但常被忽视的环节关注不足。主流路线要么依赖代码编程，要么直接调用图像模型，均无法兼顾逻辑严谨性与视觉专业性。PaperBanana的切入点在于引入“参考驱动”的多智能体协作机制，通过检索高质量学术插图作为风格与结构指南，弥补单一模型在学术规范理解上的缺失。

## 核心方法

### 方法参照系

学术插图生成可视为从源上下文 $S$ 和沟通意图 $C$ 到视觉表示 $I$ 的映射。与通用图像生成不同，该任务要求严格的内容忠实度与特定的学术美学规范。现有方法通常直接提示图像模型，缺乏对学术风格的结构化约束，导致输出常偏离出版标准。

### 参考驱动的多智能体协作

PaperBanana的核心创新在于引入Retriever、Planner、Stylist、Visualizer、Critic五个智能体，形成线性规划与迭代优化闭环。Retriever从参考集 $\mathcal{R}$ 中检索 $N$ 个最相关示例 $\mathcal{E}$，其选择基于视觉结构而非主题相似性，公式为：

$$ \mathcal{E} = \text{VLM}_{\text{retriever}}(S, C, \mathcal{R}) $$

这一设计解决了直接生成时缺乏风格锚点的问题，使Planner能基于具体示例进行上下文学习，生成详细文本描述 $P$。Stylist智能体进一步遍历参考集，自动合成美学指南 $\mathcal{G}$，优化描述为 $P^*$，确保输出符合学术审美。

### 迭代优化与自我纠错

Visualizer与Critic构成迭代优化循环，执行 $T=3$ 轮。Visualizer将描述 $P_t$ 转化为图像 $I_t$，Critic则对照源上下文 $(S, C)$ 检查事实错误与视觉瑕疵，生成修正描述 $P_{t+1}$：

$$ P_{t+1} = \text{VLM}_{\text{critic}}(I_t, S, C, P_t) $$

该机制解决了单次生成中常见的事实性错误与风格不一致问题。通过多轮反馈，系统能逐步修正连接错误、冗余元素等细节，最终输出 $I_T$ 满足出版级要求。对于统计图，Visualizer转为生成Matplotlib代码，确保数值精度。

## 实验评估

实验基于自建PaperBananaBench（292例NeurIPS 2025插图），对比Vanilla、Few-shot、Paper2Any基线。主结果显示，PaperBanana在Overall得分上达60.2%，较Vanilla Nano-Banana-Pro（43.2%）提升17.0%，在Conciseness（+37.2%）与Readability（+12.9%）上优势显著。

| 方法 | Faithfulness | Conciseness | Readability | Aesthetic | Overall |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Vanilla Nano-Banana-Pro | 43.0 | 43.5 | 38.5 | 65.5 | 43.2 |
| Few-shot Nano-Banana-Pro | 41.6 | 49.6 | 37.6 | 60.5 | 41.8 |
| Paper2Any | 6.5 | 44.0 | 20.5 | 40.0 | 8.5 |
| **PaperBanana (Ours)** | **45.8** | **80.7** | **51.4** | **72.1** | **60.2** |
| Human | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |

消融实验表明，Stylist智能体提升Conciseness（+17.5%）但降低Faithfulness（-8.5%），Critic智能体则有效弥补这一损失，恢复Faithfulness。Retriever的语义检索与随机检索效果相近，暗示通用结构模式比精确内容匹配更重要。评估采用VLM-as-a-Judge，与人类标注的Kendall’s tau相关性为0.45，虽达“较强一致性”标准，但主观性仍存。代码与超参数已开源，但图像生成模型（Nano-Banana-Pro）的特定参数设置限制了跨模型复现性。

## 关联研究分析

从问题动机看，PaperBanana与DeepScientist等多智能体科研系统共享“分工协作”架构，但前者聚焦视觉生成，后者侧重假设验证。DeepScientist依赖贝叶斯优化进行资源分配，而PaperBanana采用固定迭代轮次，因视觉生成无需动态资源调度。这一差异源于任务特性：插图生成是确定性映射，而科学发现是开放探索。

从方法设计看，PaperBanana的Stylist智能体与ToolUniverse等基础设施不同，后者解决工具接口标准化，前者解决美学规范自动化。PaperBanana未涉及工具调用，而是直接依赖图像生成模型，这限制了其处理复杂代码生成任务的能力。与Paper2Any相比，后者侧重高层想法呈现，而PaperBanana强调方法论细节忠实度，导致其在Faithfulness上显著优于Paper2Any（45.8% vs 6.5%）。

## 总结

PaperBanana解决了学术插图生成中内容忠实度与视觉美学的矛盾，通过参考驱动的多智能体协作，将出版级插图生成从人力密集任务转化为自动化流程。其核心贡献在于验证了“检索-规划-风格-渲染-批评”闭环的有效性，在自建基准上Overall得分达60.2%，较基线提升17.0%。然而，实验暴露了基础模型的感知局限：Critic智能体常无法识别连接错误，导致最终输出仍存在逻辑瑕疵。当参考集涵盖非主流学术风格时，Stylist智能体自动合成的美学指南是否仍能保持忠实度，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.23265)