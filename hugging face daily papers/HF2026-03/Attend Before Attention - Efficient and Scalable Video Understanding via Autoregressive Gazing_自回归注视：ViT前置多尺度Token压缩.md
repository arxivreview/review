# HuggingFace最新推荐论文 ｜Attend Before Attention: Efficient and Scalable Video Understanding via Autoregressive Gazing ｜自回归注视：ViT前置多尺度Token压缩

研究机构：美国麻省理工学院

作者：Baifeng Shi、Stephanie Fu、Long Lian 等 13 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.12254)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.12254)

> 长视频理解面临高时空分辨率下的计算冗余困境，现有方法多在LLM端剪枝而忽略ViT瓶颈。AutoGaze在ViT前引入3M参数轻量模型，通过自回归解码多尺度Patch并基于重建损失阈值自适应停止，实现4-100倍Token缩减。该方法将NVILA-8B扩展至1K帧4K分辨率，在VideoMME上达67.0%，但在通用长视频基准上未超越最强代理式方法，其效率优势是否以牺牲复杂推理能力为代价存疑。

## 研究背景

多模态大语言模型（MLLMs）处理视频时，视觉Transformer（ViT）需编码所有像素，而视频存在显著时空冗余——静态背景仅需观察一次，动态区域才携带新信息。这种冗余导致计算资源浪费，使模型无法扩展至小时级或4K分辨率视频。为缓解此问题，Token压缩技术应运而生，但主流方法如LongVU、VideoChat-Flash仅在LLM端剪枝，ViT仍处理全量像素，形成效率瓶颈。

长视频理解领域已从均匀采样转向查询感知动态策略，但现有方案在高分辨率场景下失效：启发式方法（如基于注意力分数）精度不足，代理式推理（如LongVT）虽提升证据定位但增加延迟。AutoGaze的切入点在于将压缩前置到ViT之前，通过重建损失约束实现信息保真与计算效率的平衡，而非依赖任务特定的查询信号。

## 核心方法

### 方法参照系

视频Token压缩通常分为空间、时间或时空维度，标准流程为：ViT编码全帧→LLM端基于注意力或规则剪枝。本文的关键差异在于压缩发生在ViT之前，且以重建损失而非任务相关性为优化目标，实现分辨率无关的自适应Patch选择。

### 自回归多尺度注视机制

AutoGaze采用卷积编码器与自回归Transformer解码器（共3M参数），逐帧解码Patch索引。解码过程类似LLM，但词表为Patch索引$\{1, \dots, V\}$。设计动机是解决启发式方法无法动态适应场景变化的问题：模型参考前帧特征与已选Patch历史，避免冗余选择。

$$
\mathcal{L}^*(N_{1:T}) = \min_{p_{1}^{1:N_1}, \dots, p_{T}^{1:N_T}} \sum_{t=1}^{T} L(\mathbf{X}[t], \text{Recon}(\mathbf{X}[t]_{p_t^{1:N_t}}))
$$

该公式表示在给定注视长度$N_{1:T}$下，最小化重建损失的Patch选择策略。AutoGaze通过解码器附加的损失预测头，在每步解码时预测当前重建损失，一旦低于用户阈值$\epsilon$即停止该帧注视，实现自适应长度控制。

### 多尺度Patch与训练范式

多尺度注视允许不同区域使用不同分辨率Patch（32/64/112/224px），设计动机是低细节区域（如纯色背景）可用粗粒度表示，高细节区域需细粒度捕捉。训练分两阶段：先用贪心搜索生成的注视序列进行下一Token预测（NTP）预训练，再用GRPO强化学习以重建损失为奖励后训练。

$$
A_{t}^k = \frac{G_{t}^k - \text{mean}(G_{t}^{1:N_t})}{\text{std}(G_{t}^{1:N_t})}, \quad G_{t}^k = \sum_{\tau=t}^{T} \gamma^{N_t-k} (-l_{\tau}^{\tau})
$$

该公式定义GRPO中的优势函数，$G_{t}^k$为从第$k$步到视频结束的折扣负重建损失总和。RL后训练使模型发现比贪心搜索更优的注视序列，将注视率从0.102降至0.094（重建损失0.7时）。

## 实验评估

实验使用SigLIP2-SO400M和NVILA-8B-Video，在VideoMME、LVBench、MLVU等基准评估。基线覆盖空间/时间/时空Token缩减方法（ToMe、FastV、LongVU等），但缺失代理式推理框架（LongVT、Video-o3）的直接对比。

| 方法 | VideoMME (w/o sub) | L-VidBench (val) | HLVid (test) |
| :--- | :--- | :--- | :--- |
| NVILA-8B-Video | 64.2 | 57.7 | 42.5 |
| + AutoGaze | 67.0 | 61.0 | 52.6 |
| VideoChat-Flash | 65.1 | 58.5 | 48.1 |

AutoGaze在HLVid上超越前SOTA 4.5%，但在VideoMME上低于Flow4Agent（68.3%）。消融显示RL后训练比仅NTP预训练降低注视率10%，多尺度注视提升效率2.3倍。

| 训练阶段 | 重建损失 | 注视率 |
| :--- | :--- | :--- |
| 无训练 | 0.7 | 0.263 |
| 仅NTP | 0.7 | 0.102 |
| NTP+RL | 0.7 | 0.094 |

评估边界：HLVid仅含268个QA对，样本量小；未报告置信区间；代码开源但超参数细节有限。

## 关联研究分析

从问题动机看，AutoGaze与LongVU均解决Token冗余，但LongVU依赖ViT特征在LLM端剪枝，而AutoGaze在ViT前压缩。这一差异源于任务特性：高分辨率视频的瓶颈在ViT计算而非LLM上下文，前置压缩更直接。但AutoGaze基于重建损失优化，未考虑查询语义，可能在稀疏证据任务上不如代理式方法精准。

从方法设计看，AutoGaze借鉴LLM自回归范式，与Video-o3的交错线索搜索形成对比。Video-o3通过工具调用主动检索，AutoGaze通过重建约束被动选择。前者支持多跳推理但延迟高，后者效率高但推理深度受限。这种取舍暗示：当任务要求细粒度时序定位时，压缩-推理联合优化可能比单一压缩更有效。

## 总结

AutoGaze解决的核心矛盾是高时空分辨率视频的计算冗余与信息保真冲突。其切入点在于将压缩前置到ViT之前，通过重建损失阈值实现自适应Patch选择，避免了启发式方法的精度不足和代理式方法的延迟开销。方法上，AutoGaze采用3M参数自回归模型解码多尺度Patch，结合NTP预训练与RL后训练，实现4-100倍Token缩减。实验证明其在HLVid上达52.6%，超越前SOTA 4.5%，但在VideoMME上未超越最强代理式方法。边界在于：重建损失优化未考虑查询语义，可能在复杂推理任务上信息损失过大。当注视率降至1%以下时，模型对细粒度时序关系的捕捉能力是否显著下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.12254)