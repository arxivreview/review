# HuggingFace最新推荐论文 ｜OS-Helix: Unifying GUI Interaction and Code Execution in Native Computer-Using Agents ｜OS-Helix：原生GUI与代码混合执行的计算机使用智能体

研究机构：中国科学技术大学、新加坡国立大学

作者：Bowen Yang、Kaiming Jin、Zichen Ding 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.22234)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.22234)

> 导读 真实桌面自动化既非纯视觉也非纯程序化，智能体需同时理解用户界面并高效操作文件与系统状态。现有方法若仅在推理时向GUI模型附加代码工具，会破坏已习得的视觉策略，无法实现可靠的路由。OS-Helix提出端到端训练策略，将GUI动作与代码执行统一于单一动作空间，通过应用-工件组合构建可执行桌面状态，并引入Step-balanced GSPO解决混合动作优化不平衡问题。该工作验证了原生混合协调的有效性，但其在Windows平台的迁移仍受限于系统命令层的适配。

## 研究背景

当计算机使用智能体（Computer-Using Agent, CUA）面对真实桌面任务时，纯视觉感知在定位微小或模糊界面元素时易失效，而细粒度交互使结构化状态操作变得繁琐。程序化控制虽能直接操作文件与系统状态，却无法处理依赖视觉布局或仅通过界面暴露的软件行为。这一互补性催生了混合执行范式，但现有框架依赖外部编排或预定义接口，未能让单一策略原生学习GUI与代码的路由。

早期GUI智能体如UI-TARS通过端到端模型统一感知与动作，但受限于纯视觉动作空间，在长程任务中面临错误累积与效率瓶颈。代码智能体如OpenClaw擅长结构化操作，却缺乏对动态界面的感知能力。初步实验表明，向Qwen3-VL-32B-Instruct朴素地暴露代码执行能力，反而使其在OSWorld-Verified上的成功率从约34%降至约32%，证明提示级组合无法产生协调行为。OS-Helix的切入点在于：通过高质量混合数据训练，将GUI/代码路由能力内化至模型策略中，而非依赖推理时的工具拼接。

## 核心方法

### 统一混合动作空间与数据基础设施

OS-Helix将GUI交互与代码执行视为改变同一数字状态的互补方式，构建统一动作空间 $\mathcal{A}_{\text{hybrid}} = \mathcal{A}_{\text{GUI}} \cup \mathcal{A}_{\text{meta}} \cup \mathcal{A}_{\text{code}}$。策略 $\pi_\theta$ 根据用户指令 $q$、历史上下文 $h_i$ 和屏幕观测 $o_i$ 选择动作 $a_i$。代码动作在独立进程中执行，其输出作为工具响应追加至上下文。

为构建混合监督信号，OS-Helix引入应用-工件组合（Application-Artifact Composition），将版本化应用与真实文件工件配对，实例化可复现的桌面状态。通过应用-工件兼容性图组织有效配对，确保任务状态的可执行性。任务合成采用解耦流水线：探索代理基于环境状态生成指令，独立评估代理构建基于规则的验证器，确保任务终态可验证且不限制解决路径。

### Step-balanced GSPO优化策略

在强化学习（Reinforcement Learning, RL）阶段，标准GSPO因代码动作的token数量远超GUI动作，导致优化信号被代码步主导，引发策略向代码密集型行为漂移。Step-balanced GSPO修改样本级重要性比率的聚合方式，按动作步而非原始token计数构建权重。

对于训练样本 $i$，定义token级对数重要性权重 $\delta_{i,t} = \log \frac{\pi_\theta(y_{i,t} | h_{i,t})}{\pi_{\text{old}}(y_{i,t} | h_{i,t})}$。标准GSPO对所有有效token求平均，而Step-balanced GSPO先计算每个动作步 $k$ 的平均token级对数权重，再对动作步求平均：

$$
\log \hat{r}_i(\theta) = \frac{1}{K_i} \sum_{k=1}^{K_i} \left( \frac{1}{|a_{i,k}|} \sum_{t \in a_{i,k}} \delta_{i,t} \right)
$$

该公式确保每个动作步对样本级比率的贡献相等，无论其token长度如何，从而平衡GUI与代码动作的优化信号，防止长代码动作主导梯度更新。

## 实验评估

实验在OSWorld-Verified（361个任务）和WindowsAgentArena上进行，基线覆盖Agentic框架、通用模型及骨干网络。OS-Helix-27B-RL在OSWorld-Verified上达到66.44%成功率，较SFT阶段提升3.69个百分点，较混合基线提升19.89个百分点。在WindowsAgentArena上，OS-Helix-27B-RL达到63.87%，较Qwen3.5-27B GUI基线提升23.05个百分点，验证了跨平台迁移能力。

| 方法 | OSWorld-Verified (%) | WindowsAgentArena (%) |
| :--- | :--- | :--- |
| Qwen3.5-27B (GUI) | 46.50 | 40.82 |
| Qwen3.5-27B (Hybrid) | 46.50 | 56.41 |
| OS-Helix-27B (SFT) | 62.75 | 57.95 |
| OS-Helix-27B-RL | 66.44 | 63.87 |

消融实验揭示关键设计决策：移除训练中的思维链（CoT）导致成功率下降12.82个百分点，证明CoT不仅是训练目标，更是执行时的状态表示。混合SFT数据较纯GUI SFT在10K样本预算下提升3.05个百分点，证实混合轨迹训练对代码动作利用的必要性。标准GSPO使代码动作比例从27.9%升至40.0%，而Step-balanced GSPO维持26.1%的平衡比例，验证了优化平衡机制的有效性。

评估边界方面，论文未报告置信区间，且WindowsAgentArena实验仅使用SFT，未包含RL阶段，限制了跨平台RL增益的评估。此外，约10%的不可行任务导致模型过度执行，移除后成功率提升3-5个百分点，表明模型缺乏校准的拒绝能力。

## 关联研究分析

从问题动机看，OS-Helix与UI-TARS均追求端到端统一建模，但UI-TARS局限于纯视觉动作空间，在结构化文件操作任务上效率低下。OS-Helix通过引入代码动作，将任务分解为GUI感知与程序化执行，解决了纯视觉方法在精确状态操作上的瓶颈。然而，OS-Helix未与纯代码智能体（如OpenClaw）在相同任务集上对比，无法量化混合策略相对于纯代码策略在视觉依赖任务上的具体优势。

从方法设计看，OS-Helix与Agent S3均处理混合执行，但Agent S3依赖外部框架协调GUI与代码，性能耦合于昂贵推理与手工编排。OS-Helix通过原生策略学习路由，消除了外部依赖。Step-balanced GSPO与EvoCUA-1.5的Step-Level Policy Optimization均针对多步优化，但后者未处理混合动作粒度差异。Step-balanced GSPO是否适用于其他异构动作空间（如语音与文本混合），论文未给出回答。

## 总结

OS-Helix解决了GUI智能体在真实桌面任务中视觉定位脆弱与程序化操作覆盖不足的核心矛盾，通过原生混合策略训练实现了GUI与代码的协调路由。其核心贡献在于应用-工件数据合成管线与Step-balanced GSPO优化算法，在OSWorld-Verified上达到66.44%成功率，显著超越纯视觉基线。然而，模型在Windows平台仍受限于系统命令层适配，且缺乏对不可行任务的校准拒绝能力。当混合动作空间进一步扩展至语音或触觉模态时，Step-balanced GSPO的按步聚合机制是否仍能维持优化平衡，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.22234)