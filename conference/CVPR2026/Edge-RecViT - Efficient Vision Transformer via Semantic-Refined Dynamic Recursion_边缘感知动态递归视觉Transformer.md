# CVPR2026最新论文 ｜Edge-RecViT: Efficient Vision Transformer via Semantic-Refined Dynamic Recursion ｜边缘感知动态递归视觉Transformer

作者：YiZhou Li、Jinyi Xu、Mingyu Yin 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_21471707f34e)

> 视觉Transformer（ViT）在边缘部署中面临计算冗余与参数膨胀的双重瓶颈，现有Token自适应方法虽能降低浮点运算量（FLOPs），却因全局注意力机制导致语义贫乏的前景中心Token被过度计算，且深层参数因早退机制而闲置。本文切入点在于利用边缘Token的结构丰富性替代前景重要性作为计算分配依据，并引入递归参数共享以消除层级冗余。通过边缘感知排名器与共享隐藏层结合，Edge-RecViT在ImageNet-1K上以23.2M参数和24.39 GFLOPs达到82.0% Top-1准确率，较DeiT-Base减少73%参数，但其递归结构在密集预测任务中的泛化能力尚未验证。

## 研究背景

ViT将图像切分为固定大小的Patch并投影为Token序列，通过自注意力机制建模长程依赖。然而，自注意力的二次方复杂度导致高分辨率输入下计算量激增。为缓解此问题，Token自适应方法（如DynamicViT、A-ViT）在层间插入过滤模块，动态决定每个Token是否进入下一层。这些方法通常基于前景重要性分配计算深度，但可视化显示前景中心区域（色彩均匀、语义稀疏）被分配了最深计算，而富含结构信息的边缘Token反而早退。

主流Token自适应路线存在两个核心瓶颈：一是全局注意力使相似前景Token形成高相似度簇，导致排名器误判其重要性；二是即使Token早退，模型仍保留全量独立层参数，深层权重利用率低，部署收益有限。参数共享是解决冗余的自然选择，但ViT的层级抽象特性要求不同层执行不同变换，全层共享易导致表示坍缩。Edge-RecViT的切入点在于：边缘Token缺乏相似对应物，其结构复杂性可作为更可靠的计算深度信号；同时，Token级异质性（不同Token走不同递归路径）可打破全层共享的均匀性，使递归结构在ViT中可行。

## 核心方法

### 方法参照系

标准ViT采用固定深度与独立层参数，Token自适应方法（如DynamicViT）在层间插入轻量预测模块决定Token去留，但保留全量参数。本文问题与该通用流程的关键差异在于：将计算分配依据从“前景重要性”转向“边缘语义丰富度”，并将独立层参数替换为共享递归层，以同时解决计算冗余与参数冗余。

### 边缘感知排名器（EARR）

EARR置于Patch Embedding之后、Transformer之前，通过两层MLP预测每个Token的计算深度。设计动机是解决现有排名器因全局注意力导致的“前景中心过度计算”问题：边缘Token在自注意力中缺乏相似对应物，其结构复杂性（如边界、纹理）是更可靠的语义丰富度指标。EARR将Token表示 $X' \in \mathbb{R}^{C \times N}$ 映射为深度Logits：

$$
H^{(1)} = \text{GELU}(W_1 X'), \quad Z = W_2 H^{(1)}
$$

其中 $W_1 \in \mathbb{R}^{2C \times C}$，$W_2 \in \mathbb{R}^{L \times 2C}$，$L=12$ 为最大深度。对每个Token $i$，通过Softmax归一化得到深度概率 $p_i$，选择最大概率对应的深度 $d_i = \arg\max_l p_{i,l}$。[CLS] Token强制分配最大深度 $d_0=L$，确保全局语义聚合。该设计使结构复杂的边缘Token获得更深递归，而背景Token早退，实现计算资源向语义关键区域的精准分配。

### 递归Transformer块与正则化

递归块包含Head、共享Hidden、Tail三层，参数分别记为 $\theta_h, \theta_r, \theta_t$。设计动机是解决Token自适应方法中“深层参数闲置”问题：全层共享通常导致表示坍缩，但EARR赋予每个Token不同递归路径，引入Token级异质性，恢复功能多样性。Token $i$ 的输出计算为：

$$
y_i^{(l)} = \begin{cases} f(x_i, \theta_h), & l=1 \\ f(y_i^{(l-1)}, \theta_r), & 1 < l \leq 11 \\ f(y_i^{(10)}, \theta_t), & l=L \end{cases}
$$

Token在 $l=d_i$ 处终止，输出 $y_i = y_i^{(d_i)}$。为防止排名器坍缩，引入两项正则化：STB-Loss约束Logits尺度，防止极端深度分配；DU-Loss确保期望深度分布与实际分布一致，避免Token集中于浅层或深层。总损失为：

$$
\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{CCE}} + \lambda_{\text{stb}} \mathcal{L}_{\text{stb}} + \lambda_{\text{du}} \mathcal{L}_{\text{du}}
$$

其中 $\mathcal{L}_{\text{CCE}}$ 为置信度加权交叉熵，$\mathcal{L}_{\text{stb}} = \frac{1}{N}\sum_{i=1}^N (\log \sum_{l=1}^L e^{z_{i,l}})^2$，$\mathcal{L}_{\text{du}} = \sum_{l=1}^L |E_l - A_l|$。该设计使共享层在保持参数效率的同时，通过动态递归实现层级特征学习。

## 实验评估

| 模型 | 参数量 (M) | FLOPs (G) | CIFAR-10 (%) | CIFAR-100 (%) |
|---|---|---|---|---|
| Edge-RecViT (Tiny) | 1.6 | 1.72 | 99.00±0.3 | 90.11±0.4 |
| DeiT-Ti | 5.8 | 2.6 | 98.19 | 86.61 |
| Edge-RecViT (Small) | 6.0 | 6.36 | 99.05±0.2 | 90.30±0.2 |
| DeiT-S | 22.2 | 9.2 | 98.63 | 88.71 |
| Edge-RecViT (Base) | 23.2 | 24.39 | 99.16±0.2 | 90.78±0.2 |
| DeiT-B | 86.0 | 35.2 | 99.1 | 90.8 |

实验在ImageNet-1K、CIFAR-10/100上进行，基线覆盖DeiT、ViT、EA-ViT、TinyViT，但缺失ToMe、SPOT等最新Token合并方法。Edge-RecViT-Base以23.2M参数和24.39 GFLOPs达到82.0% Top-1（ImageNet-1K），较DeiT-B减少73%参数和31% FLOPs，精度提升0.2%。在CIFAR-10/100上，Edge-RecViT-Base达到99.16%/90.78%，略优于DeiT-B的99.1%/90.8%。

| 变体 | 参数量 (M) | FLOPs (G) | Top-1 (%) |
|---|---|---|---|
| No Ranker (Fixed Depth) | 35.2 | 82.1 | — |
| With Ranker (Ours) | 24.4 | 82.0 | — |
| Non recursion (Full Independent) | 24.4 | 81.4 | — |
| Recursion (Middle layers Shared) | 24.4 | 82.0 | 82.0 |
| Recursion (Full layers Shared) | 24.3 | 68.9 | 68.9 |

消融显示，EARR将FLOPs从82.1G降至82.0G（注：此处表格数据与正文描述存在不一致，正文称FLOPs减少30.5%，但表格显示固定深度与动态深度FLOPs接近，可能因表格为Base配置下的局部消融），精度基本不变。参数共享策略中，中间层共享（Middle layers Shared）达到82.0% Top-1，优于全独立（81.4%）和全共享（68.9%），验证了“Head/Tail独立+中间共享”设计的必要性。移除STB-Loss导致Top-1降至69.2%，移除DU-Loss降至61.1%，表明正则化对排名稳定性至关重要。

评估仅报告Top-1准确率、参数量和FLOPs，未提供实际硬件延迟或能效数据，与“硬件感知设计至关重要”的领域共识存在差距。代码开源，训练使用8×A100-40GB GPU，300 epochs，AdamW优化器，超参数公开，可复现性良好。

## 关联研究分析

从问题动机看，Edge-RecViT与DynamicViT、A-ViT同属Token自适应路线，但计算分配依据不同：DynamicViT基于前景重要性，Edge-RecViT基于边缘语义丰富度。这一差异源于对“语义丰富度”定义的不同：前者假设前景整体重要，后者认为边缘是结构信息的关键载体。根源在于全局注意力机制的副作用——相似前景Token被过度强化，而边缘Token因缺乏相似对应物被低估。Edge-RecViT通过EARR显式建模边缘特性，纠正了这一偏差，但EARR作为前置模块，其预测是否受限于浅层特征、能否准确捕捉深层语义边界，论文未给出验证。

从方法设计看，Edge-RecViT与EA-ViT、MiniViT同属参数共享路线，但共享粒度不同：EA-ViT采用嵌套弹性架构，仅共享部分参数；Edge-RecViT采用全层递归共享，仅Head/Tail独立。这一差异源于对“表示坍缩”的解决策略不同：EA-ViT通过弹性子模型避免坍缩，Edge-RecViT通过Token级异质性（不同递归深度）打破均匀性。Edge-RecViT的参数压缩率更高（73% vs EA-ViT的有限减少），但递归结构在密集预测任务（如分割）中的适用性未探索，其动态深度分配是否保留空间细节，是任务特性决定的潜在盲区。

## 总结

Edge-RecViT要解决的核心矛盾是ViT在边缘部署中计算冗余与参数膨胀的共存问题。现有Token自适应方法降低FLOPs但保留全量参数，参数共享方法减少参数但易导致表示坍缩。本文抓住“边缘Token结构丰富性”与“Token级异质性”两个被忽略的点：前者提供更可靠的计算深度信号，后者使全层共享在ViT中可行。通过EARR与递归块结合，Edge-RecViT在ImageNet-1K Base上以23.2M参数和24.39 GFLOPs达到82.0% Top-1，较DeiT-B减少73%参数。其边界在于：实验仅覆盖分类任务，未验证递归结构在密集预测中的空间细节保留能力；EARR作为前置模块，其预测精度是否受限于浅层特征，论文未给出回答。当输入包含复杂纹理或模糊边界时，EARR能否准确区分“结构丰富”与“语义贫乏”，是递归动态分配机制鲁棒性的关键考验。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_21471707f34e)