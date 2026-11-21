# HuggingFace最新推荐论文 ｜SplatAnything: Gaussian Spacing Normalization for Feed-forward 3DGS across Arbitrary Scenes ｜高斯间距归一化：前馈式3D高斯泼溅的跨场景泛化

研究机构：浙江大学

作者：Hao Yu、Zhenwei Wang、Yongzhen Hu 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2611.08264)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2611.08264)

> 导读：前馈式3D高斯泼溅（3DGS）旨在通过单次网络推理实现跨场景泛化，但现有方法在跨尺度场景下泛化能力受限。主流方法依赖几何基础模型输出的径向距离归一化（RDNorm）空间，该空间未直接约束相邻高斯中心的间距，导致高斯尺度监督存在歧义。本文提出高斯间距归一化（GSNorm），通过计算场景级中位高斯间距作为归一化因子，将几何与高斯预测统一至一致的空间参考系。该机制有效消除了尺度监督歧义，显著提升了前馈3DGS在跨域、跨尺度及外推视角下的重建质量。然而，该方法高度依赖几何基础模型的先验，在极端稀疏或无纹理场景下的鲁棒性仍存疑。

## 研究背景

当系统需要从少量图像重建3D场景时，前馈式3DGS通过直接预测高斯参数消除了逐场景优化的计算成本。为了处理不同场景的尺度差异，现有方法通常引入几何基础模型提取深度与位姿，并采用径向距离归一化（RDNorm）将重建几何缩放至数值稳定范围。然而，RDNorm仅规范了全局径向统计量，未直接规范相邻像素反投影3D点之间的空间距离，即高斯间距。由于高斯尺度需与局部高斯间距匹配以实现表面覆盖，RDNorm下高斯间距的剧烈波动导致相似局部观测对应不同的高斯尺度目标，引发监督歧义。

前馈式重建的泛化能力与细节平衡是该领域的核心瓶颈。PixelSplat等早期方法通过像素对齐实现快速推理，但牺牲了稀疏视图下的几何一致性；YoNoSplat等后续工作引入无位姿联合估计，但在极端稀疏视图下仍不稳定。这些方法均继承了RDNorm空间，未能解决跨场景尺度变化带来的高斯尺度监督歧义。SplatAnything精准定位了这一被忽略的归一化空间缺陷，提出GSNorm以规范高斯间距，为前馈3DGS的跨场景泛化提供了更一致的空间参考。

## 核心方法

### 方法参照系

前馈式3DGS的标准流程为：输入图像，通过几何基础模型预测深度与位姿，随后在归一化空间内预测高斯属性。本文问题与该通用流程的关键差异在于：标准流程直接继承几何模型的RDNorm空间，而本文在几何预测后、高斯预测前，引入GSNorm重新缩放坐标，将高斯预测空间与高斯间距统计量对齐。

### 高斯间距定义与RDNorm的局限

在像素对齐预测范式下，每个有效像素反投影的3D点即为高斯中心。高斯间距 $d_i(u)$ 定义为相邻像素反投影点间的空间距离。在针孔相机模型下，局部高斯间距近似为：

$$ d_i(u) \approx D_i(u) \sqrt{\frac{1}{f_{x,i} f_{y,i}}} $$

其中 $D_i(u)$ 为深度，$f_{x,i}, f_{y,i}$ 为焦距。RDNorm的归一化因子 $s_r$ 基于所有有效像素到参考相机原点的平均径向距离计算：

$$ s_r = \frac{1}{N_p} \sum_{i=1}^N \sum_{u \in \Omega_i} \|P_i(u)\|_2 $$

RDNorm规范了全局径向统计量，但归一化后的高斯间距 $d_r(u) \approx D_i(u) / (s_r \sqrt{f_{x,i} f_{y,i}})$ 仍随场景尺度和相机配置剧烈变化。这种变化导致高斯尺度监督目标不一致，模型易在小物体场景产生孔洞，或在大型室外场景产生过度平滑。

### 高斯间距归一化（GSNorm）

为消除尺度监督歧义，GSNorm将场景级归一化因子定义为中位高斯间距。对于任意场景级尺度 $s$，特征高斯间距为 $d_s(u) \approx D_i(u) / (s \sqrt{f_{x,i} f_{y,i}})$。GSNorm选择 $s_g$ 使得场景级中位高斯间距被规范化：

$$ s_g = \text{median}_{i, u \in \Omega_i} \left( D_i(u) \sqrt{\frac{1}{f_{x,i} f_{y,i}}} \right) $$

利用 $s_g$ 对几何、深度和相机平移进行重新缩放：$P_g = P / s_g$，$D_g = D / s_g$，$t_g = t / s_g$。GSNorm在保留局部几何变化相对关系的同时，规范了场景级中位高斯间距，为高斯尺度预测提供了直接关联表面覆盖的参考系，从而缓解了跨场景和跨视角的泛化瓶颈。

## 实验评估

实验在ScanNet、NRGBD、DL3DV、Tanks & Temples、Mip-NeRF 360、ETH3D和DTU七个数据集上进行，评估指标为DISTS和LPIPS。基线覆盖包括无位姿方法（AnySplat, YoNoSplat, DA3-GS, Mirror2-GS, QuerySplat）和有位姿方法（DepthSplat, TokenGS, tttLRM, ReSplat等）。

| 方法 | ScanNet DISTS↓ | NRGBD DISTS↓ | DL3DV DISTS↓ | Tanks & Temples DISTS↓ | Mip-NeRF 360 DISTS↓ | ETH3D DISTS↓ | DTU DISTS↓ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| YoNoSplat | 0.265 | 0.285 | 0.375 | 0.424 | 0.405 | 0.321 | 0.484 |
| Mirror2-GS | 0.193 | 0.235 | 0.246 | 0.306 | 0.283 | 0.205 | 0.347 |
| SplatAnything (Ours) | 0.184 | 0.195 | 0.221 | 0.252 | 0.233 | 0.147 | 0.229 |

在4-64输入视图设定下，SplatAnything在七个数据集上均取得最优DISTS分数，较Mirror2-GS在ETH3D上降低0.058，在DTU上降低0.118，验证了GSNorm在跨域和跨尺度场景下的泛化优势。

消融实验对比了RDNorm、RDNorm+尺度校准与GSNorm。

| 归一化空间 | 1视图 DISTS↓ | 4视图 DISTS↓ | 8视图 DISTS↓ | 16视图 DISTS↓ | 32视图 DISTS↓ | 64视图 DISTS↓ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Radial Distance Norm. | 0.308 | 0.223 | 0.223 | 0.218 | 0.225 | 0.224 |
| RDNorm + Scale Calibration | 0.323 | 0.249 | 0.252 | 0.245 | 0.253 | 0.234 |
| Gaussian Spacing Norm. (Ours) | 0.294 | 0.198 | 0.196 | 0.190 | 0.197 | 0.217 |

GSNorm在所有视图数量下均优于RDNorm。RDNorm+尺度校准虽缓解了孔洞问题，但导致过度平滑，证明事后尺度校正无法解决RDNorm引入的监督歧义。评估协议引入了外推视角和输入稀疏度控制，但主报指标DISTS/LPIPS对高频细节敏感，可能掩盖几何结构上的潜在缺陷。论文未提供代码URL，复现依赖WorldMirror 2.0等闭源或特定模型。

## 关联研究分析

从问题动机看，YoNoSplat与SplatAnything均致力于消除对SfM预处理的依赖，实现无位姿前馈重建。YoNoSplat通过共享ViT编码器提取特征并联合估计位姿，但其像素对齐策略在跨尺度场景下易产生浮点伪影。SplatAnything指出，YoNoSplat等方法的泛化瓶颈并非仅源于位姿估计误差，更深层的原因在于其继承的RDNorm空间导致高斯间距不一致。SplatAnything通过GSNorm直接规范高斯间距，为像素对齐范式提供了更稳定的尺度参考，这是YoNoSplat未探索的归一化空间盲区。

从方法设计看，DepthSplat与SplatAnything同属“几何先验+高斯预测”框架。DepthSplat结合单目深度先验与多视图匹配，但其高斯属性预测仍在RDNorm空间内进行。SplatAnything在DepthSplat的几何预测后插入了GSNorm重缩放步骤，将高斯预测空间与高斯间距统计量对齐。DepthSplat在大型视角外推下几何精度受限，而SplatAnything通过GSNorm缓解了尺度监督歧义，在ETH3D和DTU等跨尺度数据集上DISTS显著低于DepthSplat（0.147 vs 0.445，0.229 vs 0.370）。

## 总结

前馈式3DGS在跨场景泛化时面临高斯尺度监督歧义的核心矛盾，现有方法因继承RDNorm空间而无法规范高斯间距。SplatAnything抓住这一归一化空间缺陷，提出GSNorm，通过场景级中位高斯间距重新缩放坐标，为高斯预测提供一致空间参考。实验表明，SplatAnything在七个跨域数据集上DISTS均优于基线，在ETH3D上达到0.147，验证了GSNorm的有效性。然而，该方法高度依赖几何基础模型的先验，在极端稀疏或无纹理场景下可能失效，且仅重建输入视图可见区域，未观测区域存在孔洞。当几何基础模型在极端稀疏输入下无法恢复可靠几何时，GSNorm的归一化因子计算是否会因有效像素过少而失去鲁棒性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2611.08264)