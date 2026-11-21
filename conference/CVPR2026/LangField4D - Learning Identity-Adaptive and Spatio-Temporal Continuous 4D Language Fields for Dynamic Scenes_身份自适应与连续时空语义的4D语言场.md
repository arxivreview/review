# CVPR2026最新论文 ｜LangField4D: Learning Identity-Adaptive and Spatio-Temporal Continuous 4D Language Fields for Dynamic Scenes ｜身份自适应与连续时空语义的4D语言场

研究机构：浙江大学、华中科技大学

作者：Yichao Xu、Qiaowei Miao、Jinsheng Quan 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_159d59408b5b)

> 动态场景中的开放词汇查询要求模型在时间轴上精确区分物体实例及其状态变化，但现有4D高斯泼溅方法因高斯原语身份随变形场漂移导致语义歧义，且离散状态原型无法捕捉连续的时间过渡。LangField4D通过引入身份自适应高斯分组模块解决身份振荡问题，并基于TetraPlane表示实现连续时空语义学习。该方法在HyperNeRF数据集上将时间敏感查询的vIoU从47.04%提升至64.31%，验证了连续语义建模的有效性，但其对上游分割模型的依赖限制了在复杂动态环境中的泛化能力。

## 研究背景

4D高斯泼溅（4DGS）通过变形场驱动静态高斯原语在时间轴上的运动，实现了动态场景的高效渲染。然而，这种几何驱动的变形机制并未考虑语义一致性：当变形场将高斯原语从物体A边界拉伸至物体B边界时，该高斯原语的身份编码（Identity Encoding）仍保持初始值，导致同一高斯在不同时刻被错误地关联到不同物体实例，即“高斯ID振荡”（Gaussian ID Oscillation）。这一现象使得基于静态身份假设的语义场在动态场景中失效，无法支持细粒度的开放词汇查询。

现有4D语言场方法如4DLangSplat采用双场设计：静态场编码不变语义，动态场通过聚类每帧语义为K个状态原型并插值来建模时间变化。这种离散原型设计引入了“动作边界偏差”（Action Boundary Bias），模糊了物体状态转换的精确时间边界，导致时间敏感查询（如“饼干破碎的时刻”）定位不准。同时，静态身份假设与变形场的几何扭曲相互冲突，使得语义分割在物体运动过程中出现不一致。LangField4D针对这两个核心缺陷，提出将身份编码纳入变形场解码器以实现自适应更新，并用连续潜空间替代离散原型以消除边界偏差。

## 核心方法

### 4DGS变形场与语义场挂载架构

LangField4D基于4DGS框架，其核心流程包括：利用DEVA生成时空一致掩码，提取CLIP语言特征作为监督信号；通过身份自适应高斯分组（IdaGG）模块为每个高斯分配动态身份编码；最后通过TetraPlane表示将离散身份标签映射为连续语言特征。与标准4DGS仅预测位置、旋转、缩放变形不同，本文在变形场解码器中新增身份适应头，将语义维度纳入时空特征分解体系，实现了几何变形与语义身份的统一建模。

### 身份自适应高斯分组（IdaGG）

IdaGG模块解决高斯ID振荡问题，其设计动机在于：静态身份编码无法适应变形场导致的几何扭曲，需根据时空上下文动态调整高斯的实例归属。具体实现中，给定高斯的空间位置 $(x, y, z)$ 和时间戳 $t$，查询HexPlane获得时空特征 $f_d$，该特征隐含了高斯实例归属的变化信息。在多头MLP解码器中集成轻量级身份适应头 $\phi_{id}$，预测身份编码的适应项 $\Delta e$：

$$
e' = e + \phi_{id}(f_d)
$$

其中 $e$ 为初始身份编码，$e'$ 为适应后的动态身份编码。通过可微渲染将 $e'$ 投射到2D视图，利用交叉熵损失 $\mathcal{L}_{2d}$ 和3D正则化损失 $\mathcal{L}_{3d}$ 优化，确保同一实例的高斯在任意时刻获得一致的离散标签 $l$。该机制使高斯原语能够随变形场动态调整其语义归属，消除了因几何扭曲导致的身份歧义。

### 连续时空语义学习（TetraPlane）

TetraPlane表示解决离散状态原型的边界偏差问题，其设计动机在于：K个状态原型的插值无法精确捕捉物体状态的连续变化，需在潜空间中实现任意时间点的语义编码。该机制将语义坐标 $l$ 作为新维度，构建5D耦合空间 $(x, y, z, t, l)$，并将其分解为四个多分辨率2D平面：空间语义平面 $P_{xl}, P_{yl}, P_{zl}$ 编码不变语义，时间语义平面 $P_{tl}$ 融合物体级线索与时间信息。给定高斯 $g$，通过双线性插值从各平面检索特征 $f_c(g)$，经Hadamard积融合后由MLP $\phi_d$ 生成最终语义特征：

$$
f_{sem}(g) = \phi_d \left( \prod_{c \in \{xl, yl, zl, tl\}} f(g)_c \right)
$$

该公式表明，语义特征由空间不变性与时间动态性共同决定。通过交替优化静态与动态语义目标，结合总变分正则化 $\mathcal{L}_{TV}$ 和时间平滑正则化 $\mathcal{L}_{smooth}$，TetraPlane实现了连续、身份感知的语义建模，支持在任意时间点的精确语义查询。

## 实验评估

实验在HyperNeRF和Neu3D数据集上进行，基线包括4DLangSplat、LangSplat、Gaussian Grouping和Feature-3DGS。4DLangSplat是当前4D开放词汇语义理解的最强基线，但本文未对比其他4D生成SOTA方法（如SS4D），因任务目标不同（语义理解 vs 场景生成）。

| 方法 | HyperNeRF mIoU | Neu3D mIoU |
| :--- | :--- | :--- |
| Feature-3DGS | 36.63 | 34.96 |
| Gaussian Grouping | 50.49 | 49.93 |
| LangSplat | 74.92 | 61.49 |
| 4DLangSplat | 80.93 | 55.18 |
| LangField4D | 83.09 | 71.62 |

LangField4D在HyperNeRF上mIoU达83.09%，较4DLangSplat提升2.16%；在Neu3D上mIoU达71.62%，较4DLangSplat提升16.44%。时间敏感查询任务中，LangField4D的vIoU为64.31%，较4DLangSplat的47.04%提升17.27%，Acc从67.65%提升至84.79%。

| 模块配置 | Time-Agnostic mIoU | Time-Varying vIoU |
| :--- | :--- | :--- |
| MLPs | 80.85 | 51.61 |
| MLPs+IdaGG | 82.63 | 52.59 |
| TetraPlane | 81.94 | 60.03 |
| TetraPlane+IdaGG | 83.09 | 64.31 |

消融实验显示，IdaGG对时间不变查询的mIoU提升1.78%（80.85→82.63），对时间敏感查询的vIoU提升0.98%（51.61→52.59）；TetraPlane对时间敏感查询的vIoU提升8.42%（51.61→60.03），对时间不变查询的mIoU提升1.09%（80.85→81.94）。两者结合后，时间敏感vIoU达64.31%，较单独使用TetraPlane提升4.28%，表明身份自适应与连续语义建模存在协同效应。

评估指标包括mIoU、vIoU和Acc，但未报告计算效率或内存占用。实验在单张RTX A6000 GPU上进行，超参数遵循4D-GS默认设置。论文未提供代码URL，可复现性受限。

## 关联研究分析

从问题动机看，LangField4D与4DLangSplat均针对4D动态场景的开放词汇查询，但4DLangSplat假设高斯身份静态不变，而LangField4D识别出变形场导致的身份振荡问题。这一差异源于任务特性：4DLangSplat的离散状态原型设计适合粗粒度时间分割，但无法处理物体边界处的细粒度语义转换；LangField4D的连续TetraPlane表示则通过潜空间插值消除了边界偏差，但依赖DEVA提供的精确掩码作为监督。

从方法设计看，LangField4D与Gaussian Grouping共享身份编码学习思路，但Gaussian Grouping针对静态3D场景，身份编码固定；LangField4D将身份编码纳入变形场解码器，实现动态适应。与HexPlane相比，LangField4D将语义坐标 $l$ 作为新维度扩展至5D空间，而HexPlane仅分解4D时空特征。这种扩展使语义场能够显式编码实例身份，但增加了计算复杂度。

## 总结

LangField4D解决的核心矛盾是4DGS变形场导致的身份振荡与离散状态原型的边界偏差。其切入点在于将身份编码纳入变形场解码器实现动态适应，并用连续潜空间替代离散原型。方法通过IdaGG模块和TetraPlane表示，在HyperNeRF上将时间敏感vIoU从47.04%提升至64.31%，在Neu3D上将mIoU从55.18%提升至71.62%。论文自身暴露的局限在于依赖DEVA进行精确分割和身份标注，当上游分割模型在复杂动态场景中失效时，LangField4D的语义一致性将随之退化。当DEVA无法准确区分快速运动或遮挡物体时，IdaGG的身份适应机制是否仍能维持语义一致性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_159d59408b5b)