# ICLR2026最新论文 ｜From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors ｜从空间到动作：基于空间基础先验的视觉-语言-动作模型

研究机构：新加坡国立大学、新加坡南洋理工大学

作者：Zhengshen Zhang、Hao Li、Yalun Dai 等 13 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.17439)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.17439)

> 视觉-语言-动作模型（Vision-Language-Action Model, VLA）旨在让机器人通过自然语言指令执行复杂操作，但现有模型多基于2D编码器，缺乏3D几何感知导致泛化能力受限。直接注入3D输入依赖昂贵传感器且破坏视觉-语言对齐，而弱3D线索又无法提供足够的几何先验。FALCON通过解耦架构，将空间基础模型提取的3D空间Token直接注入动作头，在保留RGB-only鲁棒性的同时支持可选的深度与位姿输入。该设计在仿真与真实任务中显著提升了空间推理与泛化性能，但其对动态场景几何精度的依赖及未覆盖的长程记忆能力仍存疑。

## 研究背景

当机器人执行“将苹果放入顶层抽屉”这类指令时，它必须同时理解语义意图与物体的3D空间位置。传统VLA模型将动作表示为语言Token，依赖2D图像与文本对齐，但2D投影丢失了深度与尺度信息，导致模型在物体高度变化或背景杂乱时难以准确规划轨迹。这种2D语义与3D几何的模态鸿沟，使得模型无法从平面图像中恢复度量空间结构，成为制约其进入物理世界交互的核心障碍。

为弥合这一鸿沟，现有VLA研究主要沿两条路线展开：一是直接消费显式3D表示（如点云、深度图），如PointVLA与GeoVLA，但这类方法依赖专用传感器，在缺乏3D标注的大规模数据集（如Open X-Embodiment）上难以扩展，且模态可迁移性差；二是将3D特征嵌入VLM输入空间，如SpatialVLA与3D-VLA，但强行对齐空间嵌入与文本Token会破坏预训练的视觉-语言对齐，导致零样本泛化能力下降，且弱几何信号不足以支撑精细的空间推理。FALCON的切入点在于将3D空间处理从VLM主干中解耦，通过独立的空间分支提取几何先验，并在动作生成阶段进行融合，从而在保留语义完整性的同时实现灵活的模态输入。

## 核心方法

### 方法参照系

通用VLA流程通常将视觉与语言输入编码为统一序列，通过LLM生成动作Token。本文的关键差异在于，它不将3D信息融入VLM的文本流，而是引入并行的空间基础模型分支，仅在动作头阶段融合语义与空间特征，避免了VLM内部的对齐漂移。

### 具身空间模型（ESM）

ESM旨在解决弱3D线索几何信号不足的问题，通过注入深度与位姿条件增强空间Token的几何保真度。给定输入图像 $I_t$，ESM首先通过DINO将其编码为视觉Token $\mathbf{T}^{vis}$，并与可学习相机Token $\mathbf{t}^{cam}$ 拼接后输入空间编码器 $E_{spl}(\cdot)$：

$$ \mathbf{T}^{spl} = E_{spl}([\mathbf{T}^{vis} \parallel \mathbf{t}^{cam}]) $$

该公式通过交叉与自注意力块提取全局3D几何先验。为支持可选3D输入，ESM将归一化深度图 $D_t'$ 与有效掩码 $M_{dpt}$ 拼接后，经卷积层编码为深度Token $\mathbf{T}^{dpt}$，并通过随机条件注入策略（$b_d, b_p \sim \text{Bernoulli}(p)$）在训练时随机决定是否融合深度与位姿，确保模型在无3D输入时仍具备空间推理能力。

### 空间增强动作头

空间增强动作头（Spatial-Enhanced Action Head）旨在解决3D信息与文本Token强行对齐导致的语义干扰问题。该设计借鉴大脑皮层（语义推理）与小脑（运动控制）的分工，将空间Token直接注入动作决策而非VLM主干。具体地，ESM输出的空间Token $\mathbf{T}^{spl}$ 经最大池化压缩为向量 $\mathbf{t}^{spl}$，再通过MLP适配器投影至VLM特征空间得到 $\hat{\mathbf{t}}^{spl}$，最后与VLM提取的语义动作Token $\hat{\mathbf{t}}^{act}$ 通过逐元素相加融合：

$$ \mathbf{t}^{fused} = \hat{\mathbf{t}}^{act} + \hat{\mathbf{t}}^{spl} $$

该公式以极低计算开销实现语义与空间信息的对齐，使动作预测同时依赖高层任务意图与底层几何约束，避免了在VLM内部进行复杂特征对齐的开销与风险。

## 实验评估

实验在CALVIN、SimplerEnv仿真基准及11项真实机器人任务上进行，基线覆盖RT-1-X、OpenVLA、SpatialVLA等主流VLA方法，但缺失3DThinkVLA、3DVLA等最新具身智能SOTA对比。在SimplerEnv Google Robot任务中，FALCON平均成功率达62.9%，显著优于SpatialVLA的55.3%与RT-2-X的46.3%；在Bridge-WidowX任务中，FALCON平均成功率56.3%，领先SpatialVLA的42.7%。

| 基准 | 任务 | FALCON | SpatialVLA | RT-2-X |
|---|---|---|---|---|
| SimplerEnv (Google) | Average | 62.9% | 55.3% | 46.3% |
| SimplerEnv (Google) | Drawer Apple | 41.7% | 0.0% | 3.7% |
| SimplerEnv (WidowX) | Average | 56.3% | 42.7% | - |
| SimplerEnv (WidowX) | Put Spoon | 62.5% | 16.7% | - |

消融实验显示，模态可迁移性设计有效：在CALVIN ABCD→D设置中，RGB-only训练的FALCON在测试时加入深度输入，平均长度从4.08提升至4.09；而RGB-D训练的模型在测试时移除深度，性能保持鲁棒。在ABC→D零样本设置中，RGB-only FALCON加入测试时深度后，平均长度从3.91提升至3.95，匹配全RGB-D训练模型性能，验证了随机条件注入策略的有效性。

评估边界方面，论文未报告LIBERO与RoboTwin基准成绩，无法与领域SOTA（如3DThinkVLA 98.7% LIBERO）直接对比；未提供置信区间，数值比较需谨慎；代码未公开，仅提供项目页面，可复现性受限。

## 关联研究分析

从问题动机看，FALCON与SpatialVLA均旨在解决VLA的3D感知缺失，但SpatialVLA将3D特征嵌入VLM输入空间，依赖大规模具身指令微调恢复对齐，而FALCON将3D处理外置于动作头，通过解耦架构避免对齐破坏。这一差异源于任务特性：SpatialVLA侧重语义-空间联合推理，而FALCON侧重动作执行的几何精度，后者对VLM语义完整性的依赖较低。

从方法设计看，FALCON与PointVLA同属显式3D输入路线，但PointVLA依赖点云等专用传感器，模态可迁移性差；FALCON通过ESM的随机条件注入实现RGB-only与RGB-D的灵活切换，解决了传感器依赖问题。然而，FALCON未探索多视图视频输入下的跨帧空间对应，而领域共识认为多视图一致性是视频级空间推理的核心挑战，这限制了其在动态场景中的长程记忆能力。

## 总结

FALCON要解决的核心矛盾是VLA在缺乏专用3D传感器时的空间推理能力与模态可迁移性之间的冲突。现有方法要么依赖显式3D输入导致部署受限，要么嵌入弱3D线索导致对齐破坏，而FALCON通过解耦架构与随机条件注入，在保留RGB-only鲁棒性的同时支持可选3D输入。该方法在SimplerEnv Google Robot任务中取得62.9%成功率，较SpatialVLA提升7.6%。其边界在于未覆盖LIBERO等长程任务基准，且ESM对动态场景几何精度的依赖未充分验证。当场景包含快速移动物体或复杂遮挡时，ESM提取的空间Token是否仍能保持几何一致性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.17439)