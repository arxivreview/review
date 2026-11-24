# CVPR2026最新论文 ｜ReFTA: Breaking the Weight Reconstruction Bottleneck in Tensorized Parameter-Efficient Fine-Tuning ｜无重构张量低秩适配

作者：Jingjing Zheng、Anda Tang、Qiangqiang Mao 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_051a4fafc9b1)

> 张量分解在参数高效微调（PEFT）中虽能捕捉跨层依赖并压缩参数，但直接应用导致训练时反复重构权重张量，带来高昂的计算与内存开销，阻碍了大规模部署。现有基于Tucker或Tensor-Train分解的方法因多秩超参耦合及重构瓶颈，难以在保持低参数量的同时实现高效训练。ReFTA利用张量代数性质交换特征融合与张量乘积顺序，在特征空间直接计算，彻底消除权重重构需求。该方法在视觉任务上以极少参数超越LoRA，但在NLU任务上性能持平，其理论泛化界为张量PEFT提供了首个形式化保证，然而其依赖固定可逆变换的假设在异构架构下的普适性存疑。

## 研究背景

当预训练模型权重被堆叠为高阶张量时，其内在结构并非各层独立，而是存在跨层冗余与依赖。矩阵分解方法如LoRA仅对单层权重进行低秩近似，忽略了这种跨层结构，导致参数量随层数线性增长。张量分解旨在利用这种跨层低秩结构进一步压缩参数，但传统T-SVD分解后的重构步骤要求每次前向传播都重建完整权重张量，这在大规模模型中成为计算瓶颈。

PEFT领域的主流路线已从加法式模块转向重参数化低秩更新，LoRA确立了无推理开销的标准。然而，随着模型规模扩大，固定秩的矩阵分解在复杂任务上面临表达力瓶颈，且参数量仍显冗余。张量分解路线如LoRETTA和FedTT试图通过Tucker或TT分解解决此问题，但引入了多个相互依赖的秩超参数，且训练过程中的张量重构带来了$O(dnK)$的内存复杂度，使得其在资源受限场景下难以落地。ReFTA的切入点在于识别出重构开销是张量PEFT的实际部署障碍，而非分解本身，因此致力于在保留张量低秩优势的同时，通过代数变换消除重构步骤。

## 核心方法

### 张量SVD与主成分初始化参照系

ReFTA建立在Tensor SVD（T-SVD）基础之上，将预训练权重矩阵堆叠为三阶张量$W_0 \in \mathbb{R}^{d \times n \times K}$，其中$K$为层数。参照PiSSA的主成分初始化思想，ReFTA首先通过T-SVD将$W_0$分解为主成分张量$W_{pri}$和残差张量$W_{res}$，仅微调主成分部分以降低初始化量化误差。与Tucker分解不同，T-SVD基于张量乘积（t-product）定义，保留了矩阵SVD的代数性质，使得分解后的因子具有明确的几何解释。

### 无重构特征融合机制

传统张量PEFT在训练时需将分解后的因子重构回权重空间，即计算$W_{int} \times_3 U^\top$，这一过程在前向和反向传播中重复发生，导致高昂开销。ReFTA的关键创新在于利用模式乘积的可交换性，将特征融合操作$\times_3 U^\top$移至输入特征$X$之后，从而在特征空间直接计算适配结果。具体而言，对于第$k$层，定义可训练的低秩对$A_k \in \mathbb{R}^{d \times R_k}$和$B_k \in \mathbb{R}^{R_k \times n}$，其中$R_k$由张量奇异值阈值算法确定。前向传播公式为：

$$ H = H_{int} \times_3 U_0^\top + W_{res} \times_1 X $$

其中$H_{int}$的第$k$个切片为$X A_k B_k$，$U_0$为固定的可逆线性变换（如DCT）。该公式的物理含义是：先在特征空间通过低秩矩阵$A_k, B_k$进行线性变换，再通过$U_0^\top$进行跨层特征融合，最后加上冻结的残差项。这一设计消除了对$W_{int}$的显式重构，将内存复杂度从$O(dnK)$降低至$O(mnK)$（$m$为批大小，通常$m \ll d$），显著提升了训练效率。

### 单秩配置与理论泛化界

ReFTA采用单一张量秩超参数$R$控制所有层的秩分配，通过T-SVD的奇异值阈值自动确定每层的$R_k$，避免了Tucker/TT方法中多秩超参的调优负担。此外，ReFTA提供了首个张量PEFT的理论泛化界。设损失函数为$l(g)$-Lipschitz，假设类为$\mathcal{F}_{ReFTA} = \{\phi(W \times_1 x^\top) \mid \|W\|_2 \le B\}$，则期望测试误差的上界为：

$$ \mathbb{E}[g(f_W(x), y)] \le \hat{g} + l(g)\pi l(\phi) \sqrt{\frac{R n K}{m}} + \sqrt{\frac{9 \log \frac{2}{\delta}}{2m}} $$

该界表明泛化误差与张量秩$R$的平方根成正比，理论上支持了低秩张量适配在大规模模型中的有效性，为ReFTA的设计提供了形式化依据。

## 实验评估

ReFTA在ViT-Base、ViT-Large、ViT-Huge及RoBERTa-Large上进行了评估，覆盖图像分类（OxfordPets, StanfordCars, FGVC, CIFAR100）和NLU任务（CoLA, RTE等）。基线包括LoRA、PiSSA、LoRETTA、WeGeFT等，但缺失AdaLoRA等动态秩方法。在ViT-Large上，ReFTA (R=15) 以61K参数实现了85.67%的平均准确率，超越LoRA (r=16, 1.57M参数) 的79.99%和LoRETTA (r=5, 132K参数) 的78.51%，参数量仅为LoRA的3.9%。

| 模型 | 方法 | 参数量 | 平均准确率 (%) |
| :--- | :--- | :--- | :--- |
| ViT-Large | LoRA (r=16) | 1.57M | 79.99 |
| ViT-Large | PiSSA (r=8) | 835K | 85.09 |
| ViT-Large | LoRETTA (r=5) | 132K | 78.51 |
| ViT-Large | ReFTA (R=15) | 61K | 85.67 |

消融实验显示，固定DCT作为可逆变换$U_0$比随机正交矩阵更优，且在视觉任务上提升达3-5%。学习$U_0$仅带来边际改善，表明预定义变换已足够。在CommonsenseQA上，ReFTA (r=15) 在Mistral-7B上取得86.81%准确率，与LoRA (r=8) 的86.90%持平，但参数量减少约94%。

评估边界方面，实验仅在Transformer架构上进行，未验证非Transformer模型。代码已开源，但超参数调优细节未完全披露。NLU任务中ReFTA与LoRA性能持平，暗示在文本任务上张量跨层依赖的增益可能有限，或受限于固定秩配置。

## 关联研究分析

从方法设计看，ReFTA与PiSSA共享主成分初始化思想，但PiSSA局限于单层矩阵分解，而ReFTA扩展至跨层张量分解。关键差异在于ReFTA通过代数变换消除了重构步骤，而PiSSA仍需逐层计算。这一差异源于ReFTA利用了T-SVD的t-product性质，使得特征融合与张量乘积可交换，而矩阵SVD不具备此性质。然而，ReFTA依赖固定可逆变换$U_0$，而PiSSA的初始化基于SVD，两者在频域利用上存在潜在交集但机制不同。

从问题动机看，ReFTA与LoRETTA同属张量分解路线，但LoRETTA基于Tucker分解，需处理多秩超参且存在重构开销。ReFTA的单秩配置和无重构设计使其在参数效率上超越LoRETTA 50%，但LoRETTA在NLU任务上的表现可能更稳定，因为Tucker分解能更灵活地捕捉各模式间的交互。ReFTA在NLU任务上性能持平LoRA，可能源于其固定DCT变换未能充分捕捉文本数据的局部依赖，而Tucker分解的灵活性在此类任务上更具优势。

## 总结

ReFTA旨在解决张量分解PEFT中重构开销导致的部署瓶颈，通过交换特征融合与张量乘积顺序，在特征空间直接计算适配结果，消除了权重重构需求。该方法在ViT-Large上以61K参数实现85.67%准确率，超越LoRA 5.6%且参数量减少96%，证明了无重构张量适配的有效性。然而，其在NLU任务上性能仅与LoRA持平，且依赖固定可逆变换，暗示其在异构架构或复杂文本任务上的泛化能力受限。当模型层间结构差异显著时，固定DCT变换是否仍能有效捕捉跨层依赖，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_051a4fafc9b1)