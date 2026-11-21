# HuggingFace最新推荐论文 ｜TokenDial: Continuous Attribute Control in Text-to-Video via Spatiotemporal Token Offsets ｜连续属性标量控制

研究机构：Adobe研究院、美国卡内基梅隆大学

作者：Zhixuan Liu、Peter Schaldenbrand、Yijun Li 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.27520)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.27520)

> 文本到视频生成（T2V）当前面临的核心矛盾是：模型能生成高保真视频，但无法在不破坏身份与背景的前提下，对特定属性进行连续、单调的强度调节。现有方法要么依赖离散指令导致控制粒度粗糙，要么通过微调权重导致泛化能力下降且难以实现空间定位。本文切入点在于发现预训练扩散Transformer（DiT）的视觉补丁Token空间中存在语义属性方向，通过引入可学习的加性偏移向量实现“滑块式”控制。该方法以极低的参数开销实现了外观与运动动态的连续调节，但在复杂语义解耦与长视频时序一致性上仍存局限。

## 研究背景

T2V模型通常基于潜在扩散架构，其生成过程是在压缩的潜在空间中通过迭代去噪完成。理解本文需掌握两个关键概念：一是DiT架构中的视觉补丁Token，它将视频时空体素映射为固定维度的向量序列，保留了时空对应关系；二是流匹配（Flow Matching）范式，它通过预测向量场将高斯噪声转化为清晰视频，其采样路径比传统DDPM更直，使得在中间步骤注入控制信号成为可能。

当前T2V领域的控制研究主要聚焦于离散事件对齐或主体一致性，如CogVideoX解决多事件时序问题，Kaleido解决身份漂移。然而，这些方法无法处理“程度”问题：用户希望将火焰强度从30%调至70%，而非仅仅生成“有火”或“无火”。现有滑块方法如FreeSliders基于噪声更新近似，Text Slider基于文本编码器LoRA，前者缺乏空间定位能力，后者修改文本嵌入导致全局影响且难以解耦。本文针对这一空白，提出在视觉Token空间直接注入偏移，将隐式的语义关联转化为显式的强度控制接口。

## 核心方法

### 视觉Token偏移空间构建

本文方法置于“推理时轻量级控制”类别下，与LoRA微调的关键差异在于：LoRA修改权重矩阵，影响全局且难以局部化；本文在冻结的DiT中间层注入加性偏移向量，仅改变Token值而不改变注意力结构。设视觉补丁Token序列为 $T \in \mathbb{R}^{L \times d}$，引入偏移空间 $V_{+} := \mathbb{R}^d$，定义偏移向量 $\Delta \in \mathbb{R}^d$。通过软掩码 $s \in [0,1]^L$ 控制作用区域，更新后的Token序列为 $T' = T + s \odot \Delta$。这一设计使得控制具有显式的时空定位能力，且参数量仅为rank-64 LoRA的0.256%。

### 语义对齐与自监督训练

设计动机在于解决外部监督信号在高噪声下的不稳定性。本文采用多步后验细化（Multi-step posterior refinement），从初始预测 $t$ 步开始，额外运行 $K=4$ 步去噪得到细化估计 $\hat{x}_0^{ref}$，再计算损失。对于外观控制，利用InternVideo2编码器 $E(\cdot)$ 计算预测方向与目标方向 $\mathbf{d}_{tgt}$ 的余弦距离：

$$ \mathcal{L}_{app} = 1 - \frac{E(\hat{x}_0^{ref}(\Delta)) \cdot \mathbf{d}_{tgt}}{\|E(\hat{x}_0^{ref}(\Delta))\| \|\mathbf{d}_{tgt}\|} + \lambda_a \text{LPIPS}(\hat{x}_0^{ref}(\Delta), \hat{x}_0^{ref}(\emptyset)) $$

该公式强制偏移方向与语义目标对齐，同时通过LPIPS正则化保留背景。对于运动控制，利用DINOv2特征计算光流幅度，通过缩放因子 $\gamma$ 实现运动强度调节，避免帧间对应不一致导致的梯度噪声。

### 推理时的组合式流引导

设计动机在于直接缩放偏移向量 $\Delta$ 在大强度下会扭曲生成轨迹。本文在向量场层面进行组合，定义更新量 $\tilde{u}$ 为：

$$ \tilde{u} = s_{txt} \Phi_\theta(x_t, t, c) + s_{edit} (\Phi_\theta(x_t, t, c, \Delta) - \Phi_\theta(x_t, t, c)) $$

第一项为文本引导的基础轨迹，第二项隔离了由偏移 $\Delta$ 诱导的微分速度。通过调节 $s_{edit}$ 实现连续滑块效果，既保证了文本一致性，又实现了属性的线性强度控制。

## 实验评估

实验在自建TokenDial数据集上进行，涵盖12个概念、5个属性，共生成约4,500个视频。基线覆盖FreeSliders、Text Slider、Concept Sliders及V2V编辑方法，但未对比知识库中提到的Kaleido或Aura等主体一致性SOTA，因任务侧重不同。

| 方法 | VLM Edit Qual. | VLM ID Pre. | VLM Overall | PickScore |
| :--- | :--- | :--- | :--- | :--- |
| Text Slider | 4.368 | 3.936 | 4.202 | 24.936 |
| FreeSliders | 4.202 | 3.932 | 4.153 | 24.813 |
| **TokenDial** | **4.587** | **4.988** | **4.587** | 24.942 |

TokenDial在VLM评估的编辑质量与身份保持上均显著优于基线，Overall得分4.587高于Text Slider的4.202。在可控性指标上，TokenDial的单调性（Mono.）达到0.573，远高于Text Slider的0.451，表明其滑块调节更符合线性预期。

| 方法 | Range (CR) | Mono. | Smooth (CSM) | LPIPS (SP) |
| :--- | :--- | :--- | :--- | :--- |
| Text Slider | 0.451 | 0.550 | 0.742 | 0.567 |
| **TokenDial** | **0.460** | **0.573** | 0.386 | **0.249** |

消融实验显示，引入注意力掩码后，LPIPS从0.298降至0.249，证明掩码有效抑制了背景漂移。移除后验细化会导致高噪声下编辑失效，验证了该设计的必要性。

评估边界方面，本文未使用VBench或T2V-CompBench等通用基准，无法与领域SOTA直接比较。自建数据集规模较小，且未报告置信区间。代码已开源，但依赖InternVideo2和DINOv2等外部模型，部署复杂度高于纯扩散模型。

## 关联研究分析

从方法设计看，TokenDial与Text Slider的核心差异在于控制空间的选择。Text Slider在文本编码器中学习LoRA方向，本质是修改条件输入，导致编辑效果全局化且难以实现空间定位；TokenDial在视觉Token空间注入偏移，保留了DiT内部的时空结构，使得通过注意力掩码实现局部编辑成为可能。这一差异源于任务特性：连续属性控制需要精确的时空定位，而文本嵌入缺乏这种显式结构。

从问题动机看，TokenDial与FreeSliders均追求免训练控制，但FreeSliders基于噪声更新的近似，缺乏语义监督，导致编辑方向不稳定；TokenDial引入外部VLM监督，虽增加了计算开销，但显著提升了语义对齐精度。然而，TokenDial依赖外部理解模型，若理解模型存在偏见（如“older”与“weight”耦合），编辑会继承这些偏差。论文通过去偏策略缓解，但未彻底解决，这提示了端到端语义解耦的必要性。

## 总结

TokenDial解决了T2V生成中连续属性强度不可控的矛盾，其切入点在于利用DiT视觉Token空间的线性语义特性，通过加性偏移实现低开销、可定位的滑块控制。实验证明其在编辑质量（4.587）和单调性（0.573）上优于现有滑块方法。然而，方法依赖外部VLM监督，且仅在短视频（32-64帧）上验证，长视频时序一致性未测试。当视频长度超过1分钟时，Token偏移的累积误差是否会导致属性漂移，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.27520)