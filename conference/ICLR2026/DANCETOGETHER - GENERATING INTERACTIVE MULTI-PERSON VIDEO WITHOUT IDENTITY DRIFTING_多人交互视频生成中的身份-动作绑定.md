# ICLR2026最新论文 ｜DANCETOGETHER: GENERATING INTERACTIVE MULTI-PERSON VIDEO WITHOUT IDENTITY DRIFTING ｜多人交互视频生成中的身份-动作绑定

研究机构：清华大学、香港理工大学

作者：Junhao Chen、Mingjin Chen、Jianjin Xu 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_59855532)

> 可控视频生成旨在将显式信号转化为连贯动作，但现有系统在多人交互场景下常因控制信号噪声导致身份漂移与外观混淆。本文指出，仅依赖姿态估计无法在遮挡或位置交换时维持个体身份，其切入点在于将稳定的跟踪掩码与富含语义但噪声大的姿态图融合为双模态条件。通过MaskPoseAdapter在扩散去噪的每一步强制绑定“谁”与“如何动”，该方法在自建基准上显著提升了身份一致性与交互连贯性。这一框架在特定数据集上验证了有效性，但其对长序列及开放域泛化的鲁棒性仍存疑。

## 研究背景

当视频生成模型处理多人场景时，控制信号往往存在噪声，导致生成结果中人物身份随时间推移发生漂移。这种漂移源于姿态关键点在遮挡或快速运动下的不确定性，而传统的逐帧合成加时序平滑范式无法在生成过程中维持个体身份的持久性。为解决此问题，需要一种机制在扩散模型的每一步去噪中，将身份信息与动作信号紧密耦合，而非仅在最终输出时进行校正。

可控视频生成领域的主流路线依赖于单模态条件，如文本或单一姿态图，这在单人场景中表现良好，但在多人交互中失效。现有方法如Animate Anyone和Champ主要基于单人舞蹈数据集训练，缺乏对多人位置交换和复杂交互的建模能力。当演员交叉或遮挡时，这些方法会出现严重的外观混淆，即一个人的特征“泄漏”到另一个人身上。DanceTogether针对这一瓶颈，提出在扩散过程中显式绑定身份与动作，通过融合掩码和姿态信号，确保每个个体的身份在数百帧内保持一致，同时忠实遵循噪声控制信号。

## 核心方法

### 方法参照系

本文基于StableAnimator架构，该架构使用16帧潜空间UNet，通过冻结的VAE编码器和可训练的适配器处理参考图像与姿态条件。与标准流程的关键差异在于，本文引入了针对多人场景的双模态条件融合机制，而非单一姿态输入。

### MaskPoseAdapter：双模态条件融合

MaskPoseAdapter解决了姿态关键点在遮挡下无法区分个体的问题。对于每个人$i$，姿态图$\mathbf{P}_i$和掩码$\mathbf{M}_i$分别通过编码器生成特征$\mathbf{f}_i^{pose}$和$\mathbf{f}_i^{mask}$。核心创新在于门控融合机制，通过可学习的门控权重自适应地平衡姿态与掩码的贡献：

$$ \mathbf{f}_i = \lambda \cdot w_i^{pose} \odot \mathbf{f}_i^{pose} + (1 - \lambda) \cdot w_i^{mask} \odot \mathbf{f}_i^{mask} + \text{residual} $$

其中$\lambda \approx 0.8$偏向姿态，当姿态模糊时增强掩码权重。这种设计使得网络在姿态噪声大时依赖稳定的掩码定位身份，在掩码缺失时依赖姿态捕捉运动细节，从而在每一步去噪中维持身份-动作的精确对齐。

### MultiFace Encoder：多身份紧凑注入

MultiFace Encoder解决了单身份编码在多主体场景下的扩展性问题。每个ArcFace嵌入$\mathbf{e}_i^{id}$通过两层MLP投影为$K=4$个令牌，再经FacePerceiver精炼。所有个体的令牌拼接为$\mathbf{T} \in \mathbb{R}^{(NK) \times 768}$，调制UNet的交叉注意力层。相比重复使用单身份编码器，这种共享权重设计减少了参数量，并允许模型学习身份间的关系，确保在位置交换时身份不混淆。

## 实验评估

实验在DanceTogEval-100上进行，包含100个双人交互视频。基线覆盖Animate Anyone、Champ、StableAnimator等，但缺乏DiT-based最新基线。主结果显示，DanceTogether在身份一致性上显著优于最强基线StableAnimator+Swing，HOTA从71.35提升至83.94，IDF1从82.53提升至89.59。

| 方法 | HOTA | IDF1 | MOTA | MPJPE2D |
|---|---|---|---|---|
| StableAnimator w. Dataswing | 71.35 | 82.53 | 73.89 | 1555.16 |
| DanceTog w. Datafull+DataPairFS | 83.94 | 89.59 | 79.80 | 492.24 |

消融实验表明，MaskPoseAdapter和PairFS-4K数据集对性能提升贡献最大。移除MaskPoseAdapter导致HOTA下降约5%，表明双模态融合对身份保持至关重要。PairFS-4K的加入进一步提升了MOTA，说明大规模双人数据对交互连贯性有正向影响。

评估边界方面，指标涵盖MOT、姿态误差和视频质量，但缺乏长视频（>100帧）的测试。可复现性上，论文提供了训练细节（8 A100 GPUs, 20 epochs），但未公开代码。

## 关联研究分析

从问题动机看，DanceTogether与CameraCtrl等相机控制方法不同，后者关注3D空间解耦，而本文聚焦2D像素空间中的身份绑定。这一差异源于任务特性：相机控制需几何精度，而多人交互需语义身份保持。从方法设计看，本文与StableAnimator共享UNet骨干，但MultiFace Encoder的共享权重设计是本文特有，旨在处理多身份关系。Champ使用SMPL引导，但仅生成单人，本文通过掩码融合避免了这一局限。

## 总结

DanceTogether解决的核心矛盾是多人交互中身份漂移与动作噪声的冲突。其切入点在于将稳定的掩码与噪声姿态融合，通过MaskPoseAdapter在扩散过程中强制绑定身份与动作。实验证明，该方法在HOTA和MPJPE2D上显著优于基线，HOTA提升12.6，MPJPE2D降低69%。边界在于，实验仅在100帧短片段上进行，且依赖自建数据集，缺乏开放域泛化验证。当支持集增大到更长的交互序列时，身份绑定的持久性是否仍能维持，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_59855532)