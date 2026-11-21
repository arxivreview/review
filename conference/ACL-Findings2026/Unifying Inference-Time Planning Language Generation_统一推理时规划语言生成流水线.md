# ACL-Findings2026最新论文 ｜Unifying Inference-Time Planning Language Generation ｜统一推理时规划语言生成流水线

研究机构：美国宾夕法尼亚大学、美国西北大学

作者：Prabhu Prakash Kagitha、Bo Sun、Ishan Desai 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c72fc314f24f)

> 经典规划任务要求从自然语言描述生成可被符号求解器执行的 PDDL 模型，但 LLM 直接生成 PDDL 时极易出现语法或语义错误，导致计划失效。现有方法多采用单次生成加简单重试，缺乏对中间表示（IR）选择的系统性评估，且依赖闭源大模型，开源中小模型性能骤降。本文提出基于 IR 层级的统一框架，引入高资源、语法对齐的 PyPDDL 作为中间语言，通过多阶段推理时计算换取生成可靠性。该框架在开源 32B 模型上验证了 IR 与求解器反馈的关键作用，但未探索训练时优化与推理时优化的协同效应。

## 研究背景

当 LLM 尝试将自然语言规划问题转化为 PDDL 时，其自回归生成机制难以同时维持语法正确性与语义一致性。PDDL 是一种形式化规划语言，包含领域文件（DF）定义动作语义与问题文件（PF）定义初始状态和目标，任何细微错误都会导致符号求解器（如 Fast Downward）无法生成有效计划。这种脆弱性在开源中小模型上尤为突出，因为缺乏闭源模型的海量参数冗余来容忍生成噪声。

LLM-as-formalizer 范式旨在利用 LLM 的语义理解能力生成 PDDL，再由符号求解器保证逻辑正确性，这一路线在 LLM+P（Liu et al., 2022）中确立，并在 NL2PDDL（Guan et al., 2023）中引入迭代修复。然而，现有工作多聚焦于特定组件优化（如目标生成或动作语义提取），缺乏对流水线整体架构的系统性评估，且多数实验依赖闭源模型，导致开源模型上的性能瓶颈未被充分揭示。本文切入点在于将 LLM-as-formalizer 流水线抽象为基于中间表示（IR）层级的统一框架，系统评估不同 IR 组合与反馈机制对开源模型性能的影响。

## 核心方法

### 方法参照系

本文问题属于 PDDL 形式化生成路线，标准流程为 LLM 直接生成 PDDL 后调用求解器。关键差异在于本文不假设单次生成可靠，而是将生成过程分解为多级 IR 转换，引入推理时计算以弥补开源模型的生成缺陷。

### IR 层级框架

设计动机在于解决单次 PDDL 生成在开源模型上的高错误率问题。本文提出基于 IR 数量的层级框架，Level 0 为 LLM-as-planner（直接生成计划），Level 1 为单次 PDDL 生成，Level 2 为引入一个 IR 后生成 PDDL，Level 3 为引入两个 IR。框架的核心公式为：

$$
L = \mathcal{S}(\text{Transpile}(\text{IR}_k, \dots, \text{IR}_1, I))
$$

其中 $\mathcal{S}$ 为符号求解器，$\text{Transpile}$ 表示从输入 $I$ 经过 $k$ 个 IR 到最终 PDDL 的转换过程。该公式表明，计划质量取决于 IR 链路的转换保真度，而非单次生成的准确性。

### 高资源语法对齐 IR

设计动机在于 PDDL 语法刚性且资源低，直接生成易出错，而 Python 等高资源语言具有更丰富的语法结构和更强的 LLM 先验。本文引入 PyPDDL 作为 IR，它是 PDDL 的 Python 封装，语法与 PDDL 高度对齐但资源更高。转换过程定义为：

$$
\text{PDDL} = \text{LLM}(\text{PyPDDL}, \text{Doc}_{\text{PyPDDL}})
$$

其中 $\text{Doc}_{\text{PyPDDL}}$ 为 PyPDDL 文档。该设计利用 LLM 在 Python 上的强先验，通过语法对齐降低转译错误率，相比自然语言 IR 或 Python 模拟器，PyPDDL 在 8 个 LLM-领域组合中 consistently 提升性能。

## 实验评估

实验在 BlocksWorld、Logistics、Sokoban 和 CoinCollector 四个 IPC 基准上进行，每个环境包含 100 个实例。基线覆盖 LLM-as-planner 及不同 IR 组合，但未包含 RL 类方法（如 Planner-R1）或微调模型（如 PDDL-INSTRUCT）。

| 流水线层级 | 代表 IR 组合 | 核心发现 |
| :--- | :--- | :--- |
| Level 0 | LLM-as-planner | 与 Level 1 无明确胜负（3:5） |
| Level 1 | PDDL-base | 单次生成，性能不稳定 |
| Level 2 | PyPDDL → PDDL | 8/8 组合优于 Level 0 和 1 |
| Level 3 | PDDL → PDDL → PDDL | 6/8 组合达到最高计划准确率 |

消融实验显示，NL 作为 IR  consistently 降低性能，Python Simulator 效果不稳定，而 PyPDDL 和 PDDL 作为 IR  consistently 提升性能。PyPDDL → PDDL 与 PDDL → FB PDDL 在 4/8 组合中互有胜负，表明求解器反馈并非唯一有效修复手段。

评估边界方面，本文仅使用开源模型（QwQ-32B, Qwen3-32B, gpt-oss-120b, GLM-4.5-Air-FP8），未对比闭源模型或微调模型，绝对性能数值未报告，仅展示相对提升。代码开源，但超参数（如温度 0.4）和 GPU 配置（H100）未详细披露，可复现性依赖社区验证。

## 关联研究分析

从问题动机看，本文与 NL2PDDL（Guan et al., 2023）均关注 PDDL 生成的可靠性，但 NL2PDDL 聚焦于 VAL 验证器驱动的迭代修复，而本文将修复机制泛化为 IR 层级框架，并引入高资源 IR 作为新维度。差异根源在于任务特性：NL2PDDL 假设单次生成后通过反馈修正，而本文发现开源模型单次生成错误率过高，需前置 IR 降低生成难度。

从方法设计看，本文与 Bridge-Coder（Zhang et al., 2025）共享“高资源语言辅助低资源语言生成”的思路，但 Bridge-Coder 针对编程语言迁移，本文针对规划语言生成。关键差异在于语法对齐程度：PyPDDL 与 PDDL 语法高度相似，而 Bridge-Coder 中源语言与目标语言语法差异较大，这解释了为何 PyPDDL 在本文实验中 consistently 有效，而确定性编译（Py2PDDL）性能劣于 LLM 转译——语法对齐降低了 LLM 转译的认知负荷。

## 总结

本文要解决的核心矛盾是开源中小模型在 PDDL 生成上的高错误率与推理时计算效率的权衡。切入点在于将生成过程分解为多级 IR 转换，利用高资源语法对齐 IR（PyPDDL）降低单次生成难度，并通过求解器反馈实现定向修复。本文证明了 Level 2 流水线（PyPDDL → PDDL）在 8/8 组合中优于 Level 0 和 1，Level 3 在 6/8 组合中达到最高性能。边界在于仅评估推理时优化，未探索训练时微调与推理时 IR 的协同效应，且绝对性能数值未报告。当支持集增大到 5-shot 时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_c72fc314f24f)