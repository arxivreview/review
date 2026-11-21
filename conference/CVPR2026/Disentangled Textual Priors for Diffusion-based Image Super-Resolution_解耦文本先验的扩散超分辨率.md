# CVPR2026最新论文 ｜Disentangled Textual Priors for Diffusion-based Image Super-Resolution ｜解耦文本先验的扩散超分辨率

研究机构：南京大学

作者：Lei Jiang、Xin Liu、Xinze Tong 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.07430)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.07430)

> 图像超分辨率（SR）的核心困境在于扩散模型虽能生成逼真纹理，但单一文本提示往往将全局布局与局部细节、低频结构与高频纹理混杂在同一嵌入中，导致语义可控性不足与幻觉频发。现有方法如SeeSR或FaithDiff仅使用扁平化标签或全局句子，无法区分不同频率尺度的恢复需求。DTPSR通过构建DisText-SR数据集，将文本先验沿空间层级（全局/局部）和频率语义（低频/高频）双维度解耦，并设计专用交叉注意力模块实现渐进式注入。该框架在感知质量指标上达到SOTA水平，但其对上游分割与生成模型的依赖及50步推理效率仍是显著局限。

## 研究背景

扩散模型在潜空间执行去噪过程时，其生成质量高度依赖于条件信号的结构化程度。Classifier-Free Guidance (CFG) 通过正负提示的差值放大语义特征，但传统单一提示无法区分场景整体布局与物体表面纹理，导致模型在严重退化下产生语义漂移。这种“先验纠缠”使得模型难以在恢复全局结构的同时精准填充高频细节，构成了保真度与真实感权衡中的关键瓶颈。

主流文本引导SR方法如FaithDiff和SUPIR采用全局句子描述，SeeSR使用局部标签，二者均缺乏频率维度的区分。这种设计忽略了视觉内容的多尺度本质：低频信息主导形状与色彩分布，高频信息决定边缘与纹理清晰度。当退化严重时，单一嵌入无法提供足够细粒度的语义约束，导致模型倾向于生成与输入不符的幻觉内容。DTPSR的切入点在于将文本先验显式解耦为全局、低频局部、高频局部三路，通过独立的注意力路径分别注入，从而实现对不同频率成分的可控恢复。

## 核心方法

### 方法参照系

标准扩散SR流程基于预训练T2I模型（如Stable Diffusion），通过ControlNet或SFT层注入低分辨率（LR）特征，并依赖单一文本提示进行全局引导。本文的关键差异在于将单一文本条件拆解为具有频率语义的结构化先验，并引入多分支交叉注意力机制替代传统的单一文本嵌入注入方式。

### 频率解耦文本先验注入

传统方法将全局与局部语义混在同一文本嵌入中，导致模型无法区分结构恢复与纹理生成的优先级。DTPSR引入Global Text Cross-Attention (GTCA)、Low-Frequency Cross-Attention (LFCA) 和 High-Frequency Cross-Attention (HFCA) 三个模块，分别处理全局布局、低频结构（形状、色彩）和高频细节（纹理、边缘）。文本先验通过CLIP编码器嵌入后，按顺序注入潜变量 $z_t$，形成从粗到细的渐进式恢复过程。

$$
z_t^{[g]} = \text{GTCA}(z_t, \mathbf{e}_g), \quad z_t^{[lf]} = \text{LFCA}(z_t^{[g]}, \mathbf{E}_{lf}), \quad z_t^{[hf]} = \text{HFCA}(z_t^{[lf]}, \mathbf{E}_{hf})
$$

该公式表明，潜变量依次经过全局、低频、高频三个注意力模块的调制，每一步都基于前一步的输出进行细化，确保语义引导与扩散去噪轨迹对齐。这种设计解决了单一嵌入在严重退化下无法区分结构错误与纹理缺失的问题，提升了恢复的语义一致性。

### 多分支Classifier-Free Guidance

标准CFG使用单一负提示，无法针对不同类型的语义错误进行独立抑制。DTPSR扩展为多分支CFG，为全局、低频、高频分支分别设置负提示 $c_{neg}^g, c_{neg}^{lf}, c_{neg}^{hf}$，以抑制对应尺度的幻觉。最终噪声预测由三个分支的引导项加权求和：

$$
\hat{\epsilon}_\theta = \epsilon_\theta(z_t, t, \emptyset) + \lambda_s \left( \epsilon_\theta(z_t, t, c_g, c_{lf}, c_{hf}) - \epsilon_\theta(z_t, t, c_{neg}^g, c_{neg}^{lf}, c_{neg}^{hf}) \right)
$$

其中 $\lambda_s$ 控制引导强度。该设计允许模型在不同频率尺度上独立调节生成强度，避免全局负提示对局部细节的过度抑制，从而在保持结构稳定的同时增强纹理真实感。

## 实验评估

实验在DIV2K-Val、RealSR和DRealSR三个基准上进行，对比方法覆盖Real-ESRGAN、StableSR、DiffBIR、SeeSR、SUPIR、FaithDiff等主流路线，但缺失2026年最新单步方法（如OFTSR、FlowMapSR）及频域专用方法（如HDW-SR）。

| 数据集 | 方法 | PSNR (dB) | MUSIQ | MANIQA | CLIP-IQA |
| :--- | :--- | :--- | :--- | :--- | :--- |
| RealSR | DTPSR | 22.46 | 71.84 | 0.6021 | 0.7278 |
| RealSR | SUPIR | 25.23 | 68.86 | 0.4644 | 0.6126 |
| RealSR | FaithDiff | 25.04 | 68.99 | 0.4429 | 0.6357 |
| DRealSR | DTPSR | 25.83 | 69.24 | 0.6011 | 0.7640 |
| DRealSR | SUPIR | 27.20 | 66.30 | 0.4526 | 0.6335 |
| DRealSR | FaithDiff | 26.93 | 65.09 | 0.4144 | 0.6307 |

DTPSR在MUSIQ和MANIQA上显著优于SUPIR和FaithDiff，表明其在感知质量上具有优势；但PSNR低于SUPIR约2.8 dB，反映其侧重纹理真实感而非像素保真度。

| 消融实验 | 配置 | MANIQA | CLIP-IQA | MUSIQ |
| :--- | :--- | :--- | :--- | :--- |
| 3-4 | Global + Local | 0.6011 | 0.7640 | 69.24 |
| 3-2 | Local Only | 0.5851 | 0.7471 | 68.86 |
| 4-3 | LF + HF | 0.6011 | 0.7640 | 69.24 |
| 4-1 | LF Only | 0.5850 | 0.7544 | 68.96 |
| 5-2 | Disentangled | 0.6011 | 0.7640 | 69.24 |
| 5-1 | Mixed | 0.5947 | 0.7527 | 69.05 |

消融显示，解耦策略（Exp 5-2）比混合策略（Exp 5-1）在MUSIQ上高0.19，验证了频率分离的有效性；全局与局部先验结合（Exp 3-4）比仅用局部先验（Exp 3-2）在CLIP-IQA上高0.0169，表明全局结构对语义一致性有贡献。

评估协议采用标准指标，但未报告置信区间，且推理时间为14.94秒（50步），远高于单步方法（如Realism Control One-step Diffusion的0.09秒）。代码已开源，但上游依赖Mask2Former和LLaVA，其误差可能累积影响最终结果。

## 关联研究分析

从问题动机看，DTPSR与SeeSR均关注文本引导的SR，但SeeSR使用局部标签，缺乏频率区分，导致在严重退化下易产生幻觉。DTPSR通过频率解耦，将结构恢复与纹理生成分离，解决了SeeSR在高频细节恢复上的不足。这一差异源于任务特性：视觉内容的多尺度本质要求不同频率成分需独立处理，而SeeSR的扁平化设计忽略了这一点。

从方法设计看，DTPSR与FaithDiff均使用全局文本引导，但FaithDiff未区分频率，导致全局提示对局部细节的约束不足。DTPSR引入LFCA和HFCA，分别针对低频和高频成分进行独立引导，提升了可控性。然而，DTPSR依赖上游分割模型生成区域级文本，若分割错误，文本先验将失效，而FaithDiff的全局提示对局部错误更鲁棒。这种依赖关系是DTPSR的潜在盲区，论文未给出量化分析。

## 总结

DTPSR旨在解决扩散SR中文本先验纠缠导致的语义可控性不足问题。其切入点在于将文本先验沿空间层级和频率语义双维度解耦，通过专用交叉注意力模块实现渐进式注入，并引入多分支CFG抑制幻觉。实验显示，DTPSR在RealSR上MUSIQ达71.84，MANIQA达0.6021，显著优于SUPIR和FaithDiff，但PSNR为22.46，低于SUPIR的25.23。其边界在于依赖上游分割与生成模型，且50步推理效率较低。当上游分割模型在复杂场景下出现区域错误时，解耦文本先验的鲁棒性是否仍能保持，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.07430)