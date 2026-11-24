# ACL2026最新论文 ｜Efficient Low-Resource Language Adaptation via Multi-Source Dynamic Logit Fusion ｜低资源语言高效适配的多源动态Logit融合

研究机构：北京大学

作者：Chen Zhang、Jiuheng Lin、Zhiyuan Liao 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18106)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f2f15010a1aa)

> 低资源语言（LRL）适配长期受困于标注数据稀缺与大模型算力门槛，导致现有方法难以在保持源语言能力的同时注入目标语言知识。Proxy Tuning等Logit算术方法虽规避了参数更新，但其默认的大模型主导假设在LRL场景下因大模型自身语言能力的稀释而失效。TRIMIX通过解耦语言、任务与规模三种能力向量，并引入基于困惑度的动态加权机制，在推理阶段重新平衡小模型的语言专长与大模型的通用能力。该方法以极低的训练成本实现了跨规模能力迁移，但其效果高度依赖小模型CPT的质量，且未解决底层分词器碎片化问题。

## 研究背景

当大语言模型（LLM）处理低资源语言时，其内部表示空间中的几何结构不一致导致零样本迁移性能波动，这一现象源于分词器碎片化（Tokenizer Fragmentation）与跨语言对齐（Cross-Lingual Alignment）的不稳定。分词效率低下不仅浪费上下文窗口，更使得模型在注入新语言知识时，优化过程极易引发灾难性遗忘（Catastrophic Forgetting），损害原有的英语能力或通用推理能力。

领域主流路线分为“重训练”与“轻融合”两类。继续预训练（CPT）虽能深度注入知识，但高算力成本与遗忘风险使其对学术界不可行；模型合并（Model Merging）虽轻量，但受限于同架构约束，且无法利用大模型的规模效应。Proxy Tuning（Liu et al., 2024）提出通过Logit算术将小模型知识注入大模型，但在LRL场景中，大模型自身对目标语言的弱表示会压倒小模型的专业知识，导致融合失效。TRIMIX的切入点在于挑战“大模型主导”假设，通过显式解耦并动态加权不同来源的能力，解决大模型能力稀释导致的融合失效问题。

## 核心方法

### 方法参照系

TRIMIX属于“轻融合”路线中的Logit融合变体。与标准模型合并需在参数空间进行同架构权重相加不同，TRIMIX在Logit空间进行跨规模线性组合，解耦了架构同构限制。其核心差异在于引入了基于输入分布的动态权重选择机制，而非固定的权重系数。

### 三源能力解耦

Proxy Tuning通常将大模型Logit作为基线，仅注入小模型的差异向量，隐含假设大模型具备足够的目标语言能力。TRIMIX将理想Logit $L$ 分解为三个正交的能力向量：任务解决向量 $\delta_T$、语言建模向量 $\delta_L$ 和规模效应向量 $\delta_S$。

$$
L = L_{small-base} + \alpha\delta_T + \beta\delta_L + \gamma\delta_S
$$

其中，$\delta_T = L_{large-ins} - L_{large-base}$ 提取大模型指令微调带来的任务能力；$\delta_L = L_{small-cpt} - L_{small-base}$ 提取小模型CPT带来的目标语言专长；$\delta_S = L_{large-base} - L_{small-base}$ 提取规模带来的通用能力增益。为降低推理内存开销，TRIMIX约束 $\gamma = \alpha$，使得 $L_{large-base}$ 项在计算中抵消，最终公式简化为：

$$
L = \alpha L_{large-ins} + \beta L_{small-cpt} + (1 - \alpha - \beta) L_{small-base}
$$

这一设计动机在于，LRL CPT通常涉及少于1B tokens，其语言能力远未饱和，若沿用Proxy Tuning的 $\alpha=1$ 设置，大模型的弱LRL表示会抑制小模型的强LRL信号。通过显式分离 $\delta_L$，TRIMIX允许独立调节语言专长的贡献度。

### 动态加权机制

固定权重无法适应不同任务的语言分布差异，TRIMIX引入基于困惑度（Perplexity, PPL）的动态选择策略。在推理时，系统对 $\alpha$ 和 $\beta$ 进行网格搜索，选择使输入提示困惑度最小化的权重对。

$$
(\alpha^*, \beta^*) = \arg\min_{\alpha, \beta} \text{PPL}(L_{prompt} | \alpha, \beta)
$$

该机制的物理含义是：当融合后的Logit分布更贴合输入提示的语言分布时，说明权重配置更有效地整合了语言与任务能力。实验表明，PPL引导的策略选出的权重均值（$\alpha=0.11, \beta=0.91$）接近性能上界（$\alpha=0.33, \beta=0.74$），显著优于基于熵（Entropy）的选择（$\alpha=0.95, \beta=0.61$），后者因过度依赖大模型置信度而失效。

## 实验评估

实验在Qwen2.5、Llama2、Llama3.2和Gemma3四个模型家族上，覆盖藏语、维吾尔语等8种LRL。基线包括Proxy Tuning、Model Merging和Contrastive Decoding，但缺失全参数CPT基线，限制了与“重训练”路线的直接对比。

| 方法 | 模型组合 | MiLiC-Eval Avg. | 相对提升 |
| :--- | :--- | :--- | :--- |
| Qwen2.5-14B-ins | 14B | 42.9 | - |
| Proxy Tuning | 1.5B-cpt + 14B-ins | 40.3 | -1.5% |
| TRIMIX (PPL) | 1.5B-cpt + 14B-ins | 46.3 | +4.9% |
| Gemma3-12B-ins | 12B | 45.6 | - |
| TRIMIX (PPL) | 4B-cpt + 12B-ins | 48.0 | +5.3% |

TRIMIX (PPL) 在Qwen2.5-1.5B-cpt + 14B-ins组合上取得46.3%的平均准确率，较14B-ins基线提升4.9%。在Gemma3上，尽管12B-ins基线较强（45.6%），TRIMIX仍实现5.3%的相对提升，证明方法在强基座下依然有效。

| 消融项 | 移除向量 | Kazakh Score | 性能下降 |
| :--- | :--- | :--- | :--- |
| Full TRIMIX | - | 38.1 | - |
| w/o $\delta_T$ | Task Solving | 37.2 | -0.9 |
| w/o $\delta_L$ | Language Modeling | 30.5 | -7.6 |
| w/o $\delta_S$ | Scaling Effect | 33.9 | -4.2 |

消融实验显示，移除语言建模向量 $\delta_L$ 导致性能下降7.6分，远超移除任务向量 $\delta_T$ 的0.9分，证实语言专长是LRL适配的主导因素。移除规模效应 $\delta_S$ 下降4.2分，表明规模增益虽重要但次于语言匹配。

评估边界方面，TRIMIX在藏语和蒙古语上增益有限，归因于分词器效率低（藏语分词效率仅为英语的1/10）。代码开源（GitHub），但超参数搜索依赖50个样本子集，未报告GPU成本与置信区间。

## 关联研究分析

从方法设计看，TRIMIX与DIPLomA（P30）同属轻量级适配，但DIPLomA依赖同架构权重差值合并，无法利用大模型规模效应；TRIMIX通过Logit空间融合实现跨规模迁移，但牺牲了参数空间的几何一致性。DIPLomA的线性可加性假设在指令跟随任务上成立，而TRIMIX的动态加权机制更适应LRL中语言分布的非线性变化，但两者均未解决分词器碎片化导致的底层表示缺陷。

从问题动机看，Proxy Tuning（Liu et al., 2024）在代码域成功，因代码CPT与指令微调的KL散度相当，大模型主导合理；但在LRL域，CPT数据量小导致KL散度远小于指令微调，大模型主导反而抑制语言专长。TRIMIX通过PPL动态加权纠正了这一偏差，但其有效性依赖于小模型CPT的质量。若小模型CPT数据不足，$\delta_L$ 向量本身噪声大，动态加权可能放大噪声而非提取信号，论文未对此进行鲁棒性测试。

## 总结

TRIMIX旨在解决LRL适配中数据稀缺与算力门槛的双重约束，通过解耦语言、任务与规模能力，并在推理阶段动态加权，克服了Proxy Tuning的大模型主导失效问题。实验证明，在Qwen2.5和Gemma3上，TRIMIX较单模型基线提升4.9%-5.3%，且语言建模向量是性能主导因素。其边界在于：方法未解决分词器碎片化，对藏语等低分词效率语言增益有限；且动态加权依赖小模型CPT质量，若CPT数据不足，融合效果可能退化。当小模型CPT数据量进一步减少至百万级以下时，PPL引导的权重选择是否仍能稳定提取语言信号，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_f2f15010a1aa)