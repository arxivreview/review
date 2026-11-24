# ICLR2026最新论文 ｜Lifelong Embodied Navigation Learning ｜终身具身导航学习

研究机构：中国科学院、中国科学院大学

作者：Xudong Wang、Jiahua Dong、Baichen Liu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.06073)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.06073)

> 具身导航智能体在顺序学习新任务时面临灾难性遗忘，导致无法持续积累多场景、多指令风格下的导航能力。现有联合训练方法假设任务分布固定，缺乏对未知新场景的适应机制，而固定专家数的低秩适应方法无法动态扩展以容纳无限任务。本文提出终身具身导航学习（Lifelong Embodied Navigation Learning, LENL）问题，并设计 Uni-Walker 框架，通过解耦共享与特定知识实现参数高效的持续学习。该方法在自建基准上显著优于现有低秩适应基线，但其评估局限于静态室内场景，未验证动态环境下的鲁棒性。

## 研究背景

当导航智能体在 Matterport3D 等仿真器中执行视觉语言导航（Vision-and-Language Navigation, VLN）任务时，其依赖的大语言模型（Large Language Model, LLM）骨干在微调新场景或新指令风格时，会覆盖旧任务的参数权重，导致旧任务性能骤降——这一现象称为灾难性遗忘。为缓解此问题，低秩适应（Low-Rank Adaptation, LoRA）通过冻结预训练权重并仅更新低秩矩阵来降低参数冲突，但标准 LoRA 仅存储单任务权重，无法利用任务间共享的导航常识。

多任务联合训练是构建通用导航智能体的主流路线，NaviLLM 和 OctoNav 等方法通过大规模联合微调实现跨任务泛化，但其核心假设是任务集合在训练前已知且固定。当智能体需要在线适应新场景或新指令风格时，这种静态架构无法扩展，且重新训练成本高昂。HydraLoRA 和 BranchLoRA 引入多专家结构以捕获任务共享知识，但专家数量在初始化时固定，限制了其在终身学习场景中的可扩展性。Uni-Walker 的切入点在于将导航知识显式解耦为任务共享与任务特定组件，并通过动态扩展专家子空间实现无限任务的持续学习，从而突破固定专家数的限制。

## 核心方法

### 方法参照系

本文问题属于参数高效持续学习范畴，标准流程为：冻结预训练 LLM，为每个新任务训练独立的 LoRA 适配器，推理时加载对应权重。本文与标准流程的关键差异在于：不存储独立任务权重，而是通过共享子空间与动态扩展的特定子空间组合，实现知识的继承与隔离。

### DE-LoRA 架构与知识解耦

DE-LoRA 将 LoRA 的低秩权重分解为共享编码器子空间 $\mathbf{A}$ 和特定解码器子空间 $\mathbf{B}_t$，其中 $\mathbf{A}$ 在所有任务间共享，$\mathbf{B}_t$ 为第 $t$ 个任务动态新增的专家。该设计解决了标准 LoRA 无法利用任务间共享导航常识的问题，使新任务能继承旧任务的底层空间推理能力。

$$
\Delta \mathbf{W}_t = \sum_{n=1}^{K} \mathbf{B}_n \mathbf{A}
$$

该公式表明，第 $t$ 个任务的权重更新由 $K$ 个激活的特定专家 $\mathbf{B}_n$ 与共享子空间 $\mathbf{A}$ 的乘积之和构成，实现了共享知识与特定知识的线性组合。

### 知识继承与正交约束

为最大化共享知识利用，知识继承策略（Knowledge Inheritance Strategy, KIS）通过主成分分析（Principal Component Analysis, PCA）提取同指令风格历史专家的共享变化方向，用于初始化新专家 $\mathbf{B}_t$。专家协同激活策略（Experts Co-Activation Strategy, ECAS）在推理时激活 $K$ 个相关专家，其中 $K-1$ 个冻结专家提供共享上下文，$\mathbf{B}_t$ 可训练以捕获特定知识。为隔离特定知识，专家子空间正交约束（Expert Subspace Orthogonality Constraint, ESOC）强制 $\mathbf{B}_t$ 与历史专家正交，防止特定知识污染共享子空间。

$$
\mathcal{L}_{esoc} = \lambda_{esoc} \left\| \mathbf{B}_t \mathbf{B}_t^\top - \mathbf{I} \right\|_F^2
$$

该损失函数通过最小化 $\mathbf{B}_t$ 的自相关矩阵与单位矩阵的偏差，确保新专家子空间与历史专家子空间在几何上正交，从而保证特定知识的独立性。

## 实验评估

实验在自建 LENL 基准上进行，包含 18 个 Matterport3D 场景和 3 种指令风格（VLN、OLN、DUN），前 15 个任务用于持续学习，后 3 个任务用于未见场景泛化测试。基线覆盖 Seq-FT、LwF-LoRA、EWC-LoRA、Dense/Sparse MoLE、MoLA、HydraLoRA、BranchLoRA 等持续学习经典方法，但缺失 ABot-N0 等最新导航基础模型，可能低估了统一架构在持续学习场景中的潜力。

| 方法 | Avg SR (%) | Avg SR-F (%) | Avg SPL (%) |
| :--- | :--- | :--- | :--- |
| HydraLoRA | 54 | 21 | 37.0 |
| BranchLoRA | 58 | 17 | 41.0 |
| Uni-Walker | 66 | 5 | 62.3 |

Uni-Walker 的平均成功率（SR）为 66%，较 HydraLoRA 的 54% 提升 12 个百分点，遗忘率（SR-F）从 21% 降至 5%，表明 DE-LoRA 解耦机制有效缓解了灾难性遗忘。

消融实验显示，移除 KIS 导致 SR 从 67.3% 降至 60.3%，移除 ESOC 导致 SR 从 67.3% 降至 63.5%，表明知识继承与正交约束对性能贡献显著。移除 NSCoT 导致 SR 降至 51.1%，说明导航特定思维链对指令风格理解至关重要。任务感知知识聚合（Task-Aware Knowledge Aggregation, TAKA）中，仅使用内部记忆（IM）时 SR 降至 35.0%，表明外部记忆（OM）与多模态记忆（MM）的融合对知识聚合不可或缺。

评估边界方面，本文仅在静态室内场景验证，未测试动态障碍物或城市尺度环境；未报告计算延迟与推理效率，无法评估实时部署可行性；代码已开源，但超参数配置（如 $\lambda_{ssc}=0.1$、$\omega=0.9$）的敏感性分析缺失，可复现性依赖默认设置。

## 关联研究分析

从问题动机看，Uni-Walker 与 ABot-N0 等导航基础模型的核心差异在于任务假设：ABot-N0 假设任务集合固定，通过大规模联合训练实现跨任务泛化，而 Uni-Walker 假设任务序列无限，通过参数解耦实现持续适应。这一差异源于任务特性：ABot-N0 面向静态基准评测，而 Uni-Walker 面向动态部署场景。Uni-Walker 未探索联合训练与持续学习的混合范式，可能在任务数量较少时效率低于 ABot-N0。

从方法设计看，Uni-Walker 与 HydraLoRA 的关键差异在于专家扩展机制：HydraLoRA 使用固定数量专家，而 Uni-Walker 动态新增专家并引入正交约束。这一设计解决了固定专家数在终身学习中的可扩展性瓶颈，但正交约束可能限制专家间的知识共享，导致特定知识过度隔离。Uni-Walker 未分析正交约束强度对知识共享的影响，可能在任务高度相关时性能下降。

## 总结

Uni-Walker 解决的核心矛盾是导航智能体在顺序学习新任务时的灾难性遗忘与知识积累需求。其切入点在于将导航知识显式解耦为共享与特定组件，通过 DE-LoRA 架构实现参数高效的持续学习，突破了固定专家数方法的限制。实验证明，Uni-Walker 在自建基准上达到 66% 的平均成功率，遗忘率降至 5%，显著优于 HydraLoRA 等基线。其边界在于评估局限于静态室内场景，未验证动态环境下的鲁棒性，且未报告计算效率指标。当任务序列扩展到 100 个以上时，动态扩展专家的正交约束是否会导致共享子空间退化，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.06073)