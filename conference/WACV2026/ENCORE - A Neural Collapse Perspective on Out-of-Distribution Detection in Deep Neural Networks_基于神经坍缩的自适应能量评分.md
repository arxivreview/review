# WACV2026最新论文 ｜ENCORE : A Neural Collapse Perspective on Out-of-Distribution Detection in Deep Neural Networks ｜基于神经坍缩的自适应能量评分

作者：A. Q. M. Sazzad Sayyed、Nathaniel D. Bastian、Francesco Restuccia

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dd4635919c98)

> 分布外检测（OOD Detection）旨在识别训练分布之外的样本，以消除模型对未见数据的高置信度错误预测。现有后验方法多依赖Logit空间统计量，缺乏对深层网络内部几何结构的理论解释，导致在近邻OOD场景下判别力不足。本文切入点在于利用神经坍缩（Neural Collapse, NC）理论揭示的特征几何特性，通过自适应范数缩放与余弦相似度重构Logit，提升ID与OOD的能量间隙。该方法无需重训练即可在多个基准上取得竞争力，但其性能高度依赖预训练模型是否接近NC理想状态，实际部署中的鲁棒性存疑。

## 研究背景

当深度分类器在训练末期（Terminal Phase of Training, TPT）将交叉熵损失降至极低水平时，其特征空间会涌现出一种对称几何结构，即神经坍缩。这一现象表现为类内特征方差坍缩至零，且类均值形成等角紧框架（Equiangular Tight Frame, ETF）。然而，实际部署的模型往往未完全收敛，导致特征范数不一致且类间正交性受损，使得基于标准Logit的能量分数（Energy Score）在区分语义相近的近邻OOD样本时失效，因为OOD输入在特征空间中并未严格正交于ID子空间。

OOD检测的核心瓶颈在于近邻样本与ID样本在特征空间中的重叠。传统后验方法如最大Softmax概率（MSP）和标准能量分数仅利用输出层信息，忽略了倒数第二层特征中蕴含的几何结构。虽然ViM等方法引入了主空间与零空间的分解，但其固定阈值或能量计算方式未能动态适应不同输入的特征范数差异。本文旨在通过解析NC理论中特征范数与能量间隙的内在联系，构建一种能够自适应修正非理想NC偏差的检测机制，从而在不改变模型架构的前提下提升边界区分度。

## 核心方法

### 方法参照系

本文属于后验检测中的能量评分改进路线。标准流程是直接从预训练分类器的Logit输出计算Log-Sum-Exp能量值。本文的关键差异在于不直接操作原始Logit，而是先提取倒数第二层特征，利用NC理论推导出的几何约束重构Logit计算方式，将检测信号从单纯的概率置信度转向特征空间的几何对齐度。

### 基于NC的余弦Logit重构

标准能量分数对Logit的绝对值敏感，而NC理论指出在理想状态下，分类权重与类均值对齐，且特征应具有一致范数。为解决实际模型中特征范数不一致导致的过置信问题，ENCORE将Logit重构为特征向量与类权重向量的余弦相似度。这一设计动机在于剥离范数影响，仅保留角度信息以反映类别身份，从而在特征空间几何畸变时保持判别稳定性。

$$ z_c = \kappa \cos \theta_c = \kappa \frac{w_c^T h(x)}{\|w_c\|_2 \|h(x)\|_2} $$

其中 $\theta_c$ 为特征与权重夹角，$\kappa$ 为缩放因子。该公式将Logit限制在 $[-\kappa, \kappa]$ 区间内，避免了原始Logit在OOD输入上可能出现的异常高值，为后续能量计算提供了数值稳定性基础。

### 自适应范数缩放机制

仅使用余弦相似度不足以完全恢复NC下的几何结构，因为NC5性质表明OOD特征应正交于ID子空间，其投影范数显著小于ID特征。为量化这一差异，ENCORE引入自适应缩放因子 $\kappa$，其值取决于特征在ID主空间上的投影范数与总范数之比。这一设计动机在于利用NC5的正交性假设，动态放大ID特征的能量贡献，同时抑制OOD特征的影响，从而拉大ID与OOD的能量间隙。

$$ \kappa = \exp\left(\lambda \frac{\|x_p\|}{\|x\|}\right) $$

其中 $x_p$ 为特征在ID主空间的投影，$\lambda$ 为固定常数。最终能量分数为 $E(x) = -\log \sum_{i=1}^C \exp(\kappa \cos \theta_i)$。该机制使得ID样本因投影比接近1而获得较大的 $\kappa$，进而产生更低的能量值（更高置信度），而OOD样本因投影比接近0而获得较小的 $\kappa$，能量值升高，实现了基于几何结构的自适应分离。

## 实验评估

实验在CIFAR-10和ImageNet-1K基准上进行，涵盖ResNet-18、RepVGG-A2、ConvNeXt-Small及ViT-Huge-14等架构。基线覆盖MSP、Energy、ViM、KNN、GEN等主流后验方法，但缺失训练时正则化方法（如Outlier Exposure）及最新VLM方法（如ANTS），限制了与全谱系方法的直接对比。

| 方法 | CIFAR-10 Near-OOD FPR ↓ | CIFAR-10 Near-OOD AUROC ↑ | CIFAR-10 Far-OOD FPR ↓ | CIFAR-10 Far-OOD AUROC ↑ |
| :--- | :--- | :--- | :--- | :--- |
| MSP | 53.61 | 87.69 | 31.22 | 91.03 |
| Energy | 68.18 | 86.95 | 40.41 | 91.80 |
| ViM | 47.69 | 88.55 | 25.68 | 93.17 |
| KNN | 39.42 | 88.73 | 23.73 | 93.13 |
| ENCORE | 36.27 | 91.23 | 21.11 | 94.56 |

在CIFAR-10上，ENCORE在近邻OOD的FPR95上比ViM低11.42%，比KNN低2.75%，表明其几何重构在近邻场景下具有显著优势。在ImageNet-1K（ConvNeXt）上，ENCORE近邻OOD FPR为43.55%，优于ViM的45.41%；远端OOD FPR为14.62%，优于KNN的28.46%。

| 组件 | ImageNet Near-OOD FPR ↓ | ImageNet Far-OOD FPR ↓ |
| :--- | :--- | :--- |
| Only Norm Scaling | 59.68 | 37.76 |
| Only Cosine Similarity | 79.27 | 60.85 |
| Cosine + Norm Scaling | 43.55 | 14.62 |

消融实验显示，单独使用范数缩放或余弦相似度均无法达到最佳性能，二者结合后FPR分别降低16.13%和35.65%（近邻/远端），证明角度信息与范数信息的互补性。PCA主成分数量超过300维后FPR趋于稳定，表明特征空间维度并非主要瓶颈。

评估协议采用标准FPR95和AUROC指标，代码已开源。局限在于未报告置信区间，且未对比计算效率与检测精度的权衡细节（仅提及延迟低于ViM和KNN）。此外，实验未涵盖长尾分布或对抗扰动场景，NC假设在这些极端条件下的有效性未经验证。

## 关联研究分析

从方法设计看，ENCORE与ViM同属主空间利用路线，但ViM将零空间能量作为额外Logit，而ENCORE利用主空间投影比进行自适应缩放。这一差异源于对NC5性质的不同解读：ViM假设OOD能量集中在零空间，ENCORE则假设OOD特征在ID子空间的投影范数显著减小。ENCORE的自适应机制更直接地对应NC理论中特征范数与能量间隙的关系，但在特征空间严重畸变时，PCA主空间可能无法准确表征ID流形，导致缩放因子失效。

从问题动机看，ENCORE与NECO均基于NC理论，但NECO使用固定缩放比例，ENCORE引入样本自适应缩放。这一改进解决了NECO在特征范数分布不均时的过拟合问题，但引入了对PCA估计精度的依赖。与基于扩散模型的SCOPED相比，ENCORE无需生成模型推理，计算效率更高，但缺乏生成模型提供的丰富分布信息，在复杂协变量偏移下的泛化能力可能受限。

## 总结

本文旨在解决后验OOD检测中缺乏理论支撑导致的近邻样本判别力不足问题。通过解析神经坍缩理论，ENCORE发现特征范数与能量间隙的正相关关系，并据此提出基于余弦相似度和自适应范数缩放的Logit重构方法。实验证明该方法在CIFAR-10近邻OOD上FPR95达36.27%，优于ViM和KNN；在ImageNet远端OOD上FPR95达14.62%，显著优于多数基线。其边界在于依赖预训练模型接近NC理想状态，且在PCA主空间估计不准时性能下降。当预训练模型训练轮次不足导致NC假设严重偏离时，自适应缩放因子是否仍能保持有效的ID-OOD分离，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_dd4635919c98)