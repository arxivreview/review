# ICLR2026最新论文 ｜Syncphony: Synchronized Audio-to-Video Generation with Diffusion Transformers ｜音画同步视频生成

研究机构：韩国延世大学

作者：Jibin Song、Mingi Kwon、Jaeseok Jeong 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.21893)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.21893)

> 音频信号天然携带时间轴信息，是控制视频运动节奏的理想条件，但现有Audio-to-Video (A2V) 方法依赖间接映射或浅层时序建模，导致细粒度同步失效。本文切入点在于利用预训练视频骨干的强时序能力，并通过直接交叉注意力注入音频特征。具体做法是结合运动感知损失与推理时音频同步引导，实现高帧率下的精准对齐。该方法在同步精度上显著优于基线，但其对运动强度与音频信号非严格一一对应的假设，在复杂交互场景中是否依然成立存疑。

## 研究背景

视频生成模型在视觉保真度上已趋于成熟，但文本提示缺乏显式时间戳，图像条件仅呈现静态快照，均无法精确指定“何时”发生何种运动。音频信号与视频共享同一时间轴，其波形中的峰值与节奏直接对应物理世界的动态事件，如狗吠的频率或保龄球撞击的瞬间。然而，将音频作为条件输入时，模型需解决的核心难题是如何将离散的时间线索映射为连续的视频潜变量运动，且这种映射必须保持毫秒级的时序精度。

主流A2V路线存在两类瓶颈：一是间接映射，如TempoTokens将音频投影至文本空间，丢失了复杂的时序结构；二是浅层时序建模，如AVSyncD基于图像骨干添加时间层，受限于低分辨率与有限数据，导致生成视频出现闪烁与饱和伪影。Syncphony的切入点在于摒弃间接映射，直接利用预训练自回归DiT骨干（Pyramid Flow）的强时序建模能力，并在架构中嵌入音频交叉注意力层，从而在保持高分辨率视觉质量的同时，实现音频驱动的运动同步。

## 核心方法

### 方法参照系

本文基于预训练的自回归扩散Transformer（Pyramid Flow Video），该架构通过迭代去噪生成视频潜变量块。与标准Text-to-Video (T2V) 流程的关键差异在于，本文在Transformer后期块中插入音频交叉注意力层，将音频特征直接注入视觉潜变量序列，而非通过文本中介。

### 运动感知损失

常规均方误差（MSE）损失对所有时空区域一视同仁，导致模型在静态区域表现良好时，即使动态区域时序错位，整体误差仍较低，从而削弱了对音频-运动对齐的学习。Syncphony引入运动感知损失，通过放大高运动区域的误差信号，迫使模型关注动态事件的时序精度。该损失函数定义为：

$$ \mathcal{L}_{motion} = \frac{1}{N} \sum_{l=1}^{N} \left( \| \hat{\mathbf{z}}_l - \mathbf{z}_l^{GT} \|^2 + \lambda \cdot \| \hat{\mathbf{z}}_l - \mathbf{z}_l^{GT} \| \odot \| \mathbf{z}_l^{GT} - \mathbf{z}_{l-1}^{GT} \| \right) $$

其中 $\lambda=1$，第二项通过真值帧间差异（运动强度）加权预测误差。这一设计避免了直接依赖音频信号强度作为监督，因为运动往往先于或滞后于声音（如挥锤动作），从而允许模型学习更自然的非严格对齐模式。

### 音频同步引导

在推理阶段，音频线索有时微弱，模型难以判断是否应反映在运动中。Audio Sync Guidance (ASG) 通过对比全模型与“去同步”模型（跳过音频交叉注意力层）的输出差异，强化音频影响。引导公式为：

$$ \hat{\epsilon}_{guided} = \epsilon_{\theta}(\mathbf{z}^{[t]}) + w \cdot \left( \epsilon_{\theta}(\mathbf{z}^{[t]}) - \epsilon_{off-sync}(\mathbf{z}^{[t]}) \right) $$

其中 $w$ 为引导强度。该机制无需额外训练，通过隔离同步组件，在保持视觉保真度的同时，显著提升运动与音频事件的时序一致性。

## 实验评估

实验在AVSync15（1500视频，15类动作）和TheGreatestHits（鼓击数据集）上进行，基线包括I2V模型Pyramid Flow、A2V模型TempoTokens及AVSyncD。缺失与最新SOTA A2V模型（如LTX-2）的直接对比，限制了横向可比性。

| 模型 | 数据集 | FID↓ | FVD↓ | CycleSync↑ |
| :--- | :--- | :--- | :--- | :--- |
| AVSyncD | AVSync15 | 9.2 | 491.5 | 16.38 |
| Syncphony | AVSync15 | 8.5 | 293.1 | 16.48 |
| Syncphony | TheGreatestHits | 6.7 | 166.2 | 16.18 |
| Groundtruth | TheGreatestHits | - | - | 15.99 |

Syncphony在AVSync15上FVD较AVSyncD降低40.4%，CycleSync提升0.10；在TheGreatestHits上CycleSync甚至超过真值（16.18 vs 15.99），归因于生成视频运动更清晰且无背景噪声干扰。

| 变体 | FID↓ | FVD↓ | CycleSync↑ |
| :--- | :--- | :--- | :--- |
| w/o Motion-aware Loss | 8.4 | 305.9 | 15.18 |
| w/ ASG (w=2) | 8.5 | 293.1 | 16.48 |
| w/ ASG (w=4) | 8.7 | 298.3 | 16.26 |

消融显示，移除运动感知损失导致CycleSync下降1.30，验证其对时序精度的关键作用。ASG在 $w=2$ 时达到最优平衡，$w=4$ 时虽同步略升，但FVD回升至298.3，表明过强引导导致运动夸张，损害视觉真实性。

评估指标CycleSync基于Video-to-Audio重建，克服了RelSync等指标需降采样至6fps的局限。局限在于：仅使用4块RTX 3090训练，未报告推理延迟；数据集规模较小（450/732 clips），且未覆盖长视频叙事场景。

## 关联研究分析

从方法设计看，Syncphony与AVSyncD的核心差异在于骨干网络选择。AVSyncD基于Stable Diffusion图像骨干，时序建模能力受限，导致闪烁；Syncphony采用Pyramid Flow视频骨干，天然具备高分辨率时序一致性。这一差异并非算法创新，而是架构继承的结果，暗示A2V性能瓶颈可能更多源于骨干时序能力而非条件注入方式。

从问题动机看，Syncphony与TempoTokens代表直接映射与间接映射的分野。TempoTokens将音频投影至文本空间，依赖T2V模型的语义理解，但丢失了音频的精细时序结构；Syncphony通过交叉注意力直接注入音频特征，保留了时间轴信息。然而，Syncphony未使用LLM/VLM进行语义规划，在复杂多主体交互场景中，仅靠音频线索是否足以解决语义歧义（如“狗吠”是兴奋还是恐惧），论文未给出回答。

## 总结

Syncphony旨在解决音频驱动视频生成中的细粒度时序对齐问题，其切入点在于利用预训练视频骨干的强时序能力，并通过运动感知损失与ASG强化音频-运动绑定。实验证明，该方法在AVSync15上FVD降至293.1，CycleSync达16.48，显著优于AVSyncD。其边界在于假设运动强度与音频信号存在可学习的对应关系，且仅在短时长（5秒）单事件场景中验证。当音频包含重叠声源或运动与声音存在长时滞后时，运动感知损失的加权机制是否仍能准确定位同步点，尚待验证。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.21893)