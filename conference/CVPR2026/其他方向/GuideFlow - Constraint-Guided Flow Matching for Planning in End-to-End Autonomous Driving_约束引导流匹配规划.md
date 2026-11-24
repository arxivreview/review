# CVPR2026最新论文 ｜GuideFlow: Constraint-Guided Flow Matching for Planning in End-to-End Autonomous Driving ｜约束引导流匹配规划

研究机构：北京交通大学、中国科学院

作者：Lin Liu、Caiyan Jia、Guanyi Yu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.18729)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.18729)

> 端到端自动驾驶规划需同时满足多模态意图表达与硬性安全约束，但模仿学习导致模式坍缩，而现有生成式方法缺乏约束嵌入机制。GuideFlow 通过流匹配架构，在生成过程中直接注入速度场修正、状态截断与能量基模型优化。该框架在 NavSim 测试集取得 43.0 EPDMS，验证了显式约束对规划鲁棒性的提升，但其推理延迟与长时程一致性仍存疑。

## 研究背景

**预备知识**
当规划器面对复杂交通场景时，单一轨迹预测无法覆盖多种可行驾驶意图，这一现象称为模式坍缩。为缓解此问题，生成式模型被引入以采样多样轨迹，但随机采样过程难以保证轨迹满足碰撞、车道等物理约束。流匹配（Flow Matching）通过学习从先验分布到目标分布的向量场，提供了比扩散模型更稳定的采样路径，但其直线传输特性易导致分布模式寻求，需额外机制保障约束满足。

**研究脉络**
端到端规划的主流路线分为模仿学习与生成式建模。模仿学习（如 UniAD、VAD）通过回归单一专家轨迹，虽训练稳定但无法表达歧义场景下的多意图；生成式方法（如 DiffusionDrive）虽能采样多样轨迹，但采样过程缺乏约束感知，常产生违规轨迹。现有工作多在推理后通过优化器修正轨迹，导致计算开销大且分布失真。GuideFlow 的切入点在于将约束嵌入流匹配的生成过程本身，而非事后修正，从而在保持多样性的同时确保物理可行性。

## 核心方法

### 方法参照系

GuideFlow 基于流匹配架构，将规划建模为从高斯先验 $\pi_0$ 到轨迹分布 $\pi_1$ 的传输过程。标准流匹配学习向量场 $v_\theta$，通过 ODE 积分生成轨迹。本文的关键差异在于：在采样过程中引入显式约束修正机制，而非仅依赖数据驱动学习。

### 约束引导的速度场与状态修正

**设计动机**：标准流匹配的直线传输路径易偏离约束流形，导致生成轨迹违反物理规则。本文在速度场预测与状态更新两个环节注入约束，确保轨迹始终处于可行域内。

**约束速度场（CVF）**：在每一步采样中，将模型预测的速度场 $v_\theta$ 与预定义的约束满足参考速度场 $v_t^{[c]}$ 进行加权融合：

$$ v_t^{corrected} = v_\theta + \lambda (v_t^{[c]} - v_\theta) $$

其中 $\lambda=0.1$ 控制修正强度。该公式通过最小幅度调整速度方向，使轨迹趋向约束满足的终点，同时保留原始速度场的运动合理性。

**约束流状态（CF）**：若离散化流路径 $\phi'_t$ 偏离约束流形，GuideFlow 在推理阶段直接替换接近终点的状态 $x_{[k]}$ 为约束满足锚点 $x_1^{[c]}$，并从该点继续采样。这一单次截断策略避免了逐步修正对采样平滑性的破坏，确保轨迹终止于可行区域。

### 能量基模型精化

**设计动机**：CVF 和 CF 仅保证轨迹终点满足约束，但无法优化轨迹内部的质量（如平滑性、效率）。本文引入能量基模型（EBM），在流匹配后期（$t>1$）激活能量项，引导样本向低能量且约束满足的区域收敛。

**能量函数定义**：

$$ E_\theta(x_t) = -\log p_\theta(x_t | C) + \mathcal{L}_{constraint}(x_t) $$

其中 $\mathcal{L}_{constraint}$ 评估约束满足度（如道路合规性、碰撞惩罚）。训练目标为最小化违反约束样本的能量，同时降低满足约束样本的能量，使速度场隐式学习约束感知。该机制赋予模型在数据流形内自主探索的能力，发现更优的约束满足轨迹。

## 实验评估

| 数据集 | 方法 | 指标 | 数值 |
| :--- | :--- | :--- | :--- |
| NavSim Navhard | GuideFlow + Scorer | EPDMS | 43.0 |
| NavSim Navhard | DiffusionDrive | EPDMS | 42.1 |
| Bench2Drive | GuideFlow | Driving Score | 75.21 |
| Bench2Drive | Hydra-Next | Driving Score | 73.86 |

实验在 NuScenes、ADV-NuScenes、NavSim 和 Bench2Drive 上进行。基线覆盖模仿学习（UniAD、VAD）与生成式方法（DiffusionDrive、Hydra-Next），但缺乏纯规则基线。GuideFlow 在 NavSim Navhard 上取得 43.0 EPDMS，较 DiffusionDrive 的 42.1 提升 0.9；在 Bench2Drive 上取得 75.21 Driving Score，优于 Hydra-Next 的 73.86。

| 模块 | NavSim EPDMS | Bench2Drive DS | NuScenes C.R(%) |
| :--- | :--- | :--- | :--- |
| Baseline | 23.1 | 73.86 | 0.08 |
| +CVF | 24.5 | 74.22 | 0.08 |
| +CF | 25.1 | 74.67 | 0.07 |
| +RFE | 25.5 | 74.90 | 0.07 |
| +CF+RFE | 27.1 | 75.21 | 0.07 |

消融实验显示，CF 模块贡献最大（+1.6 EPDMS），因其单次截断策略最小化对采样路径的干扰；RFE 模块在域外场景（Stage2 EPDMS）提升显著，体现其约束泛化能力。CVF 单独使用效果有限，因其逐步修正可能破坏流平滑性。

评估指标以 EPDMS 和 Driving Score 为主，缺乏对推理延迟的量化。代码已开源，但超参数 $\lambda$、$k_c$、$K$ 的敏感性分析显示，$\lambda$ 增大导致性能下降，表明约束强度需精细调节。

## 关联研究分析

从问题动机看，GuideFlow 与 DiffusionDrive 均解决生成式规划的约束缺失问题，但 DiffusionDrive 依赖推理后优化，而 GuideFlow 将约束嵌入生成过程。这一差异源于任务特性：规划需实时响应，事后优化增加延迟；GuideFlow 的显式约束设计更适合闭环场景，但可能牺牲分布多样性。

从方法设计看，GuideFlow 借鉴 Energy Matching 引入 EBM，但将其与流匹配统一，用于约束优化而非模式恢复。与 Diff-VLA 相比，后者通过语言条件引导意图，而 GuideFlow 使用 Plan Anchor 和 Reward 作为条件信号。Diff-VLA 的语义可控性更强，但 GuideFlow 的约束嵌入更直接，适合安全关键场景。

## 总结

GuideFlow 解决的核心矛盾是生成式规划中多样性与安全约束的冲突。其切入点在于将约束嵌入流匹配生成过程，通过 CVF、CF 和 RFE 三阶段机制，在保持轨迹多样性的同时确保物理可行性。实验证明，该框架在 NavSim 取得 43.0 EPDMS，在 Bench2Drive 取得 75.21 Driving Score，验证了显式约束的有效性。然而，论文未报告推理延迟，且 CF 模块的单次截断策略可能限制长时程误差修正。当采样步数增加时，约束修正的累积误差是否导致轨迹漂移，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.18729)