# HuggingFace最新推荐论文 ｜Can Natural Image Autoencoders Compactly Tokenize fMRI Volumes for Long-Range Dynamics Modeling? ｜基于2D自然图像自编码器的fMRI长时序建模

研究机构：韩国首尔大学

作者：Peter Yongho Kim、Juhyeon Park、Jungwoo Park 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.03619)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.03619)

> fMRI时序建模面临高维体素数据导致的显存瓶颈，现有体素级方法仅能处理20-50个时间步，无法捕捉数十秒尺度的慢速神经振荡。本文切入点在于利用预训练2D自然图像自编码器将3D fMRI体压缩为27个连续Token，从而在有限显存下实现256帧的长序列Transformer建模。该方法通过冻结的跨域Tokenizer与轻量级编码器结合，在人口属性预测与ADHD诊断任务上取得一致但温和的性能提升，并验证了自监督预训练的有效性。其价值在于证明了自然图像先验在脑信号压缩中的可行性，但性能增益的幅度及跨域迁移的边界仍存疑。

## 研究背景

fMRI信号本质上是4D时空数据，其分析需同时处理空间结构与时序动态。传统ROI-based方法通过解剖分割提取功能连接矩阵，虽计算高效，但丢失了细粒度3D空间信息且严重依赖ROI选择。体素级方法（如TFF、SwiFT）直接处理原始4D数据，保留了空间拓扑，但受限于Transformer的二次复杂度，单次处理的时间窗口被压缩至20-50帧，难以覆盖BOLD信号中数十秒尺度的低频振荡（如infraslow BOLD-LFP耦合）。

现有体素级模型在长时序建模上存在根本性矛盾：增加时间步长 $T$ 会导致显存呈平方级增长，而fMRI数据的高空间维度（96×96×96）进一步加剧了这一负担。SwiFT等SOTA方法在 $T=50$ 时已接近硬件极限，导致模型无法捕捉长程依赖，这在需要全局动态信息的任务（如智力预测、ADHD诊断）中尤为不利。本文的切入点在于解耦空间压缩与时序建模：不直接在体素空间进行Transformer运算，而是先通过一个预训练好的2D自然图像自编码器（DCAE）将每个3D体压缩为极少量的连续Token，从而将输入维度从百万级体素降至27个向量，使得在相同显存预算下处理 $T=256$ 帧成为可能。

## 核心方法

### 方法参照系

本文问题属于fMRI时序分类/回归任务，标准流程为：预处理fMRI数据 → 提取时空特征 → 分类/回归头。与主流体素级方法（如SwiFT）的关键差异在于特征提取阶段：本文不直接对体素进行4D卷积或注意力，而是引入一个冻结的、在自然图像上预训练的2D自编码器作为空间Tokenizer，将3D体转化为低维Token序列，再交由Transformer处理时序。

### 跨域空间Tokenization

传统做法是在fMRI数据上训练3D自编码器或直接在体素上操作，但这需要大量标注数据且计算昂贵。本文创新在于直接复用2D DCAE编码器，将3D体沿三个轴（Sagittal, Coronal, Axial）切片为2D图像，分别压缩后聚合。设计动机是规避fMRI数据稀缺导致的过拟合，并利用自然图像中丰富的空间纹理先验来保留脑信号的低层结构。具体而言，对于形状为 $(1, 96, 96, 96)$ 的体，沿深度轴切片得到96张 $96 \times 96$ 图像，每张经DCAE压缩为 $32 \times 32$ 的潜变量。三个轴的潜变量按32体素块对齐并拼接，最终每个3D体被压缩为 $27$ 个Token，嵌入维度为 $3072$。该过程无需微调，计算成本极低且可缓存。

$$
\mathbf{Z}_{\text{frame}} = \text{Concat}(\mathbf{Z}_{D}, \mathbf{Z}_{H}, \mathbf{Z}_{W}) \in \mathbb{R}^{27 \times 3072}
$$

其中 $\mathbf{Z}_{D}, \mathbf{Z}_{H}, \mathbf{Z}_{W}$ 分别为沿三个轴切片压缩后的潜变量聚合结果。此公式表明，单个3D体的全部空间信息被浓缩为27个高维向量，极大降低了后续时序建模的输入维度。

### 长时序Transformer与MTM预训练

在获得Token序列后，本文构建了一个12层Transformer编码器，采用Grouped Query Attention (GQA) 和RoPE以高效处理长序列。设计动机是解决长序列下的注意力计算瓶颈，同时通过自监督预训练弥补下游任务数据量的不足。预训练采用Masked Token Modeling (MTM)，随机掩蔽50%的Token，让模型预测被掩蔽的Token值。与Masked Image Modeling (MIM) 不同，MTM直接在Token空间操作，无需解码器重建像素，简化了训练流程。

$$
\mathcal{L}_{\text{MTM}} = \frac{1}{|\Omega|} \sum_{i \in \Omega} \| \mathbf{y}_i - \mathbf{Z}_i \|_1
$$

其中 $\Omega$ 为被掩蔽Token的索引集合，$\mathbf{y}_i$ 为预测值，$\mathbf{Z}_i$ 为真实Token值。该损失函数迫使Transformer学习Token间的时空依赖关系，从而在下游任务中提供更鲁棒的特征表示。

## 实验评估

实验在UKB（8,178人）、HCP（1,061人）和ADHD-200（533人）三个静息态fMRI数据集上进行，任务包括性别/年龄预测、智力预测及ADHD诊断。基线覆盖ROI-based（XGBoost, BrainNetCNN, BNT, meanMLP, Brain-JEPA）和体素级（TFF, SwiFT）。

| 方法 | UKB Sex ACC | UKB Age MSE | HCP Intelligence MSE | ADHD-200 Diagnosis ACC |
| :--- | :--- | :--- | :--- | :--- |
| SwiFT ($T=20$) | 97.4 | 0.366 | 0.940 | 63.3 |
| SwiFT ($T=50$) | 98.1 | 0.364 | 0.865 | 63.9 |
| TABLeT ($T=256$) | 97.7 | **0.340** | **0.835** | **65.8** |

TABLeT在HCP智力预测（MSE 0.835 vs 0.865）和ADHD诊断（ACC 65.8% vs 63.9%）上优于SwiFT，但在UKB年龄预测上MSE略优（0.340 vs 0.364），性别预测上持平。值得注意的是，SwiFT在 $T=50$ 时已接近显存极限，而TABLeT在 $T=256$ 下运行，且内存效率比SwiFT高7.33倍，训练速度快3.8倍。

消融实验显示，使用2D DCAE优于3D DCAE（在HCP Sex任务上ACC 93.8% vs 92.2%），且聚合三个轴的切片优于单一轴。MTM预训练进一步提升了HCP任务性能（如Sex ACC从93.8%提升至95.3%），表明自监督学习有效利用了无标签数据。

评估边界方面，本文仅使用静息态fMRI，未验证任务态fMRI（如视觉刺激）下的性能，而后者可能更依赖长时序动态。此外，指标未包含重建质量或功能连接保真度，仅关注下游任务性能，无法直接评估Tokenizer对神经科学解释性的贡献。代码已开源，但超参数细节（如DCAE具体版本）未在正文中详述，复现需参考附录。

## 关联研究分析

从问题动机看，本文与SwiFT同属体素级fMRI建模，但SwiFT聚焦于4D窗口注意力的架构优化，而TABLeT聚焦于输入表示的压缩。SwiFT受限于 $T=50$ 的显存瓶颈，无法探索更长时序，而TABLeT通过空间压缩解耦了这一限制。差异根源在于任务特性：静息态fMRI的慢速动态需要长窗口，而SwiFT的架构未考虑显存与 $T$ 的非线性关系，TABLeT则通过Tokenization将显存消耗与 $T$ 线性化。

从方法设计看，本文与MAE/SimMIM同属自监督预训练范式，但MAE在像素空间重建，TABLeT在Token空间预测。MAE需要解码器，计算开销大，而TABLeT的MTM直接预测Token，简化了流程。差异根源在于数据特性：fMRI数据量远小于自然图像，训练3D解码器不现实，而2D DCAE的预训练提供了强大的空间先验，使得Token空间预测成为可能。这种跨域迁移是否引入了非脑特异性的空间偏置，论文未给出回答。

## 总结

本文核心矛盾是fMRI高维空间数据与Transformer长时序建模的显存冲突。切入点在于利用2D自然图像自编码器的跨域压缩能力，将3D体转化为27个Token，从而在有限显存下实现 $T=256$ 的长序列建模。方法上，TABLeT结合冻结的2D DCAE与轻量级Transformer，并通过MTM预训练提升特征质量。实验证明，该方法在HCP智力预测（MSE 0.835）和ADHD诊断（ACC 65.8%）上优于SwiFT，且内存效率提升7.33倍。边界在于，性能增益在静息态任务上温和，且未验证任务态fMRI下的优势；2D自然图像先验是否保留了fMRI特有的功能连接拓扑，还是仅保留了低层空间结构，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.03619)