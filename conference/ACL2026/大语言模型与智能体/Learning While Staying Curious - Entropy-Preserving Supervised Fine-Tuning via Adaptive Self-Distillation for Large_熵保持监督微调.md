# ACL2026最新论文 ｜Learning While Staying Curious: Entropy-Preserving Supervised Fine-Tuning via Adaptive Self-Distillation for Large Reasoning Models ｜熵保持监督微调

研究机构：香港城市大学、香港科技大学

作者：Hao Wang、Hao Gu、Hongming Piao 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.02244)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.02244)

> 大推理模型后训练中的“SFT-then-RL”范式面临SFT阶段熵坍缩导致RL探索空间受限的困境。现有熵正则化方法因无法区分事实与推理token，导致知识遗忘或无效探索。本文提出CurioSFT，通过自适应自蒸馏在SFT阶段保留有效熵。该方法在SFT阶段提升ID/OOD性能2.5/2.9分，并显著增强下游RL阶段性能，但受限于单模态数学任务验证。

## 研究背景

SFT阶段通过交叉熵损失最大化专家token似然，导致模型输出分布熵迅速下降，即熵坍缩。熵坍缩使模型陷入低多样性模式，压缩了后续RL阶段的搜索空间。为量化探索能力，研究常用token熵作为代理指标，但盲目最大化熵会引入无根据熵，破坏事实一致性。

主流后训练范式将SFT视为RL的冷启动初始化。然而，标准SFT的刚性模仿导致模型过度自信，RL阶段增益边际化甚至退化。直接添加熵损失虽能提升熵值，但无法区分高熵推理连接词（如“wait”）与低熵事实token，导致知识遗忘或探索无效。本文切入点在于：如何在SFT阶段区分token角色，选择性保留推理token的探索空间，同时稳定事实token的知识表征。

## 核心方法

### 方法参照系

标准SFT优化目标为最小化模型分布与one-hot专家分布的交叉熵。本文问题与该通用流程的关键差异在于：标准SFT假设专家轨迹为唯一最优解，而本文认为SFT应保留模型内在的探索能力，为RL阶段提供更高维度的搜索空间。

### 自探索蒸馏

标准SFT中，模型仅对齐one-hot目标，导致熵坍缩。本文引入自探索蒸馏，利用温度缩放构建高熵教师分布。设计动机是解决盲目熵正则化导致的无根据熵问题，通过保持token概率相对顺序，仅在模型有效探索空间内扩展多样性。教师分布定义为：

$$ \pi_{tch}(\cdot | \mathbf{s}_t; \hat{\tau}) = \text{Softmax}\left( \frac{z_\phi(\cdot | \mathbf{s}_t)}{\hat{\tau}} \right) $$

其中 $\hat{\tau} > 1$ 为教师温度。该公式物理含义是：通过提高温度平滑logits，生成一个熵更高但概率排序不变的分布，作为学生模型的对齐目标。

### 熵引导温度选择

固定温度无法适应不同token的熵需求。本文提出熵引导温度选择，基于token级熵增量动态调整教师温度。设计动机是解决token无关正则化导致的知识遗忘，通过软门控机制区分高熵推理token与低熵事实token。温度选择公式为：

$$ \Delta_t = \Delta_{max} \cdot \sigma\left( \gamma (H_t - H_{pivot}) \right) $$

其中 $H_t$ 为当前token熵，$H_{pivot}$ 为熵枢轴。该公式物理含义是：当token熵远高于枢轴时，sigmoid接近1，允许最大熵增量；当熵远低于枢轴时，sigmoid接近0，抑制熵增量，从而保护事实知识。

## 实验评估

实验基于Qwen2.5-Math-7B，使用OpenR1-Math-46K数据集，评测AIME、AMC、MATH-500等ID任务及GPQA、MMLU-Pro等OOD任务。基线覆盖Vanilla SFT、GEM、DFT、PSFT等SFT变体，但缺失OPD类方法（如RLAD）及自蒸馏类方法（如Purified OPSD）。

| 方法 | AIME24 | AIME25 | AMC23 | MATH. Miner. | Olymp. | Avg. ID | Avg. OOD |
|---|---|---|---|---|---|---|---|
| Vanilla SFT | 22.9 | 26.7 | 59.6 | 85.8 | 45.5 | 48.5 | 51.3 |
| CurioSFT | 26.3 | 29.6 | 59.9 | 87.0 | 49.8 | 51.0 | 54.2 |
| CurioSFT+GRPO | 39.2 | 30.4 | 72.7 | 91.7 | 54.9 | 58.7 | 61.7 |

CurioSFT在SFT阶段将ID平均准确率从48.5%提升至51.0%，OOD从51.3%提升至54.2%，同时token熵从0.31升至0.43。RL阶段，CurioSFT+GRPO在AIME24上达到39.2%，较SFT+RL基线（32.1%）提升7.1分，验证了SFT阶段保留的探索能力对RL增益的传导。

消融实验显示，移除熵引导温度选择模块（固定 $\hat{\tau}=1.3$）导致OOD性能下降2.0分（54.2%→52.2%），证实token级自适应对知识保留的关键作用。移除独立教师模型导致性能轻微下降，表明稳定教师信号对蒸馏目标的重要性。计算开销从43.2秒/步增至53.9秒/步，增加约25%，在可接受范围内。

评估边界方面，论文未报告置信区间，且仅在数学推理任务上验证，未覆盖代码生成或多模态场景。代码已开源，超参数（如 $H_{pivot}=1.2$）敏感性分析显示方法对枢轴值鲁棒，但缺乏不同骨干网络下的系统性对比。

## 关联研究分析

从问题动机看，CurioSFT与GKD（Agarwal et al., 2024）均关注分布匹配，但GKD解决RL阶段的暴露偏差，而CurioSFT解决SFT阶段的熵坍缩。GKD通过在线采样学生轨迹提供密集监督，计算成本高；CurioSFT通过自蒸馏在离线SFT阶段保留探索，计算开销较低。这一差异源于任务阶段不同：SFT是离线过程，无法实时判断熵增是否有效，故需依赖自生成教师；RL是在线过程，可通过奖励信号直接评估探索有效性。

从方法设计看，CurioSFT与Purified OPSD（2026）均涉及自蒸馏，但Purified OPSD解决自蒸馏导致的认知退化，通过特权信息对齐保护认知行为；CurioSFT解决熵坍缩，通过温度缩放保留探索空间。Purified OPSD依赖外部特权信息，而CurioSFT仅使用模型自身分布，避免了外部教师依赖。这一差异暗示：自蒸馏教师是否足以提供比外部强教师更优的探索引导，论文未给出回答。

## 总结

CurioSFT针对SFT-then-RL范式中SFT阶段熵坍缩导致RL探索受限的核心矛盾，抓住“token角色异质性”这一被忽略的点，通过自适应自蒸馏选择性保留推理token熵。该方法在SFT阶段提升ID/OOD性能2.5/2.9分，并在RL阶段AIME24上提升7.1分。其边界在于：仅在数学任务上验证，且自蒸馏教师的能力上限受限于模型自身，可能无法提供超越外部强教师的探索引导。当骨干模型规模扩大或任务复杂度增加时，自生成教师是否仍能维持有效的探索空间，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.02244)