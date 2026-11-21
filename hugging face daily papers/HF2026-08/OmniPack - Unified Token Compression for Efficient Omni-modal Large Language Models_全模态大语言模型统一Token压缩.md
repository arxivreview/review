# HuggingFace最新推荐论文 ｜OmniPack: Unified Token Compression for Efficient Omni-modal Large Language Models ｜全模态大语言模型统一Token压缩

研究机构：西北工业大学、北京大学

作者：Wanshun Su、Yang Shi、Feihu Liu 等 13 人

论文原文见 [arXiv](https://arxiv.org/abs/2608.03812)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.03812)

> 全模态大语言模型（Omni-LLMs）在处理长音视频时面临巨大的计算开销，现有单阶段压缩方法在激进预算下易丢失全局结构证据或忽略跨模态语义协同。本文指出Pre-LLM压缩缺乏长程时空建模，Inner-LLM压缩缺乏显式音视频交互，提出OmniPack框架。该框架通过模态特异性结构压缩与查询条件化语义精炼的两阶段协同，在7.5%保留率下实现10.0倍FLOPs降低。其价值在于验证了渐进式压缩在全模态场景的优越性，但极端压缩下的细粒度任务鲁棒性仍存疑。

## 研究背景

全模态大语言模型将视觉、音频与文本输入映射至统一的LLM嵌入空间，其中视觉与音频Token数量远超文本，导致注意力计算成本呈二次方增长。为降低推理延迟，Token压缩成为关键手段，其核心在于确定保留Token子集 $V'$ 以最小化计算开销 $C(V')$，同时保持任务性能损失小于阈值 $\epsilon$。这一过程涉及剪枝位置（Pre-LLM或Intra-LLM）、重要性信号来源（视觉显著性或跨模态相关性）及预算分配策略（固定或自适应）三个子问题的耦合。

现有Omni-LLM压缩方法主要沿两条路线演进：一是仅在Pre-LLM阶段进行压缩，如OmniZip和OmniSIFT，它们依赖音频引导视频或视觉引导音频，但此时模态间语义交互有限，跨模态引导可能基于未对齐的特征；二是渐进式压缩，如SEATS，在LLM内部进一步剪枝，但其内部阶段主要依赖文本引导，未显式建模音频与视觉Token的协同交互。这两种路线在激进压缩预算下均面临瓶颈：前者易丢弃稀疏分布的全局证据，后者未能充分利用LLM内部建立的跨模态语义成熟度。

OmniPack的切入点在于识别出压缩策略应与多模态表示的语义成熟度阶段相匹配。Pre-LLM阶段应利用模态特异性时空结构消除大规模冗余，而Inner-LLM阶段应在充分多模态交互后，利用查询条件化的音视频协同进行语义精炼。这种阶段专业化策略旨在解决现有方法在结构保留与语义对齐之间的失衡。

## 核心方法

### 方法参照系

OmniPack属于Training-free的渐进式Token压缩框架，其标准流程参照SEATS等渐进剪枝方法，即先进行Pre-LLM压缩，再在LLM指定层进行Inner-LLM压缩。关键差异在于，本文在Pre-LLM阶段引入模态特异性结构变异性信号，并在Inner-LLM阶段显式建模音频-视觉协同，而非仅依赖文本引导。

### 模态特异性Pre-LLM压缩

Pre-LLM压缩旨在消除结构冗余，通常做法是基于单一显著性分数选择Top-K Token。本文创新在于融合编码器注意力与模态特异性结构变异性，并引入覆盖选择与相似性合并。设计动机是解决纯显著性选择导致Token过度集中于局部显著区域，忽略全局时空覆盖的问题。对于视频，定义相邻帧变化 $e^{v,temp}_{t,p} = 1 - \cos(x^v_{t,p}, x^v_{t+1,p})$ 和空间显著性 $e^{v,spat}_{t,p} = 1 - \frac{1}{P}\sum_{q=1}^P \cos(x^v_{t,p}, x^v_{t,q})$；对于音频，定义相邻Token变化 $e^a_t = 1 - \cos(x^a_t, x^a_{t+1})$。这些结构线索与注意力中心性向量 $a_m$ 结合，形成最终重要性向量 $s_m$。随后，通过DPC-KNN算法基于联合距离 $d_{ij} = 1 - \cos(x_i, x_j) + \lambda d^{pos}_{ij}$ 进行覆盖选择，确保保留Token在时空上的代表性。

### 查询条件化Inner-LLM压缩与Token合并

Inner-LLM压缩发生在第 $\ell$ 层Transformer块之后，此时多模态表示已充分交互。通常做法是基于文本相关性剪枝，本文创新在于引入音频-视觉协同信号。设计动机是解决Inner-LLM阶段忽略模态间互补信息的问题。Token $h^m_i$ 的相关性得分 $R^m_i$ 由三项组成：文本相关性 $\max(\cos(h^m_i, q), \max_j \cos(h^m_i, h^q_j))$，音视频协同 $\cos(h^m_i, \bar{p}^m)$，以及模态内代表性 $u^m_i$。此外，本文提出相似性感知Token合并，将未选Token $i$ 的信息通过加权平均 $\tilde{x}^m_j = x^m_j + \frac{\sum_{i:\pi_m(i)=j} w^m_i x^m_i}{1 + \sum_{i:\pi_m(i)=j} w^m_i}$ 转移至保留Token $j$，其中权重 $w^m_i = (1 + \bar{s}^m_i)/2$。这一机制避免了直接丢弃低分Token造成的不可逆信息损失，使保留Token能够聚合邻近冗余信息。

## 实验评估

实验在Qwen2.5-Omni-7B/3B和MiniCPM-o-2.6三个骨干网络上进行，评测基准包括AVUT、WorldSense、DailyOmni、VideoMME和LVOmniBench，覆盖音频中心与视频中心理解任务。基线涵盖FastV-om、VisionZip-om、OmniSIFT、SEATS等Training-free方法，但缺乏纯图像SOTA（如GRIP-VLM）作为跨模态参照，且未包含端到端学习类基线。

| 方法 | 保留率 (Pre/Inner) | FLOPs (T) | 相对FLOPs | 平均得分 | 相对性能 (%) |
|---|---|---|---|---|---|
| Qwen2.5-Omni-7B (Vanilla) | 100% / 100% | 73.2 | 100.0% | 54.6 | 100.0 |
| SEATS† | 25% / 12.5% | 11.6 | 15.8% | 52.9 | 96.7 |
| SEATS⋆ | 25% / 12.5% | 12.5 | 17.1% | 53.0 | 97.1 |
| OmniPack (w/o M) | 25% / – | 14.9 | 20.4% | 53.6 | 98.2 |
| OmniPack | 25% / 12.5% | 12.2 | 16.7% | 53.5 | 98.0 |
| OmniPack | 15% / 7.5% | 7.3 | 10.0% | 52.2 | 95.6 |
| OmniPack | 10% / 5% | 5.0 | 6.8% | 50.7 | 92.9 |

在Qwen2.5-Omni-7B上，OmniPack在15%/7.5%保留率下保持95.6%的相对性能，FLOPs降至10.0%，优于SEATS⋆（97.1% at 25%/12.5%）在更低计算量下的表现。消融实验显示，Pre-LLM阶段中，覆盖选择相比重要性选择在WorldSense和LVOmniBench上分别提升3.4%和6.1%，表明全局覆盖对长视频任务至关重要。Inner-LLM阶段引入音视频协同相比通用查询引导，在AVUT、WorldSense和DailyOmni上分别提升0.4%、0.1%和0.4%，增益较小但方向一致。

评估边界方面，论文未报告置信区间，且缺乏极端压缩率（<5%）下的鲁棒性测试。代码已开源，超参数（如 $\eta_v=0.25, \lambda=0.20$）已公开，但不同骨干网络的层选择（如Qwen2.5-Omni-3B在第26层压缩）可能影响泛化性。

## 关联研究分析

从问题动机看，OmniPack与SEATS同属渐进式压缩路线，但SEATS依赖文本引导进行Inner-LLM剪枝，而OmniPack显式建模音频-视觉协同。这一差异源于OmniPack认为在LLM内部，模态间语义已充分交互，应利用这种协同而非仅依赖文本。然而，SEATS在25%/12.5%保留率下达到97.1%相对性能，高于OmniPack的98.0%（在25%/12.5%下），但在更低保留率（15%/7.5%）下，OmniPack的95.6%优于SEATS的93.4%，表明OmniPack在激进压缩下更具优势。

从方法设计看，OmniPack与OmniSIFT同属全模态压缩，但OmniSIFT侧重时空视频压缩与视觉引导音频选择，而OmniPack强调模态特异性结构变异性与覆盖选择。OmniSIFT在15%保留率下保持89.7%相对性能，低于OmniPack的95.2%（w/o M），表明OmniPack的结构保留策略更有效。然而，OmniPack未探索端到端学习剪枝，如VisionSelector，后者在图像基准上达到98.2%相对性能，但训练成本高。OmniPack的Training-free特性使其部署更便捷，但性能上限可能受启发式规则限制。

## 总结

OmniPack旨在解决全模态大语言模型在激进Token压缩下结构证据丢失与跨模态语义协同不足的核心矛盾。其切入点在于识别压缩策略应与多模态表示的语义成熟度阶段相匹配，Pre-LLM阶段利用模态特异性结构消除冗余，Inner-LLM阶段利用查询条件化音视频协同进行语义精炼。通过融合结构变异性、覆盖选择与相似性合并，OmniPack在Qwen2.5-Omni-7B上于7.5%保留率下保持95.6%相对性能，FLOPs降低10.0倍。其边界在于未验证极端压缩率（<5%）下的细粒度任务鲁棒性，且缺乏端到端学习基线的对比。当保留率降至5%以下时，相似性合并机制是否足以防止语义结构崩塌，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.03812)