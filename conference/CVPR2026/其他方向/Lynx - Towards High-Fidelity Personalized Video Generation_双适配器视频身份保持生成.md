# CVPR2026最新论文 ｜Lynx: Towards High-Fidelity Personalized Video Generation ｜双适配器视频身份保持生成

作者：Shen Sang、Tiancheng Zhi、Tianpei Gu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.15496)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.15496)

> 个性化视频生成旨在从单张参考图锁定人物身份，同时允许文本控制动作与场景，但现有方法常陷入身份漂移或复制粘贴伪影的困境。Lynx 指出仅注入全局身份嵌入不足以保留高频细节，且直接拼接参考特征会破坏时序动态，其切入点在于将身份语义与视觉细节解耦至两个独立适配器。该方法基于 Wan2.1 扩散 Transformer，通过 ID-adapter 注入 ArcFace 令牌，Ref-adapter 注入冻结骨干提取的全层 VAE 特征，实现了高保真身份保持与强文本对齐的平衡。该框架在 800 个测试用例上刷新了人脸相似度纪录，但缺乏多身份场景验证，且依赖大规模数据增强，其泛化边界尚待考察。

## 研究背景

视频生成模型需同时处理空间细节与时间动态，这要求骨干网络具备强大的时空建模能力。扩散 Transformer（DiT）通过时空自注意力联合建模视觉令牌，解决了早期 U-Net 架构在长视频时序一致性上的不足，成为当前视频基础模型的主流选择。然而，DiT 的通用生成先验与特定人物身份特征存在空间耦合，直接微调易导致过拟合，而仅注入全局身份嵌入则丢失了纹理等高频细节，导致生成视频出现身份漂移或僵化。

个性化视频生成的核心矛盾在于身份保真度与动作自然度的权衡。早期图像域方法如 DreamBooth 依赖参数微调，计算开销大且难以扩展至视频；IP-Adapter 等免微调方法通过交叉注意力注入身份嵌入，虽提升了效率，但在视频时序中易出现细节丢失。现有视频方法如 SkyReels-A2 常采用复制粘贴机制，虽保真度高但严重损害文本可控性。Lynx 的切入点在于识别出“全局身份嵌入”与“局部视觉细节”在特征空间中的异质性，主张通过双路径注入解耦这两类信号，从而在保持 DiT 骨干通用性的同时实现精准身份控制。

## 核心方法

### 方法参照系

本文问题属于免微调个性化视频生成，标准流程通常仅通过交叉注意力注入单一身份嵌入。本文的关键差异在于引入了第二个适配器，将参考图的密集视觉特征与全局身份语义分离处理，以解决单一嵌入在高频细节保留上的失效。

### ID-adapter：身份语义注入

ID-adapter 负责注入全局身份语义，解决此前方法中身份特征与文本语义耦合导致的可控性下降问题。参考人脸经 ArcFace 编码器提取 512 维向量，通过 Perceiver Resampler 映射为 16 个 5120 维令牌，并与 16 个寄存器令牌拼接。该过程可形式化为：

$$ \mathbf{z}_{id} = \text{Resampler}(\mathbf{f}_{arc}) \oplus \mathbf{r}_{reg} $$

其中 $\mathbf{f}_{arc}$ 为 ArcFace 特征，$\mathbf{r}_{reg}$ 为寄存器令牌。$\mathbf{z}_{id}$ 随后与视觉令牌进行交叉注意力，将身份信号注入主干。此设计利用了 Resampler 的压缩能力，将高维身份信息转化为紧凑令牌，避免了直接注入原始向量导致的维度不匹配与计算冗余。

### Ref-adapter：视觉细节注入

Ref-adapter 旨在弥补 ID-adapter 在高频细节上的缺失，解决直接拼接参考特征导致的时序动态破坏问题。参考图像通过预训练 VAE 编码器提取密集特征，并送入冻结的骨干网络副本（噪声水平为 0，文本提示为 "image of a face"），获取所有 DiT 块的中间激活。这些激活作为参考令牌，通过独立的交叉注意力模块融合至生成过程：

$$ \mathbf{h}_{ref}^{(l)} = \text{CrossAttn}(\mathbf{h}_{visual}^{(l)}, \text{FrozenBackbone}(\mathbf{x}_{ref})) $$

其中 $\mathbf{h}_{visual}^{(l)}$ 为第 $l$ 层视觉令牌，$\mathbf{x}_{ref}$ 为参考图像。该设计借鉴了 ReferenceNet 的思路，通过冻结骨干提取全层特征，确保空间细节在去噪过程中被逐层保留，而非仅依赖浅层特征，从而增强了身份保真度。

## 实验评估

实验在包含 40 个主体和 20 个无偏提示的基准上进行，共 800 个测试用例。基线覆盖 SkyReels-A2、VACE、Phantom 等近期 SOTA 方法，但缺失图像域经典方法（如 InstantID）的直接视频对比，且未包含多身份场景测试。

| 模型 | Face Resemblance (facexlib) | Face Resemblance (insightface) | Face Resemblance (in-house) |
| :--- | :--- | :--- | :--- |
| SkyReels-A2 | 0.715 | 0.678 | 0.725 |
| VACE | 0.594 | 0.548 | 0.615 |
| Phantom | 0.664 | 0.659 | 0.689 |
| MAGREF | 0.575 | 0.510 | 0.591 |
| Stand-In | 0.611 | 0.576 | 0.634 |
| **Lynx** | **0.779** | **0.699** | **0.781** |

Lynx 在三个独立评估器上均取得最高人脸相似度，其中 facexlib 得分 0.779，较次优的 SkyReels-A2（0.715）提升 0.064。SkyReels-A2 虽排名第二，但其依赖复制粘贴机制导致文本对齐能力弱，在 Prompt Following 指标上仅得 0.471，远低于 Lynx 的 0.722。

| 模型 | Prompt Following | Aesthetic | Motion Naturalness | Video Quality |
| :--- | :--- | :--- | :--- | :--- |
| SkyReels-A2 | 0.471 | 0.704 | 0.824 | 0.870 |
| VACE | 0.691 | 0.846 | **0.851** | 0.935 |
| Phantom | 0.690 | 0.825 | 0.828 | 0.888 |
| MAGREF | 0.612 | 0.787 | 0.812 | 0.886 |
| Stand-In | 0.582 | 0.807 | 0.823 | 0.926 |
| **Lynx** | **0.722** | **0.871** | 0.837 | **0.956** |

Lynx 在 Prompt Following、Aesthetic 和 Video Quality 三项指标上领先，其中 Video Quality 得分 0.956，显著高于 VACE 的 0.935。VACE 在 Motion Naturalness 上以 0.851 领先，反映其较强的时序建模能力，但 Lynx 的 0.837 与之差距微小，表明双适配器设计未牺牲动作自然度。

评估协议依赖 Gemini-2.5-Pro API 进行主观质量评分，缺乏标准化置信区间报告，且基准规模（800 例）较小，可能限制统计显著性。代码未公开，超参数细节（如 Resampler 初始化具体 checkpoint）未完全披露，可复现性受限。

## 关联研究分析

从方法设计看，Lynx 与 InstantID 共享 Perceiver Resampler 用于身份令牌生成，但 InstantID 仅用于图像域且依赖 ControlNet 进行输入解耦，而 Lynx 将 Resampler 扩展至视频域并引入 Ref-adapter 处理密集特征。这一差异源于视频任务对时序动态的更高要求：InstantID 的 ControlNet 在视频时序中易引入伪影，而 Lynx 的冻结骨干特征注入更适配 DiT 的时空自注意力结构。

从问题动机看，Lynx 与 WildActor 均关注视频身份保持，但 WildActor 依赖 Actor-18M 大规模多视角数据集提供密集监督，解决身份漂移问题；Lynx 则依赖单图参考与数据增强（如 X-Nemo 表情增强、LBM 重光照），解决细节丢失问题。WildActor 的数据驱动路线在数据充足时更鲁棒，而 Lynx 的适配器路线在数据稀缺时更具灵活性。两者在极端姿态下的鲁棒性对比缺失，Lynx 未测试侧脸或严重遮挡场景，其单图参考在 3D 结构变化下的失效边界尚不明确。

## 总结

Lynx 旨在解决个性化视频生成中身份保真度与动作自然度的矛盾，现有方法因单一身份嵌入丢失细节或复制粘贴损害可控性而失效。本文通过 ID-adapter 注入 ArcFace 令牌与 Ref-adapter 注入冻结骨干 VAE 特征，解耦了身份语义与视觉细节，在 800 个测试用例上实现了 0.779 的 facexlib 人脸相似度与 0.956 的视频质量得分。其边界在于基准规模较小且缺乏多身份场景验证，单图参考在极端姿态下的鲁棒性未受测试。当参考图像包含严重遮挡或极端侧脸时，冻结骨干提取的 VAE 特征是否仍能保留足够的身份线索，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.15496)