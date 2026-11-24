# ACL2026最新论文 ｜ARES: Adaptive Red-Teaming and End-to-End Repair of Policy-Reward System ｜自适应红队测试与端到端系统修复

研究机构：美国石溪大学

作者：Jiacheng Liang、Yao Ma、Tharindu Kumarage 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18789)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18789)

> 强化学习从人类反馈（Reinforcement Learning from Human Feedback, RLHF）管道中，核心语言模型（Core LLM）与奖励模型（Reward Model, RM）的耦合失效常被忽视，导致系统级安全漏洞。现有红队测试多聚焦于单一组件，无法同时暴露策略与奖励机制的联合盲区。ARES 提出双目标探测与顺序修复框架，通过自适应生成对抗提示并联合优化 RM 与 LLM，实现系统级安全对齐。该方法在 1.7B 小模型上显著提升了安全鲁棒性，但其对大规模模型及复杂推理场景的泛化能力仍存疑。

## 研究背景

RLHF 依赖 RM 提供偏好信号以引导 Core LLM 生成安全响应，但 RM 本身可能存在训练数据偏差或评估盲区。当 RM 未能正确惩罚有害行为时，Core LLM 可能利用这一漏洞生成不安全内容，形成“策略-奖励”耦合失效。这种失效并非单一组件故障，而是两者协同作用下的系统性漏洞，传统单点修复方法难以覆盖。

早期自动化红队测试如 FLIRT、APRT 等主要关注 Core LLM 的越狱防御，将 RM 视为理想评估器；而 AdvRM 等仅加固 RM，忽略 Core LLM 的潜在漏洞。这种碎片化方法无法识别“RM 误判 + LLM 生成有害内容”的联合失效模式，导致安全对齐存在结构性盲区。ARES 的切入点在于将 RM 与 Core LLM 视为耦合系统，通过双目标探测暴露联合漏洞，并实施顺序修复以消除系统性风险。

## 核心方法

### 方法参照系

ARES 属于对齐训练优化范畴，但区别于传统单模型 RLHF，其核心差异在于将 RM 与 Core LLM 作为联合优化对象。标准 RLHF 流程中，RM 固定不变，仅优化 Core LLM；而 ARES 引入“双组件修复”范式，先修复 RM 再优化 Core LLM，确保奖励信号本身具备鲁棒性。

### 组合式对抗生成与双目标分类

ARES 的 Safety Mentor 通过组合 Topic、Persona、Goal、Tactic 四类组件生成语义连贯的对抗提示，确保攻击覆盖广泛漏洞空间。每个提示生成三元组：对抗提示、合成有害响应 $y_{synth}$ 和偏好安全响应 $y_{chosen}$。双目标分类通过并行评估 Core LLM 响应与 RM 对 $y_{synth}$ 的评分，识别三类失效：Type A（RM 误判）、Type B（LLM 漏洞）、Type C（系统级失效）。该设计解决了传统红队测试仅关注 LLM 输出的局限，通过 RM 评分直接暴露奖励机制盲区。

$$
s_{rm}(y_{synth}) \text{ 与 } s_{judge}(y_{llm}) \text{ 的联合分布决定失效类型}
$$

此公式表明，失效类型由 RM 对合成有害响应的评分与 LLM 实际响应的安全评分共同决定，Type C 失效要求两者同时失效，即 $s_{rm}(y_{synth})$ 高且 $s_{judge}(y_{llm})$ 低。

### 层级自适应采样与顺序修复

ARES 采用两级自适应采样机制：实例级权重 $w_c$ 在攻击成功后按 $w_c' = w_c(1 + \alpha)$ 更新，类别级权重同步增强，防止过度特化。修复阶段先微调 RM 以纠正 Type A 和 Type C 失效，再用修复后的 RM 优化 Core LLM。顺序修复确保 Core LLM 学习基于鲁棒奖励信号，避免被原始 RM 的漏洞误导。

$$
w_c' = w_c(1 + \alpha), \quad \alpha = 0.2
$$

该公式通过乘性更新强化成功攻击策略，$\alpha$ 值平衡探索与利用，0.2 的设定在实验中验证了稳定性。

## 实验评估

实验基于 Qwen3-1.7B 与 SkyworkRM-Qwen3-4B，使用 HarmBench、StrongReject、XSTest 等基准。基线覆盖 FLIRT、APRT、FERRET 等红队方法，但缺乏激活引导类基线（如 ActAdd）。主结果显示 ARES 在 StrongReject 上达到 0.97 安全率，HarmBench 0.95，XSTest 过度拒绝率 0.10，均优于基线。

| 基准 | Initial RLHF | Safe-RLHF | ARES (Qwen) | ARES (Ministral) |
|---|---|---|---|---|
| StrongReject | 0.79 | 0.94 | 0.97 | 0.96 |
| HarmBench | 0.75 | 0.88 | 0.95 | 0.96 |
| XSTest | 0.07 | 0.09 | 0.10 | 0.09 |

消融实验表明，自适应采样机制显著提升安全率，移除 HelpSteer 数据导致 MMLU 下降 0.05，移除 FalseReject 使 XSTest 过度拒绝率升至 0.19。数据效率方面，4k 样本即超越 10.8k 样本的 PKU-SafeRLHF 基线。

评估边界受限于 1.7B 小模型规模，未验证大规模模型下的计算成本与收敛性。代码未公开，超参数（如 $\alpha=0.2$）依赖探索性实验，可复现性受限。

## 关联研究分析

从问题动机看，ARES 与 AdvRM 均关注 RM 鲁棒性，但 AdvRM 仅加固 RM 对抗分布外攻击，忽略 Core LLM 漏洞；ARES 通过双目标探测暴露联合失效，解决“RM 误判 + LLM 生成有害内容”的系统性风险。差异根源在于任务特性：AdvRM 假设 RM 是主要瓶颈，而 ARES 认为策略-奖励耦合失效需联合修复。

从方法设计看，ARES 与 FLIRT 共享自适应红队思路，但 FLIRT 仅优化 Core LLM，ARES 引入顺序修复机制。FLIRT 的反馈循环用于生成对抗提示，ARES 扩展至 RM 评分评估，形成闭环。差异源于对 RM 角色的认知：FLIRT 视 RM 为固定评估器，ARES 视其为可修复组件。

## 总结

ARES 解决的核心矛盾是 RLHF 管道中策略-奖励耦合失效导致的系统性安全漏洞。其切入点在于将 RM 与 Core LLM 视为联合系统，通过双目标探测暴露联合盲区，并实施顺序修复。方法通过组合式对抗生成与层级自适应采样，实现高效漏洞发现；顺序修复确保 Core LLM 学习基于鲁棒奖励信号。实验证明 ARES 在 1.7B 模型上 StrongReject 安全率达 0.97，HarmBench 0.95，显著优于基线。边界在于未验证大规模模型下的计算成本与收敛性，且依赖 8B 模型作为 Safety Mentor。当模型规模扩大至 70B 以上时，双目标探测的计算开销是否线性增长，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18789)