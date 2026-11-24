# ICLR2026最新论文 ｜_NextQuill_ : CAUSAL PREFERENCE MODELING FOR ENHANCING LLM PERSONALIZATION ｜因果偏好建模

研究机构：香港中文大学、中国科学技术大学

作者：Xiaoyan Zhao、Juntao Jun、Yang Zhang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_79357001)

> 大语言模型个性化面临的核心矛盾是通用对齐与个体偏好的结构性冲突，现有微调方法往往将上下文噪声与真实偏好混同，导致对齐质量受限。本文切入点在于利用因果推断区分模型预测与真实响应中由用户历史驱动的成分，提出双侧重因果偏好建模框架。通过定义模型侧与数据侧的因果效应，NextQuill 仅对偏好驱动部分进行加权对齐。该方法在受控 SFT 对比中显著提升了生成质量，但其因果效应的静态估计假设在动态偏好场景下的有效性存疑。

## 研究背景

当 LLM 接收用户查询时，其生成过程受用户历史 $H$ 与上下文 $X$ 共同影响。传统微调将模型对所有 token 的预测统一拟合至真实响应，忽略了 $X$ 独立于 $H$ 产生的非偏好成分。这种“一刀切”的拟合导致模型难以区分哪些预测真正反映了用户偏好，哪些仅是任务上下文的通用响应。为隔离偏好信号，需引入因果效应估计，即量化 $H$ 对预测结果的独立贡献，从而将个性化对齐从全量拟合转向针对性优化。

LLM 个性化旨在使模型输出适配特定用户风格，早期研究依赖检索增强生成（RAG）注入历史上下文，但受限于静态偏好假设与事实性幻觉。随着参数高效微调（PEFT）的引入，研究者试图通过轻量级适配器编码用户偏好，但现有方法如 ContextSFT 仍将所有预测视为偏好信号，未区分上下文驱动与历史驱动的成分。这种浅层建模导致对齐过程被非偏好噪声稀释，限制了个性化深度。NextQuill 针对这一瓶颈，从因果视角重新定义偏好信号，通过分离模型内部偏好与数据侧偏好归因，实现更精准的参数更新。

## 核心方法

### 方法参照系

本文问题归属于参数高效适配路线，标准流程为使用用户历史数据微调 LLM 以适配个体偏好。与通用 SFT 的关键差异在于，本文不直接拟合所有预测与真实响应的差异，而是先通过因果图识别偏好驱动成分，再仅对这些成分进行对齐，从而避免上下文噪声干扰。

### 模型侧因果偏好效应

在标准 SFT 中，损失函数均匀计算所有 token 的预测误差，导致模型同时拟合上下文通用响应与用户特定偏好。NextQuill 在训练阶段引入模型侧因果偏好效应（Model-side Causal Preference Effect, MCE），通过干预用户历史 $H$ 来隔离偏好驱动成分。具体而言，MCE 定义为将 $H$ 设置为特定值 $h$ 与设置为空值 $\emptyset$ 时，模型对第 $t$ 个 token 预测概率之差：

$$
\text{MCE}(\hat{Y}_t | h, x) = P(\hat{Y}_t | H=\text{do}(h), x) - P(\hat{Y}_t | H=\text{do}(\emptyset), x)
$$

该公式的物理含义是量化用户历史对当前预测的独立贡献，排除了上下文 $X$ 的干扰。通过仅对齐 MCE 而非全量预测，模型得以聚焦于真正由用户偏好驱动的内部表征，解决了传统方法中偏好信号被上下文噪声稀释的问题。

### 数据侧因果偏好归因

模型侧 MCE 解决了“模型学到了什么偏好”的问题，但训练目标仍需明确“哪些真实响应 token 代表偏好”。NextQuill 引入数据侧因果偏好效应（Data-side Causal Preference Effect, DCE），量化用户特征 $U$ 对真实响应 token $y_t$ 生成的驱动程度。DCE 通过比较包含用户历史 $h$ 与不包含 $h$ 时，模型对 $y_t$ 的预测概率差异来估计：

$$
\omega_t = \begin{cases} \lambda & \text{if } \text{DCE}(Y_t=y_t | u, x) > \delta \\ \epsilon & \text{otherwise} \end{cases}
$$

其中 $\omega_t$ 为 token 权重，$\lambda$ 和 $\epsilon$ 为预设权重，$\delta$ 为阈值。该设计动机在于真实响应中部分 token（如固定句式）由上下文决定，而非用户偏好。通过 DCE 识别偏好驱动 token 并赋予更高权重 $\lambda$，训练过程得以聚焦于最具个性化价值的监督信号，避免了非偏好 token 对梯度更新的干扰。

## 实验评估

实验在 Amazon Reviews（Book/Movie/CD）与 Topic Writing 数据集上进行，基线覆盖 Base Model、RAG（Contriever, LatestK, LLM-TRSR, CoS）与 PEFT（SFT, ContextSFT, OPPU）。NextQuill 在 Book Review 上 ROUGE-1 达 0.2318，显著优于 ContextSFT 的 0.1661 与 OPPU 的 0.1502，表明因果对齐机制在生成质量上具有优势。

| 数据集 | 方法 | ROUGE-1 | ROUGE-L | BERTScore |
|---|---|---|---|---|
| Book Review | ContextSFT | 0.1661 | 0.0836 | 0.8013 |
| Book Review | NextQuill | 0.2318 | 0.1270 | 0.8182 |
| Movie Review | ContextSFT | 0.1573 | 0.0753 | 0.7943 |
| Movie Review | NextQuill | 0.2015 | 0.1041 | 0.8064 |

消融实验显示，仅使用模型侧 MCE（MCEOnly）在 Book Review 上 ROUGE-1 为 0.1827，较 Base Model 提升 142.9%；加入数据侧 DCE 对齐后（Full NextQuill）提升至 0.2318，相对提升达 208.2%。这表明数据侧 token 归因对性能提升贡献显著，验证了区分偏好驱动 token 的必要性。

评估指标涵盖 ROUGE、METEOR、BLEU、BERTScore 及 LLM-as-a-judge，但缺乏对事实性幻觉的独立量化。代码已开源，但论文未报告训练超参数细节与计算开销，且未对比 LoRA、PerFit 等最新 PEFT 变体，限制了与领域 SOTA 的直接横向比较。

## 关联研究分析

从方法设计看，NextQuill 与 SteerX 均利用因果推断解耦偏好，但 SteerX 在推理时通过因果信号引导生成，而 NextQuill 在训练时通过因果效应加权损失。这一差异源于任务目标不同：SteerX 旨在黑盒场景下的即时适配，而 NextQuill 追求参数化持久适配。NextQuill 的静态因果估计假设偏好结构稳定，这在长程动态交互中可能失效，而 SteerX 的推理时机制天然具备动态适应性，但牺牲了长期一致性。

从问题动机看，NextQuill 与 ContextSFT 同属 SFT 改进路线，但 ContextSFT 直接拟合全量预测，而 NextQuill 通过 MCE 隔离偏好成分。这一改进解决了 ContextSFT 中上下文噪声干扰偏好学习的问题，但 NextQuill 的 DCE 估计依赖参考模型，其近似误差可能影响归因精度。相比之下，OPPU 通过每用户独立适配器实现上界性能，但计算成本高昂，NextQuill 在保持单模型架构的同时接近 OPPU 效果，体现了计算效率与个性化深度的平衡。

## 总结

NextQuill 针对 LLM 个性化中偏好信号被上下文噪声稀释的核心矛盾，通过因果推断区分模型侧与数据侧的偏好驱动成分，提出双重重因果对齐框架。该方法在 Book Review 上 ROUGE-1 达 0.2318，较 ContextSFT 提升 39.6%，验证了因果对齐的有效性。然而，其 DCE 估计依赖静态参考模型，未显式建模偏好随时间的动态演化，且缺乏与最新 PEFT 变体的对比。当用户偏好发生显著漂移时，静态因果图结构是否仍能准确归因偏好成分，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_79357001)