# ICLR2026最新论文 ｜TOWARDS BETTER BRANCHING POLICIES: LEVER - - AGING THE SEQUENTIAL NATURE OF BRANCH AND BOUND TREE ｜基于Mamba序列建模的分支定界策略

研究机构：中国科学院、中国科学院大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_76000939)

> 混合整数线性规划（MILP）求解的核心瓶颈在于分支定界（B&B）搜索树的指数级膨胀，传统启发式策略缺乏对实例结构的自适应能力。现有神经分支方法多采用静态图编码或无序历史聚合，忽略了B&B树扩展过程中固有的时间序列依赖性，导致长程决策性能受限。本文提出Mamba-Branching，通过对比学习预训练判别性嵌入，并利用Mamba状态空间模型对分支路径进行自回归序列建模，以线性复杂度捕捉跨步骤依赖。该方法在异构MILP基准上超越了所有神经分支基线，但其优势高度依赖于长序列历史，在短历史或计算受限场景下的鲁棒性尚存疑。

## 研究背景

B&B算法通过递归划分可行域并计算上下界来保证MILP求解的最优性，其效率取决于分支变量选择的质量。强分支（Strong Branching, SB）虽能最大化对偶界改进，但需求解子问题LP松弛，计算开销巨大；而pscost分支利用历史统计信息，虽高效但在搜索初期因数据不足表现不佳。relpscost分支作为SCIP求解器的默认规则，结合了两者优势，但在面对异构实例分布时，其基于局部统计的决策逻辑缺乏对全局搜索轨迹的感知能力，导致泛化性能受限。

神经分支策略旨在通过数据驱动方法替代手工启发式。早期工作如FILM（Gasse et al., 2019）采用图卷积网络（GCNN）编码实例特征，但依赖实例特定结构，难以跨域迁移。后续研究转向参数化B&B树，如TreeGate（Zarpellon et al., 2021）和T-BranT（Lin et al., 2022），通过构建实例无关的特征空间实现跨实例泛化。然而，TreeGate仅利用当前节点状态，T-BranT虽引入历史数据但将其建模为无序图结构，未能显式捕捉分支决策的时间顺序性。这种“短视”或“无序”的历史处理机制，使得模型无法有效利用从根节点到当前节点的路径信息来规避死胡同或冗余探索，成为制约神经分支策略在复杂实例上性能提升的关键瓶颈。

## 核心方法

### 参数化B&B树与序列输入构建

本文沿用TreeGate的参数化B&B树框架，将每个分支步骤 $t$ 的状态表示为 $s_t = (C_t, Tree_t)$，其中 $C_t \in \mathbb{R}^{|C_t| \times 25}$ 为候选变量特征，$Tree_t \in \mathbb{R}^{61}$ 为树结构特征。与T-BranT将历史节点视为无序图不同，本文将分支路径定义为有序序列 $\mathbf{S} = (e_{0,1}, \dots, e_{0,|C_0|}, e_{0,a_0}, \dots, e_{T,1}, \dots, e_{T,|C_T|}, e_{T,a_T})$，其中 $e_{t,i}$ 为第 $t$ 步第 $i$ 个候选变量的嵌入，$a_t$ 为专家选择的分支变量索引。该设计将B&B树的扩展过程显式序列化，使得序列模型能够同时捕捉步间依赖（inter-step dependencies）和步内候选变量间的交互（intra-step interactions），解决了无序图编码无法区分时间先后顺序导致的决策偏差问题。

### 对比学习预训练嵌入层

传统模仿学习中，嵌入层直接通过交叉熵损失端到端训练，导致候选变量嵌入区分度低，难以在相似特征中识别关键差异。本文引入对比学习（Contrastive Learning, CL）预训练嵌入层，设计损失函数 $\mathcal{L}_c$ 以最大化选中变量嵌入与锚点嵌入的相似度，同时最小化其他候选变量嵌入与锚点的相似度：

$$
\mathcal{L}_c = \sum_{t=0}^{T} \left( \log \frac{\exp(\text{sim}(e_{t,a_t}, e_t^{anchor})/\tau)}{\sum_{i \in C_t} \exp(\text{sim}(e_{t,i}, e_t^{anchor})/\tau)} \right)
$$

其中 $e_t^{anchor}$ 通过候选变量嵌入的最大池化（Max Pooling）获得，$\tau$ 为温度系数。该设计动机在于，B&B中候选变量特征高度相似，标准训练难以拉开选中变量与非选中变量的嵌入距离。通过CL预训练，嵌入层在下游模仿学习前已具备高判别力，使Mamba模型能更有效地感知变量动态演化模式，缓解了长序列建模中特征模糊导致的信用分配困难。

### Mamba自回归序列建模

鉴于分支路径长度随分支步数 $T$ 和候选变量数 $|C_t|$ 呈指数增长，Transformer的二次复杂度导致推理延迟过高，可能抵消求解加速收益。本文采用Mamba状态空间模型作为序列编码器，其计算复杂度与序列长度呈线性关系。在自回归范式下，策略 $\pi_\theta$ 基于历史轨迹 $\tau_{0:t} = (s_0, a_0, \dots, a_{t-1}, s_t)$ 预测当前步分支变量分布。联合损失函数为：

$$
\mathcal{L}(\theta, \gamma) = -\frac{1}{|\mathcal{D}|} \sum_{\tau \in \mathcal{D}} \sum_{(s_t, a_t) \in \tau} \log \pi_\theta(a_t | \tau_{0:t})
$$

其中 $\gamma$ 为嵌入层参数。Mamba通过线性复杂度处理超长序列，使得模型能够容纳100步分支历史，远超Transformer受硬件限制仅能处理的10步历史，从而在长程依赖捕捉上取得实质性突破。

## 实验评估

实验在MILP-S（19训练/8测试）和MILP-L（25训练/73测试）数据集上进行，后者包含57个易解实例和16个难解实例。基线涵盖神经分支方法（GCNN, TreeGate, T-BranT, Transformer-Branching）和经典启发式（pscost, relpscost）。缺失基线包括最新的强化学习方法（如PlanB&B）和解预测方法（PaS），这可能影响对本文方法在复杂动态环境下的相对优势评估。

| 方法 | MILP-S Nodes | MILP-S Time | MILP-L Easy Nodes | MILP-L Difficult PD Integral |
| :--- | :--- | :--- | :--- | :--- |
| Mamba-Branching | 2068.83 | 111.78 | 1819.32 | 12319.55 |
| TreeGate | 2091.54 | 113.85 | 2218.29 | 14625.68 |
| T-BranT | 2668.62 | 165.59 | 2009.77 | 13538.47 |
| Transformer-Branching | 3078.56 | 3153.66 | OOM | - |
| relpscost | 7308.23 | 209.30 | 3681.06 | 17097.06 |

Mamba-Branching在MILP-S和MILP-L Easy实例上节点数均低于TreeGate和T-BranT，且在MILP-L Difficult实例上PD Integral显著优于所有神经基线，表明其在难解实例上的长期规划能力更强。然而，在MILP-S上，Mamba-Branching的节点数（2068.83）仍高于relpscost（7308.23）？不，relpscost是7308.23，Mamba是2068.83，Mamba更优。但在Table 3的Set Covering辅助实验中，Mamba-Branching节点数265.07高于relpscost的170.81，尽管时间9.64秒低于relpscost的11.96秒，显示其在特定同质场景下节点效率并非绝对优势。

消融实验显示，移除对比学习（w/o CL）导致Mamba-Branching-p节点数从2272.43上升至3001，验证了CL对嵌入判别力的关键作用。移除位置编码（w/o PE）后性能下降，证实序列顺序信息的重要性。Transformer-Branching-p因硬件限制仅使用10步历史，节点数高达5138.15，远差于Mamba-Branching-p的2272.43，凸显了长序列建模能力的决定性影响。

评估边界方面，实验未报告置信区间，且MILP-L Difficult实例因1小时时限无法获得最优解，仅使用PD Integral评估，可能低估实际求解时间。代码已开源，但超参数细节（如Mamba层数、隐藏维度）仅在附录中简要提及，复现需仔细核对。

## 关联研究分析

从问题动机看，Mamba-Branching与T-BranT均旨在解决跨实例泛化问题，但T-BranT将历史节点建模为无序图，忽略了分支决策的时间因果性。本文指出，B&B树的扩展本质是序列化过程，无序图编码无法区分“先分支变量A再分支B”与“先B再A”的路径差异，导致模型无法利用路径信息规避死胡同。这一差异源于对B&B动态结构的理解深度：T-BranT视历史为静态上下文，而Mamba-Branching视历史为动态轨迹。这种设计选择使得Mamba-Branching在长程依赖任务上表现更优，但在短历史场景下，其线性复杂度优势可能不如Transformer显著，论文未对此进行详细对比。

从方法设计看，Mamba-Branching与PlanB&B（Strang et al., 2025）均关注分支策略的长期优化，但PlanB&B采用模型基础强化学习（MBRL）和蒙特卡洛树搜索（MCTS）解决稀疏奖励问题，而Mamba-Branching采用自回归模仿学习。PlanB&B的优势在于能评估长期后果，但计算开销大；Mamba-Branching的优势在于推理效率高，但依赖专家数据质量。二者代表了“探索-利用”与“模仿-泛化”的不同取舍。Mamba-Branching未引入奖励机制，完全依赖relpscost专家数据，若专家数据存在偏差，模型可能继承其局限性，而PlanB&B通过自主探索可能发现更优策略。

## 总结

Mamba-Branching旨在解决神经分支策略在异构MILP实例上因忽略B&B树序列性质导致的泛化瓶颈。通过对比学习预训练增强嵌入判别力，并利用Mamba线性复杂度特性处理超长分支路径，该方法在MILP-L难解实例上实现了PD Integral 12319.55，显著优于TreeGate的14625.68。然而，实验显示在Set Covering同质场景下，其节点数（265.07）仍高于relpscost（170.81），表明其优势高度依赖于异构性和长历史依赖。当分支历史较短或实例结构高度同质时，Mamba的长序列建模能力是否仍能带来净收益，论文未给出明确回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_76000939)