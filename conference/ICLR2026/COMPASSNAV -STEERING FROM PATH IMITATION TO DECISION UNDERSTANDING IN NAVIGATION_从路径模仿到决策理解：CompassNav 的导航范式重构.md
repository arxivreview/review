# ICLR2026最新论文 ｜COMPASSNAV:STEERING FROM PATH IMITATION TO DECISION UNDERSTANDING IN NAVIGATION ｜从路径模仿到决策理解：CompassNav 的导航范式重构

研究机构：华东师范大学、西北工业大学

作者：LinFeng Li、Jian Zhao、Yuan Xie 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_84938314)

> 具身物体目标导航（Object-Goal Navigation, ObjectNav）旨在让智能体在未知环境中定位特定目标，其核心价值在于弥合空间感知与语义理解之间的鸿沟。现有端到端方法依赖单一路径真值进行监督，将复杂的导航任务简化为序列复制，导致智能体在动态多路径环境中泛化能力受限。CompassNav 通过构建全动作空间标注数据集与自适应奖励函数，将训练目标从模仿专家轨迹转向评估所有可行动作的相对价值。该范式在开放词汇导航上超越了更大规模的闭源模型，但在标准物体导航基准上仍落后于最新统一模型，其无显式地图设计的长时程鲁棒性存疑。

## 研究背景

当智能体面对“寻找一把椅子”这类稀疏指令时，它必须在缺乏逐步引导的情况下自主探索。传统模块化系统依赖 SLAM 构建显式几何地图，虽具备几何精度，但传感器噪声与位姿漂移会导致地图完整性受损，且工程化地图难以解读“找个安静阅读处”等非结构化人类意图。为规避显式映射的脆弱性，基于大型视觉语言模型（Large Vision-Language Models, LVLMs）的端到端（End-to-End, E2E）方法成为主流，其原生语义处理能力直接映射观测到动作。然而，当前 E2E 训练范式普遍采用路径模仿（Path Imitation），即最小化与单一专家轨迹的偏差。这种监督粒度失配（Supervision Granularity Mismatch）使得模型将导航视为记忆任务，忽略了真实环境中有效路径的非唯一性，未能习得导航的因果结构。

该领域要解决的核心矛盾是高层语义推理与低层实时控制的解耦，以及 VLM 在缺乏精确几何约束时的空间幻觉。主流路线中，模块化方法（如 VLFM）通过显式语义地图保证长时程一致性，但牺牲了部署灵活性；E2E 方法（如 Nav-R1）虽简化了架构，但受限于单路径监督，在模糊决策点缺乏对比反馈。CompassNav 的切入点在于指出路径模仿的本质缺陷：它惩罚了替代路径，导致智能体无法在决策点（Decision Point）评估所有选项的相对价值。通过引入决策理解（Decision Understanding）范式，CompassNav 试图让智能体内部化空间结构，执行“先思考后行动”（Think-then-Act）启发式，从而在动态环境中实现鲁棒导航。

## 核心方法

### 方法参照系

CompassNav 属于导航基础模型路线中的 E2E 分支，基于 Qwen2.5-VL-7B 骨干。与标准 SFT 或 RL 流程不同，其关键差异在于数据监督从单路径真值扩展为全动作空间的 A* 测地线距离标注，并采用 SFT-then-RFT 两阶段配方，其中 RFT 阶段使用定制的 Gap-Aware 奖励函数而非标准稀疏或密集奖励。

### 全动作空间密集标注

传统 VLN 数据集（如 R2R）仅提供单一路径真值，导致模型无法评估替代动作的质量。CompassNav 构建 Compass-Data-22k 数据集，利用 Action Proposal Module (APM) 基于实时深度图与占用网格识别所有可行候选动作，并离散化为极向量 $(r, \theta)$。Oracle A* Annotator 利用全局模拟器信息计算每个候选动作相对于目标的测地线距离，生成完整的动作价值向量。这一设计解决了单路径监督导致的对比反馈缺失问题，使模型能够学习动作空间中的正确性梯度。

### Gap-Aware 混合奖励函数

在 RFT 阶段，CompassNav 采用 Group-wise Reward Policy Optimization (GRPO) 框架，其核心创新在于 Gap-Aware 混合奖励函数。该函数由连续基础分数与确定性调制动态奖励组成。基础分数 $s_t[i_j]$ 通过距离向量 $d_t$ 的 Softmax 计算：

$$ s_t[i_j] = \frac{\exp(-d_t[i_j]/\tau)}{\sum_{k} \exp(-d_t[k]/\tau)} $$

其中 $\tau$ 为温度超参数，控制分布尖锐度。动态奖励由确定性因子 $g_t$ 调制，$g_t$ 衡量最优与次优动作的归一化差距：

$$ g_t = \frac{d_t^{(2)} - d_t^{(1)}}{d_t^{(max)} - d_t^{(1)}} $$

最终奖励 $r_t[i_j]$ 结合基础分数与仅对最优动作 $i^*$ 触发的奖励：

$$ r_t[i_j] = s_t[i_j] + \beta_{max} \cdot g_t \cdot \mathbb{1}[i_j = i^*] $$

该设计解决了标准二元奖励在模糊场景下缺乏细粒度反馈、线性 Min-Max 奖励在确定性场景下区分度不足的问题。通过动态调整，函数在清晰场景中提供决定性信号，在模糊场景中允许更高熵以鼓励探索。

## 实验评估

CompassNav 在 HM3D-v1-val、HM3D-v2-val 和 MP3D-val 三个未见场景验证集上评估，任务涵盖 Object-Goal 与 Instance-Image-Goal Navigation。基线覆盖模块化方法（VLFM, UniGoal, SG-Nav）与 E2E 模型（GPT-4o, Nav-R1, Qwen2-VL-7B）。

| 方法 | 类型 | HM3D SR (%) | HM3D SPL (%) | MP3D SR (%) | MP3D SPL (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| VLFM | Modular | 53.1 | 26.0 | - | - |
| UniGoal | Modular | 54.5 | 25.1 | 41.0 | 16.4 |
| GPT-4o | E2E | 52.4 | 23.5 | - | - |
| Nav-R1 | E2E | - | - | - | - |
| CompassNav | E2E | 56.6 | 27.6 | 42.0 | 17.5 |

CompassNav 在 HM3D 上以 56.6% SR 超越所有模块化基线及 GPT-4o，在 MP3D 上以 42.0% SR 领先 UniGoal。在开放词汇导航（HM3D-OVON）上，CompassNav 取得 61.6% SR，超越 Nav-R1 的 58.4%（据领域综述），且训练数据量仅为后者的十分之一。

| 配置 | SR (%) | SPL (%) |
| :--- | :--- | :--- |
| Base Model | 19.8 | 5.20 |
| SFT (Full) | 23.3 | 7.90 |
| RFT (from SFT) | 35.6 | 14.8 |
| Reward: Binary | 29.5 | 11.1 |
| Reward: Ours | 35.6 | 14.8 |

消融实验显示，SFT 阶段将 SR 从 19.8% 提升至 23.3%，RFT 阶段进一步跃升至 35.6%，验证了“冷启动”初始化的必要性。Gap-Aware 奖励相比二元奖励提升 6.1 个 SR 点，表明细粒度反馈对决策理解的关键作用。温度 $T=0.5$ 与奖励系数 $B=1.0$ 组合表现最优，过低的 $T$ 导致探索不足，过高的 $B$ 则引发奖励稀疏。

评估边界方面，论文未报告计算延迟与显存占用，无法直接对比实时性。代码未公开，仅提供项目页面，可复现性受限。指标仅包含 SR 与 SPL，缺乏对决策过程本身的量化评估（如决策点准确率），NavNuances 基准仅作为辅助验证。

## 关联研究分析

从问题动机看，CompassNav 与 Nav-R1 均基于 LVLM 微调，但 Nav-R1 依赖单路径模仿，而 CompassNav 通过全动作标注实现决策理解。这一差异源于对“导航本质”的不同假设：Nav-R1 视导航为轨迹回归，CompassNav 视其为价值评估。CompassNav 在 HM3D-OVON 上超越 Nav-R1，暗示在开放词汇场景中，评估替代路径的价值比模仿单一专家路径更具泛化性。然而，CompassNav 在 HM3D-v2 标准物体导航上（56.6% SR）显著低于 Uni-LaViRA（77.7% SR，据领域综述），这可能归因于后者采用的统一 VLA 架构与显式空间记忆模块，而 CompassNav 完全摒弃显式地图，依赖隐式参数化记忆。

从方法设计看，CompassNav 的 Gap-Aware 奖励与 VLFM 的显式语义地图形成对比。VLFM 通过构建视觉-语言前沿地图提供全局状态，CompassNav 则通过 A* 距离向量提供局部动作价值。前者在长时程一致性上更优（SPL 更高），后者在计算效率与部署灵活性上占优。CompassNav 未采用 3DGS 或 RAG 等显式记忆机制，其长时程鲁棒性依赖于 LVLM 的上下文窗口与隐式记忆能力。在无显式地图条件下，智能体在复杂布局中是否必然导致长时程上下文丢失，论文未给出直接回答，仅通过 MP3D 跨场景泛化间接验证。

## 总结

CompassNav 旨在解决 E2E 导航中路径模仿导致的泛化局限，通过全动作空间 A* 标注与 Gap-Aware 奖励函数，将训练目标从轨迹复制转向决策价值评估。该框架在 HM3D-OVON 上以 61.6% SR 超越 Nav-R1，在 HM3D 标准导航上以 56.6% SR 超越 GPT-4o 与模块化基线，证明了决策理解范式的有效性。然而，其在 HM3D-v2 上落后于 Uni-LaViRA 14.7 个 SR 点，暴露了无显式地图设计在复杂室内布局中的性能瓶颈。当环境复杂度增加、路径长度延长时，仅依赖隐式参数化记忆的 E2E 模型能否维持长时程导航的一致性，而非依赖显式空间表征，这一边界条件在现有实验中尚未被充分验证。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_84938314)