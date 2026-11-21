# ACL-Findings2026最新论文 ｜Regret-Now: A Physics-Inspired Regret Framework for Temporal Knowledge Graph Question Answering with LLMs ｜基于最小势能原理的时序知识图谱问答框架

研究机构：南开大学

作者：Danyu Huang、Yao Zhang、Jun Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_69a4e4eacf29)

> 时序知识图谱问答（TKGQA）要求模型在动态演化的知识结构中执行多步推理，但大语言模型（LLM）常因中间步骤的逻辑断裂导致级联错误，且现有自校正方法依赖主观自评，缺乏客观纠错标准。Regret-Now 将推理过程类比为粒子在势能场中的运动，通过监测语义势能的异常上升实时触发回滚机制，以物理量化指标替代 LLM 的主观反思。该框架在 CronQuestions 和 MultiTQ 上取得了优于 Reflexion 等基线的性能，但其依赖外部嵌入模型计算势能，且未与最新神经符号 SOTA 对比，其通用性存疑。

## 研究背景

时序知识图谱（Temporal Knowledge Graph, TKG）通过显式建模时间演化的关系，为 LLM 提供了结构化约束。然而，LLM 在 TKG 上的推理常出现“捷径”行为，即跳过必要的中间步骤直接得出结论，导致时间逻辑链条断裂。一旦某一步骤出错，后续推理将沿着错误路径继续，传统方法缺乏实时监测与动态纠错能力，难以挽救已断裂的推理链。

早期 TKGQA 方法主要依赖规则分解或知识图谱嵌入，其推理路径是静态的，无法在推理过程中进行实时修正。随着 LLM 的引入，研究转向基于智能体的框架，结合检索工具增强时间敏感性。然而，这些方法多为“结果导向”，缺乏推理过程中的动态验证机制，极易受级联错误影响。现有的自校正方法如 Reflexion 和 Tree-of-Thoughts (ToT) 虽然引入了反思或回溯，但其纠错决策依赖于 LLM 自身的主观评估，存在偏差且缺乏可解释性。Regret-Now 的切入点在于引入一个可量化的外部标准——最小势能原理，以客观地评估每一步推理的稳定性，从而实现实时检测与动态回滚。

## 核心方法

### 方法参照系

Regret-Now 属于神经符号推理路线，其核心流程继承自基于 LLM 的 TKGQA 框架：LLM 根据当前状态选择操作，执行检索，并基于结果进行下一步决策。与 Reflexion 等依赖 LLM 自评的方法不同，Regret-Now 在决策与执行之间插入了一个基于物理量（势能）的客观判断模块，将主观的“反思”转化为定量的“能量监测”。

### 语义势能建模

传统自校正方法缺乏客观标准，导致纠错方向不可控。Regret-Now 将 TKG 实体视为粒子，关系视为力，基于牛顿万有引力定律定义语义势能。势能 $U$ 由实体间的语义距离 $r$ 决定，距离越近，势能越低，系统越稳定。

$$
U = -\frac{Gm_1m_2}{r}
$$

其中 $G$ 为引力常数，$m_1, m_2$ 为粒子质量，$r$ 为嵌入空间中的语义距离。该公式的物理含义是：正确的推理步骤应使系统趋向更低的势能状态（更稳定的语义匹配），而错误的推理则表现为势能的异常上升（“上坡”）。

### 势能判断与后悔机制

单一势能难以区分实体推理与时间推理的偏差。Regret-Now 将势能解耦为内容级 $U_{ent}$ 和时间级 $U_{time}$，并根据当前操作类型选择相应的势能维度进行监测。

$$
U_{ent} = -\frac{Gm_1m_2}{\text{Re}(\langle u_s, q_{ent}, u_e^*, w_t \rangle) + \epsilon}
$$

当监测到势能增量 $\Delta U(k) = U(k) - U(k-1) > \tau$ 时，触发后悔模块（Regret Module）。该机制立即回滚至错误步骤之前，并将失败操作作为负反馈注入提示词，引导 LLM 重新选择更合理的操作。这一设计解决了 LLM 自评偏差问题，通过物理阈值 $\tau$ 实现了客观、可解释的实时纠错。

## 实验评估

Regret-Now 在 CronQuestions（410K 问题）和 MultiTQ（500K 问题）上进行评估，基线涵盖 BERT、CronKGQA、TSQA 以及 ToT、Reflexion 等 LLM 自校正方法。

| 方法 | CronQuestions (Hit@1) | MultiTQ (Hit@1) |
| :--- | :--- | :--- |
| Reflexion | 0.815 | 0.271 |
| Regret-Now (w/o RS) | 0.848 | 0.504 |
| Regret-Now (ours) | 0.876 | 0.543 |

Regret-Now 在两个数据集上均优于 Reflexion 和 ToT，尤其在 MultiTQ 的多跳推理任务上表现显著。消融实验显示，移除后悔阶段（RS）导致 CronQuestions 性能下降 2.8%，MultiTQ 下降 3.9%；移除自适应势能选择（PE-Sel）导致 MultiTQ 性能大幅下降 8.8%，证实了势能解耦的必要性。

| 消融变体 | CronQuestions 降幅 | MultiTQ 降幅 |
| :--- | :--- | :--- |
| w/o RS | 2.8% | 3.9% |
| w/o PE-Sel | 2.6% | 8.8% |

评估边界方面，论文使用 Hit@1 作为唯一指标，未报告置信区间。代码已开源，但势能计算依赖 TComplEx 和 CronKGQA 的预训练嵌入，限制了其在无嵌入模型场景下的适用性。

## 关联研究分析

从方法设计看，Regret-Now 与 Reflexion 的核心差异在于纠错标准的客观性。Reflexion 依赖 LLM 生成自然语言反思，其纠错方向受模型内部偏差影响；而 Regret-Now 利用嵌入空间的几何距离计算势能，提供了可量化的物理约束。这种差异源于任务特性：TKGQA 涉及结构化实体关系，嵌入空间距离能有效反映语义一致性，而通用推理任务缺乏这种结构化的度量基础。

从问题动机看，Regret-Now 与 ODL-TempLLM 等神经符号方法同属利用外部结构约束 LLM 的路线，但 Regret-Now 更侧重于推理过程中的动态监控，而非静态的本体约束。ODL-TempLLM 通过本体规则限制生成空间，而 Regret-Now 通过势能监测动态调整推理路径。这种差异暗示了两种不同的失效模式：前者防止生成非法结构，后者防止推理逻辑断裂。Regret-Now 未与 ODL-TempLLM 对比，可能是由于后者依赖特定的本体库，而 Regret-Now 更通用，但这也使得其在结构化逻辑一致性上的优势难以直接量化。

## 总结

Regret-Now 针对 LLM 在 TKGQA 中推理链断裂且缺乏客观纠错标准的问题，引入最小势能原理，通过监测语义势能的异常上升实时触发回滚。实验表明，该框架在 CronQuestions 上达到 0.876 的 Hit@1，优于 Reflexion 的 0.815，验证了物理量化指标在动态纠错中的有效性。然而，其势能计算依赖外部嵌入模型，且未与最新神经符号 SOTA（如 TECQA）对比，限制了其性能定位的准确性。当嵌入模型无法准确反映时间粒度差异时，势能监测是否仍能可靠地识别推理错误，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_69a4e4eacf29)