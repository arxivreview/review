# ICLR2026最新论文 ｜SQUEEZE THE SOAKED SPONGE: EFFICIENT - OFF POLICY RFT FOR LARGE LANGUAGE MODEL ｜离策略强化微调：ReMix 机制与效率-精度权衡

研究机构：天津大学

作者：Jing Liang、Jinyi Liu、Yi Ma 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_24960764)

> 导读

大语言模型（LLM）的强化微调（Reinforcement Finetuning, RFT）长期受限于在线策略算法的样本低效性，导致训练成本随模型规模呈指数级增长。现有方法如 PPO 和 GRPO 虽稳定但无法复用历史数据，而直接引入离策略机制又常引发训练崩溃。ReMix 通过混合策略近端策略梯度、KL-凸约束及策略重生成机制，在保持精度的同时大幅降低 Rollout 开销。该方案在 1.5B 和 7B 模型上实现了 30 至 450 倍的训练成本缩减，但其对推理路径多样性的潜在影响及与细粒度信用分配方法的兼容性尚存疑。

## 研究背景

当 LLM 执行复杂推理任务时，强化学习需通过试错生成大量响应以优化策略。这一过程依赖在线策略算法，如近端策略优化（Proximal Policy Optimization, PPO）和组相对策略优化（Group Relative Policy Optimization, GRPO），它们仅利用当前策略生成的数据，导致历史 Rollout 数据被丢弃。这种数据浪费使得 RFT 的计算成本远高于监督微调（SFT），成为限制模型规模扩展的关键瓶颈。为突破此限制，研究界开始探索离策略强化学习（Off-Policy RL），旨在复用历史策略生成的数据以提升样本效率。

主流 RFT 路线如 PPO 和 GRPO 虽在稳定性上表现优异，但其在线策略特性导致数据利用率极低。近期尝试引入离策略数据的方法，如非均匀重放策略或不对称信号学习，均未在多个主流数学推理基准上进行系统性对比，且离策略学习对推理能力演化过程的影响机制不明。ReMix 的切入点在于构建一个通用的离策略框架，使 PPO 和 GRPO 等在线策略方法能高效利用历史数据，同时通过动态约束机制防止训练不稳定，从而在效率与精度间取得平衡。

## 核心方法

### 方法参照系

ReMix 基于 PPO 和 GRPO 的近端策略梯度框架，核心差异在于数据采样分布与约束机制。标准 PPO 仅使用当前策略数据，而 ReMix 引入历史策略数据混合采样，并动态调整 KL 约束锚点，以支持离策略训练。

### 混合策略近端策略梯度

标准 PPO 的优化目标仅基于当前策略 $\pi_k$ 生成的数据，导致历史数据无法复用。ReMix 引入混合策略近端策略梯度（Mix-PPG），通过混合当前策略 $\pi_k$ 和历史策略 $\pi_{k-i}$ 的数据进行训练。其优化目标为：

$$
L_{\text{Mix-PPG}}^k(\theta) = \mathbb{E}_{s \sim d^s[\pi_k], a \sim \pi_{k-i}(\cdot|s)} \left[ \min \left( r_{\theta}^{[k-i]}(s,a) \hat{A}(s,a), \text{clip}(r_{\theta}^{[k-i]}(s,a), 1-\epsilon, 1+\epsilon) \hat{A}(s,a) \right) \right]
$$

其中 $r_{\theta}^{[k-i]}(s,a) = \frac{\pi_k(a|s)}{\pi_{k-i}(a|s)}$ 为重要性采样比率。该设计通过复用历史数据降低 Rollout 开销，但需平衡数据复用与分布对齐，避免离策略偏差导致训练崩溃。

### KL-凸约束与策略重生成

传统 RFT 使用静态 KL 约束指向基础模型 $\pi_{\text{base}}$，无法适应策略动态演化。ReMix 引入 KL-凸约束（KLC），将 KL 约束锚点设为 $\pi_{\text{base}}$ 和前一策略 $\pi_{k-1}$ 的凸组合：

$$
L_{\text{KLC}}(\theta; \pi_{\text{base}}, k) = \mathbb{E}_s \left[ \lambda D_{\text{KL}}(\pi_\theta(\cdot|s) \| \pi_{\text{base}}(\cdot|s)) + (1-\lambda) D_{\text{KL}}(\pi_\theta(\cdot|s) \| \pi_{k-1}(\cdot|s)) \right]
$$

其中 $\lambda$ 随训练步数线性衰减。该机制在保持基础能力的同时允许策略迭代优化。此外，ReMix 引入策略重生成（Policy Reincarnation），在训练中期将基础模型重置为当前策略 $\pi_T$，并切换回纯在线策略训练，实现从高效早期学习到稳定渐近收敛的无缝过渡。

## 实验评估

ReMix 在 DeepSeek-R1-Distill-Qwen-1.5B 和 7B 模型上，使用 DeepScaleR-Preview-Dataset 进行训练，并在 AIME'24、AMC'23、Minerva、OlympiadBench 和 MATH500 五个基准上评估。基线覆盖 DeepScaleR、FastCuRL、AdaptThink 等 15 个近期先进模型，但未包含 SSVPO、EP-GRPO 等最新细粒度信用分配方法。

| 模型 | AIME'24 | AMC'23 | MATH500 | Minerva | Olympiad | Avg. | Cost (Rollouts) |
|---|---|---|---|---|---|---|---|
| R1-Distill-Qwen-1.5B (Base) | 33.33 | 43.37 | 67.40 | 16.54 | 27.26 | 37.58 | N/A |
| DeepScaleR | 40.00 | 67.60 | 74.20 | 20.22 | 32.59 | 52.14 | 2.519M |
| ReMix-PPO (350 Steps) | 36.67 | 69.88 | 82.00 | 30.15 | 41.78 | 52.10 | 0.079M |
| R1-Distill-Qwen-7B (Base) | 33.33 | 68.68 | 83.80 | 30.15 | 44.44 | 52.08 | N/A |
| AceReason-Nemotron | 60.00 | 80.72 | 89.00 | 36.40 | 50.07 | 63.24 | >3.584M |
| ReMix-PPO (75 Steps) | 63.33 | 78.31 | 90.20 | 37.50 | 52.59 | 64.39 | 0.011M |

ReMix-PPO 在 1.5B 模型上以 0.079M Rollouts 达到 52.10% 平均 Pass@1，较 DeepScaleR 的 2.519M Rollouts 降低 30 倍以上；在 7B 模型上以 0.011M Rollouts 达到 64.39%，较 AceReason-Nemotron 的 >3.584M Rollouts 降低 450 倍以上。

| 模型 | AIME'24 | AMC'23 | MATH500 | Minerva | Olympiad | Avg. |
|---|---|---|---|---|---|---|
| ReMix-PPO (350 Steps) | 36.67 | 69.88 | 82.00 | 30.15 | 41.78 | 52.10 |
| ReMix-PPO w/o UTD | 36.67 | 62.65 | 82.20 | 28.68 | 42.96 | 50.63 |
| ReMix-PPO w/o KL-Convex | 30.00 | 65.06 | 81.60 | 27.94 | 42.22 | 49.36 |
| ReMix-PPO w/o Policy Reincarnation | 20.00 | 67.47 | 82.00 | 26.84 | 40.00 | 47.26 |

消融实验显示，移除策略重生成导致平均性能下降 4.84 点，移除 KL-凸约束下降 2.74 点，移除 UTD 比率下降 1.47 点。策略重生成对渐近性能的影响最大，表明离策略偏差在训练后期显著限制性能提升。

评估协议采用 Pass@1 和 Avg@32，但未报告置信区间，小样本基准（如 AIME'24）的高方差可能影响结果稳定性。代码和模型已开源，超参数设置（如 $p=0.4$, $m=2$, $N=2$）在附录中详细列出，1.5B 模型在 2 块 A800 GPU 上训练 50 小时，7B 模型在 8 块 GPU 上训练 75 小时。

## 关联研究分析

从问题动机看，ReMix 与 DAPO 均关注训练稳定性，但 DAPO 通过解耦裁剪和动态采样缓解梯度消失，而 ReMix 通过数据复用降低计算成本。DAPO 未解决样本效率问题，其动态采样仍依赖在线生成，而 ReMix 的混合策略机制直接复用历史数据，这是两者在效率维度上的根本差异。ReMix 的离策略机制可能加剧熵坍缩，但论文未提供熵值监控数据，这一潜在风险未得到验证。

从方法设计看，ReMix 与 FastGRPO 均追求加速，但 FastGRPO 优化生成阶段的推测解码，而 ReMix 优化训练阶段的数据利用率。FastGRPO 的加速依赖于草稿模型与目标策略的匹配，而 ReMix 的加速依赖于历史策略数据的复用率。ReMix 未涉及细粒度信用分配，其优势估计仍为序列级，这与 SSVPO 等步骤级方法形成对比。ReMix 的效率优势是否能在细粒度信用分配框架中保持，论文未给出回答。

## 总结

ReMix 旨在解决在线策略 RFT 的样本低效性，通过混合策略近端策略梯度、KL-凸约束及策略重生成机制，在保持精度的同时大幅降低训练成本。实验显示，ReMix-PPO 在 1.5B 模型上以 0.079M Rollouts 达到 52.10% 平均 Pass@1，较 DeepScaleR 降低 30 倍以上；在 7B 模型上以 0.011M Rollouts 达到 64.39%，较 AceReason-Nemotron 降低 450 倍以上。其边界在于未验证离策略机制对推理路径多样性的影响，且未与细粒度信用分配方法结合。当历史策略数据与当前策略分布差异过大时，KL-凸约束的线性衰减是否足以防止训练崩溃，论文未提供充分证据。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_24960764)