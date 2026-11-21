# HuggingFace最新推荐论文 ｜Reliable Chain-of-Thought via Prefix Consistency ｜前缀一致性加权投票

研究机构：日本名古屋大学、阿联酋扎耶德大学

作者：Naoto Iwase、Yuki Ichihara、Mohammad Atif Quamar 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.07654)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.07654)

> 测试时聚合旨在通过采样多条思维链（Chain-of-Thought, CoT）并投票提升大语言模型（Large Language Models, LLMs）的推理准确率，但标准多数投票（Majority Voting, MV）在正确答案处于少数派时失效。现有加权投票（Weighted Majority Voting, WMV）方法依赖对数概率或自评分，在困难任务上无法区分正确与错误轨迹。本文提出前缀一致性（Prefix Consistency, PC），利用截断再生成的答案复现率作为可靠性信号，无需内部状态访问即可优化投票权重。该方法在困难基准上以中位4.6倍更少的Token达到标准MV的准确率上限，但其有效性高度依赖任务难度分布，对高通过率任务增益有限。

## 研究背景

当LLM面对复杂推理任务时，单次生成往往不可靠，采样多条CoT并聚合成为标准做法。标准MV假设所有样本等价，直接返回众数答案，这在模型单样本成功率（Pass@1）低于50%时必然失败，因为错误答案可能占据多数。为修复此缺陷，WMV引入可靠性信号对样本加权，使高质量轨迹获得更高投票权重。

现有WMV路线主要依赖两类信号：基于对数概率的信号（如DeepConf、Response Probability）和基于文本自评分的信号（如P(True)、Self-certainty）。这些信号在简单任务上有效，但在困难任务上失效，因为模型对错误答案也可能输出高置信度，导致正确与错误轨迹的信号分布重叠。本文的切入点在于发现一个被忽视的行为规律：正确轨迹在截断再生成时更倾向于复现原答案，而错误轨迹则更可能产生新的错误答案。这种“再生成稳定性”差异构成了无需内部访问权限的可靠性代理。

## 核心方法

### 方法参照系

WMV的标准流程是：采样N条CoT，提取每条轨迹的答案，计算每条轨迹的可靠性分数$s(y_i, \ell_i)$，通过权重函数$w(s)$加权后投票。本文的关键差异在于可靠性信号的来源：传统方法从单次生成的内部状态（对数概率）或文本表面特征（自评分）提取信号，而本文通过额外的再生成步骤，从答案的复现频率中提取信号。

### 前缀一致性信号

传统WMV信号在困难任务上失效，因为模型对错误答案的置信度与正确答案无显著差异。本文引入前缀一致性，其设计动机是利用正确推理路径的内在稳定性：若初始答案正确，从中间截断并再生成时，模型更可能收敛回同一答案；若初始答案错误，再生成更可能产生不同的错误答案。具体操作为：将轨迹$y_i$截断至$\lceil \tau |y_i| \rceil$个Token，从该前缀再生成$K$条续写，得到答案集合$A_{i[\tau,K]}$。前缀一致性分数定义为答案$a$在该集合中的出现比例：

$$ c_{i[\tau]}(a) = \frac{|\{a' \in A_{i[\tau]} : a' = a\}|}{K+1} $$

该公式的物理含义是：答案在“原始+再生成”共$K+1$次尝试中复现的频率。$c=1$表示完全复现，$c=1/2$表示仅原始答案出现，$c=0$表示答案改变。此信号无需对数概率访问，且对再生成的新答案也赋予权重，使PC-WMV能恢复初始样本中缺失的正确答案。

### 加权投票与理论保证

基于前缀一致性分数，PC-WMV的投票权重为$w(c_{i[\tau]}(a))$，其中$w:[0,1]\to\mathbb{R}_{\ge0}$满足$w(0)=0$。论文采用幂函数族$w(c)=c^n$（$n\in\{1,2,3\}$），分别对应线性、二次、三次加权。Theorem 1证明了在二元答案空间下，当判别间隙$D(\tau) = r_C(\tau) - r_W(\tau) > 0$时，PC-WMV在标准MV失效的区间（Pass@1 < 0.5）内收敛到正确答案。$D$越大，PC-WMV的优势区间越宽。实验显示$D$在所有（模型，基准）组合上均为正，范围从7.4%到60.3%，验证了理论前提的普适性。

## 实验评估

实验在FrontierScience-Olympiad、HMMT Feb 2026、AIME 2025、Brumo 2025四个基准上，使用GPT-OSS-120B、GPT-OSS-20B、Nemotron3-30B、Nemotron2-9B、Ministral3-14B五个模型。基线覆盖标准MV、三种WMV信号（Self-certainty、DeepConf tail、P(True)）及两种自适应停止策略（AC、ESC）。缺失过程奖励模型（Process Reward Model, PRM）类基线，但PRM通常用于训练时监督，与测试时聚合方法不同路线。

| 基准 | 模型 | 方法 | B=1M Tokens 准确率 |
|---|---|---|---|
| FrontierScience-Olympiad | GPT-OSS-120B | Standard MV | .495±.001 |
| FrontierScience-Olympiad | GPT-OSS-120B | PC-cubic | .508±.001 |
| FrontierScience-Olympiad | Ministral3-14B | Standard MV | .141±.001 |
| FrontierScience-Olympiad | Ministral3-14B | PC-cubic | .174±.001 |
| AIME 2025 | Ministral3-14B | Standard MV | .535±.003 |
| AIME 2025 | Ministral3-14B | PC-cubic | .597±.003 |

在困难任务上，PC-cubic显著优于标准MV：FrontierScience-Olympiad上Ministral3-14B从.141提升至.174，AIME 2025上从.535提升至.597。在简单任务（如AIME 2025 GPT-OSS-120B，Pass@1=.789）上，PC-cubic（.926）仅略高于标准MV（.901），增益有限。

消融实验显示，截断比例$\tau$和再生成次数$K$影响效率-准确率权衡。$\tau=0.25, K=3$在FrontierScience-Olympiad上达到最高准确率（.562 at 5M tokens），但Token成本约为$\tau=0.75, K=1$的3.25倍。在1M-5M预算下，默认$\tau=0.75, K=1$在三个数学基准上接近最优，仅在FrontierScience-Olympiad上被更激进配置超越。判别间隙$D$与Token节省率正相关：$D$最大的单元格（如Ministral3-14B Brumo 2025，$D=51.8\%$）实现最大节省（0.18×标准MV预算）。

评估边界方面，论文未报告置信区间对超参数选择的敏感性，且仅使用精确匹配评估，未考虑部分正确性。代码已开源，但再生成步骤的额外计算开销在闭源API场景下可能抵消效率优势。

## 关联研究分析

从问题动机看，本文与FaithCoT-Bench（Shen et al., 2025）同属CoT质量评估，但目标不同：FaithCoT-Bench旨在量化CoT文本与内部计算的忠实度，而PC-WMV旨在利用CoT的行为特性优化聚合效率。FaithCoT-Bench依赖反事实干预和LLM评判，计算成本高且需实例级标注；PC-WMV仅依赖再生成稳定性，无需人工标注或内部访问。这一差异源于任务特性：忠实度评估需因果证据，而聚合优化只需行为代理。PC-WMV未验证再生成稳定性是否反映内部计算忠实性，若模型存在“表演性推理”，再生成稳定性可能虚高，论文未讨论此风险。

从方法设计看，本文与Prefix Consensus（Jindal et al., 2026）技术同源但应用目标不同：Prefix Consensus利用前缀共识引导推理路径，属于生成时干预；PC-WMV利用前缀一致性评估轨迹可靠性，属于聚合时优化。Prefix Consensus需修改生成过程，可能改变模型分布；PC-WMV保持原始生成不变，仅改变投票权重，更易于部署。两者均未探索前缀一致性与内部状态探针的结合，若再生成稳定性与内部激活模式解耦，则PC-WMV的可靠性信号可能失效。

## 总结

本文解决的核心矛盾是WMV在困难任务上因信号区分度不足而失效。现有方法依赖对数概率或自评分，在Pass@1<50%时无法区分正确与错误轨迹；本文抓住再生成稳定性的行为差异，通过截断再生成计算答案复现率，无需内部访问即可构建可靠性信号。PC-WMV在困难基准上以中位4.6倍更少的Token达到标准MV准确率上限，最大节省达21倍。其边界在于：当Pass@1接近标准MV上限时（如Nemotron3-30B AIME 2025，Pass@1=.902），PC-WMV增益消失，因为重加权空间有限。此外，论文未验证再生成稳定性在RL训练模型上是否受“表演性推理”影响，若模型学会在CoT中隐藏真实意图，再生成稳定性可能不再反映答案正确性。当模型规模扩大至1000B以上时，再生成稳定性的判别间隙$D$是否保持显著，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.07654)