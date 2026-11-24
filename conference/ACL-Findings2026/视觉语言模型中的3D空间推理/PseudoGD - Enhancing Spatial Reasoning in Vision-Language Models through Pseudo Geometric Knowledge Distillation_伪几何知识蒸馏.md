# ACL-Findings2026最新论文 ｜PseudoGD: Enhancing Spatial Reasoning in Vision-Language Models through Pseudo Geometric Knowledge Distillation ｜伪几何知识蒸馏

作者：Gwanghee Lee、Yeeun Choi、Kyoungson Jhang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2983755d5737)

> 视觉语言模型（Vision-Language Model, VLM）在3D空间推理中面临的核心困境是视觉编码器缺乏度量尺度与结构先验，导致定量距离估计与视角转换任务表现不佳。现有方案或依赖昂贵的3D点云数据，或仅通过合成数据微调无法改变编码器内部的2D语义偏置。本文切入点在于利用单目2D图像，通过深度与分割教师模型生成伪标签，将几何信息蒸馏进视觉编码器。该方法在OmniSpatial基准上提升了多种架构的空间推理能力，但其对教师模型误差的依赖及静态图像限制使其在复杂动态场景中的泛化性存疑。

## 研究背景

VLM处理3D空间任务时，首先需从2D像素中恢复度量深度与物体边界。然而，基于CLIP等预训练编码器主要学习图像-文本对的语义匹配，其内部表征缺乏焦长、物理尺寸等度量信息，导致模型无法区分“近处的大物体”与“远处的小物体”。这种2D语义与3D几何的模态鸿沟，使得模型在绝对距离估计和假设性视角转换（Hypothetical Perspective Taking）等任务上出现系统性偏差。

主流解决路线分为数据驱动与架构增强两类。数据驱动路线如SpatialVLM（Chen et al., 2024）通过合成大规模空间问答数据微调VLM，但受限于编码器固有的2D偏置，仅增加数据量无法根本改变特征空间的结构。架构增强路线如SR-3D（Cheng et al., 2025）引入多视图或点云输入，虽提升了几何保真度，但依赖专用采集设备与受控环境，数据扩展性差，且无法利用海量网络2D数据。本文指出，现有方法要么牺牲数据规模，要么牺牲几何精度，缺乏一种能在标准2D输入下内化3D几何先验且具备数据扩展性的方案。

## 核心方法

### 方法参照系

几何感知架构通常通过显式输入深度图或点云特征，经投影头对齐至LLM空间。本文的关键差异在于不依赖显式3D真值输入，而是将深度估计与分割模型作为教师，通过知识蒸馏将几何特征隐式注入2D视觉编码器，实现单目输入下的几何内化。

### 伪几何知识蒸馏

传统蒸馏方法依赖显式3D标注，而本文利用Depth Pro与SAM生成伪标签，解决3D数据稀缺问题。Depth Pro提供度量深度，注入物理尺度感；SAM提供结构分割，强化物体边界与部分-整体关系感知。通过轻量级投影头将学生编码器特征映射至教师空间，联合优化度量深度误差与结构相似度损失，使编码器在不接触3D真值的情况下习得通用几何特征。

$$
\mathcal{L}_{Distill} = \mathcal{L}_{Depth} + \mathcal{L}_{Seg}
$$

该公式表明，蒸馏目标由度量深度回归损失与结构分割损失组成，前者确保尺度准确性，后者确保结构完整性，二者互补以覆盖定量与定性空间推理需求。

### 联合训练策略

顺序训练（先几何预训练后VQA微调）易导致语义知识灾难性遗忘及特征分布失配。本文采用联合训练策略，在统一优化循环中同时优化VQA自回归损失与几何蒸馏损失，确保LLM实时适应编码器演变的视觉特征。

$$
\mathcal{L}_{Total} = \lambda_{VQA}\mathcal{L}_{VQA} + \lambda_{Depth}\mathcal{L}_{Depth} + \lambda_{Seg}\mathcal{L}_{Seg}
$$

其中 $\lambda_{VQA} = \lambda_{Depth} = \lambda_{Seg} = 1.0$。该设计避免了特征空间断裂，使几何先验与语言推理能力同步进化，解决了单独几何预训练后LLM无法有效利用新视觉特征的问题。

## 实验评估

实验在OmniSpatial基准上进行，对比SpaceLLaVA、SpaceMantis、SpaceQwen2.5-VL及SpaceThinker四种架构。基线覆盖了主流空间VLM，但缺乏与VSI-Bench等视频级基准的对比，限制了跨基准可比性。

| Method | Overall | Dynamic Reasoning | Spatial Interaction | Complex Logic | Perspective Taking |
| :--- | :--- | :--- | :--- | :--- | :--- |
| SpaceThinker-Qwen2.5† | 40.42 | 47.84 | 53.06 | 43.29 | 31.08 |
| + PseudoGD | 42.20 | 55.41 | 49.42 | 49.41 | 44.58 |
| SpaceLLaVA-13B | 36.14 | 52.70 | 21.39 | 43.53 | 38.10 |
| + PseudoGD | 38.88 | 56.76 | 30.35 | 50.59 | 45.78 |

SpaceThinker-Qwen2.5 + PseudoGD整体准确率提升1.78%至42.20%，其中假设性视角转换从31.08%跃升至44.58%，表明度量深度内化显著改善了无显式3D先验下的视角模拟能力。

消融实验未单独报告损失权重 $\lambda$ 的敏感性分析，但默认等权设置下，SpaceQwen2.5VL-3B在动态推理子项上出现负迁移（58.11%降至50.00%），暗示小模型在联合训练中可能因几何特征干扰而损失部分语义能力。

评估仅基于静态单图像，未覆盖视频时序推理；代码未公开，LoRA秩（LLM 128, Encoder 4）及投影头细节仅简述，可复现性受限。

## 关联研究分析

从问题动机看，PseudoGD与SpatialVLM均旨在解决3D数据稀缺问题，但SpatialVLM依赖合成数据规模，而PseudoGD依赖教师模型质量。SpatialVLM的瓶颈在于编码器2D偏置无法通过数据量弥补，PseudoGD则通过蒸馏直接修改编码器表征。然而，PseudoGD未验证在ScanRefer等3D Grounding基准上的表现，而领域共识认为Grounding是空间推理前置条件，这暗示其几何内化可能未充分解决定位瓶颈。

从方法设计看，PseudoGD与3D VLM-GD（Lee et al., 2025）同属几何蒸馏路线，但3D VLM-GD依赖3D基础模型提取几何线索，PseudoGD则使用2D教师模型生成伪标签。这一差异源于数据可用性：3D VLM-GD需3D真值，PseudoGD仅需2D图像。但PseudoGD的“伪”标签引入了教师误差传播风险，在镜面、透明物体等场景下可能失效，而3D VLM-GD因依赖真值避免了此问题，但牺牲了数据扩展性。

## 总结

PseudoGD针对VLM视觉编码器缺乏3D几何先验的核心矛盾，利用Depth Pro与SAM生成伪标签进行知识蒸馏，并通过联合训练避免语义遗忘。该方法在OmniSpatial基准上使SpaceThinker-Qwen2.5整体准确率提升至42.20%，假设性视角转换提升13.5%。其边界在于依赖教师模型质量，且在静态图像上验证，未覆盖动态场景。当教师模型在镜面或极端光照下产生伪标签误差时，学生编码器的几何内化是否会导致系统性空间幻觉，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_2983755d5737)