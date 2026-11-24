# CVPR2026最新论文 ｜DrivePI: Spatial-aware 4D MLLM for Unified Autonomous Driving Understanding, Perception, Prediction and Planning ｜DrivePI：空间感知4D多模态大语言模型

研究机构：天津大学、华中科技大学

作者：Zhe Liu、Runhui Huang、Rui Yang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.12799)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.12799)

> 端到端自动驾驶中，视觉-语言-动作（Vision-Language-Action, VLA）模型虽具备语义交互能力，却因缺乏细粒度3D空间表征导致感知精度与安全性不足。现有VLA方法仅依赖相机图像输出高层指令，无法生成体素级占据状态，而传统视觉-动作（Vision-Action, VA）模型虽空间精准却缺乏语言交互。DrivePI通过引入LiDAR点云与3D占据/占据流预测头，在单一0.5B参数MLLM中统一了粗粒度语言理解与细粒度空间感知。该框架在3D占据任务上超越了专用VA模型，但在轨迹规划精度上仍落后于最新SOTA，其空间增强对长尾场景泛化的实际贡献尚待闭环验证。

## 研究背景

当VLA模型处理复杂驾驶场景时，其基于离散文本token的推理机制难以捕捉连续空间几何信息——这一现象源于语言表征的高压缩性。这种空间感知精度不足导致模型在精细避障与定位上产生误差，进而削弱了轨迹规划的安全性。为弥补此缺陷，研究者尝试将专用感知模块嵌入MLLM架构，但如何在不破坏语言交互能力的前提下实现空间与语义的联合优化，仍是核心挑战。

端到端自动驾驶领域正从模块化流水线向统一架构演进。早期VA模型如UniAD和VAD通过3D感知到预测的模块化设计实现了精准空间定位，但缺乏自然语言交互能力；随后出现的VLA模型如OpenDriveVLA和ORION引入了MLLM以增强语义理解，却因缺失细粒度中间3D感知输出而牺牲了可解释性与安全保证。DrivePI的切入点在于打破VA与VLA的二元对立，通过共享骨干网络同时输出3D占据、占据流、轨迹及文本描述，旨在解决VLA模型“空间盲”与VA模型“语义哑”的双重局限。

## 核心方法

### 方法参照系

标准VLA流程将多视角图像与语言指令输入MLLM，经自注意力机制后由动作头输出轨迹。本文的关键差异在于：输入端强制引入LiDAR点云以提供精确3D几何信息，输出端新增3D占据头与占据流头，将空间感知任务与语言理解任务置于同一MLLM骨干中进行端到端联合优化，而非采用独立的感知模块。

### 空间投影与多模态融合

针对BEV特征分辨率高（通常超过$100 \times 100$）直接输入MLLM计算成本过高的问题，DrivePI采用交叉注意力机制替代传统池化操作。给定BEV特征$F_{bev} \in \mathbb{R}^{H \times W \times C}$，先将其划分为$N$个$K \times K$的patch得到$F_{patch} \in \mathbb{R}^{N \times K^2 \times C}$，再通过池化得到$F_{pool} \in \mathbb{R}^{N \times 1 \times C}$。交叉注意力公式为：

$$F_{v} = \text{Linear}(\text{CrossAttn}(Q=F_{pool}, K=F_{patch}, V=F_{patch}))$$

该设计以池化特征为查询、原始patch为键值，在压缩空间维度的同时保留了细粒度几何细节，解决了传统池化导致的空间信息丢失问题，使MLLM能够基于精确的3D几何信息进行空间推理。

### 细粒度空间头与联合优化

在MLLM输出特征$F_v$基础上，DrivePI通过线性投影将其重塑为空间特征图$F_{out} \in \mathbb{R}^{H \times W \times C}$，并接入三个专用头：3D占据头、占据流头与动作扩散头。总损失函数定义为：

$$\mathcal{L}_{total} = \lambda_1 \mathcal{L}_{llm} + \lambda_2 \mathcal{L}_{occ} + \lambda_3 \mathcal{L}_{flow} + \lambda_4 \mathcal{L}_{action}$$

其中$\lambda_i$为平衡权重，本文实验中均设为1。这一联合优化策略的设计动机在于：单一任务训练会导致特征空间偏向特定模态，而多任务共享表征迫使MLLM在语言语义与空间几何之间建立内在关联。消融实验证实，联合训练相比仅视觉头训练，RayIoU提升1.8%，L2误差降低0.52米，验证了空间任务对语言理解的特征对齐作用。

## 实验评估

实验在nuScenes数据集上进行，涵盖750个训练场景与150个验证场景，评估指标包括3D占据的RayIoU、占据流的mAVE、轨迹规划的L2误差与碰撞率，以及nuScenes-QA的准确率。基线覆盖VA类（VAD, UniAD, FB-OCC）与VLA类（OpenDriveVLA, ORION），但缺失2026年最新SOTA如HiST-VLA与SGDrive，可能因发表时点限制。

| 任务 | 指标 | DrivePI (0.5B) | 最佳VA基线 | 最佳VLA基线 |
|---|---|---|---|---|
| 3D占据 (OpenOcc) | RayIoU (%) | 49.3 | 41.9 (ALOcc-Flow-3D) | - |
| 占据流 (OpenOcc) | mAVE | 0.509 | 0.470 (CascadeFlow) | - |
| 轨迹规划 (nuScenes) | L2 (m, w/ Ego) | 0.40 | 0.33 (OmniDrive) | 0.34 (ORION) |
| 轨迹规划 (nuScenes) | Col. (%) (w/ Ego) | 0.11 | 0.30 (OmniDrive) | 0.37 (ORION) |
| 文本理解 (nuScenes-QA) | Acc. (%) | 60.7 | 57.0 (BEVDet+BUTD) | 58.2 (OpenDriveVLA-7B) |

DrivePI在3D占据任务上以49.3% RayIoU超越最佳VA基线ALOcc-Flow-3D的41.9%，但在占据流mAVE上略逊于CascadeFlow的0.470。轨迹规划方面，带Ego状态时L2误差0.40米高于OmniDrive的0.33米，但碰撞率0.11%显著低于ORION的0.37%，表明空间感知增强对安全性的贡献大于对精度的贡献。

| 消融设置 | RayIoU (%) | mAVE | L2 (m) | Col. (%) | QA Acc. (%) |
|---|---|---|---|---|---|
| 仅文本头 (I) | - | - | - | - | 61.2 |
| 仅视觉头 (II) | 47.5 | 0.69 | 1.02 | 0.39 | - |
| 联合训练 (III) | 49.3 | 0.51 | 0.50 | 0.38 | 60.7 |

联合训练相比仅视觉头，RayIoU提升1.8%，mAVE降低0.18，L2误差降低0.52米，但QA准确率从61.2%微降至60.7%。这一结果揭示了空间任务与语言任务在特征空间上的轻微竞争，但整体收益显著。数据规模消融显示，将占据QA对从28K扩展至560K，占据状态预测准确率从73.0%提升至87.0%，表明空间理解能力对数据规模敏感。

评估边界方面，本文仅报告开环nuScenes指标，未提供闭环CARLA或NAVSIM结果，无法验证空间增强在动态交互场景中的有效性。代码已开源，训练使用8×NVIDIA L40S GPU，超参数$\lambda_i=1$，但0.5B骨干的性能上限是否限制了长尾场景泛化，论文未给出回答。

## 关联研究分析

从问题动机看，DrivePI与Qwen-Drive-1.0均致力于VLA统一架构，但Qwen-Drive-1.0通过视角标签与帧标签序列化解决时空定位问题，依赖大规模预训练获取世界知识；DrivePI则通过LiDAR点云与3D占据头直接增强空间几何表征，无需依赖预训练中的空间知识。这一差异源于任务特性：Qwen-Drive-1.0侧重开放世界泛化，而DrivePI聚焦于精细空间定位。DrivePI的LiDAR依赖是否限制了其在纯视觉部署场景的泛化能力，论文未做对比实验。

从方法设计看，DrivePI与CoT4AD均引入中间表征以增强可解释性，但CoT4AD采用显式文本思维链（CoT）序列，DrivePI采用隐式3D占据/占据流预测。CoT4AD的可解释性体现在文本推理过程，便于安全审计；DrivePI的可解释性体现在空间占据状态，便于物理验证。两者在推理延迟上存在权衡：CoT4AD的文本生成增加延迟，DrivePI的占据预测计算开销较大但无需文本解码。空间占据预测是否足以替代文本CoT在逻辑一致性上的作用，现有评测多侧重最终轨迹精度，缺乏对推理过程质量的统一评估。

## 总结

DrivePI要解决的核心矛盾是VLA模型语义交互能力与空间感知精度之间的冲突。其切入点在于利用LiDAR点云提供精确几何信息，并通过3D占据/占据流头将空间感知任务与语言理解任务联合优化，从而在单一MLLM中实现双模态理解。该方法在0.5B参数规模下，3D占据RayIoU达49.3%，碰撞率降至0.11%，证明了空间增强对安全性的直接贡献。然而，其轨迹规划L2误差0.40米仍高于OmniDrive的0.33米，且仅在开环nuScenes上验证，未评估闭环动态交互场景。当支持集增大到长尾罕见场景时，0.5B骨干的空间感知能力是否足以维持安全性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.12799)