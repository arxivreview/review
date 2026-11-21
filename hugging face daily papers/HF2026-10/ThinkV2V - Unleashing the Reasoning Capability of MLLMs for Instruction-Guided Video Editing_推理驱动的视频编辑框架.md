# HuggingFace最新推荐论文 ｜ThinkV2V: Unleashing the Reasoning Capability of MLLMs for Instruction-Guided Video Editing ｜推理驱动的视频编辑框架

作者：Donghao Zhou、Haoyang He、Fan Zhang 等 13 人

论文原文见 [arXiv](https://arxiv.org/abs/2609.38541)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.38541)

> 指令引导视频编辑的核心矛盾在于，用户指令往往隐含因果逻辑而非直接描述目标外观，现有方法将多模态大语言模型（MLLM）仅作为静态语义编码器，导致模型在需要因果推理的隐式指令上频繁失效。ThinkV2V 的切入点是将 MLLM 从“编码器”改造为“显式思考者”，通过思维链（Chain-of-Thought, CoT）生成细化指令与高层语义特征，再注入扩散 Transformer（DiT）执行编辑。该框架结合渐进课程训练与推理时思维缩放，在自建基准上实现了 5B 参数模型对 10B 基线的超越。其价值在于验证了显式推理对复杂指令编辑的有效性，但推理时多轮精化的计算开销与冻结 MLLM 的推理上限存疑。

## 研究背景

当用户输入“移除背对镜头的人”这类指令时，模型需先理解“背对镜头”的空间关系与“移除”的因果后果，才能定位编辑区域。这一过程要求模型具备因果推理能力，而传统视频编辑方法将 MLLM 视为文本编码器，仅提取静态语义特征，忽略了指令背后的逻辑链条。这种“感知驱动”范式在处理显式指令（如“变红”）时有效，但在涉及时间动态、物体关系或逻辑因果的隐式指令上，模型往往锁定表面关键词而偏离真实编辑目标。

指令引导视频编辑的主流路线是特征融合，如 Omni-Video 和 LucyEdit 通过序列或通道拼接将 VAE 特征与噪声潜变量结合，但均缺乏对隐式意图的显式推理机制。VideoCoF 虽引入“帧链”推理，但未解耦 MLLM 的认知过程与视频生成器。ThinkV2V 的切入点在于，将 MLLM 的显式思考过程（CoT）与 DiT 的执行过程分离，通过可学习查询连接器将思考结果转化为稳定的编辑条件，从而在保持生成质量的同时提升指令遵循的准确性。

## 核心方法

### 方法参照系

本文问题属于“推理增强编辑”路线，其通用流程为：MLLM 解析指令 → 特征注入 DiT → 去噪生成。与 VideoCoF 等方法的差异在于，ThinkV2V 不将 MLLM 输出直接作为条件，而是引入显式 CoT 思考过程，并通过可学习查询连接器压缩与对齐语义特征，避免长序列 token 的不稳定性。

### 显式思考与特征对齐

设计动机：现有方法将 MLLM 作为静态编码器，无法捕捉指令中的因果逻辑，导致隐式指令编辑失败。本文在 MLLM 与 DiT 之间插入可学习查询连接器，将 MLLM 的 CoT 输出转化为固定长度条件。具体地，MLLM 接收源视频 $V$ 与原始指令 $I$，生成思考内容 $T$、细化指令 $\hat{I}$ 及答案 token 隐藏状态 $H_{ans}$。连接器通过交叉注意力提取紧凑特征：

$$C = \text{CrossAttn}(Q_{learn}, K_{ans}, V_{ans}) \in \mathbb{R}^{N_q \times d_c}$$

其中 $Q_{learn}$ 为可学习查询，$K_{ans}, V_{ans}$ 为 $H_{ans}$ 的键值投影。该设计将 MLLM 的高层语义压缩为 DiT 友好的条件，避免长序列 token 的冗余与不稳定，提升跨模块特征交互的鲁棒性。

### 多条件去噪与推理时缩放

设计动机：单一 MLLM 特征可能丢失细粒度视觉细节，且单次推理易产生推理漂移。本文在 DiT 中同时注入连接器特征 $C$、原始指令文本嵌入 $E_{text}$ 与源视频 VAE 特征 $z_{src}$，通过通道拼接与 token 拼接融合：

$$\hat{z}_0 = f_{DiT}(t, z_t \parallel_{ch} z_{src}, C \parallel_{tok} E_{text})$$

其中 $\parallel_{ch}$ 与 $\parallel_{tok}$ 分别为通道与 token 维度拼接。推理时，引入思维缩放机制：将细化指令反馈至 MLLM 进行多轮串行精化，生成 $N=8$ 个候选，由 MLLM 选择最符合原始意图的候选，其缓存隐藏状态用于最终生成。该机制通过迭代精化与选择，纠正单次推理的潜在漂移，提升复杂指令的编辑质量。

## 实验评估

实验在 ThinkV2V-Bench 与 OpenVE-Bench 上进行，基线包括 VACE、OmniVideo、ReCo、OpenVE-Edit 等 10B 参数模型。ThinkV2V 采用 5B 参数 DiT，在复杂指令编辑场景中整体得分显著优于 10B 基线，但在标准任务上仅具竞争力。

| 设置 | Global Style | Bg. Change | Local Change | Local Remove | Local Add | Overall |
|---|---|---|---|---|---|---|
| w/o Thinking | 2.89 | 2.71 | 3.05 | 1.46 | 2.42 | 2.51 |
| w/ Thinking + All Features | 2.95 | 2.68 | 3.09 | 1.94 | 2.46 | 2.63 |
| w/ Thinking + Answer Features | 2.93 | 2.63 | 3.02 | 2.34 | 2.47 | 2.68 |
| Simple-to-Complex | 2.93 | 2.63 | 3.02 | 2.34 | 2.47 | 2.68 |
| Serial Refinement + Selection | 3.13 | 2.67 | 3.07 | 2.30 | 2.42 | 2.72 |

消融实验显示，启用显式思考使整体得分从 2.51 提升至 2.63，使用答案特征（而非全部 token）进一步提升至 2.68，表明答案 token 的隐藏状态更具执行导向性。渐进课程训练中，“Simple-to-Complex”策略（2.68）优于“Complex Only”（2.10）与“Mixed”（2.47），验证了从简单到复杂指令的渐进学习必要性。推理时思维缩放中，仅串行精化（2.67）未带来提升，加入选择步骤后升至 2.72，说明迭代精化可能放大局部歧义，选择机制是纠正推理漂移的关键。

评估边界：ThinkV2V-Bench 为自建基准，仅覆盖 5 类推理适配任务，缺乏与免训练方法（如 TokenFlow）的对比；OpenVE-Bench 结果未提供详细数值，仅称“substantially outperforms”。可复现性方面，论文提供项目页面，但未明确代码开源状态；训练使用 32-GPU 集群，超参数（如学习率 1e-5/1e-6）已披露，但 MLLM 冻结策略可能限制推理能力上限。

## 关联研究分析

从问题动机看，ThinkV2V 与 VideoCoF 均针对复杂指令编辑，但 VideoCoF 将编辑建模为“推理后生成”，通过时空 RoPE 实现帧链对齐，而 ThinkV2V 将 MLLM 的 CoT 过程显式解耦，通过连接器将思考结果转化为条件。差异根源在于任务特性：VideoCoF 侧重时空一致性，ThinkV2V 侧重语义推理的稳定性。ThinkV2V 的连接器设计是否优于 VideoCoF 的 RoPE 对齐，论文未给出直接对比。

从方法设计看，ThinkV2V 与 LucyEdit 同属 DiT 架构，但 LucyEdit 通过通道拼接融合源视频特征，未引入显式推理机制；ThinkV2V 继承其通道拼接策略，但增加了 MLLM 思考过程与连接器。差异根源在于：LucyEdit 假设指令为显式描述，而 ThinkV2V 针对隐式指令，需通过 CoT 揭示因果逻辑。冻结 MLLM 仅训练连接器与 DiT 的策略，是否限制了推理能力的上限，论文未给出回答。

## 总结

ThinkV2V 要解决的核心矛盾是隐式指令编辑中 MLLM 推理能力与 DiT 执行能力的脱节。其切入点是显式解耦 MLLM 的思考过程，通过可学习查询连接器将 CoT 输出转化为稳定条件，结合渐进课程训练与推理时思维缩放，提升复杂指令的编辑质量。实验证明，5B 参数模型在 ThinkV2V-Bench 上整体得分达 2.72，优于 10B 基线；消融显示答案特征与选择机制是关键增益来源。本文边界在于，推理时多轮精化增加计算开销，且冻结 MLLM 可能限制推理上限；ThinkV2V-Bench 仅覆盖 5 类任务，缺乏与免训练方法的对比。当支持集增大到 5-shot 时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.38541)