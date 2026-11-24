# ICLR2026最新论文 ｜Hilbert: Recursively Building Formal Proofs with Informal Reasoning ｜递归构建形式化证明的智能体框架

研究机构：美国加州大学圣迭戈分校

作者：Sumanth Varambally、Thomas Voice、Yanchao Sun 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.22819)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.22819)

> 通用大语言模型（LLM）在自然语言数学推理上表现优异，但生成的证明常含逻辑谬误且无法机器验证，而专用证明器（Prover LLM）虽能生成可验证的 Lean 4 代码，却在复杂定理上因缺乏高层规划能力而大幅落后。现有智能体框架多采用单层分解或战术级迭代，难以应对长程依赖导致的子目标爆炸。HILBERT 通过递归子目标分解与“浅层求解”机制，将通用推理器的规划能力与专用证明器的执行能力解耦并闭环。该框架在公开模型中刷新了 MiniF2F 与 PutnamBench 的 SOTA，但其性能高度依赖底层推理器的数学能力，且推理时计算开销巨大，其泛化边界尚存疑。

## 研究背景

形式化定理证明的核心矛盾在于自然语言推理的灵活性与交互式定理证明器（ITP）严格逻辑验证之间的张力。当 LLM 尝试直接生成 Lean 4 证明时，长程依赖导致的幻觉使其在复杂定理上失效；反之，专用证明器虽能保证语法正确，却在需要调用大型库（如 Mathlib）引理或处理非标准类型系统行为时表现出脆弱性。这一困境要求系统既能进行高层数学规划，又能执行底层战术推导，且每一步都需通过 ITP 内核的实时验证。

早期工作如 DSP 和 LEGO-Prover 尝试用通用 LLM 生成证明草图，由自动定理证明器（ATP）填充细节，但受限于 ATP 的启发式能力，无法处理复杂子目标。后续智能体框架如 COPRA 和 ProofCompass 引入了迭代修正，但多局限于单层分解或战术级反馈，缺乏对深层证明结构的递归处理能力。HILBERT 的切入点在于识别出“规划”与“执行”的能力错位：通用 LLM 擅长将复杂定理拆解为逻辑子问题，而专用 Prover 擅长解决独立的、结构简单的形式化命题。通过递归分解机制，HILBERT 将前者转化为后者的输入，从而在保持机器可验证性的前提下，突破了单一模型的能力上限。

## 核心方法

### 智能体证明框架参照系

HILBERT 属于智能体证明框架路线，其标准流程为：接收形式化陈述，生成证明，验证，若失败则基于反馈修正。与仅依赖 Prover 迭代修正的框架不同，HILBERT 的关键差异在于引入通用推理器（Reasoner）作为“规划引擎”，负责子目标提取与错误诊断，而 Prover 仅作为“执行引擎”处理独立子目标。这种分工解决了 Prover 在语言密集型任务（如引理检索、错误归因）上的短板。

### 递归子目标分解与组装

当 Prover 直接证明失败时，Reasoner 介入生成包含 `sorry` 占位符的证明草图，并将草图中的 `have` 语句提取为独立定理。这一过程可形式化为：给定目标定理 $T$，Reasoner 生成草图 $S$，其中 $S = \{h_1, ..., h_n\}$，每个 $h_i$ 为子目标。系统验证 $S$ 的结构有效性，确保 $\bigwedge_{i=1}^n h_i \vdash T$ 成立。设计动机在于，单层分解无法处理子目标本身仍过于复杂的情况，递归机制允许系统对未解决的子目标 $h_i$ 再次应用分解过程，直至子目标简化到 Prover 可解的程度。

### 浅层求解与递归终止

对于 Prover 无法直接证明但数学上正确的子目标，HILBERT 引入“浅层求解”（Shallow Solve）阶段。Reasoner 结合检索到的 Mathlib 引理，尝试生成短证明（长度阈值 $K_{max} = 30$ 行）。若浅层求解失败，则触发递归分解。该机制的公式化表达为：若 $Prover(h_i) = \emptyset$ 且 $Reasoner(h_i)_{shallow} = \emptyset$，则 $h_i \leftarrow \{h_{i,1}, ..., h_{i,m}\}$。设计动机在于，浅层求解提供了递归前的最后一道防线，避免了将所有中等难度子目标都送入递归导致的计算爆炸，同时通过长度阈值防止 Reasoner 生成冗长且难以验证的“伪证明”。

## 实验评估

HILBERT 在 MiniF2F-test（244 题）和 PutnamBench（660 题）上进行了评估。基线覆盖包括 Goedel-Prover、DeepSeek-Prover、BFS-Prover 等开源 SOTA 及 SeedProver 等私有系统，但缺失了近期基于大规模强化学习的 Pythagoras-Prover 等模型。

| 方法 | MiniF2F 准确率 (%) | PutnamBench 准确率 (%) |
| :--- | :--- | :--- |
| Goedel-Prover-V2-32B (pass@4) | 74.6 | 13.4 |
| SeedProver | 50.4 | 50.4 |
| HILBERT (gpt-oss-120b) + Goedel-Prover-V2-32B | 90.8 | 13.3 |
| HILBERT (Gemini 2.5 Pro) + Goedel-Prover-V2-32B | 99.2 | 70.0 |

HILBERT 使用 Gemini 2.5 Pro 时，MiniF2F 准确率达 99.2%，较最佳公开基线提升 6.6 个百分点；PutnamBench 准确率达 70.0%，较 SeedProver 提升近 20 个百分点。值得注意的是，使用开源 gpt-oss-120b 作为推理器时，PutnamBench 准确率仅为 13.3%，与 Goedel-Prover 基线持平，表明框架性能高度依赖推理器的数学能力。

消融实验显示，移除检索模块后，MiniF2F 准确率从 99.2% 降至 97.9%，且推理 token 数从 2.3M 增至 4.0M，证明检索不仅提升精度，还显著降低计算开销。递归深度 $D=2$ 时，MiniF2F 准确率已达 98.36%，$D=3$ 时达 98.7%，表明浅层分解即可解决绝大多数问题，深层递归主要服务于极少数复杂定理。

评估边界方面，论文未报告置信区间，MiniF2F 测试集仅 244 题，统计波动可能影响结果解读。代码已开源，但推理时计算开销巨大（最难题需 27.0M tokens），限制了其在大规模库维护中的实用性。

## 关联研究分析

从问题动机看，HILBERT 与 DSP+ 的核心差异在于分解深度。DSP+ 采用单层分解，假设子目标可直接由 Prover 解决，而 HILBERT 通过递归机制处理子目标仍复杂的情况。这一差异源于任务特性：PutnamBench 等研究级基准的证明结构往往具有多层嵌套逻辑，单层分解无法覆盖。HILBERT 的递归设计是对长程依赖问题的直接响应，但论文未探讨递归深度 $D$ 与证明结构复杂度的定量关系，仅通过消融验证了 $D=5$ 的充分性。

从方法设计看，HILBERT 与 COPRA 的区别在于反馈粒度。COPRA 侧重战术级迭代，即 Prover 生成战术，Verifier 反馈错误，Prover 修正战术；而 HILBERT 侧重结构级分解，即 Reasoner 提取子目标，Prover 解决子目标，Verifier 验证结构。HILBERT 引入 Reasoner 进行错误诊断，而非仅依赖 Prover 的自修正，这解决了 Prover 在“为什么错”这一归因问题上的短板。然而，HILBERT 依赖 Reasoner 的数学正确性判断，若 Reasoner 误判子目标为“正确”但实际不可证，系统将陷入无效递归。论文未提供 Reasoner 误判率的统计，这一盲区可能影响框架在极端案例下的鲁棒性。

## 总结

HILBERT 旨在解决通用 LLM 推理能力与专用 Prover 执行能力之间的割裂，通过递归子目标分解与浅层求解机制，将两者整合为闭环智能体框架。其核心贡献在于证明了“规划-执行”解耦的有效性，在 MiniF2F 上达到 99.2% 准确率，在 PutnamBench 上达到 70.0% 准确率，显著优于现有公开基线。然而，实验暴露出框架性能对底层推理器数学能力的强依赖：使用开源 gpt-oss-120b 时，PutnamBench 准确率骤降至 13.3%，与基线无异。这一局限暗示，HILBERT 的增益并非完全来自架构设计，而是部分来自 Gemini 2.5 Pro 的固有数学能力。当推理器能力接近 Prover 时，递归分解的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.22819)