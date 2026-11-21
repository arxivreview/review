# HuggingFace最新推荐论文 ｜LoST: Level of Semantics Tokenization for 3D Shapes ｜语义层级化3D形状Token化

研究机构：英国伦敦大学学院、Adobe研究院

作者：Niladri Shekhar Dutt、Zifan Shi、Paul Guerrero 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.17995)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.17995)

> 自回归（AR）3D生成面临Token序列效率低下与早期前缀语义缺失的双重瓶颈，传统几何层级化方法无法在短序列内提供可用的形状中间态。本文提出按语义显著性排序的Level-of-Semantics Tokenization (LoST)，通过Relational Inter-Distance Alignment (RIDA)损失在潜空间注入语义结构，使任意短前缀均能解码出语义完整的形状。该方法以128个Token实现了超越现有SOTA的AR生成质量，但其性能优势是否完全归因于语义排序，还是受限于特定VAE潜空间的固有特性，仍需跨表示验证。

## 研究背景

自回归模型在3D生成中具备训练简单与单步采样优势，但其性能高度依赖Token序列的组织方式。传统方法将3D形状序列化为扁平的顶点流或基于八叉树的几何层级，这种结构源于渲染与压缩需求，而非生成建模。当AR模型尝试预测下一个Token时，几何层级导致早期Token仅包含粗糙的空间骨架，既造成Token数量膨胀，又使得短前缀解码出的形状在几何与语义上均不可用，严重限制了AR在交互式生成与多模态大语言模型集成中的应用潜力。

现有3D生成主流范式为潜空间扩散模型（Latent Diffusion Model, LDM），其通过迭代去噪在紧凑潜空间中平衡质量与效率，但AR范式提供了与语言模型无缝集成的独特路径。然而，AR 3D生成缺乏类似2D图像中成熟的语义Token化标准。OctGPT等基于几何层级的方法虽保证了空间连贯性，却将计算容量分配给几何元素而非定义类别的语义特征，导致模型在高困惑度区域挣扎。本文切入点在于重新定义3D形状的Token化原则：从空间占据的粗细粒度转向语义显著性的层级结构，确保Token序列的任意前缀均具备独立的语义完整性。

## 核心方法

### 语义显著性Token化架构

本文方法建立在Direct3D的Triplane VAE潜空间之上，该空间将点云编码为$32 \times 32 \times 3$的特征网格。与直接对网格进行ViT编码不同，LoST引入一组可学习的Register Tokens ($\mathcal{T}_R$) 作为信息瓶颈。这些Token不绑定于特定的Triplane Patch，而是通过因果掩码与嵌套Dropout机制，强制将形状的主语义信息前置到序列早期。这种设计解决了传统几何层级中“早期Token仅含空间骨架”的失效，使得模型在训练阶段即学会将粗粒度语义压缩至前几个Token，后续Token逐步补充实例特定的几何细节。

### 关系互距离对齐损失

3D形状缺乏直接的2D语义监督信号，无法直接应用REPA等基于图像特征对齐的损失。为此，本文提出RIDA损失，通过预训练一个语义提取器 $f_\theta$，将Triplane潜空间映射至与DINO特征空间具有相同关系拓扑的学生空间。RIDA的核心在于对齐样本间的相对距离而非绝对特征值，其全局关系对比损失定义为：

$$ \mathcal{L}_{global} = -\log \frac{\sum_{z_j \in Z_i^+} \exp(c_{ij} / \tau)}{\sum_{z_k \in Z_i^+ \cup Z_i^-} \exp(c_{ik} / \tau)} $$

该公式通过多正样本InfoNCE结构，利用教师空间挖掘的正负样本对，拉近语义相似3D形状在潜空间中的距离，推远不相似形状。此外，引入实例间秩蒸馏损失 $\mathcal{L}_{rank}$ 与空间结构蒸馏损失 $\mathcal{L}_{spatial}$，分别传递连续的关系结构与部件级亲和性。最终，预训练的 $f_\theta$ 作为感知损失引导扩散生成器 $G$，确保生成的Token序列在语义层级上的一致性。

## 实验评估

实验在自建300k形状数据集上进行，该数据由Direct3D管线生成，测试集采用Step1X-3D生成的1k独立形状以确保评估中立性。基线覆盖OctGPT（八叉树层级）、VertexRegen（渐进网格）及ShapeLLM-Omni（潜空间AR）。在AR生成任务中，LoST-GPT仅使用128个Token，即取得FID 34.251与DINO相似度0.758，显著优于使用1024个Token的ShapeLLM-Omni（FID 48.702, DINO 0.680）及OctGPT（FID 66.926）。

| 方法 | Num Tokens | FID ↓ | DINO ↑ |
| :--- | :--- | :--- | :--- |
| OctGPT | ~50,000 | 66.926 | ✗ |
| Llama-Mesh | ~3758 | 118.576 | ✗ |
| ShapeLLM-Omni | 1024 | 48.702 | 0.680 |
| LoST (ours) | 128 | 34.251 | 0.758 |

在Tokenizer重建任务中，LoST在极低Token预算下表现突出。当仅使用1个Token时，LoST的CD为2.271，FID为31.649，而OctGPT在~219个Token下CD为16.923，FID为341.174。这表明LoST的语义排序策略在信息极度压缩时仍能保持形状的可识别性，而几何层级方法则退化为抽象骨架。

| Num Tokens | OctGPT CD | OctGPT FID | LoST CD | LoST FID |
| :--- | :--- | :--- | :--- | :--- |
| 1 / ~219 | 16.923 | 341.174 | 2.271 | 31.649 |
| 4 / ~3615 | 1.865 | 186.611 | 1.328 | 29.255 |
| 16 / ~15031 | 0.809 | 176.137 | 0.723 | 26.565 |
| 64 / ~61962 | 0.209 | 151.393 | 0.382 | 21.133 |
| 512 / ~239004 | 0.034 | 86.098 | 0.234 | 13.591 |

评估边界方面，本文未提供与LDM SOTA（如TRELLIS）的直接对比，因范式不同导致指标不可比。代码未公开，但详细报告了ViT编码器（深度12，维度768）与DiT解码器（深度24，维度1024）的配置，训练使用8xA100 GPU。指标涵盖几何（CD）与语义（FID, DINO），但缺乏物理属性或部件级语义的细粒度评估。

## 关联研究分析

从问题动机看，LoST与FlexTok/Semanticist共享“语义显著性排序”的核心思想，但面临3D特有的监督缺失问题。2D方法可直接利用DINO图像特征进行REPA对齐，而3D形状缺乏直接的语义标签。LoST通过RIDA损失在潜空间间接构建语义结构，这是一种基于关系蒸馏的替代方案。其根源在于3D数据的多视图渲染成本高昂，直接对齐计算不可行，迫使方法转向潜空间内的拓扑对齐。

从方法设计看，LoST与ShapeLLM-Omni同属潜空间AR生成，但Token化策略截然不同。ShapeLLM-Omni依赖3D VAE的固有结构，其前缀解码缺乏语义保证，需依赖后续扩散细化；而LoST通过嵌套Dropout与因果掩码显式训练前缀可用性。这种差异源于对AR生成效率的不同权衡：ShapeLLM-Omni追求最终几何保真度，牺牲了中间态的可解释性；LoST则优先保证任意前缀的语义完整性，以支持交互式生成与早期停止。

## 总结

LoST旨在解决AR 3D生成中Token效率与语义可用性的矛盾，通过语义显著性排序替代几何层级化，使短前缀即可解码出完整形状。其核心创新在于RIDA损失，通过在Triplane潜空间对齐DINO关系结构，解决了3D语义监督缺失问题。实验证明，LoST-GPT在128个Token下实现FID 34.251，显著优于使用1024个Token的ShapeLLM-Omni。然而，该方法严格绑定于Direct3D的Triplane VAE潜空间，未验证其在其他3D表示（如VecSet或SLats）上的泛化能力。当潜空间本身的几何-语义耦合特性发生变化时，RIDA损失构建的语义层级是否仍能保持前缀解码的稳定性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.17995)