# HuggingFace最新推荐论文 ｜PackForcing: Short Video Training Suffices for Long Video Sampling and Long Context Inference ｜有界上下文下的时空压缩自回归视频生成

研究机构：复旦大学

作者：Xiaofeng Mao、Shaohao Rui、Kaining Ying 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.25730)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.25730)

> 自回归长视频生成面临误差累积与KV缓存内存线性增长的双重瓶颈，现有截断或滑动窗口策略导致长程语义丢失。PackForcing通过三分区KV缓存与双分支时空压缩，在严格限制内存的前提下实现24倍时长外推。该方法以5秒短片段训练生成2分钟视频，验证了压缩保留优于截断丢弃的假设，但其对复杂动态场景的细节保持能力仍存疑。

## 研究背景

双向扩散模型因二次方计算复杂度无法支持流式实时生成，自回归范式通过块状生成与KV缓存将复杂度降至线性，但引入了两个核心矛盾：预测误差随时间步长复利式增长导致语义漂移，以及KV缓存规模随视频时长线性膨胀超出单卡显存限制。以2分钟832×480@16FPS视频为例，全注意力上下文需约749K令牌，占用约138GB显存，远超商用GPU预算。

主流解决方案分为两类：一是历史截断或滑动窗口，如CausVid与Rolling Forcing，虽控制内存但不可逆地丢弃中间历史，导致长程一致性崩溃；二是注意力沉点与参与式压缩，如DeepForcing，通过查询重要性保留关键令牌，但仍依赖激进缓冲截断，造成中间记忆永久丢失。Self-Forcing虽通过自生成帧训练缓解曝光偏差，但在训练时长外仍出现严重误差累积，其CLIP分数在60秒内从33.89降至27.12。PackForcing的切入点在于将“选择保留”改造为“压缩保留”，通过显式时空压缩而非截断来维持全量历史的低分辨率表示，从而打破内存与一致性的刚性权衡。

## 核心方法

### 三分区KV缓存架构

自回归视频生成的标准流程是顺序缓存所有历史块的KV对，导致上下文长度随时间线性增长。PackForcing将历史上下文解耦为三个功能分区：Sink令牌（全分辨率，永不驱逐）、Mid令牌（压缩后动态路由）与Recent/Current令牌（全分辨率，双分辨率移位）。该设计动机在于解决单一驱逐策略无法同时兼顾全局语义锚定与局部细节保真的问题。Sink令牌锁定场景布局与主体身份，Mid令牌以极低分辨率保留中间记忆，Recent令牌保证局部时序连贯。

$$
|C_l| = N_{sink} B_f n + N_{mid} \cdot N_c + (B_f + 1) n
$$

该公式表明注意力上下文大小被严格限定为常数，与视频总时长$T$无关，实现了$O(1)$注意力复杂度。

### 双分支时空压缩与增量RoPE调整

Mid分区需要约32倍的令牌缩减，单路径压缩器面临空间下采样丢失纹理或语义池化破坏结构的权衡。PackForcing采用双分支架构：HR分支通过级联3D卷积保留细粒度结构，LR分支通过像素空间池化与VAE重编码保留全局布局，两者逐元素相加融合。该设计动机在于解决激进压缩下结构-语义信息失衡的问题。

$$
\mathbf{h}_{comp} = \mathbf{h}_{HR} + \mathbf{h}_{LR}
$$

其中$\mathbf{h}_{HR}$来自4阶段3D卷积（2×时间, 8×空间压缩），$\mathbf{h}_{LR}$来自池化后VAE重编码。当驱逐最旧压缩块时，Sink与Mid间出现位置间隙，破坏RoPE连续性。PackForcing利用RoPE乘法性质，仅对Sink键施加时间轴增量旋转：

$$
\mathbf{k}'_j = \mathbf{k}_j \cdot e^{i\theta_t \delta} \cdot \mathbf{1}_h \cdot \mathbf{1}_w
$$

该操作以<0.1%推理开销修正位置间隙，避免全量缓存重算，确保注意力模式在动态驱逐下保持连续。

## 实验评估

实验基于Wan2.1-T2V-1.3B骨干，在VBench-Long上评估60s与120s生成，对比CausVid、Self-Forcing、LongLive、Rolling Forcing与DeepForcing。基线覆盖蒸馏、自强制、滑动窗口与沉点压缩路线，但缺失Pyramid Forcing等最新头感知缓存方法。

| 方法 | 60s CLIP | 120s Dynamic Degree | 120s Subject Consistency |
| :--- | :--- | :--- | :--- |
| CausVid | 31.44 | 48.43 | 62.15 |
| Self-Forcing | 30.71 | 50.00 | 56.14 |
| PackForcing | 33.54 | 56.25 | 63.16 |

PackForcing在60s CLIP分数上领先Self-Forcing 2.83分，在120s Dynamic Degree上超越最强基线CausVid 7.82分。Self-Forcing从60s到120s的Subject Consistency下降6.01分，而PackForcing仅下降1.01分，验证了Sink令牌锚定全局语义的有效性。

消融实验显示，$N_{sink}=8$在动态度（49.84）与图像质量（73.18）间取得最优平衡，消耗<2%令牌预算。动态上下文选择相比FIFO策略提升Subject Consistency 0.8分与CLIP 0.12分，证明基于查询亲和力的路由优于刚性时间驱逐。

评估边界方面，VBench-Long对细粒度空间一致性不敏感，且未报告置信区间。代码已开源，超参数完整披露（AdamW, lr=2e-6, batch=8），单H200 GPU可复现120s生成。

## 关联研究分析

从问题动机看，PackForcing与DeepForcing均针对KV缓存无限增长问题，但DeepForcing依赖查询重要性选择保留令牌，本质上仍是“丢弃”策略，导致中间记忆不可逆丢失；PackForcing通过双分支压缩将丢弃令牌转化为低分辨率表示，保留了全量历史的结构信息。这一差异源于视频令牌的高冗余特性：文本令牌已高度紧凑，选择保留即可；视频令牌编码密集时空网格，压缩保留能捕获更多互补信息。

从方法设计看，PackForcing与Spatia等显式几何记忆方法形成对比。Spatia维护3D点云作为显式空间记忆，解决空间结构漂移；PackForcing通过压缩KV缓存隐式保留空间信息，无需额外几何结构。前者在3D一致性上可能更优，但引入点云维护复杂度；后者在实时性上更具优势，但压缩带来的信息损失在复杂动态场景中是否导致细节缺失，论文未给出定量回答。

## 总结

PackForcing解决的核心矛盾是长程一致性所需的广阔上下文与硬件限制下的有界内存之间的冲突。其切入点在于识别出“截断丢弃”策略的不可逆性，通过双分支时空压缩将中间历史转化为低分辨率表示，结合增量RoPE调整维持位置连续性。该方法以5秒训练片段实现24倍时长外推，在120s生成中Dynamic Degree达56.25，Subject Consistency仅下降1.01分。其边界在于压缩率固定为128倍时空体积，对高频动态细节的保留能力未充分验证；当场景包含快速运动或复杂纹理变化时，32倍令牌缩减是否足以维持局部时序连贯性，论文未提供针对性实验。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.25730)