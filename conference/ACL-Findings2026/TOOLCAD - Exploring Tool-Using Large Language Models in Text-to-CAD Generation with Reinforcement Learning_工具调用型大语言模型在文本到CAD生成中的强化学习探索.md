# ACL-Findings2026最新论文 ｜TOOLCAD: Exploring Tool-Using Large Language Models in Text-to-CAD Generation with Reinforcement Learning ｜工具调用型大语言模型在文本到CAD生成中的强化学习探索

作者：Yifei Gong、Xing Wu、Wenda Liu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.07960)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07960)

> 文本到CAD生成旨在将自然语言指令转化为可执行的参数化建模操作，但现有方法多依赖静态序列预测或一次性代码生成，难以处理多部件复杂模型中的长程推理与错误累积。本文切入点在于将大语言模型（LLM）重构为工具调用智能体，通过交互式CAD引擎反馈与在线强化学习（RL）实现迭代式建模。具体做法是构建包含规则奖励与结果监督的混合反馈环境，利用课程学习策略训练LLM自主规划并调用CAD原语工具。该框架在开源模型上实现了接近闭源模型的性能，但其对L3级精确指令的依赖及缺乏多模态输入支持，限制了其在模糊设计意图场景下的泛化能力。

## 研究背景

CAD建模的核心挑战在于离散拓扑与连续几何的异质性，以及严格的水密性约束。传统方法将建模过程视为序列预测任务，如DeepCAD（2021）通过Transformer生成草图-拉伸命令序列，但此类方法受限于命令序列难以表达复杂拓扑（如圆角、倒角）及长序列误差累积问题。当LLM介入该领域后，研究分为两条路线：一是辅助Token预测，如Text2CAD（Khan et al., 2024）利用LLM对齐多模态输入与建模命令；二是代码生成，如CAD-Assistant（Mallis et al., 2024）生成可执行脚本。然而，现有LLM方法普遍缺乏与CAD引擎的实时交互机制，导致在复杂多部件任务中，模型无法根据执行结果进行自我修正，且离线训练策略难以应对分布外任务的泛化需求。

本文针对上述瓶颈，提出TOOLCAD框架，将LLM定位为工具调用智能体而非代码生成器。该框架通过Model Context Protocol（MCP）封装CAD原语，使LLM能够直接调用几何操作工具，并引入交互式CAD Gym提供实时反馈。核心创新在于结合规则基奖励与结果监督奖励模型（ORM），通过在线课程强化学习（GRPO）训练LLM在长程推理中保持工具调用的一致性，从而解决静态生成方法在复杂拓扑构建中的失效问题。

## 核心方法

### 方法参照系

本文问题可归类为基于LLM的参数化CAD生成，但与传统“Prompt-to-Code”范式存在关键差异。传统方法将LLM视为代码生成器，输出完整的Python脚本；而TOOLCAD采用“Prompt-to-Tool”范式，LLM输出结构化的工具调用指令（如`Sketch`, `Extrude`），由CAD引擎执行并返回反馈。这一差异使得模型能够利用引擎的实时状态进行反思与修正，而非依赖一次性生成的代码正确性。

### CAD-CoT推理与工具集成

设计动机在于解决LLM在复杂多部件建模中的参数幻觉与动作序列断裂问题。传统ReAct提示策略在处理密集数值参数（坐标、角度）时易产生不一致性。TOOLCAD定制了CAD-specific ReAct策略，强制LLM在`
</think>`与`
</tool_call>`标签间严格交替，确保推理与工具调用的逻辑连贯。该机制通过结构化约束降低了长程推理中的上下文溢出风险，使模型能够分解复杂任务为原子操作序列。

$$
\pi_\theta(a_t | s_t, I) = \text{LLM}(\text{CAD-CoT Prompt}(s_t, I))
$$

其中 $s_t$ 为包含历史工具调用与反馈的状态，$I$ 为L3级专家指令。该公式表明模型策略依赖于当前状态与指令的联合上下文，通过提示工程引导LLM生成符合CAD语法规范的下一步动作。

### 混合奖励机制与在线课程RL

设计动机在于解决离线RL（如AWR）在分布外任务上的泛化不足及稀疏奖励导致的优化不稳定问题。TOOLCAD引入混合奖励机制，结合步骤级规则奖励 $R_{step}$ 与轨迹级结果奖励 $R_{ORM}$。规则奖励基于引擎反馈的“成功/失败”标签提供密集信号，而ORM（基于Qwen2.5-7B微调）通过人类偏好数据训练，对完整轨迹进行二元判断。

$$
\mathcal{L}_{GRPO} = \mathbb{E}_{\tau \sim \pi_\theta} \left[ \frac{1}{K} \sum_{k=1}^K \left( \min\left( \frac{\pi_\theta(\tau_k | \tau_{<k})}{\pi_{old}(\tau_k | \tau_{<k})} \hat{A}_{i,k}, \text{clip}\left( \frac{\pi_\theta(\tau_k | \tau_{<k})}{\pi_{old}(\tau_k | \tau_{<k})}, 1-\epsilon, 1+\epsilon \right) \hat{A}_{i,k} \right) - \beta D_{KL}[\pi_\theta || \pi_{ref}] \right) \right]
$$

该目标函数通过GRPO策略优化，其中 $\hat{A}_{i,k}$ 为相对优势，由混合奖励计算得出。课程学习策略通过监控动作序列的平均困惑度（Perplexity），当困惑度低于阈值 $\delta$ 时逐步增加部件数量，确保模型在掌握当前复杂度后再探索更复杂任务，避免灾难性遗忘。

## 实验评估

| 方法 | 骨干网络 | 平均成功率 (%) | IR ↓ | MCD ↓ |
| :--- | :--- | :--- | :--- | :--- |
| GPT-4o (ReAct) | GPT-4o | 62.7 | 9.12 | 5.88 |
| Qwen3-235B (ReAct) | Qwen3-235B | 60.5 | 25.65 | 29.83 |
| Qwen2.5-7B (+SFT) | Qwen2.5-7B | 41.2 | 16.13 | 29.43 |
| Qwen2.5-7B (+TOOLCAD) | Qwen2.5-7B | 63.9 | 1.84 | 1.26 |
| Qwen3-8B (+TOOLCAD) | Qwen3-8B | 61.8 | 1.51 | 1.12 |

实验基于DeepCAD数据集的L3级专家指令，对比了闭源LLM（GPT-4o, Qwen3-235B）与开源LLM（Qwen2.5-7B, Qwen3-8B）在提示工程、SFT及TOOLCAD训练下的表现。基线覆盖了序列生成（Text2CAD, DeepCAD）与代码生成（CAD-Assistant, CAD-Llama）两类主流路线，但缺乏与B-Rep直接生成方法（如AutoBrep）的对比，这可能因任务定义不同（代码执行 vs. 几何重建）所致。TOOLCAD在Qwen2.5-7B上取得63.9%的平均成功率，超越GPT-4o的62.7%，且IR（指令遵循率）与MCD（建模命令距离）显著降低，表明工具调用范式在复杂任务中具备更强的鲁棒性。

消融实验显示，移除步骤级规则奖励导致性能大幅下降，证明仅依赖ORM的稀疏监督不足以优化长程工具调用轨迹。课程学习策略的移除导致模型在部件数超过3时性能急剧下降，验证了结构化难度引导对长程推理稳定性的必要性。在L0-L2级模糊指令下，TOOLCAD仍保持较高成功率（L1: 61.17%, L2: 70.29%），优于Text2CAD，表明其内部化的任务轨迹结构具备一定程度的指令噪声容忍能力。

评估指标包含成功率、IR、MCD及几何质量（IoU, JSD），但未报告计算效率（如推理时间、GPU显存占用）。代码已开源，但超参数细节（如GRPO的 $\beta$ 值、课程阈值 $\delta$）仅在附录中部分披露，复现需依赖作者提供的配置脚本。

## 关联研究分析

从问题动机看，TOOLCAD与Text2CAD（Khan et al., 2024）均致力于文本到CAD的映射，但Text2CAD采用序列预测范式，依赖Transformer解码器生成命令序列，而TOOLCAD采用工具调用范式，依赖LLM的推理能力规划原子操作。这一差异源于Text2CAD受限于序列长度与误差累积，而TOOLCAD通过引擎反馈实现迭代修正。然而，TOOLCAD对L3级精确指令的依赖可能削弱其在实际设计场景中（通常提供模糊意图）的适用性，Text2CAD的多级指令训练策略在此方面更具优势。

从方法设计看，TOOLCAD与CAD-Assistant（Mallis et al., 2024）均利用LLM进行工具调用，但CAD-Assistant依赖GPT-4o的提示工程与文档字符串，缺乏系统性的RL训练，而TOOLCAD引入在线课程RL与混合奖励机制。这一差异使得TOOLCAD在复杂多部件任务中表现更优，但CAD-Assistant的闭源模型优势可能掩盖了开源模型在推理能力上的差距。TOOLCAD在Qwen2.5-7B上超越GPT-4o的结果，暗示RL训练可能比模型规模更关键，但这一结论需在更大规模的开源模型上验证。

## 总结

TOOLCAD旨在解决LLM在复杂多部件CAD建模中的长程推理与错误累积问题，通过工具调用范式与在线课程RL实现迭代式建模。其核心贡献在于构建交互式CAD Gym与混合奖励机制，使开源LLM（Qwen2.5-7B）在DeepCAD L3任务上达到63.9%成功率，超越GPT-4o。然而，该框架高度依赖L3级精确指令，且在L0-L2级模糊指令下的几何多样性（JSD 3.21）仍高于Text2CAD（10.28），表明其在创意生成方面存在局限。当设计意图仅以自然语言模糊描述时，工具调用智能体能否在不依赖精确参数指令的情况下，通过视觉反馈或几何约束自主推断合理建模路径，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07960)