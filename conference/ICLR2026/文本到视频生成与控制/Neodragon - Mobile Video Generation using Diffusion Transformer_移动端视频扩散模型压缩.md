# ICLR2026最新论文 ｜Neodragon: Mobile Video Generation using Diffusion Transformer ｜移动端视频扩散模型压缩

作者：Animesh Karnewar、Denis Korzhenkov、Ioannis Lelekas 等 13 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.06055)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.06055)

> 文本到视频生成（Text-to-Video, T2V）模型在云端已具备高保真度，但受限于显存与算力，难以在移动设备上实时运行。现有针对U-Net架构的移动端优化方案无法直接迁移至当前主流的扩散Transformer（Diffusion Transformer, DiT）骨干，导致DiT在边缘部署上存在空白。Neodragon通过文本编码器蒸馏、非对称解码器替换、MMDiT块剪枝及步数蒸馏四项技术，将Pyramidal-Flow模型适配至高通Hexagon NPU。该工作验证了DiT在移动端6.7秒生成2秒视频的工程可行性，但其质量上限受限于基础模型本身，且未解决长视频生成的时序漂移问题。

## 研究背景

视频生成的核心瓶颈在于去噪过程的计算密集性。潜在扩散模型（Latent Diffusion Model, LDM）通过在压缩潜空间执行去噪降低开销，但DiT架构的全局自注意力机制使得计算复杂度随序列长度呈二次增长。在移动端，这种复杂度直接转化为不可接受的推理延迟与功耗，且大参数量的文本编码器（如T5-XXL）往往超出设备DRAM容量，迫使模型进行CPU卸载，进一步破坏实时性。

T2V领域的主流研究聚焦于云端扩展性与语义控制精度，DiT因其扩展性成为SOTA模型（如Wan、CogVideoX）的骨干。然而，针对移动端的优化工作（如Mobile Video DiT）多局限于U-Net架构，缺乏对DiT特有的全局注意力与多模态条件注入机制的适配。Neodragon的切入点在于利用Pyramidal-Flow的时空金字塔因果结构，该结构在理论上将注意力计算复杂度降低约90倍，为DiT在资源受限设备上的部署提供了架构基础。

## 核心方法

### 时空金字塔因果注意力

Neodragon基于Pyramidal-Flow，其核心在于时空金字塔因果注意力机制。传统双向注意力复杂度为 $O(t^2 h^2 w^2)$，而Pyramidal-Flow通过因果帧生成与空间下采样，将复杂度降至 $O(t^2 h w)$ 量级。具体而言，对于 $S$ 个空间阶段，第 $i$ 阶段的token数为 $M/4^i$，总计算量 $C_{total} \approx \sum_{i=0}^{S-1} \frac{1}{4^i} \sum_{d=1}^{t} (t-d) M \cdot T(d)$。这种设计动机在于解决全分辨率双向注意力在移动端显存溢出与延迟过高的问题，通过粗到细的去噪策略，使模型能在低分辨率阶段快速建立全局结构，再在高分辨率阶段细化纹理。

### 非对称解码器蒸馏

原生VAE解码器参数庞大且计算复杂，无法在NPU上高效运行。Neodragon提出非对称解码器蒸馏，保持生成潜空间（MMDiT输出的latent）不变，仅替换解码器。训练目标为最小化重建误差：

$$ \mathcal{L}_{rec} = \| E_{dec}(\hat{z}) - x \|_2^2 + \lambda \| E_{dec}(\hat{z}) - E_{enc}(x) \|_2^2 $$

其中 $E_{dec}$ 为轻量级解码器（如TinyAEHV），$E_{enc}$ 为原生编码器。该设计解决了原生解码器在NPU上无法编译或延迟过高的问题，实现了20倍以上的参数缩减，且对VBench生成质量影响小于0.1分。

### MMDiT块剪枝与步数蒸馏

MMDiT去噪器包含24个块，其中部分块对生成质量贡献较小。Neodragon通过计算块重要性分数进行剪枝，保留18个块，参数从2.028B降至1.518B。剪枝后通过两阶段蒸馏恢复性能，第一阶段使用数据流匹配损失，第二阶段使用教师模型特征匹配。步数蒸馏则基于分布匹配蒸馏（Distribution Matching Distillation, DMD），将神经功能评估（Neural Functional Evaluation, NFE）从480步降至21步。DMD的目标函数为：

$$ \mathcal{L}_{DMD} = \mathbb{E}_{t, \epsilon} [ \| D_{student}(z_t, t) - D_{teacher}(z_t, t) \|_2^2 ] $$

该公式通过让学生模型预测与教师模型一致的流场，实现少步采样下的质量保持。这一组合策略解决了剪枝导致的语义对齐下降与多步去噪的延迟瓶颈，使端到端延迟从184.2秒降至6.7秒。

## 实验评估

实验在VBench基准上进行，对比了Pyramidal-Flow、Wan2.1、CogVideoX等云端模型及Snap Mobile Video DiT等移动端模型。Neodragon在VBench Total得分81.61，高于基线Pyramidal-Flow的80.31，但低于云端SOTA Wan2.1的83.31。在移动端对比中，Neodragon的语义得分（Sem. 73.36）高于Hummingbird 26frame（69.10），表明其在压缩后仍保持了较好的语义遵循能力。

| 模型 | 平台 | VBench Total | VBench Sem. | 延迟/备注 |
| :--- | :--- | :--- | :--- | :--- |
| Pyramidal-Flow | Server | 80.31 | 66.81 | 27s (480 NFE) |
| Wan2.1 1.3B | Server | 83.31 | 75.65 | - |
| Hummingbird 26frame | Mobile | 80.31 | 69.10 | - |
| Neodragon E2E | Mobile | 81.61 | 73.36 | 6.7s (21 NFE) |

消融实验显示，文本编码器蒸馏中，Replace-Mode（79.64）优于Extend-Mode（79.16），LoRA模式（64.74）因语义丢失严重被弃用。MMDiT剪枝中，18块模型（80.21）在质量与延迟（0.74s）间取得最佳平衡，16块模型（78.62）质量下降明显。步数蒸馏中，DMD方法在21 NFE下取得76.48分，优于Progressive Distillation的76.17分，且动态程度（D.D.）更高（86.11 vs 52.50）。

评估边界方面，VBench主要评估单事件短视频质量，未覆盖长视频叙事连贯性。Neodragon的生成分辨率限制在640×1024，且依赖Pyramidal-Flow的预训练质量，其优化策略的泛化性未在其他DiT骨干上验证。代码已开源，但NPU量化细节（如W8A16 PTQ）的复现依赖特定高通硬件环境。

## 关联研究分析

从问题动机看，Neodragon与Mobile Video DiT均针对移动端DiT部署，但后者侧重U-Net架构的轻量化，而Neodragon聚焦于DiT特有的全局注意力与多模态条件注入的NPU适配。这一差异源于DiT架构在语义对齐上的优势，但同时也带来了更高的计算复杂度，使得简单的参数缩减不足以解决延迟问题，必须结合步数蒸馏与块剪枝。

从方法设计看，Neodragon的非对称解码器蒸馏与FullDiT的全注意力融合形成对比。FullDiT通过全注意力机制融合多条件，追求语义控制的涌现能力，但计算开销大；Neodragon则通过替换解码器与剪枝块，在保持潜空间不变的前提下降低计算量。这种设计选择反映了边缘部署对计算效率的极端需求，但可能牺牲了模型对复杂空间关系的建模能力，查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

Neodragon要解决的核心矛盾是DiT架构在移动端的高计算复杂度与实时性需求之间的冲突。其切入点在于利用Pyramidal-Flow的时空金字塔结构降低注意力复杂度，并通过四项压缩技术适配NPU。该方法证明了在6.7秒内生成2秒视频的工程可行性，VBench Total得分81.61高于基线。然而，其质量上限受限于Pyramidal-Flow的预训练水平，且未解决长视频生成的时序漂移问题。当支持集增大到长序列时，金字塔因果注意力的误差累积是否会导致语义漂移，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.06055)