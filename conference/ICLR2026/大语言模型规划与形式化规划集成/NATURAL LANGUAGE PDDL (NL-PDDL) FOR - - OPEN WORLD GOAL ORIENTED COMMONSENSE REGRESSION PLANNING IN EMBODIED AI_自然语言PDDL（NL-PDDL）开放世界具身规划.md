# ICLR2026最新论文 ｜NATURAL LANGUAGE PDDL (NL-PDDL) FOR - - OPEN WORLD GOAL ORIENTED COMMONSENSE REGRESSION PLANNING IN EMBODIED AI ｜自然语言PDDL（NL-PDDL）开放世界具身规划

研究机构：加拿大多伦多大学、加拿大向量研究所

作者：Xiaotian Liu、Armin Toroghi、Jiazhou Liang 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_41880196)

> 开放世界具身规划要求智能体在部分可观测且领域知识不完整的环境中，通过常识推理确定达成目标所需的动作序列及感知需求。现有大语言模型（LLM）直接生成计划时缺乏状态追踪机制，易产生幻觉，而经典PDDL规划器虽逻辑严谨却依赖完全接地且无法处理自然语言中的语义错位。本文提出NL-PDDL框架，将PDDL符号扩展为自然语言表示，并引入基于LLM蕴含的提升回归算法，在避免穷举接地的同时解决目标与动作的语义对齐问题。该框架在ALFWorld文本与视觉任务上均取得94%和84%的成功率，显著优于基线，但其依赖LLM蕴含判断的可靠性及静态初始状态假设限制了其在动态环境中的泛化能力。

## 研究背景

开放世界规划面临的核心困境在于状态的不完整性与语义的模糊性。当智能体面对“加热面包”这一指令时，它必须识别出“烤”这一动作能实现“加热”的效果，这涉及常识蕴含推理。然而，经典PDDL规划器基于符号精确匹配，无法推断 `isToasted(bread)` 蕴含 `isHeated(bread)`，除非领域设计者显式编码该逻辑。这种符号刚性导致PDDL在开放世界中失效，因为实际环境中的对象和关系往往无法被完全预定义和接地。

为弥补LLM在长程逻辑推理中的缺陷，神经符号集成范式成为主流。早期方法如NL2PDDL（Guan et al., 2023）尝试将自然语言翻译为PDDL，再交由符号规划器求解，但这一两阶段范式存在表达瓶颈：翻译过程易引入错误的谓词或逻辑映射，且无法处理自然语言中固有的语义歧义。LLM+P（Liu et al., 2022）确立了LLM作为接口的混合架构，但仍依赖完整的PDDL生成。本文的切入点在于打破“先翻译后规划”的线性流程，直接在自然语言层面进行回归规划，利用LLM的常识推理能力在规划过程中动态解决语义错位，从而在保持符号规划逻辑严谨性的同时，获得自然语言的表达灵活性。

## 核心方法

### 方法参照系

NL-PDDL属于神经符号集成中的提升回归规划变体。与经典PDDL规划器依赖符号统一（Syntactic Unification）不同，本文的关键差异在于将统一机制替换为基于LLM的常识蕴含统一（Entailment-based Unification），允许谓词在语义层面而非语法层面匹配，从而支持开放世界下的部分可观测规划。

### 自然语言PDDL表示与提升回归

经典PDDL使用刚性符号表示谓词、对象和变量，而NL-PDDL将其替换为带类型的自然语言对应物。例如，符号谓词 `isToasted(bread)` 变为自然语言描述 “the (bread) is toasted” | “bread”:“food”，其中 `?o:food` 表示变量 `?o` 的类型为 `food`。这种表示允许用户以抽象、非完美的自然语言指定目标和动作，降低了领域建模负担。

提升回归（Lifted Regression）是NL-PDDL的核心机制，它避免了对具体对象（如 `pan3`, `toaster1`）的穷举接地。通过利用NL-PDDL中固有的变量，规划复杂度独立于对象数量。回归过程从目标公式出发，逆向推导达成目标所需的子目标。对于正谓词 $P_1(\vec{x})$，通过动作 $a_i$ 回归时，需找到可统一的谓词 $F(\vec{z})$，使得类型一致且蕴含成立：

$$
\text{Regr}^\$(P_1(\vec{x}), a_i) = \bigvee_{F(\vec{z}) \in \mathcal{F}^\$} \left( F_{a_i}(\vec{z}) \mid \theta \right)
$$

其中 $\mathcal{F}^\$ = \{ F_i(\vec{x}_i) \mid F_i(\vec{x}_i) \models_{LLM} P_1(\vec{x}) \}$ 是所有蕴含 $P_1$ 的谓词集合。该公式表明，子目标的生成依赖于LLM判断哪些动作效果在语义上蕴含目标状态，从而将常识推理嵌入规划搜索过程。

### 基于LLM蕴含的错位谓词回归

传统回归要求目标谓词与动作效果在语法上完全匹配，这在自然语言中极少发生。NL-PDDL引入基于LLM的蕴含统一，允许谓词在语义层面匹配。对于正谓词，统一条件为：(i) 类型一致，即 $t_x \models_{LLM} t_z$；(ii) 代入后动作效果蕴含目标，即 $F(\vec{z})\theta \models_{LLM} P_1(\vec{x})\theta$。对于负谓词 $\neg P_1(\vec{x})$，蕴含方向反转，即 $P_1(\vec{x})\theta \models_{LLM} F(\vec{z})\theta$。

这种设计解决了经典PDDL无法处理“加热”与“烤”之间语义错位的问题。例如，目标 “(bread) is heated” 可通过动作 “toast (?o) using (?r)” 回归，因为 “(?o) is toasted” 蕴含 “(?o) is heated”。当多个谓词蕴含同一目标时（如 “cooked” 可由 “toasted” 或 “boiled” 蕴含），NL-PDDL通过析取聚合所有蕴含谓词，生成条件计划 $\Pi$，映射子目标公式到动作序列。这一机制使得规划器能够在部分可观测环境中，通过LLM推理确定需要感知的信息（如“找到烤面包机”），而非依赖预定义的完整状态模型。

## 实验评估

实验在ALFWorld文本、ALFWorld视觉及Blocksworld三个领域进行，评估NL-PDDL在开放世界与封闭世界下的规划性能。基线覆盖直接LLM规划（GPT-4o, Gemini-2.0-Flash, LLaMA-3.1）、反思式规划（ReAct, Reflexion）及微调VLM（EMMA, InstructBLIP）。值得注意的是，基线中未包含PDDL-INSTRUCT等最新指令微调方法，可能低估了LLM在符号规划中的最新进展。

| 数据集 | 方法 | Token数 | 专家轨迹 | 微调 | 成功率(%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ALFWorld Text | GPT-4o | 1,358,934 | 0 | ✗ | 21 |
| ALFWorld Text | ReAct (w examples) | 5,507,266 | 0 | ✗ | 81 |
| ALFWorld Text | Reflexion-10 | NA | 0 | ✗ | 91 |
| ALFWorld Text | **NL-PDDL** | **443,407** | **0** | **✗** | **94** |
| ALFWorld Vision | GPT-4o | 1,823,539 | 0 | ✗ | 8 |
| ALFWorld Vision | EMMA-10 | NA | 15,237 | ✓ | 82 |
| ALFWorld Vision | **NL-PDDL** | **679,148** | **0** | **✗** | **84** |

NL-PDDL在ALFWorld文本上以94%的成功率超越ReAct（81%）和Reflexion-10（91%），且Token消耗仅为ReAct的1/12。在视觉任务上，NL-PDDL（84%）优于所有微调VLM，包括使用15,237条专家轨迹的EMMA-10（82%），表明其跨模态泛化能力。在封闭世界Blocksworld变体中，NL-PDDL在Mystery和Randomized Blocksworld上均保持70%成功率，而直接LLM规划器成功率降至0%-1%，验证了符号回归对语义扰动的鲁棒性。

消融实验显示，当目标与动作描述存在错位时（Misalignment Blocksworld），NL-PDDL成功率保持70%，而GPT-4o降至27%，ReAct降至79%（文本）和23%（模型）。这表明LLM蕴含统一机制是处理语义错位的关键。然而，NL-PDDL在Blocksworld上的70%成功率仍低于Fast Downward的100%，说明在完全可观测且符号明确的环境中，专用规划器仍具优势。

评估边界方面，论文未报告置信区间，且ALFWorld视觉任务中CoPiC达到100%成功率（据领域综述），与本文84%存在差距，可能源于评测子集或协议差异。代码未公开，超参数细节有限，可复现性依赖ALFWorld官方环境。

## 关联研究分析

从问题动机看，NL-PDDL与NL2PDDL（Guan et al., 2023）均旨在解决自然语言到形式化规划的转换，但NL2PDDL采用“翻译-求解”两阶段范式，而NL-PDDL采用“边推理边规划”的一体化流程。NL2PDDL的瓶颈在于翻译阶段的语义损失，导致下游规划失败；NL-PDDL通过提升回归将LLM推理嵌入规划过程，动态解决语义错位，避免了翻译的表达瓶颈。这一差异源于任务特性：开放世界下的部分可观测性要求规划器在规划过程中感知环境，而非依赖预生成的完整PDDL模型。

从方法设计看，NL-PDDL与Planner-in-the-Loop（Jiang et al., 2026）均利用外部验证器，但Planner-in-the-Loop将规划器诊断转化为后置修复信号，而NL-PDDL将LLM蕴含检查前置到回归步骤。Planner-in-the-Loop依赖固定符号语义下的局部修复，适用于安全关键应用；NL-PDDL依赖LLM的常识推理，适用于开放世界下的语义模糊场景。两者的差异反映了神经符号集成中验证时机与语义灵活性的权衡：后置修复保证逻辑正确性但牺牲语义灵活性，前置蕴含检查提升语义灵活性但依赖LLM推理的可靠性。

## 总结

NL-PDDL旨在解决开放世界具身规划中部分可观测性与语义模糊性的矛盾，通过自然语言PDDL表示与基于LLM蕴含的提升回归算法，在避免穷举接地的同时处理目标-动作错位。该框架在ALFWorld文本与视觉任务上分别取得94%和84%的成功率，显著优于直接LLM规划与微调VLM基线，验证了神经符号集成在开放世界中的有效性。然而，其依赖LLM蕴含判断的可靠性，且在封闭世界Blocksworld上未超越专用规划器Fast Downward（100% vs 70%），暴露了符号回归在完全可观测环境下的性能上限。当环境动态变化导致初始状态假设失效时，NL-PDDL的静态提升回归机制是否仍能保持规划有效性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_41880196)