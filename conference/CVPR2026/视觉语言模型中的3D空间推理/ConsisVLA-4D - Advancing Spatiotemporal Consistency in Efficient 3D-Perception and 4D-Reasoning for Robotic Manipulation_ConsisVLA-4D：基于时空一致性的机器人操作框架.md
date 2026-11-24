# CVPR2026最新论文 ｜ConsisVLA-4D: Advancing Spatiotemporal Consistency in Efficient 3D-Perception and 4D-Reasoning for Robotic Manipulation ｜ConsisVLA-4D：基于时空一致性的机器人操作框架

研究机构：哈尔滨工业大学

作者：Wei Li、Jizhihui Liu、Li Yixing 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.05126)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_aed4ae3c1103)

> 导读 视觉语言动作（Vision-Language-Action, VLA）模型旨在将2D视觉观测与语言指令映射为机器人动作，但现有方法在处理复杂物体布局或动作引发的场景动态变化时，常因缺乏对3D空间结构的精确感知和4D时空演化的推理能力而失效。本文切入点在于指出当前VLA模型过度依赖额外传感器或显式未来帧预测，导致计算开销大且时空一致性不足。ConsisVLA-4D通过构建跨视图、跨物体和跨场景的三级一致性机制，在仅使用2D输入的情况下高效生成3D表示并隐式推理4D动态，实现了性能与效率的双重提升。该框架在LIBERO基准上取得98.1%的平均成功率，但其在真实世界长程任务中的泛化边界及隐式推理的误差累积机制尚存疑。

## 研究背景

当机器人执行“将香蕉放入微波炉”等长程任务时，视觉编码器需从多视角图像中恢复物体的3D位置与几何关系，这一过程称为3D空间感知。然而，单目深度估计存在尺度模糊问题，且动作执行会导致场景动态变化，模型需预测未来状态以维持动作连贯性，这构成了4D时空推理的核心挑战。传统方法要么依赖LiDAR等额外传感器获取显式3D数据，要么通过世界模型显式预测未来帧，前者增加硬件成本，后者计算开销巨大且易产生累积误差。

VLA领域的主流路线分为两类：一类如OpenVLA和π0，基于预训练VLM骨干直接映射2D到动作，但缺乏显式3D几何建模，导致在复杂空间布局中物体定位偏差；另一类如TraceVLA和4D-VLA，引入历史帧或点云以增强空间理解，但受限于传感器依赖或显式预测的计算瓶颈。ConsisVLA-4D的切入点在于，借鉴人类通过双眼视觉维持空间感知一致性并预测未来状态的机制，提出无需额外传感器、仅从2D多视图输入中高效构建3D表示，并通过隐式推理实现4D时空一致性，从而在资源受限场景下提升动作生成的稳定性。

## 核心方法

### 方法参照系

本文问题属于VLA模型中的时空感知与动作生成范畴。通用流程通常包括视觉编码、语言对齐、动作预测三个阶段。本文的关键差异在于，在视觉编码与动作预测之间，显式引入了3D空间感知与4D时空推理两个中间阶段，并通过Token压缩机制确保计算效率，区别于直接端到端映射或依赖显式未来帧预测的传统范式。

### 跨视图物体语义一致性建模

CV-Aligner模块解决多视图输入中物体身份对齐与冗余过滤问题。传统方法直接融合所有视觉Token，导致计算冗余且跨视图物体身份混淆。本文通过显式语义物体选择（ES-Sel）保留指令相关物体，并利用Single-Fusion对齐跨视图物体身份。其核心公式为：

$$ \mathbf{z}_i^{\text{obj-3D}} = f_{\text{SF}}(f_{\text{ES-S}}(\mathbf{z}_i^{\text{sem}}, \mathbf{t}), \mathbf{z}_i^{\text{3D}}) $$

该公式通过交叉注意力将指令相关的语义Token与VGGT提取的3D特征融合，仅保留1/8的原始视觉Token，实现了跨视图物体语义一致性，解决了单视图深度估计的尺度模糊问题。

### 跨物体空间几何一致性建模

CO-Fuser模块解决多视图间物体空间关系歧义问题。传统方法独立处理各视图几何特征，导致跨视图空间关系不一致。本文通过Group-Fusion在DINOv2和VGGT编码器层间融合三视图几何特征，并利用隐式几何关系聚合（IG-Agg）捕获物体间空间关系。其核心公式为：

$$ (\mathbf{z}_{l+1}^{\text{geo-3D}}, \mathbf{z}_{l+1}^{\text{agg-3D}}) = f_{\text{IG-A}}(f_{\text{GF}}(\mathbf{z}_l^{\text{geo}}, \mathbf{z}_l^{\text{3D}}), \mathbf{z}_l^{\text{agg-3D}}) $$

该公式通过余弦衰减加权融合几何特征，生成紧凑的潜在表示（1/12-1/8原始规模），消除了单视图空间关系歧义，确保了跨物体空间几何一致性。

### 跨场景时空一致性推理

CS-Thinker模块解决动作执行中场景动态演化的推理问题。传统方法显式预测未来帧，计算开销大且误差累积。本文通过Spatiotemporal Consistency Attention（SC-Attn）隐式推理未来动态物体和全局深度。其核心公式为：

$$ \hat{\mathbf{A}} = \text{SC-Attn}(\mathbf{z}_{\{M,L,R\}}^{\text{obj-3D}}, \mathbf{z}_{\mathcal{L}'}^{\text{agg-3D}}, \mathbf{t}, \mathbf{0}_{\{M,L,R\}}^{\text{dyn-4D}}, \mathbf{0}^{\text{dep-4D}}, \mathbf{0}^A) $$

该公式将CV-Aligner的物体语义Token和CO-Fuser的几何Token作为隐式知识，与动作Token并行解码，实现了跨场景时空一致性，避免了显式未来帧预测的计算瓶颈。

## 实验评估

实验在LIBERO、ManiSkill2、RoboTwin 2.0仿真基准及Galaxea R1 Lite、AgileX Cobot Magic真实平台上进行，对比基线包括OpenVLA、π0、SpatialVLA、CoT-VLA等，覆盖了单系统、双系统及3D增强VLA路线，但缺失3DThinkVLA等专用3D-VLA强基线。

| 方法 | LIBERO Spatial | LIBERO Object | LIBERO Goal | LIBERO Long | LIBERO Avg |
|---|---|---|---|---|---|
| OpenVLA | 84.7 | 88.4 | 79.2 | 83.7 | 76.5 |
| π0 | 96.8 | 98.8 | 95.8 | 85.2 | 94.2 |
| SpatialVLA | 88.2 | 89.9 | 78.6 | 55.5 | 78.1 |
| ConsisVLA-4D | 98.8 | 99.8 | 98.0 | 95.6 | 98.1 |

ConsisVLA-4D在LIBERO上平均成功率98.1%，较OpenVLA提升21.6%，较SpatialVLA提升20%，验证了3D感知与4D推理对动作生成的增益。

| 消融组件 | LIBERO SR | Real-World SR |
|---|---|---|
| w/o ES-Sel. & S-Fus. | 91.7 (-6.4) | 68.3 (-10.0) |
| w/o G-Fus. & IG-Agg. | 95.6 (-2.5) | 70.0 (-8.3) |
| w/o Dyn. O. & Glob. D. | 94.7 (-3.4) | 71.6 (-6.7) |
| Full Model | 98.1 | 78.3 |

消融实验显示，移除CV-Aligner的ES-Sel.和S-Fus.导致真实世界成功率下降10.0%，移除CO-Fuser的G-Fus.和IG-Agg.下降8.3%，表明跨视图语义对齐和跨物体几何融合对真实场景鲁棒性贡献最大。CS-Thinker的隐式4D推理移除后，真实世界成功率下降6.7%，验证了时空一致性对长程任务的重要性。

评估指标涵盖仿真成功率、真实世界子任务成功率及推理延迟/吞吐量，但未报告置信区间和收敛曲线。代码已开源，训练使用4×A800 GPU，真实世界推理在单张RTX 5090上运行，超参数细节完整披露，可复现性较高。

## 关联研究分析

从问题动机看，ConsisVLA-4D与SpatialVLA均致力于从2D输入推断3D空间结构，但SpatialVLA侧重静态场景的空间关系问答，而ConsisVLA-4D聚焦动作执行中的动态场景演化。这一差异源于任务特性：问答任务只需当前帧的空间理解，而操作任务需预测动作引发的场景变化。ConsisVLA-4D通过CS-Thinker隐式推理未来状态，避免了SpatialVLA在动态场景中因缺乏时序建模而导致的动作不连贯问题。

从方法设计看，ConsisVLA-4D与TraceVLA均引入4D线索，但TraceVLA依赖显式历史帧输入，而ConsisVLA-4D通过CV-Aligner和CO-Fuser从当前多视图输入中构建3D表示，并隐式推理4D动态。这一设计选择源于对计算效率的考量：显式历史帧输入增加序列长度，导致注意力计算开销呈平方级增长，而ConsisVLA-4D的Token压缩机制将视觉输入减少至1/8，实现了2.31倍推理加速。然而，隐式推理在长程任务中的误差累积机制未得到充分验证，当任务步数超过50时，隐式预测的可靠性是否下降，论文未给出回答。

## 总结

ConsisVLA-4D要解决的核心矛盾是VLA模型在复杂动态场景中时空一致性不足与计算效率低下的冲突。现有方法或依赖额外传感器，或显式预测未来帧，均无法在资源受限场景下实现高效稳定的动作生成。本文通过CV-Aligner、CO-Fuser和CS-Thinker三级一致性机制，从2D多视图输入中高效构建3D表示并隐式推理4D动态，在LIBERO基准上取得98.1%平均成功率，推理延迟较OpenVLA降低2.31倍。其边界在于，真实世界实验仅覆盖4类长程任务，且隐式4D推理的误差累积机制未得到量化验证。当任务步数进一步增加或场景动态性增强时，隐式推理的可靠性是否仍能维持，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_aed4ae3c1103)