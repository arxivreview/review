# ACL-Findings2026最新论文 ｜Towards Identification and Intervention of Safety-Critical Parameters in Large Language Models ｜预期安全影响（ESI）：基于参数敏感度解耦安全与效用的干预框架

作者：Weiwei Qi、Zefeng Wu、Tianhang Zheng 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bebdba993896)

> 导读 大语言模型在微调后常出现安全对齐崩塌，但现有方法难以精确定位哪些参数承载安全行为，导致防御策略要么全局冻结损失效用，要么盲目更新破坏安全。本文切入点在于构建一个可微分的参数级安全敏感度度量，将安全关键参数从全参数空间中分离出来。通过引入预期安全影响（Expected Safety Impact, ESI）指标，结合可微分裁判模型估计安全梯度，并据此实施仅更新或仅冻结关键参数的干预策略。该框架在参数定位精度上优于传统剪枝指标，但在效用保持上仍受限于冻结比例，其泛化边界尚待验证。

## 研究背景

当模型经历少量良性微调后，其拒绝有害请求的能力显著下降，这一现象被称为安全对齐脆弱性。该问题的根源在于安全行为并非均匀分布于所有参数中，而是编码在特定的低维子空间内。若微调过程无差别地更新所有权重，这些关键参数将发生漂移，导致安全边界崩塌。然而，直接识别这些参数面临两大障碍：一是安全评分函数依赖于离散Token生成，不可微；二是不同模块的参数分布异质性被传统敏感度指标忽略。

现有研究路线主要分为两类：一类基于激活空间分析，如Activation Diffing通过对比微调前后激活差异定位安全方向，但该方法依赖大规模样本平均且难以直接指导参数更新；另一类基于参数剪枝指标，如SNIP和Wanda利用静态权重幅值或梯度范数估计重要性，但这些方法隐含假设参数变化是均匀或正比于静态幅值的，忽略了不同层间统计分布的差异。此外，多数方法需要对比对齐与未对齐模型，无法在单一模型内完成诊断。本文的切入点在于构建一个单模型内可计算的、考虑参数统计分布的安全敏感度指标，从而实现对安全关键参数的精确隔离与最小化干预。

## 核心方法

### 参数敏感度度量参照系

传统参数重要性评估通常采用 $| \nabla_{\theta_i} L(\theta) |$ 或 $| \theta_i \nabla_{\theta_i} L(\theta) |$ 作为指标，其中 $L(\theta)$ 为通用损失函数（如交叉熵）。这些方法将参数变化 $\Delta \theta_i$ 假设为常数或正比于静态权重幅值 $|\theta_i|$。本文的关键差异在于，将目标函数替换为预期安全值 $S(\theta)$，并用参数标准差 $\sigma(\theta_i)$ 替代静态幅值作为变化尺度的代理，以反映微调过程中参数的实际波动特性。

### 预期安全影响（ESI）指标构建

设计动机在于解决传统指标忽略参数分布异质性的问题。本文定义预期安全值 $S(\theta)$ 为有害输入分布下响应安全评分的期望：

$$ S(\theta) = \mathbb{E}_{x \sim D_{harm}} \mathbb{E}_{y \sim p_\theta(\cdot|x)} [s(y)] $$

其中 $s(y)$ 为裁判模型 $J$ 输出的安全概率。基于一阶泰勒展开，参数 $\theta_i$ 的安全影响近似为 $\Delta S \approx \nabla_{\theta_i} S(\theta) \cdot \Delta \theta_i$。为估计 $\Delta \theta_i$，本文采用参数标准差 $\sigma(\theta_i)$ 作为统计代理，定义ESI指标为：

$$ ESI(\theta_i) \equiv | \sigma(\theta_i) \nabla_{\theta_i} S(\theta) | $$

该公式的物理含义是：参数对安全值的梯度越大，且该参数在微调中越容易波动（标准差大），则其对安全崩塌的贡献越大。为解决离散Token不可微问题，本文引入Gumbel-Softmax松弛，将离散Token向量 $\tilde{y}$ 近似为连续向量，并通过投影矩阵 $M$ 桥接目标模型与裁判模型的词表空间，实现端到端梯度计算。

### 双范式干预策略

基于ESI排序，本文提出两种干预范式。对于未对齐模型，实施安全增强调优（Safety Enhancement Tuning, SET），仅更新ESI排名Top-k%的安全关键参数，冻结其余参数以保留预训练知识。对于已对齐模型，实施安全保持适应（Safety Preserving Adaptation, SPA），冻结Top-k%安全关键参数，仅更新非关键参数以适应下游任务。这一设计实现了安全与效用的细粒度解耦：SET通过最小化更新范围快速提升安全，SPA通过隔离安全子空间防止微调干扰。

## 实验评估

实验在Qwen2.5-7B/14B-base、Llama3-8B-base及Llama3-8B/70B-it、Qwen3-30B-A3B-it（MoE）上进行，使用HarmBench和WildJailbreak评估攻击成功率（ASR），GSM8K和AGNews评估效用。基线包括Random、LoRA、SafeLoRA、SN-tune及多种剪枝指标（SN、GMT、Wanda、SNIP）。

| 模型 | 方法 | HarmBench ASR (%) | WildJailbreak ASR (%) |
| :--- | :--- | :--- | :--- |
| Llama3-8B-it | Base | 15.3 | 16.3 |
| Llama3-8B-it | ESI (1%) | 59.1 | 49.3 |
| Llama3-8B-it | SNIP (1%) | 37.6 | 46.2 |
| Llama3-8B-it | Random (1%) | 15.6 | 16.5 |
| Qwen2.5-14B-base | Base | 55.1 | 67.6 |
| Qwen2.5-14B-base | ESI (1%) | 78.5 | 85.6 |
| Qwen2.5-14B-base | SNIP (1%) | 56.0 | 68.8 |
| Qwen2.5-14B-base | Random (1%) | 55.1 | 67.8 |

ESI在扰动实验中表现显著优于其他指标。在Llama3-8B-it上，仅扰动1%的ESI参数使HarmBench ASR从15.3%升至59.1%，而SNIP仅升至37.6%，Random几乎无变化。这表明ESI能更精准地定位安全关键参数。在SET实验中，Llama3-8B在R1-Safety上训练后，WildJailbreak ASR从62.5%降至19.1%，优于SafeLoRA的37.4%。在SPA实验中，Llama3-8B-it在AGNews上达到90.5%准确率，GSM8K达到78.0%，同时HarmBench ASR仅增加0.8%，而Random选择导致ASR增加10.4%。

消融实验显示，参数选择比例k对结果影响显著。当k从1%增至10%时，Random基线的ASR急剧上升，而SPA保持平稳，证明冻结比例需精确控制。MoE模型中，安全关键参数从中间层Value矩阵转移至后层MLP专家，表明架构差异导致安全编码位置不同。

评估边界方面，论文未报告置信区间，且SPA在GSM8K上的78.0%低于领域SOTA的87.40%，可能因冻结参数过多限制效用。代码已开源，但Gumbel-Softmax温度 $\tau$ 的敏感性未充分讨论。

## 关联研究分析

从方法设计看，本文与SafeLoRA同属参数约束路线，但SafeLoRA仅约束LoRA适配器权重，而本文扩展至全参数空间。SafeLoRA依赖预定义的安全子空间投影，本文则通过ESI动态识别关键参数，避免了预定义子空间的局限性。然而，SafeLoRA在LoRA场景下计算开销更低，本文的全参数ESI计算需遍历所有参数，成本更高。这一差异源于任务特性：SafeLoRA适用于参数高效微调，本文适用于全参数微调或基础模型对齐。

从问题动机看，本文与Activation Diffing均试图定位安全相关结构，但前者在激活空间，后者在参数空间。Activation Diffing通过对比微调前后激活差异识别安全方向，但难以直接指导参数更新，且依赖大规模样本平均。本文的ESI指标直接输出参数重要性排序，可即时用于冻结或更新决策。差异根源在于可微性处理：Activation Diffing依赖线性探针，本文通过Gumbel-Softmax实现端到端可微，但引入了近似误差。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

本文要解决的核心矛盾是微调过程中安全与效用的几何冲突，现有方法因无法精确定位安全关键参数而陷入全局冻结或盲目更新的困境。本文抓住参数统计分布异质性这一被忽略的点，通过ESI指标结合可微分裁判模型，实现了单模型内的安全关键参数识别。实验证明，仅扰动1%的ESI参数即可导致显著安全崩塌，SET在100次迭代内将WildJailbreak ASR降低50%以上，SPA在1000次微调中将安全退化限制在1%以内。本文的边界在于SPA的效用保持仍低于SOTA，且Gumbel-Softmax近似的偏差未量化。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_bebdba993896)