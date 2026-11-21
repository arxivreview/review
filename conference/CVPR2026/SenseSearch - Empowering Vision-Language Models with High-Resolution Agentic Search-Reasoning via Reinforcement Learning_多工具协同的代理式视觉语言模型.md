# CVPR2026最新论文 ｜SenseSearch: Empowering Vision-Language Models with High-Resolution Agentic Search-Reasoning via Reinforcement Learning ｜多工具协同的代理式视觉语言模型

作者：Yong Xien Chng、Tao Hu、Wenwen Tong 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3b6348eb5dff)

> 视觉语言模型（Vision-Language Models, VLMs）在处理高分辨率图像与长尾知识任务时，受限于静态参数与全局编码的带宽瓶颈，难以兼顾细粒度感知与实时事实检索。现有方法通常将图像裁剪与文本搜索割裂为独立模块，无法在单一推理链中动态协调多工具以解决复合任务。本文提出 SenseSearch，通过强化学习（Reinforcement Learning, RL）统一调度图像搜索、文本搜索与图像裁剪工具，并设计 BN-GSPO 算法稳定多工具轨迹的训练。该框架在搜索导向基准上取得领先，但依赖外部 API 的架构使其在离线部署与纯感知任务上的泛化能力存疑。

## 研究背景

当 VLM 面对包含微小 Logo 的赛车服图像并询问公司成立年份时，模型首先需通过图像裁剪定位 Logo，再经文本搜索获取成立年份，最后结合图像搜索识别车手出生年份进行计算。这一过程揭示了静态 VLM 的两重困境：一是高分辨率图像经全局编码后高频空间细节丢失，导致细粒度感知失效；二是预训练语料的静态性无法覆盖长尾知识与实时信息，迫使模型依赖语言先验而非视觉证据。解决此类问题需引入外部工具交互，但工具调用的时机与组合策略本身构成复杂的序贯决策问题。

早期研究将工具调用视为固定工作流，如检索增强生成（Retrieval-Augmented Generation, RAG）依赖静态文档库，或单一工具模型仅支持裁剪或搜索。MMSearch-R1 整合了图像与文本搜索，但缺乏对高分辨率局部区域的精细分析能力；DeepEyes 等“Thinking with Images”范式通过 RL 激励模型使用裁剪工具，却未解决外部知识获取问题。现有方法的核心瓶颈在于工具间的协同缺失：搜索获取的宏观信息无法直接指导裁剪的微观定位，而裁剪得到的局部特征又缺乏上下文语义支撑。本文切入点在于构建一个端到端的代理式框架，使模型在推理过程中自适应决定何时调用何种工具，从而在单一轨迹内完成“感知-检索-推理”的闭环。

## 核心方法

### 多工具交互形式化

本文基于 MMSearch-R1 的问题设定，扩展动作空间以包含图像裁剪工具。任务定义为给定查询 $q$ 与初始图像 $I_0$，模型在 $T$ 轮内通过生成推理步骤并选择动作（文本搜索、图像搜索、图像裁剪或输出答案）来迭代更新观察历史 $\mathcal{T}_t$。与单一工具方法不同，该框架要求模型在每一轮同时输出推理轨迹与一个有效工具调用，若缺失任一要素则轨迹无效。这种形式化将工具调用从固定流程转化为策略学习问题，使模型能够根据当前信息缺口动态规划后续操作。

### 冷启动监督微调

纯 RL 训练在多轮交互中易陷入“学习陷阱”，即模型因奖励稀疏而忽略新生成的视觉工具。为建立基础工具使用模式，本文引入冷启动阶段，在约 3,000 个精心筛选的多轮交互轨迹数据集 $\mathcal{D}_{\text{SFT}}$ 上进行监督微调（Supervised Fine-Tuning, SFT）。该阶段的目标函数为最大化目标轨迹的对数似然：

$$
\mathcal{L}_{\text{SFT}} = - \sum_{(x_i, y_i) \in \mathcal{D}_{\text{SFT}}} \log \pi_{\theta}(y_i \mid x_i)
$$

其中 $\pi_{\theta}$ 为模型参数。这一设计动机在于，小样本 SFT 为 RL 阶段提供了稳定的初始策略，避免模型在探索初期因格式错误或工具调用失败而获得负奖励，从而加速后续强化学习收敛。

### BN-GSPO 强化学习算法

标准 GSPO 算法对多工具轨迹中奖励尺度与长度差异敏感，导致训练不稳定。本文提出批归一化组序列策略优化（Batch-Normalized Group Sequence Policy Optimization, BN-GSPO），在组内归一化优势的基础上引入批归一化，以平衡不同难度与长度轨迹的学习信号。其序列级优化目标为：

$$
\mathcal{L}_{\text{RL}} = \mathbb{E}_{x_b, \{y_{b,g}\}} \Bigg[ \frac{1}{G} \sum_{g=1}^{G} \min (s_{b,g}(\theta )\tilde {A}_{b,g}, \mathrm {clip}_{\epsilon _{\mathrm {low}}}^{\epsilon _{\mathrm {high}}}(s_{b,g}(\theta ))\tilde {A}_{b,g}) \Bigg] - \beta \, D_{\mathrm {KL}}(\pi _{\theta }\,\|\,\pi _{\text {ref}})
$$

其中 $\tilde{A}_{b,g}$ 为经批归一化后的优势估计，$s_{b,g}(\theta)$ 为策略比率，$\pi_{\text{ref}}$ 为冻结参考策略。奖励函数 $R(\tau) = R_{\text{acc}}(\tau) + R_{\text{format}}(\tau)$ 结合 LLM-as-a-judge 评估的答案准确性与严格遵循 JSON 格式及标签协议的格式合规性。BN-GSPO 通过归一化消除不同工具调用轨迹间的奖励量级偏差，使模型能够稳定学习复杂的多工具协同策略。

## 实验评估

实验在 HR-MMSearch、MMSearch 及 HRBench-4K 等基准上进行，基线涵盖 MMSearch-R1、DeepEyes 及 Pixel-Reasoner。本文未提供可逐字定位的完整实验数值表格，故不进行表格呈现。据论文摘要，SenseSearch 在 HR-MMSearch 上比基线高出 19.18%，在 MMSearch 上取得 59.06 分，在 HRBench-4K 上达到 73.6 分，超过 DeepEyes 与 Pixel-Reasoner。这些结果表明，多工具协同在“高分辨率+知识密集”复合任务上具有显著优势，但 HRBench-4K 的 73.6 分低于领域综述中 Visual Rationale Learning 的 88.9 分，暗示搜索引入的延迟或错误传播可能在纯感知任务上抵消了裁剪收益。

消融实验未详细报告，但冷启动 SFT 的必要性通过对比纯 RL 训练的“学习陷阱”现象间接验证。设计决策中，3,000 样本的冷启动数据集规模极小，其是否足以覆盖复杂工具组合的泛化需求，论文未给出量化分析。BN-GSPO 相比标准 GSPO 的性能增益主要体现为训练稳定性，具体数值差异未在摘要中披露。

评估边界方面，HR-MMSearch 为本文新建基准，缺乏外部参照系，其难度分布与真实世界任务的匹配度未知。代码已开源，但外部 API 调用的延迟与成本未量化，限制了工程部署的可行性评估。

## 关联研究分析

从问题动机看，SenseSearch 与 DeepEyes 均旨在解决高分辨率图像的细粒度感知，但 DeepEyes 局限于像素空间操作，无法获取外部知识；而 MMSearch-R1 虽支持搜索，却缺乏局部放大能力。本文的差异在于将两类工具统一于单一 RL 框架，根源在于任务特性要求“感知”与“知识”的即时交互，而非独立处理。然而，这种统一是否导致模型在纯感知任务上因搜索干扰而性能下降，论文未通过控制变量实验验证。

从方法设计看，SenseSearch 的冷启动 SFT 与 Pixel Reasoner 的两阶段法相似，但 Pixel Reasoner 采用好奇心驱动 RL 探索像素空间，而本文使用 SFT 建立基础模式。这一差异源于本文工具集包含文本搜索，其格式约束更强，SFT 能更直接地规范输出结构。但 SFT 阶段是否限制了模型在 RL 阶段的探索多样性，从而影响最终性能上限，论文未给出回答。

## 总结

SenseSearch 旨在解决 VLM 在高分辨率与知识密集任务中感知与知识获取割裂的矛盾，通过 RL 统一调度多工具实现动态协同。其核心贡献在于 BN-GSPO 算法稳定了多工具轨迹的训练，并在 HR-MMSearch 上取得 19.18% 的提升。然而，该框架依赖外部 API，在 HRBench-4K 纯感知任务上未超越专用潜在推理模型，暴露了外部工具在离线场景与纯视觉任务中的局限。当移除搜索工具仅保留裁剪时，模型在知识密集任务上的性能衰减幅度是否显著高于纯感知任务，论文未提供对比数据。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_3b6348eb5dff)