# HuggingFace最新推荐论文 ｜SpatialBlock: Enhancing Spatial Intelligence in LVLMs via Synthetic Block-Stacking Problem ｜基于合成积木任务的LVLM空间智能增强

研究机构：韩国科学技术院

论文原文见 [arXiv](https://arxiv.org/abs/2609.07064)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.07064)

> 视觉语言模型（LVLM）在2D图像理解上表现优异，但缺乏从平面图像重建3D结构的空间智能，这一缺陷阻碍了其在自动驾驶与机器人领域的落地。现有方法依赖高成本、易噪声的真实场景3D标注，导致数据规模受限且泛化能力不足。本文借鉴发展心理学中的积木游戏范式，提出SpatialBlock-15k合成数据集，通过结构化积木堆叠任务训练LVLM的基础空间技能。该方法以极小的合成数据量显著提升了模型在真实场景空间推理基准上的表现，但其在复杂数值回归任务上的有效性仍存疑。

## 研究背景

LVLM的空间智能瓶颈源于其预训练数据中缺乏显式的3D几何先验。当模型面对需要推断深度、遮挡关系或视角变换的任务时，仅凭2D语义特征无法恢复度量空间结构。这种模态鸿沟导致模型在绝对距离估计、方位判断等定量任务上表现不佳，而解决这一问题的传统路径是引入深度图、点云或3D重建特征，但这要求输入包含额外的几何模态或依赖外部感知模块。

主流的空间智能增强路线分为架构融合与数据驱动两类。架构融合路线如SR-3D、N3D-VLM通过引入显式几何编码器或3D坐标表示，提升了几何保真度，但增加了计算开销且依赖RGB-D数据；数据驱动路线如SpatialVLM、SpatialRGPT利用大规模合成或真实场景QA数据微调，但后者面临标注成本高、噪声大、规模受限的问题。这些方法均假设通过数据规模或架构复杂度可弥补几何先验缺失，却忽视了基础空间认知技能的习得机制。

本文切入点在于将空间智能训练从“标注密集的真实场景监督”转向“结构化基础技能学习”。借鉴发展心理学中积木游戏对空间整合与心理模拟能力的促进作用，本文设计纯合成的积木堆叠任务，规避了真实场景标注的成本与噪声，旨在验证基础空间技能训练能否有效迁移至真实场景的空间推理。

## 核心方法

### 方法参照系

本文问题属于“数据合成与高效推理”路线，但区别于SpatialForge等依赖外部模块生成QA的方法，本文采用纯程序化生成积木图像，无需分割、深度估计等外部感知模块，从而保证数据的清洁性与可扩展性。

### 结构化积木任务设计

设计动机：真实场景标注依赖外部模块导致噪声大且成本高，而积木任务可通过程序化生成实现无噪声、大规模的数据构建。SpatialBlock-15k包含三类任务：3D-to-2D投影（Q1）、视角变换（Q2）、结构组合（Q3），每类5k样本。引入颜色调制作为功能线索：Q1中颜色编码深度顺序，Q2中锚点块颜色保持结构角色不变，Q3中重叠块颜色指示连接位置。这种设计模拟人类以特定物体为锚点解析场景的认知机制，使模型学习基于参考点的相对关系推理，而非仅依赖几何形状匹配。

### 双策略训练框架

设计动机：直接答案预测缺乏推理过程，难以提升复杂空间逻辑能力；而纯RL训练易导致推理能力退化。本文采用LoRA初始化+GRPO强化学习的双策略框架。LoRA初始化保留模型固有的Chain-of-Thought（CoT）能力，避免全参数微调导致的推理退化；GRPO通过多目标奖励函数优化推理链质量与答案准确性。奖励函数定义为：

$$
\mathcal{R}(y, o) = \mathcal{R}_{\text{acc}}(y,o) + \mathcal{R}_{\text{format}}(o) + \mathcal{R}_{\text{len}}(o)
$$

其中$\mathcal{R}_{\text{acc}}$验证答案正确性，$\mathcal{R}_{\text{format}}$强制CoT结构，$\mathcal{R}_{\text{len}}$约束响应长度在50-1024 token之间。GRPO目标函数为：

$$
\mathcal{J}_{\text{GRPO}}(\theta) = \mathbb{E}_{c, \{o_i\}} \left[ \frac{1}{G} \sum_{i=1}^G \min \left( \frac{\pi_\theta(o_i|c)}{\pi_{\theta_{\text{old}}}(o_i|c)} A_i, \text{clip} \left( \frac{\pi_\theta(o_i|c)}{\pi_{\theta_{\text{old}}}(o_i|c)}, 1 \pm \varepsilon \right) A_i \right) - \beta \text{KL} [\pi_\theta || \pi_{\text{ref}}] \right]
$$

该公式通过组内相对优势$A_i$优化策略，同时KL散度约束防止模型偏离参考分布，确保推理稳定性。

## 实验评估

实验在SB-Bench（自建）、MindCube、MMSI-Bench、SPBench、MMMU五个基准上进行，基线覆盖Qwen、InternVL等开源模型及SpaceQwen、SpatialLadder等空间专家模型，但缺失SR-3D、SpatialStack等架构创新类基线。主实验结果显示，SpatialBlock-4B-direct在MindCube上达51.3%，高于基线Qwen3-VL-4B-Instruct的17.0%；SpatialBlock-7B-reason在MMSI-Bench上达29.7%，高于SpaceR的27.4%。

| 模型 | 数据量 | MindCube | MMSI-Bench | SPBench | MMMU |
|---|---|---|---|---|---|
| Qwen3-VL-4B-Instruct | - | 17.0 | 26.2 | 44.5 | 47.5 |
| SpatialBlock-4B-direct | 15K | 51.3 | 27.8 | 45.9 | 47.2 |
| SpatialBlock-7B-reason | 15K | 37.9 | 29.7 | 50.9 | 55.5 |

消融实验表明，LoRA初始化优于全参数微调冷启动，后者因生成噪声推理轨迹导致性能提升有限。Synthetic-Real数据集（相对方向/距离任务）在SPBench上达43.4%，但MindCube仅32.8%，低于SpatialBlock的49.1%，证明积木任务提供的学习信号优于传统空间QA形式。

评估边界：所有基准均为多选题，未覆盖数值回归任务；代码已开源，但超参数与GPU配置未在正文中详细报告；MindCube上SpatialBlock-4B-direct的51.3%低于领域SOTA pySpatial/Think3D的62.67%，表明合成积木任务在复杂空间建模上仍有局限。

## 关联研究分析

从问题动机看，本文与SpatialVLM同属数据驱动路线，但SpatialVLM依赖大规模真实场景QA数据，本文采用纯合成积木任务。差异根源在于任务特性：SpatialVLM面向通用空间关系推理，需覆盖真实场景的长尾分布；本文聚焦基础空间技能，通过结构化任务规避标注成本，但牺牲了对真实场景复杂性的覆盖。

从方法设计看，本文与SCOUT均使用RL优化空间推理，但SCOUT针对复杂空间逻辑与数值回归，本文针对基础空间技能。差异根源在于训练目标：SCOUT的奖励函数包含几何精度约束，本文的奖励函数仅验证答案正确性与格式，未引入数值回归监督。这导致本文在MindCube等需要心理模拟的任务上表现良好，但在需要精确数值预测的任务上缺乏竞争力。

## 总结

本文核心矛盾是真实场景3D标注的高成本与LVLM空间智能训练的规模需求之间的冲突。本文抓住发展心理学中积木游戏对基础空间技能的促进作用，通过纯合成积木任务规避标注成本，验证了基础空间技能训练的有效性。SpatialBlock-4B-direct在MindCube上达51.3%，SpatialBlock-7B-reason在MMSI-Bench上达29.7%，证明合成数据可显著提升空间推理性能。但本文边界在于仅覆盖多选题形式的空间关系推理，未验证数值回归任务；且MindCube性能低于领域SOTA，表明积木任务对复杂空间建模的覆盖不足。当支持集从15k扩展到更大规模时，合成积木任务的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.07064)