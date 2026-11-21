# CVPR2026最新论文 ｜GroundVTS: Visual Token Sampling in Multimodal Large Language Models for Video Temporal Grounding ｜查询引导视觉Token采样

研究机构：复旦大学、同济大学

作者：Rong Fan、Kaiyan Xiao、Minghao Zhu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.02093)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.02093)

> 视频时间定位（VTG）旨在根据自然语言查询精准定位视频中的事件片段，但现有视频大语言模型（Vid-LLMs）依赖均匀帧采样，导致关键时序线索在输入端被稀释或丢失。本文切入点在于将采样粒度从帧级细化至Token级，通过查询引导的视觉Token采样（VTS）模块在LLM前动态筛选相关视觉特征。该方法结合渐进式优化策略，使模型适应非均匀Token分布，在Charades-STA上实现50.1 mIoU。其价值在于验证了输入端细粒度筛选对定位精度的提升，但缺乏强化学习优化，性能上限受限于监督微调（SFT）的泛化能力。

## 研究背景

视频时间定位要求模型在长序列中识别特定事件的时间边界，这依赖于视觉编码器输出的时空特征与文本查询的语义对齐。然而，Transformer架构的上下文窗口限制迫使模型采用均匀帧采样，这种策略将计算预算平均分配至所有时间步，当查询相关事件稀疏时，关键帧的视觉Token被大量无关背景Token稀释，导致模型无法捕捉细粒度动态。

主流Vid-LLMs如Qwen2.5-VL和InternVL3.5通过扩展上下文窗口或通用Token压缩缓解内存瓶颈，但忽略了采样策略对时序推理的结构性影响。现有查询引导采样方法（如基于CLIP的帧筛选）仅在视频输入阶段进行粗粒度过滤，依赖外部编码器且无法保留帧内空间细节，限制了定位精度。本文针对这一盲区，提出在视觉编码器后、LLM前进行Token级筛选，直接解决“关键视觉Token稀释”问题，而非仅解决“关键帧丢失”问题。

## 核心方法

### 方法参照系

标准Vid-LLM流程为：视频帧→视觉编码器→多模态投影→LLM。本文问题与该通用流程的关键差异在于，传统流程假设所有视觉Token对查询同等重要，而VTG任务中仅少数Token包含定位线索，需在投影后、LLM前引入查询感知的筛选机制。

### 查询引导Token评分

VTS模块首先将投影后的视觉嵌入$V$与查询嵌入$Q$投影至低维子空间，通过温度缩放的点积计算相似度：

$$s_i = \text{softmax}\left(\frac{v_i^\top q'}{\tau}\right)$$

其中$\tau$控制分布锐度。该设计动机在于解决帧级筛选无法区分帧内空间相关性的问题，Token级评分能精确定位查询相关的时空区域，避免无关背景干扰。

### 可微分Top-K选择

为保留Top-K个最相关Token，VTS采用Gumbel-Softmax松弛实现端到端训练：

$$z_i = \frac{\exp((\log s_i + g_i)/\tau_g)}{\sum_j \exp((\log s_j + g_j)/\tau_g)}$$

前向传播使用硬Top-K算子，反向传播通过连续松弛$z_i$传递梯度。该机制解决了硬选择不可微导致无法联合优化的问题，使VTS模块能与LLM协同训练，适应非均匀Token分布。

## 实验评估

实验在Charades-STA、ActivityNet-Captions和QVHighlights上评估时刻检索（MR）与高光检测（HD）任务。基线覆盖Vid-LLMs（Qwen2.5-VL、InternVL3.5）及经典VTG方法（TimeChat、NumPro），但缺失LongVA等Token压缩方法的对比。

| 方法 | Charades-STA mIoU | ActivityNet mIoU | QVHighlights R1@0.5 |
| :--- | :--- | :--- | :--- |
| Qwen2.5VL-7B-G | 31.7 | 26.7 | 2.4 |
| GroundVTS-Q | 50.1 | 36.0 | 12.3 |
| InternVL3.5-8B-G | 39.4 | 24.5 | 15.0 |
| GroundVTS-I | 41.6 | 25.7 | 40.7 |

GroundVTS-Q在Charades-STA上较基线提升18.4点mIoU，但低于领域综述中TempR1的59.8 mIoU，差距9.7点。

消融实验显示，移除位置编码导致mIoU从50.1降至9.5，证实时序位置信息对非均匀采样的必要性。采样策略对比中，Token级VTS较帧级选择提升8.5点mIoU，随机采样优于均匀采样，暗示随机丢弃可能起到数据增强作用。

评估边界方面，论文未报告置信区间，且未对比RL方法，无法隔离采样策略与优化算法的贡献。代码已开源，但VTS模块的超参数（如$\tau$、$\rho$）敏感性未充分分析。

## 关联研究分析

从问题动机看，GroundVTS与ViKey均旨在显式注入时序信息，但ViKey通过像素空间插入帧编号解决模态差异，而GroundVTS通过Token筛选解决信息稀疏问题。两者差异源于任务特性：ViKey适用于需要全局时序感知的问答任务，GroundVTS适用于需要局部精确定位的VTG任务。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

从方法设计看，GroundVTS与LongVA同属长视频高效推理路线，但LongVA侧重通用压缩以降低计算成本，GroundVTS侧重查询引导的细粒度筛选以提升定位精度。这一差异反映了“效率”与“精度”的权衡：LongVA适用于长视频通用理解，GroundVTS适用于高精度定位场景。两者可互补，但论文未验证组合效果。

## 总结

本文核心矛盾在于均匀采样导致关键视觉Token稀释，现有帧级筛选无法解决帧内空间相关性缺失。GroundVTS通过Token级查询引导采样与可微分Top-K选择，在LLM前动态保留相关特征，结合渐进式优化策略实现稳定训练。实验证明其在Charades-STA上实现50.1 mIoU，较基线提升18.4点，但低于RL方法TempR1的59.8 mIoU。边界在于缺乏强化学习优化，SFT在复杂时序推理上易过拟合，且未验证与RL方法的组合效果。当支持集增大时，Token级筛选的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.02093)