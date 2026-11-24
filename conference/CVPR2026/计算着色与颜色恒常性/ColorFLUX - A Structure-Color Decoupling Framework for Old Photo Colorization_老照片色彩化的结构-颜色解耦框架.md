# CVPR2026最新论文 ｜ColorFLUX: A Structure-Color Decoupling Framework for Old Photo Colorization ｜老照片色彩化的结构-颜色解耦框架

研究机构：中国科学技术大学

作者：Bingchen Li、Zhixin Wang、Fan Li 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.28162)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.28162)

> 老照片色彩化面临退化与颜色推断耦合的难题，现有方法要么依赖文本提示导致细节丢失，要么直接生成导致色彩失真。ColorFLUX通过结构-颜色解耦训练与渐进式偏好优化，将结构保持与颜色生成分离，并引入视觉语义提示替代文本引导。该方法在真实老照片数据集上实现了优于商业模型的视觉质量，但其对FLUX骨干的依赖限制了轻量化部署，且评估指标的主观性仍需进一步验证。

## 研究背景

老照片色彩化需同时处理图像退化与颜色缺失，这要求模型在恢复结构的同时推断合理色彩。传统流水线先修复后上色，但褪色灰度图提供的色彩信息极少，导致模型难以区分语义边界，易产生颜色渗透。为了解决这一逆问题，扩散模型（Diffusion Models）成为主流，但其生成过程往往依赖文本提示，而文本无法捕捉图像中的细粒度空间细节，导致上色结果与物体语义不一致。

早期基于GAN的方法如DeOldify虽能生成色彩，但存在模式坍塌和细节模糊问题。DDColor利用Transformer提升质量，但在高频区域表现不佳。随着FLUX等预训练扩散模型的兴起，研究重心转向如何利用其强大的生成先验。然而，直接应用这些模型到老照片时，由于老照片特有的亮度褪色和色相改变与现代照片分布存在显著差异，导致训练差距。ColorFLUX的切入点在于将结构保持与颜色生成分离，并通过视觉语义提示直接提取图像细节，避免文本引导的局限。

## 核心方法

### 方法参照系

通用图像上色流程通常包含预处理、结构注入和颜色生成。本文问题与通用流程的关键差异在于输入为退化老照片，需额外处理褪色效应，且颜色推断需符合现代审美而非历史真实。

### 结构-颜色解耦训练

在结构一致性训练阶段，通常做法是使用ControlNet注入灰度结构。本文创新在于同时输入灰度图和由Redux提取的色彩视觉提示，使用流匹配损失训练，迫使模型学习结构而非颜色。

$$ \mathcal{L}_{FM} = \mathbb{E}_{t, x_0, \epsilon} [ \| v_\theta(x_t, t) - (\epsilon - x_0) \|^2 ] $$

该公式通过优化速度场预测，确保模型在结构阶段不学习颜色信息，从而解耦结构与颜色。

### 渐进式直接偏好优化

基础颜色学习后，模型需修正褪色效应。直接学习大增强空间会导致模型过拟合于明显色彩变化。本文提出渐进式DPO（Pro-DPO），从强增强到弱增强逐步训练。

$$ \mathcal{L}_{DPO} = -\mathbb{E}_{(c, x_w, x_l)} [ \log \sigma( \beta_t ( \log \frac{\pi_\theta(x_w|c)}{\pi_{ref}(x_w|c)} - \log \frac{\pi_\theta(x_l|c)}{\pi_{ref}(x_l|c)} ) ) ] $$

该公式通过比较正负样本的对数似然比，引导模型偏好更自然、鲜艳的色彩，同时避免过度饱和。

## 实验评估

实验在DIV2K-valid-synthesized、DIV2K-valid-augmented和RealOldPhotos三个数据集上进行，对比DeOldify、DDColor、CtrlColor、FLUX-Kontext和Doubao。基线覆盖了GAN、Transformer、扩散模型及商业模型，但缺失Pik-Fix等老照片专用方法。

| 方法 | DeQA | VQ-R1 | CRI | CRA | OA |
|---|---|---|---|---|---|
| DeOldify | 4.080 | 80.95 | 83.80 | 94.78 | 80.70 |
| DDColor | 4.162 | 79.80 | 78.55 | 77.60 | 81.73 |
| CtrlColor | 4.144 | 75.40 | 80.25 | 84.04 | 83.28 |
| FLUX-Kontext | 4.209 | 77.75 | 80.00 | 83.61 | 83.48 |
| ColorFLUX | 4.293 | 80.80 | 79.70 | 82.23 | 83.73 |

ColorFLUX在DeQA和VQ-R1上取得最高分，OA得分83.73，略高于FLUX-Kontext的83.48。在RealOldPhotos上，ColorFLUX的OA为83.20，显著优于Doubao的75.24。

消融实验显示，移除结构一致性训练（SCT）导致CCS下降，验证了解耦策略对结构保持的重要性。Pro-DPO相比单阶段DPO在CRA上提升0.35，表明渐进式训练有助于学习细微色彩偏好。

评估指标主要依赖Qwen2.5-VL-72B的主观评分，缺乏客观的色彩合理性指标。RealOldPhotos仅50张，统计显著性有限。代码未开源，但提供了详细超参数（8×80GB GPU，2天训练）。

## 关联研究分析

从问题动机看，ColorFLUX与CtrlColor均基于扩散模型，但CtrlColor依赖文本提示，而ColorFLUX使用视觉语义提示。这一差异源于老照片细节丰富但文本描述困难的任务特性，视觉提示能更直接地捕捉空间语义。从方法设计看，ColorFLUX与DiffColor同属扩散模型上色，但DiffColor针对通用图像，而ColorFLUX针对老照片退化。ColorFLUX引入Pro-DPO解决褪色问题，这是DiffColor未涉及的特定退化场景。

## 总结

ColorFLUX解决了老照片色彩化中退化与颜色推断耦合的核心矛盾，通过结构-颜色解耦和Pro-DPO实现了优于商业模型的视觉质量。其边界在于依赖FLUX骨干，限制了轻量化部署，且评估指标的主观性可能高估性能。当支持集增大到5-shot时，视觉语义提示的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.28162)