# HuggingFace最新推荐论文 ｜Think-Then-Generate: Reasoning-Aware Text-to-Image Diffusion with LLM Encoders ｜思考-生成范式：基于LLM推理的文本到图像扩散模型

研究机构：上海交通大学、快手

作者：Siqi Kou、Jiachun Jin、Zetong Zhou 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.10332)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.10332)

> 文本到图像（Text-to-Image, T2I）扩散模型长期受限于“文本-像素映射器”的静态编码机制，无法处理需要世界知识推理的概念性指令。现有后训练方法仅优化扩散骨干，忽略了大语言模型（Large Language Model, LLM）编码器中蕴含的推理潜力。本文提出T2G范式，通过监督微调激活LLM的思维链（Chain-of-Thought, CoT）重写能力，并利用双组相对策略优化（Dual-GRPO）联合优化LLM与扩散Transformer（Diffusion Transformer, DiT），使模型在推理密集型基准上超越闭源SOTA，但其对推理预算的敏感性仍存疑。

## 研究背景

当T2I模型面对“解释如何解方程”或“描绘节日庆祝”等概念性指令时，传统架构将LLM仅作为冻结的特征提取器，导致模型只能执行字面描述而无法进行逻辑推断。这种局限源于扩散模型训练于描述性图文对，其文本编码器缺乏将抽象概念转化为具体视觉属性的推理路径。为突破此瓶颈，研究者引入强化学习（Reinforcement Learning, RL）对齐人类偏好，但主流方法如Flow-GRPO仅优化扩散过程，将LLM视为静态条件输入，未能利用其世界知识解决语义鸿沟。

T2I领域的核心矛盾在于计算效率、生成保真度与复杂语义逻辑一致性之间的平衡。早期潜在扩散模型（Latent Diffusion Model, LDM）解决了算力问题，扩散Transformer（DiT）解决了规模扩展性，但语义对齐仍依赖浅层文本-图像关联。2024-2025年，直接偏好优化（Direct Preference Optimization, DPO）与RLHF成为主流，然而这些方法多聚焦于美学或简单语义对齐，对需要多步推理的长提示遵循能力不足。本文切入点在于将LLM从被动编码器转变为主动推理代理，通过端到端联合优化弥合推理与渲染之间的断层。

## 核心方法

### 方法参照系

标准T2I后训练流程通常冻结LLM编码器，仅通过奖励模型优化DiT解码器。本文的关键差异在于将LLM与DiT视为复合策略模型，通过图像奖励信号同时更新两者参数，打破编码器冻结的工程惯例，实现推理过程与视觉生成的闭环对齐。

### 推理感知行为激活

设计动机在于解决LLM在缺乏视觉反馈时生成的推理轨迹与DiT渲染能力不匹配的问题。传统监督微调（Supervised Fine-Tuning, SFT）仅优化文本生成，无法保证重写后的提示词能被DiT正确解析。本文构建包含原始提示、CoT推理及重写提示的数据集，对Qwen2.5-VL进行SFT。t-SNE可视化显示，SFT后嵌入分布与预训练模型高度重叠，表明该过程保留了嵌入空间结构，维持了DiT的兼容性。这一设计确保了LLM在获得推理能力的同时，不破坏其作为条件编码器的基础功能，为后续强化学习提供了稳定的初始策略。

### Dual-GRPO联合优化

设计动机在于解决单一组件优化导致的语义-视觉错位，即LLM生成的语义丰富提示可能超出DiT的渲染能力，或DiT的视觉偏好未反馈至LLM的推理过程。本文提出Dual-GRPO，将复合模型参数化为 $\theta = \{\phi, \lambda\}$，其中 $\phi$ 为LLM参数，$\lambda$ 为DiT参数。对于给定提示 $q$，采样 $J$ 个推理序列 $\mathbf{z}_j$ 和 $K$ 个图像 $\mathbf{x}_{j,k}$，构建层级采样树。LLM的损失项 $L_t(\phi)$ 基于组内相对优势 $A_{\hat{j},t}$ 计算，该优势由同一推理输出下所有 $K$ 个图像的语义一致性奖励 $R_{sem}$ 聚合而成：

$$ A_{\hat{j},t} = \frac{1}{K} \sum_{k=1}^{K} R_{sem}(\mathbf{x}_{j,k}) - \text{mean}(\{R_{sem}(\mathbf{x}_{j',k})\}_{j'=1}^{J}) $$

DiT的损失项 $L_t(\lambda)$ 采用Flow-GRPO形式，奖励函数为美学 $R_{aes}$、物理一致性 $R_{con}$ 与语义一致性 $R_{sem}$ 的加权和。这种分层奖励机制使LLM专注于语义对齐，DiT专注于视觉质量，通过PPO裁剪与KL正则化实现稳定更新。

## 实验评估

实验在WISE和T2I-ReasonBench基准上进行，覆盖文化常识、时空理解及科学推理等维度。基线包括FLUX.1-dev、Stable Diffusion 3.5、Bagel、Janus-Pro-7B及GPT-4o、Gemini-2.0等闭源模型。本文方法在WISE上取得0.79分，较预训练Qwen-Image提升30%，接近GPT-4o的0.81分；在T2I-ReasonBench上达到92.2分，超越Gemini-2.0的84.4分。

| 模型 | 类型 | WISE Overall | T2I-ReasonBench Acc. |
| :--- | :--- | :--- | :--- |
| Qwen-Image | diffusion | 0.61 | 57.1 |
| GPT-4o | proprietary | 0.81 | 77.5 |
| Gemini-2.0 | proprietary | 0.75 | 84.4 |
| Ours | diffusion | 0.79 | 68.3 |

消融实验显示，SFT将WISE分数从0.65提升至0.74，Dual-GRPO进一步提升至0.79。T2I-ReasonBench准确率从60.9提升至68.3。这表明SFT激活了推理模式，而Dual-GRPO通过图像奖励修正了推理与渲染的偏差。值得注意的是，仅添加CoT提示而未进行SFT的零样本性能仅从0.61提升至0.65，证明缺乏任务特定监督信号的推理过程无法有效对齐视觉生成需求。

评估边界方面，论文未报告置信区间，且WISE基准仅包含1000个提示，样本量有限。代码已开源，但Dual-GRPO的超参数（如 $J, K$ 值）对性能的影响未详细分析。可复现性受限于Qwen-Image基座的特定版本，其他架构的迁移效果未知。

## 关联研究分析

从问题动机看，T2I-R1与Uni-CoT同样引入CoT推理，但前者采用双层CoT独立优化高层规划与低层生成，后者在单一多模态模型内执行宏观与微观推理。本文差异在于明确解耦LLM推理与DiT渲染，通过Dual-GRPO实现跨模态奖励传递。T2I-R1的独立优化可能导致推理轨迹与渲染能力脱节，而本文的联合优化确保了推理结果的可渲染性。这种差异源于任务特性：概念性生成需要推理与视觉的紧密耦合，而非简单的模块堆叠。

从方法设计看，Flow-GRPO仅优化扩散骨干，将LLM视为静态条件，限制了其在知识密集型任务上的表现。本文通过扩展GRPO至复合策略，解决了编码器冻结导致的语义上限问题。然而，Flow-GRPO的SDE转换机制被保留用于DiT部分，表明本文并未改变扩散过程的随机性本质，而是改变了优化对象。这种设计选择暗示，推理增强并非必须依赖统一架构，模块化联合优化同样有效。但联合优化是否导致LLM通用推理能力退化，论文未提供通用NLP基准的对比数据。

## 总结

本文核心矛盾在于T2I模型缺乏将抽象概念转化为具体视觉属性的推理能力，现有方法因冻结LLM编码器而受限于浅层语义对齐。本文抓住LLM世界知识未被利用的切入点，通过SFT激活CoT重写模式，并利用Dual-GRPO联合优化LLM与DiT，使模型在WISE上达到0.79分，在T2I-ReasonBench上达到92.2分。其边界在于实验仅验证了特定基座（Qwen-Image）上的效果，且未分析推理预算对生成质量的边际效应。当推理步数增加时，Dual-GRPO的收敛速度是否显著下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.10332)