# ACL2026最新论文 ｜Latent Attention Denoising: A Training-Free Energy-Based Framework for Mitigating Hallucinations in Vision-Language Models ｜潜在注意力去噪（LAD）：基于能量模型的无训练幻觉缓解框架

作者：Zhiwen Luo、Siyu Jiang、Weilong Jiang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9ad91f60b69f)

> 大视觉语言模型（LVLMs）在生成描述时，常因解码器内部注意力分布失衡而忽略视觉证据，产生对象幻觉。现有推理时干预方法多依赖启发式权重调整，缺乏对注意力偏差成因的统计解释，导致校正精度受限且泛化性不足。本文指出Softmax注意力隐含的独立同分布（i.i.d.）Gumbel噪声假设在LVLMs中被违背，提出潜在注意力去噪（Latent Attention Denoising, LAD），将注意力校准重构为单步基于分数的去噪过程，通过能量函数梯度引导Logits恢复视觉接地。该框架在无需重训的前提下实现了低开销的幻觉抑制，但其效果高度依赖特定架构的超参数校准，且在长序列生成中的稳定性尚未得到充分验证。

## 研究背景

当LVLMs处理图像输入时，视觉Token与文本Token在解码器中竞争注意力资源。若模型过度依赖预训练习得的文本共现统计规律，而非当前图像的视觉特征，便会生成图像中不存在的物体，即对象幻觉。这一现象的根源并非视觉编码器特征提取能力不足，而是解码阶段注意力机制的统计特性失效。标准Softmax函数作为概率归一化算子，其理论最优性建立在Logits扰动服从i.i.d. Gumbel分布的假设之上，该假设保证了无关替代项独立性（Independence of Irrelevant Alternatives, IIA），即两个Token的相对偏好仅取决于其自身Logits差值。

然而，实证分析表明LVLMs中的注意力模式呈现结构化、非i.i.d.的噪声特征，特别是“注意力汇聚”（Attention Sinks）现象——特定Token（如[BOS]或特殊视觉块）不成比例地吸收注意力概率质量，形成零和竞争，系统性压制视觉证据。这种统计误设（Statistical Misspecification）使得Softmax在多模态接地任务中变得不可靠，驱动模型滑向语言先验主导的幻觉生成。现有缓解策略如视觉对比解码（Visual Contrastive Decoding, VCD）或过度信任惩罚（OPERA）虽能部分抑制幻觉，但多基于启发式规则调整Logits或注意力权重，缺乏对偏差成因的机制解释，难以在保持生成流畅性的同时精准校正视觉接地。本文切入点在于从统计物理视角诊断Softmax的失效根源，并引入能量模型（Energy-Based Model, EBM）框架，将注意力校准转化为可解析的去噪过程，从而提供具有理论支撑的无训练干预方案。

## 核心方法

### 方法参照系

本文问题归属于推理时注意力调控范畴，与OPERA等直接重加权方法同属解码阶段干预。关键差异在于，本文不直接修改注意力权重或Logits的线性组合，而是将注意力状态视为受结构化噪声污染的潜变量，通过能量最小化原理推导校正方向，将启发式调整转化为统计推断问题。

### 统计误设诊断与能量景观重塑

传统Softmax校准假设Logits噪声为i.i.d. Gumbel分布，但LVLMs中Sink Token与视觉Token间存在强负相关，且残差分布显著偏离Gumbel形态，证实了统计误设的存在。为校正此偏差，LAD定义能量函数 $E_c(A) = p^\top A - \lambda \mathbf{1}_I^\top A$，其中 $p$ 为动态估计的Sink先验向量，$\mathbf{1}_I$ 为视觉Token指示向量。该公式的物理含义是：对Sink Token施加高能量惩罚（$p^\top A$），同时对视觉Token施加负能量激励（$-\lambda \mathbf{1}_I^\top A$），从而在能量景观中构建一个吸引视觉证据、排斥幻觉状态的势能场。这一设计解决了此前方法仅凭经验规则调整权重、无法量化“幻觉状态”与“接地状态”能量差异的问题，使校正方向具有明确的统计解释。

### 单步Langevin更新与双模式门控

基于能量函数，LAD推导出一阶Langevin更新规则 $\tilde{s} = s - \eta \nabla_A E_c(A) + \sigma \epsilon$，其中 $\eta$ 为步长，$\sigma$ 为噪声尺度，$\epsilon$ 为高斯噪声。该公式意味着：通过计算能量函数对注意力Logits的梯度，将当前状态从高能幻觉区域向低能视觉接地盆地移动，同时引入随机扰动以增强鲁棒性。为平衡上下文理解与幻觉抑制，LAD引入双模式门控机制：在Prefill阶段（理解模式），采用门控确定性更新 $\tilde{s} = s_{ctx} - g(\alpha_{visual}) \cdot \eta \cdot \nabla_A E_c(A)$，其中门控函数 $g(\alpha_{visual}) = \sigma(\frac{\alpha_{visual} - \beta}{T})$ 仅在模型表现出内在视觉对齐时激活校正；在Decode阶段（生成模式），应用完整随机更新以应对幻觉风险峰值。这一设计解决了全局校正可能破坏语言逻辑的问题，通过动态门控确保干预仅在视觉证据不足时介入，避免了过度校正导致的生成退化。

## 实验评估

实验在LLaVA-1.5、Shikra、MiniGPT-4和InstructBLIP四个架构上进行，评估基准包括CHAIR（图像描述幻觉）、POPE（对象存在性探测）和AMBER（多维幻觉评估）。基线覆盖VCD、OPERA、ICD、SID、PAI等主流推理时干预方法，但未包含2026年最新的表征编辑方法如HulluEdit或RUDDER，可能低估了与最新SOTA的差距。

| 方法 | LLaVA-1.5 CHAIRs | LLaVA-1.5 POPE Avg Acc | InstructBLIP CHAIRs | InstructBLIP POPE Avg Acc |
| :--- | :--- | :--- | :--- | :--- |
| Greedy | 43.0 | 84.83 | 45.4 | 84.05 |
| VCD | 44.8 | 83.69 | 42.4 | 84.21 |
| OPERA | 41.4 | 85.55 | 46.0 | 84.83 |
| PAI | 28.2 | 84.91 | 44.2 | 83.69 |
| LAD | 19.6 | 85.39 | 37.0 | 84.71 |

LAD在CHAIRs指标上显著优于所有基线，LLaVA-1.5上从43.0降至19.6，InstructBLIP上从45.4降至37.0，表明能量引导的注意力校准在自由形式描述中有效抑制幻觉。POPE准确率方面，LAD在LLaVA-1.5上达到85.39%，略低于OPERA的85.55%，但在InstructBLIP上达到84.71%，高于VCD的84.21%，显示其在对象存在性判断上的稳健性。值得注意的是，LAD在LLaVA-1.5上的生成长度（Len 88.5）短于Greedy（94.5），需警惕CHAIRs改善是否部分源于生成内容减少而非幻觉抑制。

消融实验显示，移除Sink Penalty项使CHAIRs升至35.8，移除Visual Incentive项升至29.6，移除自适应门控升至26.6，证实三项组件均必要。超参数敏感性分析表明，$\eta=2.1, \sigma=0.1$ 位于性能“盆地”中心，$\sigma$ 作为正则化器扩大了最优 $\eta$ 范围，增强了鲁棒性。

评估边界方面，论文未报告置信区间，且仅在静态图像上验证，未涉及视频或长序列生成场景。超参数需针对每个架构手动校准（如MiniGPT-4用 $\eta=0.6$，InstructBLIP用 $\eta=0.9$），限制了即插即用性。代码未开源，可复现性依赖论文提供的超参数配置。

## 关联研究分析

从问题动机看，LAD与OPERA均针对注意力失衡，但OPERA基于“过度信任”假设直接惩罚高注意力Token，而LAD将失衡归因于Softmax统计误设，通过能量函数量化“幻觉状态”与“接地状态”的差异。这一差异源于对幻觉机制的不同理解：OPERA视幻觉为注意力分配错误，LAD视其为概率估计失效。LAD的理论框架使其校正方向具有可解释性，但动态Sink先验 $p$ 的估计依赖跨头聚合Logits，可能在语义复杂场景中引入噪声，论文未深入探讨 $p$ 的估计误差对校正精度的影响。

从方法设计看，LAD与VCD同属解码策略优化，但VCD通过对比原始与扰动输入的Logits分布实现校正，需额外前向传播，计算开销大（TPS 10.38 vs LAD 27.99）。LAD利用Transformer残差流特性，在单步内完成校正，避免了VCD的计算冗余。然而，LAD的随机更新 $\sigma \epsilon$ 在Decode阶段引入噪声，可能在长序列生成中累积误差，而VCD的确定性对比机制在此方面更稳定。LAD的双模式门控虽解决了Prefill阶段的过度校正问题，但门控函数 $g(\alpha_{visual})$ 的阈值 $\beta$ 和温度 $T$ 需手动调整，缺乏自适应机制，这在多模态对齐模块（如Q-Former）复杂的架构中可能失效，论文未提供相关实验验证。

## 总结

LAD旨在解决LVLMs中因Softmax统计误设导致的注意力竞争失衡问题，现有启发式方法缺乏对偏差成因的机制解释，而LAD通过能量模型将注意力校准重构为单步去噪过程，提供了具有统计物理基础的校正框架。实验表明，LAD在LLaVA-1.5上将CHAIRs从43.0降至19.6，在InstructBLIP上从45.4降至37.0，显著优于VCD和OPERA等基线，同时保持与Greedy解码相当的推理速度。然而，其效果高度依赖架构特定的超参数校准，且仅在静态图像上验证，未探讨长序列生成中随机噪声的累积效应。当生成序列长度超过500 Token时，Langevin更新的随机性是否会导致视觉接地漂移，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_9ad91f60b69f)