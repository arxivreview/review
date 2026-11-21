# HuggingFace最新推荐论文 ｜(1D) Ordered Tokens Enable Efficient Test-Time Search ｜有序Token结构下的测试时搜索

研究机构：瑞士洛桑联邦理工学院

作者：Zhitong Gao、Parham Rezaei、Ali Cy 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.15453)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.15453)

> 自回归视觉生成长期受制于推理时缺乏有效的质量引导机制，现有加速方案仅关注计算效率而忽视生成质量的动态优化。本文切入点在于发现1D有序Token的中间态具备全局语义，可被验证器可靠评估，从而构建测试时搜索（Test-Time Search, TTS）框架。通过对比1D有序与2D网格Token在Beam Search等算法下的表现，验证了Token结构对TTS效率的决定性影响。该研究揭示了表征结构对推理时扩展性的底层约束，但其在高分辨率动态场景下的泛化能力仍存疑。

## 研究背景

自回归模型将图像离散化为Token序列进行预测，传统2D网格Token按光栅扫描顺序排列，其前缀仅对应固定空间区域（如左上角），缺乏全局语义信息。测试时搜索（Test-Time Search, TTS）通过验证器评估候选序列以优化生成质量，但其有效性依赖于中间状态的可验证性。当序列前缀无法反映整体语义时，验证器信号失效，导致搜索效率低下。

现有自回归视觉生成研究聚焦于Token化保真度与推理加速，如VAR通过Next-Scale预测提升全局一致性，StepVAR等通过剪枝降低延迟。然而，这些工作未系统探讨Token结构对推理时搜索能力的制约。主流2D网格Token因空间局部性限制，中间态语义稀疏，难以支撑有效的验证器引导。本文切入点在于利用1D有序Token（如FlexTok）的粗到细层级结构，其前缀可解码为语义完整的低分辨率图像，为TTS提供了可验证的中间状态。

## 核心方法

### 方法参照系

标准自回归生成流程为：Token化→序列预测→解码。本文问题与该通用流程的关键差异在于，将推理阶段从单一序列预测扩展为验证器引导的搜索过程，核心变量是Token序列的结构属性（有序vs网格）对搜索空间可验证性的影响。

### 有序Token的语义可验证性

1D有序Tokenizer通过嵌套丢弃（Nested Dropout）训练，确保任意前缀可解码为有效图像。其设计动机在于解决2D网格Token前缀语义稀疏导致的验证器失效问题。在搜索过程中，第$t$步的候选前缀$\mathbf{x}_{1:t}$通过解码器映射为图像，验证器$g$计算其与条件$c$的相似度：

$$
\hat{\mathbf{x}} = \arg\max_{\mathbf{x} \in \mathcal{K}} g(\text{Dec}(\mathbf{x}), c)
$$

其中$\mathcal{K}$为搜索空间。该公式表明，1D有序Token使中间态$\text{Dec}(\mathbf{x}_{1:t})$具备全局语义，验证器可基于此进行有效评分，从而引导搜索向高质量区域收敛。

### 搜索算法与验证器协同

Beam Search在每步扩展$k$个前缀，采样$M$个候选Token，保留验证器评分最高的$k$个。其设计动机在于利用1D有序Token的层级结构，在早期步骤即锁定全局语义方向。与Best-of-N不同，Beam Search利用前缀信息，避免重复探索无效分支。验证器覆盖图像-文本对齐（CLIP、ImageReward）、图像-图像对齐（DreamSim）及图像质量（Aesthetic Score）三类，通过秩聚合构建集成验证器，弥补单一验证器的偏置。

## 实验评估

实验在COCO Karpathy验证集（300/1000图像）、GenEval（553提示）及DreamBench++（1350实例）上进行，基线包括FlexTok（1D有序）、2D网格Token（控制变量）、Janus-1.3B及LlamaGen-L。核心对比聚焦于不同搜索算法下Token结构对TTS增益的影响。

| 模型 | Tokenizer | 提示类型 | 基线 | Beam Search | 增益 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Semanticist | 1D ordered | Simple | 74.60 | 85.02 | +10.42 |
| LlamaGen-L | 2D grid | Simple | 76.85 | 80.36 | +3.51 |
| Semanticist | 1D ordered | Complex | 70.67 | 83.12 | +12.45 |
| LlamaGen-L | 2D grid | Complex | 73.52 | 77.56 | +4.04 |

在COCO CLIPScore上，FlexTok Beam Search达93.44%，较基线提升13.05点；2D网格仅提升2.53点。GenEval准确率上，FlexTok集成验证器达67%，2D网格基线为57%。消融显示，Beam Search对1D Token的增益显著高于Best-of-N，而Lookahead Search虽提升2D Token性能，但计算成本激增。

评估边界方面，实验未覆盖高分辨率（>256x256）动态场景，且缺乏与扩散模型TTS的直接对比。代码与权重已开源，但搜索超参数（如Beam宽度）未提供完整敏感性分析，可复现性依赖特定配置。

## 关联研究分析

从问题动机看，VAR等层级生成模型关注训练时的全局一致性，而本文聚焦推理时的质量优化。VAR的Next-Scale预测通过粗到细生成提升保真度，但未引入外部验证器；本文的TTS框架在推理阶段引入验证器，利用1D有序Token的语义结构实现动态引导。差异根源在于任务目标：VAR优化分布匹配，本文优化条件对齐。

从方法设计看，StepVAR等加速方法通过剪枝降低计算量，属于效率导向；本文的Beam Search通过搜索提升质量，属于质量导向。StepVAR的剪枝策略基于结构-纹理重要性，而本文的搜索策略基于验证器评分。两者在1D有序Token上可互补：剪枝减少候选空间，搜索优化保留分支。但本文未探索剪枝与搜索的联合优化，查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

本文核心矛盾在于自回归模型推理时缺乏有效的质量引导机制，现有加速方案仅关注效率而忽视语义优化。本文抓住1D有序Token中间态具备全局语义这一被忽略的特性，通过构建SoTo框架，利用验证器引导Beam Search实现测试时扩展。实验证明，1D有序Token在Beam Search下CLIPScore提升13.05点，显著优于2D网格的2.53点。边界在于实验局限于256x256分辨率及静态场景，未验证动态分辨率下的误差累积。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.15453)