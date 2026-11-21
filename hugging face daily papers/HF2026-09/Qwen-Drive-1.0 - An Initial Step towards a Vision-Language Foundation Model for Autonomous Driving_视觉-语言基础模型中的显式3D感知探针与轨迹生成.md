# HuggingFace最新推荐论文 ｜Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving ｜视觉-语言基础模型中的显式3D感知探针与轨迹生成

研究机构：华中科技大学

作者：Xin Zhou、Zongchuang Zhao、Zhibo Yang 等 16 人

论文原文见 [arXiv](https://arxiv.org/abs/2609.00111)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.00111)

> 端到端自动驾驶（E2E）旨在通过单一网络直接映射传感器输入至控制信号，以消除模块化流水线中的信息瓶颈。现有视觉-语言-动作（VLA）模型依赖文本监督适配驾驶任务，导致3D空间表征缺失与通用知识灾难性遗忘。本文在预训练视觉-语言模型（VLM）外挂显式鸟瞰图（BEV）感知头与流匹配规划专家，统一3D感知、问答与轨迹规划。该架构在NAVSIM闭环规划中取得90.7分，但开环3D感知精度低于专用检测器，验证了通用性与空间精度的权衡。

## 研究背景

当VLM处理多视角驾驶图像时，视觉token序列缺乏显式的视角与时间戳标识，导致模型无法准确定位时空信息。为解决此问题，需引入视角标签与帧标签进行序列化。然而，纯文本的视觉问答（VQA）监督无法约束3D布局、深度或占据状态，模型可能生成流畅的场景描述却在3D空间上保持模糊。这种空间表征的缺失进一步引发灾难性遗忘：大规模驾驶域适配会覆盖预训练获得的通用世界知识，削弱模型在分布外（OOD）场景中的推理能力。

自动驾驶领域正经历从几何回归到具身认知的转变。早期工作如TransFuser和UniAD确立了基于BEV特征共享的确定性回归范式，但缺乏语义理解。2024年后，DriveGPT4等引入大语言模型（LLM）进行场景描述，却暴露出推理与动作脱节的缺陷。当前VLA路线面临两大瓶颈：一是文本VQA目标不直接约束3D几何，导致空间感知精度不足；二是域适配导致通用能力丢失，无法满足座舱-驾驶一体化部署对多轮对话与指令遵循的要求。Qwen-Drive-1.0的切入点在于保留VLM架构不变，通过外部模块显式暴露3D信息，并在训练数据中混合通用VQA以保留通用能力。

## 核心方法

### 方法参照系

VLA统一架构通常通过共享骨干融合感知、推理与控制。标准流程将多模态输入序列化为token，通过自注意力机制交互，最后由LM Head生成文本或回归轨迹。本文的关键差异在于：不修改VLM主干，而是外挂BEV感知头作为3D探针，并使用独立的Planning Expert通过流匹配生成轨迹，而非依赖文本中介或简单回归。

### 显式3D感知探针

纯文本VQA无法提供可评估的3D几何约束，导致模型在精细避障与定位上存在误差。本文引入BEV感知头，读取视觉编码器特征 $F_v$ 与VLM输出特征 $F_m$，通过深度基视图变换构建3D体素特征 $V(p)$：

$$ V(p) = \sum_{i \in \Omega(p)} D_i(u_i, v_i, d_i) F_v^i(u_i, v_i) $$

该公式将图像特征沿相机射线根据预测深度概率分布到3D空间，为BEV Transformer提供显式几何先验。BEV头联合优化3D检测、语义占据与地图分割，其损失函数为：

$$ \mathcal{L}_{perc} = \mathcal{L}_{det} + \mathcal{L}_{occ} + \mathcal{L}_{map} $$

这一设计解决了文本监督无法直接评估3D布局的问题，使模型具备可检查的3D场景结构接口，同时通过 $F_m$ 的梯度路径增强VLM的空间表征能力。

### 流匹配规划专家

现有VLA模型常通过next-token预测输出轨迹，难以捕捉驾驶行为的多模态分布。本文设计Planning Expert，利用VLM缓存的键值对（KV）条件化噪声轨迹，通过流匹配生成未来50个航点。定义线性插值路径 $\tau_t = (1-t)\tau_0 + t\tau_1$，其中 $\tau_1$ 为归一化真值轨迹。规划专家预测干净端点 $\hat{\tau}_1$ 而非流速度，其目标函数为：

$$ \mathcal{L}_{plan} = \mathcal{L}_{fm} + 2 \times 10^{-4} \mathcal{L}_{\Delta 1} + 2 \times 10^{-5} \mathcal{L}_{\Delta 2} $$

其中 $\mathcal{L}_{fm}$ 为诱导流速度与目标流速度之间的平方误差，$\mathcal{L}_{\Delta j}$ 为时间差异的Huber惩罚。端点参数化降低了对异构数据集传感器噪声的敏感性，而时间正则项确保轨迹的平滑性，解决了确定性回归无法表达多模态分布的问题。

## 实验评估

实验在nuScenes、OpenScene、NAVSIM及Waymo Open Dataset上进行。基线覆盖BEVFormerV2、PETR等专用3D检测器，以及Gemma4-12B、InternVL3.5-8B等通用VLM。在nuScenes 3D感知上，Qwen-Drive-1.0-SFT达到43.95 mAP和60.99 map mIoU，超越BEVFormerV2* 2.01 mAP，但NDS为34.13，低于专用检测器BEVFormerV2*的40.47（据领域综述推算，原文未直接对比NDS绝对值，仅提及超越mAP）。在NAVSIM闭环规划中，Qwen-Drive-1.0-RL取得90.7 EPDMS，超越HiST-VLA的88.6。

| 方法 | nuScenes mAP | nuScenes Map mIoU | NAVSIM EPDMS |
|---|---|---|---|
| Qwen-Drive-1.0-SFT | 43.95 | 60.99 | - |
| Qwen-Drive-1.0-RL | - | - | 90.7 |
| BEVFormerV2* | 41.94 | 57.62 | - |
| HiST-VLA | - | - | 88.6 |

消融实验显示，使用预训练ViT（SigLIP-Qwen）替代ResNet-50一致提升了专用检测器性能，但收敛后的头仍落后BEVFormerV2* 6.34 mAP，表明视觉-语言预训练特征支持视觉-文本对齐但不直接暴露3D结构。跨数据集迁移中，nuScenes-only头在OpenScene上NDS仅16.50，混合训练提升至41.86，但占据mIoU下降26.6%，揭示标签语义与标注流程差异导致的负迁移。

评估边界方面，论文未报告置信区间，数值比较需谨慎。代码与模型权重已开源，但BEV头的相机嵌入设计限制了跨传感器配置的泛化。评估协议侧重开环精度与闭环分数，缺乏对推理过程逻辑一致性的独立验证，且未覆盖计算效率维度。

## 关联研究分析

从问题动机看，Qwen-Drive-1.0与DrivePI均针对VLM空间感知不足，但DrivePI引入LiDAR点云作为额外输入以提供精确3D信息，而本文仅依赖相机图像并通过BEV头显式预测3D结构。这一差异源于任务特性：DrivePI侧重感知精度，本文侧重通用能力保留与座舱-驾驶一体化部署。本文未探索LiDAR融合，可能在复杂遮挡场景下空间精度受限，但避免了传感器成本增加。

从方法设计看，Qwen-Drive-1.0与CoT4AD同属VLA统一架构，但CoT4AD通过显式思维链（CoT）增强可解释性，而本文采用流匹配生成轨迹，未显式生成CoT文本。这一选择牺牲了安全审计所需的透明性，换取了实时性与多模态分布捕捉能力。CoT4AD的CoT生成增加推理延迟，而本文的Planning Expert通过缓存KV实现高效条件化，更适合毫秒级响应需求。两者在可解释性与实时性上的取舍，反映了VLA架构在认知深度与部署效率之间的不同定位。

## 总结

Qwen-Drive-1.0旨在解决VLA模型中3D空间表征缺失与通用知识灾难性遗忘的矛盾。通过外挂BEV感知头与流匹配规划专家，在保留VLM架构的前提下统一3D感知、问答与规划。实验证明其在NAVSIM闭环规划中取得90.7 EPDMS，超越HiST-VLA，但nuScenes 3D检测NDS为34.13，低于专用检测器。该架构的边界在于：BEV头依赖相机标定，跨传感器配置泛化能力受限；流匹配生成轨迹缺乏显式CoT，可解释性不足。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.00111)