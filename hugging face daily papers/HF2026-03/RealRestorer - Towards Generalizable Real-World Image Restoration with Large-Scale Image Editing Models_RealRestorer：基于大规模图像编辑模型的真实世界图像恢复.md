# HuggingFace最新推荐论文 ｜RealRestorer: Towards Generalizable Real-World Image Restoration with Large-Scale Image Editing Models ｜RealRestorer：基于大规模图像编辑模型的真实世界图像恢复

研究机构：南方科技大学、中国科学院

作者：Yufeng Yang、Xianfang Zeng、Zhangqi Jiang 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.25502)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.25502)

> 全合一图像恢复（All-in-One Image Restoration, AiOIR）旨在通过单一模型处理多种退化，但现有方法多依赖合成数据，导致在真实世界复杂退化下泛化能力不足。本文切入点在于利用大规模开源图像编辑模型（Step1X-Edit）的强生成先验，通过两阶段渐进混合训练策略适配真实退化分布。具体做法是构建包含Web风格退化与真实采集数据的高保真配对数据集，微调DiT骨干网络，并引入无参考基准RealIR-Bench进行评估。该工作验证了生成式先验在真实域的有效性，但其在保真度指标上显著落后于专用回归模型，且推理成本高昂，限制了实时部署。

## 研究背景

真实世界图像常受模糊、雨雾、噪声等多种退化叠加影响，且退化类型未知。传统AiOIR模型如AirNet或PromptIR虽能处理多任务，但训练数据多为合成退化，导致模型在真实场景中出现域差距（Domain Gap），表现为细节丢失或伪影生成。为解决此问题，领域共识认为需引入退化感知机制或生成式先验，但现有生成式方法（如LucidFlux）多聚焦于感知质量提升，缺乏对真实世界复杂退化分布的系统性适配。

主流路线在参数冲突与域差距之间做出取舍：MoE架构（如MiM-DiT）通过动态路由缓解参数冲突，但依赖预训练骨干且对未知退化适应性有限；扩散模型（如PixRestore）提升感知质量，但计算成本高且可能引入幻觉。本文抓住“开源闭源性能鸿沟”与“真实域数据稀缺”两个被忽略的点，提出利用开源图像编辑模型作为基座，通过数据工程缩小合成-真实分布偏移，而非单纯优化架构。

## 核心方法

### 方法参照系

本文问题属于“扩散与流匹配生成”路线，但与传统从头训练或轻量微调不同，其核心差异在于利用预训练图像编辑模型的语义先验，通过两阶段训练实现从编辑到恢复的知识迁移，而非直接优化恢复损失。

### 两阶段渐进混合训练

设计动机：单阶段训练易过拟合合成数据或真实数据，导致泛化能力不足。本文在Transfer Training阶段使用约1M合成配对数据，以1e-5学习率、1024×1024分辨率训练，使模型习得基础恢复能力。随后在Supervised Fine-tuning阶段引入约100K真实世界退化数据，采用余弦退火学习率，并保留少量合成数据以防止过拟合。该策略通过渐进式数据混合，平衡了生成能力与真实域适配，最终FS分数较单阶段训练提升0.004。

$$
\mathcal{L}_{total} = \mathcal{L}_{diffusion} + \lambda \mathcal{L}_{consistency}
$$

其中$\mathcal{L}_{diffusion}$为扩散去噪损失，$\mathcal{L}_{consistency}$为内容一致性约束，$\lambda$为平衡系数。该公式确保模型在去除退化的同时保持原始场景结构。

### 无参考评估框架

设计动机：真实场景缺乏配对Clean图，传统PSNR/SSIM不适用。本文提出RealIR-Bench，包含464张真实退化图像，采用VLM（Qwen3-VL-8B-Instruct）评估退化严重程度，定义恢复分数（RS）为恢复前后退化分数的差值，并结合LPIPS计算感知相似度分数（LPS）。最终分数（FS）定义为：

$$
FS = \alpha \cdot RS + (1-\alpha) \cdot LPS
$$

其中$\alpha$为归一化权重。该框架通过VLM语义理解与感知度量结合，量化了退化去除能力与内容保持能力的权衡，解决了无参考评估的难题。

## 实验评估

实验在RealIR-Bench与FoundIR上进行，基线覆盖Nano Banana Pro、GPT-Image-1.5等闭源SOTA及Qwen-Image-Edit-2511等开源模型，但缺失传统AiOIR专用模型（如AirNet、PromptIR）的直接对比。

| 方法 | 开源 | Rain Removal (LPS↓/RS↑/FS↑) | Deblurring (LPS↓/RS↑/FS↑) | Avg Total (LPS↓/RS↑/FS↑) |
| :--- | :--- | :--- | :--- | :--- |
| Nano Banana Pro | No | 0.429 / 2.063 / 0.535 | 0.326 / 1.068 / 0.144 | 0.413 / 1.306 / 0.153 |
| GPT-Image-1.5 | No | 0.236 / 2.120 / 0.438 | 0.326 / 1.068 / 0.144 | 0.525 / 1.578 / 0.150 |
| RealRestorer | Yes | 0.371 / 1.076 / 0.135 | 0.582 / 1.900 / 0.159 | 0.445 / 1.312 / 0.146 |

RealRestorer在开源模型中排名第一，平均FS 0.146，较次优开源模型Qwen-Image-Edit-2511（0.127）高0.019，但与闭源SOTA Nano Banana Pro（0.153）仍有0.007差距。在FoundIR上，RealRestorer平均PSNR 21.45 dB，低于MiM-DiT的30.50 dB，反映生成式模型在保真度上的妥协。

消融实验显示，移除Progressively-Mixed策略导致FS下降0.004，验证其有效性。但28步去噪过程导致计算成本显著高于小规模模型，且对镜面自拍等语义模糊场景处理失败，暴露了生成式模型在物理一致性上的局限。

评估边界方面，RealIR-Bench仅覆盖9种单一退化，未测试复合退化；FoundIR评估依赖配对Clean图，无法反映真实无参考场景。代码与模型将开源，但超参数细节有限，复现性依赖Step1X-Edit基座。

## 关联研究分析

从问题动机看，本文与MiM-DiT同属DiT骨干，但MiM-DiT侧重MoE路由解决参数冲突，本文侧重数据分布解决域差距。MiM-DiT在FoundIR上PSNR 30.50 dB，远高于RealRestorer的21.45 dB，根源在于MoE架构对保真度的优化更直接，而RealRestorer依赖生成先验，牺牲保真度换取感知质量。这种差异源于任务特性：MiM-DiT面向多任务基准，RealRestorer面向真实世界无参考场景。

从方法设计看，本文与PromptIR均使用提示引导，但PromptIR通过可学习提示动态编码退化信息，本文采用固定提示引导编辑模型。PromptIR在CDD11上PSNR 28.50 dB，RealRestorer未在该基准测试，但其在真实域的优势源于数据工程而非提示机制。固定提示是否限制了模型对未知混合退化的自适应能力，论文未给出回答。

## 总结

RealRestorer要解决的核心矛盾是合成数据训练模型在真实世界退化下的泛化失效。本文抓住开源图像编辑模型的强生成先验，通过两阶段渐进混合训练与Web风格数据增强，缩小合成-真实分布偏移。实验证明其在开源模型中SOTA，平均FS 0.146，但FoundIR上PSNR 21.45 dB显著低于专用回归模型。边界在于28步去噪的高计算成本与语义模糊场景的处理失败。当支持集增大到真实复合退化时，固定提示与生成先验的协同效应是否仍能维持感知质量优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.25502)