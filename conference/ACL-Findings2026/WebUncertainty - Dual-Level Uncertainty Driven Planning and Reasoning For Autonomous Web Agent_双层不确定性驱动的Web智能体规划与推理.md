# ACL-Findings2026最新论文 ｜WebUncertainty: Dual-Level Uncertainty Driven Planning and Reasoning For Autonomous Web Agent ｜双层不确定性驱动的Web智能体规划与推理

研究机构：合肥工业大学

作者：Lingfeng Zhang、Yongan Sun、Jinpeng Hu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17821)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17821)

> 长程Web任务中，静态规划难以适应动态界面，而线性推理易因幻觉导致错误级联。现有方法要么僵化执行预定义步骤，要么盲目信任LLM生成的动作，缺乏对“环境未知”与“模型无知”的区分。WebUncertainty通过任务不确定性驱动规划模式切换，并结合动作不确定性量化MCTS搜索，实现了在复杂交互中的鲁棒决策。该方法在WebArena上取得46.9%成功率，显著优于基线，但其纯文本设定与高计算开销限制了实际部署的泛化性。

## 研究背景

Web智能体在长程任务中面临双重困境：规划阶段无法预知网页动态变化，推理阶段LLM可能生成不存在的元素操作。这种不确定性若未被显式建模，会导致智能体在局部最优中迷失或陷入幻觉循环。解决此问题需区分两类不确定性：源于环境动态性的任务不确定性，以及源于模型知识缺失的动作不确定性。

当前主流Web智能体架构基于ReAct范式，交替执行推理与行动。然而，静态显式规划在网页布局突变时失效，而隐式规划易受局部噪声干扰。同时，基于蒙特卡洛树搜索（MCTS）的推理方法虽能探索多路径，但传统评估机制无法区分“模型不知道”（认知不确定性）与“环境本身模糊”（随机不确定性），导致搜索预算浪费在无效分支上。WebUncertainty的切入点在于将不确定性量化嵌入规划与推理的核心循环，通过动态切换策略与置信度引导搜索，解决长程任务中的错误累积问题。

## 核心方法

### 方法参照系

WebUncertainty建立在POMDP框架下，将Web导航建模为部分可观测马尔可夫决策过程。与标准ReAct线性执行不同，该框架将决策解耦为规划与推理两个层级，分别处理任务级与动作级不确定性。

### 任务不确定性驱动的自适应规划

规划阶段的核心失效在于静态策略无法适应环境动态性。WebUncertainty引入分析智能体评估任务不确定性 $u_{plan} \in [0, 1]$，该值反映当前网页状态与剩余目标 $T_{rem}$ 的匹配复杂度。

$$
g_t = \begin{cases} \text{First}(\pi_{plan}^{exp}(T_{rem}, O_t)) & \text{if } u_{plan} \le \delta \\ \pi_{plan}^{imp}(T_{rem}, O_t) & \text{if } u_{plan} > \delta \end{cases}
$$

当不确定性低于阈值 $\delta$ 时，采用显式规划生成完整子目标序列，确保长程连贯性；当不确定性高于阈值时，切换至隐式规划直接预测即时子目标，以灵活应对未知环境。这一机制解决了静态规划在动态网页中因预定义步骤失效而导致的执行中断。

### 动作不确定性驱动的MCTS推理

推理阶段的核心失效在于LLM幻觉导致操作不存在元素。WebUncertainty在MCTS扩展阶段生成 $K$ 个候选动作及置信度 $c_i$，通过ConActU策略量化认知不确定性（EU）与随机不确定性（AU）。

$$
EU = 1 - E, \quad AU = H_{norm} \cdot E
$$

其中 $E$ 为平均置信度，$H_{norm}$ 为归一化预测熵。EU高表明模型缺乏知识（幻觉风险），AU高表明存在多个有效选项（环境模糊）。在模拟阶段，根据EU/AU组合对奖励 $R$ 进行调制：高EU高AU施加严格惩罚 $R=-5$，高EU低AU施加标准惩罚 $R=-1$，低EU高AU保留基础分数，低EU低AU触发重新生成。该机制通过区分错误来源，避免搜索树在幻觉分支上过度扩展，提升了决策的可靠性。

## 实验评估

实验在WebArena（812任务）与WebVoyager（129任务子集）上进行，对比Browser Use、Agent-E、WebPilot及AgentOccam。基线覆盖线性执行、层级规划及MCTS搜索路线，但缺失多模态方法如Avenir-Web及记忆增强方法如WebCoach。

| Agent | Backbone | WebArena SR (%) | WebVoyager SR (%) |
| :--- | :--- | :--- | :--- |
| WebPilot | GPT-4-Turbo | 37.6 | 62.0 |
| AgentOccam | GPT-4-Turbo | 43.1 | 64.3 |
| WebUncertainty | GPT-4-Turbo | 46.9 | 65.9 |
| WebPilot | Qwen-Max | 34.5 | 55.8 |
| AgentOccam | Qwen-Max | 38.4 | 58.9 |
| WebUncertainty | Qwen-Max | 40.1 | 63.6 |

WebUncertainty在两个基准上均取得最高成功率，尤其在Reddit域（67.0%）显著优于WebPilot（37.7%），验证了AU量化在模糊环境中的优势。Qwen-Max骨干下，WebUncertainty（63.6%）超越GPT-4-Turbo版本的WebPilot（62.0%），表明不确定性管理可弥补模型推理能力的不足。

消融实验显示，移除ConActU策略导致WebVoyager成功率下降9.3%，WebArena下降3.4%，证实动作不确定性量化对抑制幻觉的关键作用。固定为显式或隐式规划模式均导致性能下降，证明动态切换机制的必要性。

评估边界方面，本文仅使用文本模态（Accessibility Tree），未涵盖视觉接地误差；MCTS每子目标扩展上限设为10，计算开销未报告；WebVoyager子集排除了不稳定页面，可能高估实际环境鲁棒性。代码已开源，超参数 $\delta=0.4, \tau=6$ 在敏感性分析中表现稳定。

## 关联研究分析

从问题动机看，WebUncertainty与Branch-and-Browse均针对长程任务错误恢复，但前者通过MCTS树内化回溯，后者依赖显式树结构搜索。WebUncertainty的优势在于将不确定性量化融入节点评估，避免了Branch-and-Browse中重复无效操作的冗余计算，但牺牲了实时性。从方法设计看，WebUncertainty与WebPilot同属MCTS架构，但WebPilot依赖固定评估函数，而WebUncertainty通过ConActU动态调制奖励。这一差异源于WebPilot未区分幻觉与环境噪声，导致搜索预算浪费；WebUncertainty的改进是否在所有动态环境中均有效，论文未提供跨域对比数据。

## 总结

WebUncertainty解决的核心矛盾是长程Web任务中规划僵化与推理幻觉的耦合失效。其切入点在于显式区分任务不确定性（环境动态性）与动作不确定性（模型知识缺失），通过动态规划切换与置信度引导MCTS搜索，实现了错误来源的解耦。实验证明该方法在WebArena上取得46.9%成功率，Qwen-Max骨干下超越GPT-4-Turbo版本的WebPilot。然而，纯文本设定忽略了视觉接地误差，MCTS计算开销未量化，且WebVoyager子集排除了不稳定页面。当网页布局发生视觉级突变时，仅依赖文本Accessibility Tree的不确定性量化是否仍能准确区分幻觉与环境噪声，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17821)