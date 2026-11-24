# ACL2026最新论文 ｜Stable Signer: Hierarchical Sign Language Generative Model ｜层级化手语生成模型

研究机构：美国罗格斯大学、新加坡南洋理工大学

作者：Sen Fang、Yalin Feng、Hongbin Zhong 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.04048)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.04048)

> 手语生成（Sign Language Production, SLP）旨在将自然语言文本转化为连贯、自然的手语视频，但传统多阶段流水线因中间表示误差累积导致生成质量停滞。现有方法在姿态回归中陷入“平均姿态”陷阱，且语义理解与视频渲染割裂，难以端到端优化。本文提出 Stable Signer，通过语义理解链接器（SLUL）与混合专家姿态生成模块（SLP-MoE）重构生成链路，实现从文本到视频的两级端到端映射。该方法在 How2Sign 数据集上显著提升了生成保真度，但其对规则先验数据库的依赖限制了跨语言泛化能力。

## 研究背景

手语生成面临的核心困境在于模态转换的离散性与连续性冲突。文本输入是离散的语义符号，而手语视频是连续的空间-时间运动序列。传统方法将这一过程拆解为文本到 Gloss（手语词素）、Gloss 到姿态序列、姿态到视频渲染三个独立阶段。这种级联结构导致每一阶段的预测误差都会传递至下一环节，最终在视频渲染阶段表现为动作僵硬或语义偏差。此外，由于同一 Gloss 对应多种合法的手势表达，模型在训练时若强制回归单一 Ground Truth（GT），会学习到所有可能姿态的均值，即“平均姿态”，导致生成动作缺乏表现力且模糊。

SLP 领域的研究长期受限于数据异构性与评估标准不统一。早期工作如 Progressive Transformers 和 Neural Sign Actors 虽引入了自回归或扩散模型，但仍未解决多 GT 下的优化目标冲突问题。Fast-SLP Transformers 等近期方法尝试加速生成，但依然依赖独立的姿态预测模块，未能将语义信息直接注入视频渲染过程。Stable Signer 的切入点在于识别出 SLP 任务中“规则可先验化”的特性：与手语识别不同，生成任务只需输出一种合法手势，因此可利用规则库约束姿态空间，将优化压力从姿态回归转移至语义理解与视频渲染的协同优化上。

## 核心方法

### 方法参照系

传统 SLP 流程遵循 Text2Gloss -> Gloss2Pose -> Pose2Vid 的三级架构，各模块独立训练。本文的关键差异在于将 Gloss2Pose 重构为基于规则先验的检索增强模块，并将语义特征直接耦合至 Pose2Vid 的扩散渲染过程，形成两级端到端训练框架。

### 语义理解链接器（SLUL）

SLUL 负责将复杂提示或文本统一转换为精确的 Gloss 序列，其设计动机在于解决传统翻译模型对长尾语义处理不足的问题。该模块采用 T5 编码器-解码器架构，引入语义感知 Gloss 掩码损失（SAGM Loss）以增强鲁棒性。SAGM Loss 通过随机掩码 Gloss 令牌，迫使模型在缺失表面线索时依赖编码器语义进行重建，其核心公式为：

$$ L_{SAGM} = -\sum_{t} \mathbb{1}[m_t=1] \log p_\theta(g_t | \tilde{g}, H) + \lambda_{KL} D_{KL}(p_\theta(\cdot|\tilde{g}, H) \| p_\theta(\cdot|g, H)) $$

该公式通过交叉熵项重建被掩码的 Gloss，并通过 KL 散度约束掩码与非掩码后验分布的一致性，防止解码器在表面线索消失时发生语义漂移。

### 混合专家姿态生成（SLP-MoE）

SLP-MoE 接收 SLUL 输出的语义特征 $H$，通过门控机制从规则先验数据库中检索并融合姿态序列，其设计动机在于规避多 GT 导致的平均姿态问题。门控权重 $w_k$ 由语义查询 $q = Pool(H)$ 生成，姿态序列 $\mathbf{p}_{pose}$ 为各专家检索结果的加权混合：

$$ \mathbf{p}_{pose} = \sum_{k=1}^{K} w_k \phi_k(g), \quad w_k = \text{softmax}(q \cdot \theta_k) $$

随后，混合姿态经过稳定性约束优化，惩罚 jerk（急动度）并保留手部关键点保真度，最终驱动 ControlNeXt/Wan 扩散模型渲染视频。这一机制将姿态生成从“回归学习”转变为“检索-平滑”过程，确保输出姿态既符合语义又具备解剖学合理性。

## 实验评估

实验在 How2Sign 数据集上进行，基线覆盖 Progressive Transformers、Neural Sign Actors、Fast-SLP Transformers 及 SignLLM。本文方法在 Pose Video 生成任务中，Test 集 BLEU-4 达到 15.67，显著高于 SignLLM 的 13.93；在最终视频生成任务中，Test 集 BLEU-4 达到 21.03，较 Fast-SLP Transformers 提升 63.7%。

| 方法 | Dev BLEU-4 | Test BLEU-4 | Dev ROUGE | Test ROUGE |
|---|---|---|---|---|
| SignLLM | 18.68 | 13.93 | 60.47 | 50.91 |
| Fast-SLP | 17.19 | 12.85 | 55.85 | 46.89 |
| Stable Signer | 23.24 | 15.67 | 70.68 | 59.56 |

消融实验表明，SLUL 的引入使 Dev 集 BLEU-3 从 21.98 提升至 34.23，验证了语义理解对姿态生成的关键作用。SLP-MoE 的加入进一步将 Dev 集 BLEU-4 提升至 25.55，ROUGE 达到 78.98，证明混合专家机制有效缓解了平均姿态问题。视频质量评估中，Stable Signer 的 FID 为 21.04，Hand Pose 误差为 17.68，均优于 SignDiff 的 25.22 和 20.04，表明语义-姿态协同优化提升了生成视频的视觉保真度与运动自然度。

评估边界方面，本文仅在 How2Sign（ASL）上验证，缺乏 PHOENIX-2014T（DGS）或 CSL-Daily（CSL）的跨语言对比，泛化能力存疑。指标上，BLEU 分数虽高，但无法完全反映手语的空间语法正确性。可复现性方面，论文提供了项目主页，但未公开规则先验数据库的构建细节，限制了第三方复现。

## 关联研究分析

从问题动机看，Stable Signer 与 SignLLM 均关注语义理解对生成的影响，但 SignLLM 依赖端到端的 LLM 解码器直接生成姿态，而本文采用“规则检索+扩散渲染”的解耦策略。这一差异源于任务特性：SignLLM 假设 LLM 具备空间推理能力，而本文认为姿态生成更适合由规则约束的确定性过程完成。SignLLM 在 How2Sign 上的 BLEU-4 为 13.93，低于本文的 15.67，暗示在 ASL 域内，显式规则先验可能比隐式 LLM 推理更有效地规避平均姿态陷阱。

从方法设计看，本文与 MaDiS 同属扩散模型生成路线，但 MaDiS 聚焦于掩码扩散策略以提升生成效率，而本文引入 MoE 机制解决姿态选择问题。MaDiS 在 CSL-Daily 上取得 4.80 BLEU-4，而本文在 How2Sign 上取得 15.67，两者数据集难度与评估协议不同，直接比较缺乏公平性。本文未对比 MaDiS 等最新 SLP 方法，可能低估了其在其他手语域的性能表现。

## 总结

Stable Signer 针对 SLP 中多 GT 导致的平均姿态问题，提出通过规则先验与 MoE 机制重构姿态生成流程，并结合 SAGM Loss 实现语义-姿态端到端优化。该方法在 How2Sign 上将 Test 集 BLEU-4 从 13.93 提升至 15.67，FID 降至 21.04，验证了层级化生成框架的有效性。然而，其性能高度依赖人工构建的规则先验数据库，且仅在 ASL 域内验证，跨语言泛化能力未知。当规则库覆盖的手势类型扩展至更复杂的语法结构时，检索-平滑机制是否仍能保持解剖学合理性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.04048)