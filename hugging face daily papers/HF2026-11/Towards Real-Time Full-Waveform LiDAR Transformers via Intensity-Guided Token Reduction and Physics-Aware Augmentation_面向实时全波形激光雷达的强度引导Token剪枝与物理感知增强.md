# HuggingFace最新推荐论文 ｜Towards Real-Time Full-Waveform LiDAR Transformers via Intensity-Guided Token Reduction and Physics-Aware Augmentation ｜面向实时全波形激光雷达的强度引导Token剪枝与物理感知增强

研究机构：日本庆应义塾大学

作者：Kotaro Oishi、Kazuma Ikeda、Ryosei Hara 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2611.07613)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2611.07613)

> 导读 全波形激光雷达（Full-waveform LiDAR, FWL）通过记录每个像素的完整时间强度直方图，保留了多路径回波和弱信号等丰富反射特征，但庞大的数据量导致Transformer模型推理延迟远超实时要求，且公开数据稀缺导致模型在未见场景泛化能力不足。现有图像Token剪枝方法假设信息在二维空间均匀分布，盲目丢弃FWL中稀疏的高强度目标信号，而常规数据增强破坏了ToF波形结构与视锥几何。本文提出FWL-ToPM，利用FWL特有的强度稀疏性，通过基于强度的Token剪枝剔除低强度背景，并结合空间填充曲线序列化的Token合并保留关键波形内容；同时提出FWLAug，在保留ToF波形结构和视锥几何的前提下进行数据增强。该工作确立了首个实时FWL Transformer，在Ghost-FWL基准上实现8倍加速与9点F1提升，但其剪枝策略对低反射率物体的潜在误删风险及单传感器平台限制仍需进一步验证。

## 研究背景

当自动驾驶系统面对玻璃、水等低反射率物体或雾、雨等恶劣天气时，传统LiDAR仅记录脉冲峰值强度，无法捕捉复杂反射特性，导致鬼影和噪声点云，严重干扰目标检测与SLAM。全波形激光雷达（FWL）通过记录每个像素的完整时间强度直方图，保留了多路径回波和弱信号，为鬼影检测和雾天鲁棒重建提供了物理基础。然而，FWL数据量远大于点云，且绝大部分为低强度背景噪声，直接应用Vision Transformer (ViT) 会导致计算成本激增，现有FWL Transformer在高端GPU上推理速度仍远低于实时要求。

在FWL Transformer的实际部署中，计算效率与泛化能力构成双重瓶颈。一方面，现有图像Token剪枝方法（如DynamicViT、ToMe）假设信息在二维空间广泛分布，无法适应FWL数据中高强度信号稀疏分布的特性，盲目剪枝会丢弃编码目标反射的关键Token。另一方面，公开FWL数据稀缺，玻璃等少数类样本不足导致模型过拟合主导类，而标准图像和点云增强方法忽略了ToF波形结构和视锥几何，扭曲了每条射线的波形。本文针对这两个被忽略的物理结构特性，提出强度引导的Token剪枝与物理感知增强框架，以同时解决实时推理与跨场景泛化问题。

## 核心方法

### 方法参照系

FWL-ToPM以ViT为骨干网络进行体素级分类，输入FWL数据 $V \in \mathbb{R}^{H \times W \times T}$ 被划分为3D补丁，通过3D卷积投影为补丁Token，经Transformer编码器提取特征后由线性解码器输出类别对数。与标准ViT处理均匀分布图像不同，FWL数据中高强度信号稀疏分布，低强度背景占据绝大多数，导致均匀Token化产生大量无信息Token，稀释特征表示并增加计算负担。本文在Token化与自注意力计算之间引入强度引导的剪枝与合并机制，以适配FWL的物理结构。

### 强度引导Token剪枝与空间感知合并

FWL数据中高强度峰值稀疏分布，低强度区域多为噪声。本文提出基于强度的Token剪枝，评估每个补丁的最大信号强度 $m_i$，按升序排序后移除底部 $\rho_{low}$ 比例的补丁，仅将高强度补丁 $P_{high}$ 输入编码器。训练时排除被剪枝区域的损失，推理时将其预测为噪声标签。该剪枝不修改网络权重，可直接应用于预训练模型。

剪枝后 $P_{high}$ 仍包含冗余Token，且形成稀疏不规则子集，导致现有基于固定网格的Token合并方法失效。本文引入空间填充曲线（Morton order）将 $P_{high}$ 序列化为1D序列，保持3D空间邻近性，随后按等间隔选择目标Token（dst tokens），计算源Token（src tokens）与dst的余弦相似度，按合并比例 $\rho_m$ 将高相似度src Token与dst Token平均合并。

$$
\text{Merge}(src, dst) = \frac{1}{k+1} \left( \sum_{j=1}^{k} src_j + dst \right)
$$

该公式表示将 $k$ 个高相似度源Token与目标Token进行平均聚合。通过空间填充曲线序列化，合并操作在稀疏Token序列中仍能保持空间分布均匀性，避免局部区域过度聚合，从而在降低自注意力计算复杂度的同时保留目标相关波形内容。

### 物理感知数据增强

针对FWL数据稀缺与少数类过拟合问题，本文提出FWLAug，包含FWLShiftMix与FWLCutMix两种增强策略，均严格保留ToF波形结构与视锥几何。FWLShiftMix将物体沿LiDAR射线方向平移 $\Delta d \sim U(-3, 15)$ 米，计算平移后点 $r'_{h,w} = r_{h,w} + \Delta d u_{h,w}$ 并重新投影至范围视图，沿 $T$ 轴平移波形以匹配新位置。平移产生的空白区域 $\Omega_{blank}$ 由另一场景的含玻璃区域 $\Omega_{src}$ 填充，保留每条射线的波形结构。

FWLCutMix扩展CutMix至FWL数据，从源样本 $V_{src}$ 中优先选择含少数类（玻璃）的裁剪区域 $\Omega_{src}$，粘贴至目标样本 $V_{dst}$ 的随机位置。裁剪尺寸由混合比例 $\lambda$ 决定：

$$
\ell_H = \lfloor H \sqrt{1 - \lambda} \rfloor, \quad \ell_W = \lfloor W \sqrt{1 - \lambda} \rfloor
$$

该公式定义了裁剪区域的高度和宽度。沿 $T$ 轴完整粘贴波形，确保时间结构不被破坏。这两种增强策略通过优先采样玻璃区域缓解类别不平衡，同时通过3D空间操作保持物理一致性，提升模型对未见场景的泛化能力。

## 实验评估

实验在Ghost-FWL数据集上进行，输入尺寸为 $(168 \times 200 \times 300)$，评估指标为排除噪声类的平均F1分数（F1-mean）和每秒推理帧数（FPS）。基线包括FWL专用方法（Scheuble et al., 2021; Ikeda et al., 2024）及图像Token剪枝方法（DynamicViT, ToMe）。FWL-ToPM在F1-mean达到0.592，推理速度53.2 FPS，较前作SOTA（Ikeda et al., 2024）提升约9点F1并实现8倍加速。

| Method | Pruning | Merging | F1-mean | FPS |
| :--- | :---: | :---: | :---: | :---: |
| Scheuble et al. [31] | – | – | 0.497 | 1.97 |
| Ikeda et al. [10] | – | – | 0.503 | 6.54 |
| Ours w/o FWL-ToPM | – | – | 0.555 | 2.01 |
| DynamicViT [30] | ✓ | – | 0.480 | 20.0 |
| Ours w/Pruning | ✓ | – | 0.591 | 20.3 |
| ToMe [2] | – | ✓ | 0.543 | 5.24 |
| Ours w/Merging | – | ✓ | 0.565 | 18.0 |
| Ours w/FWL-ToPM | ✓ | ✓ | 0.592 | 53.2 |

FWL-ToPM的剪枝与合并组件均优于图像基线，且组合使用达到最佳F1-FPS权衡。消融实验表明，单独剪枝在20 FPS时保持0.591的F1，但进一步剪枝至80 FPS时精度大幅下降；单独合并仅达18 FPS。两者结合通过剪枝移除背景、合并聚合有效信息，实现50 FPS以上的实时性能。

| Method | FWLCutMix | FWLShiftMix | Ghost-FWL F1-mean | Ghost-FWL Glass | OOD F1-mean | OOD Glass |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Ours w/o Aug | ✗ | ✗ | 0.592 | 0.352 | 0.406 | 0.491 |
| Ours w/ FWLAug | ✗ | ✓ | 0.622 | 0.376 | 0.425 | 0.494 |
| Ours w/ FWLAug | ✓ | ✓ | 0.617 | 0.385 | 0.452 | 0.575 |
| Ours w/ FWLAug | ✓ | ✗ | 0.586 | 0.315 | 0.434 | 0.606 |

FWLAug在OOD测试集上带来4.6点F1提升，玻璃类提升8.4点。FWLShiftMix对域内精度贡献更大，而两者结合驱动OOD性能提升，表明其互补效应。评估协议局限在于OOD测试集仅500帧，且未进行跨传感器平台验证，系统级延迟（含预处理）未纳入评估。

## 关联研究分析

从问题动机看，Ghost-FWL（Ikeda et al., 2024）确立了FWL鬼影检测任务与数据格式，但其Transformer架构未考虑FWL数据的强度稀疏性，导致推理速度仅6.54 FPS。本文的强度引导剪枝直接针对FWL直方图的物理特性，而Ghost-FWL采用均匀Token化，这一差异源于对FWL数据分布假设的不同：前者假设高强度信号稀疏且关键，后者假设信息均匀分布。

从方法设计看，ToMe（Bolya et al., 2023）通过二分图匹配合并相似Token，假设Token在密集网格中均匀分布。本文的合并机制在剪枝后的稀疏不规则子集上运行，必须引入空间填充曲线序列化以恢复空间邻近性，否则固定网格采样会因区域无Token而失效。这一差异揭示了通用Token合并方法在稀疏3D数据上的适用性盲区，查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

本文针对FWL Transformer实时推理与泛化瓶颈，抓住FWL数据强度稀疏性与ToF波形物理结构这两个被现有方法忽略的特性，提出强度引导Token剪枝与物理感知增强框架。FWL-ToPM通过剪枝低强度背景与空间感知合并，在Ghost-FWL上实现53.2 FPS与0.592 F1-mean，较前作提升8倍速度与9点精度；FWLAug在OOD测试集上提升4.6点F1。该工作确立了首个实时FWL Transformer，但其边界在于剪枝策略可能误删低反射率物体的弱信号，且FWLAug未建模距离依赖的强度衰减与跨场景反射路径一致性。当支持集增大到 5-shot 时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2611.07613)