# ACL2026最新论文 ｜Learning What Matters: Dynamic Dimension Selection and Aggregation for Interpretable Vision-Language Reward Modeling ｜视觉-语言多维奖励模型

研究机构：浙江大学、南京大学

作者：Qiyuan Chen、Hongsen Huang、Jiahe Chen 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.05445)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05445)

> 视觉-语言奖励模型（Reward Model, RM）面临生成式与判别式范式的效率-可解释性权衡：前者提供文本批评但推理延迟高，后者输出标量但无法区分感知与推理错误。VL-MDR通过指令感知的维度动态选择与掩码聚合，在单次前向传播中解耦评估标准与响应评分。该框架在7B规模下实现了超越判别式基线的性能，但其维度分类法的静态性与冻结视觉塔的设计限制了细粒度感知的动态适应能力。

## 研究背景

当VLM生成“图中有3只猫”而实际只有2只时，传统判别式RM仅输出一个低分标量，无法指示错误源于计数失误还是对象识别失败。这种“黑盒”反馈阻碍了针对性优化，而生成式RM虽能输出“计数错误”的文本批评，但自回归解码导致推理延迟增加3倍以上。这一矛盾在基于可验证奖励的强化学习（Reinforcement Learning with Verifiable Rewards, RLVR）普及后加剧：RLVR依赖确定性奖励信号，但单一标量无法提供过程级监督，导致模型在提升逻辑推理的同时出现感知能力遗忘。

现有RM研究分为两条路线：生成式RM（如LLaVA-Critic）通过文本批评提供可解释性，但受限于位置偏差与高延迟；判别式RM（如Skywork-VL）将偏好学习建模为标量回归，高效但无法解耦多维质量。两者均无法区分“感知盲点”与“推理偏差”，导致反馈信号无法指导模型迭代。VL-MDR的切入点在于：评估标准应由指令决定，而非响应内容，通过Query-Response解耦架构实现维度选择与评分的分离。

## 核心方法

### 方法参照系

判别式RM的标准流程是：VLM骨干提取响应表示，线性头输出单一标量奖励。本文的关键差异在于引入指令感知的维度预测头，将标量输出扩展为多维向量，并通过掩码机制动态选择评估维度。

### Query-Response解耦架构

该架构解决了传统RM中评估标准与响应内容耦合的问题。VL-MDR从骨干最后隐藏状态提取两个表示：指令表示 $h_{[q]}$（查询最后token）与响应表示 $h_{[r]}$（响应最后token）。因果自注意力机制确保 $h_{[q]}$ 仅编码指令意图，$h_{[r]}$ 编码完整上下文。三个并行头分别处理维度预测、评分与加权，实现评估标准与响应质量的解耦。

### 动态维度选择与掩码聚合

维度预测头 $\phi$ 将 $h_{[q]}$ 映射为相关性logits $\mathbf{l} \in \mathbb{R}^K$，通过Top-$k$掩码 $\mathbf{m} \in \{0,1\}^K$ 选择激活维度。评分头 $\psi$ 将 $h_{[r]}$ 映射为维度分数 $\mathbf{s} \in \mathbb{R}^K$。加权头 $\omega$ 预测重要性logits $\mathbf{u} = \omega(h_{[q]})$，通过掩码归一化计算最终权重：

$$
\alpha_k = \frac{m_k \cdot \exp(u_k)}{\sum_{j=1}^{K} [m_j \cdot \exp(u_j)]}
$$

该公式确保无关维度（$m_k=0$）被严格排除，最终奖励 $R(x,y) = \sum_{k=1}^{K} \alpha_k s_k$ 仅由激活维度贡献。这一设计解决了固定维度聚合中无关维度噪声掩盖真实错误的问题，使模型能针对特定指令（如“计数”vs“推理”）动态调整评估重点。

## 实验评估

实验基于Qwen2.5-VL-7B-Instruct骨干，冻结视觉塔与投影器，微调LLM与奖励头。基线覆盖生成式（LLaVA-Critic, UnifiedReward-Think）与判别式（Skywork-VL, IXC-2.5）RM，缺失基于CoT的推理型RM基线。

| 模型 | 参数量 | General | Hallucination | Reasoning | Overall Acc | Macro Acc |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| UnifiedReward-Think | 7B | 77.35 | 72.50 | 65.62 | 71.45 | 71.82 |
| Skywork-VL | 7B | 65.75 | 79.84 | 60.88 | 72.98 | 68.82 |
| VL-MDR | 7B | 71.27 | 75.17 | 69.09 | 73.06 | 71.84 |

VL-MDR在Overall Acc上以73.06%超越UnifiedReward-Think的71.45%，在Reasoning维度（69.09% vs 65.62%）显著领先，但Hallucination维度（75.17% vs 79.84%）低于Skywork-VL。

| 方法 | Gran. | L_rank | Gate | Overall | Macro |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Scalar | 1 | − | − | 64.55 | 60.87 |
| Coarse-7D | 7 | ✓ | ✓ | 67.12 | 64.20 |
| Fine w/o Gate | 21 | ✓ | − | 69.77 | 68.51 |
| VL-MDR | 21 | ✓ | ✓ | 70.81 | 69.96 |

消融显示21维细粒度监督比7维粗粒度提升2.65个百分点Overall Acc，但Top-$k$扫描表明$k=3$时性能峰值，$k>5$后性能下降，验证了维度选择而非维度数量的关键作用。

评估协议限于静态图像问答，未测试动态视频或时序推理场景。代码未公开，超参数（$k=3$, $\xi=0.3$）固定，缺乏跨骨干网络的泛化性验证。

## 关联研究分析

从问题动机看，VL-MDR与TRACE在“解耦感知与推理”目标上一致，但TRACE通过子问题分解暴露推理链中的静默失败，而VL-MDR在奖励信号层面实现解耦。TRACE的诊断粒度是步骤级，VL-MDR是维度级，前者适用于推理链质量评估，后者适用于偏好对齐。这一差异源于任务特性：TRACE面向推理忠实性评估，VL-MDR面向偏好学习，维度解耦比步骤分解更适合标量奖励场景。

从方法设计看，VL-MDR与Vision-SR1同属感知推理协同优化路线，但Vision-SR1通过多维奖励自训练直接优化VLM，VL-MDR作为独立RM提供外部监督。Vision-SR1的奖励信号内嵌于训练循环，VL-MDR的维度选择机制可独立于VLM架构。这一设计使VL-MDR能适配不同骨干网络，但冻结视觉塔导致细粒度感知维度（如Object Counting）的评分能力受限，与Vision-SR1的全参数微调形成对比。

## 总结

VL-MDR解决的核心矛盾是判别式RM的效率与生成式RM的可解释性无法兼得。其切入点在于Query-Response解耦：评估标准由指令决定，响应评分独立进行，通过动态维度选择实现细粒度反馈。该框架在7B规模下以73.06%的Overall Acc超越UnifiedReward-Think，验证了多维解耦的有效性。但21维分类法的静态性与冻结视觉塔的设计限制了模型对新型感知任务的适应能力。当指令涉及未在训练集中出现的细粒度感知维度时，维度预测头的泛化性能是否衰减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05445)