# HuggingFace最新推荐论文 ｜VINO: A Unified Visual Generator with Interleaved OmniModal Context ｜统一视觉生成器 VINO：交错全模态上下文下的图像与视频联合生成编辑

研究机构：上海交通大学、快手

作者：Junyi Chen、Tong He、Zhoujie Fu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.02358)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.02358)

> 导读 视觉生成领域长期受困于文本到图像、文本到视频与视觉编辑模型各自独立部署的碎片化格局，导致多模态信号在同时输入时缺乏可靠的解耦与优先级机制，引发语义冲突。VINO 通过耦合冻结的视觉语言模型（VLM）与多模态扩散 Transformer（MMDiT），将文本、参考图像与视频编码为交错的条件 token，并引入可学习查询 token 与 VAE 潜变量直通机制，在单一骨干中统一处理生成与编辑任务。该架构在 OpenVE-Bench 视频编辑基准上以 3.18 的 Overall 分数超越所有开源基线，同时保持了与骨干模型相当的生成质量。其价值在于验证了统一框架的可行性，但 VLM 对视觉细节的压缩是否构成像素级编辑的精度上限，论文未提供量化证据。

## 研究背景

当扩散模型在像素或潜空间执行去噪时，其条件信号通常来自文本编码器输出的语义向量。然而，编辑任务依赖短指令修改局部区域，而生成任务依赖长描述构建全局场景，两者在指令长度与空间粒度上存在分布差异。更关键的是，当参考图像与视频同时作为条件输入时，模型需区分不同视觉来源的时空结构，否则注意力机制会将静态图像潜变量误读为视频序列的一部分，导致首帧结构畸变。

视频编辑领域的主流路线在数据效率与精度间做出不同取舍：免训练方法通过操纵预训练模型的注意力矩阵实现零样本编辑，规避了数据稀缺瓶颈，但精度上限受限于预训练先验；端到端方法如 VACE 通过大规模指令-视频配对数据训练统一 DiT 架构，提升了复杂指令遵循能力，但数据成本高且任务间存在干扰。现有统一框架多聚焦于视频域，图像与视频生成编辑的联合建模仍缺乏系统性方案，异构模态信号在单一扩散骨干中的解耦机制尚未建立。

VINO 的切入点在于将 VLM 作为统一前端编码器处理所有控制信号，同时通过 VAE 潜变量直通保留视觉细节，解决了 VLM 压缩导致的高频纹理丢失问题。该设计将多模态条件注入从“文本编码器替换”升级为“语义-潜变量双通道注入”，为统一视觉生成提供了架构基础。

## 核心方法

### 方法参照系

统一多任务框架的标准流程是：预训练生成骨干 + 任务特定条件模块 + 多任务混合训练。本文的关键差异在于条件模块从单一文本编码器扩展为 VLM 与 VAE 潜变量的双通道注入，且训练策略从直接多任务混合改为渐进式分布对齐。

### 可学习查询 Token 与 VLM 条件编码

VINO 在 VLM 输入端追加一组可学习查询 token，这些 token 与系统提示、用户指令及视觉引用标识共同构成 VLM 的输入序列。VLM 处理后，其倒数第二层隐藏状态经两层 MLP 投影为 MMDiT 的条件 token。可学习 token 的设计动机在于弥合长描述与短指令的分布差异：在渐进训练的第二阶段，模型同时接触长短 prompt，可学习 token 被优化为“短指令精炼器”，将简洁编辑指令映射为与长描述兼容的条件空间。该机制的优化稳定性由训练曲线验证：引入可学习 token 后，T2V、T2I、I2V 任务的梯度范数方差显著降低，损失曲线更平滑。

$$
\mathbf{c}_{\text{VLM}} = \text{MLP}_2(\text{MLP}_1(h_{\text{VLM}}^{(L-1)}))
$$

其中 $h_{\text{VLM}}^{(L-1)}$ 为 VLM 倒数第二层隐藏状态，$\mathbf{c}_{\text{VLM}}$ 为注入 MMDiT 的条件 token。该公式表明 VLM 输出经线性投影后直接进入扩散骨干，无需任务特定适配器。

### VAE 潜变量直通与特殊边界 Token

VLM 编码压缩了视觉细节，无法支持局部编辑所需的结构精度。VINO 将参考图像/视频的 VAE 潜变量直接注入 MMDiT，与 VLM 条件 token 并行。关键创新在于复用 VLM 中的视觉起始/结束特殊 token 作为 VAE 潜变量块的边界标记：每个参考视觉源的 VLM token 与 VAE 潜变量共享相同的边界标记，使 MMDiT 的注意力机制能将同一视觉源的语义与潜变量特征分组。消融实验显示，移除特殊 token 后，模型将静态图像潜变量误读为视频时序序列，首帧出现严重结构畸变。

$$
\mathbf{z}_{\text{VAE}} = [\mathbf{e}_{\text{start}}, \mathbf{z}_{\text{img}}^{(1)}, \mathbf{e}_{\text{end}}, \mathbf{z}_{\text{img}}^{(2)}, \mathbf{e}_{\text{end}}, \dots, \mathbf{z}_{\text{video}}]
$$

其中 $\mathbf{e}_{\text{start}}$ 和 $\mathbf{e}_{\text{end}}$ 为投影后的特殊 token，$\mathbf{z}_{\text{img}}^{(i)}$ 为第 $i$ 个参考图像的 VAE 潜变量，$\mathbf{z}_{\text{video}}$ 为噪声目标视频潜变量。该排列确保不同视觉来源在 MMDiT 序列中具有明确的位置边界。

## 实验评估

VINO 在 Geneval、VBench、OpenS2V、ImgEdit、GEdit 与 OpenVE-Bench 上评估，基线覆盖开源（VACE-14B、OmniVideo、ICVE、Ditto、OpenVE-Edit）与闭源（Sora、Veo3、Kling1.6、Gemini2.5、GPT4o）系统。OpenVE-Bench 上 VINO 以 Gemini 2.5 Pro 为评判者取得 3.18 Overall 分数，显著高于 VACE-14B 的 1.57 与 OpenVE-Edit 的 1.48；以 Qwen3VL 为评判者时，VINO 取得 4.34 Overall，同样领先所有基线。VBench 上 VINO 的 Total 分数 82.80 与骨干 HunyuanVideo 的 83.24 接近，表明渐进训练未导致生成能力灾难性遗忘。

| 基准 | 指标 | VINO | 最强开源基线 | 最强闭源基线 |
|---|---|---|---|---|
| OpenVE-Bench (Gemini) | Overall | 3.18 | Lucy-Edit 2.07 | - |
| OpenVE-Bench (Qwen3VL) | Overall | 4.34 | Lucy-Edit 3.99 | - |
| VBench | Total | 82.80 | Wan2.1-14B 83.69 | Veo3 85.06 |
| ImgEdit | Average | 4.18 | Step1x-EditV1.1 4.01 | Seedream4 4.46 |

消融实验聚焦三个组件：可学习 token 的移除导致训练不稳定与编辑精度下降；Image CFG 尺度增加强化身份保持但抑制运动多样性，存在最优平衡点；特殊边界 token 的移除导致跨模态潜变量混淆。这些结果验证了双通道注入与边界标记机制的必要性。

评估边界方面，VINO 未报告计算效率指标（FPS、内存占用），无法评估实时性；OpenVE-Bench 的评判者为 MLLM，其评分标准与人类偏好的对齐度未量化；代码已开源，但训练数据构成（O(100)k 样本）与具体数据集混合比例未完全披露，可复现性受数据获取限制。

## 关联研究分析

从问题动机看，VINO 与 VACE 同属统一多任务框架，但 VACE 侧重任务解耦（通过视频条件单元区分不同编辑任务），而 VINO 侧重模态交错（通过 VLM+VAE 双通道处理异构视觉源）。这一差异源于任务定义：VACE 假设编辑任务类型已知，VINO 假设视觉源类型与数量可变。VINO 的特殊边界 token 机制解决了 VACE 未明确处理的“多参考视觉源解耦”问题，但 VACE 的任务嵌入设计可能更适合标准化编辑任务，VINO 的通用性是否以任务精度为代价，论文未提供对比实验。

从方法设计看，VINO 与 Bagel 均使用 VLM+Diffusion 架构，但 Bagel 仅依赖 VLM 特征作为条件，VINO 增加 VAE 潜变量直通以保留细节。这一设计选择源于 VLM 的信息压缩瓶颈：VLM 将图像编码为固定长度 token，丢失高频纹理，而编辑任务（如局部替换）需要像素级精度。VINO 的 VAE 直通机制是否在所有编辑任务上均优于纯 VLM 条件，论文未做消融；若 VLM 压缩损失可通过更强的 VLM 缓解，VAE 直通的计算开销是否值得，存在权衡空间。

## 总结

VINO 要解决的核心矛盾是视觉生成与编辑任务的碎片化部署导致的多模态信号解耦失效。现有方法或依赖任务特定模块（VACE），或仅使用 VLM 特征（Bagel），无法同时处理异构视觉源与短指令编辑。VINO 通过 VLM+VAE 双通道注入与特殊边界 token 机制，在单一 MMDiT 骨干中实现了图像/视频生成编辑的统一，OpenVE-Bench 上 3.18 的 Overall 分数验证了编辑能力，VBench 82.80 的 Total 分数确认了生成能力的保持。其边界在于 VLM 压缩对高频纹理编辑的影响未量化，且计算效率未评估。当参考图像数量增加至 5 个以上时，特殊边界 token 的注意力解耦能力是否退化，论文未提供实验证据。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.02358)