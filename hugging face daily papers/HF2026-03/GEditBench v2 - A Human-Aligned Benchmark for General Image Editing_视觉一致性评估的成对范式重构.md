# HuggingFace最新推荐论文 ｜GEditBench v2: A Human-Aligned Benchmark for General Image Editing ｜视觉一致性评估的成对范式重构

研究机构：新加坡南洋理工大学、东南大学

作者：Zhangqi Jiang、Zheng Sun、Xianfang Zeng 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.28547)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.28547)

> 指令式图像编辑（IBIE）在复杂指令下常因过度修改非目标区域而破坏视觉一致性，但现有基准依赖闭源API的绝对评分，既难复现又与人类偏好错位。本文切入点在于将评估范式从Pointwise转向Pairwise，并构建专用开源评估器。通过区域解耦数据合成训练PVC-Judge，并在GEditBench v2上验证其人类对齐度。该工作填补了开源、细粒度一致性评估的空白，但其对多轮编辑与物理一致性的覆盖仍显不足。

## 研究背景

当编辑模型执行“将棉衬衫换成丝绸”指令时，需在渲染新材质的同时严格保留主体身份与背景光影。这种对非目标区域像素级保持的要求，构成了视觉一致性（Visual Consistency, VC）的核心定义。然而，VC的量化评估长期依赖视觉语言模型（VLM）作为裁判（VLM-as-a-Judge），现有协议普遍采用Pointwise绝对评分，即让VLM对单张图像打分。这种范式存在固有缺陷：绝对分数受限于训练分布的天花板效应，且闭源API（如GPT-4.1）的不透明性导致结果难以复现，开源小模型又缺乏足够的先验知识进行可靠判断。

IBIE领域已从基础语义编辑演进至复杂场景下的精细控制，Nano Banana Pro等模型展示了强大的泛化能力，但社区关注点正从“指令遵循”转向“指令边界”的精确界定。现有基准如GEdit-Bench和ImgEdit-Bench虽引入了VLM评估，但任务覆盖局限于预定义类别，且评估指标与人类偏好的成对比较（Pairwise Comparison）机制存在系统性偏差。本文针对这一评估缺口，提出GEditBench v2基准与PVC-Judge评估模型，旨在通过开源、人类对齐的成对评估体系，解决现有协议在VC维度上的失真问题。

## 核心方法

### 评估范式参照系

当前IBIE评估的主流流程是：利用VLM对编辑结果进行Pointwise评分，涵盖指令遵循（IF）、视觉质量（VQ）和视觉一致性（VC）三个维度。该流程的关键差异在于，本文摒弃了绝对评分，强制采用Pairwise比较范式，并针对VC维度开发了专用微调模型，而非直接调用通用VLM。

### 成对偏好数据合成

Pointwise评分的天花板效应源于模型学习的是到绝对分数的刚性映射，导致对分布外（OOD）编辑产生相似分数。为克服此局限，本文设计了对象中心与人类中心的数据合成流水线。其核心在于任务自适应的区域解耦（Region Decoupling）：利用Qwen3-VL-8B-Instruct定位编辑目标，将图像划分为编辑区 $\Omega_{edit}$ 与非编辑区 $\Omega_{non}$。

$$
\mathcal{L}_{consistency} = \lambda_1 \cdot \mathcal{M}_{low}(\Omega_{non}) + \lambda_2 \cdot \mathcal{M}_{task}(\Omega_{edit})
$$

该公式表明，一致性评估由两部分加权组成：在非编辑区 $\Omega_{non}$ 使用SSIM、LPIPS等低层指标强制视觉不变性；在编辑区 $\Omega_{edit}$ 使用任务特定指标（如颜色修改仅计算亮度通道的SSIM）以解耦身份保持与编辑效果。这种空间锚定的评估策略，确保了偏好对的生成严格聚焦于“非目标区域是否被意外修改”，从而为PVC-Judge提供了高质量的训练信号。

### 专用评估器微调

基于上述偏好对，本文对Qwen3-VL-8B-Instruct进行LoRA微调，构建PVC-Judge。训练采用AdamW优化器，学习率 $2.0 \times 10^{-6}$，LoRA秩 $r=64$。

$$
\mathcal{L}_{pairwise} = -\log \sigma(f(x_w) - f(x_l))
$$

该损失函数优化相对偏好，而非绝对分数。与Pointwise不同，Pairwise训练使模型学习区分两张图像的相对优劣，从而在评估新模型时保持判别力，避免了绝对评分的分布外泛化失效。PVC-Judge专门针对VC维度设计，而IF和VQ维度仍依赖GPT-4o进行成对评估，以利用其丰富的世界知识。

## 实验评估

实验在GEditBench v2（1,200样本，23任务）和VCReward-Bench（3,506专家标注偏好对）上进行。基线覆盖包括Nano Banana Pro、GPT-Image-1.5、FLUX.2系列、Qwen-Image-Edit等主流开源与闭源模型，但缺失MIRA、EditThinker等推理型编辑器的直接对比。

| 模型 | Overall ELO | 95% CI | Arena ELO |
| :--- | :--- | :--- | :--- |
| Nano Banana Pro | 1,096 | -6/+6 | 1,251 |
| Seedream 4.5 | 1,089 | -7/+7 | 1,196 |
| GPT Image 1.5 | 1,071 | -7/+6 | 1,270 |
| FLUX.2 [klein] 9B | 1,039 | -6/+6 | 1,166 |
| Qwen-Image-Edit-2511 | 1,038 | -6/+6 | 1,164 |

PVC-Judge在VCReward-Bench上的平均准确率为81.82%，超越GPT-5.1的76.89%。GEditBench v2的Overall Elo与人类标注Arena Elo的Spearman相关系数为0.929，验证了评估体系的有效性。

消融实验显示，每任务样本数 $N$ 从500增至1,500时，VC评估准确率稳步提升，超过1,500后趋于饱和。这表明区域解耦数据合成在中等规模下即可达到性能上限，无需过度增加数据量。

评估边界方面，GEditBench v2排除了多图像输入任务，因开源VLM在多图像理解上存在显著性能差距（Qwen2.5-VL-7B比GPT-4o低8.41%）。代码与模型已开源，训练使用8块NVIDIA L40S GPU，超参数公开，具备高可复现性。

## 关联研究分析

从问题动机看，本文与EditReward（Wu et al., 2025）均关注编辑质量评估，但EditReward侧重构建大规模人类偏好数据集以训练奖励模型用于RL后训练，而本文聚焦于基准评估中VC维度的人类对齐。EditReward的奖励信号用于优化模型参数，本文的PVC-Judge用于评估模型性能，二者在应用环节上形成互补。本文的Pairwise范式直接挑战了GEdit-Bench（Liu et al., 2025）等现有基准的Pointwise惯例，其根源在于绝对评分在OOD场景下的判别力衰减，这一差异是否在所有编辑任务中均成立，论文未给出跨任务的系统性验证。

从方法设计看，本文与ImgEdit-Bench（Ye et al., 2025c）同属VLM-as-a-Judge框架，但ImgEdit-Bench依赖闭源GPT-4o进行Pointwise评分，本文则通过区域解耦数据合成训练开源8B模型进行Pairwise评分。这一设计选择解决了闭源API不可复现与开源小模型先验不足的双重瓶颈。然而，区域解耦依赖Qwen3-VL-8B-Instruct的定位精度，若定位掩码存在偏差，可能导致 $\Omega_{non}$ 包含部分编辑区域，从而引入评估噪声。这种对定位精度的依赖，在复杂遮挡或模糊边界场景下的鲁棒性，论文未提供定量分析。

## 总结

本文要解决的核心矛盾是IBIE评估中视觉一致性维度与人类偏好的错位，以及闭源API带来的不可复现性。现有Pointwise评分范式受限于天花板效应，无法准确捕捉非目标区域的细微变化，而本文通过区域解耦数据合成与Pairwise微调，构建了开源、人类对齐的PVC-Judge。实验证明PVC-Judge在VCReward-Bench上达到81.82%准确率，超越GPT-5.1，且GEditBench v2与人类偏好高度相关（$\rho=0.929$）。本文的边界在于排除了多图像输入任务，且区域解耦依赖定位模型的精度。当编辑指令涉及多对象交互或模糊边界时，区域解耦的掩码质量是否足以支撑可靠的VC评估，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.28547)