# AAAI2026最新论文 ｜StoryBox: Collaborative Multi-Agent Simulation for Hybrid Bottom-Up Long-Form Story Generation Using Large Language Models ｜混合自底向上长程故事生成

研究机构：中山大学

作者：Zehao Chen、Rong Pan、Haoran Li

论文原文见 [arXiv](https://arxiv.org/abs/2510.11618)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.11618)

> 长程叙事生成面临结构僵化与细节缺失的双重困境，传统自顶向下方法先定大纲再填充，导致情节发展受限且角色行为缺乏动态性。StoryBox 将多智能体沙盒模拟作为叙事素材源，通过智能体交互涌现事件，再由 Storyteller Agent 进行自底向上的章节迭代生成。该方法在 20 个自建场景上实现了平均 12,000 词的连贯故事，但在科学验证与定量诊断上缺乏严格标准，其“涌现”质量仍依赖主观评估。

## 研究背景

长程故事生成的核心挑战在于维持数千词尺度下的逻辑连贯性与角色一致性。传统自顶向下方法（如 DOC-V2, Re[3]）先构建故事大纲，再逐章扩展，这种预设结构虽保证了宏观框架，却限制了角色行为的自然演化，导致情节显得机械且可预测。与此同时，基于大语言模型（LLM）的多智能体模拟（如 Generative Agents, IBSEN）虽能产生动态交互，但多用于短剧本或社会动力学研究，缺乏将离散交互事件转化为长程连贯叙事的系统性机制。

现有方案在“结构控制”与“内容涌现”之间难以平衡。自顶向下框架牺牲了微观行为的丰富性，而纯模拟方法则缺乏宏观叙事结构的约束，导致事件碎片化。StoryBox 的切入点在于提出“混合自底向上”范式：利用多智能体沙盒模拟生成具有时间戳和上下文细节的涌现事件，作为叙事的“原材料”；同时引入 Storyteller Agent，通过动态窗口摘要与迭代检索，将这些离散事件组织为具有起承转合的长程故事。这一设计旨在保留模拟的自发性的同时，通过生成式控制实现宏观结构的连贯。

## 核心方法

### 方法参照系

本文问题可置于“基于 LLM 的叙事生成”通用流程中，但关键差异在于事件来源。传统流程依赖预定义大纲或单一 LLM 直接生成，而 StoryBox 将“事件生成”与“故事写作”解耦，前者由多智能体模拟驱动，后者由专用 Agent 驱动，形成“模拟-摘要-生成”的三级流水线。

### 多智能体沙盒模拟与事件涌现

沙盒模拟是故事素材的源头，其设计动机在于解决传统生成中角色行为缺乏“意外性”与“环境交互”的问题。每个智能体由 Persona Scratch Information 定义，包含 Name, Age, Innate, Learned, Currently, Lifestyle 等静态属性，以及动态的 Daily Plan Requirements。为打破日常行为的单调性，引入 Abnormal Factor $\alpha$，控制智能体偏离日常计划、执行冲突或探索行为的概率。智能体行为分为 move, chat, none 三类，每次交互生成一个事件 $e_i$，其结构定义为：

$$
e_i = \{ id, t_{start}, t_{end}, participants, location, description, detail \}
$$

其中 $detail$ 包含环境状态、角色情绪及动机等上下文信息，确保事件不仅是动作记录，更是叙事素材。该设计使得事件具有时间连续性与空间关联性，为后续摘要提供丰富的语义基础。

### 动态窗口摘要与迭代故事生成

Storyteller Agent 负责将离散事件转化为连贯故事，其核心创新在于“动态窗口摘要”与“迭代章节生成”机制。由于沙盒事件数量庞大，直接输入 LLM 会超出上下文窗口，因此首先按角色和日期进行初步摘要，随后引入动态窗口机制，由 LLM 自适应决定窗口大小 $W$，将事件分组并压缩为摘要序列 $S = \{s_1, s_2, ..., s_k\}$。故事生成采用迭代循环：首先确定故事类型与标题，然后逐章生成。第 $j$ 章的生成输入包括：当前章节信息、前 $j-1$ 章的摘要历史 $H_{j-1}$，以及通过向量检索从事件库中获取的相关事件 $R_j$。章节生成后，其摘要被追加至 $H_j$，形成闭环。这一机制确保了长程叙事中信息的渐进式披露与逻辑连贯，避免了传统方法中因上下文截断导致的情节断裂。

## 实验评估

实验在 20 个自建故事场景上进行，基线包括 Vanilla LLMs (GPT-4o, DeepSeek-V3)、Structured Frameworks (Re[3], DOC-V2) 及 Multi-Agent Simulations (IBSEN)。评估采用人类与 LLM 双评，涵盖 Plot, Creativity, Character Development, Language Use, Conflict Quality, Overall 六个维度，以及 Character Behavior Consistency 和 Average Word Count。

| 方法 | Avg. Word Count | Plot | Creativity | Char. Dev. | Lang. Use | Conf. Qual. | Overall |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| GPT-4o | ~1,000 | 3 | 4 | 3 | 4 | 3 | 3 |
| DeepSeek-V3 | ~1,000 | 3 | 2 | 3 | 3 | 3 | 3 |
| Re[3] | ~10,000 | 4 | 4 | 4 | 4 | 4 | 4 |
| DOC-V2 | ~10,000 | 4 | 4 | 4 | 4 | 4 | 4 |
| IBSEN | ~10,000 | 4 | 4 | 5 | 4 | 4 | 4 |
| StoryBox | ~12,000 | 5 | 5 | 5 | 5 | 5 | 5 |

*注：表中数值为基于 Figure 4 趋势的定性排名映射，原文未提供具体分数，仅显示相对强弱。StoryBox 在所有维度上均排名第一，平均词数约 12,000，显著高于基线的 1,000-10,000 词。*

消融实验显示，移除 Abnormal Behavior 导致 Creativity 和 Conflict Quality 下降最显著，证实了“意外性”对叙事张力的关键作用；移除 Object Description 主要影响 Language Use，说明环境细节对语言丰富度的贡献；禁用 Dynamic Window 则降低 Plot 连贯性，验证了动态摘要在长程一致性中的必要性。

评估边界方面，本文依赖主观评分，缺乏定量诊断工具（如耦合增益）来区分真实社会动力学与模型伪影。可复现性上，代码已开源，但模拟耗时较长（14 天模拟需约 7 小时），且依赖 GPT-4o mini 等特定模型，跨模型泛化性未充分验证。

## 关联研究分析

从问题动机看，StoryBox 与 IBSEN 同属多智能体叙事生成，但 IBSEN 侧重短剧本的导演-演员协作，而 StoryBox 聚焦长篇小说的自底向上涌现。差异根源在于任务尺度：长程叙事需要更复杂的事件摘要与状态管理机制，IBSEN 的短程设计无法处理 12,000 词以上的上下文依赖。从方法设计看，StoryBox 与 Generative Agents 共享角色建模思路，但将环境模型从网格改为树状结构，以支持更灵活的空间探索。这一改动是否导致事件空间过于稀疏，进而影响情节密度，论文未给出定量分析。

## 总结

StoryBox 解决了长程叙事生成中结构僵化与细节缺失的矛盾，通过多智能体模拟提供涌现事件，并利用动态窗口摘要与迭代生成实现宏观连贯。实验证明其在长度（12,000 词）与多维质量上优于基线，但评估仍依赖主观评分，缺乏对“涌现”质量的定量诊断。当模拟时长从 1 天延长至 30 天时，故事质量的提升是否呈线性增长，还是存在边际递减效应，论文未给出明确回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.11618)